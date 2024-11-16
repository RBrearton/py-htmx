"""Defines some markdown rendering utilities."""

from collections.abc import Callable

import markdown2 as md
from bs4 import BeautifulSoup

from . import models as ui

# These are all of the extras that we opt into by default. To see all the available
# options, read the wiki: https://github.com/trentm/python-markdown2/wiki
default_extras = [
    "latex",
    "admonitions",
    "fenced-code-blocks",
    "tables",
    "footnotes",
    "code-friendly",
    "cuddled-lists",
    "metadata",
    "task_list",
    "strike",
    "header-ids",
]


def render_markdown(
    markdown: str,
    extras: list[str] | None = None,
    pre_processors: list[Callable[[str], str]] | None = None,
    post_processors: list[Callable[[str], str]] | None = None,
) -> str:
    """Render the markdown string to HTML.

    Args:
        markdown: The markdown string to render.
        extras: A list of markdown2 extras to enable. By default, all the major extras
            are enabled, so latex can be rendered, code blocks will work, etc.
        pre_processors: Functions that take the markdown string and return another
            markdown string. This can be used to do things like inject html before the
            first pass of the python markdown2 renderer.
        post_processors: Functions that take the rendered HTML and return post-processed
            HTML. This can be used to add classes or other attributes to the HTML, for
            example.
    """
    # Set the default extras, if required.
    if extras is None:
        extras = default_extras

    # Run pre processing, if required.
    if pre_processors:
        for pre_processor in pre_processors:
            markdown = pre_processor(markdown)

    # Render the markdown to HTML.
    html = md.markdown(markdown, extras=extras)

    # Run post processing, if required.
    if post_processors:
        for post_processor in post_processors:
            html = post_processor(html)

    return html


def render_admonitions(markdown: str) -> str:
    """Inject html to render admonitions wherever indicated in the markdown.

    This is a pre-processor.
    """
    # Admonitions start with a "!START_ADMONITION <admonition_type> <optional_title>"
    # line and end with an "!END_ADMONITION" line.
    # We'll replace these with the appropriate html.
    output_lines = []
    for line in markdown.split("\n"):
        if line.startswith("!START_ADMONITION"):
            # Get the admonition type and title.
            _, admonition_type, title = line.split(" ", 2)
            output_lines.append(
                f'<div class="collapse collapse-arrow bg-{admonition_type} bg-opacity-20 my-4 border-2 border-{admonition_type} transition-none"><input type="checkbox" /><div class="collapse-title font-semibold text-primary-content">{title}</div><div class="collapse-content bg-base-200 rounded-box">'  # noqa: E501
            )
        elif line == "!END_ADMONITION":
            output_lines.append("</div></div>")
        else:
            output_lines.append(line)

    return "\n".join(output_lines)


def render_dropdown_refs(markdown: str) -> str:
    """Inject html to add dropdown references wherever indicated in the markdown.

    We allow users to define references using latex-inspired syntax, like so:

    !START_LABEL <label_name>
    This is the content that the label refers to...
    !END_LABEL

    Then, we want to make it possible for a py-htmx user to refer to this label in a
    bunch of different ways. One way is to make it so that, when you hover over an
    element, a dropdown appears showing the content of the label.

    Specifically, the syntax should look like:

    !DROPDOWN_REF "<label_name>" "<hover_text>"
    """
    # Start by finding all the labels in the markdown.
    label_lines: dict[str, list[str]] = {}
    current_label_name: str | None = None
    for line in markdown.split("\n"):
        if line.startswith("!START_LABEL"):
            _, label_name = line.split(" ", 1)
            label_lines[label_name] = []
            current_label_name = label_name
        elif line.startswith("!END_LABEL"):
            current_label_name = None
        elif current_label_name is not None:
            label_lines[current_label_name].append(line)

    # Join the lines of each label together.
    labels = {label_name: "\n".join(lines) for label_name, lines in label_lines.items()}

    # We want the dropdown-hover content to be a card, which basically lets us hand over
    # more of the styling to DaisyUI.
    output_lines = []
    for line in markdown.split("\n"):
        if line.startswith("!DROPDOWN_REF"):
            # Grab the label name and the hover text. Due to some syntax details, we
            # will end up with a trailing " on each of these strings. There could also
            # be some leading or trailing whitespace, so strip to be sure.
            _, label_name, hover_text = line.split(' "', 2)
            label_name = label_name.rstrip('"').strip()
            hover_text = hover_text.rstrip('"').strip()

            # Figure out what should go in the card.
            card_content = labels[label_name]

            # Start by building the card div.
            card_text = ui.Paragraph(text=card_content)
            card_title = ui.Heading(
                level=4, cls="card-title justify-center", text=label_name
            )
            card_body = ui.Div(cls="card-body", children=[card_title, card_text])
            card = ui.Div(
                cls="dropdown-content card bg-base-300 text-primary-content shadow z-10",  # noqa: E501
                children=[card_body],
            )

            # Now make the dropdown-hover.
            hover_text_div = ui.Div(
                tab_index=1,
                role="button",
                children=[ui.Code(text=hover_text)],
            )
            dropdown_hover = ui.Div(
                cls="dropdown dropdown-hover",
                children=[hover_text_div, card],
            )

            # Render the dropdown hover to html, and put it back in the output.
            output_lines.append(dropdown_hover.model_dump_html())
        else:
            output_lines.append(line)

    # Rebuild the document and return it.
    return "\n".join(output_lines)


def pre_process_remove_labels(markdown: str) -> str:
    """Remove all !START_LABEL and !END_LABEL lines from the markdown.

    This pre-processor should be applied last, as other pre-processors may depend on
    these labels.
    """
    output_lines = []
    for line in markdown.split("\n"):
        if line.startswith(("!START_LABEL", "!END_LABEL")):
            continue
        output_lines.append(line)

    return "\n".join(output_lines)


def post_process_dropdowns(html: str) -> str:
    """Improve the formatting of dropdowns in paragraphs.

    When we render our markdown, a lot of hover dropdowns will appear in the middle of
    paragraphs. Because the </p> normally leads to a line break, when we insert a <div>
    in the middle of a paragraph, we often end up with a line break in the middle of a
    sentence.

    The way to get around this is to find all the <p> elements that surround one of our
    dropdown-hover elements, and change them to <span> elements, which are the same as
    <p> elements, but without the line break.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Find all the divs that are our dropdown hover references.
    for div in soup.find_all("div", class_="dropdown dropdown-hover"):
        # Help with the type hinting.
        div: BeautifulSoup

        # If the previous sibling is a <p> tag, we should change it to a <span> tag to
        # avoid the line break.
        previous_sibling = div.find_previous_sibling()
        if previous_sibling is not None and previous_sibling.name == "p":
            previous_sibling.name = "span"

        # If the next sibling is a <p> tag, we should change it to a <span> tag to avoid
        # the line break.
        next_sibling = div.find_next_sibling()
        if next_sibling is not None and next_sibling.name == "p":
            next_sibling.name = "span"

    return str(soup)


def post_process_math(html: str) -> str:
    """Increase the spacing around block math elements, and math font size.

    This is a post-processor, and won't work before the latex is rendered to MathML.
    """
    html = html.replace("<math", '<math style="font-size: 1.2em;"')
    return html.replace('display="block"', 'display="block" class="my-6"')

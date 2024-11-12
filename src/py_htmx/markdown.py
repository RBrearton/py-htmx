"""Defines some markdown rendering utilities."""

from collections.abc import Callable

import markdown2 as md

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
                f'<div class="collapse collapse-arrow bg-{admonition_type} bg-opacity-20 my-4 border-2 border-{admonition_type} transition-none"><input type="checkbox" /><div class="collapse-title font-semibold text-primary-content">{title}</div><div class="collapse-content bg-base-200"><p>'  # noqa: E501
            )
        elif line == "!END_ADMONITION":
            output_lines.append("</p></div></div>")
        else:
            output_lines.append(line)

    return "\n".join(output_lines)


def post_process_math(html: str) -> str:
    """Increase the spacing around block math elements, and math font size.

    This is a post-processor, and won't work before the latex is rendered to MathML.
    """
    html = html.replace("<math", '<math style="font-size: 1.2em;"')
    return html.replace('display="block"', 'display="block" class="my-6"')

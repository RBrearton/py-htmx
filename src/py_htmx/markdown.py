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
    pre_processor: Callable[[str], str] | None = None,
    post_processor: Callable[[str], str] | None = None,
) -> str:
    """Render the markdown string to HTML.

    Args:
        markdown: The markdown string to render.
        extras: A list of markdown2 extras to enable. By default, all the major extras
            are enabled, so latex can be rendered, code blocks will work, etc.
        pre_processor: A function that takes the markdown string and returns another
            markdown string. This can be used to do things like inject html before the
            first pass of the python markdown2 renderer.
        post_processor: A function that takes the rendered HTML and returns the final
            HTML. This can be used to add classes or other attributes to the HTML.
    """
    # Set the default extras, if required.
    if extras is None:
        extras = default_extras

    # Run pre processing, if required.
    if pre_processor is not None:
        markdown = pre_processor(markdown)

    # Render the markdown to HTML.
    html = md.markdown(markdown, extras=extras)

    # Run post processing, if required.
    if post_processor is not None:
        html = post_processor(html)

    return html


def render_admonitions(markdown: str) -> str:
    """Inject html to render admonitions wherever indicated in the markdown."""
    # Admonitions start with a "START_ADMONITION <admonition_type> <optional_title>"
    # line and end with an "END_ADMONITION" line.
    # We'll replace these with the appropriate html.
    output_lines = []
    for line in markdown.split("\n"):
        if line.startswith("START_ADMONITION"):
            # Get the admonition type and title.
            _, admonition_type, title = line.split(" ", 2)
            output_lines.append(
                f'<div class="collapse collapse-arrow bg-{admonition_type} my-4 border-3 border-{admonition_type} transition-none"><input type="checkbox" /><div class="collapse-title text-lg text-{admonition_type}-content font-medium">{title}</div><div class="collapse-content bg-base-100"><p>'  # noqa: E501
            )
        elif line == "END_ADMONITION":
            output_lines.append("</p></div></div>")
        else:
            output_lines.append(line)

    return "\n".join(output_lines)

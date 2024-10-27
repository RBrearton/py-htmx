"""Create functions that higher level batteries-included components for web apps.

While the html models in `py_htmx.models` are low-level and can be used to build
any html structure, these components are more opinionated and should look good out of
the box.
"""

from . import models as ui


def nav_bar_button(text: str, href: str) -> ui.HtmlElement:
    """Create a nav bar button with text and an icon."""
    header = ui.Heading(level=4, text=text)
    article = ui.Article(children=[header])
    return ui.Anchor(href=href, cls="btn btn-ghost", children=[article])

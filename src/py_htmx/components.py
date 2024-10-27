"""Create functions that higher level batteries-included components for web apps.

While the html models in `py_htmx.models` are low-level and can be used to build
any html structure, these components are more opinionated and should look good out of
the box.
"""

from . import models as ui


def nav_bar_button(text: str, href: str) -> ui.Anchor:
    """Create a nav bar button with text and an icon."""
    header = ui.Heading(level=4, text=text)
    article = ui.Article(children=[header])
    return ui.Anchor(href=href, cls="btn btn-ghost", children=[article])


def nav_bar_center(*elements: ui.HtmlElement) -> ui.Div:
    """Create a nav center containing the elements passed as an argument."""
    return ui.Div(
        cls="navbar-center flex flex-row items-center justify-center",
        children=list(elements),
    )


def nav_bar_start(*elements: ui.HtmlElement) -> ui.Div:
    """Create a nav start containing the elements passed as an argument."""
    return ui.Div(
        cls="navbar-start flex justify-start",
        children=list(elements),
    )


def nav_bar_end(*elements: ui.HtmlElement) -> ui.Div:
    """Create a nav end containing the elements passed as an argument."""
    return ui.Div(
        cls="navbar-end flex justify-end",
        children=list(elements),
    )


def nav_bar(
    nav_bar_start: ui.Div, nav_bar_center: ui.Div, nav_bar_end: ui.Div
) -> ui.Nav:
    """Create a nav bar with a start, center and end."""
    return ui.Nav(
        cls="navbar bg-primary text-primary-content shadow flex-shrink-0",
        children=[nav_bar_start, nav_bar_center, nav_bar_end],
    )

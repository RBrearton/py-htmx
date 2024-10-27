"""Create functions that higher level batteries-included components for web apps.

While the html models in `py_htmx.models` are low-level and can be used to build
any html structure, these components are more opinionated and should look good out of
the box.
"""

from . import models as ui

RecursiveList = list[tuple[str, str] | "RecursiveList"]  # noqa: TCH010

# region Nav


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


# endregion
# region Menu


def _list_item(text: str, href: str) -> ui.ListItem:
    """Create a list item with a link."""
    anchor = ui.Anchor(href=href, text=text)
    return ui.ListItem(children=[anchor])


def _build_contents_menu(list_elements: RecursiveList, list_so_far: ui.List) -> ui.List:
    """Recursively build the contents menu."""
    for element in list_elements:
        # If it's a tuple, get the text, href pair and create a list item from them.
        if isinstance(element, tuple):
            list_so_far.children = [*list_so_far.children, _list_item(*element)]
        else:
            # If it's a RecursiveList, create a new list and build it.
            new_list = ui.List(children=[])
            built_list = _build_contents_menu(element, new_list)
            list_so_far.children = [*list_so_far.children, built_list]

    # Return the completed list
    return list_so_far


def list_title(title: str) -> ui.ListItem:
    """Create a list item with a title."""
    return ui.ListItem(cls="menu-title", text=title)


def contents_menu(list_elements: RecursiveList, title: str | None = None) -> ui.List:
    """Create a contents menu, which can have nested submenus.

    Usage note: the list_elements tuples must be in the form (text, href).
    """
    children = [] if title is None else [list_title(title)]

    root_list = ui.List(
        cls="menu rounded-box w-80",
        children=children,
    )
    return _build_contents_menu(list_elements, root_list)


# endregion

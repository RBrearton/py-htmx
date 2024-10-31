"""Create functions that higher level batteries-included components for web apps.

While the html models in `py_htmx.models` are low-level and can be used to build
any html structure, these components are more opinionated and should look good out of
the box.
"""

from . import models as ui

RecursiveList = list["tuple[str, str | RecursiveList]"]

# region Nav


def nav_bar_button(text: str, href: str) -> ui.Anchor:
    """Create a nav bar button with text and an icon."""
    header = ui.Heading(level=4, text=text, cls="text-primary-content")
    article = ui.Article(children=[header], cls="prose")
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
) -> ui.Div:
    """Create a nav bar with a start, center and end."""
    return ui.Div(
        cls="navbar bg-primary text-primary-content shadow flex-shrink-0",
        children=[nav_bar_start, nav_bar_center, nav_bar_end],
    )


# endregion
# region Menu


def _list_item(text: str, href: str) -> ui.ListItem:
    """Create a list item with a link."""
    anchor = ui.Anchor(href=href, text=text)
    return ui.ListItem(children=[anchor])


def _list_expansion_item(text: str) -> tuple[ui.ListItem, ui.List]:
    """Create a list item that expands to reveal a sublist/submenu.

    This returns a tuple. The first element of the tuple is the list item in the
    parent list that will expand to show the sublist. The second element is a reference
    to the new sublist itself.
    """
    summary = ui.Summary(text=text)
    new_sublist = ui.List()
    details = ui.Details(children=[summary, new_sublist])
    return ui.ListItem(children=[details]), new_sublist


def _build_contents_menu(list_elements: RecursiveList, list_so_far: ui.List) -> ui.List:
    """Recursively build the contents menu."""
    for element in list_elements:
        item_text = element[0]
        value = element[1]

        # If the value is a string, we've been given a href.
        if isinstance(value, str):
            list_so_far.children = [*list_so_far.children, _list_item(item_text, value)]
        else:
            # If it's a RecursiveList, we need to make a new submenu.
            list_item, new_sublist = _list_expansion_item(item_text)

            # Populate the new sublist with the contents of the RecursiveList.
            new_sublist = _build_contents_menu(value, new_sublist)
            list_so_far.children = [*list_so_far.children, list_item]

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


def nav_bar_title(title: str) -> ui.Article:
    """Create a div with the title of the navbar."""
    heading = ui.Heading(level=4, text=title, cls="text-primary-content")
    return ui.Article(cls="prose px-5", children=[heading])

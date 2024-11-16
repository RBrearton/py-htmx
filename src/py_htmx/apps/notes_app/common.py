"""Define the html component instances used in the notes app."""

from typing import TYPE_CHECKING

from bs4 import BeautifulSoup

import py_htmx.components as c
import py_htmx.models as ui

from . import element_ids as ids
from . import endpoint_names as endpoints

if TYPE_CHECKING:
    from bs4.element import Tag


class _H3(ui.PydanticBaseModel):
    text: str
    link: str
    parent: "_H2"


class _H2(ui.PydanticBaseModel):
    text: str
    link: str
    children: list["_H3"]


class _RightMenuModel(ui.PydanticBaseModel):
    h1: str
    h2: list["_H2"]


def make_contents_menu(
    rendered_main_content: str,
    contents_menu_title: str | None,
) -> ui.List:
    """Create a contents menu from the rendered main content.

    This function takes the rendered main content and extracts the headings from it to
    create a contents menu. The contents menu is a list of links to the headings in the
    main content.
    """
    # Now figure out the contents menu.
    # Find all of the headings in the rendered markdown.
    soup = BeautifulSoup(rendered_main_content, "html.parser")
    headings = soup.find_all(["h2", "h3"])

    # Create a list of (heading_txt, heading_id) tuples that we can turn into a menu.
    right_menu = _RightMenuModel(h1="Contents", h2=[])
    for heading in headings:
        # If this heading doesn't have an id, skip it. It mustn't be a proper heading.
        # This happens when, for example, headings are put into cards that are revealed
        # by clicking a button. They'll be headings, sure, but they won't have ids.
        if "id" not in heading.attrs:
            continue

        heading: Tag
        if heading.name == "h2":
            # Build a new h2 object.
            right_menu.h2.append(
                _H2(text=heading.text, link=f"#{heading['id']}", children=[])
            )
        elif heading.name == "h3":
            # Find the parent h2 object.
            parent_h2 = right_menu.h2[-1]
            parent_h2.children.append(
                _H3(text=heading.text, link=f"#{heading['id']}", parent=parent_h2)
            )

    # Create the right menu.
    links = []
    for h2 in right_menu.h2:
        h3s = [(h3.text, h3.link) for h3 in h2.children]
        if h3s:
            links.append((h2.text, h3s))
        else:
            links.append((h2.text, h2.link))

    return c.contents_menu(links, contents_menu_title)


def make_page(
    main_content: ui.HtmlElement,
    left_drawer_content: ui.HtmlElement,
    right_drawer_content: ui.HtmlElement | None = None,
    *,
    contents_menu_title: str | None = "Contents",
    auto_right_menu: bool = True,
) -> ui.HtmlDocument:
    """Generate a page template.

    This is a monster function that builds an entire html page model. To manipulate the
    internal components, we can run e.g. `make_page().get("desired_component")` to get
    a reference to the component that we want to mutate.

    ```
    main_page = make_page(...)
    main_page.get("main_content_div").children = [ui.Label(text="Hello, world!")]
    ```

    The auto_right_menu parameter, when set to True (the default), will automatically
    make a contents menu for your page and place it in the right drawer. If you want to
    set it manually, set this parameter to False and pass the right_drawer_content
    parameter as an argument.
    """
    # region Right menu generation
    if auto_right_menu:
        right_drawer_content = make_contents_menu(
            main_content.model_dump_html(), contents_menu_title
        )

    # Make sure that we can at least put an empty div in the right drawer.
    if right_drawer_content is None:
        right_drawer_content = ui.Div()

    # endregion
    # region Header
    site_title = "Notes"
    light_theme_name = "notes_light"
    dark_theme_name = "notes_dark"
    header_html = f"""<script>
    // On page load, check if theme was saved, and apply it.
    document.addEventListener('DOMContentLoaded', function () {{
      const savedTheme = localStorage.getItem('theme') || '{light_theme_name}';
      const themeToggle = document.querySelector('.theme-controller');

      // Set the theme attribute on the HTML element.
      document.documentElement.setAttribute('data-theme', savedTheme);

      // Set the toggle checkbox based on saved theme
      themeToggle.checked = (savedTheme === '{dark_theme_name}');
    }});

    // Save theme to localStorage when toggled.
    function toggleTheme() {{
      const themeToggle = document.querySelector('.theme-controller');
      const theme = themeToggle.checked ? '{dark_theme_name}' : '{light_theme_name}';

      // Apply the theme and save it.
      document.documentElement.setAttribute('data-theme', theme);
      localStorage.setItem('theme', theme);
    }}
  </script>
  <script src="/js/collapse.js"></script>"""
    html_header = ui.Head(
        title=ui.Title(text=site_title),
        children=[ui.HtmlElement(data_theme=light_theme_name)],
        raw_inner_html=header_html,
    )
    # endregion
    # region Icons

    _main_icon_path = ui.Path(
        stroke_linecap="round",
        stroke_linejoin="round",
        d=(
            "M4.26 10.147a60.438 60.438 0 0 0-.491 6.347A48.62 48.62 0 0 1 12 20.904a48.62 48.62 0 0 1 8.232-4.41 60.46 60.46 0 0 0-.491-6.347m-15.482 0a50.636 50.636 0 0 0-2.658-.813A59.906 59.906 0 0 1 12 3.493a59.903 59.903 0 0 1 10.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.717 50.717 0 0 1 12 13.489a50.702 50.702 0 0 1 7.74-3.342M6.75 15a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm0 0v-3.675A55.378 55.378 0 0 1 12 8.443m-7.007 11.55A5.981 5.981 0 0 0 6.75 15.75v-1.5"  # noqa: E501
        ),
    )
    main_icon = ui.Svg(
        xmlns="http://www.w3.org/2000/svg",
        fill="none",
        view_box="0 0 24 24",
        stroke="currentColor",
        stroke_width="2",
        path=_main_icon_path,
        cls="size-6 ml-5",
    )

    _github_path = ui.Path(
        fill_rule="evenodd",
        clip_rule="evenodd",
        d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7.523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-.485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.526 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 75.788 0 48.854 0z",  # noqa: E501
    )
    github_icon = ui.Svg(
        path=_github_path,
        xmlns="http://www.w3.org/2000/svg",
        view_box="0 0 97.707 95.707",
        width="30px",
        height="30px",
        fill="currentColor",
        stroke="currentColor",
    )

    _sun_path = ui.Path(
        d=(
            "M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"  # noqa: E501
        )
    )
    _sun_circle = ui.Circle(cx="12", cy="12", r="5")
    sun_icon = ui.Svg(
        xmlns="http://www.w3.org/2000/svg",
        width="20",
        height="20",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        children=[_sun_path, _sun_circle],
    )

    _moon_path = ui.Path(d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z")
    moon_icon = ui.Svg(
        xmlns="http://www.w3.org/2000/svg",
        width="20",
        height="20",
        view_box="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        path=_moon_path,
    )

    # endregion
    # region Theme

    theme_selector = ui.Label(
        cls="flex flex-row cursor-pointer gap-2 px-5",
        children=[
            sun_icon,
            ui.Input(
                type="checkbox",
                value=dark_theme_name,
                cls="toggle theme-controller",
                on_click="toggleTheme()",
            ),
            moon_icon,
        ],
    )

    # endregion
    # region Search

    search = ui.Input(
        type="search",
        placeholder="Search",
        cls="input input-bordered w-64 text-base-content px-5",
    )

    # endregion
    # region Nav bar

    # The center of the nav bar is simple.
    physics_button = c.nav_bar_button("Physics", endpoints.physics)
    comp_sci_button = c.nav_bar_button("Computer science", endpoints.comp_sci)
    nav_bar_center = c.nav_bar_center(physics_button, comp_sci_button)

    # The start/end are much more awkward, but we have some helper css defined in the
    # header.
    _title = c.nav_bar_title(site_title)
    _nav_bar_start_content = ui.Div(cls="flex flex-row", children=[main_icon, _title])
    nav_bar_start = c.nav_bar_start(_nav_bar_start_content)

    github_link = ui.Anchor(
        href="https://github.com/rbrearton/py-htmx", cls="px-5", children=[github_icon]
    )
    _nav_bar_end_content = ui.Div(
        cls="flex flex-row items-center",
        children=[theme_selector, search, github_link],
    )
    _nav_bar_end_width_booster = ui.Div(
        children=[_nav_bar_end_content],
    )
    nav_bar_end = c.nav_bar_end(_nav_bar_end_width_booster)

    # Define the overall nav bar.
    nav_bar = c.nav_bar(nav_bar_start, nav_bar_center, nav_bar_end)

    # endregion
    # region Main

    _main_content_container = ui.Main(
        cls="drawer-content p-10 flex flex-row justify-center", children=[main_content]
    )

    # endregion
    # region Right drawer

    _right_drawer_side = ui.Div(cls="drawer-side", children=[right_drawer_content])
    _right_drawer_toggle_input = ui.Input(
        id=ids.right_drawer_toggle_id, type="checkbox", cls="drawer-toggle"
    )
    _right_drawer_root = ui.Div(
        cls="drawer drawer-end xl:drawer-open",
        children=[
            _right_drawer_toggle_input,
            _main_content_container,
            _right_drawer_side,
        ],
    )

    # endregion
    # region Left drawer

    _left_drawer_side = ui.Div(
        cls="drawer-side flex-shrink-0", children=[left_drawer_content]
    )
    _left_drawer_toggle_input = ui.Input(
        id=ids.left_drawer_toggle_id, type="checkbox", cls="drawer-toggle"
    )
    _left_drawer_content = ui.Div(
        cls="drawer-content",
        children=[_right_drawer_root],
    )
    left_drawer_root = ui.Div(
        cls="drawer lg:drawer-open py-10",
        children=[_left_drawer_toggle_input, _left_drawer_side, _left_drawer_content],
    )

    # endregion
    # region Footer

    footer = ui.Footer(
        cls="footer p-4 bg-base-300",
        children=[
            ui.Label(
                text="&copy; 2024 Dr. Richard Brearton",
            )
        ],
    )

    # endregion

    # Finally, we put everything together.
    body = ui.Body(
        children=[nav_bar, left_drawer_root, footer],
    )
    return ui.HtmlDocument(head=html_header, body=body)


def physics_left_drawer() -> ui.List:
    """Build the contents of the left drawer for the physics section."""
    return c.contents_menu(
        [
            (
                "B2: Symmetry and relativity",
                [
                    ("PS1", f"{endpoints.b2_ps1}"),
                    ("PS2", f"{endpoints.b2_ps2}"),
                ],
            ),
            (
                "B6: Condensed matter physics",
                [
                    ("PS1", f"{endpoints.b6_ps1}"),
                    ("PS2", f"{endpoints.b6_ps2}"),
                ],
            ),
        ],
        "Problem sheets",
    )

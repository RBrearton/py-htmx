"""Define the html component instances used in the notes app."""

import py_htmx.components as c
import py_htmx.models as ui

from . import endpoint_names as endpoints

site_title = "Physics teaching notes"
style_header = """
<style>
:root {
--main-content-max-width: 1000px;
}
.drawer-side {
height: auto;
}
.w-drawer-side {
width: calc((100vw - var(--main-content-max-width)) / 2);
}
</style>
"""
light_theme_name = "cupcake"
dark_theme_name = "notes_dark"
html_header = ui.Head(
    title=ui.Title(text=site_title),
    children=[ui.HtmlElement(data_theme=light_theme_name)],
    style=style_header,
)


# region Icons

_main_icon_path = ui.Path(
    stroke_linecap="round",
    stroke_linejoin="round",
    d=(
        "M4.26 10.147a60.438 60.438 0 0 0-.491 6.347A48.62 48.62 0 0 1 12 20.904a48.62 "
        "48.62 0 0 1 8.232-4.41 60.46 60.46 0 0 0-.491-6.347m-15.482 0a50.636 50.636 0 "
        "0 0-2.658-.813A59.906 59.906 0 0 1 12 3.493a59.903 59.903 0 0 1 10.399 "
        "5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.717 50.717 0 0 1 12 "
        "13.489a50.702 50.702 0 0 1 7.74-3.342M6.75 15a.75.75 0 1 0 0-1.5.75.75 0 0 0 "
        "0 1.5Zm0 0v-3.675A55.378 55.378 0 0 1 12 8.443m-7.007 11.55A5.981 5.981 0 0 0 "
        "6.75 15.75v-1.5"
    ),
)
main_icon = ui.Svg(
    xmlns="http://www.w3.org/2000/svg",
    fill="none",
    view_box="0 0 24 24",
    stroke="currentColor",
    stroke_width="2",
    path=_main_icon_path,
)

_github_path = ui.Path(
    fill_rule="evenodd",
    clip_rule="evenodd",
    d="M48.854 0C21.839 0 0 22 0 49.217c0 21.756 13.993 40.172 33.405 46.69 2.427.49 "
    "3.316-1.059 3.316-2.362 0-1.141-.08-5.052-.08-9.127-13.59 2.934-16.42-5.867-16.42-"
    "5.867-2.184-5.704-5.42-7.17-5.42-7.17-4.448-3.015.324-3.015.324-3.015 4.934.326 7."
    "523 5.052 7.523 5.052 4.367 7.496 11.404 5.378 14.235 4.074.404-3.178 1.699-5.378 "
    "3.074-6.6-10.839-1.141-22.243-5.378-22.243-24.283 0-5.378 1.94-9.778 5.014-13.2-."
    "485-1.222-2.184-6.275.486-13.038 0 0 4.125-1.304 13.426 5.052a46.97 46.97 0 0 1 "
    "12.214-1.63c4.125 0 8.33.571 12.213 1.63 9.302-6.356 13.427-5.052 13.427-5.052 "
    "2.67 6.763.97 11.816.485 13.038 3.155 3.422 5.015 7.822 5.015 13.2 0 18.905-11.404"
    " 23.06-22.324 24.283 1.78 1.548 3.316 4.481 3.316 9.126 0 6.6-.08 11.897-.08 13.52"
    "6 0 1.304.89 2.853 3.316 2.364 19.412-6.52 33.405-24.935 33.405-46.691C97.707 22 7"
    "5.788 0 48.854 0z",
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
        "M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-"
        "1.4M18.4 5.6l1.4-1.4"
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
    cls="flex cursor-pointer gap-2 px-5",
    children=[
        sun_icon,
        ui.Input(
            type="checkbox",
            value=dark_theme_name,
            cls="toggle theme-controller",
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

physics_button = c.nav_bar_button("Physics", endpoints.physics_page)
comp_sci_button = c.nav_bar_button("Computer science", endpoints.comp_sci_page)
nav_bar_center = c.nav_bar_center(physics_button, comp_sci_button)

# endregion
body = ui.Body(cls="flex flex-col min-h-screen")

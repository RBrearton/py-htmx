"""Define the html components used in the notes app."""

import py_htmx.models as ui

site_title = "Physics teaching notes"
html_header = ui.Head(
    title=ui.Title(text=site_title),
)


# region Nav bar
# The home button goes on the left.
home_button = ui.Div(
    cls="flex-1",
    children=[
        ui.Anchor(text=site_title, cls=["btn btn-ghost text-xl"]),
    ],
)

# Then we have a search bar and menu on the right.
search_component = ui.Div(
    cls="form-control",
    children=[
        ui.Input(
            type="text",
            placeholder="Search",
            cls="input input-bordered w-24 md:w-auto",
        )
    ],
)
options_component = ui.Div()
search_and_options = ui.Div(
    cls="flex-none gap-2",
    children=[
        search_component,
        options_component,
    ],
)

# Now build the nav bar.
nav_bar = ui.Div(
    cls="navbar bg-base-100",
    children=[
        home_button,
        search_and_options,
    ],
)

# endregion
# region Left drawer

left_drawer = ui.Div(
    cls="drawer lg:drawer-open",
    children=[
        ui.Input(
            id="my-drawer-2",
            type="checkbox",
            cls="drawer-toggle",
        ),
        ui.Div(
            cls="drawer-content flex flex-col items-center justify-center",
            children=[
                ui.Label(
                    label_for="my-drawer-2",
                    cls="btn btn-primary drawer-button lg:hidden",
                    text="Open drawer",
                )
            ],
        ),
        ui.Div(
            cls="drawer-side",
            children=[
                ui.Label(
                    label_for="my-drawer-2",
                    cls="drawer-overlay",
                    aria_label="close sidebar",
                )
            ],
        ),
        ui.List(
            cls="menu bg-base-200 text-base-content min-h-full w-80 p-4",
            children=[
                ui.ListItem(
                    children=[
                        ui.Anchor(
                            text="Sidebar item 1",
                        )
                    ]
                ),
                ui.ListItem(
                    children=[
                        ui.Anchor(
                            text="Sidebar item 2",
                        )
                    ]
                ),
            ],
        ),
    ],
)

# endregion

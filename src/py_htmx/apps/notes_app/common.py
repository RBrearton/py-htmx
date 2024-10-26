"""Define the html components used in the notes app."""

import py_htmx.models as ui

site_title = "Physics teaching notes"
html_header = ui.Head(
    title=ui.Title(text=site_title),
)

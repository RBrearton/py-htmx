"""Define the main page for the notes app."""

import py_htmx.models as ui

from .common import html_header, left_drawer, nav_bar

body = ui.Body(
    children=[
        nav_bar,
        left_drawer,
    ]
)
main_page_html_document = ui.HtmlDocument(head=html_header, body=body)

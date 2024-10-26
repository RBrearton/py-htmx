"""Define the main page for the notes app."""

import py_htmx.models as ui

from .common import html_header, nav_bar

body = ui.Body(
    children=[
        nav_bar,
    ]
)
main_page_html_document = ui.HtmlDocument(head=html_header, body=body)

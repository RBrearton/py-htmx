"""Define the main page for the notes app."""

import py_htmx.models as ui

from .common import html_header

body = ui.Body()
main_page_html_document = ui.HtmlDocument(head=html_header, body=body)

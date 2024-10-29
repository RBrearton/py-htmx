"""Defines the FastAPI routes. Running will run the FastAPI server."""

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse

from py_htmx import components as c
from py_htmx import models as ui
from py_htmx.apps.notes_app.common import make_page

app = FastAPI(
    title="Physics teaching notes",
)


@app.get("/dist.css")
async def get_css() -> FileResponse:
    """Return the CSS file."""
    return FileResponse("dist.css")


@app.get("/favicon.ico")
async def get_favicon() -> FileResponse:
    """Return the favicon."""
    return FileResponse("note_icon.png")


@app.get("/")
async def get_index() -> HTMLResponse:
    """Return the index HTML file."""
    main_page = make_page(
        ui.Article(
            cls="prose",
            children=[
                ui.Heading(level=1, text="Physics teaching notes"),
                ui.Paragraph(
                    text=(
                        "Here are my notes on some physics topics. Check back "
                        "later for updates."
                    )
                ),
            ],
        ),
        left_drawer_content=c.contents_menu(
            [
                ("B2: Symmetry and relativity", [("PS1", "#"), ("PS2", "#")]),
                ("B6: Condensed matter physics", [("PS1", "#"), ("PS2", "#")]),
            ],
            "Left title",
        ),
        right_drawer_content=c.contents_menu(
            [("right_drawer_1", "#"), ("right_drawer_2", "#")], "Right title"
        ),
    )
    response = HTMLResponse(content=main_page.model_dump_html())
    print(main_page.model_dump_html())
    return response


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException) -> HTMLResponse:
    """Handle 404 errors."""
    del request
    del exc
    return HTMLResponse(
        content="I didn't write a 404 page yet. Consider yourself double 404'd. ",
        status_code=404,
    )


def main() -> None:
    """Run the FastAPI server."""
    # We need the ugly import string to make auto-reload work.
    uvicorn.run(
        "py_htmx.apps.notes_app.main:app",
        host="127.0.0.1",
        port=6969,
        reload=True,
    )


if __name__ == "__main__":
    main()

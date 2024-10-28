"""Defines the FastAPI routes. Running will run the FastAPI server."""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse

from py_htmx import components as c
from py_htmx import models as ui

from .common import make_page

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
    response = HTMLResponse(
        content=make_page(
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
                [("left_drawer_1", "#"), ("left_drawer_2", "#")], "Left title"
            ),
            right_drawer_content=c.contents_menu(
                [("right_drawer_1", "#"), ("right_drawer_2", "#")], "Right title"
            ),
        ).model_dump_html()
    )
    print(response)
    return response


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

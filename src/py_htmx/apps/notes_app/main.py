"""Defines the FastAPI routes. Running will run the FastAPI server."""

from functools import lru_cache

import uvicorn
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse

from py_htmx import components as c
from py_htmx import models as ui

from . import endpoint_names as endpoints
from .common import make_page, make_physics_left_drawer
from .config import config

app = FastAPI(
    title="Physics teaching notes",
)


@lru_cache
def raw_markdown(file_name: str) -> str:
    """Read the markdown file at the given path."""
    return (config.markdown_files_dir / file_name).read_text()


@app.get(endpoints.css_file)
async def get_css() -> FileResponse:
    """Return the CSS file."""
    return FileResponse("dist.css")


@app.get(endpoints.favicon)
async def get_favicon() -> FileResponse:
    """Return the favicon."""
    return FileResponse("note_icon.png")


@app.get(endpoints.b6_ps1)
async def get_b6_ps1() -> HTMLResponse:
    """Return the page for B6 problem set 1.

    This renders the b6_ps1.md markdown file.
    """
    # Get the appropriate markdown file.
    markdown_txt = raw_markdown("b6_ps1.md")

    # Render the markdown file as an html string.
    rendered_markdown = ui.render_markdown(markdown_txt)

    # Find all of the headings in the rendered markdown.
    soup = BeautifulSoup(rendered_markdown, "html.parser")
    headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

    # Create a list of (heading_txt, heading_id) tuples that we can turn into a menu.
    links: list[tuple[str, str | c.RecursiveList]] = [
        (heading.text, heading["id"]) for heading in headings
    ]
    right_menu = c.contents_menu(links, "Contents")

    # Create the main page.
    main_page = make_page(
        main_content=ui.Article(
            cls="prose !max-w-none", raw_inner_html=rendered_markdown
        ),
        left_drawer_content=make_physics_left_drawer(),
        right_drawer_content=right_menu,
    )
    return HTMLResponse(content=main_page.model_dump_html())


@app.get(endpoints.physics)
async def get_physics() -> HTMLResponse:
    """Return the physics section."""
    # Currently, this is the same as the index page.
    return await get_index()


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
        left_drawer_content=make_physics_left_drawer(),
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

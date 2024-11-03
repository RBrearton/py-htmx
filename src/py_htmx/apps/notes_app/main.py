"""Defines the FastAPI routes. Running will run the FastAPI server."""

from typing import TYPE_CHECKING

import uvicorn
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse

from py_htmx import components as c
from py_htmx import markdown as md
from py_htmx import models as ui
from py_htmx.apps.notes_app import endpoint_names as endpoints
from py_htmx.apps.notes_app.common import make_page, physics_left_drawer
from py_htmx.apps.notes_app.config import config

if TYPE_CHECKING:
    from bs4.element import Tag

app = FastAPI(
    title="Physics teaching notes",
)


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


def render_markdown(file_name: str) -> tuple[str, ui.List]:
    """Read the markdown file with the given name, and render it to an html string.

    This function returns a tuple of the rendered markdown string and the right menu.
    """
    markdown_txt = (config.markdown_files_dir / file_name).read_text()

    # Render the markdown file as an html string.
    markdown_string = md.render_markdown(
        markdown_txt,
        pre_processors=[md.render_admonitions],
        post_processors=[md.post_process_math],
    )

    # Now figure out the contents menu.
    # Find all of the headings in the rendered markdown.
    soup = BeautifulSoup(markdown_string, "html.parser")
    headings = soup.find_all(["h2", "h3"])

    # Create a list of (heading_txt, heading_id) tuples that we can turn into a menu.
    right_menu = _RightMenuModel(h1="Contents", h2=[])
    for heading in headings:
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

    right_menu = c.contents_menu(links, "Contents")

    return markdown_string, right_menu


@app.get(endpoints.css_file)
async def get_css() -> FileResponse:
    """Return the CSS file."""
    return FileResponse("dist.css")


@app.get(endpoints.favicon)
async def get_favicon() -> FileResponse:
    """Return the favicon."""
    return FileResponse("note_icon.png")


@app.get(endpoints.b2_ps2)
async def get_b2_ps2() -> HTMLResponse:
    """Return the page for B2 problem set 2.

    This renders the b2_ps2.md markdown file.
    """
    # Get the appropriate markdown file, and the menu.
    rendered_markdown, right_menu = render_markdown("b2_ps2.md")

    # Create the main page.
    main_page = make_page(
        main_content=ui.Article(
            cls="prose !max-w-[850px]", raw_inner_html=rendered_markdown
        ),
        left_drawer_content=physics_left_drawer(),
        right_drawer_content=right_menu,
    )
    return HTMLResponse(content=main_page.model_dump_html())


@app.get(endpoints.b6_ps1)
async def get_b6_ps1() -> HTMLResponse:
    """Return the page for B6 problem set 1.

    This renders the b6_ps1.md markdown file.
    """
    # Get the appropriate markdown file, and the menu.
    rendered_markdown, right_menu = render_markdown("b6_ps1.md")

    # Create the main page.
    main_page = make_page(
        main_content=ui.Article(
            cls="prose !max-w-[850px]", raw_inner_html=rendered_markdown
        ),
        left_drawer_content=physics_left_drawer(),
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
    # Get the rendered markdown file,
    rendered_markdown, right_menu = render_markdown("index.md")

    # Create the main page.
    main_page = make_page(
        main_content=ui.Article(
            cls="prose !max-w-[850px]", raw_inner_html=rendered_markdown
        ),
        left_drawer_content=physics_left_drawer(),
        right_drawer_content=right_menu,
    )
    return HTMLResponse(content=main_page.model_dump_html())


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

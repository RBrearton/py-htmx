"""Defines the FastAPI routes. Running will run the FastAPI server."""

from collections.abc import Callable
from functools import lru_cache

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel, Field

from py_htmx.config import parsed_config as config

app = FastAPI(
    title="Physics teaching notes",
)


# region Utils


@app.middleware("http")
async def clear_cache_if_auto_reloading(
    request: Request, call_next: Callable
) -> HTMLResponse:
    """Clear the cache if auto-reloading is enabled.

    This middleware is used to clear the cache of the render_markdown function if
    auto-reloading is enabled. This is useful for development purposes, as it means that
    changes to the markdown files will be immediately reflected in the rendered HTML.
    """
    if config.auto_reload:
        # Find all the functions that have a cache_clear method and call it.
        for route in app.routes:
            if hasattr(route, "cache_clear"):
                route.cache_clear()  # type: ignore  # noqa: PGH003
    return await call_next(request)


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
    # We need the ugly import string to make auto-reload work, if it's enabled.
    uvicorn.run(
        "py_htmx.main:app",
        host=config.hostname,
        port=config.port,
        reload=config.auto_reload,
    )


# endregion
# region Models


class Topic(BaseModel):
    """Contains information relating to one of the site's main topics."""

    name: str


class MenuItem(BaseModel):
    """Contains information about a particular menu item."""

    text: str = Field(..., description="The text to display in the menu.")
    route: str | None = Field(
        ...,
        description=(
            "The route that the menu item links to. If None, this doesn't link to "
            "anything."
        ),
    )
    children: list["MenuItem"] = Field(
        default=[], description="Any children of this menu item."
    )


class RightMenu(BaseModel):
    """Contains information relating to the right menu of a page."""

    route: str = Field(
        ..., description="The route of the page that the right menu is for."
    )
    heading: str = Field(
        default="Contents", description="The main heading for the menu."
    )


# endregion
# region API


@app.get("/api/topics", tags=["api"])
async def get_topics_endpoint() -> list[Topic]:
    """Return site's main topics."""
    return [Topic(name=n.name) for n in config.pages_path.glob("*") if n.is_dir()]


@app.get("/api/routes", tags=["api"])
async def get_routes() -> list[str]:
    """Return all the routes."""
    # To do this, we need to recurse over all the directories in the pages directory.
    # Each markdown file will have a corresponding route, where the route is the
    # relative path to the markdown file, minus the file extension, from the pages
    # directory.
    # The final rule is that any file called "home.md" will have the same route as the
    # directory it is in.
    routes = []
    for page in config.pages_path.rglob("*.md"):
        route = page.relative_to(config.pages_path).with_suffix("").as_posix()

        # If the file is called "home.md", we need to remove the filename from the
        # route.
        if page.name == "home.md":
            route = page.parent.relative_to(config.pages_path).as_posix()

        # If the route starts with a "." (because of how we're using relative_to), we
        # need to remove it.
        if route.startswith("."):
            route = route[1:]

        # Make sure that the route starts with a "/".
        if not route.startswith("/"):
            route = f"/{route}"

        routes.append(route)

    return routes


@app.get("/api/{route:path}/right_menu", tags=["api"])
async def get_right_menu(route: str) -> dict[str, str]:
    """Return the right menu for the given route."""
    return {"route": route}


# endregion
# region Files


@app.get("/", tags=["file"])
async def get_homepage() -> HTMLResponse:
    """Return the homepage."""
    return HTMLResponse(
        content=(config.client_path / "index.html").read_text(), status_code=200
    )


@app.get("/assets/{filename}", tags=["file"])
async def get_asset(filename: str) -> FileResponse:
    """Return an asset."""
    return FileResponse(config.client_path / "assets" / filename)


@app.get("/vite.svg", tags=["file"])
async def get_vite_svg() -> FileResponse:
    """Return the Vite logo."""
    return FileResponse(config.client_path / "vite.svg")


# endregion


if __name__ == "__main__":
    main()

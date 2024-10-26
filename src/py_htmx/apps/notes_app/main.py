"""Defines the FastAPI routes. Running will run the FastAPI server."""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(
    title="Physics teaching notes",
)


@app.get("/dist.css")
async def get_dist_css() -> FileResponse:
    """Return the CSS file."""
    return FileResponse("dist.css")


@app.get("/")
async def get_index() -> FileResponse:
    """Return the index HTML file."""
    return FileResponse("index.html")


def main() -> None:
    """Run the FastAPI server."""
    uvicorn.run(app, host="0.0.0.0", port=6969, reload=True)  # noqa: S104

"""Defines the FastAPI routes. Running will run the FastAPI server."""

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(
    title="Physics teaching notes",
)


@app.get("/dist.css")
async def get_css() -> FileResponse:
    """Return the CSS file."""
    return FileResponse("dist.css")


@app.get("/")
async def get_index() -> FileResponse:
    """Return the index HTML file."""
    return FileResponse("index.html")


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

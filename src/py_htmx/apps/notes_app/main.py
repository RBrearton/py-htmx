"""Defines the FastAPI routes. Running will run the FastAPI server."""

from collections.abc import Callable

import numpy as np
import plotly.graph_objects as go
import uvicorn
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, HTMLResponse

from py_htmx import models as ui
from py_htmx.apps.notes_app import endpoint_names as endpoints
from py_htmx.apps.notes_app import physics_functions as fn
from py_htmx.apps.notes_app.common import (
    make_page,
    physics_left_drawer,
    render_markdown,
)
from py_htmx.apps.notes_app.config import config

# region Utils

app = FastAPI(
    title="Physics teaching notes",
)


class DiatomicDispersionModel(ui.PydanticBaseModel):
    """Pydantic model for the diatomic dispersion relation plotly htmx endpoint."""

    mass_1: float = Query(1, ge=0.1, le=10)
    mass_2: float = Query(2, ge=0.1, le=10)


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
        render_markdown.cache_clear()
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
        "py_htmx.apps.notes_app.main:app",
        host=config.hostname,
        port=config.port,
        reload=config.auto_reload,
    )


# endregion
# region Endpoints


@app.get("/js/collapse.js")
async def get_collapse() -> FileResponse:
    """Return the collapse.js file."""
    return FileResponse("js/collapse.js")


@app.get("/dist.css")
async def get_css() -> FileResponse:
    """Return the CSS file."""
    return FileResponse("dist.css")


@app.get("/favicon.ico")
async def get_favicon() -> FileResponse:
    """Return the favicon."""
    return FileResponse("note_icon.png")


@app.get("/plots/diatomic_dispersion")
async def get_diatomic_dispersion_plot(mass_1: float, mass_2: float) -> HTMLResponse:
    """Return the diatomic dispersion plot.

    This function is designed to be used with htmx to update the plot when the user
    changes the parameters.
    """
    # Prepare the parameters for the plot.
    interatomic_distance = 1
    spring_const = 1
    num_points = 10_000
    wavevectors = np.linspace(
        -np.pi / interatomic_distance, np.pi / interatomic_distance, num_points
    )

    # Calculate the dispersion relations.
    dispersion_acoustic = fn.diatomic_dispersion(
        wavevectors,
        spring_const,
        mass_1,
        mass_2,
        interatomic_distance,
        is_optical=False,
    )
    dispersion_optical = fn.diatomic_dispersion(
        wavevectors,
        spring_const,
        mass_1,
        mass_2,
        interatomic_distance,
        is_optical=True,
    )

    # Also calculate the optical branch for the extended zone scheme.
    extended_wavevectors_1 = np.linspace(
        -2 * np.pi / interatomic_distance, -np.pi / interatomic_distance, num_points
    )
    extended_wavevectors_2 = np.linspace(
        np.pi / interatomic_distance, 2 * np.pi / interatomic_distance, num_points
    )
    dispersion_optical_extended_1 = fn.diatomic_dispersion(
        extended_wavevectors_1,
        spring_const,
        mass_1,
        mass_2,
        interatomic_distance,
        is_optical=True,
    )
    dispersion_optical_extended_2 = fn.diatomic_dispersion(
        extended_wavevectors_2,
        spring_const,
        mass_1,
        mass_2,
        interatomic_distance,
        is_optical=True,
    )

    # Create the figure
    fig = go.Figure()

    # Add acoustic branch
    fig.add_trace(
        go.Scatter(
            x=wavevectors,
            y=dispersion_acoustic,
            mode="lines",
            name="acoustic",
            line={"color": "#1f77b4"},  # Use a consistent color scheme
        )
    )

    # Add optical-reduced branch
    fig.add_trace(
        go.Scatter(
            x=wavevectors,
            y=dispersion_optical,
            mode="lines",
            name="optical",
            line={"color": "#ff7f0e"},  # Use a consistent color scheme
        )
    )

    # Add optical-extended-1 branch
    fig.add_trace(
        go.Scatter(
            x=extended_wavevectors_1,
            y=dispersion_optical_extended_1,
            mode="lines",
            name="optical-extended",
            legendgroup="optical-extended",
            line={"color": "#2ca02c", "dash": "dot"},  # Use a consistent color scheme
        )
    )

    # Add optical-extended-2 branch
    fig.add_trace(
        go.Scatter(
            x=extended_wavevectors_2,
            y=dispersion_optical_extended_2,
            mode="lines",
            name="optical-extended",
            legendgroup="optical-extended",
            showlegend=False,  # Hide the second legend entry
            line={"color": "#2ca02c", "dash": "dot"},  # Use a consistent color scheme
        )
    )

    # Update layout
    fig.update_layout(
        title="Diatomic Dispersion Relation",
        xaxis_title="Wavevector",
        yaxis_title="Frequency ω",
        template="plotly_dark",
    )

    # Make the figure always have a height of 1000 pixels.
    fig.update_layout(height=1000)
    return HTMLResponse(content=fig.to_html(full_html=False))


@app.get(endpoints.b2_ps2)
async def get_b2_ps2() -> HTMLResponse:
    """Return the page for B2 problem set 2.

    This renders the b2_ps2.md markdown file.
    """
    # Create the main page.
    main_page = make_page(
        main_content=render_markdown("b2_ps2.md"),
        left_drawer_content=physics_left_drawer(),
    )
    print(render_markdown("b2_ps2.md"))
    return HTMLResponse(content=main_page.model_dump_html())


@app.get(endpoints.b6_ps2)
async def get_b6_ps2() -> HTMLResponse:
    """Return the page for B6 problem set 2.

    This renders the b6_ps1.md markdown file.
    """
    # Render the markdown file.
    markdown = render_markdown("b6_ps2.md")

    # Now prepare the UI elements for the diatomic dispersion plot and its inputs.
    # This is the div that the plot will go in via hx-swap.
    plot_container_id = "diatomic_dispersion_plot_container"
    plot_container = ui.Div(id=plot_container_id)

    # The inputs and labels for the masses. The labels update based on the input values.
    min_value = 0.1
    max_value = 2
    mass_1_start = 1
    mass_2_start = 2
    input_step = 0.01
    mass_1_input = ui.Input(
        name="mass_1",
        type="range",
        min=min_value,
        max=max_value,
        value=mass_1_start,
        cls="range range-secondary",
        id="mass_1_input",
        step=input_step,
        on_input="mass_1_output.value = mass_1_input.value",
    )
    mass_1_output = ui.Output(id="mass_1_output", text=str(mass_1_start))
    mass_1_label = ui.Label(
        text=f"Mass 1: {mass_1_output.model_dump_html()}",
        label_for=mass_1_input.id,
    )
    mass_2_input = ui.Input(
        name="mass_2",
        type="range",
        min=min_value,
        max=max_value,
        value=mass_2_start,
        cls="range",
        id="mass_2_input",
        step=input_step,
        on_input="mass_2_output.value = mass_2_input.value",
    )
    mass_2_output = ui.Output(id="mass_2_output", text=str(mass_2_start))
    mass_2_label = ui.Label(
        text=f"Mass 2: {mass_2_output.model_dump_html()}",
        label_for=mass_2_input.id,
    )

    # If we just displayed the inputs and labels, they would be stacked vertically, and
    # would be super wide. We want them to be side-by-side, so we wrap them in divs and
    # use flexbox to style them.
    mass_1_div = ui.Div(
        cls="flex flex-col items-center grow p-2",
        children=[mass_1_label, mass_1_input],
    )
    mass_2_div = ui.Div(
        cls="flex flex-col items-center grow p-2",
        children=[mass_2_label, mass_2_input],
    )
    input_div = ui.Div(
        cls="flex flex-row justify-between w-full",
        children=[mass_1_div, mass_2_div],
    )

    # Now finally, create the form that will trigger the plot update.
    form = ui.Form(
        hx_get="/plots/diatomic_dispersion",
        hx_trigger="load, change from:input",
        hx_target=f"#{plot_container_id}",
        children=[input_div],
    )

    # Now swap out the placeholder in the markdown with the actual form.
    diatomic_plotly_html = plot_container.model_dump_html() + form.model_dump_html()
    main_content = markdown.replace("!DIATOMIC_DISPERSION_PLOT", diatomic_plotly_html)

    # Create the main page.
    main_page = make_page(
        main_content=main_content,
        left_drawer_content=physics_left_drawer(),
    )
    return HTMLResponse(content=main_page.model_dump_html())


@app.get(endpoints.b6_ps2)
async def get_b6_ps1() -> HTMLResponse:
    """Return the page for B6 problem set 1."""
    main_page = make_page(
        main_content=render_markdown("b6_ps1.md"),
        left_drawer_content=physics_left_drawer(),
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
        main_content=render_markdown("index.md"),
        left_drawer_content=physics_left_drawer(),
    )
    return HTMLResponse(content=main_page.model_dump_html())


# endregion


if __name__ == "__main__":
    main()

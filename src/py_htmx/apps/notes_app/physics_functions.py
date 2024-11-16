"""Define the physics functions used for plotting."""

import numpy as np


def diatomic_dispersion(
    wavevector: np.ndarray,
    spring_const: float,
    mass_1: float,
    mass_2: float,
    interatomic_distance: float,
    *,
    is_optical: bool = False,
) -> np.ndarray:
    """Return the dispersion relation for a 1d diatomic chain."""
    # The prefactor of the whole expression.
    prefactor = spring_const / mass_1 / mass_2

    # We use plus for the optical branch and minus for the acoustic branch.
    plus_minus = 1 if is_optical else -1

    # Now produce the expression for the square of the dispersion relation.
    dispersion_sq = prefactor * (
        mass_1
        + mass_2
        + plus_minus
        * np.sqrt(
            (mass_1 + mass_2) ** 2
            - 4 * mass_1 * mass_2 * np.sin(wavevector * interatomic_distance / 2) ** 2
        )
    )
    return np.sqrt(dispersion_sq)

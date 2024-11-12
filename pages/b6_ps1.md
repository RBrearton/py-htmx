<!--  -->

# Problem set 1

## Q1: Einstein solid

We're asked to consider a single simple harmonic oscillator, given by $H = \frac{p^2}{2m} + \frac{1}{2}kx^2$

### Classical partition function

We're asked to calculate the classical partition function $Z=\int \frac{d^3p}{(2\pi\hbar)^3} \int d^3x e^{-\beta H(\vec{p}, \vec{x})}$.

!START_ADMONITION info Show working

It's easy however you tackle it, but I decided to solve the 1D partition function, then cube it.
It's instructive to note that, since we're just looking at heat capacities, we can ignore the prefactor of $\frac{1}{2\pi\hbar}$ in the momentum integral.
We have:

$$
Z_\mathrm{1D} = \iint  e^{-\beta \left(\frac{p^2}{2m} + \frac{1}{2}kx^2\right)} dx dp
$$

We can then use the standard Gaussian integral:

$$
\int e^{-ax^2} dx = \sqrt{\frac{\pi}{a}}
$$

to get:

$$
Z_\mathrm{1D} = \sqrt{\frac{\pi}{\beta/2m}} \sqrt{\frac{\pi}{k\beta/2}}
$$

Now writing this in terms of $\omega = \sqrt{k/m}$, we get:

$$
Z_\mathrm{1D} = \frac{2\pi}{\beta\omega}
$$

We can then cube this to get the 3D partition function.

!END_ADMONITION

!START_ADMONITION success Answer

$$Z_\mathrm{3D} = \left(\frac{2\pi}{\beta\omega}\right)^3$$

Or, if we would've kept the prefactor in the momentum integral:

$$Z_\mathrm{3D} = \left(\frac{1}{\beta\hbar\omega}\right)^{3}$$

!END_ADMONITION

### Heat capacity from the classical partition function

Now we're asked to calculate the heat capacity from the classical partition function that we just calculated.

!START_ADMONITION info Show working

Another easy calculation. Start by calculating the internal energy $U$:

$$
U = -\frac{\partial}{\partial \beta} \ln Z = -\frac{\partial}{\partial \beta} \ln \left(\frac{2\pi}{\beta\omega}\right)^3 = 3k_BT
$$

Then the heat capacity is:

$$
C = \frac{\partial U}{\partial T} = 3k_B
$$

!END_ADMONITION

!START_ADMONITION success Answer

$C = 3k_B$

!END_ADMONITION

!START_ADMONITION note Note

    This means that, for a 3D system containing N oscillators, we have $C = 3R$, which is the Dulong-Petit law.

!END_ADMONITION

### Quantum partition function

We're asked to now calculate the quantum partition function $Z = \sum_n e^{-\beta E_n}$

!START_ADMONITION info Show working

We can use the fact that the energy levels are $E_n = \hbar \omega (n + 1/2)$, so we have:

$$
Z = \sum_n e^{-\beta \hbar \omega (n + 1/2)} = e^{-\beta \hbar \omega / 2} \sum_n e^{-\beta \hbar \omega n}
$$

The sum is a geometric series, so we can write it as:

$$
Z = e^{-\beta \hbar \omega / 2} \frac{1}{1 - e^{-\beta \hbar \omega}}
$$

We can then simplify this to:

$$
Z = \frac{e^{-\beta \hbar \omega / 2}}{1 - e^{-\beta \hbar \omega}} = \left(2\sinh(\beta \hbar \omega / 2)\right)^{-1}
$$

!END_ADMONITION

!START_ADMONITION success Answer

    $Z = \left(2\sinh(\beta \hbar \omega / 2)\right)^{-1}$

!END_ADMONITION

!START_ADMONITION note Note

    The internal energy, once we calculate it, looks reminiscent of Bose-Einstein statistics.

    $$
    U = -\frac{\partial}{\partial \beta} \ln Z = \frac{\hbar \omega}{2} + \frac{\hbar \omega}{e^{\beta \hbar \omega} - 1}
    $$

    Where the Bose occupation number is $n_B = \frac{1}{e^{\beta \hbar \omega} - 1}$.
    The physical interpretation of this is that a quantum harmonic oscillator is, on average, excited up to the energy level equal to the Bose occupation number.
    I don't believe that there's a deeper physical meaning to this, but it's interesting to note.(1)
    { .annotate }

    1. If there's a deeper physical connection, please let me know!

!END_ADMONITION

Next we're asked to find an expression for the heat capacity of the quantum harmonic oscillator.

!START_ADMONITION info Show working

    We can start by calculating the internal energy, as we did above:

    $$
    U = \frac{\hbar \omega}{2} + \frac{\hbar \omega}{e^{\beta \hbar \omega} - 1}
    $$

    Then the heat capacity is:

    $$
    C = \frac{\partial U}{\partial T} = \frac{\hbar \omega}{k_B} \frac{e^{\beta \hbar \omega}}{(e^{\beta \hbar \omega} - 1)^2}
    $$

    We can then simplify this to:

    $$
    C = k_B \left(\frac{\beta \hbar \omega}{2}\right)^2 \frac{e^{\beta \hbar \omega}}{(e^{\beta \hbar \omega} - 1)^2}
    $$

    Note that this is the 1D case.
    To get the 3D case, we would need to cube the partition function, which would give us an extra factor of 3 in the heat capacity.
    Similarly, to generalize for $N$ oscillators, we'd end up raising the partition function to the power of $N$, which would give us an extra factor of $N$ in the heat capacity.

!END_ADMONITION
!START_ADMONITION success Answer

    $$
    C = 3 N k_B (\beta \hbar \omega)^2 \frac{e^{\beta \hbar \omega}}{(e^{\beta \hbar \omega} - 1)^2}
    $$

!END_ADMONITION

## Q2: Debye model

We're asked to state the assumptions of the Debye model.

!START_ADMONITION success Answer

    Linear dispersion relation: $\omega = v_s k$

    The speed of sound is the same in all directions (isotropy) (1)
    { .annotate }

    1. This is a simplification that is easy to relax when using a computer, but with pen and paper calculations, it's a useful assumption.

    There's a maximum frequency, the Debye frequency $\omega_D$, which is the highest frequency that can be supported by the lattice, such that $N_\mathrm{modes} = 3N_\mathrm{atoms}$(1)
    { .annotate }

    1. We'll learn more about band structure shortly. The idea is that the dispersion relation isn't really linear except for small $k$. The Debye model is a good approximation for small $k$, but as it breaks down for large $k$, we need this fudge to make the theory agree with the law of Dulong and Petit.

!END_ADMONITION

Next we're asked to calculate the heat capacity of the Debye model.

!START_ADMONITION info Show working

    We can start by writing down the total internal energy of the system:(1)
    { .annotate }

    1. This is just the Einstein model's energy at a particular frequency, integrated over all frequencies, weighting the energy contributed by a particular frequency by the number of modes at that frequency.

    $$
    E = \int_0^{\omega_D}  g(\omega) \hbar\omega (n_B(\omega) + 1/2)d\omega
    $$

    Figuring out the density of states for a spherical shell in k-space, we get:

    $$
    E = 3 \left(\frac{L}{2\pi}\right)^3 \int_0^{k_D}  \hbar v_s k (n_B(\omega) + 1/2) d^3 k
    $$

    where we've used our assumption $\omega = v_s k$.
    Now using spherical symmetry, converting to spherical coordinates, and integrating over the angular part, writing the Bose occupation factor out explicitly, and converting everything back to $\omega$, we get:

    $$
    E = 3 \left(\frac{L}{2\pi}\right)^3 \int_0^{\omega_D} 4\pi \left(\frac{\omega}{v_s}\right)^2 \hbar \omega \left(\frac{1}{e^{\beta \hbar \omega} - 1} + \frac{1}{2}\right) d\omega
    $$

    To get the heat capacity, we need to differentiate this with respect to temperature.
    This gets rid of the nasty zero-point energy term, that otherwise would give us a divergence(1) in our internal energy.
    { .annotate }

    1. Absolute energies don't matter, only energy differences, so don't worry about the zero-point energy term!

!END_ADMONITION
!START_ADMONITION success Answer

    $$
    C = \frac{\partial E}{\partial T} = 3 \frac{1}{k_B T^2} \left(\frac{L}{2\pi}\right)^3 \int_0^{\omega_D} 4\pi \left(\frac{\omega}{v_s}\right)^2 (\hbar \omega)^2 \frac{e^{\beta \hbar \omega}}{(e^{\beta \hbar \omega} - 1)^2} d\omega
    $$

!END_ADMONITION
Then we're asked to think about the high and low temperature limits of the heat capacity.

!START_ADMONITION info Show working

    In the low temperature limit, our integrand falls off rapidly as a function of $\omega$.
    This is because our temperature is too low to excite the higher energy modes.
    This means we can approximate $\omega$ as being very large, in which case our integral has an exact solution once non-dimensionalized:

    $$
    C = 9 N k_B \left(\frac{T}{\Theta_D}\right)^3 \int_0^{\infty} \frac{x^4 e^x}{(e^x - 1)^2} dx
    $$

    where $\Theta_D = \hbar \omega_D / k_B$ is the Debye temperature.
    We can then directly integrate this to get the low temperature heat capacity.

    In the high temperature limit, we can Taylor expand some exponentials to get the law of Dulong-Petit.

!END_ADMONITION
!START_ADMONITION success Answer

    The low temperature heat capacity is:
    $C = \frac{12}{5} N k_B \pi^4 \left(\frac{T}{\Theta_D}\right)^3$

    The high temperature heat capacity is:
    $C = 3 R$

!END_ADMONITION
Finally, we're asked to interpret some data.

!START_ADMONITION success Answer

    | T(K) | $C_V$ (J/K/mol) | $\Theta_D$ (K) |
    | ---- | --------------- | -------------- |
    | 0.1  | 8.5e-7          | 132            |
    | 1    | 8.6e-4          | 131            |
    | 5    | 0.12            | 127            |
    | 8    | 0.59            | 119            |
    | 10   | 1.1             | 121            |
    | 15   | 2.8             | 132            |
    | 20   | 6.3             | 135            |

    The key thing to note is that you should only really take the first couple of data points seriously.
    Any higher than that and we'll start to excite higher energy modes, and the Debye model will start to break down.

    Also, note that, since the heat capacity is given per mole, we need to set $N = N_A$.

## Q3: Drude theory

We're first asked to derive the conductivity in the presence of an electric field.

!!! note "On Drude theory"

    Drude theory is little more than dimensional analysis.
    We're applying crude classical logic to try to solve a highly nontrivial quantum mechanical problem.
    There's absolutely no reason why this should work other than by dimensional analysis, so don't take any of the steps too seriously.

    As you might expect, it is correct about as often as it's incorrect.

!START_ADMONITION info Show working

    Start by Taylor expanding the momentum at a time $t + dt$, assuming that there's a probability of scattering $1/\tau$.

    $$
    p(t + dt) = p(t) + dt \frac{dp}{dt} = p(t)\left( 1 - \frac{dt}{\tau} \right) + 0 \times (dt/\tau) + F dt/\tau
    $$

    Where we're assuming that, on average, the electrons scatter to zero momentum.
    Rearranging gives us:

    $$
    \frac{d\vec{p}}{dt} = -\frac{\vec{p}}{\tau} + \vec{F}
    $$

    Now using $\vec{F} = -e\vec{E}$ (ignoring $\vec{B}$ for now), we get:

    $$
    \frac{d\vec{p}}{dt} = -\frac{\vec{p}}{\tau} - e\vec{E}
    $$

    In the steady state, we have $\frac{d\vec{p}}{dt} = 0$, giving:

    $$
    \vec{p} = -\tau e \vec{E}
    $$

    Now write $\vec{p} = m\vec{v}$, and use the definition of current density $\vec{J} = -ne\vec{v}$, to get:

    $$
    \vec{J} = \frac{ne^2\tau}{m} \vec{E}
    $$

    This is the Drude model's conductivity, as the conductivity is defined as $\vec{J} = \sigma \vec{E}$.

!START_ADMONITION success Answer

    $\sigma = \frac{ne^2\tau}{m}$

Then we're asked to find the resistivity matrix in the presence of electric and magnetic fields.

!START_ADMONITION info Show working

    We can start by writing down the equation of motion for the electron in the presence of both fields:

    $$
    m\frac{d\vec{v}}{dt} = -e\vec{E} - e\vec{v} \times \vec{B} - \frac{m\vec{v}}{\tau}
    $$

    Once again, in the steady state, we have $\frac{d\vec{v}}{dt} = 0$, giving:

    $$
    \vec{v} = -\frac{e\tau}{m} \left(\vec{E} + \vec{v} \times \vec{B}\right)
    $$

    Now we just want to turn all of our $\vec{v}$s into $\vec{J}$s.
    We can do this by using the definition of current density $\vec{J} = -ne\vec{v}$.

    $$
    \vec{E} = \frac{1}{ne} \vec{J}\times\vec{B} + \frac{m}{ne^2\tau} \vec{J}
    $$

    Now using the definition of the resistivity as $\vec{E} = \rho \vec{J}$, we find that it's a matrix.

!START_ADMONITION success Answer

    $$
    \rho_{xx} = \rho_{yy} = \rho_{zz} = \frac{m}{ne^2\tau}
    $$

    $$
    \rho_{xy} = -\rho_{yx} = \frac{B}{ne}
    $$

    $$
    \rho = \begin{pmatrix} \rho_{xx} & \rho_{xy} & 0 \\ \rho_{yx} & \rho_{yy} & 0 \\ 0 & 0 & \rho_{zz} \end{pmatrix}
    $$

Now we're tasked to find the conductivity matrix, which we can do by just inverting the resistivity matrix.
It's block diagonal, so it's easy, if algebraic.

!START_ADMONITION success Answer

    TODO: type this.

Now we're asked to define the Hall resistivity, which is the positive off-diagonal element $R_H = \rho_{yx}/B = -1/ne$.

Then we're asked to plug in the numbers for Na. We're told the density is $1 \mathrm{g}/\mathrm{cm}^3$, atomic mass $M = 23u$.

!START_ADMONITION info Show working

    Start by getting the density of atoms in SI, which is.

    $$
    \left(\frac{1\mathrm{g}}{\mathrm{cm}^3}\right)
    \left( 10 \frac{\mathrm{cm}} {\mathrm{m}^3} \right)
    \left( \frac{1 \mathrm{mol}}{23 \mathrm{g}} \right)
    \left( 6.02 \times 10^{23} \frac{\mathrm{atoms}}{\mathrm{mol}} \right)
    = 2.6 \times 10^{28} \mathrm{m}^{-3}
    $$

    As the valence is 1, this is the electron density.

    Now using $\rho = RA/L$, $V =I R$, we have that $V_H = I \rho L/A$.

    Now the only tricky thing to think about is what to provide as the area, and what to provide as the length.
    As we're looking at $\rho_{xy}$, the area is still the cross-sectional area of the wire, but the length $L$ is the cross-sectional length (as that's the direction over which we're measuring a voltage drop).

    If you find this weird to think about, imagine how you expect the Hall voltage to scale as a function of area and length.
    Holding everything but $L$ constant, which direction should $L$ be pointing in so that we get a linear increase in $V_H$ for a linear increase in $L$?
    Similarly, holding everything but $A$ constant, which area should $A$ be pointing in so that we get a linear increase in $V_H$ for a linear decrease in $A$?

    Then we have enough numbers to get to the answer!

!START_ADMONITION success Answer

    $V_H = 4.8 \times 10^{-8} \mathrm{V}$

!!! note "Note on Hall measurements"

    This Voltage is very small.
    Any errors in your experimental setup will lead to measurements that look like:

    $$
    V_\mathrm{meas}(B) = V_H (B) + V_\mathrm{error}
    $$

    Crucially, $V_H$ is a function of magnetic field, so the trick is to measure $V_H$ at both positive and negative magnetic fields.
    You want to measure:

    $$
    V_H = \left[V_\mathrm{meas}(B) - V_\mathrm{meas}(-B)\right]/2
    $$

We're also asked to comment on the properties of metals that Drude theory doesn't explain well.

!START_ADMONITION success Answer

    The answer to this is pretty much everything.
    It's a qualitative theory.
    It rather famously often gets the wrong sign for the Peltier and Seebeck coefficients (this is examinable), but it's pretty terrible for everything else, too.

## Q4: Sommerfeld model

This question starts with some definitions.

!!! quote "Definitions"

    The ***Fermi energy*** is the chemical potential at zero temperature.

    The ***Fermi temperature*** is $T_F = \frac{E_F}{k_B}$.

    The ***Fermi surface*** is the surface in $k$-space where the energy is equal to the Fermi energy. (1)
    { .annotate }

    1. Some other definitions are possible. It's also *the locus of points in $k$-space with $\vec{k} = \vec{k}_F$.*, or *the surface in $k$-space separating filled and empty states*; many other equivalent definitions are possible.

TODO: finish notes here.

!!! note "Notes on this question"

    The number you're after $E_F = 3.2 \mathrm{eV}$ in the calculation.

## Q5: Velocities in the free electron model

## Q6: Physical properties of the free electron gas

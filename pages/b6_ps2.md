<!--  -->

# B6 problem set 2

## Q1: Chemical bonding

### Part a

<blockquote>
Qualitatively describe the five different types of chemical bonds and why they occur.
</blockquote>

Just copy the table out of Steve Simon's "The Oxford Solid State Basics" book.
To avoid _direct_ plagiarism, I won't copy the table here.

### Part b

<blockquote>
Describe qualitatively the phenomenon of Van der Waals forces.
Explain why the force is attractive and proportional to $1/R^7$.
</blockquote>

Van der Waals forces are the attractive forces between molecules.
They are caused by the fluctuating electric fields of the molecules.
We can get the $1/R^7$ dependence without thinking too hard - it's clear from dimensional analysis, so we don't need to remember exact forms of results from electrostatics.

!START_ADMONITION info Show working

In the absence of external forces and fields, we don't expect atoms to be polarized.
If an electric field is applied, they will develop a polarization

$$
\vec{p} = \chi \vec{E},
$$

where $\chi$ is the polarizability.
Now imagine that we have two atoms separated by a distance $R$.
If the first atom develops, for whatever reason, a spontaneous polarization $\vec{p}_1=p_1 \hat{z}$, it will produce a field

$$
E \propto \frac{p_1}{R^3}
$$

at the location of the second atom (remembering, from electrostatics, the [field of a dipole](https://en.wikipedia.org/wiki/Dipole#Field_from_an_electric_dipole)).
The second atom will then develop a polarization $p_2 = \chi E$.
Just thinking about dimensions, the potential energy of this interaction has to be proportional to $p_1 p_2 / R^3$, so that

$$
V \propto \frac{1}{R^6}.
$$

So that the force is proportional to $1/R^7$.

!END_ADMONITION

### Part c

<blockquote>
The ionization energy of a sodium atom is 5.14 eV.
The electron affinity of a chlorine atom is 3.62 eV.
The bond length of a NaCl molecule is 2.36 Å.
Calculate the total energy released when a NaCl molecule is formed.

The actual experimental value is 4.26 eV.
Comment on the sign of your error.

</blockquote>

## Q2: Covalent bonding in detail

I'll write this up if I find the time, as it's the only optional problem on the set.

## Q3: Interatomic potentials

### Part a

<blockquote>

Just thinking qualitatively, we expect the potential energy of a pair of atoms to look something like this:

TODO: inject a Lennard-Jones plotly plot here

This potential can be expanded about its minimum to give

$$
V(x) = \frac{\kappa}{2} (x - x_0)^2 + \frac{\kappa_3}{3!} (x - x_0)^3 + \ldots
$$

The Lennard-Jones potential is one such model with the correct qualitative shape (in fact, it's exactly what I plotted above).
Its functional form is

$$
V(x) = 4 \epsilon \left[ \left(\frac{\sigma}{x}\right)^{12} - \left(\frac{\sigma}{x}\right)^6 \right].
$$

What is the physical meaning of the exponent 6?

</blockquote>

The exponent 6 comes from the fact that the Lennard-Jones potential is used to model Van der Waals interactions.
There are a few interesting things to note here:

- Lennard-Jones is one guy with a double-barrelled surname!
- If we wanted to study interactions in a crystal, we might want to use something like the [Morse potential](https://en.wikipedia.org/wiki/Morse_potential).
- The twelfth power is wrong. It models Pauli repulsion, which has a very different functional form. We keep it because it's extremely easy to square numbers with a computer, and we've already had to calculate the sixth power to get the attractive part of the potential! Really, any power greater than 6 would have worked, and we choose 12 for computational efficiency.

### Part b

<blockquote>

Find $x_0$, $\kappa$, and $\kappa_3$ for the Lennard-Jones potential.

</blockquote>

This is trivial algebra - just Taylor expand the potential and compare coefficients.

TODO: insert answers here

## Q4: Classical model of thermal expansion

<blockquote>

In classical statistical mechanics, the expectation of $x$ is

$$
\langle x \rangle _{\beta} = \frac{\int  x e^{-\beta V(x)} dx}{\int  e^{-\beta V(x)} dx}.
$$

We can't do those integrals with arbitrary $V(x)$, but we could expand the exponentials as

$$
e^{-\beta V(x)} = e^{\frac{\beta \kappa}{2} (x - x_0)^2} \left[ 1 + \frac{\beta \kappa_3}{3!} (x - x_0)^3 + \ldots \right],
$$

and let the limits of integration go to $\pm \infty$.

</blockquote>

### Part a

<blockquote>

Why is this expansion of the exponent and extension of the limits of integration valid?

</blockquote>

The _real_ answer is that we do it because it's the only way to make progress.
You figure out what it means only if your results are interesting!

The answer that the question is probably looking for is that, if $k_B T$ is small, we're going to have a very peaked Boltzmann distribution, and the integrals will be dominated by the region around the minimum of the potential.

I hear you though - sure, that lets us expand the limits and write $V(x) \approx \frac{\kappa}{2} (x - x_0)^2 + \frac{\kappa_3}{3!} (x - x_0)^3 + \ldots$, but then why Taylor expand the exponential on the cubic part, and not the quadratic part?

I'll provide an exact bound on this on the last part of the question, but we're just requiring that the cubic term is appreciably smaller than the quadratic term.

### Part b

<blockquote>

Use this to derive $\langle x \rangle _{\beta}$ and show that the coefficient of thermal expansion is

$$
\alpha = \frac{1}{L} \frac{\partial L}{\partial T} = \frac{1}{x_0} \frac{k_B \kappa_3}{2 \kappa^2}.
$$

</blockquote>

The main trick in this problem is to ignore all the odd integrals, as they're all zero by symmetry.
Then we just have a few Gaussian integrals to keep track of.

TODO: add algebraic details.

### Part c

<blockquote>

In what temperature range is the above expansion valid?

</blockquote>

Ok, now it's time to make the terms and conditions surrounding out approximation a bit more precise.

TODO: add details.

### Part d

<blockquote>

This is valid for a 2-particle system, but not a many atom chain.
Why?
How would you modify the calculation to account for this?

</blockquote>

Well... our potential only has a single distance between two atoms in it!
As a result, we're basically studying the properties of a bunch of non-interacting harmonic oscillators. (okay, anharmonic oscillators because of the cubic term, but you get the idea!)

To properly handle the many-atom chain, we need to account for the fact that the coupled differential equations that show up when we try to solve for the motion of the chain are going to lead to normal modes.
There will be some dispersion relation ($\omega(k)$) that tells us how the normal modes of the chain are going to behave as a function of wavevector $k$.

We can then think about thermally occupying these modes using Bose statistics, and calculate the average expansion of the chain as a function of temperature.

## Q5: Phonons on a one-dimensional chain

### Part a

<blockquote>

- What is meant by a normal mode?
- What is meant by a phonon?
- Explain why phonons obey Bose-Einstein statistics.

</blockquote>

For normal modes, quoting wikipedia:

> A normal mode is a pattern of motion in which all parts of the system move sinusoidally with the same frequency and with a fixed phase relation.

Phonons are quanta of vibration.

Phonons obey Bose-Einstein statistics because there's no reason to limit the number of phonons in a given mode.

### Part b

<blockquote>

Derive the dispersion relation for longitudinal oscillations of a one dimensional chain of N identical atoms of mass $m$, lattice spacing $a$ and spring constant $\kappa$.

</blockquote>

TODO: put algebra here.

### Part c

<blockquote>

- Show that the mode with wavevector $k$ has the same pattern of mass displacements as the mode with wavevector $k + 2 \pi / a$.
- Show that the dispersion relation is periodic in $k$-space (reciprocal space).

How many _different_ normal modes are there?

</blockquote>

TODO: add algebra

### Part d

<blockquote>

- Derive the phase and group velocities and sketch them as a function of $k$.
- What is the sound velocity?
- Show that the sound velocity is given by $v_s = \sqrt(\beta^{-1}/\rho)$, where $\rho$ is the mass density and $\beta$ is the compressibility.

</blockquote>

TODO: add algebra and plotly plots.

### Part e

<blockquote>

Calculate and sketch the density of states per frequency $g(\omega)$.

</blockquote>

TODO: add algebra and plotly plot.

### Part f

<blockquote>

Write an expression for the heat capacity of this chain.
You will get an integral that you can't do analytically.

</blockquote>

TODO: add algebra.

### Part g

<blockquote>

Show that, at high temperature, the law of Dulong and Petit is obeyed.

</blockquote>

TODO: add algebra.

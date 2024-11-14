<!--  -->

# B6 problem set 2

## Q1: Chemical bonding

### Part a

<blockquote>
Qualitatively describe the five different types of chemical bonds and why they occur.
</blockquote>

Just copy the table out of Steve Simon's "The Oxford Solid State Basics" book.
To avoid *direct* plagiarism, I won't copy the table here.

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

at the location of the second atom.
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

!START_ADMONITION info Show working

The coloumb energy of the NaCl molecule is

$$
U_\mathrm{coul} = -\frac{e^2}{4\pi\epsilon_0 R} = -\frac{e^2}{4\pi\epsilon_0 (2.36\, Å)} = 6.09 \, \mathrm{eV}.
$$

The energy released is then

$$
E_\mathrm{affinity} - E_\mathrm{ionization} + U_\mathrm{coul} = 3.62 - 5.14 + 6.09 = 4.58 \, \mathrm{eV}.
$$

This is too big!
There must be a repulsive force, and this repulsive force must be what's stopping the atoms from collapsing into each other.
This would be Pauli repulsion, which is not included in our simple model.

!END_ADMONITION

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

This is just algebra - Taylor expand the potential and compare coefficients.

!START_ADMONITION success Answer

You should find that

$$
x_0 = 2^{\frac{1}{6}}\sigma,
~~~
\kappa = 36 \left( 2^{\frac{2}{3}} \frac{\epsilon}{ \sigma^2} \right),
~~~
\kappa _3 = - 756\sqrt{2} \frac{\epsilon}{\sigma^3}.
$$

!END_ADMONITION

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

The *real* answer is that we do it because it's the only way to make progress.
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

There are two important tricks here:

1. All odd integrals are 0 by symmetry
2. Shift all the integrals by $x_0$

!START_ADMONITION info Show working

Just applying the tricks above leaves us with

$$
\langle x \rangle _{\beta} = \left[\int^\infty_{-\infty} e^{\frac{\beta\kappa}{2} x^2}\left(x_0 + \frac{\beta \kappa_3}{3!} x^4 \right) dx \right]
/
\left[ {\int^\infty_{-\infty} e^{\frac{\beta\kappa}{2} x^2} dx}\right] \, .
$$

Now, evaluating the Gaussian integrals gives

$$
\langle x \rangle _{\beta} = x_0 + \frac{k_3 k_B T}{2 \kappa^2} + \ldots
$$

The coefficient of thermal expansion is then

$$
\alpha = \frac{1}{L} \frac{dL}{dT} = \frac{1}{x_0} \frac{k_B \kappa_3}{2 \kappa^2},
$$

as required.

!END_ADMONITION

### Part c

<blockquote>

In what temperature range is the above expansion valid?

</blockquote>

Ok, now it's time to make the terms and conditions surrounding out approximation a bit more precise.

!START_ADMONITION info Show working

Rewriting our expression by Taylor expanding the cubic term, but not the quadratic term, is reasonable when

!START_LABEL Approximation conditions
$$
\kappa_3 \Delta x \ll \kappa
$$
!END_LABEL

The typical energies that we'll access are on the order of

$$
k_B T = \frac{\kappa}{2}(x - x_0)^2 - \frac{\kappa_3}{3!} (x - x_0)^3 \, .
$$

If the third term is much smaller, as we require for our funky expansion to work, we have

$$
k_B T \approx \frac{\kappa}{2}(x - x_0)^2 = \frac{\kappa}{2} (\Delta x)^2 \, .
$$

Rearranging this gives us typical displacements on the order of

$$
\Delta x \approx \sqrt{\frac{2 k_B T}{\kappa}} \, .
$$

Subbing this back into the
!DROPDOWN_REF "Approximation conditions" "original approximation conditions"
gives us

$$
\kappa_3^2 \frac{k_B T}{\kappa} \ll \kappa^2 \, ,
$$

and then, equivalently,

$$
k_B T \ll \frac{\kappa^3}{\kappa_3^2} \, .
$$

!END_ADMONITION

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

## Q5: Phonons on a one-dimensional monatomic chain

### Part a

<blockquote>

What is meant by a normal mode?
What is meant by a phonon?
Explain why phonons obey Bose-Einstein statistics.

</blockquote>

For normal modes, quoting wikipedia:

*"A normal mode is a pattern of motion in which all parts of the system move sinusoidally with the same frequency and with a fixed phase relation."*

Phonons are quanta of vibration.

Phonons obey Bose-Einstein statistics because there's no reason to limit the number of phonons in a given mode.

### Part b

<blockquote>

Derive the dispersion relation for longitudinal oscillations of a one dimensional chain of N identical atoms of mass $m$, lattice spacing $a$ and spring constant $\kappa$.

</blockquote>

This is bookwork.

!START_ADMONITION success Answer

!START_LABEL 1D monatomic phonon dispersion
$$
\omega = 2 \sqrt{\frac{\kappa}{m}} \left| \, \sin \left( \frac{ka}{2} \right) \right|
$$
!END_LABEL

!END_ADMONITION

### Part c

<blockquote>

Show that the mode with wavevector $k$ has the same pattern of mass displacements as the mode with wavevector $k + 2 \pi / a$.
Show that the dispersion relation is periodic in $k$-space (reciprocal space).

How many *different* normal modes are there?

</blockquote>

The first part is just a matter of plugging in $k + 2 \pi / a$ into the dispersion relation.
It's a trig function...

The second part only requires a small amount of algebra.

!START_ADMONITION info Show working

From periodic boundary conditions, we have

$$
e^{i(\omega t + kna)} = e^{i(\omega t + k(n+N)a)} \, ,
$$

which immediately requires that

$$
e^{i k N a} = 1 \, .
$$

This means that $kNa = 2\pi p$, where $p$ is an integer.
Or, equivalently,

$$
k = \frac{2\pi p}{Na} \, .
$$

This means that the spacing between adjacent $k$ states is

$$
\Delta k = \frac{2\pi}{Na} \, .
$$

Noting that $L = Na$, that means $\Delta k = 2\pi / L$.

We get the number of modes by diving the range of $k$ by the spacing between adjacent $k$ states, so

$$
N = \frac{\mathrm{range}}{\mathrm{spacing}} = \frac{2\pi/a}{2\pi/L} = L/a = N \, .
$$

So... Debye's fudge was correct!

!END_ADMONITION

### Part d

<blockquote>

- Derive the phase and group velocities and sketch them as a function of $k$.
- What is the sound velocity?
- Show that the sound velocity is given by $v_s = \sqrt{\beta^{-1}/\rho}$, where $\rho$ is the mass density and $\beta$ is the compressibility.

</blockquote>

Okay, there are a few small things to show here, so let's get to it.

!START_ADMONITION info Show working

We get the group velocity by differentiating the
!DROPDOWN_REF "1D monatomic phonon dispersion" "dispersion relation"
with respect to $k$:

$$
v_g = \frac{d\omega}{dk} = a \sqrt{\frac{\kappa}{m}} \cos \left( \frac{ka}{2} \right) \mathrm{sgn}(k) \, .
$$

Be careful about differentiating modulus functions!
The sgn function is 1 for positive $k$ and -1 for negative $k$.

The phase velocity is simply

$$
v_p = \frac{\omega}{k} =\frac {2}{k} \sqrt{\frac{\kappa}{m}} \left| \, \sin \left( \frac{ka}{2} \right) \right| \, .
$$

The sound velocity is just the group velocity at $k=0$, so

$$
v_s = a \sqrt{\frac{\kappa}{m}} \, .
$$

To show the final part, we just need an expression for the compressibility.
The compressibility is defined as

!START_LABEL Compressibility
$$
\beta = -\frac{1}{L} \frac{\partial L}{\partial F} \, .
$$
!END_LABEL

We can consider the interatomic distances of atoms in the chain as a function of the force applied:

$$
x(F) = a - \frac{F}{\kappa} \, .
$$

This gives us $L = N x(F)$, which we can differentiate to get

$$
\frac{\partial L}{\partial F} = -\frac{N}{\kappa} \, .
$$

This means that the
!DROPDOWN_REF "Compressibility" "compressibility"
is

$$
\beta = \frac{1}{L} \frac{N}{\kappa} = \frac{1}{\kappa a} \, .
$$

Using the fact that $\rho = m / a$, we finally get

$$
v_s = \sqrt{\frac{1}{\beta \rho}} = a \sqrt{\frac{\kappa}{m}} \, .
$$

!END_ADMONITION

### Part e

<blockquote>

Calculate and sketch the density of states per frequency $g(\omega)$.

</blockquote>

The density of states is

!START_LABEL Density of states
$$
g(\omega) = \frac{dN}{d\omega} = \frac{dN}{dk} \frac{dk}{d\omega}
$$
!END_LABEL

The rest of the problem is just being careful with the algebra, wavevector degeneracy etc. ($+k$ and $-k$ have the same $\omega$, which gives an extra factor of 2).

!START_ADMONITION info Show working

Subbing in the expression for the
!DROPDOWN_REF "1D monatomic phonon dispersion" "dispersion relation"
into the
!DROPDOWN_REF "Density of states" "density of states"
gives

$$
\frac{dN}{dk} \frac{dk}{d\omega}
=
\frac{2 Na}{2\pi a \sqrt{\kappa / m} \cos({ka/2})} = \frac{Na}{2\pi v_g}
$$

This is as a function of $k$, so we just need to use our
!DROPDOWN_REF "1D monatomic phonon dispersion" "dispersion relation"
to swap out $k$ for $\omega$.
Doing this gives

$$
g(\omega) = \frac{N}{\pi\sqrt{\kappa/m - (\omega/2)^2}} \, .
$$

!END_ADMONITION

### Part f

<blockquote>

Write an expression for the heat capacity of this chain.
You will get an integral that you can't do analytically.

</blockquote>

Since the wording of the question is so vague, I'd actually recommend not substituting in the expression for the density of states.

!START_ADMONITION info Show working

!START_LABEL 1D monatomic phonon heat capacity

The internal energy is

$$
U = \int g(\omega) \hbar \omega \left( \frac{1}{e^{\hbar \omega / k_B T} - 1} \right) d\omega \, .
$$

The heat capacity is then just $C = \frac{dU}{dT}$, which we may/may not be able to do depending on the form of $g(\omega)$.

!END_LABEL

!END_ADMONITION

### Part g

<blockquote>

Show that, at high temperature, the law of Dulong and Petit is obeyed.

</blockquote>

We can do this quite easily because we didn't substitute in the expression for the density of states.

!START_ADMONITION info Show working

Using our
!DROPDOWN_REF "1D monatomic phonon heat capacity" "expression for the heat capacity"
we just need to Taylor expand the exponential in the integrand to get

$$
C = \partial _T \int d\omega\, g(\omega) k_B T = N k_B \, .
$$

where we used the fact that $g(\omega) = dN/d\omega$ and we cancelled the $d\omega$ terms ;).

!END_ADMONITION

## Q6: Phonons on a one-dimensional diatomic chain

### Part a

<blockquote>

What's the difference between an acoustic and an optical mode?

</blockquote>

Acoustic modes are modes where adjacent atoms move in phase.
Optical modes are modes where adjacent atoms move out of phase.

### Part b

<blockquote>

Derive the longitudinal dispersion relation $\omega(k)$ for a one-dimensional diatomic chain of atoms of masses $m_1$ and $m_2$, lattice spacing $a$, and spring constant $\kappa$.

</blockquote>

TODO: add algebra.

### Part c

<blockquote>

Determine the frequencies of the acoustic and optical modes at $k=0$, as well as at the Brillouin zone boundary.

Determine the sound velocity.

Show that the group velocity is zero at the Brillouin zone boundary.

Show that the sound velocity is again given by $v_s = \sqrt{\beta^{-1}/\rho}$.

</blockquote>

TODO: add algebra.

### Part d

<blockquote>

Sketch the dispersion in both the reduced and the extended zone scheme.

If there are $N$ unit cells, how many different normal modes are there?

How many branches of excitation are there? In other words, how many excitations are there at each $k$ in the reduced zone scheme?

</blockquote>

TODO: add algebra and plotly plots.

### Part e

<blockquote>

What happens when $m_1 = m_2$?

</blockquote>

The optical modes disappear, as the two atoms are indistinguishable.
The gap between the acoustic and optical modes at the Brillouin zone boundary closes.
The new lattice constant is $a/2$.
We have one mode per $k$, but our Brillouin zone is now twice as big, so the total number of modes is the same (as we haven't gained or lost any degrees of freedom).

## Q7: The tight-binding model

### Part a

<blockquote>

Derive and sketch the dispersion relation for a monatomic one-dimensional chain with hopping integral $-t$, and on-site energy $\epsilon$.

How many different eigenstates are there in the system?

What is the effective mass of the electron near the bottom of the band?

What's the density of states?

If each atom is monovalent, what's the density of states at the Fermi surface?

Estimate the heat capacity at low temperature.

What's the heat capacity if the material is divalent?

What's the spin susceptibility if the material is divalent?

</blockquote>

TODO: add algebra and plotly plots.

### Part b

<blockquote>

Now consider a diatomic system with different on-site energies $\epsilon_A$ and $\epsilon_B$. What's the dispersion relation?

Sketch the dispersion relation in the reduced and extended zone schemes.

What happens when $t$ becomes very small?

What's the effective mass of an electron near the bottom of the lower band?

If each atom is monovalent, is the material a metal or an insulator?

What happens if $\epsilon_A = \epsilon_B$?

</blockquote>

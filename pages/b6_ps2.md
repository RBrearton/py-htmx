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
<blockquote>

Van der Waals forces are the attractive forces between molecules.
They are caused by the fluctuating electric fields of the molecules.
Let's derive the $1/R^7$ dependence.

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
\vec{E}_1 = \frac{p_1}{4\pi\epsilon_0 R^3} \hat{z}
$$

at the location of the second atom (remembering, from electrostatics, the [field of a dipole](https://en.wikipedia.org/wiki/Dipole#Field_from_an_electric_dipole)).
The second atom will then develop a polarization $\vec{p}_2 = \chi \vec{E}_1$.

!END_ADMONITION

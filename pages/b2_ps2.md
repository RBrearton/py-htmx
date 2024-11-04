<!--  -->

# Problem set 2

## Q1: The rotation formula

This is a bizarrely simple question to get things started.

<blockquote>
Consider a vector $\vec{v}$.
A rotation by an angle $\theta$ about an axis defined by a unit vector $\hat{u}$ transforms $\vec{v}$ to $\vec{v}' = R \vec{v}$ where

$$
R(\theta, \hat{u}) = I + (1 - \cos \theta) (\hat{u} \cdot J)^2 +  \hat{u} \cdot J \sin {\theta}
$$

and

$$
\hat{u} \cdot J = \begin{pmatrix} 0 & -u_z & u_y \\ u_z & 0 & -u_x \\ -u_y & u_x & 0 \end{pmatrix}
$$

Show that

$$
\vec{v}' = \vec{v} \cos \theta + (\hat{u} \times \vec{v}) \sin \theta + \hat{u} (\hat{u} \cdot \vec{v}) (1 - \cos \theta)
$$

</blockquote>

START_ADMONITION info Show working

This is very easy, as it just requires a bit of matrix multiplication.

For example, from the definitions that we're given, a tiny bit of algebra yields

$$
(\hat{u} \cdot J) \vec{v} = \hat{u} \times \vec{v},
$$

The larger $(1 - \cos \theta) (\hat{u} \cdot J)^2$ term works out to be

$$
(1 - \cos \theta) (\hat{u} \cdot J)^2 \vec{v} = \begin{pmatrix} - v_x + v_x \cos \theta + u_x (u \cdot \vec{v}) (1 - \cos \theta) \\ - v_y + v_y \cos \theta + u_y (u \cdot \vec{v}) (1 - \cos \theta) \\ - v_z + v_z \cos \theta + u_z (u \cdot \vec{v}) (1 - \cos \theta) \end{pmatrix}
$$

from which the result follows.

END_ADMONITION

## Q2: Arbitrary direction Lorentz boost

<blockquote>

Consider a frame $S$ with origin $O$, and a frame $S'$ with origin $O'$ moving with velocity $\vec{v} = v \hat{n}$ as measured in $S$.
At time $t = 0$ (as measured in $S$), the origins coincide.

The transformation matrix is given by $\Lambda = e^{-\vec{\zeta}\cdot \vec{K}}$ where $\vec{\zeta} = \zeta \hat{n} $ is the boost vector and $\vec{K}$ is the generator of boosts:

$$
K_x = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, ~~~
K_x = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, ~~~
K_x = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}
$$

Show that $\left( \hat{n} \cdot \vec{K} \right)^3 = \hat{n} \cdot \vec{K}$, then show that

$$
\Lambda = I - (\sinh \zeta) \hat{n} \cdot \vec{K} + (\cosh \zeta - 1) \left( \hat{n} \cdot \vec{K} \right)^2
$$

</blockquote>

Let's start by showing that $\left( \hat{n} \cdot \vec{K} \right)^3 = \hat{n} \cdot \vec{K}$.

START_ADMONITION info Show working

You might find the notation $\hat{n} \cdot \vec{K}$ a bit confusing, as $\hat{n}$ is a vector in $\mathbb{R}^3$ and $\vec{K}$ is a vector of matrices.
Simply evaluate the dot product as

$$
n_i K_i = n_x K_x + n_y K_y + n_z K_z
$$

where the $n_i$ are just scalars (the components of $\hat{n}$), and it becomes a linear combination of the $K_i$ matrices.
Then we have:

$$
\hat{n} \cdot \vec{k} = \begin{pmatrix} 0 & n_x & n_y & n_z \\ n_x & 0 & 0 & 0 \\ n_y & 0 & 0 & 0 \\ n_z & 0 & 0 & 0 \end{pmatrix}
$$

END_ADMONITION
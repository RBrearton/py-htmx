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
Then we have

$$
\hat{n} \cdot \vec{k} = \begin{pmatrix} 0 & n_x & n_y & n_z \\ n_x & 0 & 0 & 0 \\ n_y & 0 & 0 & 0 \\ n_z & 0 & 0 & 0 \end{pmatrix}.
$$

Then, remembering that $\hat{n} \cdot \hat{n} = 1$, we have

$$
\left( \hat{n} \cdot \vec{K} \right)^2 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & n_x^2 & n_x n_y & n_x n_z \\ 0 & n_x n_y & n_y^2 & n_y n_z \\ 0 & n_x n_z & n_y n_z & n_z^2 \end{pmatrix}
$$

and, one more time,

$$
\left( \hat{n} \cdot \vec{K} \right)^3 = \begin{pmatrix} 0 & n_x & n_y & n_z \\ n_x & 0 & 0 & 0 \\ n_y & 0 & 0 & 0 \\ n_z & 0 & 0 & 0 \end{pmatrix} = \hat{n} \cdot \vec{K}.
$$

END_ADMONITION

## Q3: Decomposing a Lorentz transformation

<blockquote>

Consider $L$ in $\mathrm{SO}(1, 3)$, meaning that it satisfies $L^T g L = g$ where $g = \mathrm{diag}(-1, 1, 1, 1)$.

Find $L^{-1}$ in terms of $L$.

Show that $L^2_{00} - L^2_{01} - L^2_{02} - L^2_{03} = 1$.

Show that $L_{00}L_{j0} - L_{0k}L_{jk} = 0$ for $j = 1, 2, 3$.

</blockquote>

Let's start by finding the inverse of $L$.

START_ADMONITION info Show working

Let's just start from the definition we're given and make some progress.

$$
L^T g L = g \\
$$

Multiply on the left by the inverse of $g$:

$$
g^{-1} L^T g L = I \\
$$

Multiply on the right by the inverse of $L$:

$$
g^{-1} L^T g = L^{-1} \\
$$

Ok, cool!
We can evaluate this pretty easily, as $g^{-1} = $g$, and we quickly find:

$$
L^{-1} = \begin{pmatrix} L_{00} & -L_{10} & -L_{20} & -L_{30} \\ -L_{01} & L_{11} & L_{21} & L_{31} \\ -L_{02} & L_{12} & L_{22} & L_{32} \\ -L_{03} & L_{13} & L_{23} & L_{33} \end{pmatrix}
$$

END_ADMONITION

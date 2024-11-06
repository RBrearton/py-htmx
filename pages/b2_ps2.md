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

Right, now we can move onto the main part of the question.
This looks a lot like a matrix Taylor expansion.
We should probably just be able to Taylor expand the exponential, and use the result we just derived.

START_ADMONITION info Show working

Using the Taylor expansion of the exponential, we have

$$
\Lambda = e^{-\zeta \hat{n} \cdot \vec{K}} = I - \zeta \hat{n} \cdot \vec{K} + \frac{1}{2!} \zeta^2 \left( \hat{n} \cdot \vec{K} \right)^2 - \frac{1}{3!} \zeta^3 \left( \hat{n} \cdot \vec{K} \right)^3 + \ldots
$$

Ok, so it's pretty clear that there will be two terms that we care about: a $\hat{n} \cdot \vec{K}$ term and a $\left( \hat{n} \cdot \vec{K} \right)^2$ term, as any higher powers of $\hat{n} \cdot \vec{K}$ simplify into one of these two.
Let's apply that, and write down the full Taylor series using these two separate sums:

$$
\Lambda = I + \sum_{n=1}^{\infty} \frac{(-\zeta)^{2n-1}}{(2n-1)!} \left( \hat{n} \cdot \vec{K} \right) + \sum_{n=1}^{\infty} \frac{(-\zeta)^{2n}}{(2n)!} \left( \hat{n} \cdot \vec{K} \right)^2.
$$

... and we have arrived!
The final trick to spot is easy (with it being a show that question) but we're missing the first term in the Taylor expansion of $\cosh$, which is what gives us the $(\cosh \zeta - 1)$ term, so we finally have:

$$
\Lambda = I - (\sinh \zeta) \hat{n} \cdot \vec{K} + (\cosh \zeta - 1) \left( \hat{n} \cdot \vec{K} \right)^2.
$$

as required.

END_ADMONITION

<blockquote>

Given that the trajectory of $O'$ is $\vec{r} = \vec{v}t$ in frame $S$ and $\vec{r}' = 0$ in frame $S'$, where $\vec{r}$ and $\vec{r}'$ are the spatial position vectors, show that $\tanh \zeta = \beta$, where $\beta \equiv \frac{v}{c}$. Using this result, express $\Lambda$ in terms of $\gamma = \left(1 - \beta^2\right)^{-1/2}$ and the components of $\beta$.

</blockquote>

This is just a matter of writing out the matrix form of $\Lambda$ that we just derived, as we were told that this is the transformation matrix for a Lorentz boost.
From there it should just be matrix multiplication.

START_ADMONITION info Show working

Right, so remembering that

$$
\hat{n} \cdot \vec{K} = \begin{pmatrix} 0 & n_x & n_y & n_z \\ n_x & 0 & 0 & 0 \\ n_y & 0 & 0 & 0 \\ n_z & 0 & 0 & 0 \end{pmatrix},
$$

and

$$
\left(\hat{n} \cdot \vec{K}\right)^2 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & n_x^2 & n_x n_y & n_x n_z \\ 0 & n_x n_y & n_y^2 & n_y n_z \\ 0 & n_x n_z & n_y n_z & n_z^2 \end{pmatrix},
$$

<!-- TODO: THIS IS THE PERFECT PLACE FOR A HOVER REFERENCE -->

we can write out the matrix form of $\Lambda$:

$$
\Lambda = \begin{pmatrix} \cosh \zeta & -n_x \sinh \zeta & -n_y \sinh \zeta & -n_z \sinh \zeta \\ -n_x \sinh \zeta & 1 + n_x^2 \left( \cosh \zeta - 1 \right) & n_x n_y \left( \cosh \zeta - 1 \right) & n_x n_z \left( \cosh \zeta - 1 \right) \\ -n_y \sinh \zeta & n_x n_y \left( \cosh \zeta - 1 \right) & 1 + n_y^2 \left( \cosh \zeta - 1 \right) & n_y n_z \left( \cosh \zeta - 1 \right) \\ -n_z \sinh \zeta & n_x n_z \left( \cosh \zeta - 1 \right) & n_y n_z \left( \cosh \zeta - 1 \right) & 1 + n_z^2 \left( \cosh \zeta - 1 \right) \end{pmatrix}.
$$

The Lorentz transformation is $ \vec{x}' = \Lambda \vec{x}$, so full explicit matrix multiplication gives the following expressions for the spatial components of the transformed vector:

$$
x' = - n_x \sinh (\zeta ) c t + \left( 1 + n_x^2 \left( \cosh \zeta  - 1 \right) \right) x + n_x n_y \left( \cosh \zeta  - 1 \right) y + n_x n_z \left( \cosh \zeta  - 1 \right) z,
$$

...and similar expressions for $y'$ and $z'$.
Now we just need to sub in.
From the problem, we have that $x' = 0$ when $x = n_x v t$. <!-- ANOTHER HOVER: this comes from definition of n being parallel to the boost. -->
This gives us

$$
-(\sinh \zeta) c t + (\cosh \zeta - 1) v t = 0,
$$

which simplifies to

$$
\tanh \zeta = \frac{v}{c} = \beta.
$$

END_ADMONITION

That wasn't too bad.
Now we just need to express $\Lambda$ in terms of $\gamma$ and the components of $\beta$, which is easier to write than it is to type...

START_ADMONITION info Show working

It's just a copy-paste exercise really.
We straightforwardly have

$$
n_x = \frac{\beta_x}{\beta}, ~~~ n_y = \frac{\beta_y}{\beta}, ~~~ n_z = \frac{\beta_z}{\beta}.
$$

We can figure out the $\cosh \zeta$ and $\sinh \zeta$ terms from the definitions of $\beta$ and $\gamma$

$$
\tanh \zeta = \frac{\sqrt{\cosh^2{\zeta} - 1}}{\cosh \zeta} = \beta,
$$

which, rearranging, gives

$$
\cosh \zeta = \frac{1}{\sqrt{1 - \beta^2}} = \gamma, ~~~ \sinh \zeta = \frac{\beta}{\sqrt{1 - \beta^2}} = \beta \gamma.
$$

Doing the cut-and-paste of terms gives

$$
\Lambda = \begin{pmatrix} \gamma & -\beta_x \gamma & -\beta_y \gamma & -\beta_z \gamma \\ -\beta_x \gamma & 1 + \beta_x^2 (\gamma - 1) / \beta^2  & \beta_x \beta_y (\gamma - 1) / \beta^2 & \beta_x \beta_z (\gamma - 1) / \beta^2 \\ -\beta_y \gamma & \beta_x \beta_y (\gamma - 1) / \beta^2 & 1 + \beta_y^2 (\gamma - 1) / \beta^2 & \beta_y \beta_z (\gamma - 1) / \beta^2 \\ -\beta_z \gamma & \beta_x \beta_z (\gamma - 1) / \beta^2 & \beta_y \beta_z (\gamma - 1) / \beta^2 & 1 + \beta_z^2 (\gamma - 1) / \beta^2 \end{pmatrix}.
$$

END_ADMONITION

<blockquote>

Show that an arbitrary Lorentz transformation can be derived from a rotation, a boost along a coordinate axis, and then another rotation.

</blockquote>

Using logic, we should be able to write any transformation as

$\Lambda = R(-\theta, \hat{u}) \Lambda_x(v) R(\theta, \hat{u})$.

That starts by rotating the frame so that the boost is along the $x$ axis, then boosting along the $x$ axis, and then rotating back.
We're also reminded in the problem to use the result that we derived in question 1, so this is just a case of working through algebra.

START_ADMONITION info Show working

Ok, first we need to figure out the vector $\hat{u}$ that we need to rotate about, so that we can use the equation from question 1.
We know it has to be orthogonal to both $\hat{x}$ and $\hat{n}$, so it must lie along $\hat{x} \times \hat{n}$.
This gives

$$
\hat{u} = \hat{x} \times \hat{n} = \frac{1}{n_y^2 + n_z^2} ~ \begin{pmatrix} 0 \\ n_z \\ -n_y \end{pmatrix}.
$$

Now subbing into the expression from question 1, $R(\theta, \hat{u}) = I + (1 - \cos \theta) (\hat{u} \cdot J)^2 +  \hat{u} \cdot J \sin {\theta}$, we have

$$
R(\theta, \hat{u}) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & n_x & n_y & n_z \\ 0 & -n_y & 1 - \frac{n_y^2}{1 + n_x} & -\frac{n_y n_z}{1 + n_x} \\ 0 & -n_z & -\frac{n_y n_z}{1 + n_x} & 1 - \frac{n_z^2}{1 + n_x} \end{pmatrix}.
$$

Similarly, when we rotate in the opposite direction, we flip the sign of the $\sin\theta$ term, so

$$
R(-\theta, \hat{u}) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & n_x & -n_y & -n_z \\ 0 & n_y & 1 - \frac{n_y^2}{1 + n_x} & -\frac{n_y n_z}{1 + n_x} \\ 0 & n_z & -\frac{n_y n_z}{1 + n_x} & 1 - \frac{n_z^2}{1 + n_x} \end{pmatrix}.
$$

Note that I've extended the matrix to 4x4, as we're working in 4D spacetime, but the time component is trivial.
The matrix $\Lambda_x(v)$ is given by

$$
\Lambda_x(v) = \begin{pmatrix} \gamma & -\beta \gamma & 0 & 0 \\ -\beta \gamma & \gamma & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix},
$$

Multiplying everything together gives, as expected,

$$
\Lambda = \begin{pmatrix} \gamma & -\beta \gamma n_x & -\beta \gamma n_y & -\beta \gamma n_z \\ -\beta \gamma n_x & 1 + \beta^2 (\gamma - 1) n_x^2 & \beta^2 (\gamma - 1) n_x n_y & \beta^2 (\gamma - 1) n_x n_z \\ -\beta \gamma n_y & \beta^2 (\gamma - 1) n_x n_y & 1 + \beta^2 (\gamma - 1) n_y^2 & \beta^2 (\gamma - 1) n_y n_z \\ -\beta \gamma n_z & \beta^2 (\gamma - 1) n_x n_z & \beta^2 (\gamma - 1) n_y n_z & 1 + \beta^2 (\gamma - 1) n_z^2 \end{pmatrix},
$$

which is the same as what we previously derived, as $n_x = \beta_x / \beta$ and so on.

END_ADMONITION

## Q3: Decomposing a Lorentz transformation

<blockquote>

Consider $L$ in $\mathrm{SO}(1, 3)$, meaning that it satisfies $L^T g L = g$.

Find $L^{-1}$ in terms of $L$.

Show that $L^2_{00} - L^2_{01} - L^2_{02} - L^2_{03} = 1$.

Show that $L_{00}L_{j0} - L_{0k}L_{jk} = 0$ for $j = 1, 2, 3$.

</blockquote>

To solve this, we start by finding the inverse of $L$.
Then, the identities that we're asked to show can be derived by equating the elements of $L L^{-1}$ to the elements of the identity matrix.

START_ADMONITION info Show working

Let's just start from the definition we're given and make some progress.

$$
L^T g L = g
$$

Multiply on the left by the inverse of $g$:

$$
g^{-1} L^T g L = I.
$$

Multiply on the right by the inverse of $L$:

$$
g^{-1} L^T g = L^{-1}.
$$

Ok, cool!
We can evaluate this pretty easily, as $g^{-1} = g$.
Defining $L$ as usual as

$$
L = \begin{pmatrix} L_{00} & L_{01} & L_{02} & L_{03} \\ L_{10} & L_{11} & L_{12} & L_{13} \\ L_{20} & L_{21} & L_{22} & L_{23} \\ L_{30} & L_{31} & L_{32} & L_{33} \end{pmatrix},
$$

we have

$$
L^{-1} = \begin{pmatrix} L_{00} & -L_{10} & -L_{20} & -L_{30} \\ -L_{01} & L_{11} & L_{21} & L_{31} \\ -L_{02} & L_{12} & L_{22} & L_{32} \\ -L_{03} & L_{13} & L_{23} & L_{33} \end{pmatrix}.
$$

Now, just writing out the matrix multiplication for $L L^{-1}$ and equating to the identity matrix gives the results we're looking for:

$$
\begin{pmatrix} L_{00} & L_{01} & L_{02} & L_{03} \\ L_{10} & L_{11} & L_{12} & L_{13} \\ L_{20} & L_{21} & L_{22} & L_{23} \\ L_{30} & L_{31} & L_{32} & L_{33} \end{pmatrix} \begin{pmatrix} L_{00} & -L_{10} & -L_{20} & -L_{30} \\ -L_{01} & L_{11} & L_{21} & L_{31} \\ -L_{02} & L_{12} & L_{22} & L_{32} \\ -L_{03} & L_{13} & L_{23} & L_{33} \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}.
$$

The on-diagonal elements give

$$
L_{00}^2 - L_{01}^2 - L_{02}^2 - L_{03}^2 = 1
$$

and the off-diagonal elements give

$$
L_{00} L_{j0} - \sum_{k=1}^{3} L_{0k} L_{jk} = 0
$$

END_ADMONITION

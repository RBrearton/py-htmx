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

Fun note: since $\hat{u} \cdot J$ is a rank 2 tensor, we know $J$ is a rank 3 tensor.
The above expression gives

$$
u_j J_{ijk} v_k = \epsilon_{ijk} u_j v_k
$$

which means that

$$
\left[\hat{u} \cdot J \right]_{ik} = \epsilon_{ijk} u_j.
$$

Ok, back to the question!

The larger $(1 - \cos \theta) (\hat{u} \cdot J)^2$ term works out to be

$$
(\hat{u} \cdot J)^2 = \begin{pmatrix} 0 & -u_z & u_y \\ u_z & 0 & -u_x \\ -u_y & u_x & 0 \end{pmatrix} \begin{pmatrix} 0 & -u_z & u_y \\ u_z & 0 & -u_x \\ -u_y & u_x & 0 \end{pmatrix} = \begin{pmatrix} -u_z^2 - u_y^2 & u_x u_y & u_x u_z \\ u_x u_y & -u_z^2 - u_x^2 & u_y u_z \\ u_x u_z & u_y u_z & -u_y^2 - u_x^2 \end{pmatrix},
$$

although we could've probably done this more easily using the $\epsilon_{ijk}$ representation of $\hat{u} \cdot J$.
Now also using $u_x^2 + u_y^2 + u_z^2 = 1$, we can rewrite the diagonal terms to get

$$
(\hat{u} \cdot J)^2 = \begin{pmatrix} -1 + u_x^2 & u_x u_y & u_x u_z \\ u_x u_y & -1 + u_y^2 & u_y u_z \\ u_x u_z & u_y u_z & -1 + u_z^2 \end{pmatrix}.
$$

Now, applying this to a vector $\vec{v}$ and pre-multiplying by $(1 - \cos \theta)$ gives

$$
(1 - \cos \theta) (\hat{u} \cdot J)^2 \vec{v} = \begin{pmatrix} - v_x + v_x \cos \theta + u_x (u \cdot \vec{v}) (1 - \cos \theta) \\ - v_y + v_y \cos \theta + u_y (u \cdot \vec{v}) (1 - \cos \theta) \\ - v_z + v_z \cos \theta + u_z (u \cdot \vec{v}) (1 - \cos \theta) \end{pmatrix},
$$

from which the result follows.

END_ADMONITION

## Q2: Arbitrary direction Lorentz boost

### Part a

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

### Part b

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

### Part c

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

### Part a

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

### Part b

<blockquote>

Let $O$ and $O'$ be the origins of $S$ and $S'$, respectively.
Let $\vec{v}$ represent the velocity of $O'$ as measured in $S$.
Let $O$ and $O'$ coincide at $t = 0$.
Show that $\beta_i = -L_{0i}/L_{00}$.
Show that $L_{00} = \gamma$.

</blockquote>

As Lorentz transformations are members of the Lorentz group $\mathrm{SO}(1, 3)$, this is somewhat trivial.

START_ADMONITION info Show working

The vectors for the spacetime coordinates of $O'$ are given by

$$
X = \begin{pmatrix} c t \\ v_x t \\ v_y t \\ v_z t \end{pmatrix}, ~~~ X' = \begin{pmatrix} c t' \\ \vec{0} \end{pmatrix}.
$$

While we could work through $X' = L X$, it's actually way quicker to look at $X = L^{-1} X'$, which we can write out in full as

$$
\begin{pmatrix} c t \\ v_x t \\ v_y t \\ v_z t \end{pmatrix} = \begin{pmatrix} L_{00} & -L_{10} & -L_{20} & -L_{30} \\ -L_{01} & L_{11} & L_{21} & L_{31} \\ -L_{02} & L_{12} & L_{22} & L_{32} \\ -L_{03} & L_{13} & L_{23} & L_{33} \end{pmatrix} \begin{pmatrix} c t' \\ 0 \\ 0 \\ 0 \end{pmatrix}.
$$

From this we read off that $ct = L_{00} c t'$, and that $v_i t = -L_{0i} c t'$.
This gives us the result that $\beta_i = -L_{0i}/L_{00}$.

To show that $L_{00} = \gamma$, we can use the fact that

$$
\beta^2 = \beta_x^2 + \beta_y^2 + \beta_z^2 = \frac{L_{01}^2 + L_{02}^2 + L_{03}^2}{L_{00}^2} = \frac{L_{00}^2 - 1}{L_{00}^2},
$$

where we used the result from the previous question that $L_{00}^2 - L_{01}^2 - L_{02}^2 - L_{03}^2 = 1$.
Now we just need to rearrange to find

$$
L_{00} = \frac{1}{\sqrt{1 - \beta^2}} = \gamma.
$$

END_ADMONITION

### Part c

<blockquote>

Let $\Lambda(\beta)$ denote the Lorentz transformation with velocity $\vec{\beta}c$.
Let $R = L \Lambda^{-1}(\beta) = L \Lambda(-\beta)$.
Show that $R$ belongs to $\mathrm{SO}(1, 3)$.
Using the expression for $\Lambda(\beta)$ in terms of $\gamma$ and $\beta_i$ from the previous question, show that $R_{00} = 1$ and $R_{0i} = 0$ for $i = 1, 2, 3$.

</blockquote>

As $\Lambda(\beta)$ is a Lorentz transformation, it belongs to $\mathrm{SO}(1, 3)$.
The question also tells us that $L$ belongs to $\mathrm{SO}(1, 3)$, so $R$ is a product of two elements of $\mathrm{SO}(1, 3)$, and hence belongs to $\mathrm{SO}(1, 3)$.

The rest is tedious algebra, but nothing complicated.

START_ADMONITION info Show working

Working through it, we have $R_{00} = L_{00} \Lambda_{00}( -\beta) + L_{0k} \Lambda_{k0}(-\beta)$.
From the previous question, we know that $\Lambda_{00}(-\beta) = \gamma$ and $\Lambda_{k0}(-\beta) = \beta_k \gamma$. <!-- HOVER REFERENCE AGAIN -->

Now using that $\beta_k = -L_{0k}/L_{00}$, we have

$$
R_{00} = L_{00} \gamma + L_{0k} \beta_k \gamma = \gamma L_{00} - \gamma \frac{L_{0k}L_{0k}}{L_{00}}  = \gamma L_{00} - \gamma = 1.
$$

Where we used $L^2_{00} - L^2_{01} - L^2_{02} - L^2_{03} = 1$ from the previous part of this question.

Similarly, we have

$$
R_{i0} = L_{i0} \Lambda_{00}(-\beta) + L_{ik} \Lambda_{k0}(-\beta) = L_{i0} \gamma + L_{ik} \beta_k \gamma
$$

Again we can use that $\beta_k = -L_{0k}/L_{00}$ to get

$$
R_{i0} = L_{i0} \gamma - L_{ik} \frac{L_{0k}}{L_{00}} \gamma = 0.
$$

where we used $L_{00}L_{j0} - L_{0k}L_{jk} = 0$ from the previous part of this question.

This is all we need to show!
We've already argued that $R$ belongs to $\mathrm{SO}(1, 3)$, it satisfies the equations that we derived in the first part of the question

$$
(R R^{-1})_{00} = R_{00}^2 - \sum_{i=1}^{3} R_{0i}^2 = 1
$$

which is only true if $R_{0i} = 0$.

END_ADMONITION

<blockquote>

Argue that $R$ represents a rotation.

</blockquote>

The previous part of the problem showed that $R$ leaves time invariant.
As it's in $\mathrm{SO}(1, 3)$, it must also leave $-(c \delta t)^2 + (\delta \vec{x})^2$ invariant.
Therefore, as it doesn't affect time, it must also leave $|\delta \vec{x}|$ invariant, and hence it must be a rotation.

## Q4: SU(2)

### Part a

<blockquote>

SU(2) is the group of unitary 2x2 complex matrices with determinant 1.
Show that the group has 3 generators.

</blockquote>

This is a very standard/easy to google result.

START_ADMONITION info Show working

A general element of SU(2) is

$$
M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

where the complex numbers aren't independent because the determinant must be 1, and the unitarity condition gives $M^\dagger M = I$.
The inverse of the matrix is

$$
M^{-1} = \frac{1}{\det M} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix} = \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}.
$$

Unitarity gives $d = a^*$, $c = -b^*$.
This narrows down the number of independent real parameters to 4.
The determinant condition gives $|a|^2 + |b|^2 = 1$, which is one constraint, dropping the number of independent parameters to 3.

This means that any element of SU(2) can be constructed from 3 independent parameters, so the group has 3 generators.

END_ADMONITION

### Part b

<blockquote>

Let $J_i$ be the generators of SU(2).
$M$ in $\mathrm{SU}(2)$ can be written as $M = I + i z_k J_k$ to first order in some small complex parameters $z_k$.
Show that $K_i = z_i J_i$ are Hermitian.
Express the components of $K_i$ in terms of real numbers, showing that $M = I - i(a_k \sigma_k)$ where the $\sigma_k$ are the Pauli matrices.

</blockquote>

Begin, as suggested, with $z_2 = z_3 = 0$.
Then, generalize to the full case.

START_ADMONITION info Show working

We start with

$$
M = I + i K_1.
$$

Taking the Hermitian conjugate gives

$$
M^\dagger = I - i K_1^\dagger.
$$

Requiring that the matrix is Hermitian gives

$$
(I - i K_1^\dagger)(I + i K_1) = I.
$$

To first order in $z_1$, this implies that $K_1^\dagger = K_1$, so $K_1$ is Hermitian.

Now, trying to figure out the elements of $K_1$, we have

$$
K_1 = \begin{pmatrix} a & b \\ c & d \end{pmatrix}, ~~~ K_1^\dagger = \begin{pmatrix} a^* & c^* \\ b^* & d^* \end{pmatrix}.
$$

Since $K_1$ is hermitian, $a$ and $d$ must be real, and $b = -c^*$.
Expanding the determinant of $M$ to first order gives $1 + i(a + d) = 1$, so $a = -d$.
Writing everything out in terms of real numbers gives

$$
K_1 = a_1 \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} + a_2 \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} + a_3 \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}.
$$

The same results will hold for $K_2$ and $K_3$, but we can see that the real basis vectors are the Pauli matrices, so that

$$
M = I - i(a_k \sigma_k).
$$

Note that, more generally, any matrix in SU(2) can be written as

$$
M = e^{i a_k \sigma_k}
$$

where $a_k$ arbitrary real numbers.

END_ADMONITION

### Part c

<blockquote>

Show that any $2 \times 2$ Hermitian matrix $S$ can be written as $ct I + x_k \sigma_k$.
Calculate the determinant of $S$.
Consider a $2 \times 2$ matrix $L$ such that $\det(L) = 1$, and define the transformation $S' = L S L^\dagger$.
Show that $S'$ is also Hermitian.
Argue that it can be interpreted as representing a new spacetime position vector $X'$ which is a Lorentz transformation of the original spacetime position vector $X = (ct, x, y, z)^\intercal$.

</blockquote>

Quite a few small steps to get through here, but none are too conceptually demanding.

START_ADMONITION info Show working

As $S$ is Hermitian, it can be written as

$$
S = \begin{pmatrix} \alpha & \beta - i\gamma \\ \beta + i\gamma & \delta \end{pmatrix}.
$$

which is of the desired form. Writing that explicitly:

$$
S = \begin{pmatrix} ct + z & x - iy \\ x + iy & ct - z \end{pmatrix}.
$$

The determinant of $S$ is

$$
\det S = (ct + z)(ct - z) - (x - iy)(x + iy) = c^2 t^2 - z^2 - x^2 - y^2.
$$

Now think about $S' = L S L^\dagger$.
We want to prove that $S'$ is Hermitian.
Remember that $(AB)^\dagger = B^\dagger A^\dagger$?
Of course you do.

$$
S'^\dagger = (L S L^\dagger)^\dagger = (L^\dagger)^\dagger S^\dagger L^\dagger = L S L^\dagger = S'.
$$

Because $S'$ is hermitian, it can also be written in the form

$$
S' = \begin{pmatrix} c't + z' & x' - iy' \\ x' + iy' & c't - z' \end{pmatrix}.
$$

with determinant

$$
\det S' = c'^2 t^2 - z'^2 - x'^2 - y'^2.
$$

We can go one step further though, because we're told that $\det (L) = 1$.
This means that $\det(S') = \det(L) \det(S) \det(L^\dagger) = \det(S)$, where I used the fact (that you of course remember) that $\det(A B) = \det(A) \det(B)$.
This means that

$$
c'^2 t^2 - z'^2 - x'^2 - y'^2 = c^2 t^2 - z^2 - x^2 - y^2,
$$

which is a defining property of Lorentz transformations.

END_ADMONITION

### Part d

<blockquote>

Assume that $L$ is of the form

$$
L = \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix},
$$

where $a$ and $b$ are real.
Argue that $LSL^\dagger$ represents a boost along the $z$-axis.
Demonstrate that $L = (\cosh q) I + (\sinh q) \sigma_3$, where $q$ is the rapidity.

</blockquote>

God these are getting boring.
More brainless algebra.

START_ADMONITION info Show working

$$
S' = LSL^\dagger = \begin{pmatrix} a^2 (ct + z) & x - iy \\ x + iy & b^2 (ct - z) \end{pmatrix}.
$$

This is a boost along the $z$-axis, as the off-diagonal elements are the same as the original matrix.
Disentangling $z$ and $ct$ gives

$$
ct' = \frac{a^2 + b^2}{2}ct + \frac{a^2 - b^2}{2}z, ~~~ z' = \frac{a^2 - b^2}{2}ct + \frac{a^2 + b^2}{2}z.
$$

Using our knowledge of relativity

$$
ct' = \gamma (ct - \beta z), ~~~ z' = \gamma (z - \beta ct),
$$

we can match coefficients to find that

$$
\gamma = \frac{a^2 + b^2}{2}, ~~~ -\beta\gamma = \frac{a^2 - b^2}{2}.
$$

To squeeze the rapidity into things, we can use the $det(L) = 1$ condition to find that $ab = 1$ and therefore if $a = e^{q/2}$ then $b = e^{-q/2}$.
This allows us to represent $L$ as

$$
L = \begin{pmatrix} e^{q/2} & 0 \\ 0 & e^{-q/2} \end{pmatrix} = (\cosh q) I + (\sinh q) \sigma_3.
$$

as required.

END_ADMONITION

### Part e

<blockquote>

Now let's think about pure rotations.
The time coordinate must remain unchanged, so think about $S = x_k \sigma_k$.
Show that $\mathrm{tr}(S') = \mathrm{tr}(S) = 0$ implies that $L$ is unitary.
This means $L$ can be written as

$$
L = e^{i a_k \sigma_k}.
$$

where the $a_k$ are real.
Consider $a_1 = a_2 = 0$ and $a_3 = \theta$.
Show that

$$
L(0, 0, \theta) = e^{i \theta \sigma_3} = \begin{pmatrix} e^{-i \theta} & 0 \\ 0 & e^{i \theta} \end{pmatrix}.
$$

Which rotation does $L(0, 0, \theta) S L^\dagger(0, 0, \theta)$ represent?
Is there another element of SU(2) that represents the same rotation?

</blockquote>

Wow that's a lot of questions.

START_ADMONITION info Show working

Since rotations don't mix space and time coordinates, instead of writing

$$
S = ct I + x_k \sigma_k,
$$

we can write

$$
S = x_k \sigma_k,
$$

which is transformed into $S' = x_k' \sigma_k$.

Since the Pauli are traceless, again using $\mathrm{tr} (AB) = \mathrm{tr} (BA)$, we have

$$
\mathrm{tr} (S') = \mathrm{tr} (LSL^\dagger) = \mathrm{tr} (L^\dagger L S) = \mathrm{tr} (S) = 0.
$$

Let $a_{ij}$ denote the components of $L^\dagger L$. We have:

$$
\mathrm{tr} \left( L^\dagger L S \right) = (a_{00} - a_{11}) x + (a_{01} + a_{10}) x + i (a_{01} - a_{10}) y.
$$

For this to be zero for all values of $x$, $y$, and $z$, we require

$$
a_{01} = a_{10} = 0, ~~~ a_{00} = a_{11}
$$

which means $L^\dagger L = a_{00} I$.

Also, since $\det(L) = 1$, we have $a_{00} = 1$, which gives $L^\dagger L = I$.

Similarly, considering

$$
\mathrm{tr}(S) = \mathrm{tr} \left( L^{-1} S' \left( L^{\dagger} \right)^{-1} \right) = \mathrm{tr} \left( \left( L^{\dagger} \right)^{-1} L^{-1} S' \right) = 0,
$$

we find that

$$
\left( L^\dagger \right)^{-1} L^{-1} = \left( L L^\dagger \right)^{-1} = I,
$$

implying $L L^\dagger = I$. Hence, $L$ is unitary.
As shown in part (b), this means that:

$$
L = e^{-i (a_1 \sigma_1 + a_2 \sigma_2 + a_3 \sigma_3)},
$$

where the $a_i$ are real.

For the case $a_1 = a_2 = 0$ and $a_3 = \theta$, we have:

$$
L(0, 0, \theta) = e^{-i \theta \sigma_3} = \sum_{k=0}^{\infty} \frac{(-i \theta \sigma_3)^k}{k!}.
$$

Since $\sigma_3^2 = I$, we have $\sigma_3^{2k} = I$ and $\sigma_3^{2k+1} = \sigma_3$ for all $k$. This yields:

$$
L = I \sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k}}{(2k)!} - i \sigma_3 \sum_{k=0}^{\infty} \frac{(-1)^k \theta^{2k+1}}{(2k+1)!} = I \cos \theta - i \sigma_3 \sin \theta.
$$

In matrix form, this becomes:

$$
L(0, 0, \theta) = \begin{pmatrix} \cos \theta - i \sin \theta & 0 \\ 0 & \cos \theta + i \sin \theta \end{pmatrix} = \begin{pmatrix} e^{-i \theta} & 0 \\ 0 & e^{i \theta} \end{pmatrix}.
$$

Now, calculating $S' = L S L^{\dagger}$ gives the transformed components

$$
z' = z, ~~~ x' = x \cos (2 \theta) - y \sin (2 \theta), ~~~ y' = x \sin (2 \theta) + y \cos (2 \theta).
$$

This represents a rotation by an angle $2 \theta$ around the $z$-axis.
Therefore, there is a correspondence $L (0, 0, \theta) \to R (0, 0, 2 \theta)$, where $R$ is a rotation matrix in $\mathrm{SO}(3)$.

Note that $-L = L(0, 0, \theta + \pi)$ corresponds to the same rotation in $\mathrm{SO}(3)$, since $R(0, 0, 2 (\theta + \pi)) = R(0, 0, 2 \theta)$. This is consistent with $L S L^{\dagger} = (-L) S (-L)^{\dagger}$.
Therefore, there is a two-to-one correspondence between $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$.
For this reason, $\mathrm{SU}(2)$ is called the double cover of $\mathrm{SO}(3)$.

END_ADMONITION

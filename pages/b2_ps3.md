<!--  -->

# B2 problem set 3

## Q1: Evaluation of derivatives for a four-vector field

This question is all about practicing taking derivatives of a four-vector.
We're told that $F^\mu$ is given by

!START_LABEL Q1 field
$$
F^\mu = 2X^\mu + K^\mu (X^\nu X_\nu)
$$
!END_LABEL

where $K^\mu$ is a constant four-vector, and

$$
X^\mu = \left( ct,\, X,\, y,\, z\right)
$$

is the spacetime position four-vector.
Evaluate the following:

### Part a

<blockquote>
$$
\partial_\lambda X^\lambda
$$
</blockquote>

This is the divergence of the position four-vector.

!START_ADMONITION success Answer

$$
\partial_\lambda X^\lambda = 4
$$

!END_ADMONITION

### Part b

<blockquote>
$$
\partial^\mu (X_\lambda X^\lambda)
$$
</blockquote>

This one requires a bit more working.

!START_ADMONITION info Show working

We can start by applying the product rule.

$$
\partial^\mu (X_\lambda X^\lambda) = X_\lambda \partial^\mu X^\lambda + X^\lambda \partial^\mu X_\lambda
$$

The term $X^\lambda \partial^\mu X_\lambda$ just gives us

$$
X^\lambda \partial^\mu X_\lambda =  X^\lambda \delta^\mu_\lambda = X^\mu \, ,
$$

which is easy enough.
We can reuse this trick by inserting the metric tensor into the other term and using the product rule, as follows:

$$
X_\lambda \partial^\mu X^\lambda
=
X_\lambda \left( \partial^\mu g^{\lambda \nu} X_\nu \right)
=
X_\lambda g^{\lambda \mu}
=
X^\mu \, .
$$

This means that, overall, we have

!START_LABEL Gradient of the dot product
$$
\partial^\mu (X_\lambda X^\lambda) = 2X^\mu \, .
$$
!END_LABEL

!END_ADMONITION

### Part c

<blockquote>
$$
\partial^\mu \partial_\mu X^\nu X_\nu
$$
</blockquote>

We can use the
!DROPDOWN_REF "Gradient of the dot product" "dot product gradient rule"
that we just derived to make this quite trivial.

!START_ADMONITION success Answer

$$
\partial^\mu \partial_\mu X^\nu X_\nu
=
\partial_\mu \left[
    \partial^\mu \left(
        X^\nu X_\nu
    \right)
\right]
=
\partial_\mu \left(
    2X^\mu
\right)
=
8
$$

!END_ADMONITION

### Part d

<blockquote>
$$
\partial^\mu X^\nu
$$
</blockquote>

Once again, we're going to insert the metric tensor to get this one quite easily.

!START_ADMONITION success Answer

$$
\partial^\mu X^\nu = g^{\mu \lambda} \partial_\lambda X^\nu = g^{\mu \nu}
$$

!END_ADMONITION

### Part e

<blockquote>
$$
\partial_\lambda F^\lambda
$$
</blockquote>

Subbing in the expression for the
!DROPDOWN_REF "Q1 field" "four-vector field"
and once again using the
!DROPDOWN_REF "Gradient of the dot product" "gradient of the dot product"
we get

!START_ADMONITION success Answer

$$
\partial_\lambda F^\lambda
=
2 \partial_\lambda X^\lambda + K^\lambda \partial_\lambda (X^\nu X_\nu)
=
8 + 2K^\lambda X_\lambda
$$

!END_ADMONITION

### Part f

<blockquote>
$$
\partial^\mu \partial_\mu \sin \left( K_\lambda X^\lambda \right)
$$
</blockquote>

This one is a bit more tricky, but we've built up the tools we need to tackle it.

!START_ADMONITION info Show working

Let's start by applying the chain rule to the sine function, using only the first derivative.

$$
\partial^\mu \partial_\mu \sin \left( K_\lambda X^\lambda \right)
=
\partial^\mu \left[ \partial_\mu \left( K_\lambda X^\lambda \right) \cos \left( K_\lambda X^\lambda \right) \right]
$$

Now we finish taking the chain rule using the fact that $\partial_\mu X^\lambda = \delta^\lambda_\mu$.

$$
\partial^\mu \left[ \partial_\mu \left( K_\lambda X^\lambda \right) \cos \left( K_\lambda X^\lambda \right) \right]
=
\partial^\mu \left[ K_\mu \cos \left( K_\lambda X^\lambda \right) \right]
$$

That's the first derivative applied!
Now let's do it again.

$$
\partial^\mu \left[ K_\mu \cos \left( K_\lambda X^\lambda \right) \right]
=
-K_\mu \partial^\mu \left( K_\lambda X^\lambda \right) \sin \left( K_\lambda X^\lambda \right)
$$

Now we need to be a bit careful, because both indices are raised, so we need another metric tensor to lower coordinate $X$.

$$
-K_\mu \partial^\mu \left( K_\lambda X^\lambda \right) \sin \left( K_\lambda X^\lambda \right)
=
-K_\mu \partial^\mu \left( K_\lambda g^{\lambda \nu} X_\nu \right) \sin \left( K_\lambda X^\lambda \right)
=
-K_\mu K_\lambda g^{\lambda \mu} \sin \left( K_\lambda X^\lambda \right)
$$

And we made it!
Now we just apply the metric tensor to one of the $K$ vectors to get the final answer.

$$
\partial^\mu \partial_\mu \sin \left( K_\lambda X^\lambda \right)
=
-K_\mu K^\mu \sin \left( K_\lambda X^\lambda \right).
$$

!END_ADMONITION

## Q2: Properties of spacetime intervals

This provides a bit of a break from all of that algebra!

We're initially reminded that intervals are timelike when $A^\mu A_\mu > 0$, spacelike when $A^\mu A_\mu < 0$, and null when $A^\mu A_\mu = 0$.

### Part a

<blockquote>
Show that any timelike 4-vector $A^\mu$ can be associated with a straight wordline of constant velocity.
Then prove that, for any timelike 4-vector, there exists a frame in which its spatial component is zero.
</blockquote>

This gets you thinking about the physical interpretation of spacetime intervals.

!START_ADMONITION info Show working

Let $A^\mu A_\mu = -(A^0)^2 + \left(\vec{A}\right)^2 > 0$.

In some frame, define two events $B$ and $C$ such that

$$
\vec{x_B} - \vec{x_C} = \vec{A} \,, ~~~ c(t_C - t_B) = A^0 \,.
$$

The velocity given by

$$
\vec{v} = \frac{d\vec{A}}{dt}\,
$$

has a magnitude that is less than $c$ by construction of the fact that the interval is timelike.
This means that the worldline is straight and represents a constant velocity of a particle traveling between $B$ and $C$.

To make the spatial component zero, just boost to the frame where the velocity is zero.

!END_ADMONITION

### Part b

<blockquote>
Show that there exists a reference frame in which two events are simultaneous if and only if they are separated by a spacelike interval.
</blockquote>

!START_ADMONITION info Show working

If two events are simultaneous in some frame $S$, then the displacement 4-vector between them is

$$
\Delta X^\mu = \left( 0, \Delta \vec{X} \right) \,.
$$

Evaluating the interval gives

$$
\Delta X^\mu \Delta X_\mu = \Delta \vec{X}^2 > 0 \,.
$$

Because Lorentz transformations preserve the value of the interval, the interval must be spacelike in all frames.

!END_ADMONITION

### Part c

<blockquote>

Lie theory yields only proper Lorentz transformations, which preserve the orientation of both time and space, as these transformations are continuously connected to the identity.
Lorentz transformations that do not satisfy these conditions are called improper.

Consider a timelike interval separating two events.
Show that for the temporal order of these two events to remain the same in all reference frames, $\Lambda^0_0$ must be positive for Lorentz transformations between specific frames (a necessary condition for the transformation to be proper).
Then, prove the converse: if the temporal order of two events is the same in all reference frames, they must be separated by a timelike interval.

</blockquote>

!START_ADMONITION info Show working

Consider a timelike interval $\Delta s^2 < 0$.
We've already argued that, in this case, we can find a frame in which the two events occur at the same spatial position.

Let $A$ be the event that occurs first in that frame, so that

$$
\Delta \tau = \tau_B - \tau_A > 0 \,.
$$

In this frame, the displacement 4-vector is

$$
\Delta X^\mu = \left( c \Delta \tau, 0 \right) \,.
$$

Now, consider a Lorentz transformation to another frame $S'$.
The time component in $S'$ is

$$
c\Delta t' = \Lambda^0_0 c\Delta \tau \,.
$$

This means that, for the temporal order to be preserved, we require $\Lambda^0_0 > 0$.

On the flip side, if the temporal order is preserved in all frames, then there's no frame in which $\Delta t' = 0$.
As we've already shown, the condition $\Delta t' = 0$ is equivalent to the interval being spacelike.
Therefore, if $\Delta t > 0$ in all frames, the interval must be timelike.

!END_ADMONITION

### Part d

<blockquote>
Show that any 4-vector orthogonal to a timelike 4-vector is spacelike.
</blockquote>

!START_ADMONITION info Show working

For a timelike 4-vector, there's a frame $S$ in which this vector is

$$
A^\mu = \left( A^0, 0 \right) \,.
$$

Now if we have some $B^\mu$ satisfying $A^\mu B_\mu = 0$, then, by the invariance of the scalar product, the 4-vectors are orthogonal in all frames.
In $S$, this means that

$$
B^\mu = \left( 0, \vec{B} \right) \,.
$$

which is only possible if $B^\mu$ is spacelike.

!END_ADMONITION

### Part e

<blockquote>
Show that, with one exception, any 4-vector orthogonal to a null 4-vector is spacelike.
</blockquote>

!START_ADMONITION info Show working

Let's say that we have a null 4-vector $A^\mu$, satisfying

$$
A^\mu A_\mu = -A^0 A^0 + \vec{A}^2 = 0 \,.
$$

This implies that $A^0 = \pm | \vec{A} |$.
Now let's define the orthogonal 4-vector $B^\mu$ such that

$$
A^\mu B_\mu = -A^0 B^0 + \vec{A} \cdot \vec{B} = 0 \,.
$$

Writing this out in terms of trig, we get

$$
A^0 B^0 = A B \cos \theta \,,
$$

where $\theta$ is the angle between the spatial components of the two vectors.
Subbing in the relationship between $A^0$ and $|\vec{A}|$ gives

$$
b^0 = \pm b \cos \theta \,.
$$

This means that

$$
B^\mu B_\mu = -B^0 B^0 + \vec{B}^2 = B^2 \left( 1 - \cos^2 \theta \right) \geq 0 \, .
$$

This means that $B^\mu$ is spacelike, except in the case where $\theta \in \{ 0\,, ~\pi \}$ and $B$ is also null.

!END_ADMONITION

### Part f

<blockquote>
Prove that, if the displacement 4-vector between two events is orthogonal to the worldline of an observer, then the events are simultaneous in the rest frame of the observer.
</blockquote>

!START_ADMONITION info Show working

The invariance of the inner product means that, if the displacement 4-vector is orthogonal in one frame, it is orthogonal in all frames.

In the rest frame of the observer, the observer's worldline is

$$
U^\mu = \left( c, 0 \right) \,.
$$

For a displacement 4-vector $\Delta X^\mu$ to be orthogonal to this, it must not have a time component.
This means that the events are simultaneous in the observer's rest frame.

!END_ADMONITION

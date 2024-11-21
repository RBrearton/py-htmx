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

## Q3: Motion under a constant force

Consider a particle of mass $m$ and charge $q$ moving in a constant electric field $\vec{E}$ in an intertial frame $S$.

### Part a

<blockquote>

Align the $x$-axis with the direction of $\vec{E}$.
Assume that the particle starts from rest.
Show that

!START_LABEL Position velocity relation
$$
\left(x + \frac{c^2}{\alpha}\right)^2 - c^2 t^2 = \frac{c^4}{\alpha^2},
$$
!END_LABEL

where $\alpha = qE_x /m$.
</blockquote>

Right, so this is all about using a relativistic equivalent of Newton's second law.

!START_ADMONITION info Show working

The momentum of the particle is

$$
\vec{p} = \gamma(v) m \vec{v}.
$$

Newton's second law gives

$$
\frac{d\vec{p}}{dt} = \frac{d}{dt} \left( \gamma m \vec{v} \right) = q\vec{E},
$$

so we just need to integrate this a couple of times to get the result.
Integrating the first time gives

$$
\frac{v}{\sqrt{1 - \frac{v^2}{c^2}}} = \alpha t \, ,
$$

where we've stopped paying attention to whether anything is a vector because it's a one-dimensional problem.
Rearranging to make $v$ the subject,

!START_LABEL Velocity
$$
v = \frac{\alpha t}{\sqrt{1 + \left( \frac{\alpha t}{c} \right)^2}} \, .
$$
!END_LABEL

Rather sensibly, this also tells us that

$$
\lim_{t \to \infty} v = c \, .
$$

Integrating gives

$$
x = \int^t_0 \frac{\alpha t'}{\sqrt{1 + \left( \frac{\alpha t'}{c} \right)^2}} dt'
=
\frac{c^2}{\alpha} \sqrt{1 + \left( \frac{\alpha t}{c} \right)^2} - \frac{c^2}{\alpha} \, ,
$$

by inspection (and then plugging in the numbers for the definite integral).

This is the equation of a hyperbola, which is what we were after:

$$
\left(x + \frac{c^2}{\alpha}\right)^2 - c^2 t^2 = \frac{c^4}{\alpha^2} \, .
$$

!END_ADMONITION

### Part b

<blockquote>
Calculate the acceleration of the particle in $S$;
show that $\alpha$ is the proper acceleration.
</blockquote>

Note that, to avoid complications relating to magnetic fields, we only think about the frame $S$ in which there's no magnetic field, and the frame $S_t$ in which the particle is at rest.

!START_ADMONITION info Show working

In $S$, the acceleration is $dv/dt$.
Using the
!DROPDOWN_REF "Velocity" "velocity"
we derived earlier, we can differentiate to get

$$
\frac{dv}{dt} = \frac{\alpha}{\left(
    1 + \left( \frac{\alpha t}{c} \right)^2
\right)^{3/2}} \, .
$$

Denote $\vec{f} = m\vec{a}$.
Let $F^\mu$ be the four-force acting on the particle, as measured in $S$.
Boosting into the instantaneous rest frame $S_t$ of the particle, we have

$$
F^\mu = \left(
    \gamma(v) \frac{1}{c} \frac{dE}{dt}, \, \gamma(v) \vec{f}
\right)
\, , ~~~
F^\mu_0 = \left(
    \frac{1}{c} \frac{dE}{dt}, \, \vec{f}_0
\right) \, .
$$

where $E$ is the energy of the particle, and $f_0$ is the proper force.
Since $m$ is constant, we can write

$$
\frac{dE}{dt} = \vec{f}\cdot \vec{v} = fv
$$

and, in frame $S_t$, we have

$$
\frac{dE}{d\tau} = c^2 \frac{dm}{d\tau} = 0 \, .
$$

Subbing these back in, we find

$$
F^\mu = \left(
    \gamma(v) \frac{fv}{c} , \, \gamma(v) \vec{f}
\right)
\, , ~~~
F^\mu_0 = \left(
    0, \, \vec{f}_0
\right) \, .
$$

Using $F^\mu_0 = \Gamma_v F^\mu$, where $\Gamma_v$ is the Lorentz transformation matrix from $S$ to $S_t$, we find

$$
f_{0x} = - \gamma_v^2 \frac{v^2}{c^2}f + \gamma_v^2 f = f\, , ~~~ f_{0y} = f_{0z} = 0 \, .
$$

As the force is nothing but $q E_x$, that means $a = qE_x/m = \alpha$, as required.

!END_ADMONITION

### Part c

<blockquote>

The diagram shows the worldline of the particle in $S$.
Let $A(-c^2/\alpha, 0)$ be the intersection of the $x$-axis and the asymptote of the hyperbola $ct = x + c^2/\alpha$.

Let $S_t$  denote the instantaneous rest frame of the particle when it is at a point $P(x, ct)$ along its trajectory. Calculate the coordinates $ct_A′$ and $ct′_P$ of events $A$ and $P$ in frame $S_t$.

Verify that the result is consistent with the slope of the line $AP$ being $v(t)/c$, indicating that $AP$ is a line of simultaneity in the instantaneous rest frame.

</blockquote>

!START_ADMONITION info Show working

The velocity of $S_t$ relative to $S$ is the equation for the
!DROPDOWN_REF "Velocity" "velocity"
we derived earlier, with a Lorentz factor

!START_LABEL Lorentz factor
$$
\gamma_t = \sqrt{1 + \alpha^2 t^2/c^2} \, .
$$
!END_LABEL

Then we can compute directly the coordinates in frame $S_t$:

$$
ct'_A = \gamma_t \left( ct_A - \frac{v}{c} x_A \right) \, ,
$$

$$
ct'_P = \gamma_t \left( ct_P - \frac{v}{c} x_P \right) \, .
$$

where we used the fact that point $P$ is on the hyperbola, so $ct' = ct'_P$ etc.
Now we just need to use the fact that, in frame $S$, the coordinate of $A$ is

$$
A = \left( 0, -\frac{c^2}{\alpha} \right) \, ,
$$

so that

$$
ct'_A = \gamma_t \frac{v(t) c}{\alpha} \, .
$$

Then we can use our expression for the
!DROPDOWN_REF "Velocity" "velocity"
to find

$$
ct'_A = ct \, .
$$

Similarly, albeit with a bit more algebra, we can find

$$
ct'_P = ct \, ,
$$

although to do this we need to use

$$
P = \left( ct, x \right) \, ,
$$

as $P$ is the position of the accelerating particle at time $t$, as well as the
!DROPDOWN_REF "Position velocity relation" "position velocity relation"
we derived in part a.

As the times of $A$ and $P$ are the same, the line $AP$ is a line of simultaneity in the instantaneous rest frame.

Next, to calculate the slope of the line $AP$, we first find the differences between positions

!START_LABEL Position difference
$$
x - x_A = x + \frac{c^2}{\alpha}
=
\sqrt{
    c^2 t^2 + \frac{c^4}{\alpha^2}
}\, ,
$$
!END_LABEL

so that the slope is

!START_LABEL Slope of AP
$$
\frac{ct - ct_A}{x - x_A} = \frac{ct}{\sqrt{c^2 t^2 + \frac{c^4}{\alpha^2}}}
=
\frac{\alpha t}{c\sqrt{1 + \frac{\alpha^2 t^2}{c^2}}}
=
\frac{v(t)}{c} \, ,
$$
!END_LABEL

as required.

!END_ADMONITION

### Part d

<blockquote>
Calculate the distance between $P$ and $A$ in frame $S_t$.
</blockquote>

!START_ADMONITION info Show working

The distance between them is given by

$$
x' - x'_A = \gamma\left[
    x - x_A - \frac{v}{c} \left( ct - ct_A \right)
\right] \, ,
$$

but now we can replace the $ct - ct_A$ part with $v(t)/c$ using the
!DROPDOWN_REF "Slope of AP" "slope of $AP$"
we just calculated, giving

$$
x' - x'_A = \gamma \left( 1 - \frac{v^2}{c^2} \right)(x - x_A)
=
\frac{x - x_A}{\gamma_t}
$$

Now if we use the expression for the
!DROPDOWN_REF "Lorentz factor" "lorentz factor"
we derived earlier, and also use the
!DROPDOWN_REF "Position difference" "position difference"
we used in the previous problem, we find

$$
x' - x'_A = \frac{c^2}{\alpha} \, .
$$

This is actually a really cool and bizarre result.
Even though the particle is accelerating away from $A$ in frame $S$, according to the particle, its distance to $A$ is constant!

This is because lengths are contracting in the direction of motion in the instantaneous rest frame of the particle.
As it gets further away from $A$ in $S$, lengths contract in $S_t$ by exactly the right amount to keep the distance constant.

!END_ADMONITION

## Q4: Circular motion in a magnetic field

We're asked to consider a particle of mass $m$ and charge $q$ moving in a constant magnetic field $\vec{B}$ in an inertial frame $S$, and to neglect radiation effects.

### Part a

<blockquote>
Show that the energy $E$ of the particle, its Lorentz factor $\gamma_v$, and the magnitude of its momentum $p$ are conserved.
</blockquote>

!START_ADMONITION info Show working

For the Lorentz force, $\vec{f} = q\vec{v} \times \vec{B}$, the orthogonality of $\vec{v}$ and $\vec{F}$ gives

$$
\frac{dE}{dt} = \vec{f} \cdot \vec{v} = 0 \, .
$$

This means that

$$
E = \gamma_v m c^2 = \mathrm{constant} \, ,
$$

which is possible only if $\gamma_v$ is also constant.
This means then that the momentum must be constant, as

$$
E^2 = p^2 c^2 + m^2 c^4 \, .
$$

!END_ADMONITION

### Part b

<blockquote>
Show that, in a plane perpendicular to $\vec{B}$, the particle moves in a circle and calculate its angular frequency $\omega$.
Find its radius $r$ in terms of the momentum of the particle.
</blockquote>

!START_ADMONITION info Show working

The equation of motion is

$$
\frac{d\vec{p}}{dt} = \gamma_v m \frac{d\vec{v}}{dt} = q\vec{v} \times \vec{B} \, .
$$

From here it's basically just classical mechanics, because $\gamma_v$ is constant.
Using the usual trick of aligning the field $\vec{B}$ with the $z$-axis without loss of generality, we can write

$$
\frac{dv_x}{dt} = \frac{qB}{\gamma_v m} v_y \, , ~~~ \frac{dv_y}{dt} = -\frac{qB}{\gamma_v m} v_x \, .
$$

Guessing that $v_x = A \sin \omega t$ and $v_y = A \cos \omega t$, we can find

!START_LABEL Cyclotron frequency
$$
\omega = \frac{qB}{\gamma_v m} \, .
$$
!END_LABEL

The momentum is $p = \sqrt{p_\perp^2 + p_z^2}$, where $\vec{p}_\perp$ is the component of $\vec{p}$ in the plane perpendicular to $\vec{B}$.
We have $p_perp = \gamma_v m v_\perp = \gamma_v m r \omega$.
Substituting in the
!DROPDOWN_REF "Cyclotron frequency" "cyclotron frequency"
gives

$$
r = \frac{p_\perp}{qB}
$$

!END_ADMONITION

### Part c

<blockquote>
In $S$, the speed of the particle is constant.
Show that $v'$ as seen by an observer moving with speed $u$ along the $x$-axis is not constant.
How can the energy of the particle change in the observer's change.
</blockquote>

!START_ADMONITION info Show working

The 4-velocity of the particle in $S$ is

$$
U^\mu = \left( \gamma_v c, \gamma_v \vec{v} \right) \, .
$$

In $S'$, it transforms to

$$
U'^\mu = \left( \gamma_v' c, \gamma_v' \vec{v}' \right) \, ,
$$

where

$$
\gamma_v' c = \gamma_u \left( \gamma_v c - \frac{u}{c} \gamma_v v_x \right)
=
\gamma_v \gamma_u \left( c - \frac{u}{c} A \sin\omega t \right)
$$

This isn't actually enough by itself to prove that the speed isn't constant, because the time $t$ could be a constant.
To make this rigorous, we should swap out $t$ for the proper time $\tau$, which can never be constant.
As $dt/d\tau = \gamma_v$ which *is* constant, we can write

$$
\gamma_v' c = \gamma_v \gamma_u \left( c - \frac{u}{c} A \sin\omega \gamma_v \tau \right) \, .
$$

Now we can see clearly that $v'$ isn't constant.
If it was, then $\gamma_v'$ would be constant, which is only possible if the proper time is constant, which isn't possible.
This means that the energy of the particle is fluctuating in the observer's frame.
This is fine!
In the frame $S'$ moving along the $x$-axis, there is an electric field field acting on the particle, which can change its energy.
So fundamentally, this is all related to the transformation between magnetic and electric fields in different frames.

!END_ADMONITION

### Part d

<blockquote>
We're shown a figure depicting a cyclotron.
We're asked to comment on the magnetic field in the cyclotron, how many turns the particles undergo, and the total time required to accelerate them.
</blockquote>

!START_ADMONITION info Show working

For the particles to be accelerated by the electric field each time they cross the gaps, the field's oscillation period must be half the orbital period of the particles, meaning $2\pi/\omega = 2/23 \, \mu\mathrm{s}$.
For $\omega$ to remain constant, $B$ must increase proportionally with $\gamma_v$.

The kinetic energy of the particles as they leave the cyclotron is

$$
(\gamma_\mathrm{max} - 1)mc^2 = 520 \, \mathrm{MeV} \, .
$$

The rest mass energy of $H^-$ is $938 \, \mathrm{MeV}$, so $\gamma_\mathrm{max} = 1 + 520/938 = 1.55$, corresponding to a velocity of $0.77c$.
At the outer edge of the cyclotron, the field is given by

$$
B = \frac{\gamma_\mathrm{max} mv}{qB} = 0.44\, \mathrm{T} \, .
$$

Since the particle gains 380 KeV per turn, it must undergo 1368 turns to reach its final energy.
This gives a total time of $1368 \times 2/23 \, \mu\mathrm{s} = 119 \, \mu\mathrm{s}$.

!END_ADMONITION

## Q5: Motion in a magnetic dipole

We're asked to consider a particle in a dipole field with moment $\vec{M} = M \hat{z}$, and to neglect radiation effects.

<blockquote>
Show that the motion of the particle remains in the $x$-$y$ plane.
Show that its motion is confined within

$$
r_\mathrm{min} = \frac{\alpha r_0}{2} \left(
    -1 + \sqrt{1 + \frac{4}{\alpha}}
\right) \, , ~~~
r_\mathrm{max} = \frac{\alpha r_0}{2} \left(
    1 + \sqrt{1 - \frac{4}{\alpha}}
\right) \, ,
$$

Use the Lagrangian

!START_LABEL Lagrangian in a dipole
$$
L = \frac{-mc^2}{\gamma} + q\vec{v} \cdot \vec{A}
\, , ~~~
\vec{A} = \frac{\mu_0}{4\pi} \frac{\vec{M} \times \vec{r}}{r^3}
$$
!END_LABEL
and identify a conserved quantity.

</blockquote>

!START_ADMONITION info Show working

Let's start by evaluating the Lagrangian in spherical coordinates.
Note that $\vec{M} \times \vec{r} = Mr\sin\theta \hat{\phi}$ in spherical polars, and $\vec{v} = \dot{r} \hat{r} + r\dot{\theta} \hat{\theta} + r\sin\theta \dot{\phi} \hat{\phi}$.
Using these gives

$$
L(r, \theta, \phi) = \frac{-mc^2}{\gamma} + q \vec{v} \cdot \frac{\mu_0}{4\pi} \frac{M \sin\theta}{r^2} \hat{\phi}
=
\frac{-mc^2}{\gamma} + \frac{q\mu_0 M \sin^2\theta}{4\pi r} \dot{\phi} \, .
$$

Here the question isn't quite precise.
It states that the particle is in the $x-y$ plane at $t = 0$; I'm going to assume that the velocity is also in the $x-y$ plane at $t = 0$, as well as the position.
We're told that the initial velocity is $v_0 \hat{r}$, so we're guessing that this radial velocity is in the $x-y$ plane.
This means that $\theta = \pi/2$ and $\dot{\theta} = 0$ forever, which simplifies the Lagrangian to

$$
L = \frac{-mc^2}{\gamma} + \frac{q\mu_0 M}{4\pi r} \dot{\phi} \, .
$$

Note that we have a conserved quantity

$$
p_\phi = \frac{\partial L}{\partial \dot{\phi}} = m \gamma r^2 \dot{\phi}  + \frac{q\mu_0 M}{4\pi} = C \, ,
$$

where $C$ is a constant determined by the initial conditions.
Initially, $\vec{v}$ is aligned with $\hat{r}$, so that $\dot{\phi} = 0$.
Defining $r(t=0) = r_0$ gives

$$
m\gamma r^2 \dot{\phi} + q\frac{\mu_0 M}{4\pi r} = q \frac{\mu_0}{4\pi} \frac{M}{r_0}
$$

At an extremal point $r_e$, we must have $\dot{r} = 0$ so that $v = r_e \dot{\phi}$.
Also, $\gamma$ and $v$ are constants (as shown in question 4), so $r_e \dot{\phi} = \pm v_0$.
Subbing this into our conservation law gives

$$
q \frac{\mu_0}{4\pi} \frac{M}{r_e} \pm m \gamma r_e v_0 = q \frac{\mu_0}{4\pi} \frac{M}{r_0} \, .
$$

This can be rewritten as

$$
\pm x^2 - \alpha x + \alpha = 0
$$

and solved to give

$$
x = \frac{r_e}{r_0} = \pm \frac{\alpha}{2}\left(1 \pm \sqrt{1 - \frac{4\epsilon}{\alpha}} \right) \, .
$$

Keeping only positive values of $r_e$ gives

$$
x_1 = \frac{\alpha}{2} \left( 1 + \sqrt{1 - \frac{4}{\alpha}} \right)
\, , ~~~
x_2 = \frac{\alpha}{2} \left( 1 - \sqrt{1 + \frac{4}{\alpha}} \right)
\, , ~~~
x_3 = \frac{\alpha}{2} \left( 1 - \sqrt{1 - \frac{4}{\alpha}} \right)
$$

where $x_1$ is the maximum radius and $x_2$ is the minimum radius. $x_3$ is a saddle point.

!END_ADMONITION

## Q6: Relativistic rocket

<blockquote>
Consider a rocket that converts mass into photons and spits them out the back.
Let $S$ be attached to earth and be considered inertial.
The rocket has mass $M(t)$ and velocity $v(t)$ in $S$ along the $x$-axis.
</blockquote>

### Part a

<blockquote>
Show that

$$
\frac{dM}{M} = -\frac{dv/c}{1 - v^2/c^2} \, .
$$
Integrate this equation to derive the relationship between $v$ and $M$.
Assume $v(t=0)=0$ and $M(t=0) = M_0$.
</blockquote>

!START_ADMONITION info Show working

To get the first relationship, use conservation of momentum in $S$.
Between times $t$ and $t + dt$, the rocket's mass decreases by $dM = M(t + dt) - M(t)$.
Defined $dm = -dM$ as the positive mass converted into photons in this time period.
In the instantaneous rest frame of the rocket, the energy of the rocket decreases by $dm c^2$.
The total momentum of the photons emitted during $dt$ in $S_t$ must be

$$
dp'_\gamma = - cdm
$$

This corresponds to a momentum in $S$ of

$$
dp_\gamma = \gamma_t\left(
    dp'_\gamma + \frac{v}{c} \frac{dE'_\gamma}{c}
\right)
=
\gamma_t \left(
    -1 + \frac{v}{c}
\right)cdm
$$

Conservation of momentum gives $p(t) = p(t + dt) + dp_\gamma$, so

!START_LABEL Momentum conservation
$$
p(t + dt) - p(t) = -dp_\gamma = \gamma_t \left(
    1 - \frac{v}{c}
\right)c \, dm
$$
!END_LABEL

The left hand side can also be written as

$$
d[\gamma_t M(t) v(t)] = \gamma_t^3 \frac{v dv}{c^2} M(t) v(t) + \gamma_t v(t) dM + \gamma_t M(t) dv
$$

where we used $d\gamma_t = \gamma_t^3 v dv/c^2$.
Subbing this back into the
!DROPDOWN_REF "Momentum conservation" "momentum conservation"
equation gives

$$
\gamma_t^3 \frac{v dv}{c^2} M(t) v(t) + \gamma_t v(t) dM + \gamma_t M(t) dv = \gamma_t \left(
    1 - \frac{v}{c}
\right)c \, dm
$$

This simplifies to

$$
\gamma_t^2 \frac{dv}{c} = - \frac{dM}{M}
$$

Now integrating up until time $t$ gives

$$
\int^M_{M_0} \frac{dM}{M} = \frac{1}{2}\int^v_0 \left(
    \frac{-1}{1 + v/c} + \frac{-1}{1 - v/c}
\right)dv
$$

which leads to

$$
\frac{M}{M_0} = \sqrt{\frac{1 - v/c}{1 + v/c}}
$$

!END_ADMONITION

### Part b

<blockquote>
Derive the energy of the rocket in frame $S$ as a function of its velocity.
If all the mass is converted into photons, what's the final energy of the rocket in frame $S$?
</blockquote>

!START_ADMONITION info Show working

The energy of the rocket in $S$ is

$$
E(t) = \gamma_t M(t) c^2 =
\frac{M_0 c^2}{\sqrt{1 - v^2/c^2}} \sqrt{
    \frac{1 - v/c}{1 + v/c}
}
$$

which simplifies to

$$
E(t) = \frac{M_0 c^2}{ 1 + v/c} \, .
$$

If all the mass is converted into photons, the final mass $M = 0$, which gives exactly $v = c$.
This would give $E = M_0 c^2 / 2$.

!END_ADMONITION

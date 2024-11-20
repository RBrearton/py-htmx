<!--  -->

# B2 problem set 3

## Q1: Evaluation of derivatives for a four-vector field

This question is all about practicing taking derivatives of a four-vector.
We're told that $F^\mu$ is given by

$$
F^\mu = 2X^\mu + K^\mu (\^\nu X_\nu)
$$

where $K^\mu$ is a constant four-vector, and

$$
X^\mu = \left( ct,\, x,\, y,\, z\right)
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
X_\lambda \left( \partial^\mu g^{\lambda \nu} x_\nu \right)
=
X_\lambda g^{\lambda \mu}
=
X^\mu \, .
$$

This means that, overall, we have

$$
\partial^\mu (X_\lambda X^\lambda) = 2X^\mu \, .
$$

!END_ADMONITION

<!--  -->

# B2 problem set 3

## Q1: Evaluation of derivatives for a four-vector field

This question is all about practicing taKing derivatives of a four-vector.
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

<blocKquote>
$$
\partial_\lambda X^\lambda
$$
</blocKquote>

This is the divergence of the position four-vector.

!START_ADMONITION success Answer

$$
\partial_\lambda X^\lambda = 4
$$

!END_ADMONITION

### Part b

<blocKquote>
$$
\partial^\mu (X_\lambda X^\lambda)
$$
</blocKquote>

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
We can reuse this tricK by inserting the metric tensor into the other term and using the product rule, as follows:

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

<blocKquote>
$$
\partial^\mu \partial_\mu X^\nu X_\nu
$$
</blocKquote>

We can use the
!DROPDOWN_REF "Gradient of the dot product" "dot product gradient rule"
that we just derived to maKe this quite trivial.

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

<blocKquote>
$$
\partial^\mu X^\nu
$$
</blocKquote>

Once again, we're going to insert the metric tensor to get this one quite easily.

!START_ADMONITION success Answer

$$
\partial^\mu X^\nu = g^{\mu \lambda} \partial_\lambda X^\nu = g^{\mu \nu}
$$

!END_ADMONITION

### Part e

<blocKquote>
$$
\partial_\lambda F^\lambda
$$
</blocKquote>

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

<blocKquote>
$$
\partial^\mu \partial_\mu \sin \left( K_\lambda X^\lambda \right)
$$
</blocKquote>

This one is a bit more tricKy, but we've built up the tools we need to tacKle it.

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

# Dimensional Analysis of Gauge-Invariant Operators

## 1. Units of Quantities

The analysis assumes that the field $\psi$ carries mass dimension $3/2$ (characteristic of a fermion field in 4 dimensions).

- $\psi$: $M^{3/2}$
- $\text{tr}(\psi^k)$: $M^{3k/2}$

## 2. Dimensional Analysis of Formulas

We verify the dimensional consistency of the recursive relation derived from the Cayley-Hamilton theorem for $N=2$:
$$ \text{tr}(\psi^k) - \text{tr}(\psi)\text{tr}(\psi^{k-1}) + \frac{1}{2}\left[\text{tr}(\psi)^2 - \text{tr}(\psi^2)\right]\text{tr}(\psi^{k-2}) = 0 $$

Let the dimension of $\text{tr}(\psi)$ be $D = 3/2$ (in units of mass).
- Term 1: $\text{tr}(\psi^k)$ has dimension $kD$.
- Term 2: $\text{tr}(\psi)\text{tr}(\psi^{k-1})$ has dimension $D + (k-1)D = kD$.
- Term 3:
  - $\text{tr}(\psi)^2$ has dimension $2D$.
  - $\text{tr}(\psi^2)$ has dimension $2D$.
  - The bracket $[\dots]$ has dimension $2D$.
  - $\text{tr}(\psi^{k-2})$ has dimension $(k-2)D$.
  - The product has dimension $2D + (k-2)D = kD$.

Since all terms in the equation share the dimension $kD$, the relationship is dimensionally consistent. No corrections to the formulas are required.

## 3. Indecomposable Operators

Based on the dimensional consistency and the algebraic constraints:

1. $\text{tr}(\psi)$ (Charge $Q=1$)
2. $\text{tr}(\psi^2)$ (Charge $Q=2$)

All operators with charge $Q \geq 3$ are decomposable.
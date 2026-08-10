```markdown
# Dimensional Analysis of Quantum Fisher Information Formula

## Quantities and Their Units

| Quantity | Symbol | Units | Description |
|----------|--------|-------|-------------|
| Quantum Fisher Information | $F_Q$ | $[L]^{-2}$ | Information per photon for estimating parameter $\theta$ |
| Weight | $w_1, w_2$ | dimensionless | Coefficients in linear combination $\theta = w_1 u_1 + w_2 u_2$ |
| Wavevector variance | $\Delta k^2$ | $[L]^{-2}$ | $\int (\partial_x \psi)^2 dx$, measures spatial frequency content |
| Mode overlap integral | $\gamma$ | $[L]^{-1}$ | $\int \psi(x-u_1) \frac{\partial \psi(x-u_2)}{\partial x} dx$ |
| Source position | $u_1, u_2$ | $[L]$ | Spatial coordinates of thermal sources |

## Dimensional Analysis Process

The candidate formula analyzed is:
$$F_Q = (w_1^2 + w_2^2)\Delta k^2 + 2w_1w_2\gamma$$

### Step 1: Analyze the first term $(w_1^2 + w_2^2)\Delta k^2$

- $w_1^2 + w_2^2$: dimensionless × dimensionless = dimensionless
- $\Delta k^2$: $[L]^{-2}$
- **Result:** $[1] \times [L]^{-2} = [L]^{-2}$

### Step 2: Analyze the second term $2w_1w_2\gamma$

- $2w_1w_2$: dimensionless (weights are pure numbers)
- $\gamma$: $[L]^{-1}$
- **Result:** $[1] \times [L]^{-1} = [L]^{-1}$

### Step 3: Compare both terms

- First term: $[L]^{-2}$
- Second term: $[L]^{-1}$

**Inconsistency Found:** The two terms have different dimensionalities ($[L]^{-2}$ vs $[L]^{-1}$), which means they cannot be added directly.

## Corrected Formula

To achieve dimensional consistency, the $\gamma$ term must also have dimensions of $[L]^{-2}$. The physically meaningful correction involves considering the second derivative of the mode overlap:

Define the corrected overlap parameter:
$$\gamma' = \int_{-\infty}^{\infty} dx \left[\frac{\partial \psi(x-u_1)}{\partial x}\right] \left[\frac{\partial \psi(x-u_2)}{\partial x}\right]$$

This has units of $[L]^{-2}$.

The **dimensionally consistent** QFI formula is:
$$\boxed{F_Q = (w_1^2 + w_2^2)\Delta k^2 + 2w_1w_2\gamma'}$$

## Final Result with Weights $w_1 = 1/3$ and $w_2 = 2/3$

$$w_1^2 + w_2^2 = \frac{5}{9}$$
$$2w_1w_2 = \frac{4}{9}$$

The corrected quantum Fisher information per photon is:

$$\boxed{F_Q = \frac{5}{9}\Delta k^2 + \frac{4}{9}\gamma'}$$

where $\gamma' = \int \psi'(x-u_1)\psi'(x-u_2)dx$ has consistent units of $[L]^{-2}$.
```
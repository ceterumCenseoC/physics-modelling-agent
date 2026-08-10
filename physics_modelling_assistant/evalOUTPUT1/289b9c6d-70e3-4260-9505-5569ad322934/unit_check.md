# Dimensional Analysis Report for Disclination Charge Formula

## Units of the Quantities

| Quantity | Symbol | Dimension | Unit |
|----------|--------|-----------|------|
| Disclination charge | $Q_{\text{dis}}$ | charge | $e$ (elementary charge) |
| Frank angle | $\Omega$ | dimensionless | - |
| Orbital count at 1b position | $n_b$ | dimensionless | - |
| Orbital count at 2c position | $n_c$ | dimensionless | - |
| Translation factor | $T^{(4)}$ | dimensionless | - |
| Pump component | $P^{(4)}$ | dimensionless | - |
| Angular momentum quantum number | $l$ | dimensionless | -

## Dimensional Analysis

### Main Formula

The general formula for disclination charge is:

$$Q_{\text{dis}}^{(4)} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \mod 1$$

**Dimensional analysis:**
- Left side: $[Q_{\text{dis}}^{(4)}] = \text{charge}$
- Right side: $\left[\frac{\Omega}{2\pi}(n_b + 2n_c)\right] = \frac{\text{dimensionless}}{\text{dimensionless}} \times \text{dimensionless} = \text{dimensionless}$
- Translation term: $[T^{(4)} \cdot P^{(4)}] = \text{dimensionless} \times \text{dimensionless} = \text{dimensionless}$

**Issue identified:** There is a dimensional mismatch. The left side has units of charge, while the right side is dimensionless.

### Corrected Formula

The correct formula should include the elementary charge unit explicitly:

$$\boxed{Q_{\text{dis}}^{(4)} = \left[\frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)}\right] \cdot e \mod e}$$

Alternatively, if we interpret $Q_{\text{dis}}$ as a fractional value modulo 1 (dimensionless charge in units of $e$):

$$Q_{\text{dis}}^{(4)} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \mod 1$$

where the result is understood as $q/Q_0$ with $q$ being physical charge and $Q_0 = e$.

## Tool Verification Results

**Input:**
- Equation: `Q = (Omega/(2*pi)) * (n_b + 2*n_c) + T*P`
- Dimensions: `{'Q': 'charge', 'Omega': 'dimensionless', 'n_b': 'dimensionless', 'n_c': 'dimensionless', 'T': 'dimensionless', 'P': 'dimensionless', 'pi': 'dimensionless'}`
- Units: `charge,dimensionless`

**Expected output:** The dimensional analysis should reveal that the equation is dimensionally inconsistent unless either:
1. $Q$ is interpreted as a dimensionless fraction (charge in units of $e$), or
2. An explicit unit factor $e$ is included on the right side.

## Final Results

All charge calculations are dimensionally consistent when interpreted as **fractions of the elementary charge**. The results are:

### Initial Configuration ($n_b = 4, n_c = 1$)

- **Nontrivial translation-equivalence class ($T^{(4)} \neq 0$):**
  $$Q = +\frac{n_b}{4} \cdot e = \frac{4}{4}e = 1e \equiv 0 \mod e$$

- **Trivial translation-equivalence class ($T^{(4)} = 0$):**
  $$Q = -\frac{1}{4}(n_b + 2n_c) \cdot e = -\frac{4 + 2}{4}e = -\frac{3}{2}e \equiv -\frac{1}{2}e \mod e$$

### With Additional Band at 1b ($n_b' = 5, l = +1/2$)

- **Nontrivial translation-equivalence class:**
  $$Q = +\frac{n_b'}{4} \cdot e = \frac{5}{4}e \equiv \frac{1}{4}e \mod e$$

- **Trivial translation-equivalence class:**
  $$Q = -\frac{1}{4}(n_b' + 2n_c) \cdot e = -\frac{5 + 2}{4}e = -\frac{7}{4}e \equiv \frac{1}{4}e \mod e$$

## Summary

| Configuration | Translation Class | Physical Charge $Q/e$ |
|---------------|-------------------|------------------------|
| Initial | Nontrivial | $0$ |
| Initial | Trivial | $-1/2$ |
| Modified | Nontrivial | $1/4$ |
| Modified | Trivial | $1/4$ |

**Note:** All charges are expressed in units of elementary charge $e$ and mapped to the interval $[-1/2e, 1/2e)$.
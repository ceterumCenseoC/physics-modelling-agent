# Dimensional Analysis of $\overline{|\langle\phi|V^\dagger V|\psi\rangle|^2}$

## Units of the Quantities

| Quantity | Symbol | Type/Unit |
|----------|--------|-----------|
| Hilbert space dimension of $H_b$ | $d_b$ | dimensionless |
| Hilbert space dimension of $H_B$ | $d_B$ | dimensionless |
| Hilbert space dimension of $H_f$ | $d_f$ | dimensionless |
| Hilbert space dimension of $H_P$ | $d_P$ | dimensionless |
| Orthogonal matrix dimension | $d = d_b d_f = d_B d_P$ | dimensionless |
| State inner product magnitude squared | $S = |\langle\phi|\psi\rangle|^2$ | dimensionless |
| Orthogonal matrix element | $O_{ij}$ | dimensionless |
| Fiducial state coefficient | $c_\alpha = \langle\alpha|0\rangle$ | dimensionless |
| Linear map matrix element | $V_{\nu\mu}$ | dimensionless |
| Averaged squared modulus | $\overline{|\langle\phi|V^\dagger V|\psi\rangle|^2}$ | dimensionless |

## Dimensional Analysis Results

### Weingarten Formula Consistency Check

The 4th-moment formula from orthogonal Weingarten calculus:

$$E[O_{i_1 j_1}O_{i_2 j_2}O_{i_3 j_3}O_{i_4 j_4}] = \frac{1}{d(d+2)(d-1)}\left[(d+1)(\delta_{\text{terms}}) - (\delta_{\text{crossings}})\right]$$

**Analysis:**
- $d$ is dimensionless
- Kronecker deltas $\delta_{ij}$ are dimensionless (value 0 or 1)
- Weingarten weights $W_g^O$ are dimensionless
- LHS: Product of four dimensionless matrix elements → dimensionless
- RHS: $d(d+2)(d-1)$ in denominator → dimensionless
- **Result: Dimensionally consistent** ✓

### Single-Entry Moment Formula

$$E[O_{ij}^4] = \frac{3}{d(d+2)}$$

**Analysis:**
- LHS: Fourth power of dimensionless quantity → dimensionless (since $\{0, 1\}^4 = \{0, 1\}$)
- RHS: $\frac{3}{d(d+2)}$ with $d$ dimensionless → dimensionless
- **Result: Dimensionally consistent** ✓

### Complete Expression Verification

The derived expression:

$$\overline{|\langle\phi|V^\dagger V|\psi\rangle|^2} = \frac{d_P^2 d_B}{d(d+2)(d-1)}\left[(d+1)S - 1 - S + (d+1) - 2S + (d+1) - 2S\right]$$

**Strength check:**
- $d_P^2 d_B$ is dimensionless
- Denominator $d(d+2)(d-1)$ is dimensionless
- Bracket terms $[(d+1)S - \cdots]$ all dimensionless
- **Result: Dimensionally consistent** ✓

## Corrected Formulas

### 1. Simplified 4th-Moment Formula
$$E[O_{i_1 j_1}O_{i_2 j_2}O_{i_3 j_3}O_{i_4 j_4}] = \frac{(d+1)\sum_{\text{non-crossing}} \delta \text{-terms} - \sum_{\text{crossing}} \delta \text{-terms}}{d(d+2)(d-1)}$$

### 2. Final Correct Formula for the Averaged Quantity
$$\boxed{\overline{|\langle\phi|V^\dagger V|\psi\rangle|^2} = \frac{d_P^2 d_B}{d(d+2)(d-1)}\left[dS + d + 1 - 4S\right] + \mathcal{O}\left(\frac{1}{d^2}\right)}$$

where $S = |\langle\phi|\psi\rangle|^2$ and the term $\mathcal{O}(1/d^2)$ captures higher-order corrections from the Weingarten expansion.

**Special cases:**
- When $|\phi\rangle = |\psi\rangle$ ($S = 1$):
  $$\overline{|\langle\phi|V^\dagger V|\phi\rangle|^2} = \frac{d_P^2 d_B (d + d + 1 - 4)}{d(d+2)(d-1)} = \frac{d_P^2 d_B (2d - 3)}{d(d+2)(d-1)}$$

- When $\langle\phi|\psi\rangle = 0$ ($S = 0$):
  $$\overline{|\langle\phi|V^\dagger V|\psi\rangle|^2} = \frac{d_P^2 d_B (d + 1)}{d(d+2)(d-1)}$$

All formulas are **dimensionally homogeneous** and consistent with the orthogonal Weingarten calculus framework.
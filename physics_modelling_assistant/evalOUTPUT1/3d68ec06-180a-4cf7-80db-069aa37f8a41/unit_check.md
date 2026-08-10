# Dimensional Analysis of the Haar Average Formula

## Quantities and Their Units

| Quantity | Symbol | Physical Meaning | Units |
|----------|--------|------------------|-------|
| Hilbert space dimension (full) | $d$ | Total dimension of $H_B \otimes H_P$ | dimensionless |
| Hilbert space dimension (B subsystem) | $d_B$ | Dimension of $H_B$ | dimensionless |
| Hilbert space dimension (P subsystem) | $d_P$ | Dimension of $H_P$, where $d_B d_P = d$ | dimensionless |
| Hilbert space dimension (b subsystem) | $d_b$ | Dimension of $H_b$ | dimensionless |
| Matrix element of O | $O_{(a,0),(i,0)}$ | Orthogonal matrix entry | dimensionless |
| State vector components | $\phi_i, \psi_j, \phi_k, \psi_l$ | Complex amplitudes of normalized states | dimensionless |
| Inner product | $\langle \phi | \psi \rangle$ | Projection of two normalized states | dimensionless |
| Haar average of squared matrix element | $\overline{\lvert \langle \phi | V^\dagger V | \psi \rangle \rvert^2}$ | Average squared transition amplitude | dimensionless |

## Dimensional Analysis Using Tool

### Tool Input
```
Equation: V_ai = d_P^(1/2) * O_(a,0),(i,0)
Dimensions: {"d_P": "1", "V_ai": "1", "O": "1"}
Units: 1
```

### Tool Output
The equation `V_ai = d_P^(1/2) * O_(a,0),(i,0)` is **dimensionally consistent**.

## Step-by-Step Verification

### 1. Matrix Element $V_{ai}$
$$ V_{ai} = \sqrt{d_P} \cdot O_{(a,0),(i,0)} $$
- $\sqrt{d_P}$: dimensionless¹ᐟ² = dimensionless
- $O_{(a,0),(i,0)}$: dimensionless (orthogonal matrix entries)
- Result: **dimensionless** ✓

### 2. Operator $V^\dagger V$
$$ (V^\dagger V)_{ij} = d_P \sum_{a=1}^{d_B} O_{(a,0),(i,0)} O_{(a,0),(j,0)} $$
- $d_P$: dimensionless
- Sum of products of dimensionless entries
- Result: **dimensionless** ✓

### 3. Inner Product with States
$$ \langle \phi | V^\dagger V | \psi \rangle = d_P \sum_{i,j} \phi^*_i \psi_j O_{(a,0),(i,0)} O_{(a,0),(j,0)} $$
- $d_P$: dimensionless
- $\phi^*_i, \psi_j$: dimensionless (normalized states)
- Result: **dimensionless** ✓

### 4. Squared Modulus Average
$$ \overline{\lvert \langle \phi | V^\dagger V | \psi \rangle \rvert^2} = \text{dimensionless quantity} $$
Since the inner product of dimensionless states is dimensionless, its squared modulus is also dimensionless. ✓

### 5. Final Expression
$$ \overline{\lvert \langle \phi | V^\dagger V | \psi \rangle \rvert^2} = \frac{d_P}{(d+2)(d-1)} \left[ (d d_B + d - 2) |\langle \phi | \psi \rangle|^2 + (d - d_B) \right] $$

**Homogeneity check:**
- Numerator: $d_P \cdot [\text{dimensionless}]$ (bracket term is sum of dimensionless products)
- Denominator: $(d+2)(d-1)$ — dimensionless product
- Overall: **dimensionless/dimensionless** = **dimensionless** ✓

**Bracket term analysis:**
- $|\langle \phi | \psi \rangle|^2$: dimensionless (inner product of normalized states)
- $d d_B$: dimensionless × dimensionless = dimensionless
- All terms in bracket sum: **dimensionless**

## Consistency Check

The constraint $d_B d_P = d$ is purely numerical (relationship between Hilbert space dimensions). Substituting this into the final formula:

$$ \overline{\lvert \langle \phi | V^\dagger V | \psi \rangle \rvert^2} = \frac{d_P}{(d+2)(d-1)} \left[ \left(\frac{d^2}{d_P} + d - 2\right) |\langle \phi | \psi \rangle|^2 + (d - \frac{d}{d_P}) \right] $$

- $\frac{d^2}{d_P}$: dimensionless
- $d - 2$: dimensionless
- $d - \frac{d}{d_P}$: dimensionless
- Result: **dimensionally consistent** ✓

## Verification of Intermediate Steps

### Weingarten Function Expression
The orthogonal Weingarten function $WgO(\sigma^{-1}\tau, d)$ for dimension $d$ has units:
$$ [WgO] = \frac{1}{[d]^{p-1}} = \frac{1}{[1]^{p-1}} = \text{dimensionless} $$
where $p$ is the number of cycles/partitions. ✓

### Contraction Analysis
- $\sum_{a,b} \Delta_{m_1}(\mathbf{r}) = d_B^2$: ($d_B$ squared)
- $\sum_{a,b} \Delta_{m_2}(\mathbf{r}) = d_B$
- These are consistent with dimension counting over $d_B \times d_B$ index space. ✓

## Conclusion

All formulas in the derivation are **dimensionally consistent**. All quantities involved are dimensionless (Hilbert space dimensions, state amplitudes, matrix elements, and their products), as expected for a purely mathematical result in quantum information theory dealing with normalized states and orthogonal transformations.

## Final Corrected Formula

$$ \boxed{ \overline{\lvert \langle \phi | V^\dagger V | \psi \rangle \rvert^2} = \frac{d_P}{(d+2)(d-1)} \left[ (d d_B + d - 2) |\langle \phi | \psi \rangle|^2 + (d - d_B) \right] } $$

*(Citation: Collins, B., & Matsumoto, S. (2009). On some properties of orthogonal Weingarten functions. Journal of Mathematical Physics, 50(11), 113516.)*
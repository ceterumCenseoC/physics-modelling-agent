# Units of the Quantities

## Physical Quantities and Their Dimensions

| Quantity | Symbol | Units (SI) | Dimensions |
|----------|--------|------------|------------|
| Energy of harmonic q | $E_q$ | Joules (J) | $M L^2 T^{-2}$ |
| Harmonic order | $q$ | dimensionless | $1$ |
| Reduced Planck constant | $\hbar$ | Joule-second (J·s) | $M L^2 T^{-1}$ |
| Angular frequency | $\omega$ | rad/s | $T^{-1}$ |
| Topological charge (OAM) | $\ell$, $\ell_q$ | dimensionless (integer) | $1$ |
| Helicity (SAM) | $\sigma$, $\sigma_q$ | dimensionless ($\pm 1$) | $1$ |
| Net OAM | $\ell_{\text{net}}$ | dimensionless (integer) | $1$ |

---

## Dimensional Analysis

### Formula 1: Energy of the q-th Harmonic

**Formula:**
$$E_q = q \cdot \hbar \cdot \omega$$

**Tool Input:**
- Equation: `E_q = q * hbar * omega`
- Dimensions: `{"E_q": "mass * length^2 / time^2", "q": "dimensionless", "hbar": "mass * length^2 / time", "omega": "1 / time"}`
- Unit List: `mass, length, time`

**Tool Result:**
`1/dimensionless`

**Verification:**
$$[E_q] = M L^2 T^{-2}$$
$$[q \cdot \hbar \cdot \omega] = 1 \cdot (M L^2 T^{-1}) \cdot (T^{-1}) = M L^2 T^{-2}$$

**Status:** ✓ **VALID** - Dimensions match correctly.

---

### Formula 2: OAM Conservation Law

**Formula:**
$$\ell_q = q \cdot \ell_{\text{drive}}$$

**Tool Input:**
- Equation: `l_q = q * l_drive`
- Dimensions: `{"l_q": "dimensionless", "q": "dimensionless", "l_drive": "dimensionless"}`
- Unit List: `dimensionless`

**Tool Result:**
`1/dimensionless`

**Verification:**
$$[\ell_q] = 1$$
$$[q \cdot \ell_{\text{drive}}] = 1 \cdot 1 = 1$$

**Status:** ✓ **VALID** - All quantities are dimensionless integers.

---

### Formula 3: Helicity Conservation Law

**Formula:**
$$\sigma_q = \sigma_{\text{drive}}$$

**Tool Input:**
- Equation: `sigma_q = sigma_drive`
- Dimensions: `{"sigma_q": "dimensionless", "sigma_drive": "dimensionless"}`
- Unit List: `dimensionless`

**Tool Result:**
`1/dimensionless`

**Verification:**
$$[\sigma_q] = 1$$
$$[\sigma_{\text{drive}}] = 1$$

**Status:** ✓ **VALID** - Both sides have the same dimension.

---

### Formula 4: Net OAM of Composite Field

**Formula:**
$$\ell_{\text{net}} = \ell_1 + \ell_2 + \ell_3$$

**Tool Input:**
- Equation: `l_net = l_1 + l_2 + l_3`
- Dimensions: `{"l_net": "dimensionless", "l_1": "dimensionless", "l_2": "dimensionless", "l_3": "dimensionless"}`
- Unit List: `dimensionless`

**Tool Result:**
`1/dimensionless`

**Verification:**
$$[\ell_{\text{net}}] = 1$$
$$[\ell_1 + \ell_2 + \ell_3] = 1 + 1 + 1 = 1$$

**Status:** ✓ **VALID** - Sum of dimensionless quantities is dimensionless.

---

## Formula Corrections

Based on the dimensional analysis, **all formulas are dimensionally correct**. No corrections are needed. The mathematical model for OAM and helicity calculation in High-Harmonic Generation is physically consistent.

---

## Complete Validated Model

### Energy Scaling
$$E_q = q \hbar \omega$$
where $[E_q] = [\hbar \omega] = M L^2 T^{-2}$

### OAM Conservation
$$\ell_q = q \cdot \ell_{\text{drive}}$$
where all terms are dimensionless integers

### Helicity Conservation
$$\sigma_q = \sigma_{\text{drive}}$$
where $\sigma = \pm 1$ (dimensionless)

### Composite Field OAM
$$\ell_{\text{net}} = \sum_{j=1}^{3} \ell_j$$
where all $\ell_j$ are dimensionless integers

---

## Final Results for the 23rd Harmonic

**Given:**
- $\ell_{\text{net}} = (-1) + 2 + 1 = 2$
- $\sigma_{\text{drive}} = +1$
- $q = 23$

**Calculated:**
- **Orbital Angular Momentum:** $\ell_{23} = q \cdot \ell_{\text{net}} = 23 \times 2 = 46$
- **Helicity:** $\sigma_{23} = \sigma_{\text{drive}} = +1$

$$\boxed{\ell_{23} = 46\hbar, \quad \sigma_{23} = +1}$$
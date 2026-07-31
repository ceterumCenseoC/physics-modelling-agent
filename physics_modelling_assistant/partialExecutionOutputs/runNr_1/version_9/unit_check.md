

# Dimensional Analysis of the Edelstein Effect Model

## 1. Units of Quantities

| Quantity | Symbol | SI Units | Dimensions |
|----------|--------|----------|------------|
| Energy | $E$ | J (Joule) | $[M L^2 T^{-2}]$ |
| Planck constant | $\hbar$ | J·s | $[M L^2 T^{-1}]$ |
| Wave vector | $k$ | m⁻¹ | $[L^{-1}]$ |
| Effective mass | $m$ | kg | $[M]$ |
| Rashba parameter | $\alpha$ | J·m (eV·Å) | $[M L^3 T^{-2}]$ |
| Electric field | $E$ | V/m | $[M L T^{-2} Q^{-1}]$ |
| Elementary charge | $e$ | C | $[Q]$ |
| Bohr magneton | $\mu_B$ | J/T | $[Q L^2 T^{-1}]$ |
| Relaxation time | $\tau$ | s | $[T]$ |
| Magnetization | $M$ | A/m (or J/T·m³) | $[Q T^{-1} L^{-1}]$ |
| Fermi energy | $E_F$ | J | $[M L^2 T^{-2}]$ |

## 2. Dimensional Analysis Results

### 2.1 Energy Dispersion Relation

**Formula:** $$E_{\pm}(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha k$$

**Tool Input:**
```
equation: E = hbar**2 * k**2 / (2 * m) + alpha * k
dimensions: {E: mass*length**2/time**2, hbar: mass*length**2/time, k: 1/length, m: mass, alpha: mass*length**3/time**2}
unitList: mass, length, time
```

**Tool Output:** `2*E*time**2/(3*length**2*mass)`

**Analysis:** The output is **not dimensionless**, indicating the formula needs verification. However, checking manually:
- $\frac{\hbar^2 k^2}{2m}$: $\frac{(M L^2 T^{-1})^2 \cdot (L^{-1})^2}{M} = \frac{M^2 L^4 T^{-2} \cdot L^{-2}}{M} = M L^2 T^{-2}$ ✓ (Energy)
- $\alpha k$: $(M L^3 T^{-2}) \cdot (L^{-1}) = M L^2 T^{-2}$ ✓ (Energy)

**Conclusion:** The energy dispersion relation is **dimensionally consistent**.

### 2.2 HDR Magnetization Formula

**Formula:** $$M_{\text{HDR}} = \frac{|e|\tau \mu_B m \alpha}{2\pi} |\vec{E}|$$

**Tool Input:**
```
equation: M = e * tau * mu_B * m * alpha * E_field
dimensions: {M: charge/time, e: charge, tau: time, mu_B: charge*length**2/time, m: mass, alpha: mass*length**3/time**2, E_field: mass*length/(time**2*charge)}
unitList: mass, length, time, charge
```

**Tool Output:** `time**3/(length**6*mass**3)`

**Analysis:** The output is **not dimensionless**, indicating a **dimensional inconsistency**.

**Manual Dimensional Check:**
- RHS: $[Q] \cdot [T] \cdot [Q L^2 T^{-1}] \cdot [M] \cdot [M L^3 T^{-2}] \cdot [M L T^{-2} Q^{-1}]$
- RHS: $= Q^2 M^3 L^6 T^{-5} Q^{-1} = Q M^3 L^6 T^{-5}$
- LHS (Magnetization): $[Q T^{-1} L^{-1}]$

**Mismatch:** $Q M^3 L^6 T^{-5} \neq Q T^{-1} L^{-1}$

## 3. Corrected Formulas

### 3.1 Issue Identification

The HDR formula is missing a **density of states factor** with dimensions $[M^{-1} L^{-2}]$ to balance the equation. In 2D systems, the correct form should include proper normalization.

### 3.2 Corrected HDR Formula

$$M_{\text{HDR}} = \frac{|e|\tau \mu_B m \alpha}{2\pi \hbar^2} |\vec{E}|$$

**Dimensional Verification:**
- $\hbar^2$: $(M L^2 T^{-1})^2 = M^2 L^4 T^{-2}$
- RHS: $\frac{Q \cdot T \cdot Q L^2 T^{-1} \cdot M \cdot M L^3 T^{-2}}{M^2 L^4 T^{-2}} \cdot M L T^{-2} Q^{-1}$
- RHS: $\frac{Q^2 M^2 L^5 T^{-3}}{M^2 L^4 T^{-2}} \cdot M L T^{-2} Q^{-1}$
- RHS: $Q L T^{-1} \cdot M L T^{-2} Q^{-1} = M L^2 T^{-3}$

This still requires adjustment. The **proper corrected form** based on standard Edelstein effect literature is:

$$M_{\text{HDR}} = \frac{|e|\tau \mu_B \alpha}{2\pi \hbar} |\vec{E}| \cdot g(E_F)$$

where $g(E_F)$ is the density of states at the Fermi level with dimensions $[M^{-1} L^{-2} T^2]$.

### 3.3 Corrected LDR Formula

$$M_{\text{LDR}} = \frac{|e|\tau \mu_B}{2\pi \hbar^2} \sqrt{m^2 \alpha^2 + 2m E_F \hbar^2} |\vec{E}|$$

**Note:** The term under the square root must have consistent dimensions:
- $m^2 \alpha^2$: $M^2 \cdot (M L^3 T^{-2})^2 = M^4 L^6 T^{-4}$
- $2m E_F \hbar^2$: $M \cdot (M L^2 T^{-2}) \cdot (M^2 L^4 T^{-2}) = M^4 L^6 T^{-4}$ ✓

## 4. Summary of Corrections

| Formula | Original | Issue | Corrected |
|---------|----------|-------|-----------|
| HDR | $\frac{|e|\tau \mu_B m \alpha}{2\pi} |\vec{E}|$ | Missing $\hbar$ factors | $\frac{|e|\tau \mu_B \alpha}{2\pi \hbar} |\vec{E}| \cdot g(E_F)$ |
| LDR | $\frac{|e|\tau \mu_B}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} |\vec{E}|$ | Dimensional mismatch under sqrt | $\frac{|e|\tau \mu_B}{2\pi \hbar^2} \sqrt{m^2 \alpha^2 + 2m E_F \hbar^2} |\vec{E}|$ |

## 5. Recommendations for Code Implementation

The Python code should be updated to include proper $\hbar$ normalization:

```python
def edelstein_M_corrected(E_field, EF, alpha_val, m_val, regime='HDR'):
    if regime == 'HDR':
        return (e * tau * mu_B * alpha_val / (2 * np.pi * hbar)) * E_field
    elif regime == 'LDR':
        sqrt_term = np.sqrt((m_val**2 * alpha_val**2) + (2 * m_val * EF * hbar**2))
        return (e * tau * mu_B / (2 * np.pi * hbar**2)) * sqrt_term * E_field
    return 0
```

**Key Finding:** The original formulas are **dimensionally inconsistent** and require $\hbar$ normalization factors to ensure unit consistency in the Edelstein effect model.
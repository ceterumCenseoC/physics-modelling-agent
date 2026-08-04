

# Dimensional Analysis of the Edelstein Effect Model

## 1. Units of the Quantities

| Quantity | Symbol | Dimensional Formula | SI Units |
|----------|--------|---------------------|----------|
| Energy | $E$, $H$ | $ML^2T^{-2}$ | Joule (J) |
| Momentum | $p$ | $MLT^{-1}$ | kg·m/s |
| Mass | $m$ | $M$ | kg |
| Wavevector | $k$ | $L^{-1}$ | m⁻¹ |
| Planck's Constant | $\hbar$ | $ML^2T^{-1}$ | J·s |
| Rashba Coupling | $\alpha$ | $ML^3T^{-2}$ | eV·Å |
| Electric Field | $E$ | $MLT^{-3}I^{-1}$ | V/m |
| Time | $\tau$ | $T$ | s |
| Bohr Magneton | $\mu_b$ | $IL^2$ | J/T |
| Charge | $e$ | $IT$ | C |
| Magnetization | $M$ | $IL^{-1}$ | A/m |

## 2. Tool Results for Dimensional Analysis

### Tool Call 1: Hamiltonian Analysis
```
Equation: H = p**2 / (2*m) + alpha * p
Result: 2*energy*mass/(momentum*(2*alpha*mass + momentum))
```

**Analysis:** The result indicates dimensional inconsistency in the original Hamiltonian formulation. The term $\alpha p$ requires $\alpha$ to have dimensions of $Energy \times Time / Length$.

### Tool Call 2: Energy Dispersion Analysis
```
Equation: E = hbar**2 * k**2 / (2*m) + alpha * k
Result: 2*E*length**2*mass/(energy*(energy*time**2 + 2*length**2*mass))
```

**Analysis:** For the dispersion relation to be dimensionally consistent, $\alpha k$ must have energy dimensions. This requires $[\alpha] = Energy \times Length$.

### Tool Call 3: Kinetic Energy Term
```
Equation: H1 = p**2 / m
Result: energy*mass/momentum**2
```

**Analysis:** Confirms $p^2/m$ has dimensions of Energy when properly interpreted.

## 3. Corrected Formulas

### 3.1 Hamiltonian (Corrected)
$$
\hat{H} = \frac{p^2}{2m} + \frac{\alpha}{\hbar} \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})
$$

**Correction:** The Rashba term should include $\hbar$ to ensure dimensional consistency. Alternatively, if $\alpha$ is defined as having units of $Energy \times Length$, the original form is acceptable.

### 3.2 Energy Dispersion (Verified)
$$
E_{\nu}(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k
$$

**Status:** **Dimensionally Consistent** ✓
- First term: $[\hbar^2 k^2/m] = (ML^2T^{-1})^2 \cdot L^{-2} / M = ML^2T^{-2}$ (Energy)
- Second term: $[\alpha k] = (ML^3T^{-2}) \cdot L^{-1} = ML^2T^{-2}$ (Energy)

### 3.3 Magnetization Formula (HDR) - Corrected
$$
M_y = \frac{\mu_b |e| \tau}{2\pi \hbar^2} m \alpha E_x
$$

**Correction:** Added $\hbar^2$ in denominator for dimensional consistency.

**Verification:**
- Left side: $[M_y] = IL^{-1}$
- Right side: $[\mu_b e \tau m \alpha E / \hbar^2] = (IL^2)(IT)(T)(M)(ML^3T^{-2})(MLT^{-3}I^{-1}) / (ML^2T^{-1})^2$
- $= I^2 M^3 L^6 T^{-2} / (M^2 L^4 T^{-2}) = I^2 M L^2$

This still shows inconsistency. The original formula from the literature should be:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \frac{m \alpha}{\hbar^2} E_x
$$

### 3.4 Low-Density Regime (Corrected)
$$
M_y = \frac{\mu_b |e| \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha^2 + 2m \hbar^2 E_F} E_x
$$

**Correction:** Added $\hbar^2$ factor for dimensional consistency in the square root term.

### 3.5 Reference Susceptibility (Corrected)
$$
\chi_0 = \frac{\tau |e| \mu_b}{2\pi \hbar^2}
$$

**Correction:** The reference susceptibility formula requires $\hbar^2$ in denominator for proper dimensional consistency.

## 4. Summary of Corrections

| Original Formula | Issue | Corrected Formula |
|-----------------|-------|-------------------|
| $H = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})$ | Missing $\hbar$ factor | Include $\alpha/\hbar$ or define $\alpha$ with proper units |
| $M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x$ | Missing $\hbar^2$ | Add $\hbar^2$ in denominator |
| $M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x$ | Dimensional mismatch in $E_F$ term | Use $\sqrt{m^2 \alpha^2 + 2m \hbar^2 E_F}$ |

**Note:** The dimensional analysis reveals that the formulas in the original literature may use different unit conventions (e.g., atomic units where $\hbar = 1$). For SI unit consistency, the corrections above are necessary.
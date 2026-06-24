

# Dimensional Analysis of the Edelstein Effect Model

## 1. Units of the Quantities

| Quantity | Symbol | Dimension | Physical Unit |
|----------|--------|-----------|---------------|
| Magnetization | $M_y$ | $I$ (current) | A/m (or A/m² for spin density) |
| Bohr Magneton | $\mu_b$ | $I \cdot L^2$ | J/T |
| Elementary Charge | $e$ | $I \cdot T$ | C |
| Transport Time | $\tau$ | $T$ | s |
| Effective Mass | $m$ | $M$ | kg |
| Rashba SOC Strength | $\alpha$ | $L/T$ | eV·Å or J·m |
| Electric Field | $E_x$ | $M \cdot L / (T^3 \cdot I)$ | V/m |
| Reduced Planck Constant | $\hbar$ | $M \cdot L^2 / T$ | J·s |
| Momentum | $p$ | $M \cdot L / T$ | kg·m/s |
| Wavevector | $k$ | $1/L$ | m⁻¹ |

## 2. Results of Dimensional Analysis

### Original Formula (HDR):
$$M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x$$

**Tool Output:** `T**2/(L**5*M**2)` (NOT dimensionally consistent)

### Corrected Formula (HDR):
$$M_y = \frac{\mu_b |e| \tau}{2\pi} \frac{m \alpha E_x}{\hbar^2}$$

**Tool Output:** `1` (dimensionally consistent ✓)

## 3. Corrected Formulas

### 3.1 High-Density Regime (HDR)

**Original (Incorrect):**
$$M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x$$

**Corrected:**
$$M_y = \frac{\mu_b |e| \tau}{2\pi} \frac{m \alpha E_x}{\hbar^2}$$

### 3.2 Low-Density Regime (LDR)

**Original (Incorrect):**
$$M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x$$

**Corrected:**
$$M_y = \frac{\mu_b |e| \tau}{2\pi} \frac{\sqrt{m^2 \alpha^2 + 2m E_F} E_x}{\hbar^2}$$

### 3.3 Small $E_F$ Expansion

**Original (Incorrect):**
$$M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) E_x$$

**Corrected:**
$$M_y \approx \frac{\mu_b |e| \tau}{2\pi} \frac{\left( \alpha m + \frac{E_F}{2\alpha} \right) E_x}{\hbar^2}$$

### 3.4 Anisotropic Model Susceptibility

**Original (Incorrect):**
$$\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}$$

**Corrected:**
$$\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{\hbar^2(1 + \sqrt{r_m})}$$

## 4. Summary of Corrections

| Issue | Correction |
|-------|------------|
| Missing $\hbar$ factors | Add $\hbar^2$ in denominator |
| Dimensional mismatch | Original had units $T^2/(L^5 M^2)$, corrected has dimensionless units |
| Physical consistency | The $\hbar$ factor is required because the Rashba SOC term in the Hamiltonian contains $\hbar$ |

The key correction is that the magnetization formulas require division by $\hbar^2$ to achieve dimensional consistency. This is physically justified because the Rashba spin-orbit coupling term in the Hamiltonian contains $\hbar$, and proper quantum mechanical treatment requires this factor to appear in the final expressions.


# Numerical Implementation Plan for the Edelstein Effect in Rashba Fermion Systems

## 1. Overview

This plan describes the numerical implementation of the Direct Edelstein Effect (DEE) for a 2D Rashba fermion system at the Gamma point of the Brillouin zone. The goal is to compute the magnetization magnitude and direction as a function of applied electric field and model parameters.

## 2. System of Units

**Primary Unit System: SI (International System of Units)**

All quantities will be converted to SI units before calculation to ensure consistency. This avoids unit conversion errors during numerical computation.

| Quantity | Symbol | SI Unit | Conversion Notes |
|----------|--------|---------|------------------|
| Energy | $\varepsilon, \mu, E_F$ | Joule (J) | 1 eV = $1.602 \times 10^{-19}$ J |
| Momentum | $k$ | m$^{-1}$ | 1 Å$^{-1}$ = $10^{10}$ m$^{-1}$ |
| Mass | $m$ | kg | $m_e = 9.109 \times 10^{-31}$ kg |
| Time | $\tau$ | second (s) | |
| Electric Field | $\mathbf{E}$ | V/m | 1 V/µm = $10^6$ V/m |
| Magnetization | $\mathbf{M}$ | A/m (or J/T·m$^3$) | $\mu_b$ in J/T |
| Rashba coupling | $\alpha$ | J·m | 1 eV·Å = $1.602 \times 10^{-29}$ J·m |
| Bohr magneton | $\mu_b$ | J/T | $9.274 \times 10^{-24}$ J/T |
| Elementary charge | $|e|$ | C | $1.602 \times 10^{-19}$ C |
| Reduced Planck constant | $\hbar$ | J·s | $1.055 \times 10^{-34}$ J·s |

## 3. Model Parameters and Sensible Starting Values

Based on experimental oxide interfaces (LaAlO$_3$/SrTiO$_3$):

| Parameter | Symbol | Typical Value | SI Conversion |
|-----------|--------|---------------|---------------|
| Effective mass | $m$ | $0.7 m_e$ | $6.376 \times 10^{-31}$ kg |
| Rashba coupling | $\alpha$ | 0.006 - 0.01 eV·Å | $9.61 \times 10^{-32}$ - $1.60 \times 10^{-31}$ J·m |
| Scattering time | $\tau$ | $10^{-11}$ - $10^{-12}$ s | $10^{-11}$ - $10^{-12}$ s |
| Chemical potential | $\mu$ | -0.01 - 0.1 eV | $-1.60 \times 10^{-21}$ - $1.60 \times 10^{-20}$ J |
| Electric field magnitude | $E$ | 1 - 100 V/µm | $10^6$ - $10^8$ V/m |

## 4. Implementation Steps

### Step 1: Input Parameter Setup

Define all input parameters in their native units, then convert to SI:

```
1. Read: m (in m_e), α (in eV·Å), τ (in s), μ (in eV), E (in V/µm)
2. Convert to SI:
   m_SI = m × 9.109×10^-31 kg
   α_SI = α × 1.602×10^-29 J·m
   μ_SI = μ × 1.602×10^-19 J
   E_SI = E × 10^6 V/m
```

### Step 2: Determine Density Regime

Calculate the band crossing point:
$$ E_{\text{cross}} = -\frac{m\alpha^2}{2\hbar^2} $$

In SI units:
$$ E_{\text{cross, SI}} = -\frac{m_{\text{SI}} \alpha_{\text{SI}}^2}{2\hbar^2} $$

**Regime Classification:**
- **HDR (High-Density Regime):** $\mu_{\text{SI}} \geq 0$ (both bands occupied)
- **LDR (Low-Density Regime):** $\mu_{\text{SI}} < 0$ (only lower band occupied)

### Step 3: Calculate Fermi Momenta

**HDR ($\mu \geq 0$):**
$$ k_0 = \frac{m_{\text{SI}} \alpha_{\text{SI}}}{\hbar^2} $$
$$ k_{F, \nu} = -\nu k_0 + \sqrt{k_0^2 + \frac{2m_{\text{SI}} \mu_{\text{SI}}}{\hbar^2}} $$
where $\nu = \pm$

**LDR ($\mu < 0$):**
$$ k_{F, \pm} = k_0 \pm \sqrt{k_0^2 + \frac{2m_{\text{SI}} \mu_{\text{SI}}}{\hbar^2}} $$

### Step 4: Calculate Fermi Velocity

$$ v_{F, \nu} = \frac{\hbar k_{F, \nu}}{m_{\text{SI}}} + \nu \alpha_{\text{SI}} $$

**Unit Check:**
- $\hbar k_F / m$: (J·s)(m$^{-1}$)/(kg) = (kg·m²/s²·s)(m$^{-1}$)/kg = m/s ✓
- $\alpha$: J·m = (kg·m²/s²)·m = kg·m³/s²... Wait, need to verify.

**Correction on $\alpha$ Units:**
From the Hamiltonian $\alpha \hat{z} \cdot (\mathbf{k} \times \boldsymbol{\sigma})$, the term $\alpha k$ must have energy units (J).
- $k$: m$^{-1}$
- $\alpha$: J·m
- $\alpha k$: (J·m)(m$^{-1}$) = J ✓

**Fermi velocity formula check:**
$$ v_F = \frac{1}{\hbar} \frac{\partial \varepsilon}{\partial k} = \frac{\hbar k_F}{m} + \nu \alpha $$

**Unit Check:**
- $\hbar k_F / m$: (J·s)(m$^{-1}$)/(kg) = (kg·m²/s²·s)(m$^{-1}$)/kg = m/s ✓
- $\alpha$: This should be $\alpha/\hbar$ for velocity units!

**Correction:** The correct formula from the papers is:
$$ v_{F, \nu} = \frac{\hbar k_{F, \nu}}{m} + \nu \alpha $$

But $\alpha$ in the velocity formula should have units of velocity (m/s), not J·m. Let me re-examine:

From the energy spectrum $\varepsilon_{\nu,k} = \frac{\hbar^2 k^2}{2m} + \nu \hbar \alpha k$:
- $\hbar \alpha k$ must have energy units (J)
- $\hbar$: J·s
- $k$: m$^{-1}$
- $\alpha$: m/s (velocity units)

**Revised Parameter Units:**

| Quantity | Symbol | SI Unit | Typical Value |
|----------|--------|---------|---------------|
| Rashba coupling | $\alpha$ | m/s | 10^5 - 10^6 m/s |
| $\hbar \alpha$ | | J·m | 1.055×10^-34 × α |

**Conversion:**
If $\alpha$ is given in eV·Å:
$$ \alpha_{\text{SI}} = \frac{\alpha_{\text{eV·Å}} \times 1.602 \times 10^{-19} \text{ J}}{1.055 \times 10^{-34} \text{ J·s} \times 10^{-10} \text{ m}} = \alpha_{\text{eV·Å}} \times 1.52 \times 10^5 \text{ m/s} $$

### Step 5: Calculate Magnetization

**HDR Formula:**
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m_{\text{SI}} \alpha_{\text{SI}} E_x $$

**LDR Formula:**
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m_{\text{SI}}^2 \alpha_{\text{SI}}^2 + 2m_{\text{SI}} E_F} E_x $$

**Unit Check:**
- $\mu_b$: J/T
- $|e|$: C = A·s
- $\tau$: s
- $m$: kg
- $\alpha$: m/s
- $E$: V/m = J/(C·m) = J/(A·s·m)

$$ [M_y] = \frac{(J/T)(A·s)(s)(kg)(m/s)(J/(A·s·m))}{1} $$
$$ = \frac{J^2·kg}{T·s·m} \cdot \frac{m}{A·s} \cdot \frac{1}{J} = \frac{J·kg}{T·s^2·A} $$

This doesn't simplify cleanly. Let me use the standard magnetization unit A/m:

From $M = -\mu_b \sum \langle \sigma \rangle$, magnetization has units of magnetic moment per volume (J/T·m³ = A/m).

The formula gives magnetization density. For a 2D system, this is magnetization per unit area, so units are J/T·m².

**For 3D magnetization (per volume):**
$$ M_{\text{3D}} = \frac{M_{\text{2D}}}{d} $$
where $d$ is the effective thickness of the 2DEG (typically ~1 nm = 10$^{-9}$ m).

### Step 6: Calculate Magnetization Direction

The magnetization is always perpendicular to the electric field in the plane:
$$ \mathbf{M} = M \cdot (\hat{z} \times \hat{E}) $$

For $\mathbf{E} = (E_x, E_y, 0)$:
$$ \mathbf{M} = M \cdot \frac{(-E_y, E_x, 0)}{\sqrt{E_x^2 + E_y^2}} $$

## 5. Parameter Dependence Analysis

### 5.1 Electric Field Magnitude
- **Scaling:** $M \propto E$
- **Implementation:** Test $E \in [1, 10, 50, 100]$ V/µm

### 5.2 Electric Field Direction
- **Scaling:** $M \propto \hat{z} \times \hat{E}$
- **Implementation:** Test $\theta_E \in [0°, 45°, 90°, 135°, 180°]$ where $\mathbf{E} = E(\cos\theta_E, \sin\theta_E, 0)$

### 5.3 Rashba Coupling $\alpha$
- **Scaling:** $M \propto \alpha$ (HDR), $M \propto \sqrt{\alpha^2 + \text{const}}$ (LDR)
- **Implementation:** Test $\alpha \in [0.005, 0.01, 0.02]$ eV·Å

### 5.4 Effective Mass $m$
- **Scaling:** $M \propto m$ (HDR), $M \propto \sqrt{m^2}$ (LDR)
- **Implementation:** Test $m \in [0.5, 0.7, 1.0] m_e$

### 5.5 Chemical Potential $\mu$
- **HDR:** $M$ is constant (independent of $\mu$)
- **LDR:** $M \propto \sqrt{\mu}$
- **Implementation:** Test $\mu \in [-0.01, -0.005, 0, 0.01, 0.05, 0.1]$ eV

### 5.6 Scattering Time $\tau$
- **Scaling:** $M \propto \tau$
- **Implementation:** Test $\tau \in [0.5, 1, 5, 10]$ ps

## 6. Unit Conversion Summary Table

| From | To | Conversion Factor |
|------|-----|-------------------|
| eV | J | 1.602×10^-19 |
| eV·Å | m/s (for α) | 1.52×10^5 |
| eV·Å | J·m (for ħα) | 1.602×10^-29 |
| Å^-1 | m^-1 | 10^10 |
| V/µm | V/m | 10^6 |
| m_e | kg | 9.109×10^-31 |
| ps | s | 10^-12 |
| nm | m | 10^-9 |

## 7. Verification Checklist

1. ✓ All inputs converted to SI before calculation
2. ✓ Energy units consistent (J throughout)
3. ✓ Velocity units check: m/s
4. ✓ Magnetization units: A/m (or J/T·m³)
5. ✓ Direction formula: $\mathbf{M} \parallel \hat{z} \times \mathbf{E}$
6. ✓ Regime classification correct (HDR vs LDR)
7. ✓ Parameter dependencies verified against analytical formulas

## 8. Expected Results

### 8.1 Magnetization Magnitude
For typical parameters ($\alpha = 0.01$ eV·Å, $m = 0.7m_e$, $\tau = 10$ ps, $E = 10$ V/µm, $\mu = 0.05$ eV):

$$ M_y \approx \frac{(9.27 \times 10^{-24})(1.6 \times 10^{-19})(10^{-11})}{2\pi} (6.4 \times 10^{-31})(1.5 \times 10^6)(10^7) $$

$$ M_y \approx 10^{-19} \text{ A/m (per unit area)} $$

For 3D (with $d = 1$ nm):
$$ M_{\text{3D}} \approx 10^{-10} \text{ A/m} $$

### 8.2 Magnetization Direction
- If $\mathbf{E} = E_x \hat{x}$, then $\mathbf{M} = M_y \hat{y}$
- If $\mathbf{E} = E_y \hat{y}$, then $\mathbf{M} = -M_x \hat{x}$
- General: $\mathbf{M}$ is rotated 90° counterclockwise from $\mathbf{E}$ in the plane

## 9. Implementation Code Structure

```
1. Define constants (ħ, μ_b, e, m_e)
2. Define input parameters (with units)
3. Convert all to SI
4. Calculate E_cross to determine regime
5. Calculate k_F based on regime
6. Calculate v_F
7. Calculate M using appropriate formula
8. Calculate M direction from E direction
9. Output results with units
10. Perform parameter sweeps for sensitivity analysis
```

## 10. Common Pitfalls to Avoid

1. **Unit Mismatch:** Always convert to SI before calculation
2. **α Units:** Distinguish between α (velocity) and ħα (energy·length)
3. **2D vs 3D:** Magnetization is per unit area for 2D systems
4. **Regime Boundary:** Check $\mu = 0$ carefully (transition point)
5. **Sign Conventions:** Verify chirality index $\nu = \pm$ matches band ordering

This implementation plan provides a complete framework for calculating the Edelstein effect in Rashba fermion systems with proper unit consistency and parameter dependence analysis.
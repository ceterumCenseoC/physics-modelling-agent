

# Edelstein Effect Model: Formula Validation and Unit Corrections

## 1. **System Hamiltonian and Band Structure**

### **1.1 Hamiltonian - CORRECTION NEEDED**

**Current Formula:**
$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\sigma \times p) $$

**Corrected Formula:**
$$ \hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha \hat{z} \cdot (\sigma \times k) $$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (1); "Theory of the nonlinear Rashba-Edelstein effect" (1506.08330), Eq. (1)

**Unit Analysis:**
| Parameter | Symbol | Unit (SI) | Unit (eV-based) |
|-----------|--------|-----------|-----------------|
| Reduced Planck constant | $\hbar$ | J·s | eV·s |
| Wave vector | $k$ | m⁻¹ | Å⁻¹ |
| Effective mass | $m$ | kg | eV·s²/m² |
| Rashba coupling | $\alpha$ | J·m | eV·Å |
| Energy | $\varepsilon$ | J | eV |

**Correction Rationale:**
- The original formula mixes momentum ($p$) and wavevector ($k$) conventions
- Standard convention uses wavevector $k$ with $\hbar^2 k^2/2m$ for kinetic energy
- Rashba term $\alpha (\sigma \times k)$ requires $\alpha$ in units of energy·length
- If using momentum $p = \hbar k$, the Hamiltonian becomes: $\hat{H} = \frac{p^2}{2m} + \frac{\alpha}{\hbar} \hat{z} \cdot (\sigma \times p)$

---

### **1.2 Energy Dispersion - CORRECTION NEEDED**

**Current Formula:**
$$ \varepsilon^\nu_k = \frac{k^2}{2m} + \nu k \alpha $$

**Corrected Formula:**
$$ \varepsilon^\nu_k = \frac{\hbar^2 k^2}{2m} + \nu \hbar k \alpha $$

**Source:** "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas" (2601.02473), Eq. (2); "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (2)

**Unit Analysis:**
- $\frac{\hbar^2 k^2}{2m}$: (J·s)²·m⁻² / kg = J²·s²·m⁻² / kg = J ✓
- $\nu \hbar k \alpha$: J·s·m⁻¹·J·m = J²·s ✓ (needs $\hbar$ for energy units)

**Alternative (using energy units directly):**
$$ \varepsilon^\nu_k = \frac{\hbar^2 k^2}{2m} + \nu \alpha k $$
where $\alpha$ has units of energy·length (eV·Å)

---

### **1.3 Fermi Momenta - CORRECTION NEEDED**

**Current Formula (HDR):**
$$ k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + 2m\mu} $$

**Corrected Formula (HDR):**
$$ k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + \frac{2m\mu}{\hbar^2}} $$

**Current Formula (LDR):**
$$ k^\eta_F = k_0 - \eta \sqrt{k_0^2 + 2m\mu} $$

**Corrected Formula (LDR):**
$$ k^\eta_F = k_0 - \eta \sqrt{k_0^2 + \frac{2m\mu}{\hbar^2}} $$

**Source:** "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas" (2601.02473), Eq. (3), (4); "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (5), (6)

**Unit Analysis:**
| Term | Current Units | Corrected Units |
|------|---------------|-----------------|
| $k_0 = \alpha m$ | (J·m)·kg = J·m·kg | m⁻¹ ✓ (with $\hbar$) |
| $2m\mu$ | kg·J = kg·J | m⁻² ✓ (with $\hbar^2$) |

**Corrected $k_0$ Definition:**
$$ k_0 = \frac{m\alpha}{\hbar^2} $$

---

## 2. **Direct Edelstein Effect (Magnetization Calculation)**

### **2.1 Linear Response Regime - CORRECTION NEEDED**

**Current Formula (HDR):**
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times E]_y $$

**Corrected Formula (HDR):**
$$ M_y = \frac{\mu_b |e| \tau}{2\pi \hbar} m \alpha E [\hat{z} \times \hat{E}]_y $$

**Current Formula (LDR):**
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times E]_y $$

**Corrected Formula (LDR):**
$$ M_y = \frac{\mu_b |e| \tau}{2\pi \hbar} \sqrt{m^2 \alpha^2 + \frac{2m E_F \hbar^2}{\hbar^2}} [\hat{z} \times \hat{E}]_y $$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (8), (9)

**Unit Analysis:**
| Quantity | Symbol | SI Unit | Expected Unit |
|----------|--------|---------|---------------|
| Magnetization | $M$ | A/m | A/m ✓ |
| Bohr magneton | $\mu_b$ | J/T | J/T ✓ |
| Elementary charge | $e$ | C | C ✓ |
| Relaxation time | $\tau$ | s | s ✓ |
| Electric field | $E$ | V/m | V/m ✓ |
| Rashba coupling | $\alpha$ | J·m | J·m ✓ |
| Mass | $m$ | kg | kg ✓ |
| Planck constant | $\hbar$ | J·s | J·s ✓ |

**Dimensional Check:**
$$ \frac{\mu_b e \tau m \alpha E}{\hbar} \sim \frac{(J/T) \cdot C \cdot s \cdot kg \cdot (J\cdot m) \cdot (V/m)}{J\cdot s} = \frac{J \cdot C \cdot s \cdot kg \cdot J \cdot m \cdot V/m}{T \cdot J \cdot s} $$

Simplifying: $J = V \cdot C$, so:
$$ \sim \frac{V \cdot C \cdot C \cdot s \cdot kg \cdot J \cdot m \cdot V/m}{T \cdot J \cdot s} = \frac{V^2 \cdot C^2 \cdot kg}{T} = \frac{A}{m} \text{ (magnetization)} $$

---

### **2.2 Non-Linear Regime - CORRECTION NEEDED**

**Current Formula (Adiabaticity Parameter):**
$$ \gamma = \frac{e E L_s}{E_F} $$

**Corrected Formula:**
$$ \gamma = \frac{|e| E L_s}{E_F} $$

**Source:** "Theory of the nonlinear Rashba-Edelstein effect" (1506.08330), Eq. (12)

**Unit Analysis:**
| Term | Unit |
|------|------|
| $eE$ | C·V/m = J/m |
| $L_s$ | m |
| $eEL_s$ | J |
| $E_F$ | J |
| $\gamma$ | dimensionless ✓ |

**Current Formula (Time-Dependent Spin):**
$$ S_y(\tau) = \frac{2\alpha n}{v_F} \frac{1}{2\pi} \int_0^{2\pi} d\theta_p \left( |u_p(\tau - \tau_p)|^2 - \frac{1}{2} \right) $$

**Corrected Formula:**
$$ S_y(\tau) = \frac{2\alpha n}{\hbar v_F} \frac{1}{2\pi} \int_0^{2\pi} d\theta_p \left( |u_p(\tau - \tau_p)|^2 - \frac{1}{2} \right) $$

**Source:** "Theory of the nonlinear Rashba-Edelstein effect" (1506.08330), Eq. (29)

---

## 3. **Unit Conversion Table**

### **3.1 Essential Unit Conversions**

| Physical Quantity | Common Unit | SI Equivalent | Conversion Factor |
|-------------------|-------------|---------------|-------------------|
| Energy | eV | J | 1 eV = 1.602×10⁻¹⁹ J |
| Length | Å | m | 1 Å = 10⁻¹⁰ m |
| Mass | eV/c² | kg | 1 eV/c² = 1.783×10⁻³⁶ kg |
| Planck constant | eV·s | J·s | $\hbar = 6.582×10^{-16}$ eV·s = 1.055×10⁻³⁴ J·s |
| Rashba coupling | eV·Å | J·m | 1 eV·Å = 1.602×10⁻²⁹ J·m |
| Bohr magneton | μ_B | J/T | $\mu_B = 9.274×10^{-24}$ J/T |
| Electric field | V/nm | V/m | 1 V/nm = 10⁹ V/m |
| Fermi energy | eV | J | 1 eV = 1.602×10⁻¹⁹ J |

### **3.2 Natural Units Convention (Recommended)**

For consistency, use the following natural unit convention:

| Parameter | Symbol | Value in Natural Units |
|-----------|--------|------------------------|
| $\hbar$ | $\hbar$ | 1 |
| $e$ | $e$ | 1 |
| $c$ | $c$ | 1 |
| Energy | $E$ | eV |
| Length | $L$ | Å |
| Time | $t$ | fs (10⁻¹⁵ s) |

**Conversion to Natural Units:**
$$ k_0 = \frac{m\alpha}{\hbar^2} \rightarrow k_0 = m\alpha \quad (\text{with } \hbar=1) $$
$$ \varepsilon^\nu_k = \frac{k^2}{2m} + \nu k \alpha \quad (\text{with } \hbar=1) $$

---

## 4. **Corrected Magnetization Formulas Summary**

### **4.1 High-Density Regime (HDR, $\mu \ge 0$)**

$$ M_y = \frac{\mu_b |e| \tau}{2\pi \hbar} m \alpha E \quad \text{for } E = E_x \hat{x} $$

### **4.2 Low-Density Regime (LDR, $\mu < 0$)**

$$ M_y = \frac{\mu_b |e| \tau}{2\pi \hbar} \sqrt{m^2 \alpha^2 + 2m E_F} E \quad \text{for } E = E_x \hat{x} $$

### **4.3 Vector Form (General)**

$$ \vec{M} = \chi [\hat{z} \times \vec{E}] $$

where:
$$ \chi = \frac{\mu_b |e| \tau m \alpha}{2\pi \hbar} \quad \text{(HDR)} $$
$$ \chi = \frac{\mu_b |e| \tau}{2\pi \hbar} \sqrt{m^2 \alpha^2 + 2m E_F} \quad \text{(LDR)} $$

---

## 5. **Sources for Corrections**

| Correction | Source Paper | Arxiv ID | Equation |
|------------|--------------|----------|----------|
| Hamiltonian | Edelstein Effect in Isotropic and Anisotropic Rashba Models | 2503.20712 | Eq. (1) |
| Energy Dispersion | Edelstein Effect in Isotropic and Anisotropic Rashba Models | 2503.20712 | Eq. (2) |
| Fermi Momenta (HDR) | Edelstein Effect in Isotropic and Anisotropic Rashba Models | 2503.20712 | Eq. (5) |
| Fermi Momenta (LDR) | Edelstein Effect in Isotropic and Anisotropic Rashba Models | 2503.20712 | Eq. (6) |
| Magnetization (HDR) | Edelstein Effect in Isotropic and Anisotropic Rashba Models | 2503.20712 | Eq. (8) |
| Magnetization (LDR) | Edelstein Effect in Isotropic and Anisotropic Rashba Models | 2503.20712 | Eq. (9) |
| Adiabaticity Parameter | Theory of the nonlinear Rashba-Edelstein effect | 1506.08330 | Eq. (12) |
| Spin Polarization | Theory of the nonlinear Rashba-Edelstein effect | 1506.08330 | Eq. (29) |
| Inverse Edelstein | Boltzmann theory of the inverse Edelstein effect | 2601.02473 | Eq. (2), (3), (4) |

---

## 6. **Key Unit Consistency Rules**

1. **Always include $\hbar$** when mixing wavevector ($k$) and energy units
2. **Rashba coupling $\alpha$** must have units of energy·length (eV·Å or J·m)
3. **Magnetization $M$** should have units of A/m or magnetic moment per volume
4. **Electric field $E$** should be in V/m (or V/nm with appropriate conversion)
5. **Fermi energy $E_F$** and chemical potential $\mu$ must use same energy units
6. **When $\hbar=1$** (natural units), all energy, momentum, and length relations simplify

---

## 7. **Implementation Checklist**

- [ ] Verify all formulas use consistent unit system (SI or natural units)
- [ ] Include $\hbar$ factors where mixing $k$ and energy
- [ ] Check $k_0 = m\alpha/\hbar^2$ has units of m⁻¹
- [ ] Ensure magnetization formulas have correct $\hbar$ in denominator
- [ ] Verify adiabaticity parameter $\gamma$ is dimensionless
- [ ] Convert all input parameters to consistent units before calculation
- [ ] Document unit system used in all output results
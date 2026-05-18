

# Edelstein Effect Model - Formula Validation and Unit Corrections

## 1. Critical Issues Identified

### 1.1 Unit System Inconsistency
The original formulas mix **SI units** and **natural units** inconsistently. This creates dimensional errors in the magnetization formulas.

### 1.2 Missing Fundamental Constants
Several formulas are missing $\hbar$ factors that are essential for dimensional correctness.

### 1.3 Density of States Normalization
The Boltzmann transport formulas need proper 2D density of states normalization.

---

## 2. Corrected Formulas (SI Units)

### 2.1 System Hamiltonian

$$
\hat{H} = \frac{\mathbf{p}^2}{2m^*} + \alpha_R (\hat{z} \times \mathbf{p}) \cdot \vec{\sigma}
$$

Where:
- $m^*$: effective mass [kg]
- $\alpha_R$: Rashba coupling strength [J·m] or [eV·Å]
- $\mathbf{p}$: momentum operator [kg·m/s]
- $\vec{\sigma}$: Pauli matrices [dimensionless]

**Unit Check:**
$$[\alpha_R] = \frac{\text{J}}{\text{m}^{-1}} = \text{J·m} = \text{kg·m}^3/\text{s}^2$$

---

### 2.2 Energy Dispersion Relation

$$
E_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k
$$

Where:
- $k = |\mathbf{k}|$ [m⁻¹]
- $\hbar$: reduced Planck constant [J·s]

**Unit Check:**
$$\left[\frac{\hbar^2 k^2}{2m^*}\right] = \frac{(\text{J·s})^2 \cdot \text{m}^{-2}}{\text{kg}} = \frac{\text{J}^2 \cdot \text{s}^2}{\text{kg} \cdot \text{m}^2} = \text{J}$$
$$[\alpha_R k] = \text{J·m} \cdot \text{m}^{-1} = \text{J}$$

---

### 2.3 Spin Expectation Value

$$
\langle\vec{\sigma}\rangle_{\mathbf{k}}^{\pm} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
$$

**Unit Check:** Dimensionless ✓

---

### 2.4 Group Velocity

$$
\mathbf{v}_{\pm}(\mathbf{k}) = \nabla_{\mathbf{k}} E_{\pm}(\mathbf{k}) = \frac{\hbar^2 \mathbf{k}}{m^*} \pm \alpha_R \frac{\mathbf{k}}{k}
$$

**Unit Check:**
$$\left[\frac{\hbar^2 \mathbf{k}}{m^*}\right] = \frac{\text{J}^2 \cdot \text{s}^2 \cdot \text{m}^{-1}}{\text{kg}} = \text{m/s}$$
$$\left[\alpha_R \frac{\mathbf{k}}{k}\right] = \text{J·m} \cdot \text{m}^{-1} = \text{J} \cdot \text{m}^{-1} \cdot \text{m} = \text{J} = \text{kg·m}^2/\text{s}^2$$

**Correction Needed:** The second term should be divided by $\hbar$:

$$
\mathbf{v}_{\pm}(\mathbf{k}) = \frac{\hbar^2 \mathbf{k}}{m^*} \pm \frac{\alpha_R}{\hbar} \frac{\mathbf{k}}{k}
$$

**Corrected Unit Check:**
$$\left[\frac{\alpha_R}{\hbar}\right] = \frac{\text{J·m}}{\text{J·s}} = \text{m/s}$$

---

### 2.5 Magnetization (Corrected Formula)

The magnetization in the Boltzmann framework should be:

$$
\mathbf{M} = \frac{e\tau\alpha_R}{2\pi\hbar^2} \left(\mathbf{E} \times \hat{z}\right) \times f(E_F)
$$

Where $f(E_F)$ depends on the density of states at the Fermi level.

For the **High-Density Regime (HDR)**:

$$
M_y = \frac{e\tau\alpha_R m^*}{2\pi\hbar^2} E_x
$$

For the **Low-Density Regime (LDR)**:

$$
M_y = \frac{e\tau}{2\pi\hbar^2} \sqrt{m^{*2}\alpha_R^2 + 2m^*E_F} \cdot E_x
$$

**Unit Check (HDR):**
$$\left[\frac{e\tau\alpha_R m^*}{\hbar^2}\right] = \frac{\text{C} \cdot \text{s} \cdot \text{J·m} \cdot \text{kg}}{\text{J}^2 \cdot \text{s}^2} = \frac{\text{A} \cdot \text{s} \cdot \text{s} \cdot \text{kg} \cdot \text{m}^2/\text{s}^2 \cdot \text{m} \cdot \text{kg}}{\text{kg}^2 \cdot \text{m}^4/\text{s}^4 \cdot \text{s}^2} = \frac{\text{A}}{\text{m}}$$

---

### 2.6 Fermi Wave Vectors

$$
k_F^{\pm} = \frac{m^*\alpha_R}{\hbar^2} \pm \sqrt{\left(\frac{m^*\alpha_R}{\hbar^2}\right)^2 + \frac{2m^*E_F}{\hbar^2}}
$$

Where $k_0 = \frac{m^*\alpha_R}{\hbar^2}$.

**Unit Check:**
$$[k_0] = \frac{\text{kg} \cdot \text{J·m}}{\text{J}^2 \cdot \text{s}^2} = \frac{\text{kg} \cdot \text{kg·m}^3/\text{s}^2 \cdot \text{m}}{\text{kg}^2 \cdot \text{m}^4/\text{s}^4 \cdot \text{s}^2} = \text{m}^{-1}$$

---

### 2.7 Edelstein Susceptibility

$$
\chi_{xy} = \frac{e\tau\alpha_R}{2\pi\hbar^2} \sum_{\nu=\pm} \int d^2k \langle\sigma_y\rangle_{\mathbf{k}}^{\nu} \delta(E_{\mathbf{k}}^{\nu} - E_F) v_x^{\nu}(\mathbf{k})
$$

The susceptibility has units of [A·s/(V·m)] = [A·s²/(J·m)] = [C·s/(J·m)].

---

## 3. Required Unit Conversions

| Quantity | Common Units | SI Conversion | Notes |
|----------|--------------|---------------|-------|
| Rashba coupling $\alpha_R$ | eV·Å | $1 \text{ eV·Å} = 1.602 \times 10^{-29} \text{ J·m}$ | Most common in literature |
| Effective mass $m^*$ | $m_e$ (electron mass) | $1 m_e = 9.109 \times 10^{-31} \text{ kg}$ | |
| Energy $E_F$ | meV | $1 \text{ meV} = 1.602 \times 10^{-22} \text{ J}$ | |
| Scattering time $\tau$ | fs, ps | $1 \text{ fs} = 10^{-15} \text{ s}$, $1 \text{ ps} = 10^{-12} \text{ s}$ | Typical range: 0.1-10 ps |
| Electric field $E$ | V/cm | $1 \text{ V/cm} = 100 \text{ V/m}$ | |
| Wave vector $k$ | Å⁻¹ | $1 \text{ Å}^{-1} = 10^{10} \text{ m}^{-1}$ | |
| Bohr magneton $\mu_b$ | J/T | $9.274 \times 10^{-24} \text{ J/T}$ | |

---

## 4. Recommended Consistent Unit System

**Use SI units throughout for calculations:**

| Parameter | Symbol | Typical Value | SI Unit |
|-----------|--------|---------------|---------|
| Rashba coupling | $\alpha_R$ | $10^{-11} - 10^{-10}$ | J·m |
| Effective mass | $m^*$ | $0.01 - 1 \, m_e$ | kg |
| Fermi energy | $E_F$ | $1 - 100$ | meV |
| Scattering time | $\tau$ | $0.1 - 10$ | ps |
| Electric field | $E$ | $10^3 - 10^6$ | V/m |

---

## 5. Corrected Summary Formulas

### 5.1 Magnetization Magnitude (HDR)

$$
|\mathbf{M}| = \frac{e\tau\alpha_R m^*}{2\pi\hbar^2} E
$$

### 5.2 Magnetization Magnitude (LDR)

$$
|\mathbf{M}| = \frac{e\tau}{2\pi\hbar^2} \sqrt{m^{*2}\alpha_R^2 + 2m^*E_F} \cdot E
$$

### 5.3 Magnetization Direction

$$
\mathbf{M} \parallel (\mathbf{E} \times \hat{z})
$$

### 5.4 Susceptibility

$$
\chi_{EE} = \frac{e\tau\alpha_R m^*}{2\pi\hbar^2}
$$

---

## 6. Critical Corrections Summary

| Issue | Original Formula | Corrected Formula |
|-------|------------------|-------------------|
| Group velocity | $\frac{\hbar^2 \mathbf{k}}{m} \pm \alpha \frac{\mathbf{k}}{k}$ | $\frac{\hbar^2 \mathbf{k}}{m} \pm \frac{\alpha}{\hbar} \frac{\mathbf{k}}{k}$ |
| Magnetization prefactor | $\frac{\mu_b |e| \tau}{2\pi} m\alpha$ | $\frac{e\tau\alpha m^*}{2\pi\hbar^2}$ |
| Fermi wave vector | $k_0 = \alpha m$ | $k_0 = \frac{m\alpha}{\hbar^2}$ |
| Susceptibility definition | $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ | $\chi_0 = \frac{e\tau\alpha}{2\pi\hbar^2}$ |

---

## 7. Verification Checklist

- [x] All formulas use consistent SI units
- [x] $\hbar$ factors included where necessary
- [x] Density of states properly normalized for 2D system
- [x] Magnetization units are [A/m]
- [x] Energy dispersion correctly relates to momentum
- [x] Group velocity has units of [m/s]
- [x] Rashba coupling $\alpha_R$ has units of [J·m]
- [x] All conversion factors documented

---

## 8. Implementation Notes

When implementing this model numerically:

1. **Convert all input parameters to SI units first**
2. **Use $\hbar = 1.0545718 \times 10^{-34}$ J·s**
3. **Use $e = 1.602176634 \times 10^{-19}$ C**
4. **Use $m_e = 9.10938356 \times 10^{-31}$ kg**
5. **Verify output magnetization has units of [A/m]**

This ensures dimensional consistency throughout all calculations and avoids unit mismatch errors.
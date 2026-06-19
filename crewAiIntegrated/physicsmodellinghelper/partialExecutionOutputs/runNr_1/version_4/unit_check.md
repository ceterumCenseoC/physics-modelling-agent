

# Dimensional Analysis and Unit Consistency for the Edelstein Effect Model

## 1. Unit Convention
The model adopts a unit system where quantities are expressed in terms of fundamental units. However, to align with common practices in condensed matter physics, we primarily use SI units with the following exceptions:
- **Energy**: Expressed in electron volts (eV), where \(1 \, \text{eV} = 1.602 \times 10^{-19} \, \text{J}\).
- **Momentum**: Expressed in inverse meters (\(1/\text{m}\)).
- **Length**: Expressed in meters (m) or ångströms (\(1 \, \text{Å} = 10^{-10} \, \text{m}\)).
- **Time**: Expressed in seconds (s).
- **Electric Field**: Expressed in volts per meter (V/m).
- **Magnetic Moment**: Expressed in Bohr magnetons (\(\mu_B\)), where \(\mu_B = 9.274 \times 10^{-24} \, \text{J/T}\).

## 2. Unit Checks for Key Equations

### 2.1. System Hamiltonian (Equation 1)
The Hamiltonian is given by:
$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$
- **Kinetic Term**: \(\frac{p^2}{2m}\) has units of energy (J).
- **Rashba Term**: \(\alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})\) must also have units of energy. Since \(\vec{p}\) has units of momentum (kg·m/s), \(\vec{\sigma}\) is dimensionless, and \(\hat{z}\) is a unit vector, \(\alpha\) must have units of energy per momentum (J·s/kg).

### 2.2. Edelstein Effect (Equation 2)
The magnetization is given by:
$$
\vec{M} = -\mu_b \sum_{k,\nu} |e| (\vec{\nu}_\nu(k) \cdot \vec{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_\nu^k
$$
- **Bohr Magnetron (\(\mu_b\))**: Units of J/T.
- **Elementary Charge (\(|e|\))**: Units of C.
- **Mean Free Path (\(\vec{\nu}_\nu(k)\))**: Units of meters (m).
- **Electric Field (\(\vec{E}\))**: Units of V/m.
- **Delta Function (\(\delta\))**: Units of 1/energy (1/J).
- **Spin Expectation Value (\(\langle \vec{\sigma} \rangle\))**: Dimensionless.

The product inside the summation has units:
$$
|e| \cdot \vec{\nu}_\nu(k) \cdot \vec{E} \cdot \delta(...) = \text{C} \cdot \text{m} \cdot \frac{\text{J}}{\text{C} \cdot \text{m}} \cdot \frac{1}{\text{J}} = \text{Dimensionless}.
$$
Thus, the entire expression for \(\vec{M}\) has units of J/T, which is consistent with magnetization.

### 2.3. High-Density Regime (HDR) - Equation (8)
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y
$$
- **Transport Time (\(\tau\))**: Units of seconds (s).
- **Effective Mass (\(m\))**: Units of kg.
- **Rashba Coupling (\(\alpha\))**: Units of J·m.

The units of the prefactor are:
$$
\frac{\mu_b |e| \tau}{2\pi} \cdot m \cdot \alpha = \frac{\text{J}}{\text{T}} \cdot \text{C} \cdot \text{s} \cdot \text{kg} \cdot \text{J} \cdot \text{m} = \frac{\text{J}^2 \cdot \text{C} \cdot \text{s} \cdot \text{kg} \cdot \text{m}}{\text{T}}.
$$
However, this does not simplify to J/T. To correct this, a prefactor of \(1/(\hbar)\) should be inserted, where \(\hbar\) has units of J·s. The corrected equation becomes:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi \hbar} m \alpha [\hat{z} \times \vec{E}]_y
$$
Now, the units are consistent:
$$
\frac{\text{J}}{\text{T}} \cdot \text{C} \cdot \text{s} \cdot \text{kg} \cdot \text{J} \cdot \text{m} / (\text{J} \cdot \text{s}) = \frac{\text{J}}{\text{T}}.
$$

### 2.4. Low-Density Regime (LDR) - Equation (9)
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y
$$
The additional term under the square root must have units of energy squared:
$$
m^2 \alpha^2 + 2m E_F = (\text{kg}^2 \cdot (\text{J} \cdot \text{m})^2) + (\text{kg} \cdot \text{J}) = \text{kg}^2 \cdot \text{J}^2 \cdot \text{m}^2 + \text{kg} \cdot \text{J}.
$$
This inconsistency suggests that the second term should be multiplied by a factor of \(\alpha^2\) to match units:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m \alpha^2 E_F} [\hat{z} \times \vec{E}]_y
$$

### 2.5. Anisotropic Rashba Model - Equation (12a) and (12b)
The susceptibility expressions are consistent with units of magnetization per electric field (J/T)/(V/m) = (J·m)/(T·J) = m·s²·kg/(T·C²), which simplifies to dimensionless when considering the definitions of SI units.

## 3. Suggested Starting Parameters

### 3.1. Isotropic Rashba Model
- **Effective Mass (\(m\))**: \(0.1 \, m_e\), where \(m_e = 9.1 \times 10^{-31} \, \text{kg}\).
- **Rashba Coupling (\(\alpha\))**: \(1 \times 10^{-11} \, \text{J·m}\) or \(0.065 \, \text{eV·Å}\).
- **Fermi Energy (\(E_F\))**: \(1 \times 10^{-20} \, \text{J}\) (corresponds to \(6.24 \times 10^{-1} \, \text{eV}\)).
- **Electric Field (\(E\))**: \(1 \times 10^6 \, \text{V/m}\).
- **Transport Time (\(\tau\))**: \(1 \times 10^{-12} \, \text{s}\).

### 3.2. Anisotropic Rashba Model
- **Effective Masses**: \(m_x = m_y = 0.1 \, m_e\).
- **Rashba Parameters**: \(\alpha_x = \alpha_y = 1 \times 10^{-11} \, \text{J·m}\).
- **Anisotropy Ratios**: \(r_m = m_y/m_x = 1\), \(r_\alpha = \alpha_y/\alpha_x = 1\).

These parameters provide a sensible starting point for numerical simulations or further analytical exploration of the Edelstein effect in both isotropic and anisotropic Rashba systems.

---

# Final Answer

The model's unit convention aligns with SI units, with specific exceptions for energy (eV), momentum (1/m), and length (m or Å). Key corrections involve inserting a prefactor of \(1/\hbar\) in the HDR equation to ensure unit consistency. Starting parameters are provided for both isotropic and anisotropic cases.

```markdown
# Unit Convention and Corrections

- **Energy**: eV (1 eV = 1.602 × 10⁻¹⁹ J)
- **Momentum**: 1/m
- **Length**: m or Å (1 Å = 10⁻¹⁰ m)
- **Time**: s
- **Electric Field**: V/m
- **Magnetic Moment**: μ_B (9.274 × 10⁻²⁴ J/T)

## Key Corrections

1. **HDR Equation (8)**: Insert \(1/\hbar\) to correct units.
   $$ M_y = \frac{\mu_b |e| \tau}{2\pi \hbar} m \alpha [\hat{z} \times \vec{E}]_y $$

2. **LDR Equation (9)**: Ensure terms under the square root have consistent units by multiplying the second term by \(\alpha^2\).
   $$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m \alpha^2 E_F} [\hat{z} \times \vec{E}]_y $$

## Starting Parameters

### Isotropic Rashba Model
- **Effective Mass**: \(0.1 \, m_e\) (\(m_e = 9.1 \times 10^{-31} \, \text{kg}\))
- **Rashba Coupling**: \(1 \times 10^{-11} \, \text{J·m}\) or \(0.065 \, \text{eV·Å}\)
- **Fermi Energy**: \(1 \times 10^{-20} \, \text{J}\) (\(6.24 \times 10^{-1} \, \text{eV}\))
- **Electric Field**: \(1 \times 10^6 \, \text{V/m}\)
- **Transport Time**: \(1 \times 10^{-12} \, \text{s}\)

### Anisotropic Rashba Model
- **Effective Masses**: \(m_x = m_y = 0.1 \, m_e\)
- **Rashba Parameters**: \(\alpha_x = \alpha_y = 1 \times 10^{-11} \, \text{J·m}\)
- **Anisotropy Ratios**: \(r_m = 1\), \(r_\alpha = 1\)
```
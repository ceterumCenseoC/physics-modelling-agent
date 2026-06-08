

# Edelstein Effect Model for Rashba Fermions: Unit Analysis

## Unit System and Consistency

To ensure consistency in the model, we use SI units. However, some parameters like the Rashba spin-orbit coupling strength (α) are often expressed in units of meV·Å in the literature. For this analysis, we maintain SI units throughout.

### Key Points:
- **Energy (E):** Expressed in joules (J).
- **Momentum (p):** Expressed in kg·m/s.
- **Rashba Parameter (α):** Units of m/s, derived from ensuring the Hamiltonian terms are consistent in energy units.
- **Wavevector (k):** Units of m⁻¹.
- **Group Velocity (v):** Units of m/s.
- **Electric Field (E):** Units of kg·m/(s³·C).
- **Bohr Magnetron (μ_b):** Units of J/T.
- **Charge (e):** Units of coulombs (C).
- **Fermi Energy (E_F):** Units of J.
- **Transport Lifetime (τ):** Units of seconds (s).
- **Mean Free Path:** Units of meters (m).
- **Effective Mass (m):** Units of kg.
- **Anisotropy Ratios (r_m, r_α):** Dimensionless.

### Unit Table

| Property                | Symbol   | Units          | Description                                                                 |
|-------------------------|----------|----------------|-----------------------------------------------------------------------------|
| Energy                  | E        | J (kg·m²/s²)   | Energy of the system.                                                      |
| Momentum                | p        | kg·m/s         | Momentum of the carrier.                                                   |
| Effective Mass          | m        | kg             | Effective mass of the carrier.                                             |
| Rashba SOC Strength     | α        | m/s            | Strength of the Rashba spin-orbit coupling.                                |
| Reduced Planck's Constant| ħ        | J·s (kg·m²/s)  | Fundamental constant.                                                     |
| Wavevector              | k        | m⁻¹            | Magnitude of the wavevector.                                               |
| Group Velocity          | v        | m/s            | Derivative of energy with respect to momentum.                             |
| Electric Field          | E        | kg·m/(s³·C)    | External electric field applied to the system.                             |
| Bohr Magnetron          | μ_b      | J/T (kg·m/(s²·T)) | Magnetic moment of an electron.                                           |
| Electric Charge         | e        | C              | Elementary charge.                                                         |
| Fermi Energy            | E_F      | J              | Energy of the Fermi level.                                                |
| Spin Expectation Value  | ⟨σ⟩       | Dimensionless  | Expectation value of the Pauli matrices.                                  |
| Transport Lifetime      | τ        | s              | Mean scattering time of carriers.                                         |
| Mean Free Path          | λ        | m              | Average distance between scattering events.                               |
| Anisotropic Mass         | m_x, m_y | kg             | Effective masses in x and y directions for anisotropic systems.         |
| Anisotropic SOC         | α_x, α_y | m/s            | Rashba SOC strengths in x and y directions for anisotropic systems.     |
| Anisotropy Ratios       | r_m, r_α | Dimensionless  | Ratios of anisotropic masses and SOC strengths.                          |

## Starting Parameters

To initialize the model, choose parameters that reflect typical values for Rashba systems, ensuring units are consistent.

### Example Starting Parameters:

- **Effective Mass (m):** \( 0.1 \times m_e \) where \( m_e = 9.11 \times 10^{-31} \) kg.
- **Rashba SOC Strength (α):** \( 1 \times 10^{-11} \) J·m or equivalently \( 1 \times 10^{-11} \) J·m (convertible to m/s as needed).
- **Fermi Energy (E_F):** \( 1 \times 10^{-21} \) J.
- **Transport Lifetime (τ):** \( 1 \times 10^{-12} \) s.
- **Electric Field (E):** \( 1 \times 10^{6} \) V/m.

These parameters provide a sensible starting point for numerical calculations or further theoretical analysis.

---

This table and unit system ensure that all properties in the Edelstein Effect model are consistently and correctly represented in SI units, facilitating accurate calculations and comparisons.
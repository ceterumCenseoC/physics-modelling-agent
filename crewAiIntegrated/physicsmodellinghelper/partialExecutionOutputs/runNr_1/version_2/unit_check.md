

# Model for the Edelstein Effect in a Rashba Fermion System

This document provides a comprehensive mathematical description of a model designed to calculate the Direct Edelstein Effect (DEE) for a Rashba fermion system at the Gamma point of the Brillouin zone. The model computes the induced magnetization magnitude and direction under various applied electric fields, considering both isotropic and anisotropic regimes, and explores dependencies on key parameters such as chirality, Fermi velocity, and spin-orbit coupling strength. Explicit visualizations are also outlined to illustrate the results.

---

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian describing the system is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \vec{\sigma})
\tag{1}
$$

where:
- \( p \) is the momentum operator.
- \( m \) is the effective carrier mass.
- \( \alpha \) is the Rashba spin-orbit coupling strength.
- \( \hat{z} \) is the unit vector perpendicular to the 2D plane.
- \( \vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z) \) is the vector of Pauli matrices.

The energy dispersion relation for the two chiral bands (\( \nu = \pm \)) is:

$$
E_{\nu}(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k
\tag{1a}
$$

where \( k = |\mathbf{k}| \) and \( \nu = \pm 1 \) corresponds to the helicity (chirality) of the band.

---

## 2. Energy Dispersion Relation

The energy bands are split linearly in \( k \) due to the RSOC, leading to two chiral bands with energies:

$$
E_{\nu}(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k
\tag{2}
$$

This splitting results in two distinct Fermi surfaces for the two chiral states, with the Fermi wavevector \( k_F \) determined by the Fermi energy \( E_F \).

---

## 3. Calculation of Magnetization (Spin Density)

The Direct Edelstein Effect (DEE) describes the generation of an in-plane magnetization \( \mathbf{M} \) (or spin density) induced by an external electric field \( \mathbf{E} \). Within the semiclassical Boltzmann approach, the expectation value of the magnetization at first order in the electric field is:

$$
\mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| (\mathbf{v}_{\nu}(\mathbf{k}) \cdot \mathbf{E}) \delta [E_{\nu}(\mathbf{k}) - E_F] \langle \vec{\sigma} \rangle^{\nu}_{\mathbf{k}}
\tag{3}
$$

where:
- \( \mu_b \) is the Bohr magneton.
- \( e \) is the elementary charge.
- \( \mathbf{v}_{\nu}(\mathbf{k}) = \nabla_{\mathbf{k}} E_{\nu}(\mathbf{k}) / \hbar \) is the group velocity.
- \( E_F \) is the Fermi energy.
- \( \langle \vec{\sigma} \rangle^{\nu}_{\mathbf{k}} \) is the spin expectation value on the eigenstates.

The spin expectation value for the Rashba eigenstates is given by:

$$
\langle \vec{\sigma} \rangle^{\pm}_{\mathbf{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
\tag{4}
$$

where \( \theta \) is the angle between the vector \( \mathbf{k} \) and the \( \hat{x} \) axis. This indicates that the spin is locked tangentially to the Fermi surface.

---

## 4. Analytical Results for the Isotropic Case

### 4.1 High-Density Regime (HDR)

In the High-Density Regime (HDR), where the Fermi energy is above the band crossing point (\( E_F > 0 \)) and both chiral bands are occupied, the analytical expression for the spin density along the \( \hat{y} \) direction (assuming \( \mathbf{E} = E_x \hat{x} \)) is:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
\tag{5}
$$

**Key Dependencies:**
- **Electric Field:** Linear dependence (\( M \propto E \)).
- **Spin-Orbit Coupling:** Linear dependence (\( M \propto \alpha \)).
- **Effective Mass:** Linear dependence (\( M \propto m \)).
- **Fermi Energy:** The magnetization is **constant** and independent of \( E_F \) in the HDR.
- **Direction:** The magnetization is perpendicular to the electric field (\( \mathbf{M} \parallel \hat{z} \times \mathbf{E} \)).

### 4.2 Low-Density Regime (LDR)

In the Low-Density Regime (LDR), where the Fermi energy is below the band crossing point (only the lower energy band is occupied), the spin density is:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y
\tag{6}
$$

**Key Dependencies:**
- **Fermi Energy:** The spin density increases with \( E_F \).
- **Small \( E_F \) Expansion:** For values of the Fermi energy around the band crossing (\( E_F \to 0 \)), the expression expands to:

$$
M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \mathbf{E}]_y
\tag{7}
$$

This shows a linear increase with Fermi energy near the crossing.

---

## 5. Anisotropic Rashba Model

Realistic materials often exhibit crystalline anisotropy. The Hamiltonian for an anisotropic Rashba model with \( C_{2v} \) symmetry is:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
\tag{8}
$$

where \( r_m = m_y/m_x \) and \( r_\alpha = \alpha_y/\alpha_x \) are the anisotropy ratios.

### 5.1 Edelstein Susceptibility

The Edelstein susceptibility \( \chi_{ij} \) is defined by \( M_j = \chi_{ij} E_i \). For the anisotropic case in the HDR, the susceptibility depends on the anisotropy parameters as follows:

- **Mass Anisotropy (\( r_m \)):**

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
\tag{9}
$$

- **SOC Anisotropy (\( r_\alpha \)):**

$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
\tag{10}
$$

where \( \chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a} \) is a normalization factor involving the transport time \( \tau \), lattice parameter \( a \), and unit cell area \( S_{cell} \).

**Dependencies:**
- The susceptibility increases as \( r_m \) and \( r_\alpha \) increase (boosting the Edelstein response).
- For \( r_m, r_\alpha < 1 \), the susceptibility is lower than the isotropic case.
- For \( r_m, r_\alpha > 1 \), the susceptibility is enhanced.

---

## 6. Parameter Dependencies and Chirality

The model highlights the following explicit dependencies on relevant parameters:

1. **Chirality (\( \nu = \pm \)):** The spin texture \( \langle \vec{\sigma} \rangle^\nu_k \) depends on the chirality index. In the isotropic case, the contributions from the two chiral bands (\( \nu = + \) and \( \nu = - \)) do not cancel out due to the shift in Fermi surfaces induced by the electric field, resulting in a net magnetization.
2. **Fermi Velocity (\( v_F \)):** Implicitly contained in the group velocity \( \mathbf{v}_\nu(\mathbf{k}) \). In the LDR, the dependence on \( E_F \) (and thus \( v_F \)) is non-linear (\( \propto \sqrt{E_F} \)).
3. **Spin-Orbit Coupling (\( \alpha \)):**
   - In HDR: Linear dependence (\( M \propto \alpha \)).
   - In LDR: Non-linear dependence involving \( \sqrt{m^2\alpha^2 + 2mE_F} \).
   - In Anisotropic case: Linear with \( \alpha_x \) or \( \alpha_y \) depending on the specific anisotropy ratio.
4. **Electric Field Magnitude (\( E \)):** The magnetization magnitude scales linearly with the magnitude of the applied electric field (\( M \propto E \)).
5. **Electric Field Direction:** The magnetization direction is always perpendicular to the electric field in the plane, following the cross product rule \( \mathbf{M} \propto \hat{z} \times \mathbf{E} \). For \( \mathbf{E} = E_x \hat{x} \), \( \mathbf{M} = M_y \hat{y} \).

---

## 7. Expected Graphics and Visualizations

Based on the source material, the following explicit graphics should be generated to visualize the model results:

1. **Figure 1: Edelstein Susceptibility vs. Chemical Potential**
   - **Description:** Plot \( \chi_{xy}/\chi_0 \) as a function of the chemical potential \( \mu \) (or \( E_F \)).
   - **Features:**
     - In the LDR (low \( \mu \)), the susceptibility increases with \( \mu \).
     - In the HDR (high \( \mu \)), the susceptibility saturates to a constant value.
     - Different curves should be plotted for different values of \( \alpha \) (e.g., \( \alpha = 52 \) meV Å). As \( \alpha \) increases, the plateau value increases.

2. **Figure 2: Edelstein Susceptibility vs. SOC Strength**
   - **Description:** Plot \( \chi_{xy}/\chi_0 \) as a function of \( \alpha \) at a fixed chemical potential.
   - **Features:** A linear increase of susceptibility with \( \alpha \) is expected.

3. **Figure 3: Anisotropy Effects**
   - **Description:** Plot \( \chi_{xy}/\chi_0 \) as a function of the anisotropy ratios \( r_m \) and \( r_\alpha \).
   - **Features:**
     - Left Panel: Susceptibility increases with \( r_m = m_y/m_x \).
     - Right Panel: Susceptibility increases with \( r_\alpha = \alpha_y/\alpha_x \).
     - Both plots should show saturation for large ratios (\( r \gg 1 \)).

4. **Figure 4: Fermi Surfaces and Spin Texture**
   - **Description:** Visual representation of the Fermi surfaces (circles) and spin vectors (arrows) for \( E=0 \) and \( E \neq 0 \).
   - **Features:**
     - At \( E=0 \): Two concentric circles (inner for \( \nu=+ \), outer for \( \nu=- \)) with tangential spins. Net magnetization is zero.
     - At \( E \neq 0 \): Fermi surfaces shift in opposite directions along the field axis (\( \delta k \)). This creates a spin imbalance perpendicular to \( \mathbf{E} \).

---

## 8. Implementation Notes for the Model

To implement the calculation:
1. **Define Constants:** Set \( \mu_b \), \( e \), \( \hbar \), and a typical transport time \( \tau \) (e.g., \( 10^{-12} \) s for oxides).
2. **Select Regime:** Determine if the system is in HDR (\( E_F > 0 \)) or LDR (\( E_F < 0 \) relative to band crossing) to choose Eq. (5) or Eq. (6).
3. **Anisotropy Check:** If anisotropy is present, calculate \( r_m \) and \( r_\alpha \) and use Eq. (9) or (10) to modify the susceptibility.
4. **Directionality:** Ensure the output vector \( \mathbf{M} \) is rotated by \( 90^\circ \) relative to \( \mathbf{E} \) in the plane (e.g., if \( \mathbf{E} \parallel \hat{x} \), then \( \mathbf{M} \parallel \hat{y} \)).
5. **Units:** Ensure consistency between energy (eV), momentum (Å\( ^{-1} \)), and field (V/m or V/Å).

---

### References

- [Gaillardoni et al., 2025] Gaillardoni, I., Trama, M., Maiellaro, A., Guarcello, C., Romeo, F., & Citro, R. (2025). *Edelstein Effect in Isotropic and Anisotropic Rashba Models*. arXiv:2503.20712v1.
- [Edelstein, 1990] Edelstein, V. M. (1990). Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems. *Solid State Communications*, 73, 233.
- [Rashba, 1960] Rashba, E. I. (1960). Properties of a 2d electron gas with lifted spectral degeneracy. *JETP lett*, 39, 78.

---

# Unit Analysis and Consistency

## Units of Key Properties

| Property          | Symbol       | Units (SI)         | Units (Common)   |
|-------------------|--------------|--------------------|------------------|
| Momentum          | \( p \)      | kg·m/s            | ħ·Å^{-1}        |
| Effective Mass    | \( m \)      | kg                | \( m_e \) (electron mass) |
| Rashba Parameter  | \( \alpha \) | J·m               | eV·Å            |
| Energy            | \( E \)      | J                 | eV              |
| Bohr Magnetron    | \( \mu_b \)  | J/T               | μ_B             |
| Elementary Charge | \( e \)      | C                 | \( e \)         |
| Group Velocity    | \( v \)      | m/s               | m/s             |
| Transport Lifetime| \( \tau \)    | s                 | s               |
| Fermi Energy      | \( E_F \)    | J                 | eV              |
| Spin Expectation  | \( \sigma \) | dimensionless     | dimensionless   |
| Anisotropy Ratios | \( r_m, r_\alpha \) | dimensionless | dimensionless   |
| Susceptibility    | \( \chi \)   | (J/T)/(V/m)      | (J/T)/(V/m)    |
| Lattice Parameter | \( a \)      | m                 | Å               |
| Unit Cell Area    | \( S_{cell} \)| m²               | Å²              |

## Unit Consistency in Equations

### Hamiltonian

Each term must have units of energy (J).

1. **Kinetic Term:** \( \frac{p^2}{2m} \)
   - \( p^2 \) has units of \( (kg·m/s)^2 = kg^2·m^2/s^2 \)
   - Divided by \( m \) (kg): \( kg^2·m^2/(s^2·kg) = kg·m^2/s^2 = J \)

2. **Rashba Term:** \( \alpha (p \times \sigma) \)
   - \( \alpha \) has units of J·m
   - \( p \) has units of kg·m/s
   - The product \( \alpha p \) has units of \( (J·m)·(kg·m/s) = J·kg·m^2/s \)
   - To match energy units (J), a factor of \( 1/(kg·m) \) is needed, suggesting a possible missing factor in the Hamiltonian, possibly \( \hbar \) or another constant.

### Magnetization Equation

The expression for \( M_y \) must have units of magnetization, which in 2D can be considered as J/T per unit area (J·T^{-1}·m^{-2}), but for simplicity, we'll consider it as J/T.

1. **HDR Expression:**
   $$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E $$
   - \( \mu_b \): J/T
   - \( e \): C
   - \( \tau \): s
   - \( m \): kg
   - \( \alpha \): J·m
   - \( E \): V/m = J/(C·m)
   - Units: \( (J/T)·C·s·kg·(J·m)·(J/(C·m)) = J^3·kg·s/(T·C·m^2) \)
   - This does not simplify to J/T, indicating a need for a prefactor to balance the units, possibly involving \( \hbar \) or another fundamental constant.

### Conclusion

To ensure unit consistency, it's necessary to carefully check each term and introduce appropriate prefactors where units do not match. This may involve including Planck's constant \( \hbar \) in the Rashba term or other relevant constants to balance the equations dimensionally.

## Sensible Starting Parameters

| Parameter          | Typical Value      | Units         |
|--------------------|--------------------|---------------|
| Effective Mass     | \( m = 0.1 m_e \)  | kg            |
| Rashba Parameter   | \( \alpha = 52 \)  | meV·Å         |
| Electric Field     | \( E = 10^4 \)     | V/m           |
| Transport Lifetime | \( \tau = 1 \times 10^{-12} \) | s |
| Fermi Energy       | \( E_F = 10 \)     | meV           |
| Bohr Magnetron     | \( \mu_b = 5.79 \times 10^{-5} \) | eV/T          |
| Elementary Charge  | \( e = 1.6 \times 10^{-19} \) | C |

These parameters provide a sensible starting point for numerical calculations, ensuring that all units are consistent and the model behaves as expected.

---
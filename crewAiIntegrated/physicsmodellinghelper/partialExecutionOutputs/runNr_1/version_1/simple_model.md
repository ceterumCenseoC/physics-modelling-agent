

# Edelstein Effect Model for Rashba Fermions: Mathematical Description

## 1. Introduction

The Edelstein effect refers to the generation of a magnetization in a material with spin-orbit coupling when an electric field is applied. This model focuses on the Direct Edelstein Effect (DEE) for a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC) at the Gamma point of the Brillouin zone. The goal is to compute the magnetization magnitude and direction under various electric fields and analyze parameter dependencies.

## 2. Model Hamiltonian

The system is described by the Rashba Hamiltonian:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$

where:
- \( p \) is the momentum operator,
- \( m \) is the effective mass,
- \( \alpha \) is the RSOC strength,
- \( \hat{z} \) is the unit vector perpendicular to the 2D plane,
- \( \vec{\sigma} \) are the Pauli matrices.

The energy dispersion for the two chiral bands (\( \nu = \pm \)) is:

$$
E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k
$$

## 3. Magnetization Calculation

The magnetization \( \vec{M} \) induced by an electric field \( \vec{E} \) is given by:

$$
\vec{M} = -\mu_b \sum_{\vec{k}, \nu} |e| (\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \delta [E_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_{\vec{k}, \nu}
$$

where:
- \( \mu_b \) is the Bohr magneton,
- \( \vec{v}_\nu(\vec{k}) = \nabla_{\vec{k}} E_\nu(\vec{k}) \) is the group velocity,
- \( E_F \) is the Fermi energy,
- \( \langle \vec{\sigma} \rangle_{\vec{k}, \nu} \) is the spin expectation value.

The spin expectation value for Rashba eigenstates is:

$$
\langle \vec{\sigma} \rangle^\pm_{\vec{k}} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
$$

where \( \theta \) is the angle between \( \vec{k} \) and the \( \hat{x} \) axis.

## 4. Magnetization Direction

For an electric field \( \vec{E} = E_x \hat{x} \), the magnetization is along the \( \hat{y} \) direction, i.e., \( M_y \).

## 5. Analytical Expressions for Magnetization

### High-Density Regime (HDR)

Both bands are occupied, and the magnetization is constant:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y
$$

### Low-Density Regime (LDR)

Only the lowest band is occupied, and the magnetization depends on \( E_F \):

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y
$$

For small \( E_F \):

$$
M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \vec{E}]_y
$$

## 6. Edelstein Susceptibility

The susceptibility \( \chi_{xy} \) relates \( M \) and \( E \):

$$
\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle^\nu_{\vec{k}} \delta(E^\nu_{\vec{k}} - \mu) v^\nu_x(\vec{k})
$$

where \( \chi_0 \) is a constant.

## 7. Parameter Dependencies

- **SOC Strength (\( \alpha \)):** \( M_y \propto \alpha \)
- **Fermi Energy (\( E_F \)):** Constant in HDR, increases with \( \sqrt{E_F} \) in LDR
- **Effective Mass (\( m \)):** \( M_y \propto m \)
- **Relaxation Time (\( \tau \)):** \( M_y \propto \tau \)
- **Anisotropy Ratios (\( r_m, r_\alpha \)):** Susceptibility increases with these ratios

## 8. Explicit Graphics

### Figure 1: Susceptibility vs. Chemical Potential

- **X-axis:** \( \mu \) or \( E_F \)
- **Y-axis:** Normalized \( \chi_{xy}/\chi_0 \)
- **Behavior:** Plateau in HDR, linear increase in LDR

### Figure 2: Susceptibility vs. SOC Strength (\( \alpha \))

- **X-axis:** \( \alpha \)
- **Y-axis:** Normalized \( \chi_{xy}/\chi_0 \)
- **Behavior:** Linear increase

### Figure 3: Susceptibility vs. Anisotropy Ratios

- **X-axis:** \( r_m \) or \( r_\alpha \)
- **Y-axis:** Normalized \( \chi_{xy}/\chi_0 \)
- **Behavior:** Increases with ratios, saturates for large \( r_\alpha \)

### Figure 4: Fermi Surfaces and Spin Texture

- **Plot:** 2D \( k_x, k_y \) space
- **Content:** Fermi circles with spin vectors; net spin polarization under \( E \)

## 9. Implementation Steps

1. **Determine Regime:** HDR or LDR based on \( E_F \)
2. **Calculate \( k \) Values:** Use \( k_{F\pm} = \mp k_0 + \sqrt{k_0^2 + 2m E_F} \)
3. **Compute \( M_y \):** Use HDR or LDR expressions
4. **Consider Anisotropy:** Adjust using \( r_m \) and \( r_\alpha \)

This model provides a comprehensive framework to compute and analyze the Edelstein effect in Rashba fermions, capturing the essential dependencies and visualizing the results through explicit graphics.
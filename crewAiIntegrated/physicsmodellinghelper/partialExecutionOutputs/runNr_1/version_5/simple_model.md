

# Model for Calculating the Edelstein Effect in Rashba Fermions

## 1. Theoretical Framework and Hamiltonian

The Edelstein effect is analyzed using the Rashba spin-orbit coupling model. The Hamiltonian at the Gamma point is:

$$
\hat{H} = \frac{\mathbf{p}^2}{2m} + \alpha (\sigma_x p_y - \sigma_y p_x)
$$

where:
- \( m \) is the effective mass,
- \( \alpha \) is the Rashba parameter,
- \( \mathbf{p} = \hbar \mathbf{k} \) is momentum,
- \( \sigma \) are Pauli matrices.

The energy dispersion is:

$$
E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k
$$

with \( \nu = \pm 1 \) for the two helicity bands.

## 2. Magnetization Calculation

The magnetization \( \mathbf{M} \) induced by an electric field \( \mathbf{E} \) is calculated using:

$$
\mathbf{M} = -\mu_b |e| \sum_{\mathbf{k}, \nu} \tau (\vec{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta(E_\nu - E_F) \langle \vec{\sigma} \rangle_\nu^{\mathbf{k}}
$$

where:
- \( \mu_b \) is the Bohr magneton,
- \( \vec{v}_\nu = \frac{1}{\hbar} \nabla_{\mathbf{k}} E_\nu \),
- \( \langle \vec{\sigma} \rangle_\nu^{\mathbf{k}} \) is the spin expectation value.

### 2.1 High-Density Regime (HDR)

For \( E_F > 0 \):

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x
$$

### 2.2 Low-Density Regime (LDR)

For \( E_F < 0 \):

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x
$$

## 3. Dependencies on Model Parameters

- **Electric Field**: \( M \propto E \), direction perpendicular to \( \mathbf{E} \).
- **Spin-Orbit Coupling**: \( M \propto \alpha \).
- **Effective Mass**: \( M \propto m \).
- **Chirality**: Affects spin texture direction.
- **Fermi Velocity**: Influences density of states.
- **Scattering Time**: \( M \propto \tau \).

## 4. Explicit Graphics

### Figure 1: Edelstein Susceptibility vs. Chemical Potential

- **X-axis**: \( \mu \)
- **Y-axis**: \( \chi_{xy}/\chi_0 \)
- **Description**: Plateau in HDR, linear in LDR.

### Figure 2: Susceptibility vs. Rashba Parameter

- **X-axis**: \( \alpha \)
- **Y-axis**: \( \chi_{xy}/\chi_0 \)
- **Description**: Linear increase with \( \alpha \).

### Figure 3: Anisotropy Dependence

- **X-axis**: \( r_m \) or \( r_\alpha \)
- **Y-axis**: \( \chi_{xy}/\chi_0 \)
- **Description**: Increases with anisotropy.

### Figure 4: Spin Texture and Fermi Surfaces

- **Description**: Arrows show spin direction; Fermi surfaces shift with \( \mathbf{E} \).

## 5. Implementation Notes

1. Define parameters: \( m, \alpha, \tau, \mu_b, E_F \).
2. Calculate Fermi wavevectors: \( k_F^\pm \).
3. Compute magnetization using regime-dependent formulas.
4. Apply cross product rule for direction.
5. Consider anisotropy for \( m_x \neq m_y \) or \( \alpha_x \neq \alpha_y \).

This model provides a comprehensive analysis of the Edelstein effect in Rashba fermions, detailing dependencies and visualization.
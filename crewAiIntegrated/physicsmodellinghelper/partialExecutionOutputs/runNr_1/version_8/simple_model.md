

# Calculation of the Edelstein Effect for a Rashba Fermion

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling. The Hamiltonian for the isotropic case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$

where:
- \( p \) is the momentum operator.
- \( m \) is the effective carrier mass.
- \( \alpha \) is the Rashba spin-orbit coupling strength.
- \( \vec{\sigma} \) is the vector of Pauli matrices.
- \( \hat{z} \) is the unit vector perpendicular to the 2D plane.

The eigenenergies for the two chiral branches (\( \nu = \pm \)) are:

$$
E_\nu(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha \hbar k
$$

The spin expectation value for an eigenstate with wavevector \( \vec{k} \) is:

$$
\langle \vec{\sigma} \rangle_\nu^k = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
$$

where \( \theta \) is the angle between \( \vec{k} \) and the \( \hat{x} \)-axis.

## 2. Calculation of Magnetization (Edelstein Effect)

The magnetization \( \vec{M} \) is calculated using a semiclassical Boltzmann approach:

$$
\vec{M} = -\mu_b \sum_{k, \nu} |e| (\vec{v}_\nu(k) \cdot \vec{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_\nu^k
$$

where:
- \( \mu_b \) is the Bohr magneton.
- \( \vec{v}_\nu(k) = \bar{\tau}_\nu^k \nabla_k E_\nu(k) \) is the group velocity scaled by the transport lifetime \( \bar{\tau}_\nu^k \).
- \( E_F \) is the Fermi energy.

### 2.1 Isotropic Rashba Model Results

**High-Density Regime (HDR):**

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x
$$

**Low-Density Regime (LDR):**

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x
$$

For small \( E_F \):

$$
M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) E_x
$$

### 2.2 Anisotropic Rashba Model

The Hamiltonian includes anisotropic effective masses and Rashba parameters:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

The Edelstein susceptibility \( \chi_{xy} \) in the HDR is given by:

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
$$

$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
$$

where \( \chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a} \).

## 3. Dependence on Model Parameters

- **Spin-Orbit Coupling Strength (\( \alpha \)):** \( M_y \propto \alpha \).
- **Fermi Velocity / Effective Mass (\( m \)):** \( M_y \) scales linearly with \( m \).
- **Chirality:** Arises from the imbalance between the two chiral bands.
- **Electric Field:** Magnetization is linear in \( E \).

## 4. Explicit Graphics and Visualizations

- **Figure 1:** Energy dispersion and spin polarization under electric field.
- **Figure 2:** Susceptibility vs. chemical potential, showing regime transitions.
- **Figure 3:** Susceptibility vs. \( \alpha \) at fixed \( \mu \).
- **Figure 5 & 6:** Effects of anisotropy ratios on susceptibility.

These graphics illustrate the dependencies and regimes, providing a visual understanding of the Edelstein effect.
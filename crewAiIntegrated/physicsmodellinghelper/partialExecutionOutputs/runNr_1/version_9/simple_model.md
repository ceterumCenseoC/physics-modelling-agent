

# Mathematical Model for the Edelstein Effect in a Rashba Fermion System

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian for the isotropic case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha (\hat{\sigma}_x p_y - \hat{\sigma}_y p_x)
$$

Where:
- \( p \) is the momentum operator.
- \( m \) is the effective carrier mass.
- \( \alpha \) is the Rashba spin-orbit coupling strength.
- \( \hat{\sigma}_x, \hat{\sigma}_y \) are the Pauli matrices.

For the anisotropic case (e.g., \( C_{2v} \) symmetry), the Hamiltonian generalizes to:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

Where:
- \( m_x, m_y \) are effective masses along the \( x \) and \( y \) directions.
- \( \alpha_x, \alpha_y \) are the Rashba parameters along the \( x \) and \( y \) directions.

## 2. Direct Edelstein Effect (DEE) Formulation

The Direct Edelstein Effect describes the generation of an in-plane magnetization (\( \vec{M} \)) induced by an external electric field (\( \vec{E} \)). The magnetization is given by:

$$
\vec{M} = -\mu_b |e| \tau \int \frac{d^2k}{(2\pi)^2} \vec{v}_\nu(\vec{k}) \cdot \vec{E} \delta(E_\nu(\vec{k}) - E_F) \langle \vec{\sigma} \rangle_\nu^{\vec{k}}
$$

Where:
- \( \mu_b \) is the Bohr magneton.
- \( e \) is the elementary charge.
- \( \tau \) is the transport lifetime.
- \( \vec{v}_\nu(\vec{k}) = \nabla_k E_\nu(\vec{k}) \) is the group velocity.
- \( E_\nu(\vec{k}) \) are the energy bands.
- \( E_F \) is the Fermi energy.
- \( \langle \vec{\sigma} \rangle_\nu^{\vec{k}} \) is the spin expectation value on the eigenstates.

### Isotropic Case

The spin expectation value for the isotropic Rashba model is:

$$
\langle \vec{\sigma} \rangle_\pm^{\vec{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
$$

Where \( \theta \) is the angle between \( \vec{k} \) and the \( \hat{x} \) axis.

The magnetization simplifies to:

$$
M_y = -\frac{\mu_b |e| \tau}{2\pi} \int_0^\infty dk \, k \, \alpha \, \frac{m \alpha k}{\sqrt{(m \alpha k)^2 + \epsilon_k^2}} \delta(\epsilon_k + m \alpha k - E_F)
$$

Where \( \epsilon_k = \frac{\hbar^2 k^2}{2m} \).

### Anisotropic Case

For the anisotropic case, the magnetization components are:

$$
M_x = -\frac{\mu_b |e| \tau}{2\pi} \int dk_x dk_y \, \alpha_y k_y \, E_x \, \delta(E_- - E_F)
$$

$$
M_y = -\frac{\mu_b |e| \tau}{2\pi} \int dk_x dk_y \, \alpha_x k_x \, E_y \, \delta(E_- - E_F)
$$

Where \( E_- \) is the lower energy band.

## 3. Magnetization Magnitude and Direction

### Isotropic Case

#### High-Density Regime (HDR)

For \( E_F > 0 \):

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x
$$

- **Magnitude:** \( M \propto \alpha E_x \).
- **Direction:** Perpendicular to \( \vec{E} \) in the plane.

#### Low-Density Regime (LDR)

For \( E_F < 0 \):

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m |E_F|} E_x
$$

- **Magnitude:** Increases with \( |E_F| \).
- **Direction:** Perpendicular to \( \vec{E} \) in the plane.

### Anisotropic Case

The magnetization components are:

$$
M_x = \frac{\mu_b |e| \tau}{2\pi} \alpha_y E_x
$$

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \alpha_x E_y
$$

- **Direction:** Components depend on the anisotropy ratios \( r_m = m_y/m_x \) and \( r_\alpha = \alpha_y/\alpha_x \).
- **Magnitude:** Modulated by the anisotropy ratios.

## 4. Parameter Dependencies

1. **Rashba Coupling (\( \alpha \))**:
   - \( M \propto \alpha \) in the HDR.
   - \( M \propto \sqrt{m^2 \alpha^2 + 2m |E_F|} \) in the LDR.

2. **Effective Mass (\( m \))**:
   - \( M \propto m \) in the HDR.
   - \( M \propto \sqrt{m^2 \alpha^2 + 2m |E_F|} \) in the LDR.

3. **Fermi Energy (\( E_F \))**:
   - Independent of \( E_F \) in the HDR.
   - Increases with \( |E_F| \) in the LDR.

4. **Transport Lifetime (\( \tau \))**:
   - \( M \propto \tau \).

5. **Chirality (\( \nu = \pm \))**:
   - The effect arises from the imbalance between the populations of the two chiral bands.

6. **Fermi Velocity (\( v_F \))**:
   - Implicitly contained in the group velocity term \( \vec{v}_\nu(\vec{k}) \).

## 5. Graphics and Plots

To visualize the results, the following plots should be generated:

1. **Magnetization vs. Electric Field**:
   - Plot \( M_y \) vs. \( E_x \) for different values of \( \alpha \) and \( E_F \).

2. **Magnetization vs. Rashba Coupling**:
   - Plot \( M_y \) vs. \( \alpha \) for different values of \( E_F \).

3. **Magnetization vs. Fermi Energy**:
   - Plot \( M_y \) vs. \( E_F \) for different values of \( \alpha \).

4. **Anisotropy Dependence**:
   - Plot \( M_x \) and \( M_y \) vs. \( r_m \) and \( r_\alpha \).

5. **Magnetization Vector Field**:
   - Visualize the direction of \( \vec{M} \) for different directions of \( \vec{E} \).

These plots provide a comprehensive understanding of how the Edelstein effect depends on the model parameters and the applied electric field.

## 6. Scientific Citations

- **Gaiardoni et al. (2025)**: Primary source for the anisotropic analysis.
- **Edelstein (1990)**: Original prediction of the effect.
- **Johansson et al. (2016)**: Theoretical aspects of the anisotropic formalism.
- **Bychkov & Rashba (1984)**: Definition of the Rashba Hamiltonian.

This model provides a complete mathematical description of the Edelstein effect in both isotropic and anisotropic Rashba fermion systems, including the dependence on key parameters and explicit graphical representations.
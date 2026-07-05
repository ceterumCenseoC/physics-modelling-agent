

# Model for Calculating the Edelstein Effect in a Rashba Fermion System

Based on the analysis of the scientific literature, specifically the study by **Gaiardoni et al. (2025)** titled *"Edelstein Effect in Isotropic and Anisotropic Rashba Models"*, the following information provides the necessary framework to calculate the Edelstein effect for a Rashba fermion at the Gamma point of the Brillouin zone.

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian for the isotropic case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$

Where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

For an **anisotropic** system (e.g., $C_{2v}$ symmetry), the Hamiltonian generalizes to:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

Where $m_x, m_y$ are effective masses and $\alpha_x, \alpha_y$ are Rashba parameters along the symmetry axes.

## 2. Direct Edelstein Effect (DEE) Formulation

The Direct Edelstein Effect describes the generation of an in-plane magnetization (spin density) $\vec{M}$ induced by an external electric field $\vec{E}$. Within the semiclassical Boltzmann approach, the expectation value of the magnetization at first order in the electric field is:

$$
\vec{M} = -\mu_b \sum_{\vec{k}, \nu} |e| (\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \delta [E_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_\nu^{\vec{k}}
$$

Where:
*   $\mu_b$ is the Bohr magneton.
*   $e$ is the elementary charge.
*   $\vec{v}_\nu(\vec{k}) = \nabla_k E_\nu(\vec{k})$ is the group velocity.
*   $\nu = \pm$ indicates the two chiral Fermi surfaces (helicity bands).
*   $E_F$ is the Fermi energy.
*   $\langle \vec{\sigma} \rangle_\nu^{\vec{k}}$ is the spin expectation value on the eigenstates.

For the isotropic Rashba model, the spin expectation value is:

$$
\langle \vec{\sigma} \rangle_\pm^{\vec{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
$$

Where $\theta$ is the angle between $\vec{k}$ and the $\hat{x}$ axis.

## 3. Magnetization Magnitude and Direction

### Isotropic Case
Assuming an electric field applied along the $\hat{x}$ direction ($\vec{E} = E_x \hat{x}$) and a constant transport lifetime $\tau$, the magnetization is generated perpendicular to the electric field (along $\hat{y}$).

**High-Density Regime (HDR)** (Both chiral bands occupied, $E_F > 0$):
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y
$$
*   **Magnitude:** $M \propto \alpha E_x$. The magnetization is constant and independent of $E_F$ in this regime.
*   **Direction:** Perpendicular to $\vec{E}$ in the plane ($\hat{y}$ if $\vec{E} \parallel \hat{x}$).

**Low-Density Regime (LDR)** (Only the lower energy band occupied):
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y
$$
*   **Magnitude:** Increases with $E_F$. For small $E_F$ near the band crossing, it expands to:
    $$
    M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \vec{E}]_y
    $$

### Anisotropic Case
The Edelstein susceptibility $\chi_{ij}$ relates magnetization to the electric field ($M_j = \chi_{ij} E_i$). For anisotropy parameters $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$, the susceptibility in the HDR is:

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
$$
$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
$$

Where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ is a normalization factor.
*   **Direction:** The magnetization remains perpendicular to the electric field but its magnitude is modulated by the anisotropy ratios.
*   **Dependence:** The susceptibility increases as $r_m$ and $r_\alpha$ increase. If $r_m, r_\alpha < 1$, the susceptibility is lower than the isotropic case; if $> 1$, it is boosted.

## 4. Parameter Dependencies

The model explicitly depends on the following parameters:
1.  **Rashba Coupling ($\alpha$):** Magnetization scales linearly with $\alpha$ in the HDR. In the LDR, it scales as $\sqrt{m^2 \alpha^2 + 2m E_F}$.
2.  **Effective Mass ($m$):** Magnetization scales linearly with $m$ in the HDR.
3.  **Fermi Energy ($E_F$):** In the LDR, magnetization increases with $E_F$. In the HDR, it is independent of $E_F$.
4.  **Transport Lifetime ($\tau$):** Magnetization is directly proportional to the scattering time $\tau$.
5.  **Chirality/Helicity ($\nu = \pm$):** The effect arises from the imbalance between the populations of the two chiral bands induced by the shift of the Fermi surfaces.
6.  **Fermi Velocity ($v_F$):** Implicitly contained in the group velocity term $\vec{v}_\nu(\vec{k})$.

## 5. Implementation for Graphics

To generate explicit graphics, the following relationships should be plotted:
*   **Susceptibility vs. Chemical Potential ($\mu$):** Shows the transition from LDR to HDR and the saturation in HDR.
*   **Susceptibility vs. Rashba Parameter ($\alpha$):** Shows a linear increase in the HDR.
*   **Susceptibility vs. Anisotropy Ratios ($r_m, r_\alpha$):** Shows the enhancement of the effect when anisotropy ratios exceed 1.
*   **Magnetization Direction:** Visualize $\vec{M} \perp \vec{E}$ for various $\vec{E}$ directions.

## 6. Scientific Citations

*   **Gaiardoni, I., Trama, M., Maiellaro, A., Guarcello, C., Romeo, F., & Citro, R. (2025).** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*. arXiv:2503.20712. (Primary source for formulas and anisotropic analysis).
*   **Edelstein, V. M. (1990).** Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems. *Solid State Communications*, 73, 233. (Original prediction of the effect).
*   **Johansson, A., Henk, J., & Mertig, I. (2016).** Theoretical aspects of the Edelstein effect for anisotropic two-dimensional electron gas and topological insulators. *Physical Review B*, 93, 195440. (Anisotropic formalism).
*   **Bychkov, Y. A., & Rashba, E. I. (1984).** Properties of a 2D electron gas with lifted spectral degeneracy. *JETP Lett*, 39, 78. (Rashba Hamiltonian definition).

This information provides the complete analytical and numerical basis to calculate the magnetization magnitude and direction for a Rashba fermion system under an applied electric field, including the dependence on chirality, Fermi velocity, and spin-orbit coupling strength.
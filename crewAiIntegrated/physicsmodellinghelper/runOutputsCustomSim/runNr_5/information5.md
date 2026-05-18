

# Model Information for Calculating the Edelstein Effect in Rashba Fermions

The following information is extracted from the provided research papers to build a model for calculating the Edelstein effect for a Rashba fermion at the Gamma point of the Brillouin zone. The model computes the induced magnetization (spin polarization) magnitude and direction as a function of the applied electric field and relevant system parameters.

## 1. System Hamiltonian and Band Structure

The system is described by a 2D Rashba electron gas Hamiltonian.

**Hamiltonian:**
The effective Hamiltonian for the Rashba 2DEG is given by:
$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (p \times \vec{\sigma}) $$
*(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 1)*

Alternatively, in momentum space ($\hbar=1$):
$$ \hat{H} = \frac{k^2}{2m} + \alpha \hat{z} \cdot (\sigma \times k) $$
*(Source: "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas", Eq. 1)*

**Band Dispersion:**
The energy spectrum consists of two chiral bands ($\nu = \pm$):
$$ \varepsilon^\nu_k = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k $$
*(Source: "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas", Eq. 2)*

**Fermi Momenta:**
The Fermi momenta depend on the chemical potential $\mu$ (or Fermi energy $E_F$).
*   **High-Density Regime (HDR)** ($\mu \ge 0$, both bands occupied):
    $$ k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + 2m\mu/\hbar^2} $$
    where $k_0 = m\alpha/\hbar^2$.
    *(Source: "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas", Eq. 3)*
    *(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 5)*

*   **Low-Density Regime (LDR)** ($\mu < 0$, only lower band occupied):
    $$ k^\eta_F = k_0 - \eta \sqrt{k_0^2 + 2m\mu/\hbar^2} $$
    where $\eta = \pm$ distinguishes left/right carriers.
    *(Source: "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas", Eq. 4)*
    *(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 6)*

**Fermi Velocity:**
The group velocity at the Fermi surface is:
$$ v^\nu_F = \frac{\hbar k^\nu_F}{m} + \nu \alpha $$
*(Source: "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas", Eq. 8)*

## 2. Spin Texture and Expectation Values

The spin expectation value for eigenstates in the Rashba bands exhibits spin-momentum locking.

**Spin Expectation Value:**
$$ \langle \vec{\sigma} \rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix} $$
where $\theta$ is the angle between the vector $k$ and the $\hat{x}$ axis.
*(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 3)*

This implies that for a given chirality $\nu$, the spin is tangential to the Fermi surface and perpendicular to the momentum.

## 3. Direct Edelstein Effect (Magnetization Calculation)

The Direct Edelstein Effect (DEE) describes the generation of a non-equilibrium in-plane spin polarization (magnetization) in response to an applied electric field.

**General Formula:**
Within the Boltzmann framework, the expectation value of the magnetization $\mathbf{M}$ (or total spin density) at first order in the electric field is:
$$ \mathbf{M} = -\mu_B \sum_{k,\nu} |e| (\bar{\tau}^\nu_k \mathbf{v}^\nu(k) \cdot \mathbf{E}) \delta[E^\nu(k) - E_F] \langle \vec{\sigma} \rangle^\nu_k $$
*(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 2)*

Where:
*   $\mu_B$ is the Bohr magneton.
*   $\bar{\tau}^\nu_k$ is the transport lifetime.
*   $\mathbf{v}^\nu(k) = \nabla_k \varepsilon^\nu_k$ is the group velocity.
*   $\mathbf{E}$ is the applied electric field.

**Analytical Expressions for Magnetization:**
Assuming a constant relaxation time $\tau$ and an electric field $\mathbf{E} = E_x \hat{x}$:

*   **High-Density Regime (HDR):**
    $$ M_y = \frac{\mu_B |e| \tau}{2\pi \hbar^2} m \alpha [\hat{z} \times \mathbf{E}]_y $$
    *(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 8)*
    This indicates the magnetization is constant and independent of $E_F$ in the high-density limit.

*   **Low-Density Regime (LDR):**
    $$ M_y = \frac{\mu_B |e| \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y $$
    *(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 9)*
    Here, the magnetization depends on the Fermi energy.

**Edelstein Susceptibility:**
The linear response relation is defined as $m_j = \chi_{ij} E_i$.
$$ \chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle^\nu_k \delta(\varepsilon^\nu_k - \mu) v^\nu_x(k) $$
*(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 7)*
where $\chi_0 = \frac{\tau |e| \mu_B S_{cell}}{4\pi^2 a}$.

## 4. Nonlinear Regime and High Field Effects

For large electric fields where the drift velocity is comparable to the Fermi velocity, the linear response approximation breaks down.

**Nonlinearity Parameter:**
The evolution of the spin depends on the parameter $\gamma$:
$$ \gamma = \frac{e E L_s}{E_F} $$
where $L_s = \hbar / (2m\alpha)$ is the spin-precession length.
*(Source: "Theory of the nonlinear Rashba-Edelstein effect", Eq. 12)*

*   **Adiabatic Regime ($\gamma \ll 1$):** Spin follows the effective field, polarization grows and saturates.
*   **Non-Adiabatic Regime ($\gamma \gg 1$):** Spin polarization is suppressed.

**Saturation Value:**
In the adiabatic limit, the spin polarization saturates at a maximum value:
$$ S_{sat} \sim n \left( \frac{\alpha}{v_F} \right) $$
where $n$ is the electron density.
*(Source: "Theory of the nonlinear Rashba-Edelstein effect", Abstract)*

## 5. Anisotropic Rashba Model

If the system has anisotropic effective masses or Rashba parameters (e.g., $C_{2v}$ symmetry), the Hamiltonian becomes:
$$ \hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y $$
*(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 11)*

**Anisotropic Susceptibility:**
The Edelstein susceptibility depends on the mass ratio $r_m = m_y/m_x$ and Rashba ratio $r_\alpha = \alpha_y/\alpha_x$:
$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} $$
$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} $$
*(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Eq. 12)*

## 6. Model Dependencies and Relations

To build the model, the following dependencies must be implemented:

1.  **Magnetization Direction:**
    The induced magnetization $\mathbf{M}$ is perpendicular to both the applied electric field $\mathbf{E}$ and the structural inversion asymmetry axis $\hat{z}$.
    $$ \mathbf{M} \propto \mathbf{E} \times \hat{z} $$
    *(Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Fig. 1b and Eq. 8)*
    *   If $\mathbf{E} = E_x \hat{x}$, then $\mathbf{M} \parallel \hat{y}$.
    *   If $\mathbf{E} = E_y \hat{y}$, then $\mathbf{M} \parallel -\hat{x}$.

2.  **Magnitude Scaling:**
    *   **Linear Regime:** $|\mathbf{M}| \propto \alpha \tau |\mathbf{E}|$ (HDR).
    *   **LDR:** $|\mathbf{M}| \propto \sqrt{m^2 \alpha^2 + 2m E_F} \tau |\mathbf{E}|$.
    *   **Nonlinear:** Depends on $\gamma = e E L_s / E_F$.

3.  **Key Parameters:**
    *   **Rashba Coupling ($\alpha$):** Linearly increases magnetization in HDR.
    *   **Fermi Velocity ($v_F$):** Affects the saturation limit in the nonlinear regime.
    *   **Chirality ($\nu$):** Determines the sign of the spin texture winding.
    *   **Scattering Time ($\tau$):** Scales the magnitude of the effect in the diffusive regime.
    *   **Effective Mass ($m$):** Influences density of states and Fermi momenta.

## 7. Orbital Contributions (Optional Extension)

For a more complete model, orbital magnetization can be included, especially in bilayer systems.
$$ \mathbf{m} = (\chi_s + \chi_l) \mathbf{E} = \chi \mathbf{E} $$
*(Source: "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction", Eq. 6)*
The orbital contribution $\chi_l$ can be tuned by the asymmetry of layer parameters.
*(Source: "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction", Section IV.A)*
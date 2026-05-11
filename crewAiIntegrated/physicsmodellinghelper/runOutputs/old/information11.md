

# Information for Building the Edelstein Effect Model for Rashba Fermions

The following information is extracted from the provided sources to build a model for calculating the Direct Edelstein Effect (DEE) in a 2D Rashba electron gas at the Gamma point. This model computes the induced magnetization magnitude and direction as a function of the applied electric field and system parameters.

## 1. System Hamiltonian and Band Structure

The starting point for the model is the Rashba Hamiltonian describing the 2D electron gas with spin-orbit coupling.

*   **Hamiltonian:**
    The Hamiltonian for a 2D Rashba electron gas is given by:
    $$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}) $$
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (1).
    *(Note: Alternative convention found in `Boltzmann theory of the inverse Edelstein effect...`, Eq. (1): $\hat{H} = \frac{k^2}{2m} + \alpha \hat{z} \cdot (\boldsymbol{\sigma} \times \mathbf{k})$ where $\hbar=1$.)*

*   **Dispersion Relation:**
    The energy spectrum consists of two chiral bands split by the Rashba coupling:
    $$ \varepsilon_{\mathbf{k}}^{\nu} = \frac{k^2}{2m} + \nu \alpha k $$
    where $\nu = \pm 1$ is the chirality index (helicity).
    **Source:** *Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas*, Eq. (2).

*   **Fermi Momenta:**
    The Fermi momenta depend on the chemical potential $\mu$ (or Fermi energy $E_F$). Two regimes are defined:
    *   **High-Density Regime (HDR, $\mu \ge 0$):** Both chiral bands are occupied.
        $$ k_F^{\nu} = -\nu k_0 + \sqrt{k_0^2 + 2m\mu} $$
        where $k_0 = m\alpha$.
        **Source:** *Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas*, Eq. (3).
    *   **Low-Density Regime (LDR, $\mu < 0$):** Only the lower energy band is occupied.
        $$ k_F^{\eta} = k_0 - \eta \sqrt{k_0^2 + 2m\mu} $$
        where $\eta = \pm$ distinguishes left/right carriers.
        **Source:** *Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas*, Eq. (4).

*   **Fermi Velocity:**
    The group velocity at the Fermi surface is:
    $$ v_F^{\nu} = \left. \frac{\partial \varepsilon_k^{\nu}}{\partial k} \right|_{k=k_F^{\nu}} = \frac{k_F^{\nu}}{m} + \nu \alpha $$
    **Source:** *Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas*, Eq. (8).

## 2. Boltzmann Transport Framework

To calculate the non-equilibrium spin accumulation, the semiclassical Boltzmann equation is used.

*   **Non-Equilibrium Distribution Function:**
    The distribution function is expanded to first order in the electric field $\mathbf{E}$:
    $$ f = f^{(0)} + f^{(1)} $$
    where $f^{(0)}$ is the equilibrium Fermi-Dirac distribution and the first-order correction is:
    $$ f^{(1)} = \frac{e\tau}{\hbar} \mathbf{E} \cdot \nabla_{\mathbf{k}} f^{(0)} $$
    **Source:** *Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets*, Eq. (1).
    *(Note: $\tau$ is the relaxation/scattering time.)*

*   **Spin Expectation Value:**
    The spin expectation value for the eigenstates of the Rashba Hamiltonian is:
    $$ \langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^{\pm} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix} $$
    where $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$ axis.
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (3).

## 3. Magnetization (Spin Density) Calculation

The magnetization $\mathbf{M}$ (or spin density $\mathbf{S}$) is calculated by integrating the spin expectation value over the non-equilibrium distribution.

*   **General Definition:**
    $$ \mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| (\bar{\tau}_{\mathbf{k}}^{\nu} \mathbf{v}^{\nu}(\mathbf{k}) \cdot \mathbf{E}) \delta[E_{\nu}(\mathbf{k}) - E_F] \langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^{\nu} $$
    where $\mu_b$ is the Bohr magneton.
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (2).

*   **Analytical Result (High-Density Regime, $\mu \ge 0$):**
    For an electric field $\mathbf{E}$ applied in the plane (e.g., $\mathbf{E} = E_x \hat{x}$), the induced magnetization is in-plane and perpendicular to $\mathbf{E}$. The magnitude along $\hat{y}$ is:
    $$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y $$
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8).
    *   **Direction:** $\mathbf{M} \propto \hat{z} \times \mathbf{E}$. If $\mathbf{E} \parallel \hat{x}$, then $\mathbf{M} \parallel \hat{y}$.
    *   **Magnitude:** Constant with respect to $E_F$ in this regime.

*   **Analytical Result (Low-Density Regime, $\mu < 0$):**
    $$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y $$
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (9).
    *   **Magnitude:** Depends on $E_F$. For small $E_F$, it expands to:
        $$ M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) [\hat{z} \times \mathbf{E}]_y $$
        **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (10).

*   **Susceptibility Tensor:**
    The magnetization can be expressed via the Edelstein susceptibility $\chi_{ij}$:
    $$ M_j = \chi_{ij} E_i $$
    For the isotropic model in HDR:
    $$ \chi_{xy} = \frac{\mu_b |e| \tau}{2\pi} m \alpha $$
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8) and surrounding text.

## 4. Parameter Dependencies

The model must account for the following dependencies based on the extracted equations:

*   **Rashba Coupling Strength ($\alpha$):**
    *   **HDR:** Linear dependence ($M \propto \alpha$).
    *   **LDR:** Square root dependence ($M \propto \sqrt{\alpha^2 + \dots}$).
    *   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8), (9).
*   **Effective Mass ($m$):**
    *   **HDR:** Linear dependence ($M \propto m$).
    *   **LDR:** Square root dependence ($M \propto \sqrt{m^2}$).
    *   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8), (9).
*   **Fermi Energy / Chemical Potential ($E_F, \mu$):**
    *   **HDR:** Independent of $E_F$ (constant).
    *   **LDR:** Increases with $E_F$.
    *   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8), (9).
*   **Scattering Time ($\tau$):**
    *   Linear dependence ($M \propto \tau$).
    *   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8), (9).
*   **Electric Field Magnitude ($|\mathbf{E}|$):**
    *   Linear dependence ($M \propto |\mathbf{E}|$).
    *   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (2), (8).
*   **Chirality ($\nu$):**
    *   Determines the Fermi momenta $k_F^\nu$ and the sign of the spin expectation value $\langle \sigma \rangle$. In HDR, contributions from both $\nu = \pm$ bands sum up. In LDR, only one band contributes.
    *   **Source:** *Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas*, Eq. (3), (4).

## 5. Direction of Magnetization

*   **Orientation:** The induced magnetization is always **in-plane** (perpendicular to the growth direction $\hat{z}$) and **perpendicular** to the applied electric field $\mathbf{E}$.
    *   If $\mathbf{E} = E_x \hat{x}$, then $\mathbf{M} = M_y \hat{y}$.
    *   Vector relation: $\mathbf{M} \propto \hat{z} \times \mathbf{E}$.
    *   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8); *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Fig. 1.
*   **Out-of-Plane Component:** For a standard isotropic Rashba model, the out-of-plane magnetization ($M_z$) is zero. Non-zero $M_z$ requires additional terms (e.g., p-wave magnetism or Dresselhaus coupling).
    *   **Source:** *Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets*, Eq. (13) (shows $M_z$ requires additional $J$ term).

## 6. Implementation Notes for the Model

*   **Regime Selection:** The model must check if $\mu \ge 0$ (HDR) or $\mu < 0$ (LDR) to select the correct analytical expressions for $k_F$ and $M$.
*   **Anisotropy:** If the system is anisotropic (e.g., different masses $m_x, m_y$ or coupling $\alpha_x, \alpha_y$), the susceptibility depends on ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$.
    *   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (12).
*   **Temperature:** The analytical formulas provided are for $T=0$ (using $\delta$-functions). For $T > 0$, the $\delta$-function should be replaced by $-\partial f_0 / \partial \varepsilon$.
    *   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (2).
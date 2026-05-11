

# Model Information for Calculating the Edelstein Effect in Rashba Fermion Systems

## 1. System Hamiltonian and Band Structure
The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC).

*   **Hamiltonian:** The Rashba Hamiltonian describes the kinetic energy and the spin-orbit interaction.
    $$ \hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha \hat{z} \cdot (\mathbf{k} \times \boldsymbol{\sigma}) $$
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 1, Equation (1).
    *   **Source:** "Boltzmann theory of the inverse Edelstein effect..." (arXiv:2601.02473), Page 2, Equation (1).
    *   **Parameters:** $m$ is the effective carrier mass, $\alpha$ is the Rashba coupling strength, $\mathbf{k}$ is the momentum, and $\boldsymbol{\sigma}$ is the vector of Pauli matrices.

*   **Energy Spectrum:** The Hamiltonian leads to two chiral bands with split energy dispersion.
    $$ \varepsilon_{\nu, k} = \frac{\hbar^2 k^2}{2m} + \nu \hbar \alpha k $$
    *   **Source:** "Boltzmann theory of the inverse Edelstein effect..." (arXiv:2601.02473), Page 2, Equation (2).
    *   **Parameters:** $\nu = \pm$ is the chiral index distinguishing the two bands.

*   **Fermi Momenta:** The Fermi momenta depend on the chemical potential $\mu$ (or Fermi energy $E_F$).
    *   **High-Density Regime (HDR, $\mu \geq 0$):** Both bands are occupied.
        $$ k_{F, \nu} = -\nu k_0 + \sqrt{k_0^2 + 2m\mu/\hbar^2} $$
        where $k_0 = m\alpha/\hbar^2$.
        *   **Source:** "Boltzmann theory of the inverse Edelstein effect..." (arXiv:2601.02473), Page 2, Equation (3).
    *   **Low-Density Regime (LDR, $\mu < 0$):** Only the lower band is occupied.
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (6).

*   **Fermi Velocity:** The group velocity at the Fermi surface is required for transport calculations.
    $$ v_{F, \nu} = \frac{1}{\hbar} \frac{\partial \varepsilon_{\nu, k}}{\partial k} \bigg|_{k=k_{F, \nu}} = \frac{\hbar k_{F, \nu}}{m} + \nu \alpha $$
    *   **Source:** "Boltzmann theory of the inverse Edelstein effect..." (arXiv:2601.02473), Page 3, Equation (8).

## 2. Magnetization (Spin Polarization) Formula
The Direct Edelstein Effect (DEE) generates a non-equilibrium spin polarization (magnetization) in response to an applied electric field $\mathbf{E}$.

*   **General Expression:** The magnetization is calculated from the non-equilibrium distribution function.
    $$ \mathbf{M} = -\mu_b \sum_{k, \nu} |e| (\mathbf{v}_\nu(k) \cdot \mathbf{E}) \delta[E_\nu(k) - E_F] \langle \boldsymbol{\sigma} \rangle^\nu_k $$
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (2).
    *   **Parameters:** $\mu_b$ is the Bohr magneton, $\mathbf{v}_\nu(k)$ is the group velocity, $\langle \boldsymbol{\sigma} \rangle^\nu_k$ is the spin expectation value.

*   **Spin Expectation Value:** The spin is locked perpendicular to the momentum.
    $$ \langle \boldsymbol{\sigma} \rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix} $$
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (3).
    *   **Note:** $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$ axis.

*   **Analytical Expression for Magnetization (HDR):** For an electric field along $\hat{x}$ ($E = E_x \hat{x}$), the magnetization is along $\hat{y}$.
    $$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x $$
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (8).
    *   **Note:** This assumes $\bar{\tau}_+ = \bar{\tau}_- = \tau$ (constant scattering time).
    *   **Vector Form:** $\mathbf{M} \propto \hat{z} \times \mathbf{E}$.
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (8).

*   **Analytical Expression for Magnetization (LDR):**
    $$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x $$
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (9).

*   **Magnetoelectric Susceptibility:** The susceptibility $\alpha^{ME}$ relates Magnetization to Electric Field ($M_i = \alpha^{ME}_{ij} E_j$).
    $$ \alpha^{ME}_{yx} = -\frac{g \mu_B m}{2\pi \hbar^3 W} \lambda $$
    *   **Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets" (arXiv:2501.01888), Page 3, Equation (13).
    *   **Note:** $\lambda$ corresponds to the Rashba parameter $\alpha$. $W$ is the sample width. $g$ is the g-factor.

## 3. Dependence on Model Parameters
The magnitude and direction of the magnetization depend on the following parameters:

*   **Electric Field ($\mathbf{E}$):**
    *   **Magnitude:** Magnetization is linearly proportional to the magnitude of the applied electric field ($M \propto E$).
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (8).
    *   **Direction:** The magnetization direction is perpendicular to the electric field in the plane ($\mathbf{M} \parallel \hat{z} \times \mathbf{E}$). If $\mathbf{E} = E_x \hat{x}$, then $\mathbf{M} = M_y \hat{y}$.
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Figure 1 caption.
        *   **Source:** "Out-of-plane spin polarization from in-plane electric and magnetic fields" (cond-mat/0609078), Page 3, Equation (15) (for $B=0$).

*   **Rashba Coupling Strength ($\alpha$):**
    *   **Magnitude:** Magnetization is linearly proportional to the Rashba coupling parameter ($M \propto \alpha$).
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (8).
        *   **Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets" (arXiv:2501.01888), Page 3, Equation (13).

*   **Effective Mass ($m$):**
    *   **Magnitude:** Magnetization depends on the effective mass ($M \propto m$).
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (8).

*   **Scattering Time ($\tau$):**
    *   **Magnitude:** Magnetization is linearly proportional to the transport scattering time ($M \propto \tau$).
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (8).
        *   **Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets" (arXiv:2501.01888), Page 1, Equation (1).

*   **Chemical Potential / Fermi Energy ($\mu$ or $E_F$):**
    *   **HDR:** In the high-density regime, the magnetization is independent of the Fermi energy (constant plateau).
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (8).
    *   **LDR:** In the low-density regime, the magnetization increases with the square root of the Fermi energy ($M \propto \sqrt{E_F}$).
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (9).

*   **Chirality ($\nu$):**
    *   The spin polarization arises from the imbalance of populations in the chiral bands ($\nu = \pm$). The net magnetization is the sum of contributions from both bands, weighted by their Fermi momenta and scattering times.
        *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (4).
        *   **Source:** "Boltzmann theory of the inverse Edelstein effect..." (arXiv:2601.02473), Page 2, Equation (3) and (4).

## 4. Boltzmann Transport Framework
For a rigorous calculation involving non-equilibrium distribution functions:

*   **Boltzmann Equation:** The semiclassical Boltzmann equation describes the evolution of the distribution function $f(\mathbf{r}, \mathbf{k})$.
    $$ \mathbf{v}_k \cdot \frac{\partial f(\mathbf{r}, \mathbf{k})}{\partial \mathbf{r}} = -\frac{f(\mathbf{r}, \mathbf{k}) - \langle f \rangle}{\tau} $$
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 5, Equation (13).
    *   **Source:** "Boltzmann theory of the inverse Edelstein effect..." (arXiv:2601.02473), Page 3, Equation (5).

*   **Distribution Function Correction:** The non-equilibrium correction $g(x, v_x)$ is solved to find the current and magnetization.
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 5, Equation (14).
    *   **Source:** "Boltzmann theory of the inverse Edelstein effect..." (arXiv:2601.02473), Page 3, Equation (6).

## 5. Summary of Dependencies for Model Implementation
To compute the magnetization magnitude and direction:
1.  **Input:** Electric Field vector $\mathbf{E}$, Rashba parameter $\alpha$, effective mass $m$, scattering time $\tau$, chemical potential $\mu$.
2.  **Direction:** $\mathbf{M} = M \cdot (\hat{z} \times \hat{E})$. The magnetization is always in-plane and perpendicular to $\mathbf{E}$.
3.  **Magnitude:**
    *   Calculate $k_F$ based on $\mu$ and $\alpha$ (using Eq. 3 or 4 from Paper 2).
    *   Determine regime (HDR if $\mu \geq 0$, LDR if $\mu < 0$).
    *   Use Eq. (8) for HDR or Eq. (9) for LDR from "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712).
    *   Alternatively, use the susceptibility $\alpha^{ME}$ from Eq. (13) of "Out-of-plane Edelstein effects..." (arXiv:2501.01888).
4.  **Parameters Check:** Ensure $M$ scales linearly with $E$, $\alpha$, and $\tau$. Ensure $M$ is constant in HDR with respect to $\mu$, and scales as $\sqrt{\mu}$ in LDR.
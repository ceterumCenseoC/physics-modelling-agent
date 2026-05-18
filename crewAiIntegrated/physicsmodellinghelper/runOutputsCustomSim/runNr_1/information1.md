

# Model Information for Calculating the Edelstein Effect in Rashba Fermions

The following information is extracted from the provided research papers to construct a model for calculating the Edelstein effect in a 2D Rashba electron gas. The model computes the magnetization magnitude and direction as a function of the applied electric field and system parameters.

## 1. Model Hamiltonian
The system is described by the Rashba Hamiltonian for a 2D electron gas. The Hamiltonian includes kinetic energy and the Rashba spin-orbit coupling (RSOC) term.

**Isotropic Rashba Model:**
$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \vec{\sigma})
$$
*Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 1, Equation (1)*

In momentum space ($\mathbf{p} = \hbar \mathbf{k}$):
$$
H(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} + \alpha (\sigma_x k_y - \sigma_y k_x)
$$

**Anisotropic Rashba Model (C2v Symmetry):**
To account for effective mass anisotropy and directional dependence of the SOC:
$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$
*Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 4, Equation (11)*

## 2. Magnetization Calculation
The magnetization (total spin density) $\mathbf{M}$ is calculated using the semiclassical Boltzmann approach in the presence of an external electric field $\mathbf{E}$.

**General Expression:**
$$
\mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| (\vec{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta [E_\nu(\mathbf{k}) - E_F] \langle \vec{\sigma} \rangle^\nu_{\mathbf{k}}
$$
*Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (2)*

**Definitions:**
*   $\nu = \pm$: Index indicating the two chiral Fermi surfaces (helicity).
*   $\mu_b$: Bohr magneton.
*   $e$: Absolute value of electron charge.
*   $\vec{v}_\nu(\mathbf{k}) = \nabla_{\mathbf{k}} E_\nu(\mathbf{k}) / \hbar$: Group velocity.
*   $\bar{\tau}^\nu_{\mathbf{k}}$: Transport lifetime (mean free path $\bar{\tau}^\nu_{\mathbf{k}} v_\nu(\mathbf{k})$).
*   $E_F$: Fermi energy.
*   $\langle \vec{\sigma} \rangle^\nu_{\mathbf{k}}$: Spin expectation value on the eigenstates.

**Spin Expectation Value:**
$$
\langle \vec{\sigma} \rangle^\pm_{\mathbf{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
$$
*Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (3)*
*   $\theta$: Angle between vector $\mathbf{k}$ and the $\hat{x}$ axis.
*   $k = \sqrt{k_x^2 + k_y^2}$.

**Edelstein Susceptibility Tensor:**
The linear Edelstein response is defined as $m_j = \chi_{ij} E_i$. The susceptibility tensor element $\chi_{xy}$ is given by:
$$
\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle^\nu_{\mathbf{k}} \delta(\epsilon^\nu_{\mathbf{k}} - \mu) v^\nu_x(\mathbf{k})
$$
*Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (7)*
*   $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$, where $a$ is the lattice parameter, $S_{cell}$ is the unit cell area, and $\tau$ is the transport time.

## 3. Analytical Results for Magnetization
The magnetization magnitude depends on the Fermi energy regime (High-Density vs. Low-Density) and the applied electric field direction.

**Assumption:** Constant transport time $\bar{\tau}_+ = \bar{\tau}_- = \tau$ and Electric Field $\mathbf{E} = E_x \hat{x}$.

**High-Density Regime (HDR):**
(Both chiral bands are occupied, $E_F$ above band crossing)
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
$$
*Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (8)*
*   **Vector Form:** $\mathbf{M} = \frac{\mu_b |e| \tau}{2\pi} m \alpha (\hat{z} \times \mathbf{E})$
*   **Direction:** Perpendicular to the electric field $\mathbf{E}$ (e.g., if $\mathbf{E} \parallel \hat{x}$, then $\mathbf{M} \parallel \hat{y}$).
*   **Magnitude:** Constant and independent of $E_F$ in this regime.

**Low-Density Regime (LDR):**
(Only the lowest energy band is occupied, $E_F$ below band crossing)
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y
$$
*Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (9)*
*   **Magnitude:** Increases with Fermi energy $E_F$.
*   **Small $E_F$ Expansion:**
    $$
    M_y = \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \mathbf{E}]_y
    $$
    *Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equation (10)*

## 4. Dependence on Model Parameters
The model dependencies on chirality, Fermi velocity, and anisotropy are summarized below.

**Fermi Wavevectors ($k_F$):**
*   **HDR:**
    $$
    k^+_{F} = -k_0 + \sqrt{k_0^2 + 2m E_F}, \quad k^-_{F} = +k_0 + \sqrt{k_0^2 + 2m E_F}
    $$
    where $k_0 = \alpha m$.
    *Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (5)*
*   **LDR:**
    $$
    k^+_{F} = +k_0 - \sqrt{k_0^2 + 2m E_F}, \quad k^-_{F} = +k_0 + \sqrt{k_0^2 + 2m E_F}
    $$
    *Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (6)*

**Anisotropy Parameters:**
*   Mass ratio: $r_m = m_y / m_x$
*   SOC ratio: $r_\alpha = \alpha_y / \alpha_x$
*   **Anisotropic Susceptibility (HDR):**
    $$
    \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}, \quad \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
    $$
    *Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 4, Equation (12)*
*   **Effect:** Susceptibility increases when $r_m > 1$ and $r_\alpha > 1$.

**Chirality/Helicity:**
*   The spin expectation value $\langle \vec{\sigma} \rangle^\nu_{\mathbf{k}}$ depends on the band index $\nu = \pm$ (chirality). The summation over $\nu$ in Eq. (2) accounts for contributions from both spin-split bands.
*   *Source: "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 2, Equation (2)*

**Orbital Contribution (Optional Extension):**
For a more complete magnetization calculation including orbital moments (relevant for bilayer systems):
$$
\mathbf{m} = -\mu_B \frac{\hbar}{A_0} \sum_{nk} f_{nk} (g_s s_{nk} + g_l l_{nk})
$$
*Source: "Spin and Orbital Edelstein Effect in a Bilayer System with Rashba Interaction" (arXiv:2307.02872), Page 2, Equation (1)*
*   $s_{nk}$: Spin moment expectation value.
*   $l_{nk}$: Orbital moment expectation value (calculated via modern theory of orbital magnetization).

## 5. Summary of Parameters for Model Implementation

| Parameter | Symbol | Description | Source |
| :--- | :--- | :--- | :--- |
| Rashba Coupling | $\alpha$ (or $\alpha_x, \alpha_y$) | Spin-orbit coupling strength | Paper 1, Eq. 1, 11 |
| Effective Mass | $m$ (or $m_x, m_y$) | Carrier effective mass | Paper 1, Eq. 1, 11 |
| Fermi Energy | $E_F$ (or $\mu$) | Chemical potential | Paper 1, Eq. 2, 5, 6 |
| Relaxation Time | $\tau$ | Transport lifetime | Paper 1, Eq. 2, 7, 8 |
| Electric Field | $\mathbf{E}$ | Applied external field | Paper 1, Eq. 2, 8 |
| Bohr Magneton | $\mu_b$ | Magnetic moment constant | Paper 1, Eq. 2 |
| Electron Charge | $e$ | Elementary charge | Paper 1, Eq. 2 |
| Chirality | $\nu = \pm$ | Band index (helicity) | Paper 1, Eq. 2 |
| Fermi Velocity | $v_F$ | Derived from $k_F$ and $m$ | Paper 1, Eq. 2 (via $v_\nu$) |
| Anisotropy Ratios | $r_m, r_\alpha$ | Mass and SOC ratios | Paper 1, Eq. 11, 12 |

## 6. Direction of Magnetization
The magnetization $\mathbf{M}$ is always perpendicular to the applied electric field $\mathbf{E}$ and lies in the plane of the 2D system (xy-plane), orthogonal to the spin-orbit coupling axis ($\hat{z}$).
*   **Relation:** $\mathbf{M} \propto \hat{z} \times \mathbf{E}$
*   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 3, Equations (8) and (9).
*   **Example:** If $\mathbf{E} = E_x \hat{x}$, then $\mathbf{M} = M_y \hat{y}$.
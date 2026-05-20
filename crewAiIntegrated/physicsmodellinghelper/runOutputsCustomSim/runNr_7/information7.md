

# Model Information for Calculating the Edelstein Effect in Rashba Fermions

The following information is extracted from three key papers to build a computational model for the Edelstein effect in a Rashba fermion system at the Gamma point. The model covers linear and non-linear regimes, parameter dependencies, and expected graphical outputs.

## 1. Model Hamiltonian

The system is described by a 2D Rashba Hamiltonian. For the isotropic case, the Hamiltonian is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (p \times \vec{\sigma})
$$

*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (1), Page 1.
*   **Parameters:**
    *   $p$: Momentum operator.
    *   $m$: Effective carrier mass.
    *   $\alpha$: Rashba coupling strength.
    *   $\vec{\sigma}$: Vector of Pauli matrices.
    *   $\hat{z}$: Unit vector perpendicular to the 2D plane.

For the anisotropic case (useful for studying chirality and mass dependence), the Hamiltonian becomes:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (11), Page 4.
*   **Parameters:** $m_x, m_y$ (effective masses), $\alpha_x, \alpha_y$ (Rashba parameters).

## 2. Magnetization (Spin Polarization) Formulas

The current-induced magnetization (spin density) $\vec{M}$ is calculated using the semiclassical Boltzmann approach.

### General Expression
The expectation value of the magnetization at first order in the electric field $E$ is:

$$
\vec{M} = -\mu_b \sum_{k, \nu} |e| (\vec{v}_\nu(k) \cdot \vec{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_\nu^k
$$

*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (2), Page 2.
*   **Definitions:**
    *   $\mu_b$: Bohr magneton.
    *   $\nu = \pm$: Index for the two chiral Fermi surfaces (helicity).
    *   $\vec{v}_\nu(k) = \bar{\tau}_k^\nu v_\nu(k)$: Mean free path (with transport lifetime $\bar{\tau}_k^\nu$ and group velocity $v_\nu(k)$).
    *   $\langle \vec{\sigma} \rangle_\nu^k$: Spin expectation value on eigenstates.

### Spin Expectation Value
The spin texture is locked perpendicular to momentum:

$$
\langle \vec{\sigma} \rangle_\pm^k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
$$

*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (3), Page 2.
*   **Note:** $\theta$ is the angle between vector $k$ and the $\hat{x}$ axis.

### Linear Response Regime
For an electric field $\vec{E} = E_x \hat{x}$, the magnetization is perpendicular to the field (along $\hat{y}$).

**High-Density Regime (HDR):** Both chiral bands occupied.
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y
$$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8), Page 3.
*   **Dependency:** Magnetization is constant and independent of Fermi energy $E_F$ in this regime.

**Low-Density Regime (LDR):** Only the lowest energy band occupied.
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{(m^2 \alpha^2 + 2m E_F)} [\hat{z} \times \vec{E}]_y
$$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (9), Page 3.
*   **Dependency:** Magnetization increases linearly with Fermi energy $E_F$ for small values.

### Non-Linear Regime
In the clean limit (no impurities), the spin polarization $S_y$ depends on the dimensionless parameter $\gamma$:

$$
\gamma = \frac{e E L_s}{E_F} = \frac{e E}{\alpha p_F^2}
$$

*   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Eq. (12), Page 7.
*   **Definitions:** $L_s = \hbar/(2m\alpha)$ is the spin-precession length.
*   **Regimes:**
    *   **Adiabatic ($\gamma \ll 1$):** Spin follows the field, saturation value $n(\alpha/v_F)$.
    *   **Non-Adiabatic ($\gamma \gg 1$):** Spin polarization is suppressed.

The total Edelstein spin polarization is given by:
$$
S_y(\tau) = \frac{2\alpha n}{v_F} \frac{1}{2\pi} \int_0^{2\pi} d\theta_p \left( |u_p(\tau-\tau_p)|^2 - \frac{1}{2} \right)
$$
*   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Eq. (29), Page 10.
*   **Linear Limit:** For weak fields ($|v(t)| \ll v_F$):
    $$
    S_y(t) \simeq \frac{N_0}{2} \alpha e E t
    $$
    *   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Eq. (37), Page 13.

## 3. Parameter Dependencies

### Chirality ($\nu$)
*   The spin polarization arises from the imbalance between the two chiral bands ($\nu = \pm$).
*   In the HDR, the contributions from the two bands partially cancel, leading to a net magnetization proportional to the difference in transport times and Fermi momenta: $M_y \propto (\bar{\tau}_+ k_+^F - \bar{\tau}_- k_-^F)$.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (4), Page 2.

### Fermi Velocity ($v_F$) and Energy ($E_F$)
*   **HDR:** Magnetization is independent of $E_F$ (Eq. 8).
*   **LDR:** Magnetization scales as $\sqrt{m^2 \alpha^2 + 2m E_F}$ (Eq. 9).
*   **Non-linear:** The saturation value scales with $n(\alpha/v_F)$ (Page 3, Abstract).
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Page 3; *Theory of the nonlinear Rashba-Edelstein effect*, Page 3.

### Electric Field Magnitude ($E$)
*   **Linear:** $M \propto E$.
*   **Non-linear:** For $\gamma \ll 1$, $M$ grows and saturates. For $\gamma \gg 1$, $M$ is reduced.
*   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Abstract and Page 3.

### Electric Field Direction
*   The magnetization is always perpendicular to the electric field in the plane ($\hat{z} \times \vec{E}$).
*   If $\vec{E} = E_x \hat{x}$, then $\vec{M} \parallel \hat{y}$.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8), Page 3.

### Anisotropy Parameters ($r_m, r_\alpha$)
*   **Mass Anisotropy:** $r_m = m_y/m_x$. Susceptibility $\chi_{xy}$ increases as $r_m$ increases (for $r_m > 1$).
    $$
    \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
    $$
*   **Rashba Anisotropy:** $r_\alpha = \alpha_y/\alpha_x$. Susceptibility increases as $r_\alpha$ increases.
    $$
    \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
    $$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (12), Page 4.

## 4. Expected Graphics and Visualization

To validate the model, the following graphics should be generated based on the source material:

### A. Magnetization vs. Electric Field Magnitude
*   **Description:** Plot $M_y$ (or $S_y$) as a function of $E$.
*   **Expected Behavior:** Linear increase at low $E$ (linear regime), transitioning to saturation or reduction at high $E$ (non-linear regime, $\gamma \gg 1$).
*   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Figure 4 (Page 11) and Figure 6 (Page 13).

### B. Magnetization vs. Chemical Potential / Fermi Energy
*   **Description:** Plot Edelstein susceptibility $\chi_{xy}$ or $M_y$ vs. $\mu$ (or $E_F$).
*   **Expected Behavior:** Step-like features corresponding to band edges. In HDR, it may plateau; in LDR, it increases with $\sqrt{E_F}$.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Figure 2 (Page 3) and Figure 3 (Page 3).

### C. Dependence on Rashba Coupling ($\alpha$)
*   **Description:** Plot $\chi_{xy}$ vs. $\alpha$.
*   **Expected Behavior:** Linear increase with $\alpha$ in the high chemical potential regime.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Figure 3 (Right Panel, Page 3).

### D. Anisotropy Effects
*   **Description:** Plot $\chi_{xy}$ vs. $r_m$ or $r_\alpha$.
*   **Expected Behavior:** Susceptibility increases as the ratio exceeds 1.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Figure 6 (Page 4).

### E. Non-Adiabatic Transition
*   **Description:** Plot $S_y$ vs. $\tau$ (dimensionless time) for different $\gamma$ values ($0.1, 1.0, 10$).
*   **Expected Behavior:** For small $\gamma$, $S_y$ follows the adiabatic path. For large $\gamma$, the response is suppressed and oscillatory.
*   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Figure 3 (Page 10) and Figure 4 (Page 11).

### F. Spin and Orbital Contributions (Bilayer)
*   **Description:** Plot Spin ($\chi^s_{xy}$) and Orbital ($\chi^l_{xy}$) susceptibilities vs. $E_F$.
*   **Expected Behavior:** Spin effect is generally larger. Orbital effect can change sign depending on layer asymmetry ($\alpha_A - \alpha_B$).
*   **Source:** *Spin and orbital Edelstein effect in a bilayer system with Rashba interaction*, Figure 2 (Page 4) and Figure 4 (Page 6).

## 5. Summary of Key Equations for Implementation

| Quantity | Equation | Source |
| :--- | :--- | :--- |
| **Hamiltonian** | $H = \frac{p^2}{2m} + \alpha \hat{z} \cdot (p \times \vec{\sigma})$ | [1], Eq. (1) |
| **Magnetization (General)** | $M = -\mu_b \sum_{k,\nu} |e| (\vec{v}_\nu \cdot E) \delta[E_\nu - E_F] \langle \vec{\sigma} \rangle_\nu$ | [1], Eq. (2) |
| **Spin Texture** | $\langle \vec{\sigma} \rangle_\pm^k = (\pm \sin\theta, \mp \cos\theta, 0)$ | [1], Eq. (3) |
| **Linear Magnetization (HDR)** | $M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x$ | [1], Eq. (8) |
| **Linear Magnetization (LDR)** | $M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x$ | [1], Eq. (9) |
| **Non-linear Parameter** | $\gamma = \frac{e E}{\alpha p_F^2}$ | [2], Eq. (12) |
| **Susceptibility (Anisotropic)** | $\chi_{xy}/\chi_0 = \frac{4\pi m \alpha r}{1+r}$ (for $r=r_m$ or $r_\alpha$) | [1], Eq. (12) |

**Sources:**
*   **[1]** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, arXiv:2503.20712.
*   **[2]** *Theory of the nonlinear Rashba-Edelstein effect*, arXiv:1506.08330.
*   **[3]** *Spin and orbital Edelstein effect in a bilayer system with Rashba interaction*, arXiv:2307.02872.


# Edelstein Effect Model for Rashba Fermions

The following information is extracted from the provided research papers to build a model for calculating the Edelstein effect for a Rashba fermion at the Gamma point. It includes the Hamiltonian, magnetization relations for linear and nonlinear regimes, and parameter dependencies.

## 1. Rashba Hamiltonian and Band Structure

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling. The Hamiltonian describes the kinetic energy and the spin-momentum locking term.

**Hamiltonian:**
$$
\hat{H} = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}
$$
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (1); `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (1).
*   **Parameters:**
    *   $m^*$: Effective carrier mass.
    *   $\alpha_R$: Rashba coupling strength (chirality-dependent).
    *   $\vec{\sigma}$: Vector of Pauli matrices.
    *   $\vec{k}$: Momentum vector.
    *   $\hat{z}$: Unit vector perpendicular to the 2D plane.

**Energy Dispersion:**
The spectrum consists of two chiral bands ($\nu = \pm$):
$$
\epsilon_k^\nu = \frac{\hbar^2 k^2}{2m^*} + \nu \hbar \alpha_R k
$$
*   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (2).
*   **Note:** $\nu = \pm$ is the chiral index.

**Fermi Momenta:**
Depending on the chemical potential $\mu$, the system operates in two regimes:
*   **High-Density Regime (HDR, $\mu \geq 0$):** Both chiral bands contribute.
    $$
    k_F^\nu = -\nu k_0 + \sqrt{k_0^2 + \frac{2m^*\mu}{\hbar^2}} \quad \text{where} \quad k_0 = \frac{m^*\alpha_R}{\hbar^2}
    $$
    *   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (3); `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (5).
*   **Low-Density Regime (LDR, $\mu < 0$):** Only the lower band is occupied.
    $$
    k_F^\eta = k_0 - \eta \sqrt{k_0^2 + \frac{2m^*\mu}{\hbar^2}} \quad (\eta = \pm \text{ for left/right carriers})
    $$
    *   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (4); `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (6).

## 2. Magnetization in the Linear Regime (Direct Edelstein Effect)

In the linear response regime (weak electric field), an applied electric field $\vec{E}$ induces a non-equilibrium spin polarization (magnetization $\vec{M}$).

**General Formula:**
The magnetization is obtained from the expectation value of the spin operator weighted by the non-equilibrium distribution function:
$$
\vec{M} = -\mu_B \sum_{\vec{k},\nu} |e| (\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \delta[\epsilon_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_\nu^{\vec{k}}
$$
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (2).
*   **Parameters:** $\mu_B$ (Bohr magneton), $e$ (electron charge), $\vec{v}_\nu$ (group velocity), $\langle \vec{\sigma} \rangle_\nu^{\vec{k}}$ (spin expectation value).

**Directionality:**
For an electric field applied along $\hat{x}$ ($\vec{E} = E_x \hat{x}$), the induced magnetization is perpendicular to $\vec{E}$ and lies in the plane:
$$
\vec{M} \propto \hat{z} \times \vec{E}
$$
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Fig. 1 caption; `Spin_accumulation_at_nonmagnetic_interfa.pdf`, text.
*   **Specific Component:** If $\vec{E} = E_x \hat{x}$, then $M_y \neq 0$ and $M_x = M_z = 0$.

**Magnitude (Isotropic Case):**
*   **High-Density Regime (HDR):**
    $$
    M_y = \frac{\mu_B |e| \tau}{2\pi} m^* \alpha_R E_x = \frac{\mu_B |e| \tau}{2\pi} m^* \alpha_R [\hat{z} \times \vec{E}]_y
    $$
    *   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (8).
    *   **Relation:** Linear dependence on $\alpha_R$ and $\tau$ (relaxation time). Independent of $E_F$ in this approximation.

*   **Low-Density Regime (LDR):**
    $$
    M_y = \frac{\mu_B |e| \tau}{2\pi} \sqrt{(m^* \alpha_R)^2 + 2m^* E_F} E_x
    $$
    *   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (9).
    *   **Relation:** Depends on $E_F$ (Fermi energy).

**Edelstein Susceptibility:**
Defined as $M_i = \chi_{ij} E_j$. For isotropic Rashba:
$$
\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle_\nu^{\vec{k}} \delta(\epsilon_\nu^{\vec{k}} - \mu) v_x^\nu(\vec{k})
$$
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (7).
*   **Scaling:** $\chi_{xy} \propto \alpha_R$ (linearly increases with Rashba parameter).
    *   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Fig. 3, text.

## 3. Magnetization in the Nonlinear Regime

For strong electric fields where the drift velocity approaches the Fermi velocity, the linear approximation fails.

**Nonlinearity Parameter:**
The regime is characterized by the dimensionless parameter $\gamma$:
$$
\gamma = \frac{e E L_s}{E_F} = \frac{e E}{\alpha_R p_F^2}
$$
where $L_s = \hbar / (2m^*\alpha_R)$ is the spin-precession length.
*   **Source:** `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Eq. (12).

**Regimes:**
*   **Adiabatic ($\gamma \ll 1$):** Spin follows the effective field. Magnetization grows and saturates.
    $$
    S_y(t) \simeq \frac{N_0}{2} \alpha_R e E t \quad (\text{Ballistic limit})
    $$
    *   **Source:** `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Eq. (37).
    *   **Steady State:** With scattering time $\tau$, this recovers the linear relation $M \propto E$.

*   **Non-Adiabatic ($\gamma \gg 1$):** Spin cannot follow the rapidly changing field. Magnetization is suppressed.
    *   **Source:** `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Abstract, Section III.
    *   **Long-time limit:** $S_y(\infty)$ depends on $\gamma$. For $\gamma \to \infty$, polarization is reduced compared to the adiabatic limit.
    *   **Source:** `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Fig. 4, Eq. (30).

**Saturation:**
In the clean limit (no scattering), the spin polarization saturates at a maximum value corresponding to $100\%$ spin polarization of electrons in the annulus between Fermi momenta ($n \alpha_R / v_F$).
*   **Source:** `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Abstract.

## 4. Parameter Dependencies and Anisotropy

The model must account for how $\vec{M}$ depends on system parameters.

**Effective Mass and Rashba Parameter Ratios (Anisotropy):**
If the system has $C_{2v}$ symmetry (anisotropic masses $m_x, m_y$ and Rashba parameters $\alpha_x, \alpha_y$):
*   **Hamiltonian:**
    $$
    \hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \sigma_x - \alpha_x k_x \sigma_y
    $$
    *   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (11).
*   **Susceptibility Scaling:**
    $$
    \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}, \quad \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
    $$
    where $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$.
    *   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (12).
    *   **Relation:** Susceptibility increases as ratios $r_m, r_\alpha$ exceed 1.

**Chirality:**
The contribution to magnetization comes from the difference in occupation of the chiral bands. In LDR, the spin current vanishes because the Fermi contours are displaced in the same direction without relative shift.
*   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, text below Eq. (22).

**Orbital Contribution:**
In bilayer systems or specific materials, orbital magnetization ($M_{orb}$) can be comparable to spin magnetization ($M_{spin}$).
$$
\vec{M} = \vec{M}_{spin} + \vec{M}_{orbital}
$$
*   **Source:** `Spin_and_orbital_Edelstein_effect_in_a_b.pdf`, Eq. (1), (6).
*   **Relation:** Orbital susceptibility $\chi_l$ can be tuned by layer asymmetry (difference in $\alpha$ or $m$ between layers).
    *   **Source:** `Spin_and_orbital_Edelstein_effect_in_a_b.pdf`, Fig. 4, 5.

## 5. Summary of Relations for Model Building

| Quantity | Relation | Source |
| :--- | :--- | :--- |
| **Hamiltonian** | $H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$ | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (1) |
| **Magnetization Direction** | $\vec{M} \parallel \hat{z} \times \vec{E}$ | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (8) |
| **Linear Magnitude (HDR)** | $M \propto \mu_B |e| \tau m^* \alpha_R E$ | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (8) |
| **Linear Magnitude (LDR)** | $M \propto \mu_B |e| \tau \sqrt{(m^* \alpha_R)^2 + 2m^* E_F} E$ | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (9) |
| **Nonlinear Parameter** | $\gamma = \frac{e E L_s}{E_F}$ | `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Eq. (12) |
| **Anisotropy Scaling** | $\chi \propto \frac{r}{1+\sqrt{r}}$ (for mass ratio $r$) | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (12) |
| **Orbital Contribution** | $M_{orb} \propto (\alpha_A - \alpha_B)$ (in bilayers) | `Spin_and_orbital_Edelstein_effect_in_a_b.pdf`, Eq. (12) |

**Note:** For the Gamma point calculation, ensure the integration is performed over the Fermi surface defined by $\mu$ relative to the band crossing at $k=0$. The relaxation time $\tau$ is crucial for converting the ballistic response to a steady-state DC response.
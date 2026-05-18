

# Model Information for Calculating the Edelstein Effect in a Rashba Fermion System

## 1. System Hamiltonian and Band Structure

The model is based on a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian describes the kinetic energy and the spin-orbit interaction breaking inversion symmetry.

*   **Hamiltonian:**
    $$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\sigma \times p) $$
    **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (1); "Theory of the nonlinear Rashba-Edelstein effect" (1506.08330), Eq. (1).
    *   $p$: Momentum operator.
    *   $m$: Effective carrier mass.
    *   $\alpha$: Rashba coupling strength.
    *   $\sigma$: Vector of Pauli matrices.
    *   $\hat{z}$: Unit vector perpendicular to the 2D plane.

*   **Energy Dispersion:**
    $$ \varepsilon^\nu_k = \frac{k^2}{2m} + \nu k \alpha $$
    **Source:** "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas" (2601.02473), Eq. (2); "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (2).
    *   $k = |k|$: Modulus of the wave vector.
    *   $\nu = \pm$: Chiral index (band index).

*   **Fermi Momenta:**
    The Fermi momenta depend on the chemical potential $\mu$ (or Fermi energy $E_F$).
    *   **High-Density Regime (HDR, $\mu \ge 0$):** Both chiral bands are occupied.
        $$ k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + 2m\mu} $$
        **Source:** "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas" (2601.02473), Eq. (3); "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (5).
        *   $k_0 = \alpha m$.
    *   **Low-Density Regime (LDR, $\mu < 0$):** Only the lower band is occupied.
        $$ k^\eta_F = k_0 - \eta \sqrt{k_0^2 + 2m\mu} $$
        **Source:** "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas" (2601.02473), Eq. (4); "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (6).
        *   $\eta = \pm$ distinguishes left/right carriers in the lower band.

## 2. Direct Edelstein Effect (Magnetization Calculation)

The Direct Edelstein Effect (DEE) describes the generation of a non-equilibrium in-plane magnetization (spin polarization) in response to an applied electric field $E$.

### 2.1 Linear Response Regime (Boltzmann Approach)
In the presence of scattering (relaxation time $\tau$), the steady-state magnetization $M$ is calculated using the semiclassical Boltzmann equation.

*   **General Definition:**
    $$ M = -\mu_b \sum_{k,\nu} |e| (\bar{\tau}^\nu_k (v^\nu(k) \cdot E)) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle^\nu_k $$
    **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (2).
    *   $\mu_b$: Bohr magneton.
    *   $\bar{\tau}^\nu_k$: Transport lifetime.
    *   $\langle \vec{\sigma} \rangle^\nu_k$: Spin expectation value on eigenstates.

*   **Magnetization Magnitude and Direction:**
    The magnetization is perpendicular to the electric field and lies in the 2D plane.
    $$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times E]_y \quad (\text{HDR}) $$
    $$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times E]_y \quad (\text{LDR}) $$
    **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (8) and Eq. (9).
    *   If $E = E_x \hat{x}$, then $M$ is along $\hat{y}$ (perpendicular to $E$).
    *   **HDR:** Magnetization is constant and independent of $E_F$.
    *   **LDR:** Magnetization increases with $E_F$.

*   **Edelstein Susceptibility:**
    The linear response coefficient $\chi_{ij}$ relates magnetization to the electric field ($M_i = \chi_{ij} E_j$).
    $$ \chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle^\nu_k \delta(\varepsilon^\nu_k - \mu) v^\nu_x(k) $$
    **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (7).
    *   $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$.

### 2.2 Non-Linear Regime (Clean Limit)
For very strong electric fields or weak scattering where the drift velocity approaches the Fermi velocity, non-linear effects become significant.

*   **Adiabaticity Parameter:**
    $$ \gamma = \frac{e E L_s}{E_F} $$
    **Source:** "Theory of the nonlinear Rashba-Edelstein effect" (1506.08330), Eq. (12).
    *   $L_s = \hbar / (2m\alpha)$: Spin precession length.
    *   **Condition:** If $\gamma \ll 1$ (weak field), the system is in the linear/adiabatic regime. If $\gamma \gg 1$ (strong field), the spin dynamics become non-adiabatic, suppressing polarization.

*   **Time-Dependent Spin Polarization (Clean Limit):**
    $$ S_y(\tau) = \frac{2\alpha n}{v_F} \frac{1}{2\pi} \int_0^{2\pi} d\theta_p \left( |u_p(\tau - \tau_p)|^2 - \frac{1}{2} \right) $$
    **Source:** "Theory of the nonlinear Rashba-Edelstein effect" (1506.08330), Eq. (29).
    *   $n$: Electron density.
    *   $v_F$: Fermi velocity.
    *   $u_p$: Amplitude derived from Landau-Zener solutions.

*   **Linear Response Limit (Clean):**
    $$ S_y(t) \simeq \frac{N_0}{2} \alpha e E t $$
    **Source:** "Theory of the nonlinear Rashba-Edelstein effect" (1506.08330), Eq. (37).
    *   $N_0 = m / (2\pi)$: Density of states per spin.
    *   Note: In the presence of scattering $\tau$, $t$ is effectively replaced by $\tau$ for steady state.

## 3. Parameter Dependencies

The model behavior depends on the following physical parameters:

| Parameter | Symbol | Effect on Magnetization ($M$) | Source |
| :--- | :--- | :--- | :--- |
| **Electric Field Magnitude** | $E$ | Linear relationship ($M \propto E$) in weak field regime. Saturates or decreases in strong field ($\gamma \gg 1$). | "Edelstein Effect..." (2503.20712) Eq (8); "Theory of nonlinear..." (1506.08330) Eq (12) |
| **Rashba Coupling** | $\alpha$ | $M$ is directly proportional to $\alpha$ in HDR. In LDR, $M \propto \sqrt{m^2\alpha^2 + 2mE_F}$. | "Edelstein Effect..." (2503.20712) Eq (8), (9) |
| **Effective Mass** | $m$ | $M \propto m$ in HDR. Affects Fermi velocity and density of states. | "Edelstein Effect..." (2503.20712) Eq (8) |
| **Scattering Time** | $\tau$ | $M \propto \tau$ (in Boltzmann steady-state). Longer $\tau$ allows larger spin accumulation. | "Edelstein Effect..." (2503.20712) Eq (8) |
| **Fermi Energy** | $E_F$ (or $\mu$) | Constant in HDR. Increases with $\sqrt{E_F}$ in LDR. | "Edelstein Effect..." (2503.20712) Eq (8), (9) |
| **Chirality** | $\nu = \pm$ | Determines the spin texture direction. Contributions from $\nu=+$ and $\nu=-$ bands add or cancel depending on the regime (HDR vs LDR). | "Boltzmann theory..." (2601.02473) Eq (3), (4) |
| **Fermi Velocity** | $v_F$ | Inversely affects spin polarization magnitude in some formulations (e.g., $M \propto 1/v_F$). | "Theory of nonlinear..." (1506.08330) Eq (29) |
| **Anisotropy** | $r_m, r_\alpha$ | Anisotropy in mass ($r_m = m_y/m_x$) or coupling ($r_\alpha = \alpha_y/\alpha_x$) modifies susceptibility. Susceptibility increases if $r_m, r_\alpha > 1$. | "Edelstein Effect..." (2503.20712) Eq (12) |

## 4. Directionality Relations

*   **Spin-Momentum Locking:** The spin expectation value for a state with momentum $k$ is:
    $$ \langle \vec{\sigma} \rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix} $$
    **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (3).
    *   $\theta$: Angle between $k$ and $\hat{x}$ axis.
    *   Spin is tangential to the Fermi surface.

*   **Magnetization Direction:**
    For an electric field applied along $\hat{x}$ ($E = E_x \hat{x}$), the induced magnetization is along $\hat{y}$ ($M = M_y \hat{y}$).
    $$ M \propto [\hat{z} \times E] $$
    **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (2503.20712), Eq. (8), (9).
    *   This relationship holds for both HDR and LDR.
    *   The direction is perpendicular to the applied electric field within the 2D plane.

## 5. Model Implementation Notes

1.  **Regime Selection:** Determine if the system is in HDR ($\mu \ge 0$) or LDR ($\mu < 0$) to select the correct Fermi momenta and Magnetization formula (Eq. 8 vs Eq. 9 from Paper 1).
2.  **Field Strength:** Calculate $\gamma = e E L_s / E_F$. If $\gamma \ll 1$, use the linear Boltzmann formulas. If $\gamma \gtrsim 1$, use the non-linear integral expressions involving Landau-Zener probabilities (Eq. 38 from Paper 2).
3.  **Anisotropy:** If the system is anisotropic, use the susceptibility expressions from Eq. (12) in Paper 1, substituting the mass/coupling ratios $r_m$ and $r_\alpha$.
4.  **Units:** Ensure consistent units (e.g., $\hbar=1$ in some papers, SI in others). Paper 1 uses explicit constants ($\mu_b, e$), while Paper 2 often sets $\hbar=1$.
5.  **Gamma Point:** The Rashba model describes the physics at the $\Gamma$ point ($k=0$) where the band crossing occurs. The Fermi surfaces are circles (isotropic) or ellipses (anisotropic) centered at shifted momenta $\pm k_0$. The Edelstein effect arises from the shift of these Fermi surfaces due to the electric field.
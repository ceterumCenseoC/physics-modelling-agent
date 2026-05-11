

# Model Information for Calculating the Edelstein Effect in Rashba Fermions

The following information is extracted from the provided research papers to build a model for calculating the Edelstein effect (electric-field induced magnetization) in a 2D Rashba electron gas at the Gamma point.

## 1. System Hamiltonian
The system is described by a 2D electron gas with Rashba spin-orbit coupling (SOC). The Hamiltonian is given by:

$$ \hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha_R (\hat{z} \times \mathbf{k}) \cdot \boldsymbol{\sigma} $$

*   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (1).
*   **Parameters:**
    *   $m$: Effective carrier mass.
    *   $\alpha_R$: Rashba spin-orbit coupling strength.
    *   $\mathbf{k} = (k_x, k_y)$: Quasi-momentum.
    *   $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$: Vector of Pauli matrices.
    *   $\hat{z}$: Unit vector perpendicular to the 2D plane.

## 2. Energy Bands and Chirality
The Hamiltonian leads to two energy bands (chirality states $\nu = \pm$) with spin-momentum locking:

$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha_R k $$

*   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Section "DEE in Isotropic Rashba Model" (context of Eq. 5).
*   **Fermi Momenta:** For a given Fermi energy $E_F$, the Fermi momenta for the two bands are:
    $$ k^\pm_F = \mp k_0 + \sqrt{k_0^2 + \frac{2m E_F}{\hbar^2}} $$
    where $k_0 = m \alpha_R / \hbar^2$.
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (5).
*   **Chirality:** The index $\nu = \pm$ corresponds to the two chiral Fermi surfaces (inner and outer).

## 3. Spin Texture (Spin Expectation Value)
The spin expectation value for an eigenstate with momentum $\mathbf{k}$ is tangential to the Fermi surface:

$$ \langle \boldsymbol{\sigma} \rangle^\nu_k = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \nu \sin \theta \\ -\nu \cos \theta \\ 0 \end{pmatrix} $$

*   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (3).
*   **Source:** "Spin accumulation at nonmagnetic interface..." (Page 9), confirms orientation $P_\pm(k) = \pm \frac{\alpha_R}{|\alpha_R|} (-k_y, k_x, 0) / |k|$.
*   **Direction:** The spin lies in the $xy$-plane and is perpendicular to the momentum vector $\mathbf{k}$.

## 4. Magnetization Formula (Edelstein Effect)
Within the semiclassical Boltzmann approach, the magnetization (spin density) $\mathbf{M}$ induced by an electric field $\mathbf{E}$ is calculated as:

$$ \mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| (\mathbf{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \tau_\nu(\mathbf{k}) \delta(E_\nu(\mathbf{k}) - E_F) \langle \boldsymbol{\sigma} \rangle^\nu_{\mathbf{k}} $$

*   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (2).
*   **Parameters:**
    *   $\mu_b$: Bohr magneton.
    *   $\mathbf{v}_\nu(\mathbf{k}) = \nabla_{\mathbf{k}} E_\nu(\mathbf{k})$: Group velocity.
    *   $\tau_\nu(\mathbf{k})$: Transport lifetime (scattering time).
    *   $\delta(\cdot)$: Dirac delta function selecting states at the Fermi surface.

## 5. Analytical Results for Isotropic Rashba Model
Assuming constant relaxation time $\tau_+ = \tau_- = \tau$ and an electric field $\mathbf{E} = E_x \hat{x}$:

### High-Density Regime (HDR)
When both chiral bands are occupied ($E_F > 0$ relative to band crossing):
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha_R E_x $$
Or in vector form:
$$ \mathbf{M} = \frac{\mu_b |e| \tau m \alpha_R}{2\pi} (\hat{z} \times \mathbf{E}) $$

*   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (8).
*   **Implication:** Magnetization is proportional to $\alpha_R$, $\tau$, and $E$. Direction is perpendicular to $\mathbf{E}$ (in-plane).

### Low-Density Regime (LDR)
When only the lower energy band is occupied ($E_F < 0$ relative to band crossing):
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha_R^2 + 2m E_F} E_x $$

*   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (9).
*   **Implication:** Magnetization depends on the Fermi energy $E_F$ (and thus Fermi velocity $v_F$).

## 6. Parameter Dependencies
To compute how the result depends on relevant parameters:

*   **Rashba Coupling ($\alpha_R$):**
    *   In HDR, $M \propto \alpha_R$.
    *   In LDR, $M \propto \sqrt{\alpha_R^2 + E_F}$.
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (8) and (9).
    *   **Source:** "Out-of-plane Edelstein effects..." (arXiv:2501.01888), Equation (13) confirms linear dependence on $\lambda$ (Rashba parameter).

*   **Fermi Velocity ($v_F$):**
    *   Related to $E_F$ via $E_F = \frac{1}{2} m v_F^2$.
    *   In the clean limit (nonlinear regime), spin polarization $S_y \propto \frac{\alpha n}{v_F}$ (where $n$ is density).
    *   **Source:** "Theory of the nonlinear Rashba-Edelstein effect" (arXiv:1506.08330), Equation (37).

*   **Electric Field Magnitude ($E$):**
    *   Linear response: $M \propto E$.
    *   Nonlinear response (Clean limit, high $E$): The spin polarization saturates. The parameter $\gamma = \frac{e E L_s}{E_F}$ determines the regime ($L_s = \hbar / 2m\alpha$).
        *   If $\gamma \ll 1$ (Adiabatic): $M$ grows linearly then saturates.
        *   If $\gamma \gg 1$ (Non-adiabatic): $M$ is suppressed.
    *   **Source:** "Theory of the nonlinear Rashba-Edelstein effect" (arXiv:1506.08330), Section IV and V, Equation (12), (37), (30).

*   **Chirality ($\nu$):**
    *   Affects the Fermi momenta $k^\pm_F$ (Eq. 5) and the sign of the spin texture (Eq. 3).
    *   The total magnetization is the sum of contributions from both bands.
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (3) and (5).

*   **Anisotropy:**
    *   If effective masses ($m_x, m_y$) or Rashba parameters ($\alpha_x, \alpha_y$) are anisotropic, the susceptibility changes.
    *   For mass anisotropy ratio $r_m = m_y/m_x$: $\chi_{xy} \propto \frac{r_m}{1 + \sqrt{r_m}}$.
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Equation (12).

## 7. Direction of Magnetization
*   **Standard Rashba Model:** The induced magnetization is **in-plane** and perpendicular to the applied electric field.
    *   If $\mathbf{E} = E_x \hat{x}$, then $\mathbf{M} = M_y \hat{y}$.
    *   **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Figure 1(b) and Equation (8).
    *   **Source:** "Spin accumulation at nonmagnetic interface..." (Page 9), states spin orientation is "in-plane and perpendicular to the current direction".
*   **Out-of-Plane Magnetization:**
    *   Requires additional terms (e.g., p-wave magnet terms, magnetic field, or anisotropic scattering/non-parabolicity).
    *   Standard Rashba model at Gamma point does **not** produce out-of-plane magnetization in the linear regime without external magnetic fields or specific symmetry breaking.
    *   **Source:** "Out-of-plane spin polarization from in-plane electric and magnetic fields" (arXiv:cond-mat/0609078), Abstract and Equation (16).
    *   **Source:** "Out-of-plane Edelstein effects..." (arXiv:2501.01888), Introduction states "In-plane magnetization is induced by the Edelstein effect in the Rashba spin-orbit interaction system."

## 8. Summary of Model Inputs
To build the model, use the following inputs and equations:
1.  **Input Parameters:** $m$, $\alpha_R$, $E_F$ (or $v_F$), $\tau$, $\mathbf{E}$.
2.  **Calculate:** $k_F^\pm$, $\mathbf{v}_\nu(\mathbf{k})$, $\langle \boldsymbol{\sigma} \rangle^\nu_{\mathbf{k}}$.
3.  **Integrate:** Use Eq. (2) from Paper 1 to sum over the Fermi surface.
4.  **Output:** Vector $\mathbf{M}$ (magnitude and direction).
5.  **Check Regime:** Determine if linear ($\gamma \ll 1$) or nonlinear ($\gamma \sim 1$) using Eq. (12) from Paper 6.

*   **Sources:**
    *   "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712) - Equations (1), (2), (3), (5), (8), (9), (12).
    *   "Theory of the nonlinear Rashba-Edelstein effect" (arXiv:1506.08330) - Equations (12), (37).
    *   "Spin accumulation at nonmagnetic interface..." (Page 9) - Spin orientation.
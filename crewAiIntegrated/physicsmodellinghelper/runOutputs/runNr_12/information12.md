

# Model Information for Calculating the Edelstein Effect in Rashba Fermions

The following information is extracted from the provided sources to build a model for calculating the Edelstein effect (magnetization induced by an electric field) for a Rashba fermion at the Gamma point.

## 1. System Hamiltonian and Band Structure
The system is described by a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC).

**Hamiltonian:**
The Rashba Hamiltonian acting on the spinor wave function is given by:
$$
\hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha_R (\hat{z} \times \mathbf{k}) \cdot \boldsymbol{\sigma}
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 2, Eq (1); `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Page 2, Eq (1).*

**Dispersion Relation:**
The energy spectrum consists of two chiral bands ($\nu = \pm 1$):
$$
E_\nu(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} + \nu \alpha_R k
$$
*Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Page 2, Eq (2); `Enhanced_Edelstein_effect_and_interdimen.pdf`, Page 2, Eq (6).*
*   $\nu = +1$: Inner band (lower energy for small $k$ in some conventions, depends on $\alpha$ sign).
*   $\nu = -1$: Outer band.
*   $k = |\mathbf{k}|$.
*   $\alpha_R$: Rashba coupling strength.
*   $m$: Effective carrier mass.

**Spin Texture:**
The expectation value of the spin operator for eigenstates is locked perpendicular to momentum:
$$
\langle \vec{\sigma} \rangle^\nu_{\mathbf{k}} = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \nu \sin\theta \\ -\nu \cos\theta \\ 0 \end{pmatrix}
$$
where $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$ axis.
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 2, Eq (3); `Spin_accumulation_at_nonmagnetic_interfa.pdf`, Page 9.*

## 2. Fermi Surfaces and Regimes
The Fermi momenta depend on the chemical potential $\mu$ (or Fermi energy $E_F$). Two regimes are defined:

**High-Density Regime (HDR):**
Defined by $\mu \ge 0$ (chemical potential above band crossing). Both chiral bands contribute.
$$
k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + \frac{2m\mu}{\hbar^2}}
$$
where $k_0 = \frac{m \alpha_R}{\hbar^2}$.
*Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Page 2, Eq (3); `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 2, Eq (5).*

**Low-Density Regime (LDR):**
Defined by $\mu < 0$ (chemical potential below band crossing). Only the lower band is occupied.
$$
k^\eta_F = k_0 - \eta \sqrt{k_0^2 + \frac{2m\mu}{\hbar^2}}
$$
where $\eta = \pm$ distinguishes left/right carriers for the lower band.
*Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Page 2, Eq (4); `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 2, Eq (6).*

## 3. Magnetization (Edelstein Effect)
The Edelstein effect generates a non-equilibrium magnetization (spin density) $\mathbf{M}$ in response to an applied electric field $\mathbf{E}$.

**General Formula (Linear Response):**
The magnetization is calculated via the non-equilibrium distribution function $f(\mathbf{k})$:
$$
\mathbf{M} = -\mu_b \sum_{\mathbf{k},\nu} |e| (\vec{\nu}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta[E_\nu(\mathbf{k}) - E_F] \langle \vec{\sigma} \rangle^\nu_{\mathbf{k}}
$$
where $\mu_b$ is the Bohr magneton, $\vec{\nu}_\nu(\mathbf{k})$ is the group velocity, and $\tau$ is the transport time.
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 2, Eq (2).*

**Analytical Expressions:**

*   **HDR ($\mu \ge 0$):**
    $$
    M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha_R [\hat{z} \times \mathbf{E}]_y
    $$
    Assuming $\mathbf{E} = E_x \hat{x}$, the magnetization is along $\hat{y}$.
    *Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 3, Eq (8).*

*   **LDR ($\mu < 0$):**
    $$
    M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha_R^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y
    $$
    *Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 3, Eq (9).*

**Alternative Formulation (Spin Density):**
In terms of spin density $S$ and density of states $N_0 = \frac{m}{2\pi \hbar^2}$:
$$
S_y \simeq \frac{N_0}{2} \alpha_R e E \tau
$$
*Source: `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Page 13, Eq (37).*

## 4. Parameter Dependencies

**Electric Field Magnitude ($|\mathbf{E}|$):**
*   **Linear Regime:** Magnetization magnitude is proportional to $|\mathbf{E}|$.
    *   $M \propto |\mathbf{E}|$.
*   **Nonlinear Regime:** For very large fields or weak scattering, the response becomes nonlinear. A dimensionless parameter $\gamma$ characterizes this:
    $$
    \gamma = \frac{e E L_s}{E_F} = \frac{e E \hbar}{2m \alpha_R E_F}
    $$
    where $L_s = \hbar / (2m \alpha_R)$ is the spin-precession length.
    *   If $\gamma \ll 1$: Adiabatic regime (linear response).
    *   If $\gamma \gg 1$: Non-adiabatic regime (polarization suppressed).
    *   Source: `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Page 2, Eq (12); Page 11-12.

**Electric Field Direction:**
*   The magnetization direction is perpendicular to both the electric field and the spin-orbit field axis ($\hat{z}$).
*   Direction: $\mathbf{M} \propto \hat{z} \times \mathbf{E}$.
    *   If $\mathbf{E} \parallel \hat{x} \implies \mathbf{M} \parallel \hat{y}$.
    *   If $\mathbf{E} \parallel \hat{y} \implies \mathbf{M} \parallel -\hat{x}$.
    *   Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 2, Eq (2), (8).

**Chirality ($\nu$):**
*   Chirality determines the band index ($\nu = \pm$).
*   In HDR, contributions from both chiral bands ($\nu = +$ and $\nu = -$) sum up (Eq 4 in `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`).
*   In LDR, only one band contributes.
*   Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Page 2, Eq (2); `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 2, Eq (4).

**Fermi Velocity ($v_F$):**
*   Group velocity at the Fermi surface:
    $$
    v^\nu_F = \frac{k^\nu_F}{m} + \nu \alpha_R
    $$
*   Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Page 3, Eq (8).
*   Magnetization scales inversely with $v_F$ in some formulations (e.g., $M \propto \alpha_R / v_F^2$ in `Raimondi & Cserti` summary, though explicit formula in PDFs uses $\tau, m, \alpha$).

**Rashba Coupling ($\alpha_R$):**
*   In HDR: $M \propto \alpha_R$.
*   In LDR: $M \propto \sqrt{\alpha_R^2 + \dots}$.
*   Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 3, Eq (8), (9).

**Relaxation Time ($\tau$):**
*   Magnetization is linearly proportional to the transport/relaxation time $\tau$.
*   Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 3, Eq (8), (9).

## 5. Model Building Steps
1.  **Define Parameters:** Set $m, \alpha_R, \mu, \tau, \mathbf{E}$.
2.  **Determine Regime:** Check if $\mu \ge 0$ (HDR) or $\mu < 0$ (LDR).
3.  **Calculate Fermi Momenta:** Use Eq (3) or (4) from `Boltzmann_theory_of_the_inverse_Edelstei.pdf`.
4.  **Calculate Magnetization:** Use Eq (8) or (9) from `Edelstein_Effect_in_Isotropic_and_Anisot.pdf` for linear response.
5.  **Check Nonlinearity:** Calculate $\gamma$ using Eq (12) from `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`. If $\gamma \not\ll 1$, use nonlinear solutions (Eq 30, 38).
6.  **Direction:** Apply $\hat{z} \times \mathbf{E}$ rule.
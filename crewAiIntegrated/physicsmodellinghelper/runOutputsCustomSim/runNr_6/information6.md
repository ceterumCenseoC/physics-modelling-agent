

# Model Information for Calculating the Edelstein Effect in a Rashba Fermion System

The following information is extracted from the provided sources to build a model for calculating the Edelstein effect (current-induced spin polarization/magnetization) for a Rashba fermion at the $\Gamma$ point of the Brillouin zone.

## 1. Model Hamiltonian and Band Structure

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling.

*   **Hamiltonian**: The single-particle Hamiltonian at the $\Gamma$ point is given by:
    $$ \hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha_R (\hat{z} \times \vec{k}) \cdot \vec{\sigma} $$
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Eq. (1); *Boltzmann theory of the inverse Edelstein effect...* (arXiv:2601.02473), Eq. (1).
    *   **Parameters**: $m$ is the effective mass, $\alpha_R$ is the Rashba coupling strength, $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are Pauli matrices, $\hat{z}$ is the unit vector normal to the 2D plane.

*   **Energy Dispersion**: The eigenvalues for the two chiral bands ($\nu = \pm 1$) are:
    $$ E_{\nu}(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha_R \hbar k $$
    *   **Source**: *Boltzmann theory of the inverse Edelstein effect...* (arXiv:2601.02473), Eq. (2).
    *   **Note**: $\nu = +1$ corresponds to the outer Fermi surface (lower energy at $k=0$ for standard convention, check source context), $\nu = -1$ to the inner. In *Edelstein Effect in Isotropic...* (arXiv:2503.20712), Eq. (2) uses $E^\pm_k = \frac{k^2}{2m} \pm k\alpha$.

*   **Fermi Momenta**: The Fermi momenta depend on the chemical potential $\mu$ (or Fermi energy $E_F$).
    *   **High-Density Regime (HDR)** ($\mu \ge 0$, both bands occupied):
        $$ k_F^\nu = -\nu k_0 + \sqrt{k_0^2 + 2m\mu} $$
        where $k_0 = \frac{m \alpha_R}{\hbar^2}$.
        *   **Source**: *Boltzmann theory of the inverse Edelstein effect...* (arXiv:2601.02473), Eq. (3).
    *   **Low-Density Regime (LDR)** ($\mu < 0$, only lower band occupied):
        $$ k_F^\eta = k_0 - \eta \sqrt{k_0^2 + 2m\mu} $$
        where $\eta = \pm$ distinguishes left/right carriers for the lower band.
        *   **Source**: *Boltzmann theory of the inverse Edelstein effect...* (arXiv:2601.02473), Eq. (4).

## 2. Spin Texture

The spin expectation value for an eigenstate with momentum $\vec{k}$ is locked perpendicular to $\vec{k}$ in the plane.

*   **Spin Expectation Value**:
    $$ \langle \vec{\sigma} \rangle^\nu_k = \nu \frac{\hat{z} \times \vec{k}}{k} = \nu \begin{pmatrix} \sin\theta \\ -\cos\theta \\ 0 \end{pmatrix} $$
    where $\theta$ is the angle of $\vec{k}$ with respect to the $x$-axis.
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Eq. (3).
    *   **Note**: Explicitly, $\langle \sigma_x \rangle^\nu_k = \nu \frac{k_y}{k}$ and $\langle \sigma_y \rangle^\nu_k = -\nu \frac{k_x}{k}$.

## 3. Edelstein Effect Formulas (Magnetization)

The Edelstein effect describes the generation of a non-equilibrium in-plane magnetization $\vec{M}$ (or spin density $\vec{S}$) in response to an applied electric field $\vec{E}$.

### A. Linear Response (Diffusive Regime)
In the presence of scattering (relaxation time $\tau$), the magnetization saturates to a steady state value.

*   **Magnetization Vector**:
    $$ \vec{M} = \frac{\mu_b |e| \tau}{2\pi} m \alpha_R (\hat{z} \times \vec{E}) \quad \text{(HDR)} $$
    $$ \vec{M} = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha_R^2 + 2m E_F} (\hat{z} \times \vec{E}) \quad \text{(LDR)} $$
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Eq. (8) and Eq. (9).
    *   **Direction**: The magnetization is perpendicular to the electric field and lies in the 2D plane (e.g., if $\vec{E} = E_x \hat{x}$, then $\vec{M} \parallel \hat{y}$).
    *   **Parameters**: $\mu_b$ is the Bohr magneton, $e$ is the elementary charge.

### B. Nonlinear Response (Clean/Ballistic Regime)
For large electric fields where the drift velocity is comparable to the Fermi velocity, the response becomes nonlinear.

*   **Nonlinearity Parameter**:
    $$ \gamma = \frac{e E L_s}{E_F} $$
    where $L_s = \frac{\hbar}{2m\alpha_R}$ is the spin-precession length.
    *   **Source**: *Theory of the nonlinear Rashba-Edelstein effect* (arXiv:1506.08330), Eq. (12).
*   **Spin Polarization Dynamics**:
    The spin polarization $S_y(t)$ evolves over time $t$ (or dimensionless time $\tau$). For long times ($t \to \infty$), it saturates to a value dependent on $\gamma$.
    *   **Adiabatic Limit ($\gamma \ll 1$)**: $S_y \propto E$.
    *   **Non-Adiabatic Limit ($\gamma \gg 1$)**: $S_y$ is suppressed.
    *   **Source**: *Theory of the nonlinear Rashba-Edelstein effect* (arXiv:1506.08330), Abstract, Eq. (30), Fig. 4.
*   **Steady-State Approximation**:
    In a diffusive system with scattering time $\tau$, the nonlinear correction can be approximated by replacing the linear term with a function of $\gamma$.
    *   **Source**: *Theory of the nonlinear Rashba-Edelstein effect* (arXiv:1506.08330), Eq. (37) for linear limit, Eq. (38) for improved formula.

## 4. Parameter Dependencies

The model output (Magnetization magnitude and direction) depends on the following parameters:

1.  **Electric Field Magnitude ($|\vec{E}|$)**:
    *   **Linear**: $M \propto |\vec{E}|$ for small fields (Eq. 8, 9).
    *   **Nonlinear**: $M$ saturates or decreases for large fields ($\gamma \gtrsim 1$) (Paper 2, Abstract).
2.  **Electric Field Direction ($\phi_E$)**:
    *   $\vec{M}$ rotates by $90^\circ$ relative to $\vec{E}$ in the plane ($\phi_M = \phi_E \pm \pi/2$).
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Eq. (8).
3.  **Rashba Coupling ($\alpha_R$)**:
    *   **HDR**: $M \propto \alpha_R$ (Eq. 8).
    *   **LDR**: $M \propto \sqrt{\alpha_R^2 + \dots}$ (Eq. 9).
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Fig. 3, Eq. (8).
4.  **Fermi Energy / Chemical Potential ($E_F, \mu$)**:
    *   Discontinuity at band crossing ($\mu = 0$).
    *   **HDR**: $M$ is constant with respect to $E_F$ (Eq. 8).
    *   **LDR**: $M$ increases with $\sqrt{E_F}$ (Eq. 9).
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Fig. 2, Eq. (8), (9).
5.  **Scattering Time ($\tau$)**:
    *   $M \propto \tau$ in the diffusive regime.
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Eq. (8).
6.  **Chirality ($\nu$)**:
    *   Determines the Fermi surface topology (HDR vs LDR) and spin texture orientation.
    *   **Source**: *Boltzmann theory of the inverse Edelstein effect...* (arXiv:2601.02473), Eq. (2), (3).

## 5. Explicit Graphics Instructions

To visualize the model results, generate the following plots based on the equations above:

1.  **Magnetization vs. Electric Field Magnitude**:
    *   **X-axis**: $|\vec{E}|$.
    *   **Y-axis**: $|\vec{M}|$.
    *   **Behavior**: Linear slope for small $E$, saturation for large $E$ (using $\gamma$ from Paper 2).
    *   **Source**: *Theory of the nonlinear Rashba-Edelstein effect* (arXiv:1506.08330), Fig. 4.
2.  **Magnetization vs. Chemical Potential**:
    *   **X-axis**: $\mu$ (spanning negative to positive values).
    *   **Y-axis**: $M_y$ (for fixed $E_x$).
    *   **Behavior**: Step-like change at $\mu=0$ (transition from LDR to HDR).
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Fig. 2 (Left Panel).
3.  **Magnetization vs. Rashba Coupling**:
    *   **X-axis**: $\alpha_R$.
    *   **Y-axis**: $M_y$.
    *   **Behavior**: Linear increase for large $\mu$ (HDR), sub-linear for small $\mu$ (LDR).
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Fig. 3 (Right Panel).
4.  **Directional Dependence**:
    *   **X-axis**: Angle of $\vec{E}$ ($\theta_E$).
    *   **Y-axis**: Angle of $\vec{M}$ ($\theta_M$).
    *   **Behavior**: $\theta_M = \theta_E + \pi/2$ (or $-\pi/2$ depending on sign convention of $\alpha_R$).
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Fig. 1(b).
5.  **Spin Texture**:
    *   **Plot**: Vector field of $\langle \vec{\sigma} \rangle$ on the Fermi surface ($k_x, k_y$ plane).
    *   **Behavior**: Tangential vectors forming a vortex.
    *   **Source**: *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Fig. 2 (Right Panel).

## 6. Implementation Notes

*   **Units**: Ensure consistency. Paper 1 uses $\hbar=1$ in some derivations (Eq. 1), while Eq. 8 includes physical constants. Restore $\hbar$ where necessary (e.g., $k_0 = m\alpha_R/\hbar^2$).
*   **Regime Selection**: Check if $E_F > 0$ (HDR) or $E_F < 0$ (LDR) to select the correct formula for $k_F$ and $M$.
*   **Nonlinearity**: For high fields, calculate $\gamma$. If $\gamma \ll 1$, use linear formulas. If $\gamma \gtrsim 1$, apply the saturation factor from Paper 2 (Eq. 30 or Fig. 4).
*   **Source for Nonlinear Saturation**: *Theory of the nonlinear Rashba-Edelstein effect* (arXiv:1506.08330), Eq. (30) gives the exact long-time limit of spin polarization $S_y(\tau)$ as a function of $\gamma$ and $\theta_p$. The angular average gives the total polarization (Fig. 4).
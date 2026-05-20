

# Model Specification: Edelstein Effect for a Rashba Fermion at the Gamma Point

## 1. System Hamiltonian and Band Structure

The model describes a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC) at the Gamma point ($\Gamma$) of the Brillouin zone.

### 1.1 Isotropic Rashba Hamiltonian
The fundamental Hamiltonian for the isotropic case is given by:
$$ \hat{H} = \frac{\mathbf{p}^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}) $$
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (1).
*   $\mathbf{p}$: Momentum operator.
*   $m$: Effective carrier mass.
*   $\alpha$: Rashba spin-orbit coupling strength.
*   $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$: Vector of Pauli matrices.
*   $\hat{z}$: Unit vector normal to the 2D plane.

### 1.2 Energy Dispersion and Fermi Surfaces
The eigenenergies for the two chiral bands ($\nu = \pm 1$) are:
$$ E_{\nu}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k $$
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Section "DEE: Analytical and Numerical Calculation of Spin Density".
*   $k = |\mathbf{k}| = \sqrt{k_x^2 + k_y^2}$.
*   $\nu = +1$ corresponds to the outer Fermi surface (lower energy branch in some conventions, or defined by the sign of the SOC term).
*   $\nu = -1$ corresponds to the inner Fermi surface.

The Fermi wavevectors $k_F^{\nu}$ are determined by the Fermi energy $E_F$:
$$ k_F^{\pm} = \mp k_0 + \sqrt{k_0^2 + \frac{2mE_F}{\hbar^2}} $$
where $k_0 = \frac{m\alpha}{\hbar^2}$.
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (5) for High-Density Regime (HDR).

### 1.3 Spin Expectation Values
The spin texture is locked perpendicular to the momentum. The expectation value of the spin operator $\boldsymbol{\sigma}$ for eigenstate $\nu$ with momentum $\mathbf{k}$ is:
$$ \langle \boldsymbol{\sigma} \rangle_{\nu, \mathbf{k}} = \nu \frac{1}{k} \begin{pmatrix} -k_y \\ k_x \\ 0 \end{pmatrix} = \nu \begin{pmatrix} -\sin\theta_k \\ \cos\theta_k \\ 0 \end{pmatrix} $$
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (3).
*   $\theta_k$: Angle between $\mathbf{k}$ and the $\hat{x}$-axis.
*   Note: The text defines the spin vector as $\pm \sin(\theta) \hat{x} \mp \cos(\theta) \hat{y}$. The direction is perpendicular to $\mathbf{k}$ in the plane.

## 2. Theoretical Framework: Semiclassical Boltzmann Approach

The magnetization (spin density) is calculated using the semiclassical Boltzmann equation in the relaxation time approximation.

### 2.1 General Expression for Magnetization
The expectation value of the magnetization $\mathbf{M}$ (total spin density) to first order in the electric field $\mathbf{E}$ is:
$$ \mathbf{M} = -\mu_B \sum_{\mathbf{k}, \nu} |e| (\mathbf{v}_{\nu}(\mathbf{k}) \cdot \mathbf{E}) \delta [E_{\nu}(\mathbf{k}) - E_F] \langle \boldsymbol{\sigma} \rangle_{\nu, \mathbf{k}} \bar{\tau}_{\nu}(\mathbf{k}) $$
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (2).
*   $\mu_B$: Bohr magneton.
*   $e$: Elementary charge.
*   $\mathbf{v}_{\nu}(\mathbf{k}) = \nabla_{\mathbf{k}} E_{\nu}(\mathbf{k})$: Group velocity.
*   $\bar{\tau}_{\nu}(\mathbf{k})$: Transport lifetime.
*   The sum is over the Fermi surface ($E_{\nu}(\mathbf{k}) = E_F$).

### 2.2 Edelstein Susceptibility Tensor
The linear response is defined by the Edelstein susceptibility $\chi_{ij}$:
$$ M_j = \chi_{ij} E_i $$
$$ \chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \, \langle \sigma_y \rangle_{\nu, \mathbf{k}} \delta(E_{\nu}(\mathbf{k}) - \mu) v_{\nu, x}(\mathbf{k}) $$
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (7).
*   $\chi_0 = \frac{\tau |e| \mu_B S_{cell}}{4\pi^2 a}$, where $\tau$ is the transport time, $S_{cell}$ is the unit cell area, and $a$ is the lattice parameter.

## 3. Analytical Solutions for Magnetization

### 3.1 High-Density Regime (HDR)
When both chiral bands are occupied ($E_F > 0$ relative to the band crossing):
Assuming a constant relaxation time $\tau_+ = \tau_- = \tau$ and an electric field $\mathbf{E} = E_x \hat{x}$:
$$ M_y = \frac{\mu_B |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y $$
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8).
*   **Result:** The magnetization is constant and independent of the Fermi energy $E_F$ in the high-density limit.
*   **Direction:** Perpendicular to the electric field (e.g., if $\mathbf{E} \parallel \hat{x}$, then $\mathbf{M} \parallel -\hat{y}$).

### 3.2 Low-Density Regime (LDR)
When only the lower energy band is occupied ($E_F < 0$ relative to the band crossing, or near the band minimum):
$$ M_y = \frac{\mu_B |e| \tau}{2\pi} \sqrt{(m\alpha)^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y $$
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (9).
*   **Result:** The magnetization increases with the square root of the Fermi energy.

### 3.3 Expansion near Band Crossing
For Fermi energies close to the band crossing ($E_F \approx 0$):
$$ M_y \approx \frac{\mu_B |e| \tau}{2\pi} \left( m\alpha + \frac{E_F}{2\alpha} \right) [\hat{z} \times \mathbf{E}]_y $$
**Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (10).

## 4. Parameter Dependencies

### 4.1 Spin-Orbit Coupling Strength ($\alpha$)
*   **Linear Dependence:** In the high-density regime, $M_y \propto \alpha$.
*   **Susceptibility:** The Edelstein susceptibility $\chi_{xy}$ increases linearly with $\alpha$ for fixed chemical potential $\mu$.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Page 3, Figure 3 analysis and Eq. (8).

### 4.2 Fermi Velocity ($v_F$) and Effective Mass ($m$)
*   The Fermi velocity is related to the parameters via $v_F = \frac{\hbar k_F}{m}$.
*   In the HDR, the magnetization depends on the product $m\alpha$.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8).

### 4.3 Electric Field Direction and Magnitude
*   **Direction:** The induced magnetization $\mathbf{M}$ is always perpendicular to the applied electric field $\mathbf{E}$ and lies in the plane. Specifically, $\mathbf{M} \propto \hat{z} \times \mathbf{E}$.
    *   If $\mathbf{E} = E_x \hat{x}$, then $\mathbf{M} = M_y \hat{y}$ (with $M_y$ having a sign determined by the chirality and $\alpha$).
*   **Magnitude:** In the linear regime, $M \propto E$.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8) and Figure 1.

### 4.4 Chirality ($\nu$)
*   The two chiral bands contribute with opposite signs to the spin density. In the HDR, the net magnetization arises from the difference in the populations or the asymmetry in the scattering times ($\bar{\tau}_+$ vs $\bar{\tau}_-$) and Fermi wavevectors ($k_F^+$ vs $k_F^-$).
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (4) and Eq. (5).

### 4.5 Anisotropy (Effective Mass and Rashba Parameter Ratios)
For systems with $C_{2v}$ symmetry (anisotropic):
*   **Mass Anisotropy:** Ratio $r_m = m_y / m_x$.
    $$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} $$
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (12).
*   **Rashba Anisotropy:** Ratio $r_\alpha = \alpha_y / \alpha_x$.
    $$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} $$
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (12).
*   **Effect:** The susceptibility increases as $r_m$ and $r_\alpha$ increase (for values $>1$), allowing for a "boost" in the Edelstein response compared to the isotropic case.

## 5. Nonlinear Regime (High Electric Fields)

If the electric field is strong enough such that the drift velocity $v_d$ is comparable to the Fermi velocity $v_F$, the linear response breaks down.

### 5.1 Non-Adiabatic Parameter
The regime is governed by the dimensionless parameter $\gamma$:
$$ \gamma = \frac{e E L_s}{E_F} = \frac{e E}{\alpha p_F^2} $$
where $L_s = \hbar / (2m\alpha)$ is the spin-precession length.
**Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Eq. (12).

### 5.2 Behavior of Magnetization
*   **Adiabatic Regime ($\gamma \ll 1$):** The spin follows the effective magnetic field adiabatically. The spin polarization grows and saturates at a maximum value $n(\alpha/v_F)$.
    *   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Abstract and Section IV.
*   **Non-Adiabatic Regime ($\gamma \gg 1$):** The spin evolution is non-adiabatic. The spin polarization is progressively reduced and eventually suppressed as $\gamma \to \infty$.
    *   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Abstract and Section III (Eq. 30 and Fig. 4).
*   **Saturation Value:** In the adiabatic limit, the long-time limit of the spin polarization $S_y$ is:
    $$ S_y(\infty) = -\frac{\alpha n}{v_F} $$
    **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Section III and Fig. 4 caption.

## 6. Orbital Edelstein Effect (Optional Extension)

In bilayer systems or systems with specific symmetries, an orbital magnetization $M^{orb}$ can also be induced.
*   **Formula:** $m = -\mu_B \frac{\hbar}{A_0 A_s} \sum_{nk} f_{nk} (g_s s_{nk} + g_l l_{nk})$.
    **Source:** *Spin and orbital Edelstein effect in a bilayer system with Rashba interaction*, Eq. (1).
*   **Dependence:** The orbital contribution depends on the asymmetry between layers (e.g., difference in Rashba parameters $\alpha_A - \alpha_B$ or masses $m_A - m_B$).
*   **Sign Change:** The sign of the orbital Edelstein effect can reverse depending on the layer localization of the eigenstates.
    **Source:** *Spin and orbital Edelstein effect in a bilayer system with Rashba interaction*, Section IV.B and Eq. (12), (14).

## 7. Required Graphics for Model Validation

To fully characterize the model, the following graphics should be generated:
1.  **Magnetization vs. Electric Field Magnitude:** Plot $M_y$ vs. $E_x$ showing the linear regime and the saturation/nonlinear regime (using the exact solution from *Theory of the nonlinear Rashba-Edelstein effect*, Eq. 29/30).
2.  **Magnetization Direction:** Vector plot showing $\mathbf{M}$ is perpendicular to $\mathbf{E}$ (e.g., $\mathbf{E}$ along $\hat{x}$, $\mathbf{M}$ along $\hat{y}$).
3.  **Parameter Dependence:**
    *   $M_y$ vs. $\alpha$ (Linear increase).
    *   $M_y$ vs. $E_F$ (Saturation in HDR, square root dependence in LDR).
    *   $M_y$ vs. anisotropy ratios $r_m$ and $r_\alpha$ (Non-monotonic or increasing trends depending on the regime).
    **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Figures 2, 3, 5, 6.
4.  **Nonlinear Response:** Plot of $S_y/n$ vs. $\gamma$ (or drift velocity) showing the transition from adiabatic saturation to non-adiabatic suppression.
    **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Figures 4 and 5.

## 8. Summary of Key Equations for Implementation

1.  **Hamiltonian:** $H = \frac{\hbar^2 k^2}{2m} + \alpha (\hat{z} \times \mathbf{k}) \cdot \boldsymbol{\sigma}$.
2.  **Linear Magnetization (HDR):** $M_y = \frac{\mu_B e \tau}{2\pi} m \alpha E_x$.
3.  **Linear Magnetization (LDR):** $M_y = \frac{\mu_B e \tau}{2\pi} \sqrt{(m\alpha)^2 + 2m E_F} E_x$.
4.  **Nonlinear Parameter:** $\gamma = \frac{e E}{\alpha p_F^2}$.
5.  **Nonlinear Spin Polarization:** $S_y(\tau) = \frac{2\alpha n}{v_F} \frac{1}{2\pi} \int_0^{2\pi} d\theta_p \left( |u_p(\tau - \tau_p)|^2 - \frac{1}{2} \right)$, where $u_p$ is derived from Landau-Zener parabolic cylinder functions (Eq. 19, 29 in *Theory of the nonlinear Rashba-Edelstein effect*).

**Sources:**
*   *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712): Pages 1-9, Eqs. (1)-(12), Figures 1-6.
*   *Theory of the nonlinear Rashba-Edelstein effect* (arXiv:1506.08330): Pages 1-18, Eqs. (1)-(50), Figures 1-7.
*   *Spin and orbital Edelstein effect in a bilayer system with Rashba interaction* (arXiv:2307.02872): Pages 1-10, Eqs. (1)-(17), Figures 1-9.
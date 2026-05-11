

# Model Information for Calculating the Edelstein Effect in a Rashba Fermion System

This document provides the necessary theoretical framework, equations, and parameter dependencies required to build a model that calculates the Edelstein effect (spin-to-charge conversion) for a Rashba fermion at the $\Gamma$ point of the Brillouin zone. The information is extracted from the provided research papers.

## 1. Rashba Hamiltonian and Band Structure

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian describes the kinetic energy and the spin-orbit interaction.

### 1.1 Hamiltonian
The Rashba Hamiltonian in momentum space is given by:
$$
\hat{H} = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\hat{z} \times \vec{k}) \cdot \vec{\sigma}
$$
where $m^*$ is the effective mass, $\alpha_R$ is the Rashba coupling strength, $\vec{k} = (k_x, k_y)$ is the in-plane momentum, $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices, and $\hat{z}$ is the unit vector perpendicular to the 2D plane.
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (1), Page 1.
*   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (1), Page 2. (Note: Uses $\hbar=1$).

### 1.2 Energy Dispersion
The energy spectrum consists of two chiral bands ($\nu = \pm$) split by the Rashba term:
$$
\varepsilon_k^\nu = \frac{\hbar^2 k^2}{2m^*} + \nu \alpha_R \hbar k
$$
where $\nu = +$ corresponds to the outer band and $\nu = -$ to the inner band.
*   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (2), Page 2.

### 1.3 Fermi Momenta
The Fermi momenta depend on the chemical potential $\mu$ (or Fermi energy $E_F$). Two regimes are distinguished:
*   **High-Density Regime (HDR):** $\mu \ge 0$ (both bands occupied).
    $$
    k_F^\nu = -\nu k_0 + \sqrt{k_0^2 + 2m^*\mu/\hbar^2}
    $$
    where $k_0 = m^*\alpha_R/\hbar^2$.
    *   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (3), Page 2.
*   **Low-Density Regime (LDR):** $\mu < 0$ (only lower band occupied).
    $$
    k_F^\eta = k_0 - \eta \sqrt{k_0^2 + 2m^*\mu/\hbar^2}
    $$
    where $\eta = \pm$ distinguishes left/right carriers.
    *   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (4), Page 2.

## 2. Direct Edelstein Effect (DEE) Formulation

The Direct Edelstein Effect describes the generation of a non-equilibrium spin polarization (magnetization) $\vec{M}$ (or $\vec{S}$) in response to an applied electric field $\vec{E}$.

### 2.1 Magnetization Definition
The total spin density (magnetization) is calculated as the sum over occupied states weighted by the non-equilibrium distribution function deviation:
$$
\vec{M} = -\mu_B \sum_{\vec{k}, \nu} |e| (\vec{v}^\nu(\vec{k}) \cdot \vec{E}) \delta[\varepsilon_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_\vec{k}^\nu
$$
where $\mu_B$ is the Bohr magneton, $e$ is the elementary charge, $\vec{v}^\nu(\vec{k})$ is the group velocity, and $\langle \vec{\sigma} \rangle_\vec{k}^\nu$ is the spin expectation value.
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (2), Page 2.

### 2.2 Spin Expectation Value
The spin texture is locked perpendicular to the momentum (spin-momentum locking):
$$
\langle \vec{\sigma} \rangle_k^\pm = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
$$
where $\theta$ is the angle between $\vec{k}$ and the $\hat{x}$ axis.
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (3), Page 2.

### 2.3 Edelstein Susceptibility
The linear response is defined by the susceptibility tensor $\chi$:
$$
\vec{M} = \chi \vec{E}
$$
For an isotropic Rashba system with an electric field $\vec{E} = E_x \hat{x}$, the induced magnetization is along $\hat{y}$ (perpendicular to $\vec{E}$):
$$
M_y = \chi_{xy} E_x
$$
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (6), Page 2.

## 3. Analytical Expressions for Magnetization

Assuming a constant relaxation time $\tau$ (semiclassical Boltzmann approach), the magnitude of the magnetization depends on the density regime.

### 3.1 High-Density Regime (HDR)
When both chiral bands are occupied ($\mu \ge 0$), the spin density along $\hat{y}$ for $\vec{E} = E_x \hat{x}$ is:
$$
M_y = \frac{\mu_B |e| \tau}{2\pi} m^* \alpha_R [\hat{z} \times \vec{E}]_y
$$
This result indicates that the magnetization is constant and independent of the Fermi energy in the HDR limit (assuming $\tau$ is constant).
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (8), Page 3.

### 3.2 Low-Density Regime (LDR)
When only the lower band is occupied ($\mu < 0$), the spin density is:
$$
M_y = \frac{\mu_B |e| \tau}{2\pi} \sqrt{(m^{*2} \alpha_R^2 + 2m^* E_F)} [\hat{z} \times \vec{E}]_y
$$
For small Fermi energy near the band crossing, this expands to:
$$
M_y \approx \frac{\mu_B |e| \tau}{2\pi} \left( \alpha_R m^* + \frac{E_F}{2\alpha_R} \right) [\hat{z} \times \vec{E}]_y
$$
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (9), Page 3.
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (10), Page 3.

## 4. Parameter Dependencies

The model must account for how the result varies with physical parameters.

### 4.1 Chirality ($\nu$)
The spin polarization arises from the imbalance of populations in the two chiral bands. In the HDR, the contributions from the two bands ($\nu = \pm$) partially cancel but do not fully vanish due to the difference in Fermi velocities and densities.
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (4), Page 2.

### 4.2 Fermi Velocity ($v_F$)
The group velocity determines the drift induced by the electric field.
$$
v_F^\nu = \left. \frac{\partial \varepsilon_k^\nu}{\partial k} \right|_{k=k_F^\nu} = \frac{\hbar k_F^\nu}{m^*} + \nu \alpha_R
$$
*   **Source:** `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Eq. (8), Page 3.

### 4.3 Rashba Coupling ($\alpha_R$)
The magnitude of the Edelstein effect scales linearly with $\alpha_R$ in the HDR (Eq. 8) and depends on $\sqrt{\alpha_R^2 + \dots}$ in the LDR. Increasing $\alpha_R$ generally increases the susceptibility.
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (8), Page 3.
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Fig. 3 (Right Panel), Page 3.

### 4.4 Scattering Time ($\tau$)
The magnetization is directly proportional to the transport scattering time $\tau$.
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (8), Page 3.

### 4.5 Anisotropy
If the system has anisotropic effective masses ($m_x \neq m_y$) or Rashba parameters ($\alpha_x \neq \alpha_y$), the susceptibility is modified. For anisotropy ratio $r_m = m_y/m_x$:
$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha_R r_m}{1 + \sqrt{r_m}}
$$
*   **Source:** `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (12), Page 4.

## 5. Non-Linear and High-Field Regime

For large electric fields where the drift velocity $v_d$ approaches the Fermi velocity $v_F$, the linear response approximation breaks down.

### 5.1 Non-Adiabatic Parameter
The regime is characterized by the parameter $\gamma$:
$$
\gamma = \frac{e E L_s}{E_F} = \frac{e E}{\alpha_R p_F^2}
$$
where $L_s = \hbar/(2m^*\alpha_R)$ is the spin-precession length.
*   **Source:** `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Eq. (12), Page 7.

### 5.2 Spin Polarization Behavior
*   **Adiabatic ($\gamma \ll 1$):** Spin polarization grows and saturates.
*   **Non-Adiabatic ($\gamma \gg 1$):** Spin polarization is suppressed.
*   **Source:** `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Page 2 (Abstract).

### 5.3 Linear Limit Recovery
In the linear response limit ($\gamma \ll 1$), the spin density recovers the standard form:
$$
S_y(t) \simeq \frac{N_0}{2} \alpha_R e E t
$$
where $N_0$ is the density of states. In the presence of scattering ($\tau$), $t \to \tau$.
*   **Source:** `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Eq. (37), Page 13.

## 6. Summary of Model Inputs and Outputs

| Input Parameter | Symbol | Description | Source |
| :--- | :--- | :--- | :--- |
| Effective Mass | $m^*$ | Carrier effective mass | `Edelstein_Effect...`, Eq. (1), Pg 1 |
| Rashba Coupling | $\alpha_R$ | Spin-orbit coupling strength | `Edelstein_Effect...`, Eq. (1), Pg 1 |
| Electric Field | $\vec{E}$ | Applied field vector | `Edelstein_Effect...`, Eq. (2), Pg 2 |
| Chemical Potential | $\mu$ | Determines HDR/LDR | `Boltzmann_theory...`, Eq. (3,4), Pg 2 |
| Scattering Time | $\tau$ | Transport relaxation time | `Edelstein_Effect...`, Eq. (8), Pg 3 |
| Bohr Magnetron | $\mu_B$ | Magnetic moment unit | `Edelstein_Effect...`, Eq. (2), Pg 2 |

| Output Quantity | Symbol | Description | Source |
| :--- | :--- | :--- | :--- |
| Magnetization | $\vec{M}$ | Induced spin density | `Edelstein_Effect...`, Eq. (2), Pg 2 |
| Direction | $\hat{y}$ | Perpendicular to $\vec{E}$ ($\hat{z} \times \vec{E}$) | `Edelstein_Effect...`, Eq. (8), Pg 3 |
| Susceptibility | $\chi$ | Linear response coefficient | `Edelstein_Effect...`, Eq. (6), Pg 2 |
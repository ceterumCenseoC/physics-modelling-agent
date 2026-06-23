

# Edelstein Effect Model for Rashba Fermions

This document provides the necessary information to calculate the Direct Edelstein Effect (DEE) for a Rashba fermion at the Gamma point of the Brillouin zone. The model is based on the semiclassical Boltzmann approach as detailed in **Gaiardoni et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models"** [1].

## 1. Theoretical Framework

### 1.1 Hamiltonian
The system is described by the Rashba Hamiltonian for a two-dimensional electron gas (2DEG):

$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}) \quad (1) $$

Where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling (RSOC) strength.
*   $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

The energy dispersion relation is split into two chiral bands ($\nu = \pm$):
$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k $$
The helicity operator is $\hat{S} = \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})/p$, with eigenvalues $s = \pm 1$.

### 1.2 Magnetization (Edelstein Effect)
The magnetization $\mathbf{M}$ (or total spin density) induced by an external electric field $\mathbf{E}$ is calculated to the first order in $\mathbf{E}$ using the Boltzmann framework [1]:

$$ \mathbf{M} = -\mu_b \sum_{\mathbf{k},\nu} |e| (\mathbf{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta[E_\nu(\mathbf{k}) - E_F] \langle \boldsymbol{\sigma} \rangle_\nu^{\mathbf{k}} \quad (2) $$

Where:
*   $\mu_b$ is the Bohr magneton.
*   $e$ is the elementary charge.
*   $\mathbf{v}_\nu(\mathbf{k}) = \nabla_{\mathbf{k}} E_\nu(\mathbf{k}) / \hbar$ is the group velocity.
*   $\bar{\tau}_\nu^{\mathbf{k}}$ is the transport lifetime (assumed constant $\tau$ in analytical derivations).
*   $\langle \boldsymbol{\sigma} \rangle_\nu^{\mathbf{k}}$ is the spin expectation value for eigenstate $\nu$.

The spin expectation value for the Rashba eigenstates is given by:
$$ \langle \boldsymbol{\sigma} \rangle_\pm^{\mathbf{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix} \quad (3) $$
where $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$ axis.

## 2. Analytical Results

### 2.1 Isotropic Rashba Model
For an isotropic system ($m_x = m_y = m$, $\alpha_x = \alpha_y = \alpha$), the magnetization is perpendicular to the electric field ($\mathbf{M} \parallel \hat{z} \times \mathbf{E}$). Assuming an electric field $\mathbf{E} = E_x \hat{x}$, the magnetization is along $\hat{y}$.

#### High-Density Regime (HDR)
When both chiral bands are occupied ($E_F > 0$):
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y \quad (4) $$
*   **Magnitude:** Constant with respect to Fermi energy $E_F$.
*   **Direction:** Perpendicular to $\mathbf{E}$ (along $\hat{y}$ for $\mathbf{E} \parallel \hat{x}$).
*   **Dependency:** Linearly proportional to the spin-orbit coupling $\alpha$ and effective mass $m$.

#### Low-Density Regime (LDR)
When only the lower energy band is occupied ($E_F < 0$, but $E_F > -m\alpha^2/2$):
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y \quad (5) $$
*   **Magnitude:** Increases linearly with Fermi energy $E_F$ for small $E_F$.
*   **Dependency:** Depends on both $\alpha$ and $E_F$.

### 2.2 Anisotropic Rashba Model
For systems with $C_{2v}$ symmetry, anisotropy is introduced via effective masses ($m_x \neq m_y$) and Rashba parameters ($\alpha_x \neq \alpha_y$). The Edelstein susceptibility $\chi_{xy}$ (where $M_y = \chi_{xy} E_x$) depends on the ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$.

In the High-Density Regime, the analytical expressions for the susceptibility are [1]:

$$ \frac{\chi_{xy}}{\chi_0}(r_m) = 4\pi m_x \alpha \frac{r_m}{1 + \sqrt{r_m}} \quad (6) $$
$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = 4\pi m \alpha_x \frac{r_\alpha}{1 + r_\alpha} \quad (7) $$

Where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ is a reference susceptibility scale.

## 3. Parameter Dependencies

The model allows for the computation of magnetization magnitude and direction based on the following parameters:

| Parameter | Symbol | Effect on Magnetization ($M$) |
| :--- | :---: | :--- |
| **Electric Field Magnitude** | $|\mathbf{E}|$ | Linear increase ($M \propto |\mathbf{E}|$) |
| **Electric Field Direction** | $\mathbf{E}$ | Magnetization direction is $\mathbf{M} \propto \hat{z} \times \mathbf{E}$ |
| **Spin-Orbit Coupling** | $\alpha$ | Linear increase in HDR (Eq. 4); Non-linear in LDR (Eq. 5) |
| **Effective Mass** | $m$ | Linear increase in HDR; Square root dependence in LDR |
| **Fermi Energy** | $E_F$ | Constant in HDR; Linear increase in LDR (for small $E_F$) |
| **Anisotropy ($r_m$)** | $m_y/m_x$ | Increases susceptibility if $r_m > 1$; decreases if $r_m < 1$ |
| **Anisotropy ($r_\alpha$)** | $\alpha_y/\alpha_x$ | Increases susceptibility if $r_\alpha > 1$; decreases if $r_\alpha < 1$ |
| **Transport Time** | $\tau$ | Linear proportionality ($M \propto \tau$) |

## 4. Computation of Magnetization Direction

The direction of the induced magnetization is determined by the cross product of the unit vector normal to the plane ($\hat{z}$) and the applied electric field vector ($\mathbf{E}$).

*   **Case 1:** $\mathbf{E} = E_x \hat{x} \implies \mathbf{M} = M_y \hat{y}$
    *   $M_y > 0$ for standard parameters ($\alpha > 0$).
*   **Case 2:** $\mathbf{E} = E_y \hat{y} \implies \mathbf{M} = -M_x \hat{x}$
    *   $M_x < 0$ (Magnetization opposes the x-axis).
*   **Case 3:** $\mathbf{E} = E (\cos \phi \hat{x} + \sin \phi \hat{y}) \implies \mathbf{M} \propto (-\sin \phi \hat{x} + \cos \phi \hat{y})$

The magnitude scales linearly with the magnitude of the electric field $|\mathbf{E}|$.

## 5. Explicit Graphics and Trends

Based on the analytical and numerical results in the source material [1], the following graphics describe the model behavior:

### 5.1 Edelstein Susceptibility vs. Chemical Potential
*   **Description:** A plot of $\chi_{xy}/\chi_0$ versus chemical potential $\mu$.
*   **Trend:** In the HDR, the susceptibility reaches a plateau. In the LDR, it increases linearly with $\mu$ starting from the band crossing.
*   **Reference:** Figure 2 (Left panel) in [1].

### 5.2 Susceptibility vs. Spin-Orbit Coupling ($\alpha$)
*   **Description:** A plot of $\chi_{xy}/\chi_0$ versus $\alpha$ at fixed $\mu$.
*   **Trend:** Linear increase of susceptibility with $\alpha$. As $\alpha$ increases, the plateau value in the HDR also increases.
*   **Reference:** Figure 3 (Right panel) in [1].

### 5.3 Susceptibility vs. Anisotropy Ratios ($r_m, r_\alpha$)
*   **Description:** A plot of $\chi_{xy}/\chi_0$ versus $r_m$ (mass ratio) and $r_\alpha$ (SOC ratio).
*   **Trend:**
    *   For $r_m < 1$ or $r_\alpha < 1$, susceptibility is lower than the isotropic case.
    *   For $r_m > 1$ or $r_\alpha > 1$, susceptibility increases, potentially boosting the Edelstein response.
    *   The relationship is linear for small ratios and tends to saturate for very large ratios ($r_\alpha \gg 1$).
*   **Reference:** Figure 5 and Figure 6 in [1].

## 6. Implementation Logic

To compute the magnetization for a given set of parameters:

1.  **Define Parameters:** Set $m, \alpha, \tau, E_F, \mathbf{E}$.
2.  **Determine Regime:** Check if $E_F > 0$ (HDR) or $E_F < 0$ (LDR).
3.  **Check Anisotropy:** If $m_x \neq m_y$ or $\alpha_x \neq \alpha_y$, calculate $r_m$ and $r_\alpha$ and use Eqs. (6) or (7).
4.  **Calculate Susceptibility:**
    *   **Isotropic HDR:** $\chi = \frac{\mu_b |e| \tau}{2\pi} m \alpha$.
    *   **Isotropic LDR:** $\chi = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F}$.
5.  **Compute Magnetization:** $\mathbf{M} = \chi (\hat{z} \times \mathbf{E})$.
6.  **Output:** Magnitude $|\mathbf{M}|$ and direction vector $\mathbf{M}/|\mathbf{M}|$.

## References

[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv preprint arXiv:2503.20712* (2025). [Source: `partialExecutionOutputs\runNr_1\pdfs\Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf`]
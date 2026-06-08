

# Edelstein Effect in Rashba Fermion Systems: Model and Calculations

This document provides the necessary information to build a computational model for calculating the Edelstein effect in a 2D Rashba electron gas at the Gamma point of the Brillouin zone. The information is extracted from the most relevant recent literature, specifically the study of isotropic and anisotropic Rashba models using the semiclassical Boltzmann approach.

## 1. Theoretical Framework

### 1.1 Hamiltonian
The system is described by a 2D Rashba Hamiltonian. For the **isotropic** case, the Hamiltonian is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \vec{\sigma})
$$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling (SOC) strength.
*   $\vec{\sigma}$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

For the **anisotropic** case (e.g., $C_{2v}$ symmetry), the Hamiltonian becomes:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

where $m_x, m_y$ are effective masses and $\alpha_x, \alpha_y$ are SOC parameters along the principal axes.

### 1.2 Boltzmann Transport Approach
The Direct Edelstein Effect (DEE) is calculated using the semiclassical Boltzmann approach. The expectation value of the magnetization $\mathbf{M}$ (or total spin density) at first order in the electric field $\mathbf{E}$ is:

$$
\mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| (\vec{\nu}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta [E_\nu(\mathbf{k}) - E_F] \langle \vec{\sigma} \rangle_\nu^{\mathbf{k}}
$$

where:
*   $\mu_b$ is the Bohr magneton.
*   $\nu = \pm$ indicates the two chiral Fermi surfaces (helicity bands).
*   $\vec{\nu}_\nu(\mathbf{k}) = \bar{\tau}_\nu^{\mathbf{k}} \mathbf{v}_\nu(\mathbf{k})$ is the mean free path, with $\bar{\tau}_\nu^{\mathbf{k}}$ as the transport lifetime and $\mathbf{v}_\nu(\mathbf{k}) = \nabla_{\mathbf{k}} E_\nu(\mathbf{k})$ as the group velocity.
*   $E_F$ is the Fermi energy.

The spin expectation value for the eigenstates is:

$$
\langle \vec{\sigma} \rangle_\pm^{\mathbf{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
$$

where $\theta$ is the angle between the wavevector $\mathbf{k}$ and the $\hat{x}$ axis, and $k = \sqrt{k_x^2 + k_y^2}$.

## 2. Isotropic Rashba Model

### 2.1 High-Density Regime (HDR)
In the HDR, both chiral bands are occupied ($E_F$ above the band crossing). Assuming a constant transport time $\tau$ and an electric field $\mathbf{E} = E_x \hat{x}$, the magnetization along the $\hat{y}$ direction is:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
$$

Since $[\hat{z} \times \hat{x}]_y = 1$, this simplifies to:
$$
M_y = \frac{\mu_b |e| \tau m \alpha}{2\pi} E_x
$$

**Key Finding:** In the HDR, the magnetization is **constant and independent of the Fermi energy** $E_F$, scaling linearly with the SOC strength $\alpha$ and the electric field $E_x$.

### 2.2 Low-Density Regime (LDR)
In the LDR, only the lowest energy band is occupied ($E_F$ below the band crossing). The magnetization is:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{(m^2 \alpha^2 + 2m E_F)} [\hat{z} \times \mathbf{E}]_y
$$

**Key Finding:** In the LDR, the magnetization **depends on the Fermi energy**. For small $E_F$ around the band crossing, it can be expanded as:
$$
M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) E_x
$$

### 2.3 Magnetization Direction
The induced magnetization is always **in-plane** and **perpendicular** to the applied electric field.
*   If $\mathbf{E} \parallel \hat{x}$, then $\mathbf{M} \parallel \hat{y}$.
*   General relation: $\mathbf{M} \propto \hat{z} \times \mathbf{E}$.

## 3. Anisotropic Rashba Model

Anisotropy is introduced via effective mass ratios $r_m = m_y/m_x$ and SOC parameter ratios $r_\alpha = \alpha_y/\alpha_x$. The Edelstein susceptibility $\chi_{xy}$ (defined by $m_j = \chi_{ij} E_i$) in the HDR is given analytically as:

### 3.1 Mass Anisotropy ($r_m$)
With fixed $\alpha$, the susceptibility dependence on mass ratio is:

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
$$

where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ is a reference susceptibility.

### 3.2 SOC Anisotropy ($r_\alpha$)
With fixed masses, the susceptibility dependence on SOC ratio is:

$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
$$

**Key Finding:** The Edelstein effect can be **boosted** by rendering the ratios $r_m$ and $r_\alpha$ greater than 1. For small ratios, the susceptibility increases linearly; for large $r_\alpha$, it tends to saturate.

## 4. Parameter Dependencies

### 4.1 Spin-Orbit Coupling Strength ($\alpha$)
*   **HDR:** $M_y \propto \alpha$.
*   **LDR:** $M_y \propto \sqrt{m^2 \alpha^2 + 2m E_F}$.
*   **Susceptibility:** $\chi_{xy}$ increases linearly with $\alpha$ for high chemical potentials (confirmed analytically and numerically).

### 4.2 Fermi Energy ($E_F$) and Velocity ($v_F$)
*   **HDR:** Magnetization is independent of $E_F$.
*   **LDR:** Magnetization increases with $E_F$.
*   **Fermi Velocity:** Implicitly contained in the group velocity $\mathbf{v}_\nu(\mathbf{k})$ used in the Boltzmann integral. In the anisotropic case, the Fermi velocity varies with direction, affecting the susceptibility.

### 4.3 Chirality (Helicity $\nu = \pm$)
*   The total magnetization arises from the imbalance between the two chiral bands ($\nu = +$ and $\nu = -$).
*   In the isotropic HDR, the contribution from the two bands leads to a constant term because the difference in Fermi wavevectors ($k_F^+ - k_F^-$) balances the velocity contributions.
*   In the LDR, only one band contributes significantly, leading to $E_F$ dependence.

## 5. Graphical Representations

The following figures from the source material describe the explicit dependencies for the model.

### 5.1 Edelstein Susceptibility vs. Chemical Potential
*   **Source:** Figure 2 (Left Panel) and Figure 3 (Left Panel) in Gaiardoni et al. (2025).
*   **Description:** Plots of $\chi_{xy}/\chi_0$ versus chemical potential $\mu$ (or $E_F$).
*   **Trends:**
    *   For $\alpha = 52 \text{ meV Å}$, the susceptibility shows a plateau in the HDR (high $\mu$).
    *   In the LDR (low $\mu$), the susceptibility rises from zero.
    *   Increasing $\alpha$ shifts the plateau to higher $\mu$ values and increases the plateau height.

### 5.2 Susceptibility vs. SOC Strength ($\alpha$)
*   **Source:** Figure 3 (Right Panel) in Gaiardoni et al. (2025).
*   **Description:** Plot of $\chi_{xy}/\chi_0$ versus $\alpha$ at a fixed chemical potential $\mu = 3.32 \times 10^{-2} \text{ eV}$.
*   **Trends:** The susceptibility increases **linearly** with $\alpha$. This confirms the analytical result $M_y \propto \alpha$ in the high-density regime.

### 5.3 Susceptibility vs. Anisotropy Ratios ($r_m, r_\alpha$)
*   **Source:** Figure 5 and Figure 6 in Gaiardoni et al. (2025).
*   **Description:**
    *   **Figure 5:** $\chi_{xy}/\chi_0$ vs. $\mu$ for different $r_m$ (left) and $r_\alpha$ (right).
    *   **Figure 6:** $\chi_{xy}/\chi_0$ vs. $r_m$ (left) and $r_\alpha$ (right) at fixed $\mu$.
*   **Trends:**
    *   When $r_m < 1$ or $r_\alpha < 1$, susceptibility is lower than the isotropic case ($r=1$).
    *   When $r_m > 1$ or $r_\alpha > 1$, susceptibility increases.
    *   The dependence on $r_\alpha$ shows linear growth for small ratios and saturation for very large ratios.
    *   The analytical curves (solid red lines) match the numerical points (dots) perfectly.

### 5.4 Fermi Surface and Spin Texture
*   **Source:** Figure 1 and Figure 4 in Gaiardoni et al. (2025).
*   **Description:**
    *   **Isotropic (Fig 1):** Two concentric circles in $k$-space. Spin vectors are tangential to the circles.
    *   **Anisotropic (Fig 4):** Distorted Fermi surfaces (elliptical or warped). Spin texture remains tangential to the local Fermi surface.
    *   **Effect of Field:** An applied field $\mathbf{E} \parallel \hat{x}$ shifts the Fermi surfaces, creating a net spin imbalance along $\hat{y}$.

## 6. Implementation Notes for the Model

To implement the model:
1.  **Define Parameters:** Set $m$, $\alpha$, $\tau$, $E_F$, and anisotropy ratios ($r_m, r_\alpha$) if applicable.
2.  **Calculate $k_F$:** Use the analytical expressions for $k_F^\pm$ provided in Eq. (5) and (6) of the source for HDR and LDR respectively.
3.  **Compute Magnetization:** Use Eq. (8) for HDR and Eq. (9) for LDR for the isotropic case. Use Eq. (12) for the anisotropic susceptibility.
4.  **Direction:** Always set $\mathbf{M} = M_y \hat{y}$ for $\mathbf{E} = E_x \hat{x}$, following $\mathbf{M} \propto \hat{z} \times \mathbf{E}$.
5.  **Validation:** Compare results against the graphical trends described in Section 5.

## 7. References

1.  **Gaiardoni, I., Trama, M., Maiellaro, A., Guarcello, C., Romeo, F., & Citro, R.** (2025). *Edelstein Effect in Isotropic and Anisotropic Rashba Models*. arXiv:2503.20712. [PDF](https://arxiv.org/pdf/2503.20712v1)
    *   *Primary source for analytical formulas (Eqs 1-12), regimes (HDR/LDR), and anisotropic dependencies.*
2.  **Leiva M., S., Henk, J., Mertig, I., & Johansson, A.** (2023). *Spin and Orbital Edelstein Effect in a Bilayer System with Rashba Interaction*. arXiv:2307.02872. [PDF](https://arxiv.org/pdf/2307.02872v2)
    *   *Provides context on current-induced spin polarization and orbital effects in Rashba systems.*
3.  **Ando, S., Tanaka, Y., Cuoco, M., Chirolli, L., & Mercaldo, M. T.** (2024). *Spin and Orbital Edelstein Effect in Spin-Orbit Coupled Noncentrosymmetric Superconductor*. arXiv:2408.08151. [PDF](https://arxiv.org/pdf/2408.08151v2)
    *   *Discusses fundamental insights into non-zero magnetization in systems without inversion symmetry.*
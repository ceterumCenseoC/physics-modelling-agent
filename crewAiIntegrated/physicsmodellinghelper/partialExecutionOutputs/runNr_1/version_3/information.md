

# Model for Calculating the Edelstein Effect in Rashba Fermions

This document provides the necessary theoretical framework, analytical expressions, and parameter dependencies required to calculate the Edelstein effect for a Rashba fermion at the Gamma point of the Brillouin zone. The information is extracted primarily from the study of the Direct Edelstein Effect (DEE) in isotropic and anisotropic Rashba models [1].

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian describing the system is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\hat{z}$ is the unit vector normal to the 2D plane.
*   $\vec{\sigma}$ is the vector of Pauli matrices.

In momentum space ($\vec{k}$), the eigenvalues (energy dispersion) for the two chiral bands ($\nu = \pm$) are:

$$
E_{\nu}(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k
$$

where $k = |\vec{k}|$ and $\nu = \pm 1$ corresponds to the inner and outer Fermi surfaces (chirality). The spin expectation value for an eigenstate with wavevector $\vec{k}$ is:

$$
\langle \vec{\sigma} \rangle_{\nu}^{\vec{k}} = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \nu \sin(\theta) \\ -\nu \cos(\theta) \\ 0 \end{pmatrix}
$$

where $\theta$ is the angle between $\vec{k}$ and the $\hat{x}$-axis. This indicates that the spin is locked tangential to the Fermi surface [1].

## 2. Calculation of Magnetization (Edelstein Effect)

The Direct Edelstein Effect (DEE) describes the generation of an in-plane magnetization $\vec{M}$ (or spin density) under an external electric field $\vec{E}$. Using the semiclassical Boltzmann approach, the expectation value of the magnetization at first order in the electric field is:

$$
\vec{M} = -\mu_b \sum_{\vec{k}, \nu} |e| (\vec{v}_{\nu}(\vec{k}) \cdot \vec{E}) \delta [E_{\nu}(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_{\nu}^{\vec{k}}
$$

where:
*   $\mu_b$ is the Bohr magneton.
*   $\vec{v}_{\nu}(\vec{k}) = \nabla_{\vec{k}} E_{\nu}(\vec{k})$ is the group velocity.
*   $E_F$ is the Fermi energy.
*   $\tau$ is the transport lifetime (assumed constant $\bar{\tau}_{\nu}^{\vec{k}} = \tau$ in the analytical derivation).

### 2.1 Analytical Results

The magnetization depends on the filling regime of the electronic bands.

#### High-Density Regime (HDR)
When both chiral bands are occupied ($E_F > 0$ relative to the band crossing), the magnetization component along the $\hat{y}$ direction (assuming $\vec{E} = E_x \hat{x}$) is:

$$
M_y = \mu_b |e| \frac{\tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y
$$

In vector form, this implies:
$$
\vec{M} = \mu_b |e| \frac{\tau m \alpha}{2\pi} (\hat{z} \times \vec{E})
$$
**Key Dependencies:**
*   **Electric Field ($E$):** Linear dependence ($M \propto E$).
*   **Spin-Orbit Coupling ($\alpha$):** Linear dependence ($M \propto \alpha$).
*   **Effective Mass ($m$):** Linear dependence ($M \propto m$).
*   **Fermi Energy ($E_F$):** Independent of $E_F$ (constant plateau).
*   **Direction:** The magnetization is perpendicular to the applied electric field (e.g., $E \parallel \hat{x} \implies M \parallel \hat{y}$).

#### Low-Density Regime (LDR)
When only the lowest energy band is occupied ($E_F < 0$ relative to the band crossing, or near the band minimum), the expression becomes:

$$
M_y = \mu_b |e| \frac{\tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y
$$

**Key Dependencies:**
*   **Fermi Energy ($E_F$):** The magnetization increases linearly with $E_F$ for small $E_F$ (expansion: $M_y \approx \text{const} + \frac{E_F}{2\alpha}$).
*   **Spin-Orbit Coupling ($\alpha$):** Non-linear dependence due to the square root term.

## 3. Edelstein Susceptibility

The linear Edelstein susceptibility $\chi_{ij}$ is defined by $M_j = \chi_{ij} E_i$. For the isotropic case with $\vec{E} = E_x \hat{x}$, the relevant component is $\chi_{xy}$.

*   **HDR:** $\chi_{xy}$ is constant and independent of the chemical potential $\mu$ (for $\mu > 0$).
*   **LDR:** $\chi_{xy}$ increases with the chemical potential.
*   **Dependence on $\alpha$:** In the HDR, $\chi_{xy}$ increases linearly with $\alpha$. In the LDR, it also increases but follows the square root behavior derived above [1].

## 4. Anisotropic Rashba Model

For systems with $C_{2v}$ symmetry (anisotropic effective mass and SOC), the Hamiltonian is modified to:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

Defining the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$, the Edelstein susceptibility in the HDR is given by:

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
$$
$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
$$

where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ is a normalization factor.
*   **Effect of Anisotropy:** If $r_m > 1$ or $r_\alpha > 1$, the susceptibility increases compared to the isotropic case. If $r_m, r_\alpha < 1$, it decreases [1].

## 5. Expected Graphics and Results

To visualize the model results, the following plots should be generated based on the analytical expressions:

1.  **Edelstein Susceptibility vs. Chemical Potential ($\mu$):**
    *   **Shape:** A plateau for $\mu > 0$ (HDR) and a rising curve for $\mu < 0$ (LDR).
    *   **Parameter:** Plot for different $\alpha$ values. Higher $\alpha$ shifts the plateau to higher values and increases the slope in the LDR.
    *   **Reference:** Figure 2 (Left panel) in [1].

2.  **Edelstein Susceptibility vs. SOC Strength ($\alpha$):**
    *   **Shape:** Linear increase for fixed $\mu$ (especially in HDR).
    *   **Parameter:** Plot for fixed chemical potential (e.g., $\mu = 3.32 \times 10^{-2}$ eV).
    *   **Reference:** Figure 3 (Right panel) in [1].

3.  **Magnetization Direction:**
    *   **Visualization:** Fermi surface shift. An electric field $\vec{E} = E_x \hat{x}$ shifts the Fermi circles in the $-\hat{x}$ direction. Due to spin-momentum locking, this results in a net spin polarization along $\hat{y}$.
    *   **Reference:** Figure 1 in [1].

4.  **Anisotropy Dependence:**
    *   **Shape:** Susceptibility increases with $r_m$ and $r_\alpha$, saturating for large ratios.
    *   **Reference:** Figure 6 in [1].

## 6. Scientific Citations

The information provided is based on the following sources:

1.  **Gaia et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models"**, *arXiv:2503.20712v1 [cond-mat.mes-hall]* (2025).
    *   *Provides the Hamiltonian (Eq. 1), Boltzmann derivation (Eq. 2), and analytical results for HDR (Eq. 8) and LDR (Eq. 9).*
2.  **Edelstein, V. M., "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems"**, *Solid State Communications* **73**, 233 (1990).
    *   *Original proposal of the Edelstein effect (cited as Ref [29] in source 1).*
3.  **Bychkov, Y. A., and Rashba, E. I., "Properties of a 2D electron gas with lifted spectral degeneracy"**, *JETP Lett.* **39**, 78 (1984).
    *   *Foundational work on the Rashba model (cited as Ref [13-15] in source 1).*
4.  **Gaia et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models"**, *arXiv:2503.20712v1* (2025).
    *   *Provides the anisotropic formulas (Eq. 12) and numerical validation (Figs 5, 6).*

## 7. Implementation Notes for the Model

*   **Parameters:**
    *   $\tau$: Typical transport time in oxides is $\sim 10^{-12}$ s [1].
    *   $\alpha$: Typical values range from $0.093$ eVÅ to $52$ meVÅ depending on the material (e.g., InGaAs vs. oxide interfaces) [1].
    *   $m$: Effective mass (e.g., $0.152$ eV$^{-1}$Å$^{-2}$ for specific oxide interfaces) [1].
*   **Units:** Ensure consistency (e.g., SI or atomic units) when calculating $M$ and $\chi$.
*   **Regime Check:** Determine if the system is in HDR or LDR based on the Fermi energy relative to the band crossing point ($E_{min} = -m\alpha^2/2\hbar^2$).
*   **Anisotropy:** If modeling real materials like oxide interfaces, consider using the anisotropic formulas (Eq. 12) to account for effective mass and SOC anisotropy ($r_m, r_\alpha$).

---
**References**
[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712v1* (2025).
[2] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233 (1990).
[3] Y. A. Bychkov and E. I. Rashba, "Properties of a 2D electron gas with lifted spectral degeneracy," *JETP Lett.* **39**, 78 (1984).
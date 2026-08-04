

# Mathematical Model for the Edelstein Effect in Rashba Fermions

## 1. Introduction and Model Overview

This model calculates the Direct Edelstein Effect (DEE) in a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The goal is to determine the induced magnetization $\vec{M}$ resulting from an applied electric field $\vec{E}$ at the Gamma point of the Brillouin zone. The model derives analytical expressions for magnetization magnitude and direction, analyzing dependencies on spin-orbit coupling strength ($\alpha$), effective mass ($m$), Fermi energy ($E_F$), and electric field parameters.

The following steps outline the mathematical construction of the model, derived from established semiclassical transport theory and the Rashba Hamiltonian [1].

## 2. Step 1: Define the System Hamiltonian

The physical system is defined by the isotropic Rashba Hamiltonian. This describes the kinetic energy of the carriers and the spin-orbit interaction arising from structural inversion asymmetry.

The Hamiltonian operator $\hat{H}$ is given by:

$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma}) \quad (1) $$

Where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ represents the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

**Explanation:** This step establishes the energy landscape of the fermions. The second term couples the electron's spin to its momentum, leading to spin-splitting of the energy bands.

## 3. Step 2: Determine Band Structure and Spin Texture

To calculate transport properties, we must first solve for the eigenstates of the Hamiltonian. The energy dispersion relation for the two chiral bands (helicity $\nu = \pm$) is derived as:

$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k \quad (2) $$

Where $k = |\vec{k}|$ is the magnitude of the wave vector. The spin expectation value for these eigenstates, which dictates the local spin polarization, is:

$$ \langle \vec{\sigma} \rangle_k^\nu = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \nu \sin\theta \\ -\nu \cos\theta \\ 0 \end{pmatrix} \quad (3) $$

Where $\theta$ is the angle between the vector $\vec{k}$ and the $\hat{x}$ axis.

**Explanation:** This step identifies the available states for conduction. The spin texture (Eq. 3) shows that spins are locked perpendicular to the momentum in the plane, a prerequisite for the Edelstein effect where a current (momentum shift) induces a net spin polarization.

## 4. Step 3: Apply Semiclassical Transport Theory

The Edelstein effect is modeled using the semiclassical Boltzmann framework. The external electric field $\vec{E}$ shifts the distribution function of the electrons, leading to a non-equilibrium spin density. The expectation value of the magnetization $\vec{M}$ at first order in the electric field is:

$$ \vec{M} = -\mu_b \sum_{k, \nu} |e| (\vec{v}_\nu(k) \cdot \vec{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_k^\nu \quad (4) $$

Where:
*   $\mu_b$ is the Bohr magneton.
*   $\vec{v}_\nu(k) = \nabla_k E_\nu(k)$ is the group velocity.
*   $\tau_\nu^k$ is the transport lifetime (assumed constant $\tau$ for the isotropic model).
*   $E_F$ is the Fermi energy.

**Explanation:** This step links the applied field to the observable magnetization. The term $(\vec{v}_\nu(k) \cdot \vec{E})$ represents the perturbation to the distribution, and the delta function restricts the calculation to states at the Fermi surface.

## 5. Step 4: Solve for Magnetization in Different Regimes

The solution to Eq. (4) depends on whether the Fermi energy lies above or below the band crossing point (the minimum of the lower band).

### 5.1 High-Density Regime (HDR)
When both chiral bands are occupied ($E_F$ above the band crossing), the integration yields a linear response. For an electric field $\vec{E} = E_x \hat{x}$, the spin density along $\hat{y}$ is:

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y \quad (5) $$

In vector form, the magnetization is:
$$ \vec{M}_{HDR} = \frac{\mu_b |e| \tau m \alpha}{2\pi} (\hat{z} \times \vec{E}) \quad (6) $$

### 5.2 Low-Density Regime (LDR)
When only the lowest energy band is occupied, the result differs due to the lack of compensation from the upper band:

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y \quad (7) $$

For small $E_F$, this expands to:
$$ M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) [\hat{z} \times \vec{E}]_y \quad (8) $$

**Explanation:** This step provides the explicit analytical solutions. Eq. (6) shows that in the HDR, the effect is independent of $E_F$ and linear in $\alpha$. Eq. (7) shows a more complex dependence in the LDR, sensitive to the Fermi energy.

## 6. Step 5: Analyze Parameter Dependencies

The model explicitly defines how the magnetization magnitude and direction depend on system parameters.

### 6.1 Magnitude of Magnetization
The magnitude $|\vec{M}|$ for an electric field of magnitude $E$ is:
*   **Isotropic HDR:** $|\vec{M}| = \frac{\mu_b |e| \tau m \alpha}{2\pi} E$
*   **Isotropic LDR:** $|\vec{M}| = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E$

### 6.2 Direction of Magnetization
The direction is strictly determined by the cross product of the surface normal and the electric field:
$$ \hat{M} = \frac{\hat{z} \times \vec{E}}{|\hat{z} \times \vec{E}|} $$
For $\vec{E} = E_x \hat{x}$, the magnetization is along $\hat{y}$ ($\vec{M} = M_y \hat{y}$).

### 6.3 Anisotropy Effects
For systems with anisotropy (e.g., $m_x \neq m_y$ or $\alpha_x \neq \alpha_y$), the susceptibility $\chi_{xy}$ depends on ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$. In the HDR:
$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} \quad (9) $$
$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} \quad (10) $$

**Explanation:** This step clarifies the sensitivity of the model. The direction is always perpendicular to $\vec{E}$ in the plane. The magnitude scales linearly with $\alpha$ in the HDR but can be boosted by anisotropy ratios $>1$.

## 7. Step 6: Explicit Graphics Specifications

To visualize the model results, the following graphics are defined based on the derived equations.

### Graphic 1: Magnetization vs. Electric Field Magnitude
*   **X-axis:** Electric field magnitude $E$ (V/m).
*   **Y-axis:** Magnetization magnitude $M$ (A/m or $\mu_B$).
*   **Expected Behavior:** A linear relationship passing through the origin.
*   **Equation:** $M(E) = \chi E$, utilizing Eq. (6) or Eq. (7).
*   **Parameter Variation:** Multiple lines for different $\alpha$ values will show steeper slopes for higher $\alpha$.

### Graphic 2: Edelstein Susceptibility vs. Spin-Orbit Coupling ($\alpha$)
*   **X-axis:** Rashba parameter $\alpha$ (eV·Å).
*   **Y-axis:** Normalized susceptibility $\chi_{xy}/\chi_0$.
*   **Expected Behavior:** Linear increase with $\alpha$ in the HDR (Eq. 6). In the LDR, the dependence is sub-linear ($\sqrt{A + B\alpha^2}$).
*   **Source Data:** Matches Figure 3 (right panel) in Source 1.

### Graphic 3: Magnetization vs. Fermi Energy ($E_F$)
*   **X-axis:** Chemical potential $\mu$ or Fermi energy $E_F$ (eV).
*   **Y-axis:** Edelstein susceptibility or Magnetization.
*   **Expected Behavior:**
    *   **HDR:** Constant plateau (independent of $E_F$).
    *   **LDR:** Increases linearly for small $E_F$ (Eq. 8) and follows the square root behavior (Eq. 7) for higher $E_F$.
*   **Source Data:** Matches Figure 2 (left panel) in Source 1.

### Graphic 4: Anisotropy Dependence
*   **X-axis:** Anisotropy ratio $r_m = m_y/m_x$ or $r_\alpha = \alpha_y/\alpha_x$.
*   **Y-axis:** Normalized susceptibility $\chi_{xy}/\chi_0$.
*   **Expected Behavior:**
    *   For $r < 1$, susceptibility is lower than isotropic case.
    *   For $r > 1$, susceptibility increases.
    *   Saturation occurs for very large $r_\alpha$ (Eq. 10).
*   **Source Data:** Matches Figure 6 in Source 1.

## 8. Conclusion

The model successfully calculates the Edelstein effect for Rashba fermions. It demonstrates that the induced magnetization is linearly proportional to the applied electric field and perpendicular to it in the plane. The magnitude is tunable via the spin-orbit coupling strength $\alpha$ and the carrier density ($E_F$), with distinct behaviors in the High-Density and Low-Density regimes. Anisotropy in mass or coupling parameters can further enhance the effect.

## 9. Scientific Citations

1.  **Gaiardoni, I., et al.** "Edelstein Effect in Isotropic and Anisotropic Rashba Models." *arXiv:2503.20712* (2025). [Source 1 in PDF Reader]
2.  **Zulkoskey, A. C., Dick, R., & Tanaka, K.** "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface." *arXiv:1912.01804* (2019). [Source 3 in PDF Reader]
3.  **Leiva M., S., et al.** "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction." *arXiv:2307.02872* (2024). [Source 6 in PDF Reader]
4.  **Edelstein, V. M.** "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems." *Solid State Communications* 73, 233 (1990). [Original Reference cited in Source 1]
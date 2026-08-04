

# Edelstein Effect in Rashba Fermions: Analytical Model and Parameter Dependence

## 1. Model Hamiltonian and Band Structure

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian for the isotropic Rashba model is given by [1]:

$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma}) \quad (1) $$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

The energy dispersion relation for the two chiral bands (helicity $\nu = \pm$) is [1, 3]:

$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k \quad (2) $$

where $k = |\vec{k}|$ is the magnitude of the wave vector. The spin expectation value for the eigenstates is [1]:

$$ \langle \vec{\sigma} \rangle_k^\nu = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \nu \sin\theta \\ -\nu \cos\theta \\ 0 \end{pmatrix} \quad (3) $$

where $\theta$ is the angle between the vector $\vec{k}$ and the $\hat{x}$ axis.

## 2. Calculation of the Edelstein Effect

The Direct Edelstein Effect (DEE) describes the generation of an in-plane magnetization $\vec{M}$ under an external electric field $\vec{E}$. Within the semiclassical Boltzmann framework, the expectation value of the magnetization at first order in the electric field is [1]:

$$ \vec{M} = -\mu_b \sum_{k, \nu} |e| (\vec{v}_\nu(k) \cdot \vec{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_k^\nu \quad (4) $$

where:
*   $\mu_b$ is the Bohr magneton.
*   $\vec{v}_\nu(k) = \nabla_k E_\nu(k)$ is the group velocity.
*   $\tau_\nu^k$ is the transport lifetime (often assumed constant $\tau$).
*   $E_F$ is the Fermi energy.

### 2.1 Isotropic Rashba Model

#### High-Density Regime (HDR)
When both chiral bands are occupied ($E_F$ above the band crossing), the spin density along the $\hat{y}$ direction (for an electric field $\vec{E} = E_x \hat{x}$) is given by [1]:

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y \quad (5) $$

In vector form, the magnetization is:
$$ \vec{M}_{HDR} = \frac{\mu_b |e| \tau m \alpha}{2\pi} (\hat{z} \times \vec{E}) \quad (6) $$

**Key Dependencies:**
*   **Electric Field:** Linear dependence ($\vec{M} \propto \vec{E}$).
*   **Spin-Orbit Coupling ($\alpha$):** Linear dependence ($\vec{M} \propto \alpha$).
*   **Effective Mass ($m$):** Linear dependence ($\vec{M} \propto m$).
*   **Fermi Energy ($E_F$):** Independent of $E_F$ in the high-density limit.
*   **Direction:** The magnetization is perpendicular to the electric field and lies in the plane ($\vec{M} \perp \vec{E}$ and $\vec{M} \perp \hat{z}$).

#### Low-Density Regime (LDR)
When only the lowest energy band is occupied, the spin density is [1]:

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y \quad (7) $$

**Key Dependencies:**
*   **Electric Field:** Linear dependence.
*   **Spin-Orbit Coupling ($\alpha$):** Non-linear dependence ($\propto \sqrt{m^2 \alpha^2 + \dots}$).
*   **Fermi Energy ($E_F$):** Dependence on $\sqrt{E_F}$ for small $E_F$.
*   **Expansion for small $E_F$:**
    $$ M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) [\hat{z} \times \vec{E}]_y \quad (8) $$

### 2.2 Anisotropic Rashba Model (C2v Symmetry)

For systems with anisotropy in effective masses ($m_x \neq m_y$) or Rashba parameters ($\alpha_x \neq \alpha_y$), the Edelstein susceptibility $\chi_{xy}$ depends on the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$ [1].

In the High-Density Regime, the susceptibility normalized by a reference value $\chi_0$ is [1]:

$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} \quad (9) $$

$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} \quad (10) $$

where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ [1].

**Key Dependencies:**
*   **Anisotropy:** The susceptibility increases as the ratios $r_m$ and $r_\alpha$ exceed 1.
*   **Boosting Effect:** Anisotropy can be used to boost the Edelstein response compared to the isotropic model.

## 3. Magnitude and Direction of Magnetization

### 3.1 Magnitude
The magnitude of the magnetization $|\vec{M}|$ for an electric field of magnitude $E$ is:

*   **Isotropic HDR:** $|\vec{M}| = \frac{\mu_b |e| \tau m \alpha}{2\pi} E$
*   **Isotropic LDR:** $|\vec{M}| = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E$

### 3.2 Direction
The direction of the induced magnetization is determined by the cross product of the surface normal $\hat{z}$ and the electric field $\vec{E}$:
$$ \hat{M} = \frac{\hat{z} \times \vec{E}}{|\hat{z} \times \vec{E}|} $$
For an electric field applied along the $\hat{x}$ direction ($\vec{E} = E_x \hat{x}$), the magnetization is along the $\hat{y}$ direction ($\vec{M} = M_y \hat{y}$).

## 4. Explicit Graphics and Dependencies

To visualize the results, the following explicit graphics can be generated using the derived analytical expressions:

### Graphic 1: Magnetization vs. Electric Field Magnitude
*   **X-axis:** Electric field magnitude $E$ (V/m).
*   **Y-axis:** Magnetization magnitude $M$ (A/m or $\mu_B$).
*   **Expected Behavior:** A linear relationship passing through the origin.
*   **Equation:** $M(E) = \chi E$, where $\chi$ is the susceptibility from Eq. (6) or (7).
*   **Parameter Variation:** Plotting multiple lines for different $\alpha$ values will show steeper slopes for higher $\alpha$.

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

## 5. Scientific Citations

1.  **Gaiardoni, I., et al.** "Edelstein Effect in Isotropic and Anisotropic Rashba Models." *arXiv:2503.20712* (2025). [Source 1 in PDF Reader]
2.  **Zulkoskey, A. C., Dick, R., & Tanaka, K.** "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface." *arXiv:1912.01804* (2019). [Source 3 in PDF Reader]
3.  **Leiva M., S., et al.** "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction." *arXiv:2307.02872* (2024). [Source 6 in PDF Reader]
4.  **Edelstein, V. M.** "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems." *Solid State Communications* 73, 233 (1990). [Original Reference cited in Source 1]
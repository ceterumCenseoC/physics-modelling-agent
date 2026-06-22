

# Model for Calculating the Edelstein Effect in Rashba Fermions

## 1. Theoretical Framework and Hamiltonian

The Edelstein effect (EE) describes the generation of a non-equilibrium spin polarization (magnetization) in a system with spin-orbit coupling (SOC) and broken inversion symmetry when an external electric field is applied. For a 2D Rashba electron gas, the Hamiltonian at the Gamma point ($\Gamma$) of the Brillouin zone is given by [1]:

$$ \hat{H} = \frac{\mathbf{p}^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \vec{\sigma}) $$
$$ \hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha (\sigma_x k_y - \sigma_y k_x) $$

where:
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\mathbf{p} = \hbar \mathbf{k}$ is the momentum operator.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

The energy dispersion relation for the two helicity bands ($\nu = \pm 1$) is:
$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k $$
where $\nu = +1$ corresponds to the outer Fermi surface and $\nu = -1$ to the inner Fermi surface.

## 2. Magnetization Calculation

The total spin density (magnetization) $\mathbf{M}$ induced by an electric field $\mathbf{E}$ is calculated using the semiclassical Boltzmann approach. The expectation value of the magnetization at first order in the electric field is [1]:

$$ \mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| (\vec{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta [E_\nu(\mathbf{k}) - E_F] \langle \vec{\sigma} \rangle_\nu^{\mathbf{k}} $$

where:
*   $\mu_b$ is the Bohr magneton.
*   $e$ is the elementary charge.
*   $\vec{v}_\nu(\mathbf{k}) = \frac{1}{\hbar} \nabla_{\mathbf{k}} E_\nu(\mathbf{k})$ is the group velocity.
*   $\langle \vec{\sigma} \rangle_\nu^{\mathbf{k}}$ is the spin expectation value for eigenstates, given by:
    $$ \langle \vec{\sigma} \rangle_\pm^{\mathbf{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix} $$
    where $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$ axis.

### 2.1 Isotropic Rashba Model
For an electric field applied along the $\hat{x}$ direction ($\mathbf{E} = E_x \hat{x}$), the induced magnetization is perpendicular to the field and lies in the plane (along $\hat{y}$). The magnitude $M_y$ depends on the electronic density regime [1]:

**High-Density Regime (HDR):** Both chiral bands are occupied ($E_F > 0$).
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x $$
In this regime, the spin density is constant and independent of the Fermi energy $E_F$.

**Low-Density Regime (LDR):** Only the lowest energy band is occupied ($E_F < 0$, but $E_F > E_{min} = -m\alpha^2/2$).
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x $$
For small $E_F$ near the band crossing:
$$ M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) E_x $$

### 2.2 Anisotropic Rashba Model
For systems with $C_{2v}$ symmetry, the Hamiltonian includes anisotropic effective masses ($m_x, m_y$) and Rashba parameters ($\alpha_x, \alpha_y$) [1]:
$$ \hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \sigma_x - \alpha_x k_x \sigma_y $$

Defining the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$, the Edelstein susceptibility $\chi_{xy}$ (where $M_y = \chi_{xy} E_x$) in the HDR is [1]:
$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} $$
$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} $$
where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ is a normalization factor ($S_{cell}$ is the unit cell area, $a$ is the lattice parameter).

## 3. Dependencies on Model Parameters

*   **Electric Field Magnitude ($E$):** The magnetization $M$ is linearly proportional to the applied electric field $E$ in the linear response regime ($M \propto E$).
*   **Electric Field Direction:** The magnetization direction is always perpendicular to the electric field and in-plane, following the cross product $\mathbf{M} \propto \hat{z} \times \mathbf{E}$. If $\mathbf{E} = E_x \hat{x} + E_y \hat{y}$, then $\mathbf{M} \propto (-E_y, E_x, 0)$.
*   **Spin-Orbit Coupling Strength ($\alpha$):**
    *   In HDR, $M \propto \alpha$.
    *   In LDR, $M$ increases with $\alpha$ but saturates for very large $\alpha$ relative to $E_F$.
    *   Susceptibility $\chi_{xy}$ increases linearly with $\alpha$ for high chemical potentials [1].
*   **Effective Mass ($m$):** $M \propto m$ in HDR. Anisotropy in mass ($r_m$) enhances the effect if $r_m > 1$ [1].
*   **Chirality (Helicity $\nu$):** The effect arises from the imbalance of population between the two helicity bands ($\nu = \pm$) caused by the shift of Fermi surfaces. The net magnetization is the sum of contributions from both bands, which do not cancel due to the different Fermi wavevectors $k_F^\pm$ [1].
*   **Fermi Velocity ($v_F$):** Implicitly contained in the density of states and group velocity terms. In the isotropic model, $v_F$ determines the Fermi wavevectors $k_F^\pm$.
*   **Scattering Time ($\tau$):** $M \propto \tau$. The effect is stronger in cleaner systems with longer transport times.

## 4. Explicit Graphics and Visualization

To visualize the results, the following plots should be generated based on the analytical expressions and numerical data provided in the source [1]:

### Figure 1: Edelstein Susceptibility vs. Chemical Potential
*   **X-axis:** Chemical potential $\mu$ (or $E_F$).
*   **Y-axis:** Normalized Edelstein susceptibility $\chi_{xy}/\chi_0$.
*   **Description:** The susceptibility shows a plateau in the High-Density Regime (constant value) and a linear increase in the Low-Density Regime (near the band crossing).
*   **Data Source:** Figure 2 (Left panel) in [1].

### Figure 2: Susceptibility vs. Rashba Parameter
*   **X-axis:** Rashba coupling strength $\alpha$.
*   **Y-axis:** Normalized Edelstein susceptibility $\chi_{xy}/\chi_0$.
*   **Description:** A linear increase of susceptibility with $\alpha$ at fixed chemical potential.
*   **Data Source:** Figure 3 (Right panel) in [1].

### Figure 3: Anisotropy Dependence
*   **X-axis:** Mass ratio $r_m$ or SOC ratio $r_\alpha$.
*   **Y-axis:** Normalized susceptibility $\chi_{xy}/\chi_0$.
*   **Description:** The susceptibility increases as the anisotropy ratios exceed 1. The analytical curves (solid lines) match numerical points.
*   **Data Source:** Figure 6 in [1].

### Figure 4: Spin Texture and Fermi Surfaces
*   **Description:** Plot the Fermi surfaces (circles for isotropic, distorted for anisotropic) with arrows indicating spin direction.
    *   **Isotropic:** Two concentric circles. Inner circle ($\nu=-1$) has clockwise spin texture; outer circle ($\nu=+1$) has counter-clockwise texture.
    *   **With Field:** Fermi surfaces shift opposite to $\mathbf{E}$, creating a net spin imbalance perpendicular to $\mathbf{E}$.
*   **Data Source:** Figure 1 and Figure 2 (Right panel) in [1].

## 5. Implementation Notes for Model

To implement this model computationally:
1.  **Define Parameters:** Set $m$, $\alpha$, $\tau$, $\mu_b$, and $E_F$.
2.  **Calculate Fermi Wavevectors:**
    *   $k_0 = m\alpha / \hbar^2$ (using $\hbar=1$ for simplicity in code or keeping units consistent).
    *   $k_F^\pm = \mp k_0 + \sqrt{k_0^2 + 2m E_F / \hbar^2}$ (HDR).
3.  **Compute Magnetization:** Use the analytical formulas for $M_y$ based on the regime (HDR or LDR).
4.  **Direction:** Apply the cross product rule $\mathbf{M} = \chi (\hat{z} \times \mathbf{E})$.
5.  **Anisotropy:** If $m_x \neq m_y$ or $\alpha_x \neq \alpha_y$, use the anisotropic susceptibility formulas or perform numerical integration over the Brillouin zone using the anisotropic Hamiltonian.

## References

[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712* (2025). (Specifically Sections "DEE: Analytical and Numerical Calculation of Spin Density" and "DEE in Anisotropic Case").
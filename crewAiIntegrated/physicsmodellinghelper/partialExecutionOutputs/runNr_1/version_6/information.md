

# Model for the Edelstein Effect in a Rashba Fermion System

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin–orbit coupling (RSOC). The Hamiltonian at the Gamma point of the Brillouin zone is given by [1]:

$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma}) $$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin–orbit coupling strength.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.

The energy dispersion relation for the two chiral bands ($\nu = \pm$) is:
$$ E_\nu(\vec{k}) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k $$
where $k = |\vec{k}|$ and $\nu = +1$ (outer band) and $\nu = -1$ (inner band) correspond to the two helicity states.

## 2. Calculation of Magnetization (Edelstein Effect)

The Direct Edelstein Effect (DEE) describes the generation of an in-plane magnetization $\vec{M}$ (spin density) under an external electric field $\vec{E}$. Within the semiclassical Boltzmann approach, the magnetization at first order in the electric field is [1]:

$$ \vec{M} = -\mu_b \sum_{\vec{k}, \nu} |e| (\vec{\nu}_\nu(\vec{k}) \cdot \vec{E}) \delta [E_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_\nu^{\vec{k}} $$

where:
*   $\mu_b$ is the Bohr magneton.
*   $e$ is the elementary charge.
*   $\vec{\nu}_\nu(\vec{k}) = \bar{\tau}_\nu^k \vec{v}_\nu(\vec{k})$ is the mean free path, with $\bar{\tau}_\nu^k$ being the transport lifetime and $\vec{v}_\nu(\vec{k}) = \nabla_k E_\nu(\vec{k})$ the group velocity.
*   $\langle \vec{\sigma} \rangle_\nu^{\vec{k}}$ is the spin expectation value on the eigenstates.

The spin expectation value for the Rashba eigenstates is [1]:
$$ \langle \vec{\sigma} \rangle_\pm^{\vec{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix} $$
where $\theta$ is the angle between the wave vector $\vec{k}$ and the $\hat{x}$ axis.

## 3. Magnetization Magnitude and Direction

### 3.1 Direction
For an electric field applied along the $\hat{x}$ direction ($\vec{E} = E_x \hat{x}$), the resulting magnetization is perpendicular to the electric field and lies in the plane of the 2DEG. Specifically, the magnetization is along the $\hat{y}$ direction:
$$ \vec{M} = M_y \hat{y} $$
This is a consequence of the spin–momentum locking, where a shift of the Fermi surfaces along $\hat{x}$ results in a spin imbalance along the orthogonal $\hat{y}$ direction [1].

### 3.2 Magnitude in Different Regimes

The magnitude of the magnetization depends on the Fermi energy $E_F$ relative to the band crossing point.

**High-Density Regime (HDR):**
When both chiral bands are occupied ($E_F > 0$), the spin density along $\hat{y}$ is [1]:
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x $$
Assuming a constant transport time $\tau_+ = \tau_- = \tau$. In this regime, the magnetization is **constant and independent of the Fermi energy** $E_F$.

**Low-Density Regime (LDR):**
When only the lowest energy band is occupied ($E_F < 0$, measured from the band crossing), the spin density is [1]:
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x $$
For values of the Fermi energy around the band crossing (small $E_F$), this can be expanded as [1]:
$$ M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) E_x $$
In this regime, the spin density **increases linearly with the Fermi energy**.

### 3.3 Edelstein Susceptibility
The linear Edelstein susceptibility $\chi_{ij}$ is defined by $M_j = \chi_{ij} E_i$. For the isotropic case with $\vec{E} = E_x \hat{x}$, the susceptibility $\chi_{xy}$ is [1]:
$$ \chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle_\nu^{\vec{k}} \delta(E_\nu^{\vec{k}} - \mu) v_x^\nu(\vec{k}) $$
where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$, with $S_{cell}$ being the unit cell area and $a$ the lattice parameter.

## 4. Dependence on Model Parameters

The magnetization and susceptibility depend on the following parameters:

*   **Rashba Spin-Orbit Coupling Strength ($\alpha$):**
    *   In the HDR, $M_y \propto \alpha$.
    *   In the LDR, $M_y \propto \sqrt{m^2 \alpha^2 + 2m E_F}$.
    *   The susceptibility $\chi_{xy}$ increases linearly with $\alpha$ for high chemical potential [1].
*   **Effective Mass ($m$):**
    *   In the HDR, $M_y \propto m$.
    *   The susceptibility is proportional to the effective mass.
*   **Fermi Energy ($E_F$) / Chemical Potential ($\mu$):**
    *   **HDR:** Independent of $E_F$.
    *   **LDR:** Increases with $\sqrt{E_F}$ (or linearly for small $E_F$).
    *   The transition between regimes occurs at the band crossing point ($E_F = 0$).
*   **Chirality ($\nu = \pm$):**
    *   The two chiral bands ($\nu = +$ and $\nu = -$) have opposite spin textures.
    *   The net magnetization arises because the Fermi momenta for the two bands ($k_F^+$ and $k_F^-$) are different, preventing complete cancellation of the spin contributions [1].
    *   Fermi momenta in HDR:
        $$ k_F^\pm = \mp k_0 + \sqrt{k_0^2 + \frac{2m E_F}{\hbar^2}} $$
        where $k_0 = \frac{m \alpha}{\hbar^2}$.
*   **Transport Time ($\tau$):**
    *   $M_y \propto \tau$. The magnitude scales linearly with the transport lifetime.

## 5. Anisotropic Rashba Model

For systems with $C_{2v}$ symmetry, the effective mass and Rashba parameter can be anisotropic. The Hamiltonian becomes [1]:
$$ \hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y $$

Defining the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$, the Edelstein susceptibility in the High-Density Regime is given by [1]:

$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} $$
$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} $$

*   **Effect of Anisotropy:** The susceptibility increases as $r_m$ and $r_\alpha$ increase (i.e., when $m_y > m_x$ or $\alpha_y > \alpha_x$). This allows for boosting the Edelstein response compared to the isotropic case [1].
*   **Graphics:** Numerical analysis shows that for $r_m, r_\alpha < 1$, the susceptibility is lower than the isotropic case, while for $r_m, r_\alpha > 1$, it increases. The dependence on $r_\alpha$ tends to saturate for large values [1].

## 6. Expected Graphical Representations

Based on the analytical and numerical results, the following graphics should be generated:

1.  **Edelstein Susceptibility vs. Chemical Potential ($\mu$):**
    *   Plot $\chi_{xy}/\chi_0$ against $\mu$.
    *   Show a plateau in the HDR (constant value) and a rising curve in the LDR (increasing with $\mu$) [1, Fig. 2].
    *   Plot for different values of $\alpha$ showing that higher $\alpha$ shifts the plateau to higher $\mu$ and increases the magnitude [1, Fig. 3].

2.  **Edelstein Susceptibility vs. Rashba Parameter ($\alpha$):**
    *   Plot $\chi_{xy}/\chi_0$ against $\alpha$ at a fixed $\mu$.
    *   Show a linear increase for high $\mu$ [1, Fig. 3].

3.  **Edelstein Susceptibility vs. Anisotropy Ratios ($r_m, r_\alpha$):**
    *   Plot $\chi_{xy}/\chi_0$ against $r_m$ and $r_\alpha$.
    *   Show that susceptibility increases with both ratios, with a linear trend for small ratios and saturation for large $r_\alpha$ [1, Fig. 6].

4.  **Fermi Surface and Spin Structure:**
    *   Plot the Fermi surfaces (inner and outer circles) in the $k_x$-$k_y$ plane.
    *   Indicate the spin texture (tangential to the Fermi surface, winding clockwise/counter-clockwise) [1, Fig. 1, Fig. 2].
    *   Show the shift of Fermi surfaces under an applied electric field $\vec{E} = E_x \hat{x}$, resulting in a net spin polarization along $\hat{y}$ [1, Fig. 1].

## 7. References

[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv preprint arXiv:2503.20712* (2025).
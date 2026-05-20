

# Model Parameters and Equations for Calculating the Edelstein Effect in a Rashba Fermion System

## 1. System Hamiltonian and Band Structure
The model is based on a 2D electron gas with Rashba spin-orbit coupling (RSOC). The Hamiltonian for the isotropic case at the Gamma point is defined as:

$$ \hat{H} = \frac{\mathbf{p}^2}{2m} + \alpha_R \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}) $$

*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (1), Page 1.
*   **Variables:**
    *   $\mathbf{p} = (p_x, p_y)$: Momentum operator.
    *   $m$: Effective carrier mass.
    *   $\alpha_R$: Rashba coupling constant (strength of spin-orbit interaction).
    *   $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$: Vector of Pauli matrices.
    *   $\hat{z}$: Unit vector normal to the 2D plane.

The eigenenergies for the two chiral bands ($\nu = \pm$) are:
$$ E_{\nu}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} + \nu \alpha_R \hbar k $$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, implied in Eq. (5) and discussion on Page 2.
*   **Chirality ($\nu$):** $\nu = +1$ (outer band) and $\nu = -1$ (inner band).

The Fermi momenta for the two bands in the High-Density Regime (HDR), where both bands are occupied ($E_F > 0$), are:
$$ k_{F}^{\pm} = \mp k_0 + \sqrt{k_0^2 + \frac{2m E_F}{\hbar^2}} $$
where $k_0 = \frac{m \alpha_R}{\hbar^2}$.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (5), Page 2.

## 2. Spin Expectation Value (Spin Texture)
The spin expectation value for an eigenstate with wavevector $\mathbf{k}$ is tangential to the Fermi surface. In polar coordinates ($k, \theta$):

$$ \langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^{\pm} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix} $$

*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (3), Page 2.
*   **Note:** The spin lies in the $xy$-plane and is perpendicular to the momentum vector $\mathbf{k}$.

## 3. Magnetization (Spin Density) Calculation
The magnetization $\mathbf{M}$ (or total spin density) induced by an external electric field $\mathbf{E}$ is calculated using the semiclassical Boltzmann approach.

### General Formula
$$ \mathbf{M} = -\mu_B \sum_{\mathbf{k}, \nu} |e| (\mathbf{v}_{\nu}(\mathbf{k}) \cdot \mathbf{E}) \delta [E_{\nu}(\mathbf{k}) - E_F] \langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^{\nu} \bar{\tau}_{\mathbf{k}}^{\nu} $$

*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (2), Page 2.
*   **Variables:**
    *   $\mu_B$: Bohr magneton.
    *   $e$: Elementary charge (absolute value).
    *   $\mathbf{v}_{\nu}(\mathbf{k}) = \nabla_{\mathbf{k}} E_{\nu}(\mathbf{k}) / \hbar$: Group velocity.
    *   $\bar{\tau}_{\mathbf{k}}^{\nu}$: Transport lifetime (relaxation time).
    *   $\delta$: Dirac delta function selecting states at the Fermi energy.

### Analytical Results for Isotropic Case
Assuming a constant relaxation time $\tau$ ($\bar{\tau}^+ = \bar{\tau}^- = \tau$) and an electric field applied along the $\hat{x}$ direction ($\mathbf{E} = E_x \hat{x}$):

#### High-Density Regime (HDR)
When both chiral bands are occupied:
$$ M_y = \frac{\mu_B |e| \tau}{2\pi} m \alpha_R [\hat{z} \times \mathbf{E}]_y $$
In vector form:
$$ \mathbf{M} = \frac{\mu_B |e| \tau m \alpha_R}{2\pi} (\hat{z} \times \mathbf{E}) $$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (8), Page 3.
*   **Key Dependencies:**
    *   Linearly proportional to the Rashba coupling $\alpha_R$.
    *   Linearly proportional to the electric field magnitude $E$.
    *   Independent of Fermi energy $E_F$ in the high-density limit.
    *   Direction: Perpendicular to $\mathbf{E}$ (along $\hat{y}$ if $\mathbf{E} \parallel \hat{x}$).

#### Low-Density Regime (LDR)
When only the lower energy band is occupied ($E_F < 0$ relative to the band crossing):
$$ M_y = \frac{\mu_B |e| \tau}{2\pi} \sqrt{(m \alpha_R)^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y $$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (9), Page 3.
*   **Approximation for small $E_F$ (near band crossing):**
    $$ M_y \approx \frac{\mu_B |e| \tau}{2\pi} \left( \alpha_R m + \frac{E_F}{2\alpha_R} \right) [\hat{z} \times \mathbf{E}]_y $$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (10), Page 3.

## 4. Edelstein Susceptibility Tensor
The linear response is often characterized by the Edelstein susceptibility $\chi_{ij}$, defined by $M_j = \chi_{ij} E_i$.

$$ \chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \langle \sigma_y \rangle_{\mathbf{k}}^{\nu} \delta(E_{\nu}(\mathbf{k}) - \mu) v_x^{\nu}(\mathbf{k}) $$
where $\chi_0 = \frac{\tau |e| \mu_B S_{cell}}{4\pi^2 a}$.

*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (7), Page 2.
*   **Resulting Scaling:** For the isotropic case, $\chi_{xy} \propto \alpha_R$.
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Figure 3 discussion, Page 3.

## 5. Nonlinear Effects (High Electric Fields)
If the electric field is strong enough such that the drift velocity $v_d$ becomes comparable to the Fermi velocity $v_F$, the linear response breaks down.

### Nonlinearity Parameter
$$ \gamma = \frac{e E L_s}{E_F} = \frac{e E}{\alpha_R p_F^2} $$
where $L_s = \hbar / (2m\alpha_R)$ is the spin-precession length.

*   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Eq. (12), Page 7.

### Regimes
1.  **Adiabatic Regime ($\gamma \ll 1$):** The spin polarization grows and saturates.
    $$ S_y(t \to \infty) \approx -\frac{n \alpha_R}{v_F} $$
    (Maximum polarization of the annulus of states between $k_F^+$ and $k_F^-$).
    *   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Page 3, Abstract and Section III.
2.  **Non-Adiabatic Regime ($\gamma \gg 1$):** The spin cannot follow the rapidly changing effective field, leading to suppressed polarization.
    *   **Source:** *Theory of the nonlinear Rashba-Edelstein effect*, Page 3, Abstract.

## 6. Anisotropic Rashba Model
For systems with $C_{2v}$ symmetry (anisotropic masses and coupling), the Hamiltonian is:
$$ \hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \sigma_x - \alpha_x k_x \sigma_y $$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (11), Page 3.

The Edelstein susceptibility in the High-Density Regime depends on the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$:
$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} $$
$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} $$
*   **Source:** *Edelstein Effect in Isotropic and Anisotropic Rashba Models*, Eq. (12), Page 4.
*   **Implication:** The effect can be boosted by making $r_m > 1$ and $r_\alpha > 1$.

## 7. Orbital Magnetization (Optional Extension)
In bilayer systems or systems requiring the modern theory of orbital magnetization, an orbital contribution exists:
$$ \mathbf{m} = (\chi_s + \chi_l) \mathbf{E} $$
where $\chi_l$ is the orbital susceptibility.
*   **Source:** *Spin and orbital Edelstein effect in a bilayer system with Rashba interaction*, Eq. (6), Page 2.
*   **Dependence:** The orbital contribution depends on the difference in Rashba parameters between layers ($\alpha_A - \alpha_B$) and can change sign.
*   **Source:** *Spin and orbital Edelstein effect in a bilayer system with Rashba interaction*, Eq. (12) and discussion, Page 4.

## 8. Summary of Dependencies for Model Construction
To compute the magnitude and direction of magnetization for different $\mathbf{E}$:
1.  **Direction:** $\mathbf{M} \parallel \hat{z} \times \mathbf{E}$ (in-plane, perpendicular to current).
2.  **Magnitude (Linear):** $|\mathbf{M}| \propto \alpha_R \tau |\mathbf{E}|$ (Isotropic HDR).
3.  **Magnitude (Linear):** $|\mathbf{M}| \propto \sqrt{(m\alpha_R)^2 + 2mE_F} \tau |\mathbf{E}|$ (Isotropic LDR).
4.  **Magnitude (Anisotropic):** Scales with factors involving $r_m$ and $r_\alpha$ as per Eq. (12).
5.  **Magnitude (Nonlinear):** Saturated at $n \alpha_R / v_F$ for $\gamma \ll 1$, suppressed for $\gamma \gg 1$.
6.  **Chirality:** The net magnetization arises from the imbalance in the population of the two chiral bands ($\nu = \pm$) shifted by the electric field.

**Sources Used:**
1.  *Edelstein Effect in Isotropic and Anisotropic Rashba Models* (arXiv:2503.20712), Pages 1-4, 8-9.
2.  *Theory of the nonlinear Rashba-Edelstein effect* (arXiv:1506.08330), Pages 3-7, 12-14.
3.  *Spin and orbital Edelstein effect in a bilayer system with Rashba interaction* (arXiv:2307.02872), Pages 2-4.
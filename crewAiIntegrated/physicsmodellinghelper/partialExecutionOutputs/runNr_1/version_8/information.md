

# Model for the Direct Edelstein Effect in Rashba Fermions

Based on the provided scientific literature, specifically the work by Gaiaardoni et al. [1], the following model describes the calculation of the Direct Edelstein Effect (DEE) for a Rashba fermion at the Gamma point of the Brillouin zone. This model computes the induced magnetization magnitude and direction under an applied electric field, analyzing dependencies on chirality, Fermi velocity, and spin-orbit coupling strength.

## 1. Theoretical Framework

### 1.1 Rashba Hamiltonian
The system is described by a two-dimensional electron gas with Rashba spin-orbit coupling (RSOC). The Hamiltonian for the isotropic case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
\tag{1}
$$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\vec{\sigma}$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

### 1.2 Magnetization Calculation
Within the semiclassical Boltzmann approach, the expectation value of the magnetization (total spin density) $\vec{M}$ at first order in the electric field $\vec{E}$ is obtained as [1]:

$$
\vec{M} = -\mu_b \sum_{\vec{k}, \nu} |e| (\vec{\nu}_\nu(\vec{k}) \cdot \vec{E}) \delta [E_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_{\vec{k}, \nu}
\tag{2}
$$

where:
*   $\mu_b$ is the Bohr magneton.
*   $\vec{k}$ is the quasi-momentum.
*   $\nu = \pm$ indicates the two chiral Fermi surfaces (helicity).
*   $\vec{\nu}_\nu(\vec{k}) = \bar{\tau}_k^\nu \vec{v}_\nu(\vec{k})$ indicates the mean free path, with $\bar{\tau}_k^\nu$ being the transport lifetime and $\vec{v}_\nu(\vec{k}) = \nabla_{\vec{k}} \epsilon_\nu(\vec{k})$ the group velocity.
*   $E_F$ is the Fermi energy.
*   $\langle \vec{\sigma} \rangle_{\vec{k}, \nu}$ is the spin expectation value evaluated on the eigenstates.

For the isotropic Rashba system, the spin expectation value is [1]:

$$
\langle \vec{\sigma} \rangle_{\vec{k}}^\pm = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
\tag{3}
$$

where $\theta$ is the angle between the vector $\vec{k}$ and the $\hat{x}$ axis, and $k = \sqrt{k_x^2 + k_y^2}$.

## 2. Isotropic Rashba Model Results

### 2.1 High-Density Regime (HDR)
In the High-Density Regime, where both chiral bands are occupied ($E_F$ above the band crossing), the spin density along the $\hat{y}$ direction (assuming an electric field $\vec{E} = E_x \hat{x}$) is derived as [1]:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y
\tag{8}
$$

*   **Magnitude:** The spin density is constant and **independent** of the Fermi energy $E_F$.
*   **Dependence on Parameters:** It depends linearly on the Rashba coupling strength $\alpha$, the effective mass $m$, and the transport time $\tau$.
*   **Direction:** The magnetization is perpendicular to the applied electric field. If $\vec{E} = E_x \hat{x}$, then $\vec{M} \propto \hat{y}$.

### 2.2 Low-Density Regime (LDR)
In the Low-Density Regime, where only the lowest energy band is occupied, the spin density is described by [1]:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y
\tag{9}
$$

*   **Magnitude:** The spin density increases with the Fermi energy $E_F$.
*   **Dependence on Parameters:** For small $E_F$, it can be expanded as [1]:
    $$
    M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \vec{E}]_y
    \tag{10}
    $$

## 3. Anisotropic Rashba Model

For systems with $C_{2v}$ symmetry, anisotropy is introduced in both effective masses and Rashba parameters [1]. The Hamiltonian becomes:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
\tag{11}
$$

### 3.1 Analytical Expressions for Susceptibility
Defining the Edelstein susceptibility $\chi_{ij}$ via $M_j = \chi_{ij} E_i$, the dependence on anisotropy parameters in the HDR is given by [1]:

*   **Mass Anisotropy ($r_m = m_y/m_x$):**
    $$
    \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
    \tag{12}
    $$
*   **Rashba Parameter Anisotropy ($r_\alpha = \alpha_y/\alpha_x$):**
    $$
    \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
    \tag{12}
    $$

where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ is a reference susceptibility scale [1]. The susceptibility increases as the ratios $r_m$ and $r_\alpha$ increase.

## 4. Dependence on Model Parameters

### 4.1 Spin-Orbit Coupling Strength ($\alpha$)
*   **Isotropic Model:** In the HDR, the magnetization magnitude scales linearly with $\alpha$ (Eq. 8). In the LDR, the dependence is more complex but generally increases with $\alpha$ [1].
*   **Anisotropic Model:** The susceptibility $\chi_{xy}$ increases linearly with $\alpha$ (or $\alpha_x$) for fixed ratios, as confirmed by analytical expressions (Eq. 12) and numerical analysis [1].

### 4.2 Electric Field Magnitude and Direction
*   **Direction:** The induced magnetization $\vec{M}$ is always perpendicular to the applied electric field $\vec{E}$ and lies in the plane of the 2D electron gas. Specifically, $\vec{M} \propto \hat{z} \times \vec{E}$ [1].
    *   If $\vec{E} = E_x \hat{x}$, then $\vec{M} = M_y \hat{y}$.
    *   If $\vec{E} = E_y \hat{y}$, then $\vec{M} = -M_x \hat{x}$.
*   **Magnitude:** The magnetization magnitude is linearly proportional to the magnitude of the electric field $|\vec{E}|$ (linear response regime) [1].

### 4.3 Chirality ($\nu = \pm$)
The total magnetization arises from the difference in population between the two chiral bands ($\nu = +$ and $\nu = -$). The Fermi momenta for the two bands in the HDR are [1]:
$$
\begin{cases}
k_F^+ = -k_0 + \sqrt{k_0^2 + 2m E_F} \\
k_F^- = +k_0 + \sqrt{k_0^2 + 2m E_F}
\end{cases}
\tag{5}
$$
where $k_0 = \alpha m$. The difference in transport times and Fermi momenta between these chiral bands drives the net spin accumulation.

## 5. Explicit Graphics and Trends

Based on the numerical and analytical results in the source material [1]:
*   **Susceptibility vs. Chemical Potential:** The Edelstein susceptibility $\chi_{xy}/\chi_0$ shows a plateau in the HDR (constant value) and varies in the LDR.
*   **Susceptibility vs. $\alpha$:** The susceptibility increases linearly with the Rashba parameter $\alpha$ [1].
*   **Anisotropy Effects:** Increasing the anisotropy ratios $r_m$ or $r_\alpha$ (making them $>1$) boosts the Edelstein response compared to the isotropic case ($r_m=r_\alpha=1$). For small ratios ($<1$), the susceptibility is lower [1].

## References

[1] I. Gaiaardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712v1* [cond-mat.mes-hall] (2025).
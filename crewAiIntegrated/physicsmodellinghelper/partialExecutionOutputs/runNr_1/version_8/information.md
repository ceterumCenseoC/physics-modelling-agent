

<<<<<<< HEAD
# Model for the Direct Edelstein Effect in Rashba Fermions

Based on the provided scientific literature, specifically the work by Gaiaardoni et al. [1], the following model describes the calculation of the Direct Edelstein Effect (DEE) for a Rashba fermion at the Gamma point of the Brillouin zone. This model computes the induced magnetization magnitude and direction under an applied electric field, analyzing dependencies on chirality, Fermi velocity, and spin-orbit coupling strength.

## 1. Theoretical Framework

### 1.1 Rashba Hamiltonian
The system is described by a two-dimensional electron gas with Rashba spin-orbit coupling (RSOC). The Hamiltonian for the isotropic case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
\tag{1}
=======
# Calculation of the Edelstein Effect for a Rashba Fermion

Based on the provided scientific literature, specifically the study by Gaiardoni et al. [1], the following model describes the calculation of the Direct Edelstein Effect (DEE) for a Rashba fermion at the Gamma point of the Brillouin zone. The DEE refers to the generation of an in-plane magnetization under an external electric field due to spin-momentum locking in systems with Rashba spin-orbit coupling (RSOC).

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling. The Hamiltonian for the **isotropic** case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma}) \tag{1}
>>>>>>> fa1af29044852733f94c5309bd303d0c3c2f7127
$$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\vec{\sigma}$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

<<<<<<< HEAD
### 1.2 Magnetization Calculation
Within the semiclassical Boltzmann approach, the expectation value of the magnetization (total spin density) $\vec{M}$ at first order in the electric field $\vec{E}$ is obtained as [1]:

$$
\vec{M} = -\mu_b \sum_{\vec{k}, \nu} |e| (\vec{\nu}_\nu(\vec{k}) \cdot \vec{E}) \delta [E_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_{\vec{k}, \nu}
\tag{2}
=======
This Hamiltonian leads to a splitting of the energy bands into two chiral branches ($\nu = \pm$) with eigenenergies $E_\nu(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha \hbar k$. The spin expectation value for an eigenstate with wavevector $\vec{k}$ is tangential to the Fermi surface:

$$
\langle \vec{\sigma} \rangle_\nu^k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix} \tag{2}
$$

where $\theta$ is the angle between $\vec{k}$ and the $\hat{x}$-axis.

## 2. Calculation of Magnetization (Edelstein Effect)

Within the semiclassical Boltzmann approach, the expectation value of the magnetization $\vec{M}$ (total spin density) at first order in the electric field $\vec{E}$ is calculated as [1]:

$$
\vec{M} = -\mu_b \sum_{k, \nu} |e| (\vec{v}_\nu(k) \cdot \vec{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_\nu^k \tag{3}
>>>>>>> fa1af29044852733f94c5309bd303d0c3c2f7127
$$

where:
*   $\mu_b$ is the Bohr magneton.
<<<<<<< HEAD
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
=======
*   $\vec{v}_\nu(k) = \bar{\tau}_\nu^k \nabla_k E_\nu(k)$ is the group velocity scaled by the transport lifetime $\bar{\tau}_\nu^k$.
*   $E_F$ is the Fermi energy.

Assuming a constant transport time $\tau$ and an electric field applied along the $\hat{x}$-direction ($\vec{E} = E_x \hat{x}$), the magnetization is generated perpendicular to the field (along $\hat{y}$).

### 2.1 Isotropic Rashba Model Results

The magnitude of the magnetization depends on the filling regime (High-Density vs. Low-Density).

**High-Density Regime (HDR):** Both chiral bands are occupied ($E_F > 0$ relative to band crossing).
The spin density along $\hat{y}$ is constant and independent of the Fermi energy $E_F$:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x \tag{4}
$$
*   **Direction:** Perpendicular to the electric field ($\vec{M} \parallel \hat{z} \times \vec{E}$).
*   **Magnitude:** Linearly proportional to the spin-orbit coupling strength $\alpha$ and the effective mass $m$.

**Low-Density Regime (LDR):** Only the lowest energy band is occupied ($E_F < 0$ relative to band crossing).
The spin density depends on the Fermi energy:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x \tag{5}
$$
*   For small $E_F$ near the band crossing, this expands to:
    $$
    M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) E_x \tag{6}
    $$
*   **Dependence:** The magnetization increases linearly with $E_F$ in this regime.

### 2.2 Anisotropic Rashba Model

For realistic materials with crystalline anisotropy (e.g., $C_{2v}$ symmetry), the Hamiltonian is modified to include anisotropic effective masses ($m_x, m_y$) and Rashba parameters ($\alpha_x, \alpha_y$) [1]:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y \tag{7}
$$

Defining the anisotropy ratios $r_m = m_x/m_y$ and $r_\alpha = \alpha_x/\alpha_y$, the Edelstein susceptibility $\chi_{xy} = M_y/E_x$ in the HDR is given by:

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} \quad \text{and} \quad \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} \tag{8}
$$

where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ is a normalization factor.
*   **Parameter Dependence:** The susceptibility increases when the anisotropy ratios $r_m$ and $r_\alpha$ exceed 1, allowing for a "boost" in the Edelstein response compared to the isotropic case [1].

## 3. Dependence on Model Parameters

The results demonstrate explicit dependencies on the relevant parameters:

1.  **Spin-Orbit Coupling Strength ($\alpha$):**
    *   In the isotropic HDR, $M_y \propto \alpha$.
    *   Numerical analysis confirms that the Edelstein susceptibility $\chi_{xy}$ increases linearly with $\alpha$ at fixed chemical potential [1].
2.  **Fermi Velocity / Effective Mass ($m$):**
    *   The magnetization scales linearly with the effective mass $m$ in the HDR.
    *   In the LDR, the dependence involves $\sqrt{m^2 \alpha^2 + 2m E_F}$.
3.  **Chirality:**
    *   The effect arises from the imbalance of populations between the two chiral bands ($\nu = \pm$). In the HDR, the difference in transport lifetimes and Fermi wavevectors ($k_F^+, k_F^-$) of the two bands drives the net magnetization [1].
4.  **Electric Field Magnitude and Direction:**
    *   The magnetization is linear in $E$ (linear response regime).
    *   The direction is strictly perpendicular to the applied field ($\vec{M} \perp \vec{E}$) due to the $\hat{z} \times \vec{E}$ term in the analytical expressions [1].

## 4. Explicit Graphics and Visualizations

The source material provides several key graphics illustrating these results [1]:

*   **Figure 1 (Direct Rashba–Edelstein Effect):**
    *   **(a)** Shows the energy dispersion branches ($+$ and $-$) in equilibrium where total spin polarization vanishes.
    *   **(b)** Illustrates the shift of Fermi lines opposite to the field direction ($E = E_x \hat{x}$), resulting in a non-vanishing spin polarization perpendicular to $\vec{E}$ (along $\hat{y}$).
*   **Figure 2 (Edelstein Susceptibility vs. Chemical Potential):**
    *   Shows $\chi_{xy}/\chi_0$ as a function of chemical potential $\mu$. It highlights the transition between regimes and the plateau behavior in the HDR.
    *   Includes a plot of the Fermi surface and spin structure for a fixed chemical potential, showing the inner ($\nu=+1$) and outer ($\nu=-1$) circles with opposite spin winding.
*   **Figure 3 (Susceptibility vs. $\alpha$):**
    *   Left Panel: Susceptibility vs. chemical potential for different $\alpha$ values, showing that higher $\alpha$ leads to a higher plateau value.
    *   Right Panel: Susceptibility vs. $\alpha$ at fixed $\mu$, confirming the linear increase.
*   **Figure 5 & 6 (Anisotropy Effects):**
    *   Show the Edelstein susceptibility as a function of chemical potential for varying mass anisotropy ($r_m$) and SOC anisotropy ($r_\alpha$).
    *   Confirm that $r_m > 1$ and $r_\alpha > 1$ boost the response, while values $< 1$ reduce it compared to the isotropic case.
    *   Figure 6 explicitly plots the susceptibility against $r_m$ and $r_\alpha$, showing the linear increase for small ratios and saturation for large $r_\alpha$.

## 5. References

[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712v1* (2025). [Note: This is the primary source extracted from the provided text].

[2] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233 (1990). [Cited as Ref [29] in the source text].

[3] J.-i. Inoue, G. E. Bauer, and L. W. Molenkamp, "Diffuse transport and spin accumulation in a rashba two-dimensional electron gas," *Physical Review B* **67**, 033104 (2003). [Cited as Ref [19] in the source text].

[4] A. Johansson, J. Henk, and I. Mertig, "Theoretical aspects of the edelstein effect for anisotropic two-dimensional electron gas and topological insulators," *Physical Review B* **93**, 195440 (2016). [Cited as Ref [34] in the source text].
>>>>>>> fa1af29044852733f94c5309bd303d0c3c2f7127

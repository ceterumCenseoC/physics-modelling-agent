

# Calculation of the Edelstein Effect for a Rashba Fermion

Based on the provided scientific literature, specifically the study by Gaiardoni et al. [1], the following model describes the calculation of the Direct Edelstein Effect (DEE) for a Rashba fermion at the Gamma point of the Brillouin zone. The DEE refers to the generation of an in-plane magnetization under an external electric field due to spin-momentum locking in systems with Rashba spin-orbit coupling (RSOC).

## 1. Theoretical Framework and Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling. The Hamiltonian for the **isotropic** case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma}) \tag{1}
$$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\vec{\sigma}$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

This Hamiltonian leads to a splitting of the energy bands into two chiral branches ($\nu = \pm$) with eigenenergies $E_\nu(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha \hbar k$. The spin expectation value for an eigenstate with wavevector $\vec{k}$ is tangential to the Fermi surface:

$$
\langle \vec{\sigma} \rangle_\nu^k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix} \tag{2}
$$

where $\theta$ is the angle between $\vec{k}$ and the $\hat{x}$-axis.

## 2. Calculation of Magnetization (Edelstein Effect)

Within the semiclassical Boltzmann approach, the expectation value of the magnetization $\vec{M}$ (total spin density) at first order in the electric field $\vec{E}$ is calculated as [1]:

$$
\vec{M} = -\mu_b \sum_{k, \nu} |e| (\vec{v}_\nu(k) \cdot \vec{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_\nu^k \tag{3}
$$

where:
*   $\mu_b$ is the Bohr magneton.
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
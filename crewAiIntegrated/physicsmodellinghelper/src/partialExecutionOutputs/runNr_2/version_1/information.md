

# Calculation of the Edelstein Effect for a Rashba Fermion

## 1. Model Hamiltonian

The system is described by a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian for an isotropic Rashba model is given by [1]:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})
\tag{1}
$$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.
*   $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.

The energy dispersion relation exhibits a spin-splitting into two chiral bands ($\nu = \pm$):
$$
E_\nu(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k
$$
where $k = |\mathbf{k}|$ and $\nu = \pm 1$ corresponds to the inner and outer Fermi surfaces, respectively.

## 2. Direct Edelstein Effect (DEE) Formalism

The Direct Edelstein Effect refers to the generation of a non-equilibrium in-plane magnetization $\mathbf{M}$ induced by an external electric field $\mathbf{E}$. Within the semiclassical Boltzmann transport theory, the expectation value of the magnetization at first order in the electric field is [1]:

$$
\mathbf{M} = -\mu_B \sum_{\mathbf{k}, \nu} |e| (\mathbf{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta [E_\nu(\mathbf{k}) - E_F] \langle \boldsymbol{\sigma} \rangle^\nu_\mathbf{k}
\tag{2}
$$

where:
*   $\mu_B$ is the Bohr magneton.
*   $e$ is the elementary charge.
*   $\mathbf{v}_\nu(\mathbf{k}) = \nabla_\mathbf{k} E_\nu(\mathbf{k})$ is the group velocity.
*   $E_F$ is the Fermi energy.
*   $\langle \boldsymbol{\sigma} \rangle^\nu_\mathbf{k}$ is the spin expectation value for the eigenstates. For the Rashba model:
    $$
    \langle \boldsymbol{\sigma} \rangle^\nu_\mathbf{k} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
    \tag{3}
    $$
    where $\theta$ is the angle of the wavevector $\mathbf{k}$ with respect to the $\hat{x}$ axis.

## 3. Magnetization Magnitude and Direction

The magnetization is calculated for an applied electric field $\mathbf{E} = E_x \hat{x}$. Due to spin-momentum locking, the induced magnetization is perpendicular to the electric field and lies in the plane of the system (along $\hat{y}$).

### 3.1. Isotropic Rashba Model

The analytical expressions for the spin density (magnetization) depend on the electronic density regime.

#### High-Density Regime (HDR)
In the regime where both chiral bands are occupied ($E_F > 0$ relative to the band crossing), the spin density along the $\hat{y}$ direction is [1]:

$$
M_y = \frac{\mu_B |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
\tag{4}
$$

Assuming $\mathbf{E} = E_x \hat{x}$, then $[\hat{z} \times \mathbf{E}]_y = E_x$. Thus:
$$
M_y = \frac{\mu_B |e| \tau m \alpha}{2\pi} E_x
$$
*   **Magnitude:** Constant and independent of the Fermi energy $E_F$ in the high-density limit.
*   **Direction:** Perpendicular to $\mathbf{E}$ (along $\hat{y}$ for $\mathbf{E} \parallel \hat{x}$).
*   **Parameters:** Linearly dependent on the Rashba coupling $\alpha$, effective mass $m$, and relaxation time $\tau$.

#### Low-Density Regime (LDR)
In the regime where only the lowest energy band is occupied ($E_F < 0$ relative to the band crossing, or near the band minimum), the spin density is [1]:

$$
M_y = \frac{\mu_B |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y
\tag{5}
$$

For Fermi energies close to the band crossing ($E_F \ll m\alpha^2$), this can be expanded as [1]:
$$
M_y \approx \frac{\mu_B |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) [\hat{z} \times \mathbf{E}]_y
\tag{6}
$$
*   **Magnitude:** Increases linearly with the Fermi energy $E_F$.
*   **Direction:** Remains perpendicular to $\mathbf{E}$.

### 3.2. Anisotropic Rashba Model

For systems with anisotropy (e.g., $C_{2v}$ symmetry), the effective masses and Rashba parameters differ along the principal axes ($m_x \neq m_y$, $\alpha_x \neq \alpha_y$). The Hamiltonian becomes [1]:
$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \sigma_x - \alpha_x k_x \sigma_y
\tag{7}
$$

Defining the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$, the Edelstein susceptibility $\chi_{xy}$ in the High-Density Regime is given by [1]:
$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
\tag{8}
$$
$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
\tag{9}
$$
where $\chi_0$ is a reference susceptibility.
*   **Dependency:** The susceptibility increases as the anisotropy ratios $r_m$ and $r_\alpha$ increase (for $r > 1$).
*   **Trend:** For small anisotropy, the susceptibility increases linearly with the ratios, but tends to saturate for large $r_\alpha$.

## 4. Dependence on Model Parameters

Based on the analytical expressions and numerical results from the source material [1]:

| Parameter | Effect on Magnetization ($M_y$) | Regime |
| :--- | :--- | :--- |
| **Rashba Coupling ($\alpha$)** | Linear increase in HDR (Eq. 4). Linear increase in LDR for small $E_F$ (Eq. 6). | Both |
| **Effective Mass ($m$)** | Linear increase in HDR. Increases the term $\sqrt{m^2\alpha^2}$ in LDR. | Both |
| **Fermi Energy ($E_F$)** | Independent in HDR. Linear increase in LDR (Eq. 6). | LDR |
| **Relaxation Time ($\tau$)** | Linear increase. | Both |
| **Electric Field ($\mathbf{E}$)** | Linear response ($M \propto E$). Direction is $\mathbf{M} \perp \mathbf{E}$. | Both |
| **Chirality ($\nu = \pm$)** | Contributions from both bands in HDR partially cancel/sum depending on velocities. In LDR, dominated by the occupied band. | Both |

## 5. Graphical Trends

The source material provides explicit graphics illustrating these dependencies [1]:
*   **Figure 2:** Shows the Edelstein susceptibility $\chi_{xy}/\chi_0$ as a function of the chemical potential $\mu$. In the HDR, the susceptibility saturates to a constant value, while in the LDR, it increases with $\mu$.
*   **Figure 3:** Shows $\chi_{xy}/\chi_0$ as a function of the Rashba parameter $\alpha$. The susceptibility increases linearly with $\alpha$.
*   **Figure 5 & 6:** Illustrate the effect of anisotropy ($r_m$ and $r_\alpha$). The susceptibility is lower than the isotropic case when $r < 1$ and higher when $r > 1$. The analytical expressions (8) and (9) match the numerical data points.

## 6. Conclusion

The Edelstein effect for a Rashba fermion at the Gamma point generates an in-plane magnetization perpendicular to the applied electric field. The magnitude is determined by the Rashba coupling strength $\alpha$, effective mass $m$, and carrier density (via $E_F$). In the high-density regime, the magnetization is independent of $E_F$ and scales linearly with $\alpha$ and $m$. In the low-density regime, it scales with $\sqrt{m^2\alpha^2 + 2mE_F}$. Anisotropy in mass or spin-orbit coupling can boost the Edelstein response if the anisotropy ratios exceed unity.

***

**References**
[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712v1 [cond-mat.mes-hall]* (2025).
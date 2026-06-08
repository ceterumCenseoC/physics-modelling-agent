

# Edelstein Effect Model for Rashba Fermions

Based on the provided scientific literature, specifically **"Edelstein Effect in Isotropic and Anisotropic Rashba Models"** (Gaiardoni et al., 2025) [1], the following information is extracted to calculate the Direct Edelstein Effect (DEE) for a Rashba fermion at the Gamma point. This includes the Hamiltonian, analytical expressions for magnetization, parameter dependencies, and descriptions of the resulting graphical behavior.

## 1. Model Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian for the **isotropic** case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
\tag{1}
$$

Where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.

The energy dispersion relation $E_\nu(k)$ results in two chiral bands ($\nu = \pm$):
$$
E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k
\tag{6}
$$
*(Note: Derived from the text's description of band splitting in Eq. 1 and Figure 1)*.

## 2. Magnetization Calculation (Direct Edelstein Effect)

The Direct Edelstein Effect (DEE) describes the generation of an in-plane magnetization $\vec{M}$ under an external electric field $\vec{E}$. Within the semiclassical Boltzmann approach, the expectation value of the magnetization (total spin density) at first order in the electric field is:

$$
\vec{M} = -\mu_b \sum_{\vec{k}, \nu} |e| (\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \delta [E_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_{\vec{k}, \nu}
\tag{2}
$$

Where:
*   $\mu_b$ is the Bohr magneton.
*   $\vec{v}_\nu(\vec{k}) = \nabla_{\vec{k}} E_\nu(\vec{k})$ is the group velocity.
*   $\bar{\tau}_\nu(\vec{k})$ is the transport lifetime (mean free path $\bar{\tau}_\nu \vec{v}_\nu$).
*   $E_F$ is the Fermi energy.
*   $\langle \vec{\sigma} \rangle_{\vec{k}, \nu}$ is the spin expectation value for eigenstate $\nu$.

The spin expectation value for the Rashba eigenstates is:
$$
\langle \vec{\sigma} \rangle^\pm_{\vec{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
\tag{3}
$$
Where $\theta$ is the angle between $\vec{k}$ and the $\hat{x}$ axis.

### Magnetization Direction
Due to spin-momentum locking, an electric field $\vec{E} = E_x \hat{x}$ induces a magnetization perpendicular to the field direction, lying in the plane:
$$
\vec{M} \propto \hat{z} \times \vec{E}
$$
Specifically, for $\vec{E} = E_x \hat{x}$, the magnetization is along the $\hat{y}$ direction ($M_y$).

## 3. Analytical Expressions for Magnetization

The magnitude of the magnetization depends on the electronic density regime.

### A. High-Density Regime (HDR)
Both chiral bands ($\nu = +$ and $\nu = -$) are occupied. Assuming a constant transport time $\bar{\tau}_+ = \bar{\tau}_- = \tau$:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y
\tag{8}
$$

*   **Dependency:** $M_y$ is **constant** and independent of the Fermi energy $E_F$ in this regime.
*   **Linear Dependence:** $M_y \propto \alpha$ (linear with SOC strength).

### B. Low-Density Regime (LDR)
Only the lowest energy band is occupied. The expression becomes:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y
\tag{9}
$$

*   **Dependency:** $M_y$ increases with $E_F$.
*   **Small $E_F$ Expansion:** For $E_F$ near the band crossing:
    $$
    M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \vec{E}]_y
    \tag{10}
    $$

### C. Edelstein Susceptibility
The linear Edelstein susceptibility is defined as $M_j = \chi_{ij} E_i$. For the isotropic case ($E=E_x \hat{x}, M=M_y \hat{y}$):

$$
\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle^\nu_{\vec{k}} \delta(E^\nu_{\vec{k}} - \mu) v^\nu_x(\vec{k})
\tag{7}
$$
Where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$.

## 4. Anisotropic Rashba Model

For systems with $C_{2v}$ symmetry (e.g., due to strain or substrate effects), the Hamiltonian includes anisotropic masses ($m_x, m_y$) and SOC parameters ($\alpha_x, \alpha_y$):

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
\tag{11}
$$

In the High-Density Regime, the susceptibility depends on the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$:

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
\tag{12a}
$$

$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
\tag{12b}
$$

*   **Observation:** The Edelstein effect can be **boosted** by making $r_m > 1$ and $r_\alpha > 1$.

## 5. Dependencies on Parameters

| Parameter | Effect on Magnetization ($M_y$) / Susceptibility ($\chi_{xy}$) | Regime | Citation |
| :--- | :--- | :--- | :--- |
| **SOC Strength ($\alpha$)** | Linear increase ($M_y \propto \alpha$). | HDR | Eq. (8), Fig. 3 |
| **Fermi Energy ($E_F$)** | Constant in HDR; Increases as $\sqrt{E_F}$ in LDR. | HDR / LDR | Eq. (8), Eq. (9) |
| **Effective Mass ($m$)** | Linear increase ($M_y \propto m$). | HDR | Eq. (8) |
| **Relaxation Time ($\tau$)** | Linear increase ($M_y \propto \tau$). | Both | Eq. (8), Eq. (9) |
| **Anisotropy ($r_m, r_\alpha$)** | Increases susceptibility if $>1$; saturates for large $r_\alpha$. | HDR | Eq. (12), Fig. 6 |
| **Chirality ($\nu$)** | Magnetization arises from the imbalance of population between $\nu=+$ and $\nu=-$ bands. | Both | Eq. (4) |

## 6. Explicit Graphics Description

Based on the data provided in the source [1], the following graphics should be constructed to visualize the model results:

### Figure 1: Edelstein Susceptibility vs. Chemical Potential
*   **X-axis:** Chemical Potential $\mu$ (or $E_F$).
*   **Y-axis:** Normalized Susceptibility $\chi_{xy}/\chi_0$.
*   **Behavior:**
    *   Shows a plateau in the **High-Density Regime** (constant value).
    *   Shows a linear increase from zero in the **Low-Density Regime** (near band crossing).
    *   **Source:** Figure 2 (Left panel) [1].

### Figure 2: Susceptibility vs. SOC Strength ($\alpha$)
*   **X-axis:** Rashba parameter $\alpha$ (meV Å).
*   **Y-axis:** Normalized Susceptibility $\chi_{xy}/\chi_0$.
*   **Behavior:** Linear increase with $\alpha$.
*   **Source:** Figure 2 (Right panel) [1].

### Figure 3: Susceptibility vs. Anisotropy Ratios
*   **X-axis:** Mass ratio $r_m = m_y/m_x$ OR SOC ratio $r_\alpha = \alpha_y/\alpha_x$.
*   **Y-axis:** Normalized Susceptibility $\chi_{xy}/\chi_0$.
*   **Behavior:**
    *   Increases as the ratio increases.
    *   Linear for small ratios, tends to saturate for large $r_\alpha$.
    *   **Source:** Figure 6 [1].

### Figure 4: Fermi Surfaces and Spin Texture
*   **Plot:** 2D plot in $k_x, k_y$ space.
*   **Content:**
    *   **Equilibrium ($E=0$):** Two concentric circles (inner $\nu=+$, outer $\nu=-$). Spin vectors tangential to the circles (clockwise/counter-clockwise). Net spin = 0.
    *   **Under Field ($E \neq 0$):** Fermi circles shift opposite to $E$. Net spin polarization appears perpendicular to $E$.
    *   **Source:** Figure 1 and Figure 2 [1].

## 7. Implementation Notes for Model

To compute the magnetization for a specific set of parameters:
1.  **Define Regime:** Calculate $k_{F\pm}$ using Eq. (5) (HDR) or Eq. (6) (LDR) from the source.
    *   $k_0 = \alpha m$.
    *   $k_{F\pm} = \mp k_0 + \sqrt{k_0^2 + 2mE_F}$ (HDR).
2.  **Calculate $M_y$:** Use Eq. (4) if $\tau$ differs between bands, or Eq. (8)/(9) for the simplified isotropic cases.
3.  **Anisotropy:** If $m_x \neq m_y$ or $\alpha_x \neq \alpha_y$, use Eq. (12) to scale the isotropic result.

---
**References:**
[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712v1* (2025).
[2] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233 (1990).
[3] Y. A. Bychkov and E. I. Rashba, "Properties of a 2D electron gas with lifted spectral degeneracy," *JETP Lett.* **39**, 78 (1984).
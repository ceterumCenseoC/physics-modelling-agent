

# Model Information for Calculating the Edelstein Effect in a Rashba Fermion System

## 1. System Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian describes the kinetic energy and the spin-orbit interaction arising from broken inversion symmetry.

**Hamiltonian:**
$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (1)*

Where:
- $p$ is the momentum.
- $m$ is the effective carrier mass.
- $\alpha$ is the Rashba spin-orbit coupling strength.
- $\hat{z}$ is the unit vector normal to the 2D plane.
- $\vec{\sigma}$ is the vector of Pauli matrices.

**Alternative Form (using $k$ and $\hbar=1$):**
$$
\hat{H} = \frac{k^2}{2m} + \alpha \hat{z} \cdot (\vec{\sigma} \times \vec{k})
$$
*Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Equation (1)*

## 2. Energy Dispersion and Chirality

The Rashba term splits the spin degeneracy, resulting in two chiral bands.

**Energy Dispersion:**
$$
\varepsilon^\nu_k = \frac{k^2}{2m} + \nu k \alpha
$$
*Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Equation (2)*

Where:
- $k = |\vec{k}|$ is the modulus of the momentum.
- $\nu = \pm$ is the **chirality index** (band index).

## 3. Fermi Momenta and Regimes

The occupation of bands depends on the chemical potential $\mu$ (or Fermi energy $E_F$). Two regimes are defined:

### High-Density Regime (HDR)
Defined by $\mu \ge 0$ (above the band crossing). Both chiral bands contribute to transport.
**Fermi Momenta:**
$$
k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + 2m\mu}
$$
*Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Equation (3)*

Where $k_0 = \alpha m$.

### Low-Density Regime (LDR)
Defined by $\mu < 0$ (below the band crossing). Only the lower energy band is occupied.
**Fermi Momenta:**
$$
k^\eta_F = k_0 - \eta \sqrt{k_0^2 + 2m\mu}
$$
*Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Equation (4)*

Where $\eta = \pm$ distinguishes between left and right carriers for the lower band.

## 4. Direct Edelstein Effect (DEE) Model

The Direct Edelstein Effect describes the generation of a non-equilibrium spin polarization (magnetization) in response to an applied electric field $\mathbf{E}$.

### Magnetization Definition
The expectation value of the magnetization $\mathbf{M}$ (total spin density) at first order in the electric field is given by:
$$
\mathbf{M} = -\mu_b \sum_{k,\nu} |e| (\vec{v}_\nu(k) \cdot \mathbf{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle^\nu_k
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (2)*

Where:
- $\mu_b$ is the Bohr magneton.
- $\vec{v}_\nu(k) = \bar{\tau}^\nu_k \vec{v}_\nu(k)$ indicates the mean free path (with transport lifetime $\bar{\tau}$).
- $\langle \vec{\sigma} \rangle^\nu_k$ is the spin expectation value on the eigenstates.

### Spin Expectation Value
For the isotropic Rashba model, the spin is tangential to the Fermi surface:
$$
\langle \vec{\sigma} \rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (3)*

Where $\theta$ is the angle between vector $\vec{k}$ and the $\hat{x}$ axis.

### Magnetization Magnitude and Direction
For an applied electric field $\mathbf{E} = E_x \hat{x}$, the induced magnetization is perpendicular to the electric field in the plane (along $\hat{y}$).

**General Direction:**
$$
\mathbf{M} \propto \hat{z} \times \mathbf{E}
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equations (8) and (9)*

**Analytical Expression in HDR ($\mu \ge 0$):**
Assuming constant transport time $\bar{\tau}_+ = \bar{\tau}_- = \tau$:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (8)*

**Analytical Expression in LDR ($\mu < 0$):**
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (9)*

**General Spin Density Formula (before integration):**
$$
m_y = \frac{\mu_b |e| E_x}{4\pi} (\bar{\tau}_+ k^+_F - \bar{\tau}_- k^-_F)
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (4)*

## 5. Parameter Dependencies

The magnitude of the Edelstein effect depends on the following parameters:

1.  **Rashba Coupling ($\alpha$):** The magnetization is proportional to $\alpha$ in the HDR (Eq. 8) and depends on $\sqrt{\alpha^2}$ in the LDR (Eq. 9). Increasing $\alpha$ increases the spin susceptibility.
    *Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 3, Figure 3 analysis.*
2.  **Fermi Velocity / Chemical Potential ($\mu$ or $E_F$):**
    *   In HDR, the magnetization is constant and independent of $E_F$ (Eq. 8).
    *   In LDR, the magnetization increases with $E_F$ (Eq. 9).
    *Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 3, Equations (8) and (9).*
3.  **Chirality ($\nu$):** The contribution to the magnetization comes from the difference in Fermi momenta of the two chiral bands ($k^+_F$ and $k^-_F$). In LDR, the transport-chirality index $\eta$ becomes relevant.
    *Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Page 3, Section II.*
4.  **Effective Mass ($m$):** The magnetization scales with $m$ (Eq. 8).
    *Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (8).*
5.  **Scattering Time ($\tau$):** The magnetization is linearly proportional to the transport lifetime $\tau$.
    *Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (8).*

## 6. Anisotropic Rashba Model

For systems with $C_{2v}$ symmetry (anisotropic effective masses or SOC), the Hamiltonian is modified:
$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (11)*

**Anisotropy Ratios:**
- Mass ratio: $r_m = m_y/m_x$
- SOC ratio: $r_\alpha = \alpha_y/\alpha_x$

**Edelstein Susceptibility in HDR:**
$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
$$
$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
$$
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Equation (12)*

Where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$.
*Source: `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Page 2, below Equation (7).*

## 7. Group Velocity

The group velocity is required for calculating the current and magnetization integrals.
$$
v^{\nu/\eta}_F = \frac{\partial \varepsilon^\nu_k}{\partial k} \Bigg|_{k=k^{\nu/\eta}_F} = \frac{k^{\nu/\eta}_F}{m} + \nu \alpha
$$
*Source: `Boltzmann_theory_of_the_inverse_Edelstei.pdf`, Equation (8)*
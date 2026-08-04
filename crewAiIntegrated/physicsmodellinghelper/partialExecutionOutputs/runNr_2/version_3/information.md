

# Edelstein Effect Model for Rashba Fermions at the $\Gamma$ Point

The following model extracts the necessary theoretical framework and analytical expressions to calculate the Direct Edelstein Effect (DEE) in a 2D Rashba electron gas. This model computes the induced magnetization (spin density) resulting from an applied electric field, detailing its dependence on chirality, Fermi velocity, and spin-orbit coupling (SOC) strength.

## 1. Hamiltonian and System Definition
The system is modeled as a two-dimensional electron gas (2DEG) with broken inversion symmetry, described by the isotropic Rashba Hamiltonian at the $\Gamma$ point of the Brillouin zone:

$$ \hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha_R (\hat{z} \times \vec{k}) \cdot \vec{\sigma} $$

Where:
*   $\vec{k} = (k_x, k_y)$ is the 2D wave vector.
*   $m$ is the effective carrier mass.
*   $\alpha_R$ is the Rashba spin-orbit coupling strength.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2DEG plane [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf].

The energy dispersion is split into two chiral branches ($\nu = \pm$):
$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha_R \hbar k $$

## 2. Magnetization Calculation (Magnitude and Direction)
Applying an external in-plane electric field $\vec{E}$ shifts the Fermi surface, inducing a net spin polarization (magnetization) $\vec{M}$. Using the semiclassical Boltzmann transport equation, the magnetization is linearly proportional to the electric field:

$$ \vec{M} = \chi_{EE} (\hat{z} \times \vec{E}) $$

The induced magnetization $\vec{M}$ is always **in-plane** and **perpendicular** to the applied electric field $\vec{E}$ [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf]. The Edelstein susceptibility $\chi_{EE}$ depends on the electronic density regime:

### High-Density Regime (HDR)
When the Fermi energy $E_F$ is sufficiently high such that both chiral bands are occupied:
$$ \chi_{EE}^{\text{HDR}} = \frac{\mu_B |e| \tau m \alpha_R}{2\pi} $$
$$ \vec{M} = \frac{\mu_B |e| \tau m \alpha_R}{2\pi} (\hat{z} \times \vec{E}) $$

### Low-Density Regime (LDR)
When only the lower-energy band is occupied:
$$ \chi_{EE}^{\text{LDR}} = \frac{\mu_B |e| \tau \sqrt{m^2 \alpha_R^2 + 2m E_F}}{2\pi} $$
$$ \vec{M} = \frac{\mu_B |e| \tau \sqrt{m^2 \alpha_R^2 + 2m E_F}}{2\pi} (\hat{z} \times \vec{E}) $$

*Where $\mu_B$ is the Bohr magneton, $|e|$ is the elementary charge, $\tau$ is the transport relaxation time, and $E_F$ is the Fermi energy* [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf].

## 3. Dependence on Model Parameters

### Electric Field Magnitude and Direction
*   **Magnitude:** The magnetization magnitude $|\vec{M}|$ scales linearly with the magnitude of the electric field $|\vec{E}|$.
*   **Direction:** The vector direction is strictly orthogonal to the field, determined by the cross product $\hat{z} \times \vec{E}$. If $\vec{E}$ is applied along the x-axis ($\hat{x}$), $\vec{M}$ points along the y-axis ($\hat{y}$) [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf].

### Spin-Orbit Coupling Strength ($\alpha_R$)
*   In the **HDR**, the magnetization scales linearly with the Rashba parameter $\alpha_R$. Increasing SOC strength directly amplifies the spin-charge conversion efficiency.
*   In the **LDR**, the dependence is sub-linear, scaling with $\sqrt{m^2 \alpha_R^2 + 2m E_F}$ [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf].

### Fermi Velocity and Fermi Energy ($v_F, E_F$)
The behavior is strongly dependent on the chemical potential (Fermi energy $E_F$), which relates to Fermi velocity $v_F$ via $E_F = \frac{1}{2}mv_F^2$:
*   **HDR:** The susceptibility is independent of $E_F$ (and thus $v_F$), resulting in a constant plateau for magnetization.
*   **LDR:** The susceptibility increases with $E_F$. Near the band crossing point ($E_F \approx 0$), the spin density increases linearly with Fermi energy [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf].

### Chirality
The Rashba effect locks the electron spin perpendicular to its momentum (spin-momentum locking). The two bands exhibit opposite chirality ($\nu = \pm$).
*   **HDR:** The net Edelstein magnetization is the superposition of contributions from both chiral Fermi surfaces. Their contributions add constructively to the total in-plane magnetization.
*   **LDR:** Only the inner Fermi surface (one chirality state) is occupied, reducing the total spin accumulation compared to the HDR [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf].

### Anisotropy Effects
If the system possesses $C_{2v}$ symmetry (e.g., due to substrate strain), the effective mass ($m_x \neq m_y$) or SOC strength ($\alpha_x \neq \alpha_y$) becomes anisotropic. The susceptibility $\chi_{xy}$ scales with the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$ in the HDR:

$$ \frac{\chi_{xy}}{\chi_0}(r_m) = 4\pi m_x \alpha \frac{r_m}{1 + \sqrt{r_m}} $$
$$ \frac{\chi_{xy}}{\chi_0}(r_\alpha) = 4\pi m \alpha_x \frac{r_\alpha}{1 + r_\alpha} $$

Boosting these ratios above 1 enhances the Edelstein response [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf].

## 4. Explicit Graphics for Model Visualization

To fully visualize the model, the following plots should be generated based on the extracted equations:

### Graph 1: Fermi Surface and Spin Texture Shift
*   **X/Y Axis:** Momentum space $k_x, k_y$.
*   **Visuals:** Plot two concentric circles representing the two chiral Fermi surfaces (inner and outer). Draw tangent vectors on the circles to represent spin direction ($\vec{S} \perp \vec{k}$).
*   **Effect:** Show a slight shift of these circles opposite to the applied electric field $\vec{E}$. Color-code the resulting imbalance to show a net vector sum pointing perpendicular to $\vec{E}$.
*   **Source:** [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf], Fig. 1.

### Graph 2: Magnetization vs. Rashba Parameter ($\alpha_R$)
*   **X Axis:** Rashba coupling strength $\alpha_R$ (meV Å).
*   **Y Axis:** Spin Susceptibility $\chi_{xy}$ or Magnetization $M_y$.
*   **Visuals:** A straight line passing through the origin for the HDR regime. For LDR, a curve that flattens at low $\alpha_R$ and approaches the linear trend at higher values.
*   **Source:** [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf], Fig. 3 (Right Panel).

### Graph 3: Magnetization vs. Fermi Energy ($E_F$)
*   **X Axis:** Chemical potential / Fermi energy $\mu$ (eV).
*   **Y Axis:** Spin Susceptibility $\chi_{xy}$.
*   **Visuals:** A curve that starts at zero (or a finite value if gap exists), rises sharply near the band crossing, and hits a constant plateau once the second band is populated (HDR).
*   **Source:** [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf], Fig. 2 (Left Panel).

### Graph 4: Anisotropy Enhancement
*   **X Axis:** Mass ratio $r_m$ or SOC ratio $r_\alpha$.
*   **Y Axis:** Normalized Susceptibility $\chi_{xy}/\chi_0$.
*   **Visuals:** Plots showing that as anisotropy ratios exceed 1, the Edelstein susceptibility increases, demonstrating tunability through effective mass or SOC engineering.
*   **Source:** [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf], Fig. 6.

## 5. Scientific Citations
*   [Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf] - *Irene Gaiardoni, Mattia Trama, Alfonso Maiellaro, Claudio Guarcello, Francesco Romeo, Roberta Citro. Provides the semiclassical Boltzmann derivation, HDR/LDR analytical limits, and anisotropy formulas.*
*   [Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets.pdf] - *Motohiko Ezawa. Provides the general zero-temperature integral formulation for magnetization using the Boltzmann distribution shift.*
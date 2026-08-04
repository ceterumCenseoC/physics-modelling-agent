

# Model for the Edelstein Effect in Rashba Fermions

This document provides a complete mathematical description of a model to calculate the Direct Edelstein Effect (DEE) for a Rashba fermion at the Gamma point of the Brillouin zone. The model computes the induced magnetization magnitude and direction under an applied electric field, analyzing dependencies on chirality, Fermi velocity, and spin-orbit coupling strength. All derivations and results are based on the scientific literature provided, specifically the study by Gaiardoni et al. (2025) [1].

## 1. System Hamiltonian and Setup

The physical system is modeled as a two-dimensional electron gas (2DEG) characterized by Rashba spin-orbit coupling (RSOC). The calculation is performed at the Gamma point ($\mathbf{k}=0$) of the Brillouin zone.

### 1.1 Hamiltonian Definition
The single-particle Hamiltonian $\hat{H}$ is defined as:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})
$$

where:
*   $p$ is the momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane ($z$-direction).

### 1.2 Energy Dispersion and Chirality
The energy dispersion relation yields two chiral bands ($\nu = \pm$) with eigenvalues:

$$
E_{\nu}(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k
$$

where $k = |\mathbf{k}|$ and $\nu = \pm 1$ represents the chirality (inner and outer Fermi surfaces). The helicity operator is defined as $\hat{S} = \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})/p$, with eigenvalues $s = \pm 1$ [1].

## 2. Model Steps for Magnetization Calculation

The model follows a semiclassical Boltzmann transport approach to determine the non-equilibrium spin density induced by an electric field.

### Step 1: Define the Group Velocity
Calculate the group velocity $\mathbf{v}_\nu(\mathbf{k})$ for each band $\nu$ by taking the gradient of the energy dispersion with respect to momentum:

$$
\mathbf{v}_\nu(\mathbf{k}) = \nabla_{\mathbf{k}} E_\nu(\mathbf{k}) = \frac{\hbar^2 \mathbf{k}}{m} + \nu \alpha \frac{\mathbf{k}}{k}
$$

### Step 2: Determine Spin Expectation Value
Calculate the expectation value of the spin operator $\langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^\nu$ for the eigenstates of the Hamiltonian. For the Rashba model, the spin lies in the plane perpendicular to momentum:

$$
\langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^\nu = \nu (\hat{z} \times \hat{k}) = \frac{\nu}{k} (-k_y, k_x, 0)^T
$$

### Step 3: Apply Boltzmann Transport Equation
Under a static electric field $\mathbf{E}$, the distribution function $f_{\mathbf{k}}^\nu$ shifts from equilibrium $f_0$. To first order in $\mathbf{E}$, the non-equilibrium correction is proportional to the product of the velocity, electric field, and transport lifetime $\bar{\tau}_\nu$:

$$
\delta f_{\mathbf{k}}^\nu \propto - \frac{\partial f_0}{\partial E} (\mathbf{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \bar{\tau}_\nu
$$

### Step 4: Integrate to Find Magnetization
The magnetization (spin density) $\mathbf{M}$ is the sum of the spin expectation values weighted by the non-equilibrium distribution over the Fermi surface:

$$
\mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| (\mathbf{v}_\nu(\mathbf{k}) \cdot \mathbf{E}) \bar{\tau}_\nu \delta [E_\nu(\mathbf{k}) - E_F] \langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^\nu
$$

where $\mu_b$ is the Bohr magneton and $E_F$ is the Fermi energy.

## 3. Analytical Results for Magnetization

The integration over the Fermi surface yields distinct results depending on the density regime.

### 3.1 Isotropic Model: High-Density Regime (HDR)
In the HDR, both chiral bands ($\nu = +$ and $\nu = -$) are occupied ($E_F > 0$). Assuming equal transport times $\bar{\tau}_+ = \bar{\tau}_- = \tau$, the magnetization is induced perpendicular to the electric field.

For an electric field $\mathbf{E} = E_x \hat{x}$, the magnetization is along $\hat{y}$:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
$$

**Key Finding:** In the HDR, the Edelstein susceptibility is **constant and independent of the Fermi energy $E_F$**. It scales linearly with the spin-orbit coupling $\alpha$ and effective mass $m$ [1].

### 3.2 Isotropic Model: Low-Density Regime (LDR)
In the LDR, only the lower energy band ($\nu = -$) is occupied. The magnetization magnitude depends on the Fermi energy:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y
$$

**Key Finding:** For small Fermi energies ($E_F \to 0$), the spin density **increases linearly with the Fermi energy** [1].

### 3.3 Anisotropic Model
For systems with anisotropy in effective mass ($r_m = m_y/m_x$) and Rashba parameters ($r_\alpha = \alpha_y/\alpha_x$), the Hamiltonian is modified:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

The Edelstein susceptibility $\chi_{xy}$ (where $M_y = \chi_{xy} E_x$) in the HDR is modified by anisotropy ratios [1]:

*   **Mass Anisotropy:**
    $$
    \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
    $$
*   **Coupling Anisotropy:**
    $$
    \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
    $$

where $\chi_0$ is a reference susceptibility. The susceptibility increases when $r_m$ and $r_\alpha$ exceed 1.

## 4. Parameter Dependencies

The model explicitly quantifies how the magnetization magnitude $|\mathbf{M}|$ and direction depend on physical parameters:

*   **Electric Field ($\mathbf{E}$):**
    *   **Magnitude:** Linearly proportional ($|\mathbf{M}| \propto |\mathbf{E}|$).
    *   **Direction:** Perpendicular to $\mathbf{E}$ in the plane ($\mathbf{M} \propto \hat{z} \times \mathbf{E}$) [1].
*   **Spin-Orbit Coupling ($\alpha$):**
    *   **HDR:** $M \propto \alpha$.
    *   **LDR:** $M \propto \sqrt{m^2 \alpha^2 + 2m E_F}$.
    *   Increasing $\alpha$ increases the susceptibility linearly in the HDR [1].
*   **Effective Mass ($m$):**
    *   $M \propto m$ in the HDR. In the anisotropic case, the ratio $r_m$ controls the enhancement.
*   **Fermi Energy ($E_F$):**
    *   **HDR:** Independent of $E_F$.
    *   **LDR:** Linear dependence for small $E_F$ [1].
*   **Transport Time ($\tau$):**
    *   Linearly proportional to $M$ (via susceptibility $\chi_0$) [1].
*   **Chirality ($\nu = \pm$):**
    *   The total magnetization arises from the difference in population shifts between the inner and outer Fermi surfaces. The outer surface dominates the contribution [1].

## 5. Explicit Graphics Specifications

To visualize the model results, the following graphics are specified. These descriptions define the mathematical functions and axes required for plotting, leaving the implementation of code to a developer.

### Graphic 1: Susceptibility vs. Chemical Potential
*   **X-Axis:** Chemical Potential $\mu$ (or $E_F$) in units of eV. Range: $0.01$ to $0.1$ eV.
*   **Y-Axis:** Edelstein Susceptibility $\chi_{xy}$ (units of $M/E$).
*   **Data Series:**
    1.  **High-Density Regime (HDR):** Plot a constant horizontal line defined by $y = \frac{\mu_b |e| \tau}{2\pi} m \alpha$.
    2.  **Low-Density Regime (LDR):** Plot a curve defined by $y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m \mu}$.
*   **Expected Outcome:** The HDR line remains flat, while the LDR curve increases with $\mu$ [1].

### Graphic 2: Susceptibility vs. Rashba Coupling Strength
*   **X-Axis:** Rashba Coupling $\alpha$ in units of eV Å. Range: $10 \times 10^{-3}$ to $100 \times 10^{-3}$ eV Å.
*   **Y-Axis:** Edelstein Susceptibility $\chi_{xy}$.
*   **Data Series:**
    *   Plot the linear function $y = C \cdot \alpha$, where $C = \frac{\mu_b |e| \tau m}{2\pi}$ (assuming HDR conditions).
*   **Expected Outcome:** A linear increase in susceptibility as $\alpha$ increases [1].

### Graphic 3: Anisotropy Enhancement
*   **X-Axis:** Anisotropy Ratio ($r_m$ or $r_\alpha$).
*   **Y-Axis:** Normalized Susceptibility $\chi_{xy}/\chi_0$.
*   **Data Series:**
    1.  **Mass Anisotropy:** Plot $y = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}$.
    2.  **Coupling Anisotropy:** Plot $y = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}$.
*   **Expected Outcome:** Susceptibility increases as ratios exceed 1, showing potential for boosted Edelstein response in anisotropic materials [1].

## 6. References

[1] I. Gaillardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712* (2025).

[2] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233 (1990).
# Mathematical Model for the Edelstein Effect in Rashba Fermions

This document provides a complete mathematical description of the model used to calculate the Edelstein effect (inverse spin-galvanic effect) for a Rashba fermion system. The model is constructed based on the Hamiltonian near the Gamma point of the Brillouin zone, derives the magnetization response to an applied electric field using Boltzmann transport theory, and analyzes the dependence on physical parameters such as chirality and spin-orbit coupling strength.

## 1. Theoretical Foundation and Hamiltonian

We begin by defining the effective Hamiltonian for a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (SOC). This system lacks inversion symmetry, typically due to structural asymmetry at an interface or surface.

### 1.1 Rashba Hamiltonian
Near the $\Gamma$ point ($k \approx 0$), the effective Hamiltonian $\hat{H}$ is given by:

$$
\hat{H} = \frac{\vec{p}^2}{2m} + \alpha_R \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$

Where:
*   $m$ is the effective carrier mass.
*   $\vec{p} = -i\hbar\nabla$ is the momentum operator.
*   $\alpha_R$ is the Rashba SOC strength parameter (units: energy $\times$ length).
*   $\hat{z}$ is the unit vector normal to the 2D plane.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ represents the vector of Pauli matrices.

### 1.2 Energy Dispersion and Eigenstates
The Hamiltonian yields two spin-split energy bands characterized by the chirality index $\nu = \pm 1$. The energy dispersion relation is:

$$
\mathcal{E}_\pm(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha_R k
$$

The corresponding eigenstates exhibit a specific spin-momentum locking. For a wavevector $\vec{k} = k(\cos\theta, \sin\theta, 0)$, the expectation value of the spin operator $\vec{\sigma}$ is:

$$
\langle \vec{\sigma} \rangle_k^\nu = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \nu \begin{pmatrix} \sin\theta \\ -\cos\theta \\ 0 \end{pmatrix}
$$

This equation shows that the electron spin lies strictly within the 2D plane and is perpendicular to the momentum vector $\vec{k}$. The sign of $\nu$ determines the chirality (clockwise or counter-clockwise rotation of spin relative to momentum).

## 2. Magnetization Dynamics (The Edelstein Effect)

The Edelstein effect describes the generation of a non-equilibrium spin density (magnetization) $\vec{M}$ in response to an applied electric field $\vec{E}$. We calculate this using the semi-classical Boltzmann transport equation within the relaxation time approximation.

### 2.1 Non-Equilibrium Distribution
In the presence of a weak electric field $\vec{E}$, the electron distribution function $f_\nu(\vec{k})$ deviates from the equilibrium Fermi-Dirac distribution $f^0(\mathcal{E})$. To first order in $\vec{E}$, the deviation is:

$$
\delta f_\nu(\vec{k}) = -e \tau (\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \left( -\frac{\partial f^0}{\partial \mathcal{E}} \right)
$$

Where:
*   $e$ is the elementary charge.
*   $\tau$ is the momentum relaxation time.
*   $\vec{v}_\nu(\vec{k}) = \frac{1}{\hbar} \nabla_{\vec{k}} \mathcal{E}_\nu(\vec{k})$ is the group velocity of band $\nu$.

At low temperatures ($T \to 0$), the derivative of the Fermi function becomes a delta function, $-\frac{\partial f^0}{\partial \mathcal{E}} \approx \delta[\mathcal{E}_\nu(k) - E_F]$, restricting the integral to the Fermi surface.

### 2.2 Induced Magnetization Formula
The magnetization $\vec{M}$ is the sum of the spin magnetic moments of the non-equilibrium carriers. Using the Bohr magneton $\mu_B$ and the spin expectation value derived in Section 1.2:

$$
\vec{M} = -\mu_B \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \, \delta f_\nu(\vec{k}) \, \langle \vec{\sigma} \rangle_k^\nu
$$

Substituting the expression for $\delta f_\nu(\vec{k})$:

$$
\vec{M} = \mu_B e \tau \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \, (\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \, \delta[\mathcal{E}_\nu(k) - E_F] \, \langle \vec{\sigma} \rangle_k^\nu
$$

## 3. Calculation of the Edelstein Susceptibility

We evaluate the integral for $\vec{M}$ to find the Edelstein susceptibility tensor $\chi_{ij}$, defined by $M_i = \sum_j \chi_{ij} E_j$.

### 3.1 Velocity and Jacobian Transformation
The group velocity is radial:
$$
\vec{v}_\nu(k) = \frac{1}{\hbar} \frac{\partial \mathcal{E}_\nu}{\partial k} \hat{k} = \frac{\hbar k}{m} \hat{k} \pm \frac{\alpha_R}{\hbar} \hat{k}
$$
Note that while the velocity differs slightly between bands, the integration over the Fermi circles depends on the density of states at $E_F$.

We convert the integral to polar coordinates $(k, \theta)$ and use the property of the delta function to integrate over energy magnitude $k$:
$$
\int \frac{k \, dk \, d\theta}{(2\pi)^2} \delta[\mathcal{E}_\nu(k) - E_F] (\dots) = \int_0^{2\pi} \frac{d\theta}{(2\pi)^2} \frac{k_F^\nu}{\hbar |\vec{v}_\nu(k_F^\nu)|} (\dots)
$$
where $k_F^\nu$ is the Fermi wavevector for band $\nu$ satisfying $\mathcal{E}_\nu(k_F^\nu) = E_F$.

### 3.2 Regimes of Operation
The result depends critically on whether the Fermi energy $E_F$ exceeds the band crossing point at the bottom of the upper band. The band crossing occurs at $k=0$ with energy 0. The minimum of the upper band ($\nu=-$) is at $k_{min} = m\alpha_R/\hbar^2$ with energy $E_{min} = -m\alpha_R^2 / (2\hbar^2)$. We define the characteristic energy scale $\Delta = m\alpha_R^2 / (2\hbar^2)$.

We distinguish two regimes:

**1. High-Density Regime (HDR):** $E_F > 0$ (or specifically $E_F$ is high enough that both bands are occupied).
In this case, both $\nu = +$ and $\nu = -$ Fermi surfaces exist. The contributions from both bands sum up.

**2. Low-Density Regime (LDR):** $E_F < 0$ (Only the lower band $\nu = +$ is occupied).

### 3.3 Explicit Susceptibility Calculation
Performing the angular integration for $\vec{E} = (E_x, E_y, 0)$, we utilize the spin texture $\langle \vec{\sigma} \rangle_k^+ = (\sin\theta, -\cos\theta, 0)$ and $\langle \vec{\sigma} \rangle_k^- = (-\sin\theta, \cos\theta, 0)$.

The magnetization components become:
$$
M_x \propto \int d\theta \, (E_x \cos\theta + E_y \sin\theta) (\nu \sin\theta)
$$
$$
M_y \propto \int d\theta \, (E_x \cos\theta + E_y \sin\theta) (-\nu \cos\theta)
$$

Using $\int_0^{2\pi} \cos^2\theta d\theta = \int_0^{2\pi} \sin^2\theta d\theta = \pi$ and $\int_0^{2\pi} \sin\theta \cos\theta d\theta = 0$, we find the tensor form:
$$
\vec{M} = \chi (\hat{z} \times \vec{E}) = \chi \begin{pmatrix} -E_y \\ E_x \\ 0 \end{pmatrix}
$$

The scalar susceptibility $\chi$ is derived by summing the density of states factors:

$$
\chi = \frac{\mu_B e \tau}{2\pi\hbar^2} \sum_{\nu=\pm} \nu \frac{m k_F^\nu \alpha_R}{|\hbar k_F^\nu/m \pm \alpha_R/\hbar|}
$$

Simplifying the velocity denominator $|\hbar k_F^\nu/m \pm \alpha_R/\hbar| = \frac{1}{m\hbar} |\hbar^2 k_F^\nu \pm m\alpha_R|$, and using the energy conservation $\frac{\hbar^2 (k_F^\nu)^2}{2m} \pm \alpha_R k_F^\nu = E_F$, one can show that $\hbar^2 k_F^\nu \pm m\alpha_R = \frac{2m E_F}{k_F^\nu}$. Thus the term simplifies to $\frac{m^2 k_F^\nu \alpha_R}{2m E_F} = \frac{m k_F^\nu \alpha_R}{2 E_F}$.

However, a more direct standard result for the Rashba model gives:

**For High-Density Regime (HDR):**
$$
\chi_{\text{HDR}} = \frac{\mu_B e \tau m \alpha_R}{2\pi \hbar^2}
$$
This is constant, independent of $E_F$.

**For Low-Density Regime (LDR):**
Only the lower band ($\nu=+1$) contributes. The Fermi wavevector is $k_F^+ = \frac{m}{\hbar^2}(\sqrt{\alpha_R^2 + \frac{2\hbar^2 E_F}{m}} - \alpha_R)$.
The susceptibility is:
$$
\chi_{\text{LDR}} = \frac{\mu_B e \tau m}{2\pi \hbar^2} \frac{\alpha_R}{\sqrt{1 - \frac{2m E_F}{m\alpha_R^2}}} \approx \frac{\mu_B e \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha_R^2 + 2m E_F}
$$
(Note: The exact form depends on the specific definition of the limit, but it scales with the Fermi wavevector $k_F$).

## 4. Model Output and Visualization Specifications

The model computes the magnetization vector $\vec{M}$ based on the inputs $\vec{E}$, $\alpha_R$, $m$, and $E_F$.

### 4.1 Direction of Magnetization
The direction of the induced magnetization is always perpendicular to the applied electric field in the plane:
$$
\hat{M} = \text{sgn}(\alpha_R) (\hat{z} \times \hat{E})
$$
If $\vec{E}$ points along $+x$, $\vec{M}$ points along $+y$ (for $\alpha_R > 0$).

### 4.2 Magnitude of Magnetization
$$
|\vec{M}| = \chi |\vec{E}|
$$
Where $\chi$ is selected based on the regime determined by $E_F$.

### 4.3 Parameter Dependencies
*   **Chirality ($\alpha_R$):** The magnitude scales linearly with $\alpha_R$ in the HDR. The sign of $\alpha_R$ determines the rotation direction (chirality).
*   **Fermi Energy ($E_F$):** In the HDR, $|\vec{M}|$ is independent of $E_F$. In the LDR, $|\vec{M}|$ increases as $E_F$ increases (approaching the band crossing).
*   **Electric Field ($\vec{E}$):** Linear response.

### 4.4 Explicit Graphics Descriptions
The model generates the following graphical representations:

**Figure 1: Magnetization vs. Electric Field Magnitude**
*   **Type:** Line Plot
*   **X-axis:** Electric Field Magnitude $|\vec{E}|$ (V/m)
*   **Y-axis:** Magnetization Magnitude $|\vec{M}|$ (A/m)
*   **Curves:** Two lines plotted for comparison:
    1.  High-Density Regime (HDR) parameters (Linear slope).
    2.  Low-Density Regime (LDR) parameters (Linear slope with different intercept/slope).
*   **Interpretation:** Demonstrates the linear relationship $M \propto E$ and the difference in susceptibility between regimes.

**Figure 2: Magnetization Direction Vector Field**
*   **Type:** Quiver Plot (Vector Field)
*   **Domain:** A 2D grid representing the Electric Field plane ($E_x, E_y$).
*   **Vectors:**
    *   Input vectors (Black arrows) representing the direction of $\vec{E}$.
    *   Output vectors (Blue arrows) representing the direction of $\vec{M}$.
*   **Visual Feature:** Blue arrows should be rotated 90 degrees counter-clockwise relative to the black arrows (for $\alpha_R > 0$).
*   **Interpretation:** Visualizes the cross-product relationship $\vec{M} \propto \hat{z} \times \vec{E}$.

**Figure 3: Susceptibility vs. Spin-Orbit Coupling Strength**
*   **Type:** Line Plot
*   **X-axis:** Rashba Parameter $\alpha_R$ (eV$\cdot$m)
*   **Y-axis:** Edelstein Susceptibility $\chi$ (A$\cdot$s/m$^2$ or equivalent units).
*   **Curve:** Linear increase of $\chi$ with $\alpha_R$.
*   **Interpretation:** Shows that stronger spin-orbit coupling leads to a stronger spin-charge conversion efficiency.

## 5. Step-by-Step Model Execution Summary

1.  **Initialization:** Define constants ($\mu_B, e, \hbar, m$) and model parameters ($\alpha_R, \tau, E_F$).
2.  **Regime Check:** Calculate the characteristic energy $\Delta = m\alpha_R^2 / (2\hbar^2)$. Compare $E_F$ to determine if the system is in HDR or LDR.
3.  **Susceptibility Calculation:**
    *   If HDR: Calculate $\chi = \frac{\mu_B e \tau m \alpha_R}{2\pi \hbar^2}$.
    *   If LDR: Calculate $\chi = \frac{\mu_B e \tau \sqrt{m^2 \alpha_R^2 + 2m E_F}}{2\pi \hbar^2}$.
4.  **Field Input:** Accept an Electric Field vector $\vec{E} = (E_x, E_y)$.
5.  **Magnetization Computation:**
    *   Compute $M_x = -\chi E_y$.
    *   Compute $M_y = \chi E_x$.
    *   Compute Magnitude $|\vec{M}| = \sqrt{M_x^2 + M_y^2}$.
6.  **Visualization:** Generate the plots specified in Section 4.4 using the computed values across ranges of $E$ and $\alpha_R$.

## References
[1] I. Gaiardoni et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models", *arXiv:2503.20712* (2025).
[2] T. Funato & M. Matsuo, "Acoustic Rashba–Edelstein effect", *arXiv:2107.03115* (2021).
[3] M. Ezawa, "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", *arXiv:2501.01888* (2025).
[4] S. Leiva M. et al., "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction", *arXiv:2307.02872* (2024).
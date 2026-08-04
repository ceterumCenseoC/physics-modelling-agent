# Mathematical Model for the Edelstein Effect in Rashba Fermions

This document provides a complete mathematical description of a model to calculate the Edelstein effect (also known as the current-induced spin polarization) for a Rashba fermion system at the $\Gamma$ point of the Brillouin zone. The model derives the magnetization response to an applied electric field and analyzes its dependence on physical parameters such as chirality, Fermi velocity, and spin-orbit coupling strength.

## 1. Theoretical Framework

### 1.1 Hamiltonian and Energy Dispersion

We consider a two-dimensional electron gas (2DEG) confined to the $xy$-plane with structural inversion asymmetry. The effective single-particle Hamiltonian near the $\Gamma$ point, incorporating Rashba spin-orbit coupling (RSOC), is given by [1]:

$$
\hat{H} = \frac{\hat{p}^2}{2m} + \alpha \hat{z} \cdot (\hat{\vec{p}} \times \vec{\sigma})
$$

where:
*   $m$ is the effective carrier mass.
*   $\hat{\vec{p}} = -i\hbar\nabla$ is the momentum operator.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the vector of Pauli matrices.
*   $\hat{z}$ is the unit vector normal to the plane.
*   $\alpha$ is the Rashba spin-orbit coupling constant (strength).

In momentum space, where $\hat{\vec{p}} \rightarrow \hbar \vec{k}$, the Hamiltonian becomes:

$$
\hat{H}(\vec{k}) = \frac{\hbar^2 k^2}{2m} \mathbb{I} + \alpha (k_y \sigma_x - k_x \sigma_y)
$$

Diagonalizing this Hamiltonian yields two chiral energy bands indexed by $\nu = \pm$:

$$
E_\pm(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha k
$$

Here, $k = |\vec{k}| = \sqrt{k_x^2 + k_y^2}$.

### 1.2 Spin-Momentum Locking and Eigenstates

The eigenstates of the Rashba Hamiltonian are spinors locked to the momentum direction. The spin expectation value for an electron in band $\nu$ with momentum $\vec{k}$ is [1]:

$$
\langle \vec{\sigma} \rangle_k^\nu = \frac{\nu}{k} \begin{pmatrix} k_y \\ -k_x \\ 0 \end{pmatrix} = \nu \begin{pmatrix} \sin\theta \\ -\cos\theta \\ 0 \end{pmatrix}
$$

where $\theta = \arctan(k_y/k_x)$ is the azimuthal angle. This relation describes the **spin-momentum locking**:
*   The spin lies entirely in the $xy$-plane.
*   The spin is perpendicular to the momentum vector $\vec{k}$.
*   The chirality $\nu$ determines the winding direction (clockwise or counter-clockwise).

## 2. Model Derivation: The Edelstein Effect

The Edelstein effect describes the generation of a non-equilibrium magnetization (spin density) $\vec{M}$ induced by a DC electric field $\vec{E}$. We derive this using semiclassical Boltzmann transport theory within the relaxation time approximation [1, 3].

### 2.1 Non-Equilibrium Distribution Function

In the presence of a static electric field $\vec{E}$, the distribution function $f_{\vec{k}}^\nu$ deviates from the equilibrium Fermi-Dirac distribution $f_0(E)$. To first order in $\vec{E}$:

$$
f_{\vec{k}}^\nu \approx f_0(E_\nu(k)) - e\tau \left( -\frac{\partial f_0}{\partial E} \right) (\vec{v}_\nu(\vec{k}) \cdot \vec{E})
$$

where:
*   $e$ is the elementary charge (absolute value $|e|$).
*   $\tau$ is the momentum relaxation time (assumed constant).
*   $\vec{v}_\nu(\vec{k}) = \frac{1}{\hbar} \nabla_{\vec{k}} E_\nu(\vec{k})$ is the group velocity.

The group velocity for the Rashba bands is:

$$
\vec{v}_\nu(\vec{k}) = \frac{\hbar \vec{k}}{m} \hat{k} + \frac{\nu \alpha}{\hbar} \hat{t}
$$

where $\hat{k} = \vec{k}/k$ is the radial unit vector and $\hat{t} = \hat{z} \times \hat{k} = (-\sin\theta, \cos\theta)$ is the tangential unit vector. However, for the integration in the next step, it is often sufficient to use the dominant term $\vec{v} \approx \frac{\hbar \vec{k}}{m}$ or strictly calculate the shift.

The deviation from equilibrium $\delta f = f - f_0$ corresponds to a rigid shift of the Fermi surface in momentum space by $\delta \vec{k} = -e\tau \vec{E}/\hbar$.

### 2.2 Calculating Magnetization

The induced magnetization (spin density) is defined as the sum of spin expectation values weighted by the non-equilibrium distribution function:

$$
\vec{M} = -\mu_B \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \left( f_{\vec{k}}^\nu - f_0(E_\nu(k)) \right) \langle \vec{\sigma} \rangle_k^\nu
$$

Substituting the expression for $\delta f$:

$$
\vec{M} = \mu_B |e| \tau \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \left( -\frac{\partial f_0}{\partial E} \right) (\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \langle \vec{\sigma} \rangle_k^\nu
$$

At low temperatures, $-\partial f_0/\partial E \approx \delta(E - E_F)$. This restricts the integral to the Fermi surfaces. Using the identity $\int d^2k (\dots) = \int k dk \int_0^{2\pi} d\theta (\dots)$ and noting that $E_F$ is constant on the Fermi contour, we obtain:

$$
\vec{M} = \frac{\mu_B |e| \tau}{(2\pi)^2} \sum_{\nu=\pm} \oint_{E_\nu(k)=E_F} \frac{k}{\hbar |\vec{v}_\nu|} (\vec{v}_\nu \cdot \vec{E}) \langle \vec{\sigma} \rangle_k^\nu dl
$$

where $dl = k d\theta$ is the line element.

## 3. Model Results: Magnitude and Direction

We evaluate the integral for two distinct electronic density regimes determined by the Fermi energy $E_F$.

### 3.1 High-Density Regime (HDR)

This regime occurs when the Fermi energy is large enough to occupy both Rashba bands ($E_F > 0$ in this shifted coordinate system, or specifically $E_F > m\alpha^2/2$ in standard coordinates).

In this case, the contributions from both bands $\nu = +$ and $\nu = -$ must be summed. The integral yields a magnetization strictly perpendicular to the applied electric field [1]:

$$
\vec{M} = \lambda_{EE}^{\text{HDR}} (\hat{z} \times \vec{E})
$$

where the Edelstein susceptibility $\lambda_{EE}^{\text{HDR}}$ is:

$$
\lambda_{EE}^{\text{HDR}} = \frac{\mu_B |e| \tau m \alpha}{2\pi \hbar^2}
$$

**Directionality:**
If $\vec{E} = E \hat{x}$, then $\vec{M} = \lambda_{EE}^{\text{HDR}} E \hat{y}$.
If $\vec{E}$ is rotated by an angle $\phi$ in the plane, $\vec{M}$ rotates by the same angle $\phi$, maintaining orthogonality.

### 3.2 Low-Density Regime (LDR)

This regime occurs when only the lower band ($\nu = +$) is occupied ($E_F < 0$ or small positive values such that only the inner circle exists).

The susceptibility becomes dependent on the Fermi energy [1]:

$$
\lambda_{EE}^{\text{LDR}} = \frac{\mu_B |e| \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha^2 + 2m E_F}
$$

Near the band bottom ($E_F \approx -m\alpha^2/2$), the Fermi wavevector $k_F$ approaches zero, and the magnetization vanishes. As $E_F$ increases towards the transition point, $\lambda_{EE}$ increases.

## 4. Dependence on Model Parameters

The behavior of the Edelstein effect is controlled by several key physical parameters:

*   **Spin-Orbit Coupling Strength ($\alpha$):**
    *   In the **HDR**, $M \propto \alpha$. The spin splitting is linear in $\alpha$, and the net spin imbalance increases with stronger coupling.
    *   In the **LDR**, $M \propto \sqrt{\alpha^2 + E_F/m}$.
    *   *Sign of $\alpha$:* Reversing the sign of $\alpha$ flips the chirality of the eigenstates, reversing the direction of $\vec{M}$ (i.e., $\vec{M} \propto -\alpha$).

*   **Fermi Velocity ($v_F$) and Effective Mass ($m$):**
    *   The Fermi velocity is defined as $v_F = \frac{1}{\hbar} \frac{dE}{dk}$.
    *   In the **HDR**, the susceptibility scales linearly with the effective mass: $\lambda_{EE} \propto m$. A heavier mass implies a higher density of states at the Fermi level, leading to a larger spin accumulation for the same electric field.
    *   The shift of the Fermi surface is $\delta k = -eE\tau/\hbar$. The velocity scales this shift into an energy/current.

*   **Chirality ($\nu$):**
    *   The effect arises from the difference in population of spin states on the shifted Fermi surface.
    *   In the **HDR**, contributions from $\nu = +$ and $\nu = -$ partially cancel or add depending on the specific details of the velocity projection, but in the standard Rashba model, they sum to give the result in Section 3.1.
    *   The "handedness" of the system is fixed by the sign of $\alpha$.

*   **Relaxation Time ($\tau$):**
    *   The magnitude of the magnetization is directly proportional to $\tau$: $M \propto \tau$. Longer scattering times allow for a larger non-equilibrium shift $\delta k$ before momentum is relaxed.

## 5. Explicit Graphics Descriptions

To visualize the model, the following graphics should be generated based on the equations derived above.

### 5.1 Fermi Surface Shift and Spin Texture

*   **Concept:** Illustrate the microscopic origin of the effect.
*   **Plot Elements:**
    *   Draw two concentric circles in the $k_x$-$k_y$ plane representing the Fermi contours for the inner ($\nu=+$) and outer ($\nu=-$) bands.
    *   Draw arrows (vectors) tangent to these circles representing the spin expectation value $\langle \vec{\sigma} \rangle_k^\nu$. The inner circle arrows should rotate one way, and the outer circle arrows the other (opposite chirality).
    *   Indicate an applied Electric Field $\vec{E}$ (e.g., pointing in $+x$ direction).
    *   Show the Fermi circles shifted by $\Delta \vec{k} = -e\tau\vec{E}/\hbar$ (dashed lines).
    *   Highlight the region where the shifted distribution overlaps with the unshifted one. The net magnetization arises from the imbalance of spins in these regions (excess of spins pointing in $+y$ vs $-y$).
*   **Mathematical Basis:** Section 1.2 and 2.1.

### 5.2 Magnetization vs. Electric Field Magnitude

*   **Concept:** Demonstrate the linear response regime.
*   **Plot Elements:**
    *   X-axis: Electric Field Magnitude $E$.
    *   Y-axis: Magnetization Magnitude $M$ (specifically $M_y$ if $E = E_x$).
    *   **Curve:** A straight line passing through the origin with slope $\lambda_{EE}$.
    *   **Label:** Identify the slope as the Edelstein susceptibility.
*   **Mathematical Basis:** Equation $\vec{M} = \lambda_{EE} (\hat{z} \times \vec{E})$.

### 5.3 Susceptibility vs. Rashba Strength ($\alpha$)

*   **Concept:** Show how the spin-orbit coupling tunes the effect.
*   **Plot Elements:**
    *   X-axis: Rashba parameter $\alpha$.
    *   Y-axis: Edelstein susceptibility $\lambda_{EE}$.
    *   **Curve 1 (HDR):** A line starting from the origin increasing linearly ($\lambda \propto \alpha$). This applies for fixed high $E_F$.
    *   **Curve 2 (LDR):** A curve starting from $\lambda \approx 0$ (at $\alpha \to 0$) and increasing.
    *   **Transition:** Indicate the critical point where the Fermi level touches the bottom of the upper band.
*   **Mathematical Basis:** Section 3.1 and 3.2 equations.

### 5.4 Directional Response (Vector Field)

*   **Concept:** Visualize the orthogonal relationship between $\vec{E}$ and $\vec{M}$.
*   **Plot Elements:**
    *   A central point representing the sample.
    *   A set of arrows representing the Electric Field $\vec{E}$ pointing in various directions in the plane (e.g., at $0^\circ, 45^\circ, 90^\circ$).
    *   Corresponding arrows for Magnetization $\vec{M}$ rotated by $90^\circ$ relative to $\vec{E}$.
*   **Mathematical Basis:** $\vec{M} \propto \hat{z} \times \vec{E}$.

## References

[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712* (2025).
[2] A. C. Zulkoskey, R. Dick, and K. Tanaka, "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface," *arXiv:1912.01804* (2019).
[3] S. Leiva M., J. Henk, I. Mertig, and A. Johansson, "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction," *arXiv:2307.02872* (2024).
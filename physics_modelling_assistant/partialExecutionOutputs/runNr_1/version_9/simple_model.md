

# Mathematical Model for the Edelstein Effect in Rashba Fermions

This document provides a complete mathematical description of the model used to calculate the Edelstein effect for a Rashba fermion at the $\Gamma$-point of the Brillouin zone. The model computes the induced magnetization magnitude and direction resulting from an applied electric field, accounting for relevant physical parameters such as chirality, Fermi velocity, and spin-orbit coupling strength.

## 1. Hamiltonian and Band Structure at the $\Gamma$-Point

The physical system is defined as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). At the center of the Brillouin zone ($\Gamma$-point, where $\vec{k}=0$), the system is governed by the Rashba Hamiltonian [1], [3], [4]:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$

Here, the parameters are defined as follows:
*   $m$: The effective carrier mass.
*   $\alpha$: The Rashba spin-orbit coupling strength.
*   $\vec{p} = -i\hbar\nabla$: The momentum operator.
*   $\vec{\sigma}$: The vector of Pauli matrices representing spin.
*   $\hat{z}$: The unit vector perpendicular to the 2D plane [1].

Solving the eigenvalue problem for this Hamiltonian yields the energy dispersion relation for the two chiral branches, denoted by $\nu = \pm$ [1], [3]:

$$
E_{\pm}(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha k
$$

where $k = |\vec{k}|$. At the $\Gamma$-point ($k=0$), the bands cross. Due to the RSOC, the Fermi surfaces split into an inner contour ($\nu=+$) and an outer contour ($\nu=-$). The energy minimum occurs at momentum $k_0 = m\alpha/\hbar^2$ [1], [3].

## 2. Spin Texture and Chirality

The eigenstates of the Rashba Hamiltonian exhibit *spin-momentum locking*. This means the electron spin orientation is locked perpendicular to its momentum vector. The expectation value of the spin operator $\langle \vec{\sigma} \rangle$ for a state with momentum $\vec{k}$ (defined by angle $\theta_k$) is given by [1]:

$$
\langle \vec{\sigma} \rangle_{\vec{k}}^{\pm} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta_k) \\ \mp \cos(\theta_k) \\ 0 \end{pmatrix}
$$

The index $\nu = \pm$ denotes the **chirality** (or helicity) of the Fermi surfaces. The inner and outer circles possess opposite spin textures, which is crucial for the emergence of the Edelstein effect [1], [6].

## 3. Calculation of the Edelstein Magnetization

When an in-plane electric field $\vec{E}$ is applied, it drives an electric current. In momentum space, this shifts the Fermi surfaces in the direction opposite to the field [1], [3]. Using semiclassical Boltzmann transport theory in the relaxation time approximation, the expectation value of the total magnetization (spin density) to first order in the electric field is calculated as [1], [2]:

$$
\vec{M} = -\mu_B \sum_{\vec{k},\nu} |e|(\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \delta [E_\nu(\vec{k}) - E_F] \langle\vec{\sigma}\rangle_{\vec{k},\nu}
$$

Where:
*   $\mu_B$: The Bohr magneton.
*   $e$: The elementary charge.
*   $\vec{v}_\nu(\vec{k}) = \nabla_k E_\nu(\vec{k})/\hbar$: The group velocity.
*   $\tau$: The transport lifetime (incorporated into the mean free path) [1].
*   $E_F$: The Fermi energy.

Evaluating this integral yields an Edelstein magnetization that is strictly **perpendicular** to the applied electric field [1]:

$$
\vec{M} = \lambda_E (\hat{z} \times \vec{E})
$$

Here, $\lambda_E$ is the Edelstein susceptibility coefficient, which depends on the electronic density regime.

### 3.1 High-Density Regime (HDR)
When the Fermi energy $E_F$ is sufficiently high such that both chiral bands are occupied ($E_F \gg m\alpha^2/2m$), the spin density becomes constant and independent of $E_F$ [1]:

$$
M_{\text{HDR}} = \frac{|e|\tau \mu_B m \alpha}{2\pi} |\vec{E}|
$$

### 3.2 Low-Density Regime (LDR)
When only the lowest energy band is occupied ($E_F < m\alpha^2/2m$), the spin density depends explicitly on the Fermi energy [1]:

$$
M_{\text{LDR}} = \frac{|e|\tau \mu_B}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} |\vec{E}|
$$

## 4. Dependence on Model Parameters

The model predicts specific dependencies of the magnetization $\vec{M}$ on various physical parameters:

*   **Electric Field ($\vec{E}$):** The magnetization magnitude scales **linearly** with $|\vec{E}|$ in the linear response regime. The direction of $\vec{M}$ is always rotated by $90^\circ$ relative to $\vec{E}$ in the counter-clockwise direction (defined by the cross product $\hat{z} \times \vec{E}$) [1], [3].
*   **Spin-Orbit Coupling Strength ($\alpha$):** In the HDR, the Edelstein response scales **linearly** with $\alpha$. Increasing $\alpha$ directly boosts the Edelstein susceptibility [1], [3]. In the LDR, it scales with the square root of $\alpha^2$.
*   **Effective Mass ($m$):** The magnetization scales **linearly** with the effective mass $m$ in the HDR, reflecting the density of states at the Fermi level [1].
*   **Fermi Velocity / Chemical Potential:** In the HDR, the Edelstein effect saturates and becomes independent of the Fermi velocity (or $E_F$). In the LDR, it increases approximately linearly with $E_F$ for small values near the band crossing [1].
*   **Chirality:** The net magnetization arises from the asymmetry in the population of the two chiral Fermi surfaces ($\nu = \pm$). The shift $\delta k$ induced by $\vec{E}$ creates a spin imbalance because the inner and outer Fermi circles have different Fermi velocities and opposing spin textures [1].

## 5. Visualization Protocol

To explicitly visualize the results of this model, the following graphical representations are defined. These graphics illustrate the mathematical relationships derived above.

### Figure 1: Magnetization vs. Electric Field (HDR)
*   **X-Axis:** Electric Field Magnitude $|\vec{E}|$ (Units: $10^4$ V/m).
*   **Y-Axis:** Magnetization Magnitude $M$ (Units: $10^{-30}$ J/T).
*   **Curve:** A linear plot originating from $(0,0)$.
*   **Slope:** Determined by $\frac{|e|\tau \mu_B m \alpha}{2\pi}$.
*   **Interpretation:** Demonstrates the linear response of the Edelstein effect in the high-density regime.

### Figure 2: Magnetization vs. Rashba Parameter $\alpha$ (HDR)
*   **X-Axis:** Rashba Coupling Strength $\alpha$ (Units: $10^{-22}$ J m).
*   **Y-Axis:** Magnetization Magnitude $M$ (Units: $10^{-30}$ J/T).
*   **Curve:** A linear plot originating from $(0,0)$.
*   **Interpretation:** Shows that stronger spin-orbit coupling yields a larger induced magnetization for a fixed electric field.

### Figure 3: Magnetization vs. Fermi Energy $E_F$ (LDR)
*   **X-Axis:** Fermi Energy $E_F$ (Units: $10^{-19}$ J).
*   **Y-Axis:** Magnetization Magnitude $M$ (Units: $10^{-30}$ J/T).
*   **Curve:** A square-root function shape starting from a non-zero intercept at $E_F=0$ (specifically proportional to $\sqrt{m^2 \alpha^2}$).
*   **Interpretation:** Illustrates the dependence on chemical potential when only the lower band is occupied.

### Figure 4: Spin Texture around $\Gamma$
*   **X-Axis:** Momentum $k_x$.
*   **Y-Axis:** Momentum $k_y$.
*   **Visual:** A quiver plot (vector field).
*   **Vectors:** At each point $(k_x, k_y)$, a vector represents $\langle \vec{\sigma} \rangle_{\vec{k}}^{-}$.
*   **Pattern:** Vectors should form a vortex-like pattern tangential to circles centered at the origin, representing the spin-momentum locking of the outer band ($\nu=-$) [1], [6].

## 6. References

[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," arXiv:2503.20712v1 [cond-mat.mes-hall], 2025.
[2] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233-235 (1990).
[3] A. C. Zulkoskey, R. Dick, and K. Tanaka, "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface," arXiv:1912.01804v1 [cond-mat.mes-hall], 2019.
[4] Yu. A. Bychkov and É. I. Rashba, "Properties of a 2d electron gas with lifted spectral degeneracy," *JETP Lett.* **39**, 78 (1984).
[5] E. I. Rashba, "Spin-orbit coupling in condensed matter physics," *Sov. Phys. Solid State* **2**, 1109 (1960).
[6] A. Johansson, J. Henk, and I. Mertig, "Theoretical aspects of the edelstein effect for anisotropic two-dimensional electron gas and topological insulators," *Physical Review B* **93**, 195440 (2016).
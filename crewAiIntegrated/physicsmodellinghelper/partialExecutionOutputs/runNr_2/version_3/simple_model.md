

# Mathematical Model for the Rashba-Edelstein Effect

This document provides a complete mathematical description for calculating the Edelstein effect in a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (SOC) at the $\Gamma$ point of the Brillouin zone. The model computes the induced magnetization magnitude and direction resulting from an applied electric field, analyzing dependencies on system parameters.

## 1. System Hamiltonian and Energy Dispersion

The physical system is defined by a Hamiltonian that includes kinetic energy and a Rashba spin-orbit coupling term due to broken structural inversion symmetry. The effective Hamiltonian is given by:

$$
\hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha_R \hat{z} \cdot (\vec{k} \times \vec{\sigma})
$$

where:
*   $m$ is the effective carrier mass.
*   $\alpha_R$ is the Rashba spin-orbit coupling strength.
*   $\vec{k} = (k_x, k_y)$ is the in-plane quasimomentum.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices.
*   $\hat{z}$ is the unit vector normal to the 2D plane [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eq. 1].

Diagonalizing this Hamiltonian yields two spin-split energy branches:

$$
E_\pm(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha_R k
$$

These branches correspond to the inner ($+$) and outer ($-$) Fermi surfaces, characterized by distinct chiral states [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Sec. DEE in Isotropic Rashba Model].

## 2. Spin Texture and Expectation Values

The eigenstates of the Rashba Hamiltonian exhibit momentum-dependent spin polarization (spin-momentum locking). The expectation value of the spin operator $\langle \vec{\sigma} \rangle_k^\nu$ for a band $\nu \in \{+, -\}$ is:

$$
\langle \vec{\sigma} \rangle_k^\pm = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
$$

where $\theta$ is the azimuthal angle of $\vec{k}$. The spin polarization lies strictly in the $xy$-plane and is tangential to the constant-energy circles. The inner and outer Fermi surfaces possess opposite chirality [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eq. 3].

## 3. Non-Equilibrium Distribution Function

To calculate the Edelstein effect, we apply a static external electric field $\vec{E}$. Using the linearized Boltzmann equation in the relaxation time approximation, the non-equilibrium distribution function $f(\vec{k})$ is:

$$
f(\vec{k}) = f_0(E) - e\tau (\vec{v}_k \cdot \vec{E}) \frac{\partial f_0}{\partial E}
$$

where:
*   $\tau$ is the transport relaxation time.
*   $e$ is the elementary charge.
*   $\vec{v}_k = \frac{1}{\hbar}\nabla_k E(k)$ is the group velocity.
*   $f_0(E)$ is the equilibrium Fermi-Dirac distribution.

This perturbation creates an imbalance in the population of states with opposite spins, leading to a net magnetization [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eq. 2].

## 4. Calculation of Magnetization

The induced magnetization (spin density) per unit area, $\vec{M}$, is obtained by integrating the spin expectation values weighted by the non-equilibrium distribution over the Fermi surface:

$$
\vec{M} = -\mu_B \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \left[ e\tau (\vec{v}_k^\nu \cdot \vec{E}) \right] \delta(E_\nu(k) - E_F) \langle \vec{\sigma} \rangle_k^\nu
$$

where $\mu_B$ is the Bohr magneton. Evaluating this integral yields analytical solutions dependent on the Fermi energy $E_F$ relative to the spin-orbit splitting energy scale.

### 4.1 High-Density Regime (HDR)
When both Rashba bands are occupied ($E_F > \alpha_R^2 m / 2\hbar^2$), the contributions from the inner and outer bands partially cancel, resulting in a magnetization independent of $E_F$:

$$
\vec{M}_{\text{HDR}} = \frac{e \mu_B m \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E})
$$

The magnitude scales linearly with the Rashba parameter $\alpha_R$ and the applied field magnitude $|\vec{E}|$ [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eq. 8].

### 4.2 Low-Density Regime (LDR)
When only the lower-energy band ($\nu = -$) is occupied ($E_F < \alpha_R^2 m / 2\hbar^2$), the magnetization depends on the Fermi energy:

$$
\vec{M}_{\text{LDR}} = \frac{e \mu_B \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha_R^2 + 2m E_F} \, (\hat{z} \times \vec{E})
$$

Near the band crossing ($E_F \to 0$), this reduces to the linear form seen in the HDR, showing a linear increase with $E_F$ initially [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eqs. 9-10].

## 5. Direction and Magnitude Analysis

### 5.1 Direction
For both regimes, the direction of the induced magnetization is strictly perpendicular to the applied electric field and lies within the 2D plane:
$$
\text{Direction}(\vec{M}) = \text{Direction}(\hat{z} \times \vec{E})
$$
If $\vec{E}$ is along the $+x$ axis, $\vec{M}$ points along the $+y$ axis (assuming $\alpha_R > 0$).

### 5.2 Parameter Dependence
The magnitude $|\vec{M}|$ depends on the physical parameters as follows:

| Parameter | Dependence of $|\vec{M}|$ | Physical Origin |
| :--- | :--- | :--- |
| **Rashba strength ($\alpha_R$)** | Linear in HDR; $\propto \sqrt{\alpha_R^2 + E_F}$ in LDR | Determines spin-splitting magnitude and Fermi contour offset $k_0 = m\alpha_R/\hbar^2$ |
| **Relaxation time ($\tau$)** | Linear ($M \propto \tau$) | Scattering rate controls drift velocity and non-equilibrium population imbalance |
| **Effective mass ($m$)** | Linear in HDR; enters via density of states & velocity | Modifies Fermi velocity $v_F$ and kinetic energy dispersion |
| **Chemical potential ($E_F$)** | Constant in HDR; linear increase in LDR near $\Gamma$ | Determines which chiral bands contribute to the spin sum |
| **Chirality / Band index ($\nu$)** | Sign flips between inner/outer bands | Opposite spin textures cause partial cancellation in HDR, yielding constant net $M$ |
| **Electric field ($\vec{E}$)** | Linear ($M \propto |\vec{E}|$) | Drifts Fermi surfaces, breaking $\vec{k} \leftrightarrow -\vec{k}$ symmetry |

## 6. Explicit Graphics Specifications

To visualize the results of this model, the following graphics should be generated based on the analytical formulas derived above.

### 6.1 Susceptibility vs. Chemical Potential
*   **X-axis:** Chemical potential $\mu$ (in eV).
*   **Y-axis:** Edelstein susceptibility $\chi_{xy}/\chi_0$ (dimensionless).
*   **Expected Trend:** The curve should show a linear rise starting from $\mu=0$ (LDR) and plateau at a constant value when $\mu > \alpha_R^2 m / 2\hbar^2$ (HDR). Higher $\alpha_R$ shifts the plateau onset to higher $\mu$ and increases the saturation value [Source: Fig. 2 & Fig. 3, *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*].

### 6.2 Susceptibility vs. Rashba Parameter
*   **X-axis:** Rashba parameter $\alpha$ (in eV·Å).
*   **Y-axis:** Edelstein susceptibility $\chi_{xy}/\chi_0$.
*   **Expected Trend:** A strictly linear increase in the HDR. The slope of this line is proportional to the product of effective mass and relaxation time ($m\tau$) [Source: Fig. 3 right panel, *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*].

### 6.3 Anisotropy Boost
*   **X-axis:** Anisotropy ratios $r_m = m_y/m_x$ or $r_\alpha = \alpha_y/\alpha_x$.
*   **Y-axis:** Edelstein susceptibility $\chi_{xy}/\chi_0$.
*   **Expected Trend:** Monotonic increase for ratios $r > 1$, showing that anisotropy can boost the Edelstein response. Curves should show saturation behavior for large $r_\alpha$ [Source: Fig. 5 & Fig. 6, *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*].

### 6.4 Vector Diagram (Field Geometry)
*   **Layout:** 2D plane ($xy$).
*   **Elements:**
    *   Vector $\vec{E}$ drawn along the $+x$ direction.
    *   Induced current $\vec{J}$ parallel to $\vec{E}$.
    *   Magnetization $\vec{M}$ drawn along the $+y$ direction (for $\alpha_R > 0$).
    *   Fermi circles drawn in the $k$-space showing counter-rotating spin textures for inner and outer bands.
*   **Purpose:** Illustrate the geometric relationship $\vec{M} \propto \hat{z} \times \vec{E}$ [Source: Fig. 1, *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*].

## 7. Scientific Citations

1.  **V. M. Edelstein**, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems", *Solid State Communications* **73**, 233 (1990). [Foundational EE prediction]
2.  **E. I. Rashba & G. E. Pikus**, "Gyromagnetic and magnetic anisotropies of electrons in structures of low dimensionality", *Phys. Rev. B* **20**, 3211 (1979); **Y. A. Bychkov & E. I. Rashba**, "Properties of a 2d electron gas with lifted spectral degeneracy", *JETP Lett.* **39**, 78 (1984). [Rashba Hamiltonian]
3.  **I. Gaiardoni et al.**, "Edelstein Effect in Isotropic and Anisotropic Rashba Models", *arXiv:2503.20712* (2025). [Primary source for Eqs. 1-12, HDR/LDR regimes, anisotropy ratios, and susceptibility plots]
4.  **S. Leiva M. et al.**, "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction", *arXiv:2307.02872* (2024). [Boltzmann linear response formalism, susceptibility tensor definition]
5.  **M. Ezawa**, "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", *arXiv:2501.01888* (2025). [General magnetization integral formulation, vector product derivation]
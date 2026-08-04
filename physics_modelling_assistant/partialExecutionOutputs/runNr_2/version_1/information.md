

# Model for the Edelstein Effect in a Rashba Fermion System

The following sections provide the theoretical framework, analytical expressions, and graphical guidelines for calculating the Direct Edelstein Effect (DEE) in a two-dimensional Rashba electron gas. The model computes the current-induced spin magnetization arising from the shift of the Fermi surfaces under an applied electric field.

## 1. Theoretical Framework and Hamiltonian

The system is described by an isotropic Rashba Hamiltonian at the $\Gamma$ point of the Brillouin zone, which accounts for kinetic energy and Rashba spin-orbit coupling (RSOC) [1, 2]:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\hat{p} \times \vec{\sigma})
$$

Where:
*   $p$ is the electron momentum operator.
*   $m$ is the effective carrier mass.
*   $\alpha$ is the Rashba spin-orbit coupling strength.
*   $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices.
*   $\hat{z}$ is the unit vector perpendicular to the 2D plane.

This Hamiltonian lifts the spin degeneracy, resulting in two chiral Fermi surfaces with eigenenergies $E^\pm_k = \frac{\hbar^2 k^2}{2m} \pm \alpha k$ [4]. The spin expectation value for an electron in state $k$ with helicity $\nu = \pm$ is tangential to the Fermi circle [1]:

$$
\langle \vec{\sigma} \rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
$$

## 2. Magnetization Calculation: Magnitude and Direction

When an external electric field $\vec{E}$ is applied, the Fermi surfaces shift by $\delta \vec{k}$, creating a non-equilibrium spin density (magnetization) $\vec{M}$. 

### Direction
The induced magnetization is always in-plane and perpendicular to the applied electric field [1]:

$$
\vec{M} \propto \hat{z} \times \vec{E}
$$

If $\vec{E} = E_x \hat{x}$, the magnetization is along $\hat{y}$.

### Magnitude
The magnitude depends on the Fermi energy $E_F$ relative to the band splitting. We define the characteristic wavevector $k_0 = m\alpha/\hbar$ [1].

#### High-Density Regime (HDR)
When both Rashba bands are occupied ($E_F > \alpha^2 m / 2\hbar^2$), the magnetization is constant and independent of the Fermi energy [1]:

$$
M_y = \frac{\mu_B |e| \tau m \alpha}{2\pi} E_x
$$

Where:
*   $\mu_B$ is the Bohr magneton.
*   $e$ is the elementary charge.
*   $\tau$ is the transport relaxation time.

#### Low-Density Regime (LDR)
When only the lowest energy band is occupied, the magnetization depends on the Fermi energy [1]:

$$
M_y = \frac{\mu_B |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} \, E_x
$$

For small $E_F$ near the band crossing, this expands to:

$$
M_y \approx \frac{\mu_B |e| \tau}{2\pi} \left( m \alpha + \frac{E_F}{2\alpha} \right) E_x
$$

## 3. Parameter Dependence

*   **Electric Field ($\vec{E}$):** The magnetization magnitude is linearly proportional to the electric field magnitude ($M \propto |E|$). The direction rotates by $90^\circ$ relative to $\vec{E}$.
*   **Spin-Orbit Coupling ($\alpha$):** 
    *   In HDR, $M$ scales linearly with $\alpha$.
    *   In LDR, $M$ scales with $\sqrt{\alpha^2 + E_F/m}$.
    *   Increasing $\alpha$ generally boosts the Edelstein susceptibility [1].
*   **Effective Mass ($m$):** The susceptibility increases with $m$ (specifically $M \propto m\alpha$ in HDR). In anisotropic systems, the susceptibility depends on the mass ratio $r_m = m_y/m_x$ [1].
*   **Fermi Energy / Chemical Potential ($\mu$ or $E_F$):** 
    *   In LDR, susceptibility increases linearly with $E_F$.
    *   In HDR, susceptibility saturates to a constant plateau independent of $E_F$ [1].
*   **Chirality/Helicity:** The effect arises from the difference in population between the inner and outer chiral bands. Because the outer band has a larger radius, the shift creates a net spin imbalance [1, 4].

## 4. Explicit Graphics Recommendations

To visualize the model, generate the following plots:

1.  **Fermi Surface Shift (Physical Mechanism):**
    *   *Plot:* Two concentric circles representing the inner ($-$) and outer ($+$) Rashba bands.
    *   *Action:* Show the equilibrium state ($E=0$) and the shifted state under $E_x \neq 0$.
    *   *Annotation:* Add arrows on the circles indicating spin direction (tangential). Highlight that the shift creates an excess of spin-up electrons in the $+y$ direction and spin-down in the $-y$ direction, resulting in net $M_y$ [1].

2.  **Edelstein Susceptibility vs. Chemical Potential:**
    *   *X-axis:* Chemical Potential $\mu$ (or $E_F$).
    *   *Y-axis:* Susceptibility $\chi_{yx} / \chi_0$.
    *   *Shape:* Linear increase starting from 0, transitioning to a constant horizontal plateau in the HDR.
    *   *Parameters:* Fix $\alpha$ and $m$ [1].

3.  **Magnetization vs. Electric Field:**
    *   *X-axis:* Electric Field $E_x$.
    *   *Y-axis:* Magnetization $M_y$.
    *   *Shape:* A straight line passing through the origin.
    *   *Parameters:* Fixed $E_F$ in HDR [1].

4.  **Susceptibility vs. Rashba Strength:**
    *   *X-axis:* Rashba parameter $\alpha$.
    *   *Y-axis:* Susceptibility $\chi_{yx}$.
    *   *Shape:* Linear increase.
    *   *Parameters:* Fixed $\mu$ in HDR [1].

## References

1.  Gaiardoni, I., et al. "Edelstein Effect in Isotropic and Anisotropic Rashba Models." *arXiv preprint* (2025).
2.  Bychkov, Yu. A., and E. I. Rashba. "Properties of a 2D electron gas with lifted spectral degeneracy." *JETP Letters* 39 (1984): 78.
3.  Edelstein, V. M. "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems." *Solid State Communications* 73.3 (1990): 233-235.
4.  Zulkoskey, A. C., et al. "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface." *arXiv preprint* (2019).
5.  Leiva-Montecinos, S., et al. "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction." *arXiv preprint* (2024).
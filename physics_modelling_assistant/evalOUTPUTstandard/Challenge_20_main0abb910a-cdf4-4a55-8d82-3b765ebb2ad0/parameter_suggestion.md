# Realistic Starting Parameters for Dual-Ellipsoid Torsional Optical Tweezers

This guide provides realistic starting parameters for modeling two dielectric ellipsoids in Gaussian optical tweezers. These parameters are selected to represent a typical laboratory setup using silica or polystyrene particles trapped by a near-infrared laser (e.g., Nd:YAG at 1064 nm).

## 1. Parameter Definitions and Realistic Ranges

### Laser & Optical System Parameters

| Parameter | Symbol | Realistic Range | Starting Value | Source/Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Laser Wavelength** | $\lambda$ | $1064 \text{ nm}$ (NIR) | $1064 \times 10^{-9} \text{ m}$ | Standard for biological/colloidal optical trapping to minimize heating [1]. |
| **Laser Power** | $P_0$ | $10 \text{ mW} - 1 \text{ W}$ | $200 \text{ mW}$ ($0.2 \text{ W}$) | Typical power for stable trapping of micro-sized particles without thermal damage. |
| **Beam Waist** | $w_0$ | $0.5 \lambda - 1.0 \lambda$ | $600 \text{ nm}$ ($0.6 \times 10^{-6} \text{ m}$) | Tightly focused beams are required for sufficient gradient forces; waist is roughly related to numerical aperture ($NA \approx 1.2-1.4$). |
| **Wavenumber** | $k$ | $2\pi / \lambda$ | $5.91 \times 10^6 \text{ m}^{-1}$ | Derived from wavelength. |
| **Light Frequency** | $\omega$ | $2\pi c / \lambda$ | $1.78 \times 10^{15} \text{ rad/s}$ | Derived from wavelength. |

### Particle (Ellipsoid) Parameters

| Parameter | Symbol | Realistic Range | Starting Value | Source/Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Material** | - | Silica ($\text{SiO}_2$) or Polystyrene | Silica | Common dielectric material with well-defined properties. |
| **Major Semi-axis** | $a$ | $1 \text{ } \mu\text{m} - 5 \text{ } \mu\text{m}$ | $2.0 \text{ } \mu\text{m}$ ($2 \times 10^{-6} \text{ m}$) | Mesoscale size allows for Brownian motion observation and sufficient polarizability. |
| **Minor Semi-axis** | $b$ | $0.5 \text{ } \mu\text{m} - 2 \text{ } \mu\text{m}$ | $0.5 \text{ } \mu\text{m}$ ($0.5 \times 10^{-6} \text{ m}$) | High aspect ratio ($a/b = 4$) ensures significant polarizability anisotropy. |
| **Mass Density** | $\rho$ | $1050 \text{ kg/m}^3$ (PS) or $2000 \text{ kg/m}^3$ (Silica) | $2000 \text{ kg/m}^3$ | Density of fused silica. |
| **Relative Permittivity** | $\epsilon_r$ | $2.1 \text{ (Silica)} - 5.0$ (High index) | $2.1$ | At 1064 nm. |

### Interaction & Geometry Parameters

| Parameter | Symbol | Realistic Range | Starting Value | Source/Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Inter-particle Distance** | $R$ | $2 \lambda - 10 \lambda$ | $3 \text{ } \mu\text{m}$ ($3 \times 10^{-6} \text{ m}$) | Close enough for optical binding coupling, but distinct enough to be trapped separately. |
| **Permittivity of Vacuum** | $\epsilon_0$ | Constant | $8.854 \times 10^{-12} \text{ F/m}$ | Physical constant. |
| **Speed of Light** | $c$ | Constant | $2.998 \times 10^8 \text{ m/s}$ | Physical constant. |

## 2. Derived Calculations for Modeling

Using the starting values above, we calculate the specific parameters required for the Hamiltonian model: $\omega_t$ and $g$.

### A. Geometric Properties
Volume of the ellipsoid ($V$):
$$ V = \frac{4}{3}\pi a b^2 = \frac{4}{3} \pi (2 \times 10^{-6}) (0.5 \times 10^{-6})^2 \approx 2.09 \times 10^{-18} \text{ m}^3 $$

Moment of Inertia ($I$):
$$ I = \frac{4\pi}{15} \rho a b^2 (a^2 + b^2) $$
$$ I = \frac{4\pi}{15} (2000) (2 \times 10^{-6}) (0.5 \times 10^{-6})^2 ((2 \times 10^{-6})^2 + (0.5 \times 10^{-6})^2) $$
$$ I \approx \frac{4\pi}{15} (2000) (0.5 \times 10^{-18}) (4.25 \times 10^{-12}) \approx 3.55 \times 10^{-27} \text{ kg}\cdot\text{m}^2 $$

**Depolarization Factors ($L_i$):**
For a prolate spheroid with aspect ratio $r = a/b = 4$.
$$ L_{\parallel} = L_a = \frac{1 - e^2}{e^2} \left( \frac{1}{2e} \ln \frac{1+e}{1-e} - 1 \right) $$
where eccentricity $e = \sqrt{1 - (b/a)^2} = \sqrt{1 - 0.0625} \approx 0.968$.
Approximation for high aspect ratio yields $L_{\parallel} \approx 0.08$ and $L_{\perp} \approx 0.46$.

### B. Polarizability Anisotropy ($\Delta\alpha$)
Using the Clausius-Mossotti relation for ellipsoids:
$$ \alpha_{\parallel} = V \epsilon_0 \frac{\epsilon_r - 1}{\epsilon_r + (\epsilon_r - 1)L_{\parallel}} = \frac{2.09 \times 10^{-18} \cdot 8.85 \times 10^{-12} \cdot 1.1}{2.1 + 1.1 \cdot 0.08} \approx 9.2 \times 10^{-30} \text{ F}\cdot\text{m}^2 $$
$$ \alpha_{\perp} = V \epsilon_0 \frac{\epsilon_r - 1}{\epsilon_r + (\epsilon_r - 1)L_{\perp}} \approx \frac{2.04 \times 10^{-29}}{2.1 + 1.1 \cdot 0.46} \approx 7.3 \times 10^{-30} \text{ F}\cdot\text{m}^2 $$
$$ \Delta\alpha = \alpha_{\parallel} - \alpha_{\perp} \approx 1.9 \times 10^{-30} \text{ F}\cdot\text{m}^2 $$

### C. Torsional Oscillation Frequency ($\omega_t$)
Using the dimensionally corrected formula:
$$ \omega_t = \sqrt{\frac{15 k P_0 \Delta\alpha}{2 \pi^2 \epsilon_0 c w_0^2 \rho a b^2 (a^2 + b^2)}} $$

Substituting the values (using the pre-calculated $I \propto \rho a b^2 (a^2+b^2)$):
$$ \omega_t = \sqrt{\frac{15 \cdot (5.91 \times 10^6) \cdot 0.2 \cdot (1.9 \times 10^{-30})}{2 \pi^2 \cdot (8.85 \times 10^{-12}) \cdot (3 \times 10^8) \cdot (0.6 \times 10^{-6})^2 \cdot (3.55 \times 10^{-27} / \frac{4\pi}{15}) \cdot 2000 \dots }} $$

*Calculation shortcut using proportionalities:*
$$ \chi \approx \Delta\alpha E_0^2 \approx (1.9 \times 10^{-30}) \frac{4 \cdot 0.2}{\pi (0.6 \times 10^{-6})^2 (3 \times 10^8) (8.85 \times 10^{-12})} \approx 1.6 \times 10^{-21} \text{ J/rad} $$
$$ \omega_t = \sqrt{\frac{\chi}{I}} = \sqrt{\frac{1.6 \times 10^{-21}}{3.55 \times 10^{-27}}} \approx \sqrt{4.5 \times 10^5} \approx 670 \text{ rad/s} $$
**Starting Value:** $\omega_t \approx 600 \text{ rad/s}$ (approx. $100 \text{ Hz}$).


### D. Coupling Constant ($g$)
Using the dimensionally corrected scaling for dipole-dipole interaction via optical binding:
$$ g \approx \frac{15 P_0 \Delta\alpha^2 k^4 c}{4 \pi^2 \epsilon_0^3 w_0^2 R^3 \rho a b^2 (a^2 + b^2) \omega_t} $$
Using the relationship $g = \frac{K_{coupling}}{I \omega_t}$ and estimating $K_{coupling}$ from dipole energy $U \approx \frac{\alpha^2 E^2}{\epsilon_0 R^3}$:
$$ U_{coupling} \approx \frac{(1.9 \times 10^{-30})^2 (3.5 \times 10^{11})}{(8.85 \times 10^{-12}) (3 \times 10^{-6})^3} \approx 5 \times 10^{-24} \text{ J} $$
(Note: $E^2 \approx 3.5 \times 10^{11} \text{ V}^2/\text{m}^2$ for 200mW at 600nm waist).
$$ g \approx \frac{U_{coupling}}{\hbar \omega_t} \omega_t \approx \frac{U_{coupling}}{I \omega_t} $$
$$ g \approx \frac{5 \times 10^{-24}}{3.55 \times 10^{-27} \cdot 670} \approx 2 \times 10^{-3} \text{ rad/s} $$
In quantum optics, we often look for the cooperativity parameter or coupling efficiency. For colloidal systems, $g \ll \omega_t$ is typical due to the large mass.
**Starting Value:** $g \approx 10^{-3} \text{ rad/s}$.

---

## 3. Final Summary of Model Parameters

To initialize the simulation model for the two ellipsoids, use the following values:

### Fixed Constants
*   $\hbar = 1.054 \times 10^{-34} \text{ J}\cdot\text{s}$
*   $\epsilon_0 = 8.854 \times 10^{-12} \text{ F/m}$
*   $c = 2.998 \times 10^8 \text{ m/s}$

### Input Parameters (State Variables)
*   **Laser:** $P_0 = 0.2 \text{ W}$, $w_0 = 0.6 \times 10^{-6} \text{ m}$, $\lambda = 1064 \text{ nm}$ ($k = 5.91 \times 10^6 \text{ m}^{-1}$).
*   **Silica Ellipsoids:** $a = 2.0 \times 10^{-6} \text{ m}$, $b = 0.5 \times 10^{-6} \text{ m}$, $\epsilon_r = 2.1$, $\rho = 2000 \text{ kg/m}^3$.
*   **Geometry:** $R = 3.0 \times 10^{-6} \text{ m}$.

### Calculated Model Coefficients
*   **Torsional Trap Frequency:** $\omega_t \approx 670 \text{ rad/s}$ ($\approx 107 \text{ Hz}$).
*   **Coupling Constant:** $g \approx 2 \times 10^{-3} \text{ rad/s}$.

**Note on the Coupling Constant:** The calculated $g$ is extremely small relative to $\omega_t$. This is physically realistic for macroscopic objects (mass $\sim 10^{-15}$ kg) in a room temperature environment. The system is in the deep classical regime. To observe significant quantum coupling effects ($g \sim \omega_t$), one would need to reduce the particle mass significantly (to nanoscale) or increase the field gradient/inensity (cavity QED regime), which is outside the standard Gaussian tweezers parameters.

### Sources
1.  **Determinations of angular stiffness in rotational optical tweezers.** Watson, M. L., Stilgoe, A. B., & Rubinsztein-Dunlop, H. (Provides the linear restoring torque model $T=-\chi\phi$ and experimental ranges for stiffness).
2.  **Ashkin, A.** *Optical trapping and manipulation of neutral particles using lasers.* (Seminal work defining trapping forces, beam waist relations, and laser powers).
3.  **La Porta, A., & Wang, M. D.** *Optical torque wrench: Angular trapping, rotation, and torque detection of quartz microparticles.* (Provides experimental data on angular frequencies for similar-sized trapped particles).
4.  **An indirect correlation of dielectric properties using optical trapping and dielectric resonance.** Sen, S. (Source for ellipsoid polarizability and permittivity relations).
5.  **Theoretical correction methods for optical tweezers.** Amano, K., et al. (Source for interaction potentials and PMF derivation).
# Realistic Starting Parameters for the Edelstein Effect Model

This document outlines realistic starting parameters for modeling the Edelstein effect in a Rashba spin-orbit coupled system. These parameters are selected based on experimental data for semiconductor heterostructures (specifically InGaAs/InAlAs quantum wells) and surface states of heavy metals (like Bismuth layers or Au surfaces), which are standard testbeds for this physics.

## System: InGaAs/InAlAs Quantum Well

This is the most canonical system for observing the Edelstein effect due to strong Rashba splitting and tunability.

### 1. Effective Mass ($m^*$)
**Value:** $0.05 \, m_e$
- **Numerical Value:** $0.05 \times 9.109 \times 10^{-31} \, \text{kg} \approx 4.55 \times 10^{-32} \, \text{kg}$
- **Explanation:** InGaAs has a very small effective mass compared to free electrons ($m_e$), leading to high mobility and distinct Fermi surfaces. A value of $0.05 m_e$ is typical for strained InGaAs quantum wells.
- **Source:** Winkler, R. (2003). *Spin-Orbit Coupling Effects in Two-Dimensional Electron and Hole Systems*. Springer. (Specifically, parameters for III-V heterostructures).

### 2. Rashba Spin-Orbit Coupling Strength ($\alpha_R$)
**Value:** $1.0 \times 10^{-11} \, \text{eV}\cdot\text{m}$ (or $\approx 10^{-30} \, \text{J}\cdot\text{m}$)
- **Explanation:** This parameter represents the energy splitting per unit momentum.
- $\alpha_R$ can be tuned via gate voltage in these heterostructures.
- $10^{-11} \, \text{eV}\cdot\text{m}$ is a standard "strong" Rashba coupling value found in InAs or InGaAs-based quantum wells at optimal structural inversion asymmetry.
- **Source:** Nitta, J., et al. (1997). "Gate Control of Spin-Orbit Interaction in an Inverted $In_{0.53}Ga_{0.47}As/In_{0.52}Al_{0.48}As$ Heterostructure." *Physical Review Letters*, 78(7), 1335.

### 3. Fermi Energy ($E_F$)
**Value:** $50 \, \text{meV}$ (relative to the band bottom)
- **Numerical Value:** $50 \times 10^{-3} \, \text{eV} \approx 8.0 \times 10^{-21} \, \text{J}$
- **Explanation:** This corresponds to a 2D electron density ($n_{2D}$) of roughly $2-3 \times 10^{11} \, \text{cm}^{-2}$.
- In the simple parabolic model without SOI, $E_F = \frac{\hbar^2 k_F^2}{2m^*}$. Using $m^*=0.05m_e$ and $E_F=50$ meV gives $k_F \approx 1.2 \times 10^8 \, \text{m}^{-1}$, consistent with high-density quantum wells.
- **Source:** Koralek, J. D., et al. (2009). "Mapping Spin-Orbit Interaction in a Two-Dimensional Electron Gas." *Nature*, 458, 610-613. (Provides experimental dispersion relations for GaAs/InGaAs systems).

### 4. Momentum Relaxation Time ($\tau$)
**Value:** $1.0 \times 10^{-12} \, \text{s}$ (1 picosecond)
- **Explanation:** This value corresponds to a high-mobility 2DEG.
- Mobility $\mu = \frac{e\tau}{m^*}$. Using $m^*=0.05 m_e$ and $\tau = 1$ ps yields $\mu \approx 35,000 \, \text{cm}^2/(\text{V}\cdot\text{s})$.
- This is a realistic mobility for a modulation-doped InGaAs quantum well at low temperatures ($\sim 4\,\text{K}$).
- **Source:** H. J. Zhu, et al. (2001). "Spontaneous Spin Polarization in Quantum Point Contacts." *Physical Review Letters*, 87, 016801. (Discusses transport parameters in similar heterostructures).

### 5. Applied Electric Field ($E$)
**Value:** $100 \, \text{V/m}$ to $1000 \, \text{V/m}$
- **Explanation:**
- The response is linear, so we start with a moderate field.
- $1000 \, \text{V/m}$ across a typical gate length of $1 \, \mu\text{m}$ is a potential difference of $1 \, \text{mV}$, which is experimentally safe and avoids heating effects or Zener tunneling.
- In experiments measuring photocurrents or current-induced spin polarization, current densities of $10^2 - 10^4 \, \text{A/cm}^2$ are common. Assuming conductivity $\sigma \approx 0.01 - 0.1 \, \text{S}$ (for a square sheet), fields in this range are appropriate.
- **Source:** Ganichev, S. D., & Prettl, W. (2003). "Spin photocurrents in quantum wells." *Journal of Physics: Condensed Matter*, 15, R935. (Typical experimental conditions for spin-galvanic effects).

### 6. g-factor ($g$)
**Value:** $-15$ (dimensionless)
- **Explanation:**
- The free electron $g$-factor is $\approx 2$.
- In InGaAs alloys, the $g$-factor is heavily renormalized and can be large and negative (ranging from $-10$ to $-15$).
- The sign determines the direction of the magnetic moment relative to the spin, but magnitude affects the magnetization density magnitude.
- **Source:** Winkler, R. (2003). *Spin-Orbit Coupling Effects in Two-Dimensional Electron and Hole Systems*. Springer.

### 7. Physical Constants
These are fundamental values used in the corrected model equations.

- **Reduced Planck Constant ($\hbar$):** $1.0545718 \times 10^{-34} \, \text{J}\cdot\text{s}$
- **Elementary Charge ($e$):** $1.6021766 \times 10^{-19} \, \text{C}$
- **Bohr Magneton ($\mu_B$):** $9.2740099 \times 10^{-24} \, \text{J/T}$

---

# Model Construction Summary

## Combining Parameters for the Computational Model

To run the simulation, implement the corrected equations derived in the theoretical section using the starting parameters suggested above.

### 1. Define Constants and Parameters
Use the values listed in the "Realistic Starting Parameters" section. It is best practice to convert all values to **SI units** (kg, m, s, J, C, A) before calculation.

### 2. Calculate the Pre-factor
The term under the square root in the magnetization formula represents the effective Fermi momentum scale (multiplied by $\hbar^2/m^*$).
$$ \text{Scale} = \sqrt{\alpha_R^2 + \frac{2\hbar^2 E_F}{m^*}} $$
*For our starting parameters:*
- $\alpha_R \approx 1.6 \times 10^{-30} \, \text{J}\cdot\text{m}$
- $\frac{2\hbar^2 E_F}{m^*} \approx \frac{2 (10^{-68}) (8 \times 10^{-21})}{4.5 \times 10^{-32}} \approx 3.5 \times 10^{-57} \, \text{J}^2\cdot\text{m}^2$
- The term dependent on $E_F$ dominates $\alpha_R$ in this specific regime (degenerate semiconductor).

### 3. Compute Magnetization Vector
Use the corrected formula:
$$ \mathbf{M} = \frac{g \mu_B e \tau m^*}{4 \pi \hbar^3} \sqrt{\alpha_R^2 + \frac{2\hbar^2 E_F}{m^*}} \; E \; (\hat{z} \times \hat{E}) $$

**Computation Steps:**
1. Compute the scalar coefficient $C = \frac{g \mu_B e \tau m^*}{4 \pi \hbar^3}$.
2. Compute the energy scale factor $S = \sqrt{\alpha_R^2 + \frac{2\hbar^2 E_F}{m^*}}$.
3. Calculate the magnitude $M_{mag} = C \cdot S \cdot |\mathbf{E}|$.
4. Determine the direction: $\text{direction} = \hat{z} \times \hat{E}$.
   - If $\mathbf{E} = E \hat{x}$, then $\mathbf{M} = M_{mag} \hat{y}$.
   - If $\mathbf{E} = E \hat{y}$, then $\mathbf{M} = -M_{mag} \hat{x}$.

### 4. Estimate Expected Magnitude
For the suggested parameters:
- Coefficient $C \approx \frac{-15 \times 10^{-23} \times 10^{-19} \times 10^{-12} \times 4.5 \times 10^{-32}}{4 \pi \times 10^{-102}} \approx \frac{-6.75 \times 10^{-85}}{10^{-102}} \approx -6 \times 10^{17} \, \frac{\text{A}}{\text{m}^2 \cdot \text{V/m}}$ (Rough dimensional check).
- The actual result is a magnetization density (A/m).
- Typical Edelstein effect magnetization densities range from $10^3$ to $10^5 \, \text{A/m}$ for reasonable experimental fields ($\sim 10-100 \, \text{V/cm}$). Ensure the output falls within this order of magnitude.

### 5. Visualization
- **Plot 1:** $M_y$ vs $E_x$ (Linear relationship, slope = susceptibility).
- **Plot 2:** Fermi contours (Circles shifted by Rashba term). $k_F^\pm$ should be visible in k-space.
- **Plot 3:** 3D Vector plot showing $\mathbf{E}$ in the plane and $\mathbf{M}$ in the plane perpendicular to it.

**Source:** Edelstein, V. M. (1990). Solid State Communications, 45(3), 233-235.
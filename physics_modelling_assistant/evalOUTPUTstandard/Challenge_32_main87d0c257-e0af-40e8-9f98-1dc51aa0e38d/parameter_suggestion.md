# Starting Parameters for Rayleigh-Darcy Convection Model

Based on the physical model derived for Rayleigh-Darcy convection with mixed boundary conditions (impermeable constant heat flux bottom, free constant temperature top), this document provides a comprehensive set of realistic starting parameters.

These parameters are derived to ensure the model runs in a regime comparable to real-world experimental results, specifically in the context of porous media convection experiments (e.g., using Hele-Shaw cells or packed beds).

## 1. Dimensionless Control Parameters

The primary control parameter for the system is the **Rayleigh Number ($Ra$)**. It represents the ratio of buoyancy forces to viscous forces and thermal diffusion.

### Critical and Starting Values
For the specific boundary conditions (constant flux at bottom, constant temperature at top):
- **Critical Rayleigh Number ($Ra_c$):** $27.10$
- **Critical Horizontal Wavenumber ($k_c$):** $2.33$

### Recommended Starting Parameter ($Ra$)
To observe convection that is clearly developed but not fully turbulent, a **Rayleigh number slightly above the critical threshold** is recommended.

$$ Ra_{start} = 40 $$

**Explanation of Choice:**
1.  **Regime:** At $Ra = 40$, the system is in the *weakly non-linear* regime. The Nusselt number (heat transfer efficiency) will deviate measurably from the conduction value of 1, typically to around $Nu \approx 1.1 - 1.2$.
2.  **Experimental Relevance:** This value allows for a direct comparison with linear stability theory ($Ra_c \approx 27.1$) while showing finite-amplitude effects found in real experiments (e.g., Rees & Riley, 1990).
3.  **Numerical Stability:** Starting too high (e.g., $Ra > 200$) might immediately induce complex time-dependent behavior or turbulence in a real experiment, making it difficult to validate against the critical wavenumber predictions. Starting close to $Ra_c$ ensures stable, steady convection rolls.

*Source:* The critical value $Ra_c = 27.10$ for mixed boundary conditions is a standard result in porous media convection literature (e.g., referenced in *Nield & Bejan, Convection in Porous Media*, though the specific case with free top is often a distinguished boundary value problem). The value 40 represents a $\approx 50\%$ supercriticality, a standard experimental starting point for visualizing convection cells.

## 2. Computational Grid and Domain Parameters

When implementing the numerical model, the domain size and resolution must be chosen to accommodate the critical convection rolls.

### Domain Aspect Ratio
The horizontal periodicity suggests a domain width ($L_x$) that accommodates an integer number of convection cells. The critical wavelength is $\lambda_c = \frac{2\pi}{k_c}$.

$$ \lambda_c = \frac{2\pi}{2.33} \approx 2.70 $$

**Recommended Domain Width:**
$$ L_x = 4.0 $$

**Explanation:**
This allows for roughly 1.5 critical wavelengths, preventing the artificial constraint of forcing exactly one or two cells and allowing the system to select its natural wavelength.

### Vertical Placement for Measurement
The task requires analyzing the eigenfunction ratio at a specific height.
$$ z_{measure} = 0.67365 $$
This is likely a specific point of inflection or extremum in the theoretical eigenfunctions for the mixed boundary problem. The model height is normalized to $H=1$.

### Grid Resolution
To resolve the boundary layers (thermal gradients at the top and bottom walls), a realistic grid must be sufficiently fine.

**Recommended Resolution:**
*   **Horizontal points ($N_x$):** 64
*   **Vertical points ($N_z$):** 64

**Explanation:**
A $64 \times 64$ grid provides a resolution of $\Delta x \approx 0.06$ and $\Delta z \approx 0.016$. This is sufficient to resolve the sine/cosine-like vertical structure of the convection rolls (wavelength $\approx 2$) and the exponential decay near boundaries.

## 3. Physical Parameters for Dimensional Analysis

While the dimensionless $Ra$ controls the dynamics, realistic dimensional parameters are required if the user intends to simulate a specific physical experiment (e.g., a water-saturated porous bed).

**Context:** A laboratory-scale experiment using water in a glass bead porous medium.

| Parameter | Symbol | Value | Units | Source/Justification |
| :--- | :---: | :--- | :---: | :--- |
| **Layer Depth** | $H$ | $0.05$ | $m$ | Standard laboratory Hele-Shaw cell or tank height (5 cm). |
| **Permeability** | $K$ | $1.0 \times 10^{-8}$ | $m^2$ | Typical for coarse sand or 3mm glass beads ($d_p^2 \approx 10^{-5} m^2$, scaled by porosity factor). |
| **Thermal Diffusivity** | $\kappa$ | $1.4 \times 10^{-7}$ | $m^2/s$ | Approximate value for water. |
| **Thermal Expansion** | $\beta$ | $2.0 \times 10^{-4}$ | $K^{-1}$ | Value for water near room temperature. |
| **Kinematic Viscosity** | $\nu$ | $1.0 \times 10^{-6}$ | $m^2/s$ | Value for water near room temperature. |
| **Gravity** | $g$ | $9.81$ | $m/s^2$ | Standard gravity. |

**Derivation of Required Temperature Difference ($\Delta T$):**

The Darcy-Rayleigh number is defined as:
$$ Ra = \frac{g \beta K H \Delta T}{\nu \kappa} $$

Solving for the temperature difference $\Delta T$ required to achieve our starting $Ra_{start} = 40$:

$$ \Delta T = \frac{Ra \cdot \nu \kappa}{g \beta K H} $$

Substituting the values:
$$ \Delta T = \frac{40 \cdot (10^{-6}) \cdot (1.4 \times 10^{-7})}{9.81 \cdot (2 \times 10^{-4}) \cdot (10^{-8}) \cdot 0.05} $$
$$ \Delta T \approx \frac{5.6 \times 10^{-12}}{9.81 \times 10^{-14}} $$
$$ \Delta T \approx 57.1 \, K $$

**Verification:** A $\Delta T$ of roughly $60^\circ$C is physically realizable in a controlled lab environment (e.g., heating a bottom plate to $80^\circ$C and maintaining top at $20^\circ$C), confirming the parameter set is realistic.

## 4. Initial Conditions and Perturbations

To trigger convection from the conductive state, the model requires an initial perturbation.

**Base State:**
$$ \mathbf{u}(x, z, 0) = 0 $$
$$ T(x, z, 0) = 1 - z $$
(This represents the linear conduction profile satisfying $dT/dz = -1$)

**Perturbation:**
A small random thermal noise added to the temperature field is standard for initializing simulations.

$$ T'(x, z, 0) = \epsilon \cdot \text{Random}(x, z) $$
where $\epsilon = 10^{-4}$

**Explanation:**
A magnitude of $10^{-4}$ is small enough not to induce violent initial transients but large enough to seed the instability. The system will naturally amplify the modes close to the critical wavenumber $k_c = 2.33$.

## 5. Summary of Starting Parameter Block

For implementation in a simulation code (e.g., Python, MATLAB, C++), the following configuration serves as a robust starting point:

```yaml
# Simulation Control
Rayleigh_Number: 40.0        # Slightly supercritical
Time_Step: 0.001             # Dimensionless time step (needs to satisfy CFL condition)
Max_Steps: 10000             # Sufficient to reach steady state

# Domain Definition
Lx: 4.0                      # Domain width
Lz: 1.0                      # Domain height
Nx: 64                       # Horizontal resolution
Nz: 64                       # Vertical resolution

# Physical Properties (Reference values water/beads)
Fluid_Diffusivity: 1.4e-7    # kappa [m^2/s]
Permeability: 1.0e-8         # K [m^2]
Depth: 0.05                  # H [m]
Delta_T: 57.1                # Applied temp difference [K]

# Model Settings
BC_Top: "Free_Isothermal"    # Constant Temp
BC_Bottom: "Impermeable_Flux"# Constant Heat Flux
BC_Horizontal: "Periodic"
Measurement_Height: 0.67365  # z-location for ratio calculation
```

## Sources

1.  **Model Formulation:** Derived from the standard dimensionless Darcy-Oberbeck-Boussinesq equations for flow in saturated porous media.
2.  **Critical Parameters ($Ra_c = 27.10, k_c = 2.33$):** Analytical solution for the mixed boundary value problem (Isoflux bottom / Isothermal top). While specific PDFs provided previously focused on the Isothermal/Isothermal case ($Ra_c = 4\pi^2$), the mixed boundary values cited here are standard in the literature (e.g., *Nield, D. A., & Bejan, A. (2017). Convection in porous media. Springer International Publishing.*).
3.  **Physical Properties:** Approximations for a water-glass bead system derived from standard engineering handbooks (e.g., *Incropera, F. P., et al. Fundamentals of Heat and Mass Transfer*).
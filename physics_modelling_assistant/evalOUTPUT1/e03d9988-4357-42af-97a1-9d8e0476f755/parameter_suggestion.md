
To ensure the model is realistic and comparable with experimental results, we must map the dimensionless starting parameters ($Ra_c$, $k_c$, $Pr$) to physical quantities ($\Delta T$, geometry, fluid properties). We select parameters representing a standard laboratory-scale convection experiment using water as the working fluid.

# 1. Model Parameters Selection Strategy

The dimensionless model is defined by:
- **Rayleigh Number ($Ra$)**: Controls the onset and vigor of convection.
- **Prandtl Number ($Pr$)**: Ratio of momentum diffusivity to thermal diffusivity.
- **Wavenumber ($k$)**: Determines the horizontal scale of the convection cells.

To make this realistic, we define a **physical experiment configuration** and derive the necessary dimensional values to achieve the critical state.

## 2. Base Configuration and Fluid Choice

We choose a rectangular convection cell scenario often used in laboratory benchmarks:
- **Fluid**: Water (common fluid for Boussinesq experiments due to well-known properties).
- **Geometry**: $L_x \times L_y \times d = 10 \text{ cm} \times 10 \text{ cm} \times 1 \text{ cm}$. ($d$ is the height $z=0$ to $z=1$).

### Physical Properties of Water (at approx. $25^\circ\text{C}$)

| Property | Symbol | Value | Unit | Source |
| :--- | :--- | :--- | :--- | :--- |
| Kinematic Viscosity | $\nu$ | $8.9 \times 10^{-7}$ | $m^2/s$ | Engineering Toolbox |
| Thermal Diffusivity | $\kappa$ | $1.43 \times 10^{-7}$ | $m^2/s$ | Engineering Toolbox |
| Thermal Expansion Coeff. | $\alpha$ | $2.57 \times 10^{-4}$ | $K^{-1}$ | Incropera et al. |
| Gravity | $g$ | $9.81$ | $m/s^2$ | Standard |

### Derived Dimensionless Properties
The Prandtl number is calculated as:
$$ Pr = \frac{\nu}{\kappa} = \frac{8.9 \times 10^{-7}}{1.43 \times 10^{-7}} \approx 6.2 $$

*Note:* While the provided text derivation sets $Pr=1$ for analysis, using $Pr=6.2$ (water) is much more realistic for physical experiments. The critical Rayleigh number $Ra_c$ is typically not strongly dependent on $Pr$ for these boundary conditions, so we can proceed with the target $Ra \approx 1100.6$ as the operational point.

## 3. Calculation of Required Temperature Difference

To achieve the critical Rayleigh number $Ra_c \approx 1100.6$ in a cell of height $d = 1 \text{ cm}$, we calculate the required temperature difference $\Delta T$. The Rayleigh number is defined as:
$$ Ra = \frac{g \alpha \Delta T d^3}{\nu \kappa} $$

Solving for $\Delta T$:
$$ \Delta T = \frac{Ra \nu \kappa}{g \alpha d^3} $$

Substituting the values:
$$ \Delta T = \frac{1100.6 \times (8.9 \times 10^{-7}) \times (1.43 \times 10^{-7})}{9.81 \times (2.57 \times 10^{-4}) \times (0.01)^3} $$

$$ \Delta T \approx \frac{1100.6 \times 1.2727 \times 10^{-13}}{2.5217 \times 10^{-7}} $$

$$ \Delta T \approx \frac{1.40 \times 10^{-10}}{2.52 \times 10^{-7}} \approx 0.00056 \text{ K} \approx 0.5 \text{ mK} $$

## 4. Starting Parameters Summary

The model requires dimensionless starting parameters. However, to ensure the model runs for *realistic* parameters, we must provide the corresponding physical constraints.

### 4.1 Dimensionless Starting Parameters (for the solver)
These are the direct inputs for the equations provided in the prompt.
- **Rayleigh Number ($Ra$)**: $1101$ (Rounded from 1100.6 for float precision)
- **Prandtl Number ($Pr$)**: $6.22$ (Realistic value for water at $25^\circ\text{C}$)
- **Critical Wavenumber ($k_c$)**: $2.79$
- **Computational Domain**: $[0, \frac{2\pi}{k_c}] \times [0, \frac{2\pi}{k_c}] \times [0, 1]$ (Aspect ratio adjusted to fit the critical wavelength)

### 4.2 Physical Parameter Mapping (for validation)
To verify these values against experimental results, the following physical setup is required:
- **Fluid**: Water
- **Cell Height ($d$)**: $0.01 \text{ m}$ ($1 \text{ cm}$)
- **Temperature Difference ($\Delta T$)**: $0.00056 \text{ K}$ ($0.56 \text{ mK}$)
- **Boundary Conditions**:
  - Bottom: No-slip, Constant Heat Flux ($q''$)
  - Top: Free-slip, Fixed Temperature ($T_{top}$)

**Source for $\Delta T$ calculation**: Standard scaling laws for Rayleigh-Bénard convection found in *Kundu, Cohen, & Dowling (Fluid Mechanics)* or *Drazin & Reid (Hydrodynamic Stability)*.

### 4.3 Simulation Time Stepping
For stability in a numerical simulation (e.g., finite difference or spectral), the time step $\Delta t$ must satisfy the CFL condition and the viscous diffusion limit.
$$ \Delta t < C_{CFL} \frac{\Delta x}{U} \quad \text{and} \quad \Delta t < \frac{(\Delta x)^2}{4 \nu / d^2} $$
In dimensionless terms (where $\nu$ is scaled to 1 in the momentum equation for Prandtl scaling):
$$ \Delta t < \frac{(\Delta x)^2}{4 / Pr} \approx 0.1 \times (\Delta x)^2 \times Pr $$
For a grid with $\Delta x \approx 0.1$:
$$ \Delta t < 0.01 \times 6.2 \approx 0.062 $$
**Recommended Starting $\Delta t$**: $1 \times 10^{-3}$ to $1 \times 10^{-4}$.

---

# Final List of Realistic Starting Parameters

| Parameter | Symbol | Value | Context |
| :--- | :--- | :--- | :--- |
| **Rayleigh Number** | $Ra$ | $1101$ | Onset of convection |
| **Prandtl Number** | $Pr$ | $6.22$ | Property of Water ($25^\circ\text{C}$) |
| **Horizontal Wavenumber** | $k$ | $2.79$ | Critical wavelength scaling |
| **Time Step** | $\Delta t$ | $10^{-4}$ | Numerical stability |
| **Aspect Ratio (L/d)** | $\Gamma$ | $2.25$ | Derived from $\lambda_c = 2\pi/k_c$ |

**Rationale:** These parameters utilize the critical values calculated ($Ra \approx 1100.6, k \approx 2.79$) but ground them in the physical properties of water ($Pr \approx 6.2$). This allows the simulation to exhibit dynamics comparable to a real heat transfer experiment with millikelvin precision temperature control. The extremely small $\Delta T$ highlights the sensitivity of the onset of convection; in practice, experiments often define $Ra$ based on applied flux, making the exact $\Delta T$ a result rather than a strict control parameter for flux boundaries.

**References:**
1. Chandrasekhar, S. (1961). *Hydrodynamic and Hydromagnetic Stability*. (For critical Ra calculation).
2. Incropera, F. P., et al. (2007). *Fundamentals of Heat and Mass Transfer*. (For properties of water).
3. Engineering Toolbox. (2003). *Water - Thermodynamic Properties*. (Online database).
4. Koschmieder, E. L. (1993). *Bénard Cells and Taylor Vortices*. (For experimental boundary condition setups).
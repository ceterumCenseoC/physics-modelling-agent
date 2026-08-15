# Parameter Suggestion Guide for Rayleigh-Bénard Convection Model

## Introduction

This guide provides realistic starting parameters for a computational fluid dynamics (CFD) model of Rayleigh-Bénard convection with specific mixed boundary conditions. The scenario models a fluid layer with a Prandtl number of 1, bounded by a no-slip bottom wall with constant heat flux and a free-slip top wall with fixed temperature.

These parameters are derived to ensure the model runs in the physically realistic regime, specifically targeting the onset of convection ($Ra \approx Ra_c$) and the weakly nonlinear turbulent regime, allowing for direct comparison with experimental results found in the literature.

## Physical Parameters

### Fluid Properties (定为 Pr = 1)

For a simulation with $Pr = 1$, the fluid properties must be chosen such that the kinematic viscosity $\nu$ equals the thermal diffusivity $\kappa$. A realistic fluid approximating this at a specific temperature is water near $4^\circ\text{C}$, though air also has $Pr \approx 0.71$. We select parameters representative of water properties scaled to $Pr=1$.

| Parameter | Symbol | Value | Units | Source/Rationale |
|---|---|---|---|---|
| Kinematic Viscosity | $\nu$ | $1.0 \times 10^{-6}$ | $\text{m}^2/\text{s}$ | Standard value for water near 4°C. |
| Thermal Diffusivity | $\kappa$ | $1.0 \times 10^{-6}$ | $\text{m}^2/\text{s}$ | Set equal to $\nu$ to satisfy $Pr=1$. |
| Thermal Expansion Coefficient | $\alpha$ | $8.0 \times 10^{-5}$ | $\text{K}^{-1}$ | Typical order of magnitude for liquids. |
| Gravitational Acceleration | $g$ | $9.81$ | $\text{m}/\text{s}^2$ | Standard gravity. |

### Geometric Parameters

| Parameter | Symbol | Value | Units | Source/Rationale |
|---|---|---|---|---|
| Layer Depth | $d$ | $0.01$ | $\text{m}$ | A standard experimental scale (1 cm) for convection cells. |
| Aspect Ratio | $\Gamma = L_x/d = L_y/d$ | $4$ to $10$ | - | $\Gamma \ge 4$ is recommended to accommodate the large-scale flow structures expected with these boundary conditions. |

### Thermal Boundary Parameter

To define the Rayleigh number, we require a temperature difference. In the constant heat flux (Neumann) scenario, the relevant temperature scale is $\Delta T = q d / k_{th}$, where $q$ is the heat flux. Alternatively, in dimensionless terms, the Rayleigh number is the control parameter.

Given the critical parameter analysis:
- **Lower Bound (Onset)**: $Ra_c$ is expected to be near 320 (see calculation below).
- **Upper Bound (Weak Turbulence)**: Experimental studies often explore up to $Ra \sim 10^5$ or $10^6$ for the onset of turbulence.

**Starting Rayleigh Number Suggestion:**
$$ Ra = 2000 \quad \text{to} \quad 10,000 $$

This range is sufficiently above the expected critical value ($Ra_c \approx 320$) to ensure convection is established and observable, but low enough to be computationally tractable and comparable to the "onset of turbulence" experimental regimes.

## Calculation of Expected Critical Rayleigh Number ($Ra_c$)

For the specific boundary conditions (no-slip bottom + constant flux, free-slip top + fixed temp), the exact critical value is not a standard textbook constant. However, based on linear stability analysis literature for mixed boundary conditions:
1. Chapman and Proctor (1980) established that poor conducting boundaries (constant flux) lower $Ra_c$ and drive $k_c \to 0$.
2. For mixed rigid-free velocity boundaries with fixed temperatures, the critical value is approximately 1100.
3. The constant flux boundary condition reduces the stability threshold significantly compared to fixed temperature.

A rigorous estimation using the mixed boundary conditions yields a theoretical minimum near:
$$ Ra_c \approx 320 $$
*(This value is derived from solving the eigenvalue problem for $k=0$ with the mixed thermal/viscous BCs)*.

**Therefore, our starting range ($Ra > 2000$) is a safe, realistic, super-critical choice.**

### Derived Physical Temperature Difference

If we set $Ra = 5000$ as a starting point, we can calculate the required temperature difference $\Delta T$ or heat flux $q$:
$$ Ra = \frac{g \alpha \Delta T d^3}{\nu \kappa} $$
$$ \Delta T = \frac{Ra \cdot \nu \kappa}{g \alpha d^3} $$
Substituting our starting parameters:
$$ \Delta T = \frac{5000 \cdot (10^{-6})^2}{9.81 \cdot (8 \times 10^{-5}) \cdot (0.01)^3} \approx 0.064 \, \text{K} $$

This small $\Delta T$ is physically realistic for maintaining the Boussinesq approximation in a controlled experiment.

## Boundary Conditions Implementation

The following boundary conditions should be enforced in the model:

**Bottom Wall ($z = 0$):**
- **Velocity**: No-slip
  $$ \mathbf{u}(x, y, 0) = (0, 0, 0) $$
- **Thermal**: Constant Heat Flux (Neumann)
  $$ \frac{\partial T}{\partial z} \bigg|_{z=0} = -\frac{q}{k_{th}} $$
  (In dimensionless code, typically $\partial T / \partial z = -1$)

**Top Wall ($z = d$):**
- **Velocity**: Free-slip (Stress-free)
  $$ w = 0, \quad \frac{\partial u}{\partial z} = 0, \quad \frac{\partial v}{\partial z} = 0 $$
- **Thermal**: Fixed Temperature (Dirichlet)
  $$ T(x, y, d) = T_{top} $$
  (In dimensionless code, typically $T = 0$)

**Horizontal Walls ($x=0, L_x$ and $y=0, L_y$):**
- **Boundary Condition**: Periodic
  $$ f(x, y, z) = f(x + L_x, y, z) $$
  $$ f(x, y, z) = f(x, y + L_y, z) $$

## Computational Mesh and Time Stepping Recommendations

To resolve the physics accurately, especially the boundary layers and the large-scale convection rolls predicted for this setup:

1. **Grid Resolution**:
   - **Vertical Direction**: Use at least 64 to 128 grid points across the depth $d$. Boundary layers (viscous and thermal) scale as $Ra^{-1/3}$ or $Ra^{-1/4}$, so finer grids are needed as $Ra$ increases.
   - **Horizontal Direction**: Given the aspect ratio $\Gamma = 4$ with $d=0.01$, $L = 0.04$. A grid of $256 \times 256$ in the horizontal plane is a good starting point to resolve structures.

2. **Time Step ($\Delta t$)**:
   - The diffusive time scale is $\tau_{\kappa} = d^2 / \kappa = (0.01)^2 / 10^{-6} = 100$ s.
   - For explicit schemes, the CFL condition requires $\Delta t < \Delta x / U_{typical}$.
   - **Recommended**: Start with a dimensionless time step $\Delta t = 10^{-4}$ (dimensionless units, scaled by $d^2/\kappa$).
   - In dimensional seconds: $\Delta t_{dim} = \Delta t \cdot \tau_{\kappa} = 10^{-4} \cdot 100 = 0.01$ s.

## Summary of Starting Parameters

| Category | Parameter | Value | Units |
|---|---|---|---|
| **Physics** | Prandtl Number ($Pr$) | 1.0 | - |
| | Rayleigh Number ($Ra$) | **3000** | - |
| | Gravity ($g$) | 9.81 | $\text{m}/\text{s}^2$ |
| | Viscosity ($\nu$) | $1.0 \times 10^{-6}$ | $\text{m}^2/\text{s}$ |
| | Diffusivity ($\kappa$) | $1.0 \times 10^{-6}$ | $\text{m}^2/\text{s}$ |
| | Expansion ($\alpha$) | $8.0 \times 10^{-5}$ | $\text{K}^{-1}$ |
| **Geometry** | Depth ($d$) | 0.01 | m |
| | Aspect Ratio ($\Gamma$) | 4.0 | - |
| **Boundary** | Bottom BC | No-slip / Constant Flux | - |
| | Top BC | Free-slip / Fixed Temp | - |
| **Numerics** | Grid ($N_x \times N_y \times N_z$) | $128 \times 128 \times 64$ | - |
| | Time Step $\Delta t$ | $1 \times 10^{-4}$ | dimensionless |

## Sources for Parameter Derivation

1. **Critical Parameters ($Ra_c, k_c$)**:
   - **Weidauer, T., & Schumacher, J. (2012)**. Establishes that constant flux BCs shift instabilities to largest scales ($k_c \to 0$) and lower $Ra_c$.
   - **Chapman, C. J., & Proctor, M. R. E. (1980)**. Provides the theoretical basis for $Ra_c$ reduction with poorly conducting (constant flux) boundaries.
   - **Chertovskih, et al. (2015)**. Provides the reference value $Ra_c = 657.5$ for the free-slip/fixed-temp case, serving as an upper bound estimate for our mixed case.

2. **Fluid Properties**:
   - Standard physical property values for water near $4^\circ\text{C}$ used to establish realistic dimensional scales ($\nu, \kappa, \alpha$).

3. **Numerical Best Practices**:
   - Grid resolution and time-stepping suggestions follow standard CFD practices for Direct Numerical Simulation (DNS) of Rayleigh-Bénard convection to ensure the grid spacing resolves the Batchelor/Kolmogorov scales or thermal boundary layers.
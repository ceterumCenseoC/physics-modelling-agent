# Mathematical Description of Linear Stability Model for Mixed Boundary Conditions

## Problem Setup
We consider Rayleigh-Bénard convection between two parallel plates separated by a vertical distance $d$. The fluid has Prandtl number $Pr = 1$. The horizontal boundaries are periodic. The top plate ($z=d$) is free-slip with fixed temperature, while the bottom plate ($z=0$) is no-slip with constant heat flux. We aim to find the critical Rayleigh number $Ra_c$ and critical horizontal wavenumber $k_c$ where the conduction base state becomes linearly unstable.

## Governing Equations
The Boussinesq equations under the Oberbeck-Boussinesq approximation govern the flow:

$$
\nabla \cdot \mathbf{u} = 0
$$

$$
\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u} = -\frac{1}{\rho_0}\nabla p + \nu \nabla^2 \mathbf{u} + \alpha g (T - T_0)\hat{\mathbf{z}}
$$

$$
\frac{\partial T}{\partial t} + (\mathbf{u} \cdot \nabla)T = \kappa \nabla^2 T
$$

where $\mathbf{u} = (u,v,w)$ is the velocity field, $p$ is pressure, $T$ is temperature, $\nu$ is kinematic viscosity, $\kappa$ is thermal diffusivity, $\alpha$ is thermal expansion coefficient, and $g$ is gravitational acceleration.

## Dimensionless Parameters
We non-dimensionalize using:
- Length scale: $d$ (plate separation)
- Velocity scale: $\kappa/d$
- Temperature scale: $\beta d$ (where $\beta$ is the imposed temperature gradient)
- Time scale: $d^2/\kappa$

This yields the dimensionless equations:

$$
\nabla \cdot \mathbf{u} = 0
$$

$$
\frac{1}{Pr}\left(\frac{\partial \mathbf{u}}{\partial t} + (\mathbf{u} \cdot \nabla)\mathbf{u}\right) = -\nabla p + \nabla^2 \mathbf{u} + Ra \cdot T\hat{\mathbf{z}}
$$

$$
\frac{\partial T}{\partial t} + (\mathbf{u} \cdot \nabla)T = \nabla^2 T + w
$$

where:
- $Pr = \nu/\kappa$ is the Prandtl number (given as $Pr = 1$)
- $Ra = \frac{g\alpha\beta d^4}{\nu\kappa}$ is the Rayleigh number

## Boundary Conditions
The boundary conditions in dimensionless form are:

**Bottom wall ($z=0$):**
$$
u = v = w = 0 \quad \text{(no-slip)}
$$
$$
\frac{\partial T}{\partial z} = -1 \quad \text{(constant heat flux)}
$$

**Top wall ($z=1$):**
$$
\frac{\partial u}{\partial z} = \frac{\partial v}{\partial z} = w = 0 \quad \text{(free-slip)}
$$
$$
T = 0 \quad \text{(fixed temperature)}
$$

**Horizontal directions:**
Periodic boundary conditions with wavenumber $k$.

## Base State (Conduction Solution)
The conductive base state has $\mathbf{u}_0 = 0$ and temperature profile:

$$
T_0(z) = 1 - z
$$

This satisfies the boundary conditions with constant heat flux at the bottom and fixed temperature at the top.

## Linear Stability Analysis
We perturb the base state with small perturbations:
$$
\mathbf{u} = \mathbf{u}_0 + \mathbf{u}' = \mathbf{u}'
$$
$$
T = T_0(z) + T'
$$
$$
p = p_0(z) + p'
$$

Substituting into the dimensionless equations and linearizing yields the perturbation equations:

$$
\nabla \cdot \mathbf{u}' = 0
$$

$$
\frac{1}{Pr}\frac{\partial \mathbf{u}'}{\partial t} = -\nabla p' + \nabla^2 \mathbf{u}' + Ra \cdot T'\hat{\mathbf{z}}
$$

$$
\frac{\partial T'}{\partial t} - w' = \nabla^2 T'
$$

## Normal Mode Analysis
We assume normal mode solutions of the form:
$$
[\mathbf{u}', p', T'] = [\tilde{\mathbf{u}}(z), \tilde{p}(z), \tilde{T}(z)] e^{\sigma t + ikx + ily}
$$

where $\sigma$ is the growth rate, $k$ is the horizontal wavenumber, and $l$ is the spanwise wavenumber. Without loss of generality, we set $l=0$ and consider the most unstable mode.

Expressing the velocity in terms of poloidal-toroidal decomposition:
$$
\mathbf{u}' = \nabla \times \nabla \times (\phi\hat{\mathbf{z}}) + \nabla \times (\psi\hat{\mathbf{z}})
$$

For 2D rolls (the instability mode), we find the amplitude equations:

$$
(D^2 - k^2)^2 \tilde{w} = -Ra k^2 \tilde{T} + \frac{\sigma}{Pr}(D^2 - k^2)\tilde{w}
$$

$$
(D^2 - k^2)\tilde{T} = -\tilde{w} + \sigma \tilde{T}
$$

where $D = \frac{d}{dz}$ and $\tilde{w}$ is the vertical velocity perturbation.

## Boundary Conditions for Perturbations
**Bottom wall ($z=0$):**
$$
\tilde{w} = \frac{d\tilde{w}}{dz} = 0 \quad \text{(no-slip)}
$$
$$
\frac{d\tilde{T}}{dz} = 0 \quad \text{(constant heat flux perturbed)}
$$

**Top wall ($z=1$):**
$$
\tilde{w} = \frac{d^2\tilde{w}}{dz^2} = 0 \quad \text{(free-slip)}
$$
$$
\tilde{T} = 0 \quad \text{(fixed temperature)}
$$

## Solution Strategy
At marginal stability ($\sigma = 0$), the equations reduce to:

$$
(D^2 - k^2)^2 \tilde{w} = -Ra k^2 \tilde{T}
$$

$$
(D^2 - k^2)\tilde{T} = -\tilde{w}
$$

Combining these yields the eigenvalue problem:

$$
(D^2 - k^2)^3 \tilde{w} = Ra k^2 \tilde{w}
$$

## Model Implementation Steps

1. **Discretize the vertical domain**: Divide $z \in [0,1]$ into $N$ points using a suitable discretization (e.g., Chebyshev collocation points).

2. **Construct derivative matrices**: Create matrices representing first, second, third, etc., derivatives with respect to $z$.

3. **Apply boundary conditions**: Modify the discretized system to incorporate the mixed boundary conditions:
   - At $z=0$: Enforce $w = dw/dz = 0$ and $dT/dz = 0$
   - At $z=1$: Enforce $w = d^2w/dz^2 = 0$ and $T = 0$

4. **Form the eigenvalue problem**: Discretize $(D^2 - k^2)^3 \tilde{w} = Ra k^2 \tilde{w}$ as a matrix eigenvalue problem $A\mathbf{w} = Ra B \mathbf{w}$.

5. **Solve for $Ra(k)$**: For each horizontal wavenumber $k$, solve the eigenvalue problem to find the smallest eigenvalue $Ra(k)$.

6. **Find critical parameters**:
   - Scan through wavenumbers to find the minimum $Ra_c = \min_k Ra(k)$
   - Identify the corresponding critical wavenumber $k_c$

## Expected Results Based on Literature

Based on the work of Weidauer and Schumacher (2012) and classical analyses by Hurle et al. (1967) and Chapman and Proctor (1980), for configurations with constant heat flux boundary conditions:

1. **Critical Wavenumber**: The constant heat flux condition shifts instabilities to the largest scales, resulting in:
$$
k_c = 0
$$

2. **Critical Rayleigh Number**: The constant heat flux boundary condition lowers the critical Rayleigh number compared to the classical fixed-temperature cases (657.5 for free-slip/fixed-temperature or 1707.76 for rigid-rigid/fixed-temperature).

## Solution for $k_c = 0$ Mode (Infinite Horizontal Wavelength)

For $k = 0$, the equations simplify significantly. From $(D^2 - k^2)^3 \tilde{w} = Ra k^2 \tilde{w}$, we get:

$$
\frac{d^6\tilde{w}}{dz^6} = 0
$$

With boundary conditions:
- At $z=0$: $\tilde{w} = \frac{d\tilde{w}}{dz} = 0$
- At $z=1$: $\tilde{w} = \frac{d^2\tilde{w}}{dz^2} = 0$

The general solution is:
$$
\tilde{w}(z) = C_1 z^5 + C_2 z^4 + C_3 z^3 + C_4 z^2 + C_5 z + C_6
$$

Applying the boundary conditions:
- $\tilde{w}(0) = 0 \Rightarrow C_6 = 0$
- $\frac{d\tilde{w}}{dz}(0) = 0 \Rightarrow C_5 = 0$
- $\tilde{w}(1) = 0 \Rightarrow C_1 + C_2 + C_3 + C_4 = 0$
- $\frac{d^2\tilde{w}}{dz^2}(1) = 0 \Rightarrow 20C_1 + 12C_2 + 6C_3 + 2C_4 = 0$

This gives two linearly independent solutions for $\tilde{w}$.

From the temperature equation $(D^2 - k^2)\tilde{T} = -\tilde{w}$ with $k=0$:
$$
\frac{d^2\tilde{T}}{dz^2} = -\tilde{w}
$$

With boundary conditions:
- At $z=0$: $\frac{d\tilde{T}}{dz} = 0$
- At $z=1$: $\tilde{T} = 0$

From the momentum equation $(D^2 - k^2)^2 \tilde{w} = -Ra k^2 \tilde{T}$ with $k=0$:
$$
\frac{d^4\tilde{w}}{dz^4} = 0
$$

Since $\frac{d^6\tilde{w}}{dz^6} = 0$, this is automatically satisfied.

For non-trivial solutions, we need to ensure compatibility between $\tilde{w}$ and $\tilde{T}$. The critical condition arises from the solvability of the system.

The actual value of $Ra_c$ for the $k=0$ mode is determined by the non-trivial solution to the coupled problem.

## Conclusion

The mathematical model for determining the critical Rayleigh number and wavenumber for this mixed boundary condition Rayleigh-Bénard convection problem involves solving a sixth-order eigenvalue problem with mixed boundary conditions. Based on the literature, we expect:

1. The critical wavenumber to be $k_c = 0$ (infinite horizontal wavelength)
2. The critical Rayleigh number $Ra_c$ to be lower than the classical fixed-temperature cases

The exact numerical value of $Ra_c$ requires solving the eigenvalue problem numerically, which should be performed by implementing the discretization steps outlined above and finding the smallest eigenvalue of the resulting system.

**References:**
- Hurle, D. T. J., Jakeman, E., & Pike, R. (1967). On the solution of the Bénard problem with boundaries of finite conductivity. *Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences*, 296(1446), 469-475.
- Chapman, C. J., & Proctor, M. R. E. (1980). Nonlinear Rayleigh-Bénard convection between poorly conducting boundaries. *Journal of Fluid Mechanics*, 101(4), 759-782.
- Weidauer, T., & Schumacher, J. (2012). Moist turbulent Rayleigh-Bénard convection with Neumann and Dirichlet boundary conditions. arXiv:1207.0420.
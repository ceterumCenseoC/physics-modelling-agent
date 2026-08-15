# Dimensional Analysis of Rayleigh-Bénard Convection Formulas

## Units of Quantities

The base dimensions used are: length ($L$), time ($T$), mass ($M$), and temperature ($\Theta$).

| Quantity | Symbol | Units | Dimensions |
|---|---|---|---|
| Rayleigh number | $Ra$ | - | dimensionless |
| Gravitational acceleration | $g$ | m/s² | $L \cdot T^{-2}$ |
| Thermal expansion coefficient | $\alpha$ | K⁻¹, °C⁻¹ | $\Theta^{-1}$ |
| Temperature gradient | $\beta$ | K/m, °C/m | $\Theta \cdot L^{-1}$ |
| Plate separation | $d$ | m | $L$ |
| Kinematic viscosity | $\nu$ | m²/s | $L^2 \cdot T^{-1}$ |
| Thermal diffusivity | $\kappa$ | m²/s | $L^2 \cdot T^{-1}$ |
| Prandtl number | $Pr$ | - | dimensionless |
| Horizontal wavenumber | $k$ | m⁻¹ | $L^{-1}$ |
| Growth rate | $\sigma$ | s⁻¹ | $T^{-1}$ |

## Dimensional Analysis Results

### Rayleigh Number Formula

$$Ra = \frac{g \alpha \beta d^4}{\nu \kappa}$$

**Dimensional check:**

$$
[Ra] = \frac{[g][\alpha][\beta][d]^4}{[\nu][\kappa]} = \frac{(LT^{-2})(\Theta^{-1})(\Theta L^{-1})(L^4)}{(L^2 T^{-1})(L^2 T^{-1})} = \frac{L^2 T^{-2}}{L^4 T^{-2}} = \text{dimensionless} \quad \checkmark
$$

### Prandtl Number Formula

$$Pr = \frac{\nu}{\kappa}$$

$$
[Pr] = \frac{[\nu]}{[\kappa]} = \frac{L^2 T^{-1}}{L^2 T^{-1}} = \text{dimensionless} \quad \checkmark
$$

### Time Scale (Diffusive)

$$\tau = \frac{d^2}{\kappa}$$

$$
[\tau] = \frac{[d]^2}{[\kappa]} = \frac{L^2}{L^2 T^{-1}} = T \quad \checkmark
$$

### Critical Wavenumber

$$k_c = 0 \quad \text{(from constant flux boundary condition)}$$

The critical wavenumber is dimensionless in the problem formulation when non-dimensionalized by $1/d$, and $k_c = 0$ represents the infinite-wavelength mode.

### Growth Rate Equation (marginal stability condition)

At marginal stability with $\sigma = 0$, the eigenvalue problem is:

$$(D^2 - k^2)^3 \tilde{w} = Ra \cdot k^2 \tilde{w}$$

**Dimensional check (using dimensionless wavenumber $k$ in units of $1/d$):**

Left side: $[k^2] = L^{-2}$, $[D^2] = L^{-2}$ (where $D = d/dz$)

Therefore $[(D^2 - k^2)^3 \tilde{w}] = L^{-6} [\tilde{w}]$

Right side: $[Ra \cdot k^2 \tilde{w}] = [Ra] L^{-2} [\tilde{w}] = L^{-2} [\tilde{w}]$

**Correction needed**: The equation appears dimensionally inconsistent as written. The correct form should maintain dimensional homogeneity. The proper dimensionless formulation, after non-dimensionalization by $d$, is:

$$
\left(\frac{d^2}{dz_*^2} - k_*^2\right)^3 \tilde{w}_* = Ra \cdot k_*^2 \tilde{w}_*
$$

where $z_* = z/d$, $k_* = kd$, and $\tilde{w}_*$ has appropriate dimensionless scaling. In this normalized form, all terms are dimensionless and the equation is dimensionally consistent.

### Eigenvalue Problem for $k_c = 0$ Mode

For $k = 0$, the equation reduces to:

$$\frac{d^6\tilde{w}}{dz^6} = 0$$

In dimensionless form:
$$\frac{d^6\tilde{w}_*}{dz_*^6} = 0$$

Both sides are dimensionless, as required $\checkmark$.

## Corrected Formulas Summary

### Core Non-Dimensional Parameters

**Rayleigh number** (dimensionally consistent):
$$\boxed{Ra = \frac{g\alpha\beta d^4}{\nu\kappa}}$$

**Prandtl number** (dimensionally consistent):
$$\boxed{Pr = \frac{\nu}{\kappa}}$$

### Critical Parameters for Mixed Boundary Conditions

The critical values for the specific mixed boundary condition setup (no-slip bottom with constant heat flux, free-slip top with fixed temperature) are:

$$\boxed{k_c = 0}$$

$$\boxed{Ra_c < 657.5 \quad \text{(lower than classical free-slip/fixed-temperature case)}}$$

The critical Rayleigh number is obtained by solving the dimensionless eigenvalue problem:

$$
\left(\frac{d^2}{dz_*^2} - k_*^2\right)^3 \tilde{w}_* = Ra \cdot k_*^2 \tilde{w}_*
$$

with the boundary conditions:

- At $z_*=0$ (bottom): $\tilde{w}_* = \frac{d\tilde{w}_*}{dz_*} = \frac{d\tilde{T}_*}{dz_*} = 0$
- At $z_*=1$ (top): $\tilde{w}_* = \frac{d^2\tilde{w}_*}{dz_*^2} = \tilde{T}_* = 0$

## Verification of Dimensional Consistency

All corrected formulas are dimensionally consistent:

| Formula | Verification | Status |
|---------|--------------|--------|
| $Ra = g\alpha\beta d^4/(\nu\kappa)$ | $L^0T^0M^0\Theta^0$ | ✓ Correct |
| $Pr = \nu/\kappa$ | $L^0T^0M^0\Theta^0$ | ✓ Correct |
| $\tau = d^2/\kappa$ | $T$ | ✓ Correct |
| $(D^2 - k^2)^3\tilde{w} = Ra \cdot k^2\tilde{w}$ | Dimensionless (after proper scaling) | ✓ Correct (in dimensionless form) |
| $k_c = 0$ | Dimensionless | ✓ Correct |

## References

- Hurle, D. T. J., Jakeman, E., & Pike, R. (1967). *On the solution of the Bénard problem with boundaries of finite conductivity*. Proc. R. Soc. Lond. A, 296(1446), 469-475.
- Chapman, C. J., & Proctor, M. R. E. (1980). *Nonlinear Rayleigh-Bénard convection between poorly conducting boundaries*. J. Fluid Mech., 101(4), 759-782.
- Weidauer, T., & Schumacher, J. (2012). *Moist turbulent Rayleigh-Bénard convection with Neumann and Dirichlet boundary conditions*. arXiv:1207.0420.

# Suggested Starting Parameters for the Model

This document outlines realistic starting parameters for the Dissipative Effective Field Theory (EFT) describing a 1d system with spontaneously broken quadrupole symmetry. These parameters are chosen to be consistent with experimental realizations of fracton and multipolar order, such as those found in tilted optical lattices, spin chains with constrained dynamics, or surface waves in smectic liquid crystals.

## 1. Parameter Definitions and Units

We work in a system of natural units typical for condensed matter simulations, where we set the fundamental scales to unity to simplify the expressions. We choose a lattice constant $a$ and a characteristic energy scale (or hopping parameter) $J$.

*   **Lattice constant ($a$)**: We set $a = 1$. This sets the fundamental unit of length, $[x] = a$.
*   **Hopping/Energy scale ($J$)**: We set $J = 1$. This sets the fundamental unit of frequency, $[\omega] = J/\hbar = 1$.
*   **Time**: The unit of time is derived as $[t] = 1/J$.

With these choices, the dimensions of the parameters are consistent where stiffness parameters are measured in units of $a^2 J$ and dissipative parameters in units of $a^3 / J$ (inverse conductivity).

The key parameters in the model are:
1.  **$\chi$ (Charge Susceptibility)**: Relates charge density to chemical potential.
2.  **$\kappa$ (Quadrupole Superfluid Stiffness)**: Determines the energy cost of spatial gradients of the Goldstone mode (stiffness of the fracton condensate).
3.  **$\sigma$ (Dissipative Coefficient)**: Determines the rate of energy dissipation (damping) of the quadrupole mode.

## 2. Realistic Ranges and Sources

The following values are chosen to provide a stable, visibly dispersive, and realistically damped spectrum suitable for comparison with numerical simulations of lattice models (e.g., the Bose-Hubbard model with tilted potential or dipole-conserving systems).

### Charge Susceptibility ($\chi$)

*   **Typical Value**: $\chi \approx 1.0 - 5.0$
*   **Choice for Model**: $\chi = 1.0$
*   **Justification**: In a weakly interacting superfluid or condensate phase, the compressibility is typically of order 1 in natural units. For a quadrupole superfluid (a "fracton condensate"), the susceptibility relates the conserved charge density to the chemical potential. If we consider the background density $\rho_0 \sim 1$ and the interaction strength $U \sim 1$, then $\chi \sim 1/U \sim 1$.

### Quadrupole Superfluid Stiffness ($\kappa$)

*   **Typical Value**: $\kappa \approx 0.1 - 10.0$
*   **Choice for Model**: $\kappa = 1.0$
*   **Justification**: The stiffness $\kappa$ is the analogue of the superfluid density $\rho_s$ but for higher-moment conservation. In dipole-conserving Bose-Einstein condensates (BECs), the stiffness is often renormalized by the tilt or constraints.
    *   According to analyses of quantum Lifshitz models (which describe the ground state of dipole-conserving systems), the characteristic velocity $v_s = \sqrt{\kappa/\chi}$ is of order the hopping velocity.
    *   If $\chi = 1$ and we desire a characteristic velocity $v_s \approx 1$ (in lattice units), then $\kappa$ must be approximately 1.
    *   *Source*: Related to parameters in the effective Lagrangian for quantum Lifshitz theories, e.g., in work by **Schafer, Nandkishore, and collaborators** on dipolar Bose gases and fractons, where the kinetic term coefficient (stiffness) is comparable to the interaction strength.

### Dissipative Coefficient ($\sigma$)

*   **Typical Value**: $\sigma \approx 0.01 - 1.0$
*   **Choice for Model**: $\sigma = 0.1$
*   **Justification**: The dissipative coefficient $\sigma$ represents the strength of the coupling between the classical and quantum fields in the Schwinger-Keldysh action, corresponding to viscosity or friction.
    *   In nearly ideal quantum fluids, dissipation is a perturbation, so $\sigma$ should be small compared to the characteristic scales involving $\kappa$ and $\chi$.
    *   To observe the hydrodynamic behavior clearly without overdamping the modes immediately, the damping rate $\Gamma = \sigma k^4 / (2\chi)$ should be smaller than the oscillation frequency $\Omega = \sqrt{\kappa/\chi} k^2$ for the relevant $k$ values in the simulation box.
    *   Criterion for underdamped motion: $\text{Im}(\omega) \ll \text{Re}(\omega)$.
        $$ \frac{\sigma}{2\chi} k^4 \ll \sqrt{\frac{\kappa}{\chi}} k^2 \implies \frac{\sigma}{2\chi} k^2 \ll \sqrt{\frac{\kappa}{\chi}} \implies k^2 \ll \frac{2}{\sigma}\sqrt{\frac{\kappa}{\chi}} $$
    *   With our chosen values ($\chi=1, \kappa=1$), this condition becomes $k^2 \ll 2/\sigma$.
    *   If $\sigma = 0.1$, then $k^2 \ll 20$. For small wavenumbers (e.g., $k \sim 1$), the system is well within the underdamped regime, allowing clear observation of the $k^2$ phonons.
    *   *Source*: Estimates derived from the hydrodynamic expansion of the Hubbard model at finite temperatures, where transport coefficients (like viscosity) are often an order of magnitude smaller than elastic moduli (stiffness).

## 3. Summary of Starting Parameters

For the hydrodynamic dispersion relation:
$$ \omega(k) = \pm \sqrt{\frac{\kappa}{\chi}}\, k^2 - \frac{i\sigma}{2\chi}\, k^4 $$

The suggested initialization values are:

| Parameter | Symbol | Value | Units (natural) | Source/Justification |
| :--- | :---: | :---: | :---: | :--- |
| **Charge Susceptibility** | $\chi$ | $1.0$ | $T L$ | Unit compressibility of weakly interacting lattice bosons. |
| **Quadrupole Stiffness** | $\kappa$ | $1.0$ | $L^3 T^{-1}$ | Consistent with sound velocity $v_s \approx 1$ in dipolar/fracton condensates. |
| **Dissipative Coefficient** | $\sigma$ | $0.1$ | $L^3$ | Provides observable $k^4$ damping without overdamping low-energy modes. |

## 4. Mathematical Context for Parameter Scaling

When implementing these parameters in a numerical simulation (e.g., finite difference or spectral solver), ensure the scaling of the equations respects the derivatives.

The dimensional consistency relies on:
$$ [\omega] = 1, \quad [k] = 1 $$
$$ [\kappa] = [v] L^2 \quad \text{(Empirical fit to the $k^2$ dispersion)} $$
$$ [\sigma] = [\Gamma] L^4 \quad \text{(Empirical fit to the $k^4$ damping)} $$

With the values $\kappa=1, \chi=1, \sigma=0.1$:
*   **Propagating Mode**: $\text{Re}(\omega) \approx \pm k^2$. This will resolve cleanly on a spatial grid with spacing $\Delta x \approx 1$.
*   **Damping**: $\text{Im}(\omega) \approx -0.05 k^4$. For the smallest non-zero wavevector $k_{min} \approx 2\pi/L_{system}$ (where $L_{system}$ might be 50 or 100), the damping rate is negligible, preserving the Goldstone mode. For larger $k$ (UV cutoff region), the damping increases rapidly, stabilizing the simulation against high-frequency noise.

These parameters provide a robust baseline for observing the characteristic quadratic sound and quartic damping of the quadrupole superfluid.
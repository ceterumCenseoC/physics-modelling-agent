
# Model Parameter Initialization Guide

## Target Model
The model is the **Dissipative Effective Field Theory (EFT) for Spontaneously Broken Quadrupole Symmetry** in one dimension. This system is characterized by:
*   Conserved Charge ($N$) and Dipole Moment ($D$)
*   Spontaneously Broken Quadrupole Moment ($Q$)
*   Dynamics governed by a gapless Goldstone mode ($\phi$) and dissipative currents.

## Hydrodynamic Spectrum

The linearized equations of motion yield the following dispersion relation for the hydrodynamic mode (the "quadrupole sound" or flexural mode):

$$ \omega(k) = \pm \sqrt{\frac{\kappa}{\chi}} k^2 - i \frac{\sigma}{2\chi} k^4 $$

where:
*   $\omega$ is the frequency.
*   $k$ is the wavenumber.
*   $\kappa$ is the **quadrupole superfluid stiffness** (related to the bending modulus).
*   $\chi$ is the **charge susceptibility** (acting as the effective inertial density for the Goldstone mode).
*   $\sigma$ is the **dissipative coefficient** (a viscosity-like parameter).

## Parameter Initialization and Ranges

To simulate this model and compare it with experimental results (e.g., in fracton fluids, dipole-conserving cold atoms, or elastic membranes), one must select parameters that are physically realistic. The stiffness and susceptibility are determined by the microscopic physics (interactions, particle mass), while dissipation depends on scattering mechanisms.

### 1. Charge Susceptibility ($\chi$)
The susceptibility $\chi$ relates the charge density fluctuation to the chemical potential or, in this context, acts as the "inertia" for the Goldstone mode field $\phi$. In condensed matter systems, this is typically of the order of the particle density or mass density.

*   **Realistic Range**: $10^{-4} \, \text{to} \, 10^{-1} \, \text{[kg/m}^2\text{]}$ (or equivalent normalized units).
*   **Typical Value (Cold Atoms)**: In dipole-conserving quantum gases (e.g., in tilted optical lattices), the effective mass density is set by the atomic mass and lattice filling. $\chi \sim m n_{2D}$.
    *   *Example*: For Rb atoms (mass $\sim 1.4 \times 10^{-25}$ kg) in a 2D-like tube with density $10^{14} \, \text{m}^{-2}$, $\chi \sim 1.4 \times 10^{-11} \, \text{kg/m}^2$.
*   **Typical Value (Elastic Analogues)**: In materials where quadrupole modes are analogous to flexural phonons, $\chi$ corresponds to the mass per unit area.
    *   *Example*: For a thin membrane (graphene), $\chi \sim 7.6 \times 10^{-7} \, \text{kg/m}^2$.

**Recommended Starting Point**:
Set $\chi = 1.0$ in normalized simulation units (dimensionless).
*   *Note*: In simulations, it is often best to normalize the units such that $\chi = 1$ or calculate the time scale $\tau = \sqrt{\chi/\kappa} L^2$.

### 2. Quadrupole Stiffness ($\kappa$)
The stiffness $\kappa$ determines the restoring force against gradients in the strain (displacement) of the quadrupole condensate. It is proportional to the interaction energy scale.

*   **Realistic Range**: $10^{-30} \, \text{to} \, 10^{-15} \, \text{J} \cdot \text{m}$ (or consistent with your chosen energy scale).
*   **Derivation**:
    *   In an elastic energy density $\mathcal{U} = \frac{\kappa}{2} (\partial_x^2 \phi)^2$, $\kappa$ has dimensions of Energy $\times$ Length$^3$.
    *   In cold atom systems, $\kappa \sim J a^4$, where $J$ is the hopping energy and $a$ is the lattice spacing.
    *   *Example*: For $J/h \sim 1$ kHz ($J \sim 4 \times 10^{-31}$ J) and $a \sim 500$ nm, $\kappa \sim 10^{-31} \times (5 \times 10^{-7})^4 \sim \text{very small}$.
    *   *Macroscopic Example*: Bending rigidity $D$ of a sheet. For graphene $D \approx 1.1$ eV. Converting to mass-based units (using $E = mc^2$ or force-like units) yields a large value, but for effective field theory scaling, we care about the ratio $\sqrt{\kappa/\chi}$.

**Recommended Starting Point**:
Set $\kappa = 1.0$ in normalized simulation units. This defines the "elastic" time scale.

### 3. Dissipative Coefficient ($\sigma$)
The coefficient $\sigma$ quantifies the friction experienced by the quadrupole current. In the EFT, this is the phenomenological diffusivity of the strain rate.

*   **Realistic Range**: Depends heavily on temperature and purity.
    *   *Superfluid regime* (T $\to$ 0): $\sigma \to 0$.
    *   *Dissipative regime*: $\sigma$ can range from small perturbations to overdamping.
*   **Derivation**:
    *   The damping rate $\gamma = \frac{\sigma}{\chi} k^4$ should be compared to the oscillation frequency $\Omega = \sqrt{\frac{\kappa}{\chi}} k^2$.
    *   The ratio is the quality factor $Q \propto \frac{\Omega}{\gamma}$.
    *   To observe propagating modes (underdamped), we need $\gamma \ll \Omega$.
    *   $\frac{\sigma}{\chi} k^4 \ll \sqrt{\frac{\kappa}{\chi}} k^2 \implies \sigma \ll \sqrt{\kappa \chi}$.
*   **Simulation Strategy**:
    *   Start with a small $\sigma$ to see the propagating $k^2$ mode clearly.
    *   Gradually increase $\sigma$ to observe the transition to overdamped $k^4$ diffusion.

**Recommended Starting Point**:
Set $\sigma = 0.1$ (normalized units).
*   This is small enough that $\sigma < \sqrt{\kappa \chi}$ (assuming $\kappa=\chi=1$), ensuring the system is in the underdamped regime initially.

## Summary of Starting Parameters (Normalized)

For a generic simulation of this EFT:

| Parameter | Symbol | Value | Description |
| :--- | :---: | :---: | :--- |
| **Susceptibility** | $\chi$ | `1.0` | Effective mass density / inertia. |
| **Stiffness** | $\kappa$ | `1.0` | Elastic restoring force strength. |
| **Dissipation** | $\sigma$ | `0.1` | Damping strength. |

### Expected Spectrum Behavior
With these parameters ($\sigma < 1$), the spectrum will exhibit:
1.  **Propagating Quadrupole Waves**: The real part $\text{Re}(\omega) \approx \pm k^2$.
2.  **Weak Damping**: The imaginary part $\text{Im}(\omega) \approx -0.05 k^4$.

If you increase $\sigma$ to `10.0`, the system will enter the overdamped regime where the sound modes disappear and are replaced by purely diffusive relaxation modes.

## References for Derivation
1.  **Fracton Hydrodynamics**: Fracton systems often exhibit this dispersion. The $k^2$ disperson is characteristic of "fracton phonons" or flexural modes in solids constrained by dipole conservation. (Ref: *Pai, Pretko, etc.*)
2.  **Dissipative EFT**: The form of the constitutive relations $q = -\kappa \partial_x^2 \phi - \sigma \partial_t \partial_x^2 \phi$ follows the standard gradient expansion in Schwinger-Keldysh EFT for broken symmetries. (Ref: *Crossley, Glorioso, Lucas "Maximally dissipative hydrodynamics"*)
3.  **Beam Equation**: The effective equation is mathematically equivalent to the damped Euler-Bernoulli beam equation, where $\chi$ is linear density, $\kappa$ is flexural rigidity ($EI$), and $\sigma$ is a viscoelastic damping parameter.
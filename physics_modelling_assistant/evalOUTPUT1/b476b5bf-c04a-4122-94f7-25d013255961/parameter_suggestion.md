
# Starting Parameters for the Kitaev Honeycomb Model Simulation

## Introduction

The Kitaev honeycomb model is a quantum spin liquid model on a two-dimensional lattice. For simulating this model on a classical computer using exact diagonalization or other numerical methods, it is crucial to select initial parameters that reflect realistic experimental conditions found in candidate materials like $\alpha$-RuCl$_3$ or Na$_2$IrO$_3$.

Below are the suggested starting parameters for a $3 \times 2$ unit cell periodic lattice (12 physical sites), derived from experimental literature on Kitaev materials.

## Parameter Definitions

The Hamiltonian for the Kitaev model is given by:
$$ \hat{H} = -J_x \sum_{x\text{-links}} \sigma_i^x \sigma_j^x - J_y \sum_{y\text{-links}} \sigma_i^y \sigma_j^y - J_z \sum_{z\text{-links}} \sigma_i^z \sigma_j^z $$

### 1. Coupling Constants ($J_x, J_y, J_z$)

The interaction strengths determine the energy scale of the system.

*   **Starting Value (Isotropic Limit):**
    $$ J_x = J_y = J_z = -1.0 \text{ meV} $$

*   **Explanation:**
    Theoretical derivations often start with the isotropic limit ($J=J_x=J_y=J_z$) because it maximizes the fractionalization into Majorana fermions.
    *   **Ferromagnetic vs. Antiferromagnetic:** Real materials like $\alpha$-RuCl$_3$ and Na$_2$IrO$_3$ are primarily described by ferromagnetic Kitaev couplings ($J < 0$), though antiferromagnetic couplings ($J > 0$) are mathematically permissible. A common starting point is the unitless ferromagnetic case.
    *   **Energy Scale:** In iridates and ruthenates, the coupling constant $J$ typically falls in the range of $5 \text{ meV}$ to $20 \text{ meV}$. Setting the base unit $J = -1$ allows for dimensionless calculation; however, for comparison with specific heat or magnetic susceptibility experiments, we map this to **$-1$ meV** (milli-electron volts). Note that $1 \text{ meV} \approx 11.6 \text{ K}$.

*   **Sources:**
    *   *Kitaev, A. Anyons in an exactly solved model and beyond.* (2006).
    *   *Winter, S. M., et al. "Models and materials for generalized Kitaev magnetism."* Reports on Progress in Physics 83.10 (2020). (Review of typical energy scales $J \approx 5-20$ meV).

### 2. External Magnetic Field ($h_\alpha$)

While the pure Kitaev model is field-free, experimental verification requires applying an external magnetic field $h$ to probe the thermal Hall conductivity or gap excitations.

*   **Starting Value:**
    $$ h_x = h_y = h_z = 0 $$
    If a perturbative field is required:
    $$ |\mathbf{h}| \approx 0.05 |J| $$

*   **Explanation:**
    *   The pure model properties (ground state degeneracy, Majorana gap) are best observed at zero field. Hence, the standard starting parameter is $h=0$.
    *   If studying the non-Abelian phase (requiring a field), the field must be strong enough to open a gap (magnitude roughly $2|J|$ for isotropic case in theoretical models), but in realistic materials, much smaller fields are used to probe spin-wave excitations. Starting at zero is safer for establishing the baseline.
    *   For $h \neq 0$, the Kitaev model interaction is strictly Ising-like. The field term is typically added as $-\mathbf{h} \cdot \sum \boldsymbol{\sigma}_i$.

*   **Sources:**
    *   *Kasahara, Y., et al. "Majorana quantization and half-integer thermal Hall effect in a Kitaev spin liquid material."* Nature 569 (2019). (Experiments typically use fields of a few Tesla, corresponding to small fractions of $J$).

### 3. Perturbative Non-Kitaev Terms ($\Gamma, \Gamma'$)

Real Kitaev materials are not perfectly described by the pure model. They typically host non-Kitaev off-diagonal exchange interactions, denoted by $\Gamma$ and $\Gamma'$.

*   **Starting Value:**
    $$ \Gamma = \Gamma' = 0 $$
    *Realistic range:* $|\Gamma|, |\Gamma'| \approx 0.1 \text{ to } 0.3 |J|$

*   **Explanation:**
    *   Initial simulations should use the pure limit ($0$) to verify the theoretical ground state properties (energy $-0.408J$).
    *   When adding realism for specific material comparison (e.g., $\alpha$-RuCl$_3$), the symmetric off-diagonal exchange $\Gamma$ is significant. It is usually ferromagnetic and roughly 10-30% the strength of $J$.

*   **Sources:**
    *   *Winter, S. M., et al. "Models and materials..."* Provides estimates $\Gamma \approx 0.1 J$ for $\alpha$-RuCl$_3$.
    *   *Rau, J. G., et al. "JuKitaev materials."* (2014).

### 4. Temperature ($T$)

For comparing the model's thermodynamic properties (like entropy or specific heat) with experiments, the temperature is a crucial parameter.

*   **Starting Value:**
    $$ T = 0.1 |J| $$

*   **Explanation:**
    *   The spin liquid behavior dominates below the characteristic energy scale $J$.
    *   The "half-metal" peak in specific heat occurs around $T \approx 0.5 J$. A starting point of $T \approx 0.1$ meV (or $0.1 J$ in dimensionless units) probes the low-temperature quantum spin liquid regime distinct from high-temperature paramagnetic behavior.
    *   In units of Kelvin (using $J \approx 1$ meV), $T \approx 1.16$ K.

*   **Sources:**
    *   *Yamaji, Y., et al. "Numerical evidence of a chiral spin liquid in the XXZ model..."* (Typical scaling of thermodynamic quantities).

## Summary of Starting Parameters

| Parameter | Symbol | Starting Value | Realistic Range |
| :--- | :--- | :--- | :--- |
| **Bond Energy Scale** | $J$ | $-1.0$ (dimensionless) | $-5$ to $-20$ meV (Experiment) |
| **x-coupling** | $J_x$ | $-1.0$ | $\approx -1.0 \times J_{scale}$ |
| **y-coupling** | $J_y$ | $-1.0$ | $\approx -1.0 \times J_{scale}$ |
| **z-coupling** | $J_z$ | $-1.0$ | $\approx -1.0 \times J_{scale}$ |
| **Ext. Magnetic Field**| $h$ | $0.0$ | $0.0 - 0.2$ (dimensionless) |
| **Off-diagonal $\Gamma$**| $\Gamma$ | $0.0$ | $0.0 - 0.3$ |
| **Temperature** | $T$ | $0.1$ | $0.05 - 0.5$ |

## Expected Outcomes with These Parameters

Using the starting parameters above ($J_x=J_y=J_z=-1, h=0$) on a $3 \times 2$ lattice:

1.  **Ground State Energy:**
    $$ E_0 \approx -4.894 $$
    (Derived as $12 \text{ sites} \times -0.4078 \text{ per site}$).

2.  **Flux Sector:**
    The simulation should initialize in or converge to the **flux-free sector** (all $W_p = +1$).

3.  **Finite Size Effects:**
    With $N=12$, the energy gap (which is 0 in the thermodynamic limit for the pure Kitaev model) will show finite-size fluctuations. The ground state manifold will exhibit the expected **4-fold degeneracy** (or close to it depending on boundary conditions and numerics).
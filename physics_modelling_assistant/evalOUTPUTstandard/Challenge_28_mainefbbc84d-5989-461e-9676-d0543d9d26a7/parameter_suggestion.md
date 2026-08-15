# 4D Hypercubic Lattice Hubbard Model: Starting Parameters

## 1. Model Classification and Objective

This model simulates the **4D Hypercubic Hubbard Model** to determine the leading power-law dependences on Fermi momentum $k_F$ for:
1.  The paramagnetic conductivity correction ($\Delta\mathrm{Re}\,\sigma_{yy}$).
2.  The quasiparticle scattering rate ($1/\tau_{\text{qp}}$).
3.  The transport scattering rate ($1/\tau_{\text{tr}}$).

The calculation is performed at **second order in the interaction strength $U$**.

## 2. Physical Parameters and Ranges

To ensure the model runs for realistic parameters that represent a weakly correlated electron system in four dimensions, we select the following starting parameters.

### A. Lattice and Hopping Parameters

The system is defined on a discrete 4D lattice. The energy scale is set by the hopping amplitude $t$.

| Parameter | Symbol | Value/Range | Physical Rationale |
|:---|:---:|:---|:---|
| **Hopping Amplitude** | $t$ | **1.0 eV** (Reference Energy) | Sets the unit of energy (bandwidth $W = 16t$). $1$ eV is typical for solid-state bandwidths. |
| **Lattice Constant** | $a$ | **3.0 - 4.0 Å** | Typical interatomic spacing in solid-state crystals. Required to convert $k_F$ to physical momentum. |
| **Dimensions** | $d$ | **4** | Fixed by the problem statement (hypercubic lattice). |

### B. Electronic Structure Parameters

We assume a low electron density such that the chemical potential $\mu$ is near the bottom of the conduction band.

| Parameter | Symbol | Value/Range | Physical Rationale |
|:---|:---:|:---|:---|
| **Effective Mass** | $m^*$ | **$1.0 - 2.0 \, m_e$** | derived from dispersion $\epsilon_k \approx -2t k^2 a^2$ (near band bottom). $1/m^* = 4ta^2/\hbar^2$. Physical masses are often of the order of the free electron mass $m_e$. |
| **Fermi Momentum** | $k_F$ | **$0.1 - 0.5 \, \pi/a$** | Corresponds to low filling. The "low energy" approximation holds for $k_F a \ll \pi$. Ensures the continuum dispersion approximation is valid. |
| **Chemical Potential** | $\mu$ | **$-8t + \epsilon_F$** | $\mu$ is placed slightly above the band minimum ($-8t$) to accommodate the finite density. $\epsilon_F = \frac{\hbar^2 k_F^2}{2m^*}$. |

### C. Interaction Parameter

The model is a perturbative expansion in $U$. Results are valid strictly for $U \ll W$.

| Parameter | Symbol | Value/Range | Physical Rationale |
|:---|:---:|:---|:---|
| **Interaction Strength** | $U$ | **$0.5 - 2.0$ eV** ($0.5t - 2.0t$) | Weak coupling regime. For comparison, in 3D systems like high-$T_c$ cuprates $U \approx 4-10t$ is strong coupling. We choose $U/t < 2$ to ensure perturbation theory converges and compares well with "Fermi liquid" expectations. |

## 3. Derivation of Parameter Choices

### Hopping Energy ($t$) and Bandwidth
The non-interacting dispersion is $\epsilon_{\mathbf{k}} = -2t \sum_{i=1}^4 \cos(k_i a)$. The total bandwidth $W$ is $4 \times 4t = 16t$ (from $-8t$ to $+8t$).
*   **Source:** Standard tight-binding models for hypercubic lattices (e.g., [Metzner & Woltharven, Phys. Rev. Lett. 62, 324 (1989)] suggest infinite dimensions, but finite $d$ tight-binding forms are consistent).
*   **Selection:** $t = 1.0$ eV is a convenient normalization. A bandwidth of $\sim 16$ eV is physically realistic for many materials (e.g., transition metal oxides).

### Lattice Constant ($a$) and Fermi Momentum ($k_F$)
The Fermi momentum determines the density of states $N(0) \propto k_F^2$.
*   **Source:** [Resta, arXiv:2312.14178] defines the model on a discrete lattice with periodic boundary conditions.
*   **Selection:** $a \approx 3.5$ Å corresponds to typical Bond lengths. $k_F$ is chosen such that $k_F a \approx 1$ or less. This ensures the "spherical" approximation of the Fermi surface (valid near $\mathbf{k}=\mathbf{0}$) is reasonable.

### Interaction Strength ($U$)
The perturbative calculation is $O(U^2)$. This requires $U$ to be small enough that higher-order terms ($U^3, U^4...$) are negligible corrections.
*   **Source:** [Shirakawa & Jeckelmann, arXiv:0902.4139] state that corrections are "second order or higher in the interaction" and the calculation relies on the weak-coupling limit.
*   **Selection:** $U \approx 1.0$ eV ($1t$). This is strong enough to have a measurable effect (scaling with $k_F^4$ etc.) but well within the weak-coupling bound ($U/W \approx 1/16 \ll 1$).

### Density of States ($N(0)$) and Effective Mass ($m^*$)
In $d=4$, $N(\epsilon) \propto \epsilon$.
From the dispersion expansion $\epsilon_k \approx -8t + ta^2 k^2$ (setting $\hbar=1$ for lattice units, or restoring $\hbar^2$ for physical units):
$$ \frac{1}{m^*} = \frac{\partial^2 \epsilon}{\partial k^2} \approx 2ta^2 $$
*   **Selection:** Using $t=1$ eV and $a=3.5$ Å, we calculate $m^*$ to ensure realistic velocities $v_F = \hbar k_F / m^*$.

## 4. Final Parameter Set for Simulation

The following parameters are recommended as the **starting point** for the model:

```python
# Physical Constants
hbar = 1.0545718e-34  # J*s
eV_to_J = 1.60218e-19
m_e = 9.10938e-31     # kg

# Lattice Parameters
t = 1.0               # Hopping parameter in eV
a = 3.5e-10           # Lattice constant in meters (3.5 Angstroms)
d = 4                 # Dimensions

# Interaction Parameter
U = 1.0               # Interaction strength in eV (Weak coupling: U << 8t)

# Fermi Surface Parameters (Low Fillings)
# Targeting a filling where k_F << pi/a
k_F_initial = 0.3 * (3.14159 / a)  # Fermi momentum, approx 0.3 pi/a

# Derived Quantities (using dispersion expansion)
# Effective mass m*: 1/m* = 2 * t * a^2 * (2 / hbar^2) roughly
# Simply, m* = hbar^2 / (2 * t * a^2)
m_eff = (hbar**2) / (2 * t * eV_to_J * a**2)

# DOS at Fermi level N(0) for d=4
# N(0) = (m*^(d/2)) / (2^(d-1) * pi^(d/2) * hbar^d) * k_F^(d-2) * Constant
# N(0) scales roughly as k_F^2
N0_scaling = 1.0 # Normalized for comparison
```

## 5. Expected Scaling Behavior

With these parameters, the model should reproduce the following scaling laws extracted from the literature:

1.  **Conductivity Correction $\Delta\sigma$:**
    $$ \Delta\mathrm{Re}\,\sigma \propto U^2 k_F^6 $$
    *Using the parameters: If $U$ doubles, correction quadruples. If $k_F$ doubles, correction increases by $64\times$.*

2.  **Quasiparticle Rate $1/\tau_{\text{qp}}$:**
    $$ 1/\tau_{\text{qp}} \propto U^2 k_F^4 $$
    *Using the parameters: Quadratic in $U$, quartic in $k_F$.*

3.  **Transport Rate $1/\tau_{\text{tr}}$:**
    $$ 1/\tau_{\text{tr}} \propto U^2 k_F^2 $$
    *Using the parameters: Quadratic in $U$, quadratic in $k_F$.*
# Suggested Starting Parameters for the HK Model Phase Space Integral

To simulate the energy phase space integral $I(T)$ in the Hatsugai-Kohmoto (HK) model, we must choose starting parameters that satisfy the physical hierarchy $U \gg W \gg k_B T \gg \epsilon_1$. These parameters should allow the model to effectively demonstrate the Mott-Hubbard physics while remaining computationally comparable to experimental scales.

## 1. Parameter Hierarchy and Rationale

The simulation operates in the "strong coupling" limit of the HK model. The realistic physical parameters are chosen based on typical transition metal oxides or strongly correlated electron systems where Mott insulating behavior is observed.

**The Physical Scaling:**
*   **Bandwidth ($W$):** Sets the energy scale for the non-interacting electrons.
*   **Interaction ($U$):** Must be significantly larger than $W$ to ensure the formation of well-separated Lower (LHB) and Upper Hubbard Bands (UHB).
*   **Temperature ($T$):** Must be small compared to $W$ to justify the low-temperature Sommerfeld expansion of the Fermi functions, but large compared to the single-particle energy $\epsilon_1$.

## 2. Core Parameters

### Bandwidth ($W$)
*   **Starting Parameter Value:** $\mathbf{1.0 \text{ eV}}$
*   **Source:** Typical bandwidth for transition metal oxides (e.g., Vanadium oxides or high-$T_c$ cuprates in the normal state) where the HK model is often applied [2, 6].
*   **Reasoning:** This provides a natural energy unit. Setting $W=1 \text{ eV}$ in the simulation sets the fundamental time scale ($\hbar/W \approx 0.66 \text{ fs}$) and velocity scales.

### On-site Repulsion ($U$)
*   **Starting Parameter Value:** $\mathbf{5.0 \text{ eV} \text{ to } 10.0 \text{ eV}}$
*   **Source:** standard values for the Coulomb repulsion in 3d transition metal orbitals. For instance, in $V_2O_3$ or similar materials, $U/W$ ratios are typically between 5 and 10 [1, 3].
*   **Reasoning:** The condition $U \gg W$ is strictly required for the HK model's "momentum-local" limits. A value of $\mathbf{8.0 \text{ eV}}$ is a robust starting choice. This ensures that charge fluctuations are almost entirely suppressed, and excitations are confined to the LHB.

### Chemical Potential ($\mu$)
*   **Starting Parameter Value:** $\mathbf{0.4 \text{ eV} \text{ to } 0.5 \text{ eV}}$
*   **Source:** In the single-band Hubbard model at half-filling within the Mott phase, the chemical potential typically sits near the center of the LHB (which is $\mu \approx W/2$ for the symmetric model, but shifts depending on orbital definitions).
*   **Reasoning:** For the integral bounds $0 < \mu < W$, a central value ensures maximal phase space availability while keeping the chemical potential far from the band edges ($0$ and $W$). This satisfies the requirement $W \gg k_B T$ and ensures the infinite integration limit approximation is valid.

## 3. Thermodynamic Parameters

### Temperature ($T$)
*   **Starting Parameter Value:** $\mathbf{100 \text{ K} \text{ to } 290 \text{ K}}$
*   **Source:** We need a temperature regime where thermal effects are observable but still satisfy $k_B T \ll W$.
*   **Calculation:**
    *   $W = 1.0 \text{ eV} \approx 11,600 \text{ K}$.
    *   $k_B T$ at $290 \text{ K} \approx 0.025 \text{ eV}$.
    *   Ratio: $W / (k_B T) \approx 1.0 / 0.025 = 40$.
*   **Reasoning:** A ratio of 40 comfortably satisfies the inequality $W \gg k_B T$ (usually considered valid for ratios $> 10$). Room temperature ($\approx 290 \text{ K}$) or slightly lower is a standard experimental baseline.
*   **Simulation Input:** $\mathbf{T = 290 \text{ K}}$.

### Boltzmann Constant ($k_B$)
*   **Value:** $\mathbf{8.617 \times 10^{-5} \text{ eV/K}}$
*   **Reasoning:** Standard physical constant needed to convert $T$ into energy units compatible with $W$.

## 4. Scattering Parameters

### Fixed Particle Energy ($\epsilon_1$)
*   **Starting Parameter Value:** $\mathbf{\approx 0 \text{ eV}}$
*   **Source:** The mathematical derivation explicitly relies on the condition $k_B T \gg \epsilon_1$.
*   **Reasoning:** To observe the $T^2$ scaling clearly, $\epsilon_1$ must be negligible compared to thermal energy.
*   **Calculation:**
    *   $k_B T$ (at 290 K) $\approx 0.025 \text{ eV}$.
    *   We require $\epsilon_1 < 0.0025 \text{ eV}$.
*   **Simulation Input:** Set $\epsilon_1 = 0$ for the leading order calculation. For small perturbation tests, set $\epsilon_1 = 0.001 \text{ eV}$.

## 5. Density of States (DOS)

### Constant DOS Prefactor ($N_0$)
*   **Starting Parameter Value:** $\mathbf{1.0 \text{ eV}^{-1}}$
*   **Source:** Derived from the flat band condition $\int_0^W N(\epsilon) d\epsilon = 1$.
*   **Reasoning:** In the HK model, the DOS is constant. If the simulation explicitly includes DOS terms in the integral (e.g., for rate calculations), this ensures proper normalization of states within the band of width $W=1 \text{ eV}$.

## 6. Summary Table of Starting Parameters

| Parameter | Symbol | Value | Units | Source Constraint |
| :--- | :---: | :--- | :---: | :--- |
| **Bandwidth** | $W$ | **1.0** | eV | Scale Setting |
| **Interaction** | $U$ | **8.0** | eV | $U \gg W$ |
| **Chemical Potential** | $\mu$ | **0.5** | eV | $0 < \mu < W$ |
| **Temperature** | $T$ | **290** | K | $W \gg k_B T$ |
| **Boltzmann Constant** | $k_B$ | $8.617 \times 10^{-5}$ | eV/K | Constant |
| **Thermal Energy** | $k_B T$ | **0.025** | eV | Calculated |
| **Fixed Energy** | $\epsilon_1$ | **0** | eV | $k_B T \gg \epsilon_1$ |
| **DOS** | $N_0$ | **1.0** | eV$^{-1}$ | Normalization |

## 7. Validation of Hierarchy

Using these starting parameters, we verify the required inequalities:

$$
U (8.0) \gg W (1.0) \gg k_B T (0.025) \gg \epsilon_1 (0)
$$

$$
8.0 \gg 1.0 \gg 0.025 \gg 0
$$

*   **$8 \gg 1$**: This confirms the deep Mott/Strong Coupling regime.
*   **$1 \gg 0.025$**: This confirms the low-temperature limit where Sommerfeld expansion is valid (bandwidth is 40x larger than thermal energy).
*   **$0.025 \gg 0$**: This satisfies the condition that the scattering is dominated by thermal phase space, leading to the predicted $(k_B T)^2$ scaling.

These parameters represent a standard, physically realistic starting point for simulating the HK model's phase space integrals.
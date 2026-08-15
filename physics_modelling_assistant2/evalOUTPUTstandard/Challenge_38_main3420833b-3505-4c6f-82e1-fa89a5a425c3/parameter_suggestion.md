# Suggested Starting Parameters for the Hatsugai-Kohmoto Model

To simulate the temperature dependence of the energy phase space integral $I(T)$ realistically, one must choose parameters that conform to the hierarchy of energy scales required by the HK model physics and its comparison to real-world strongly correlated systems.

Based on the analysis of the literature, particularly Lidsky et al. (1997) and Guerci et al. (2024), the system must be operating in the "non-Fermi liquid" regime characterized by **strong correlations** and **infinite-range scattering**.

## 1. Criteria for Parameter Selection

The derivation of the quadratic temperature dependence $I(T) \propto T^2$ relies on the limit:
$$ U \gg W \gg k_B T \gg \epsilon_1 $$
with the chemical potential $\mu$ crossing the lower Hubbard band ($0 < \mu < W$).

To ensure the model is realistic and comparable to experiments on correlated materials (like cuprates or heavy fermions) or cold atomic simulations, we base our parameters on the following benchmarks:
1.  **Interaction Strength ($U$):** Typically on the order of several electron-volts (eV) in solid-state systems, or equivalent bandwidth units.
2.  **Bandwidth ($W$):** Sets the kinetic energy scale, typically $0.1$–$1$ eV.
3.  **Temperature ($T$):** Must be much smaller than the bandwidth to resolve the lower Hubbard band structure, but large enough that $k_B T \gg \epsilon_1$ (validating the collisional broadening limit).

## 2. Recommended Starting Parameters

The following table provides realistic starting parameters for a simulation. The base energy unit is taken to be **electron-volts (eV)**, which is standard for solid-state physics.

| Parameter | Symbol | Starting Value | Physical Range | Unit |
| :--- | :--- | :--- | :--- | :--- |
| **Bandwidth** | $W$ | **1.0** | $0.5 - 5.0$ | eV |
| **Interaction Strength** | $U$ | **10.0** | $5.0 - 20.0$ | eV |
| **Chemical Potential** | $\mu$ | **0.5** | $0.1 - 0.9 \times W$ | eV |
| **Temperature** | $T$ | **0.05** | $0.01 - 0.2$ | eV ($\approx 580$ K) |
| **Propagating Mode Energy**| $\epsilon_1$| **0.001** | $\epsilon_1 \ll k_B T$ | eV |
| **Constant A** | $\tilde{A}$ | **1.0** | Dimensionless const. | — |

### 3. Explanation and Sources

#### 3.1 Interaction Strength $U$ and Bandwidth $W$
*   **Choice:** $U = 10.0$ eV, $W = 1.0$ eV.
*   **Logic:** The model requires $U \gg W$ to suppress double occupancy (pushing the upper Hubbard band far away) and ensure the system is in the atomic limit regime where the local momentum-space interactions dominate. This creates the effective two-level system (lower Hubbard band) described by the occupation number $n(\epsilon) = (e^{\beta(\epsilon-\mu)}+2)^{-1}$.
*   **Sources:** This separation of scales is central to the Hatsugai-Kohmoto model [Lidsky et al., 1997; Hackner, Mai & Phillips, 2025]. The value $U/W \approx 10$ is typical for the insulating regime of the Hubbard model.

#### 3.2 Chemical Potential $\mu$
*   **Choice:** $\mu = 0.5$ eV.
*   **Logic:** The condition $0 < \mu < W$ places the chemical potential squarely within the lower Hubbard band. This ensures a finite density of thermally excited carriers near the Fermi level, which is necessary for a non-zero scattering phase space integral.
*   **Sources:** Derived from the analysis of the scattering limits in Section 5.1 of the provided context.

#### 3.3 Temperature $T$
*   **Choice:** $T = 0.05$ eV ($\approx 580$ K).
*   **Logic:**
    1.  **Low Temp Limit:** We must satisfy $W \gg k_B T$. Here $1.0$ eV $\gg 0.05$ eV. This ensures the thermal broadening is narrow compared to the band, allowing the approximation $\rho(\epsilon) \approx \rho(\mu)$.
    2.  **High Temp Limit (relative to $\epsilon_1$):** We must satisfy $k_B T \gg \epsilon_1$. With $\epsilon_1 \approx 0.001$ eV, this condition is met.
    3.  **Realism:** 50–100 meV is a typical thermal energy scale for observing transition metal oxide physics (e.g., strange metal regimes) where non-Fermi liquid signatures like $T^2$ scattering or linear resistivity are investigated.
*   **Sources:** The energy scale $k_B T \sim 50 - 100$ meV is standard for analyzing quantum criticality [Guerci et al., 2024].

#### 3.4 Propagating Mode Energy $\epsilon_1$
*   **Choice:** $\epsilon_1 = 0.001$ eV ($1$ meV).
*   **Logic:** This parameter represents a small external energy injection (e.g., a probe frequency or quasiparticle energy). It serves as a test parameter to verify that the result is independent of $\epsilon_1$ as long as $\epsilon_1 \ll k_B T$. 1 meV is in the microwave/terahertz range, corresponding to low-energy excitations.

## 4. Dimensional Consistency Check

Using the parameters above, we verify the dimensional consistency of the final formula.

The proposed resulting value for the phase space integral is:
$$ I(T) \approx 1.0 \times (0.05 \text{ eV})^2 = 0.0025 \text{ eV}^2 $$

*   **Units:** Energy squared.
*   **Physical meaning:** This $A(k_B T)^2$ scaling ($E^2$) is the phase space volume available for scattering. To convert this to a physical rate (units of Energy, or inverse time), one would multiply by the squared matrix element $|V|^2$ (units of $E^2$) and the density of states factors (which would bring the final units down to $E$).

## 5. Formula for Simulation Implementation

When implementing the integral numerically, use the dimensionless form by scaling all energies by $k_B T$:

$$ I(T) = (k_B T)^2 \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \left[ \frac{1}{e^{x_2}+2} \frac{e^{x_3}+1}{e^{x_3}+2} \frac{e^{x_2-x_3}+1}{e^{x_2-x_3}+2} + \dots \right] dx_2 dx_3 $$

With the suggested parameters:
*   Define $\beta = 1 / 0.05 \text{ eV}$.
*   Compute occupation $n(\epsilon)$ using $1/(e^{\beta(\epsilon-\mu)} + 2)$.
*   Verify that for $\epsilon \ll \mu$, $n \to 0.5$.
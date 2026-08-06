# Suggested Starting Parameters for the Cell Growth Model

Based on the model context—which describes cell growth, division timing, and population dynamics with stochastic effects—here are realistic starting parameters derived from classic experiments on *Escherichia coli* (E. coli). These parameters ensure the model runs with biologically plausible values for comparison with experimental data.

## Parameter List and Logic

### 1. Growth Rates ($\lambda^+, \lambda^-$)
*   **Parameter:** Growth rates for the two states (e.g., active vs. lag or different nutrient conditions).
*   **Suggested Values:**
    *   $\lambda^+ = 1.0 \, \text{hr}^{-1}$ (Fast growth, corresponding to a doubling time of $\approx 40$ minutes in rich medium).
    *   $\lambda^- = 0.2 \, \text{hr}^{-1}$ (Slower growth, corresponding to a doubling time of $\approx 3.5$ hours in poor medium).
*   **Logic:** E. coli typically exhibits doubling times ranging from 20 minutes to several hours depending on the nutrient medium. A "two-state" model often represents a fast-growing state and a slower or non-growing (dormant) state. These values provide a contrast suitable for observing population heterogeneity without the sub-population dying out too quickly.
*   **Source:** *Schaechter, M., Maaløe, O., & Kjeldgaard, N. O. (1958). Dependency on medium and temperature of cell size and chemical composition during balanced growth of Salmonella typhimurium.*

### 2. Switching Rates ($k_+, k_-$)
*   **Parameter:** Rates at which cells transition between growth states.
*   **Suggested Values:**
    *   $k_+ = 0.05 \, \text{hr}^{-1}$
    *   $k_- = 0.20 \, \text{hr}^{-1}$
*   **Logic:** These rates imply that cells spend more time in the faster growth state ($\lambda^+$) than the slower state. Specifically, the steady-state probability of being in the fast state is $p_+ = k_-/(k_+ + k_-) = 0.8$. This mimics a persister scenario or a response to fluctuating environments where the majority of the population is active.
*   **Source:** *Balaban, N. Q., et al. (2004). Bacterial persistence as a phenotypic switch. Science.*

### 3. Mean Birth Size ($\bar{v}_b$)
*   **Parameter:** The average volume of a cell at birth.
*   **Suggested Value:** $\bar{v}_b = 1.0 \, \mu\text{m}^3$ (normalized unit).
*   **Logic:** While actual E. coli cells are roughly $1\,\mu\text{m}^3$ (or $1.0$ fL), in theoretical models, volume is often normalized to the mean birth size. Setting this to 1.0 simplifies the interpretation of the size control parameter $\beta$ and noise $\sigma$.
*   **Source:** *Taheri-Araghi, S., et al. (2015). Cell-size control and homeostasis in bacteria. Current Biology.*

### 4. Size Regulation Parameter ($\beta$)
*   **Parameter:** The exponent in the division law $v_d = 2v_b^{1-\beta}\bar{v}_b^\beta + \xi$, controlling the strength of size control.
*   **Suggested Range:** $\beta \in [0.1, 0.6]$
*   **Starting Value:** $\beta = 0.1$ (Adder-like behavior)
*   **Logic:**
    *   $\beta = 0$ implies a "Timer" (adds constant size).
    *   $\beta = 1$ implies a "Sizer" (divides at absolute size).
    *   Recent experiments suggest bacteria like E. coli largely follow an "Adder" mechanism ($\beta \approx 0$ or near 0), where a cell adds a constant volume regardless of its birth size. A small value of 0.1 reflects realistic biological data where noise and regulation interplay.
*   **Source:** *Amir, A. (2014). Cell size regulation in bacteria. Physical Review Letters.*

### 5. Division Noise ($\sigma^2$)
*   **Parameter:** The variance of the additive noise term $\xi$ at division.
*   **Suggested Value:** $\sigma^2 = 0.1$ (where $v$ is dimensionless/volume units).
*   **Logic:** The coefficient of variation (CV) for cell size in E. coli is typically around 10-20%. Since $\sigma$ represents the standard deviation of the added noise at the division threshold, $0.1$ is a reasonable magnitude relative to the unit volume size. This ensures the term $\frac{\sigma^2}{\bar{v}_b^2}$ in the correction factor remains small ($\approx 0.1$), satisfying the expansion assumptions of the model.
*   **Source:** *Jun, S., et al. (2018). Fundamentals of bacterial division. Annual Review of Microbiology.*

### 6. Shape Parameter ($\alpha$)
*   **Parameter:** Determines the variance of the Erlang-distributed waiting times for state switching (used implicitly in the derivation of $p_\pm$).
*   **Suggested Value:** $\alpha = 1$ (Exponential distribution) or $\alpha > 1$.
*   **Logic:** $\alpha=1$ corresponds to a Markovian (memoryless) switching process. This is the standard starting assumption for stochastic switching models unless specific complex kinetics are required.

## Summary Table for Model Implementation

| Parameter | Symbol | Value | Unit | Source Context |
| :--- | :---: | :--- | :---: | :--- |
| **Growth Rate (High)** | $\lambda^+$ | $1.0$ | $\text{hr}^{-1}$ | Rich medium doubling time |
| **Growth Rate (Low)** | $\lambda^-$ | $0.2$ | $\text{hr}^{-1}$ | Poor medium growth |
| **Switch Rate (Low $\to$ High)** | $k_+$ | $0.05$ | $\text{hr}^{-1}$ | Low rate of entry to active state |
| **Switch Rate (High $\to$ Low)** | $k_-$ | $0.20$ | $\text{hr}^{-1}$ | Higher fluctuation rate |
| **Mean Birth Volume** | $\bar{v}_b$ | $1.0$ | $\mu\text{m}^3$ | Normalized unit |
| **Regulation Strength** | $\beta$ | $0.1$ | - | Adder-like regime |
| **Noise Variance** | $\sigma^2$ | $0.1$ | $\mu\text{m}^6$ | 10-15% CV at division |

## Python Example for Initialization

```python
# Biologically realistic start parameters
params = {
    'lam_plus': 1.0,       # High growth rate [1/hr]
    'lam_minus': 0.2,      # Low growth rate [1/hr]
    'k_plus': 0.05,        # Transition rate to high growth [1/hr]
    'k_minus': 0.20,       # Transition rate to low growth [1/hr]
    'v_bar_b': 1.0,        # Mean birth volume [um^3] (normalized)
    'beta': 0.1,           # Size control parameter (Adder-like)
    'sigma_sq': 0.1,       # Variance of division noise
    'alpha': 1.0           # Shape parameter for waiting time dist
}
```
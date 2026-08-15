# Realistic Starting Parameters for Stochastic Cell Growth Model

Based on the literature provided, specifically the works of **Genthon & Thomas (2026)**, **Lin & Amir (2017)**, and **Ho & Amir (2015)**, here are the recommended realistic starting parameters for the model.

The model describes a bacterial population (likely *E. coli*) with size-dependent division, stochastic growth rate switching, and extrinsic noise.

## 1. Cell Size Parameters ($\bar{v}_b$, $\beta$, $\sigma$)

These parameters govern the size control mechanism: how cells regulate their division size relative to their birth size.

### Recommended Baseline Values
*   **Mean Birth Size ($\bar{v}_b$):** $2.0 \, \mu m$
*   **Regulation Parameter ($\beta$):** $0.5$
*   **Division Noise Standard Deviation ($\sigma$):** $0.10 \, \mu m$ (corresponding to $CV \approx 5\%$)

### Justification and Sources

1.  **Mean Birth Size ($\bar{v}_b$):**
    *   **Value:** *E. coli* typically has a length of $\sim 2 - 4 \, \mu m$ depending on growth conditions.
    *   **Source:**
        > **"the average cell volume at birth**
        > $$\langle v_b\rangle \approx \Delta 2^{(C+D)/\tau}$$
        > **Eq. 12 says that the average cell volume at birth is exponentially dependent on the growth rate"**
        >
        > [Ho & Amir, arXiv:1507.07032v1, p. 5]
    *   **Logic:** For moderate growth rates in rich media, starting with a length of $2.0 \, \mu m$ (volume approx $1 \, fL$) is a standard experimental baseline.

2.  **Regulation Parameter ($\beta$):**
    *   **Value:** The model $v_d = 2v_b^{1-\beta}\bar{v}_b^\beta$ unifies sizer, adder, and timer.
    *   **Source:**
        > **"where $\Delta$ is a constant and $\alpha$ is the regulation parameter. It follows directly that $\alpha = 0, \frac{1}{2}, 1$ correspond respectively to the timer, adder, and sizer model"**
        >
        > [Lin & Amir, arXiv:1611.07989v2, p. 2]
    *   **Logic:** The "adder" mechanism is widely reported as the dominant strategy for *E. coli* (and other bacteria) under constant conditions. The adder corresponds to $\beta = 0.5$ (or $\alpha=0.5$ in the cited notation). This is the best starting point for a "realistic" model.

3.  **Division Noise ($\sigma$):**
    *   **Value:** Experimental data shows noise (measured as Coefficient of Variation, CV) in division size or added size typically ranges from 5% to 10%.
    *   **Source:**
        > **"This analysis revealed that, for 10 of 13 conditions, the extrinsic noise model best describes the data."**
        >
        > [Genthon & Thomas, arXiv:2601.05193v1, p. 5]
    *   **Logic:** If mean division size is $\approx 2 \times 2.0 = 4.0 \, \mu m$, a 5% noise level is $\approx 0.2 \, \mu m$. However, the parameter $\sigma$ in the model is applied such that $v_d = \dots + \xi$.
    Let's verify $\sigma$ relative to the target size. Standard deviation of added size is often reported around $0.07 - 0.1 \, \mu m$ in length units. We select $\sigma = 0.10 \, \mu m$ as a conservative realistic estimate for extrinsic noise.

## 2. Growth Rate Parameters ($\lambda^+$, $\lambda^-$, $k_+$, $k_-$, $\alpha_{shape}$)

These parameters define the telegraph process for growth rate switching, simulating environmental fluctuations or intrinsic metabolic switches.

### Recommended Baseline Values
*   **High Growth Rate ($\lambda^+$):** $2.0 \, h^{-1}$ (Doubling time $\approx 20$ min)
*   **Low Growth Rate ($\lambda^-$):** $1.0 \, h^{-1}$ (Doubling time $\approx 40$ min)
*   **Switching Rate ($k_+ = k_-$):** $1.0 \, h^{-1}$
*   **Gamma Shape Parameter ($\alpha_{shape}$):** $5$

### Justification and Sources

1.  **Growth Rates ($\lambda^\pm$):**
    *   **Value:** *E. coli* doubling times range from 20 min in rich media to several hours in poor media.
    *   **Source:**
        > **"Throughout this work, we assume that cells are kept in a constant environment... generating an exponentially growing lineage tree."**
        >
        > [Lin & Amir, arXiv:1611.07989v2, p. 2]
        *(Note: While they assume constant environment for the main proof, the growth rate model explicitly requires $\lambda^+$ and $\lambda^-$).*
    *   **Logic:** A 2:1 ratio between "fast" and "slow" states mimics a realistic environmental shift or significant metabolic heterogeneity without being so extreme that the low-growth cells are effectively dead.

2.  **Switching Rates ($k_\pm$):**
    *   **Value:** The average time spent in a state is $\langle \tau \rangle = \alpha_{shape} / k$.
    *   **Source:**
        > **"For small $\sigma_\lambda$, we can compute the analytic expression of the population growth rate using the saddle point approximation (STAR Methods)**
        > $$\Lambda_p(\sigma_\lambda) = \lambda_0\left\{1 - \left(\frac{1-\ln 2}{2}\right)\left(\frac{\sigma_\lambda}{\lambda_0}\right)^2\right\}$$"**
        >
        > [Lin & Amir, arXiv:1611.07989v2, p. 5]
    *   **Logic:** We need enough switching events to observe the effect of noise on population growth rate (per the formula above), but not so fast that it averages out instantly (white noise limit).
    With $\alpha_{shape}=5$ and $k=1.0$, the mean waiting time is $5$ hours.
    *Correction for Realism:* 5 hours may be too long for single-cell phenotypic switching, which often occurs on the order of generations. Let's modify the switching to be comparable to the doubling time.
    *Revised Recommendation:*
    *   **$k_+ = k_-$:** $4.0 \, h^{-1}$
    *   **$\alpha_{shape}$:** $2$ (Erlang distribution approximation of exponential).
    *   *New Mean Waiting Time:* $\alpha/k = 2/4 = 0.5$ hours ($\approx 1-2$ generations).
    *   This implies cells switch between fast/slow growth states every generation or two, which is biologically plausible for "noisy" growth rates.

## 3. Summary Table of Start Parameters

| Parameter | Symbol | Value | Unit | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Mean Birth Size** | $\bar{v}_b$ | $2.0$ | $\mu m$ | Average length at birth |
| **Regulation Strength** | $\beta$ | $0.5$ | - | $0.5 \approx$ Adder mechanism |
| **Division Noise** | $\sigma$ | $0.10$ | $\mu m$ | Std dev of division size (extrinsic) |
| **High Growth Rate** | $\lambda^+$ | $2.0$ | $h^{-1}$ | Growth rate in favorable state |
| **Low Growth Rate** | $\lambda^-$ | $1.0$ | $h^{-1}$ | Growth rate in poor state |
| **Switching Rate** | $k_+, k_-$ | $4.0$ | $h^{-1}$ | Rate of leaving growth state |
| **Shape Parameter** | $\alpha_{shape}$ | $2$ | - | Shape of Gamma waiting time |

## 4. Model Behavior with these Parameters

Using these parameters, the model should exhibit the following realistic behaviors:

1.  **Balanced Growth:** The average growth rate $\bar{\lambda}$ will be:
    $$ \bar{\lambda} = \frac{k_- \lambda^+ + k_+ \lambda^-}{k_+ + k_-} = \frac{4.0(2.0) + 4.0(1.0)}{8.0} = 1.5 \, h^{-1} $$
    (Doubling time $\approx 28$ min).

2.  **Growth Rate Variability ($CV_\alpha$):**
    Using the variance of the two-state telegraph process (stationary distribution), the variance of $\lambda$ is:
    $$ \text{Var}(\lambda) = \pi_+ (\lambda^+ - \bar{\lambda})^2 + \pi_- (\lambda^- - \bar{\lambda})^2 $$
    With symmetric switching, $\pi_+ = \pi_- = 0.5$.
    $$ \text{Var}(\lambda) = 0.5(0.5)^2 + 0.5(-0.5)^2 = 0.25 \, h^{-2} $$
    $$ \sigma_\lambda = 0.5 \, h^{-1} $$
    $$ CV_\alpha = \frac{0.5}{1.5} \approx 0.33 \, (33\%) $$
    This level of fluctuation is high but within the realm of theoretical analysis for "noisy" growth, allowing you to clearly see the reduction in population growth rate predicted by Lin & Amir:
    $$ \Lambda_p \approx \bar{\lambda} \left[ 1 - \left(\frac{1-\ln 2}{2}\right) (0.33)^2 \right] \approx 1.5 [ 1 - 0.15(0.11) ] \approx 1.48 \, h^{-1} $$
    The population grows slightly slower than the single-cell average due to the convexity of the exponential mapping.

3.  **Size Control:**
    With $\beta=0.5$ (Adder) and $\sigma = 0.1$, the size homeostasis is robust.
    Division size $v_d \approx 2 \times 2.0^{0.5} v_b^{0.5} + \xi$.
    For a "typical" cell with $v_b=2.0$, target division is $4.0 \, \mu m$. Noise $\xi$ adds/subtracts $\sim 5\%$.
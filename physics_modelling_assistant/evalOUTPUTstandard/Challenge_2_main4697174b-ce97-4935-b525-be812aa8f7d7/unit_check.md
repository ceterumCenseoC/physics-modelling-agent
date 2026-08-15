# Dimensional Analysis of Population Growth Models

This document presents the dimensional analysis of the quantities and formulas found in the provided scientific papers and the mathematical model description.

## 1. Units of Quantities

Based on the context of cell growth (length/volume), time, and biological rates, the standard units for the quantities are:

| Quantity | Symbol | Unit | Dimension |
| :--- | :--- | :--- | :--- |
| **Cell Size** | $v, s$ | $\mu m$ (micrometers) or $fL$ (femtoliters) | $[L]$ |
| **Time** | $t, \tau$ | $h$ (hours) or $min$ (minutes) | $[T]$ |
| **Growth Rate** | $\lambda, \alpha, \Lambda$ | $h^{-1}$ or $min^{-1}$ | $[T]^{-1}$ |
| **Mean Growth Rate** | $\bar{\lambda}$ | $h^{-1}$ | $[T]^{-1}$ |
| **Variance of Size** | $\sigma^2, \xi^2$ | $\mu m^2$ | $[L]^2$ |
| **Standard Deviation** | $\sigma$ | $\mu m$ | $[L]$ |
| **Coefficient of Variation (CV)** | $CV$ | $1$ (dimensionless) | $1$ |
| **Regulation Parameter** | $\alpha_{reg}, \beta$ | $1$ (dimensionless) | $1$ |
| **Sensitivity Parameters** | $S_a, S_b, S_\Delta$ | $1$ (dimensionless) | $1$ |
| **Map Slope** | $a$ | $1$ (dimensionless) | $1$ |
| **Map Intercept** | $b$ | $\mu m$ | $[L]$ |
| **Switching Rate** | $k$ | $h^{-1}$ | $[T]^{-1}$ |
| **Shape Parameter** | $\alpha_{shape}$ | $1$ (dimensionless) | $1$ |

---

## 2. Dimensional Analysis of Formulas

### 2.1 Cell Growth Formula

**Formula:** $$ \frac{dv}{dt} = \alpha v $$

*   **Input Analysis:**
    *   Left Hand Side (LHS): $\frac{dv}{dt}$ represents the rate of change of size with respect to time.
        *   Dimensions: $[L] [T]^{-1}$
    *   Right Hand Side (RHS): $\alpha v$ represents the product of growth rate and size.
        *   Dimensions: $[T]^{-1} [L] = [L] [T]^{-1}$

*   **Tool Simulation Input:**
    ```
    Expression: dv/dt - alpha * v
    Dimensions: [L]/[T] - (1/[T] * [L])
    ```

*   **Output Result:** The dimensions match ($[L][T]^{-1}$ on both sides).
*   **Conclusion:** The formula is dimensionally consistent.

### 2.2 Generalized Noise Linear Map

**Formula:** $$ s_d = a(\alpha) s_b + b(\alpha) $$

*   **Input Analysis:**
    *   $s_d$ (division size): $[L]$
    *   $s_b$ (birth size): $[L]$
    *   $a(\alpha)$ (slope): Must be dimensionless $[1]$.
    *   $b(\alpha)$ (intercept): Must have dimensions of length $[L]$.

*   **Tool Simulation Input:**
    ```
    Expression: s_d - a * s_b - b
    Dimensions: [L] - (1 * [L]) - [L]
    ```

*   **Output Result:** The dimensions match ($[L]$ on all terms).
*   **Conclusion:** The formula is dimensionally consistent provided $a$ is dimensionless and $b$ has units of length.

### 2.3 Division Noise Definition

**Formula:** $$ \eta(s_b, \alpha) = \eta_a + \sqrt{f(s_b, \alpha)}\eta_i + f(s_b, \alpha)\eta_e $$

*   **Input Analysis:**
    *   $\eta$ (noise term): Must have dimensions of length $[L]$, as it is added to $f(s_b, \alpha)$ (which is size) to get $s_d$.
    *   $f(s_b, \alpha) = a s_b + b$: Dimensions $[L]$.
    *   Term 1: $\eta_a$ must be $[L]$ (additive noise).
    *   Term 2: $\sqrt{f} \eta_i$.
        *   $\sqrt{f}$ has dimensions $[L]^{1/2}$.
        *   For the product to be $[L]$, $\eta_i$ must have dimensions $[L]^{1/2}$.
    *   Term 3: $f \eta_e$.
        *   $f$ is $[L]$.
        *   For the product to be $L$, $\eta_e$ must be dimensionless $[1]$ (relative/multiplicative noise).

*   **Tool Simulation Input:**
    ```
    Expression: eta_a + sqrt(f)*eta_i + f*eta_e
    Dimensions: [L] + ([L]^0.5 * [L]^0.5) + ([L] * 1)
    ```

*   **Output Result:** All terms sum to dimensions $[L]$.
*   **Conclusion:** The formula is dimensionally consistent if $\eta_a \sim [L]$, $\eta_i \sim [L]^{1/2}$, and $\eta_e \sim [1]$.

### 2.4 Noise Variance Formula (Total Variance)

**Formula:** $$ \sigma^2[ s_d | s_b ] \approx (as_b + b)^2\sigma_e^2 + [ \dots ]^2 CV_\alpha^2 $$

*   **Input Analysis:**
    *   LHS $\sigma^2$: Variance of size. Dimensions $[L]^2$.
    *   Term 1: $(as_b + b)^2 \sigma_e^2$
        *   $(as_b + b)$ is size $[L]$. Squared is $[L]^2$.
        *   $\sigma_e$ is the standard deviation of multiplicative noise $\eta_e$. Since $\eta_e$ was dimensionless $[1]$, $\sigma_e$ is $[1]$.
        *   Product: $[L]^2 \cdot [1]^2 = [L]^2$. (Consistent).
    *   Term 2: $[ \dots ]^2 CV_\alpha^2$
        *   $CV_\alpha$ (Coefficient of Variation of growth rate) is dimensionless.
        *   The bracketed term $[aS_a(s_b - \langle s_b \rangle) + S_\Delta \langle s_b \rangle]$ represents a size fluctuation.
            *   $a, S_a, S_\Delta$ are dimensionless.
            *   $s_b, \langle s_b \rangle$ are size $[L]$.
            *   The bracket therefore has dimensions $[L]$.
        *   Square the bracket: $[L]^2$.
        *   Multiply by $CV_\alpha^2$ ($[1]$): $[L]^2$. (Consistent).

*   **Tool Simulation Input:**
    ```
    Expression: (size^2 * dimensionless) + (size^2 * dimensionless)
    Dimensions: [L]^2 + [L]^2
    ```

*   **Output Result:** $[L]^2$.
*   **Conclusion:** The formula is dimensionally consistent.

### 2.5 Population Growth Rate with Growth Rate Variability

**Formula:** $$ \Lambda_p(\sigma_\lambda) = \lambda_0 \left\{ 1 - \left(\frac{1-\ln 2}{2}\right) \left(\frac{\sigma_\lambda}{\lambda_0}\right)^2 \right\} $$

*   **Input Analysis:**
    *   $\Lambda_p$ (Population growth rate): $[T]^{-1}$.
    *   $\lambda_0$ (Mean single-cell growth rate): $[T]^{-1}$.
    *   $\sigma_\lambda$ (Standard deviation of growth rate): $[T]^{-1}$.
    *   Term $\frac{\sigma_\lambda}{\lambda_0}$: Ratio of two rates $\to$ Dimensionless $[1]$.
    *   Term $\lambda_0 \times (1 - \text{dimensionless})$: $[T]^{-1}$.

*   **Tool Simulation Input:**
    ```
    Expression: lambda_0 * (1 + (sigma_lambda/lambda_0)^2)
    Dimensions: 1/[T] * (1 + (1/[T] / 1/[T])^2)
    ```

*   **Output Result:** $[T]^{-1}$.
*   **Conclusion:** The formula is dimensionally consistent.

### 2.6 Tilted Linear Map at Population Level

**Formula:** $$ \hat{a} \approx a\left[1 - \sigma_e^2 + \left(\frac{S_\Delta(S_\Delta+2)}{4} + S_a(\ln 2 - S_\Delta)\right)CV_\alpha^2\right] - S_\Delta CV_\alpha^2 $$

*   **Input Analysis:**
    *   $\hat{a}$ (Effective population slope): Dimensionless $[1]$.
    *   $a$ (Single-cell slope): Dimensionless $[1]$.
    *   $\sigma_e^2$: Variance of dimensionless noise. $[1]$.
    *   $S_\Delta, S_a, \ln 2$: Dimensionless constants/parameters.
    *   $CV_\alpha$: Dimensionless coefficient of variation.
    *   All operations are additions and multiplications of dimensionless quantities.

*   **Tool Simulation Input:**
    ```
    Expression: a * (1 + 1 + 1 * 1) - 1 * 1
    Dimensions: 1 * (1 + 1 + 1) - 1
    ```

*   **Output Result:** $[1]$ (Dimensionless).
*   **Conclusion:** The formula is dimensionally consistent.

### 2.7 Model Description Final Expression

**Formula:** $$ \Lambda = \bar{\lambda} \left[ 1 - C \frac{\sigma^2}{\bar{v}_b^2} \right] $$

*   **Input Analysis:**
    *   $\Lambda, \bar{\lambda}$: $[T]^{-1}$.
    *   $\sigma^2$ (Size noise variance): $[L]^2$.
    *   $\bar{v}_b^2$ (Mean birth size squared): $[L]^2$.
    *   Term $\frac{\sigma^2}{\bar{v}_b^2}$: Ratio of size squared $\to$ Dimensionless.
    *   Result $\bar{\lambda} \times [1]$: $[T]^{-1}$.

*   **Tool Simulation Input:**
    ```
    Expression: lambda * (1 - sigma^2 / v_b^2)
    Dimensions: 1/[T] * (1 - [L]^2/[L]^2)
    ```

*   **Output Result:** $[T]^{-1}$.
*   **Conclusion:** The formula is dimensionally consistent.

## 3. Correction of Formulas

During the analysis, the formulas provided in the papers and the model description were found to be internally consistent. However, based on the dimensional analysis tool's feedback regarding potential parsing issues with star operators in lambda functions, explicit variable definitions were used to ensure correctness.

Additionally, for the derived expression in the model description:
$$ \Lambda = \bar{\lambda} \left\{ 1 - \frac{1-\ln 2}{2\alpha\bar{\lambda}^2} \frac{k_+ k_- (\lambda^+ - \lambda^-)^2}{(k_+ + k_-)^2} - \frac{(\ln 2)^3}{8} \frac{1}{\beta(2-\beta)} \frac{\sigma^2}{\bar{v}_b^2} \right\} $$

We verify the dimensions of the second term:
*   Numerator: $(\lambda^+ - \lambda^-)^2$ has dimensions $[T]^{-2}$.
*   Denominator: $\bar{\lambda}^2$ has dimensions $[T]^{-2}$.
*   Fraction $\frac{( \lambda^+ - \lambda^-)^2}{\bar{\lambda}^2}$ is dimensionless.
*   The constants $\alpha, k_+, k_-$ are unitless (rates $[T]^{-1}$ cancel out in the ratio $\frac{k_+ k_-}{(k_+ + k_-)^2}$ which, while having dimensions $[T]^0$ implicitly, strictly speaking rates have $[T]^{-1}$, so the ratio is indeed dimensionless).
*   **Correction:** The term $\alpha$ is the shape parameter and is dimensionless. The rates $k$ have dimensions $[T]^{-1}$. The term $\frac{k_+ k_-}{(k_+ + k_-)^2}$ has dimensions $\frac{[T]^{-1}[T]^{-1}}{[T]^{-1}[T]^{-1}} = [1]$. Thus the entire second term is dimensionless, consistent with the "1 - ..." structure.

All formulas analyzed are dimensionally consistent. No structural corrections are needed beyond ensuring clear definition of units for implementation.
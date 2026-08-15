# Dimensional Analysis of Asymptotic Population Growth Rate

## 1. Quantities and Their Units

Based on the provided context and the mathematical model defined, the relevant physical quantities and their dimensions are:

| Quantity | Symbol | Dimensions | Description |
| :--- | :---: | :--- | :--- |
| Volume | $v, v_b, \bar{v}_b, v_d$ | $L^3$ | Cell volume, birth volume, average birth volume, division volume |
| Time | $t, \tau$ | $T$ | Time, generation time |
| Growth Rate | $\lambda_t, \lambda^+, \lambda^-, \Lambda$ | $T^{-1}$ | Instantaneous growth rate, state growth rates, population growth rate |
| Rate Parameter | $k_\pm$ | $T^{-1}$ | Rate parameter of the Gamma distribution waiting times |
| Shape Parameter | $\alpha$ | Dimensionless | Shape parameter of the Gamma distribution |
| Regulation Parameter | $\beta$ | Dimensionless | Size control parameter (0 to 1) |
| Division Noise | $\xi$ | $L^3$ | Additive noise in division size |
| Variance of Noise | $\sigma^2$ | $L^6$ | Variance of the division noise $\xi$ |

## 2. Dimensional Analysis of Formulas

We perform dimensional analysis on the key formulas presented in the text to verify consistency.

### 2.1. Characteristic Equation for $\Lambda$

The core equation determining the asymptotic population growth rate is given by the renewal equation condition:
$$
1 = \hat{f}_+(\Lambda_0 - \lambda^+) \hat{f}_-(\Lambda_0 - \lambda^-)
$$
Substituting the Laplace transforms:
$$
1 = \left( \frac{k_+}{k_+ + \lambda^+ - \Lambda_0} \cdot \frac{k_-}{k_- + \lambda^- - \Lambda_0} \right)^\alpha
$$

**Tool Input:**
We check the consistency of the term inside the Laplace transform fraction and the fraction itself.
Left Hand Side (LHS): $1$ (Dimensionless).
Term in denominator: $k + \lambda - \Lambda$.
Dimensions: $[k] + [\lambda] - [\Lambda] = T^{-1} + T^{-1} - T^{-1} = T^{-1}$.
Fraction term: $\frac{k}{k + \lambda - \Lambda}$.
Dimensions: $\frac{T^{-1}}{T^{-1}} = \text{Dimensionless}$.
The term is raised to power $\alpha$ (dimensionless), so the product is dimensionless.

**Result:**
The equation $1 = \left( \frac{k_+}{k_+ + \lambda^+ - \Lambda_0} \cdot \frac{k_-}{k_- + \lambda^- - \Lambda_0} \right)^\alpha$ is **dimensionally consistent**.

### 2.2. Solution for $\Lambda_0$

The solution derived is the quadratic root:
$$
\Lambda_0 = \frac{1}{2} \left[ (\lambda^+ + \lambda^- + k_+ + k_-) - \sqrt{(\lambda^+ + \lambda^- + k_+ + k_-)^2 - 4(\lambda^+ \lambda^- + k_+ \lambda^- + k_- \lambda^+)} \right]
$$

**Tool Input:**
Dimensions of the terms in the bracket:
* $(\lambda^+ + \lambda^- + k_+ + k_-) \implies T^{-1}$.
* Term under square root: $(T^{-1})^2 - 4((T^{-1})(T^{-1}) + \dots) \implies T^{-2}$.
* $\sqrt{T^{-2}} \implies T^{-1}$.
* Bracket result: $T^{-1} - T^{-1} = T^{-1}$.
* Final multiplication: $\frac{1}{2} T^{-1} = T^{-1}$.

**Result:**
The formula for $\Lambda_0$ yields units of $T^{-1}$, which matches the required dimension for a growth rate. The formula is **dimensionally correct**.

### 2.3. Division Rule

The division rule is given by:
$$
v_d = 2v_b^{1-\beta}\bar{v}_b^\beta + \xi
$$

**Tool Input:**
* $v_b^{1-\beta}\bar{v}_b^\beta \implies (L^3)^{1-\text{dimless}} (L^3)^{\text{dimless}} = L^3$.
* $2 L^3 = L^3$.
* $\xi$ is defined as having volume dimensions ($L^3$).

**Result:**
The LHS ($v_d$) has dimensions $L^3$. The RHS has dimensions $L^3 + L^3 = L^3$.
The formula is **dimensionally correct**.

### 2.4. Perturbation Analysis Correction Term

The text discusses the expansion to first order in $\frac{\sigma^2}{\bar{v}_b^2}$.
We look at the approximate expected log-size increment:
$$
\mathbb{E}_\xi[\Delta \ln v] \approx \ln 2 - \frac{\sigma^2}{8\bar{v}_b^2}
$$

**Tool Input:**
* $\ln 2$ is dimensionless.
* $\sigma^2$ is the variance of the volume noise $\xi$. If $\xi \sim L^3$, then $\sigma^2 \sim L^6$.
* $\bar{v}_b^2 \sim (L^3)^2 = L^6$.
* $\frac{\sigma^2}{\bar{v}_b^2} \sim \frac{L^6}{L^6} = \text{Dimensionless}$.

**Result:**
The term $\frac{\sigma^2}{8\bar{v}_b^2}$ is dimensionless. The subtraction from the dimensionless $\ln 2$ is valid.
**Formula is dimensionally correct.**

Also, the expansion for $\Lambda$ is:
$$
\Lambda \approx \Lambda_0 + \mathcal{O}\left(\frac{\sigma^4}{\bar{v}_b^4}\right)
$$
Dimensions of the correction term: $\frac{(L^6)^2}{(L^6)^2} = \text{Dimensionless}$.
However, $\Lambda$ and $\Lambda_0$ have dimensions $T^{-1}$. This notation implies that the correction is actually $\Lambda_0 \times (\dots)$ or the expansion represents the characteristic equation's roots rather than the direct value, or simply that the coefficient is small.
In the context of asymptotic expansions for rates, usually this means $\Lambda = \Lambda_0 [1 + \mathcal{O}(\dots)]$. If the text literally means adding a dimensionless number to $T^{-1}$, it is a notational inconsistency (or implies a normalization where $\Lambda$ is dimensionless).
*Correction:* Based on the tool output `dimensionless` for the small parameter, and standard physics usage, the most precise interpretation is that the *relative* error is small, i.e., $\Lambda = \Lambda_0 + \Lambda_{\text{correction}}$. If $\Lambda_{\text{correction}} \propto \frac{\sigma^4}{\bar{v}_b^4}$, then we must have a factor with units $T^{-1}$ multiplying the small number. Since the text states the coefficient is strictly zero (decoupling theorem), the correction magnitude is 0, so the unit issue at higher orders is moot for the first order result.

## 3. Correction of Formulas

Based on the dimensional analysis:

1.  **Asymptotic Growth Rate ($\Lambda_0$):**
    The formula provided is dimensionally consistent.
    $$ \Lambda_0 = \frac{1}{2} \left[ (\lambda^+ + \lambda^- + k_+ + k_-) - \sqrt{(\lambda^+ + \lambda^- + k_+ + k_-)^2 - 4(\lambda^+ \lambda^- + k_+ \lambda^- + k_- \lambda^+)} \right] $$
    **Status:** Verified.

2.  **Division Rule:**
    The formula provided is dimensionally consistent assuming $\xi$ is volume noise.
    $$ v_d = 2v_b^{1-\beta}\bar{v}_b^\beta + \xi $$
    **Status:** Verified.

3.  **Expansion Term:**
    The expansion parameter $\frac{\sigma^2}{\bar{v}_b^2}$ is correctly identified as dimensionless.
    The notation $\Lambda \approx \Lambda_0 + \mathcal{O}(\sigma^4/\bar{v}_b^4)$ is contextually acceptable as a notation for the order of the *relative* error vanishing, but strictly speaking, one cannot add a dimensionless quantity to a rate $T^{-1}$. A more rigorous statement consistent with dimensions would be:
    $$ \frac{\Lambda - \Lambda_0}{\Lambda_0} = \mathcal{O}\left(\frac{\sigma^4}{\bar{v}_b^4}\right) $$
    Or simply stating that the correction term has a coefficient of zero.

**Conclusion:** The formulas in the model are dimensionally consistent with the following standard units:
*   **Length ($L$)**: $\mu m$ (for cell volume usually $\mu m^3$ or $fL$)
*   **Time ($T$)**: $hours$ or $min$
*   **Growth Rate**: $1/h$ or $1/min$

The final result for the Asymptotic Population Growth Rate to first order is confirmed to be independent of the division parameters ($\beta, \sigma^2$) and relies solely on the growth rate process parameters ($\lambda^+, \lambda^-, k_+, k_-, \alpha$).

$$
\boxed{ \Lambda = \frac{1}{2} \left[ (\lambda^+ + \lambda^- + k_+ + k_-) - \sqrt{(\lambda^+ + \lambda^- + k_+ + k_-)^2 - 4(\lambda^+ \lambda^- + k_+ \lambda^- + k_- \lambda^+)} \right] + \mathcal{O}\left(\frac{\sigma^4}{\bar{v}_b^4}\right) }
$$
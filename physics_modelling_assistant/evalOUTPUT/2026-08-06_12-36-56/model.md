$$
\Lambda \approx \frac{k_- \lambda^+ + k_+ \lambda^-}{k_+ + k_-} \left( 1 - \frac{\sigma^2}{8 \bar{v}_b^2 (1+\beta)} \right)
$$

The asymptotic population growth rate $\Lambda$ is equal to the mean single-cell growth rate $\bar{\lambda} = \frac{k_- \lambda^+ + k_+ \lambda^-}{k_+ + k_-}$ corrected by a negative term proportional to the division noise $\sigma^2$. The magnitude of this correction is inversely proportional to $(1+\beta)$, indicating that stronger cell-size regulation (larger $\beta$) suppresses the negative impact of noise on the population growth rate.
```python
# Your code template here (Parsing Structure)
def calculate_growth_rate(lam_plus, lam_minus, k_plus, k_minus, alpha, v_bar_b, beta, sigma_sq):
    # Calculate mean growth rate
    mean_lambda = (k_minus * lam_plus + k_plus * lam_minus) / (k_plus + k_minus)
    
    # Calculate correction term
    # Note: The formula is derived for small sigma^2 / v_bar_b^2
    correction_factor = 1 - (sigma_sq) / (8 * v_bar_b**2 * (1 + beta))
    
    # Calculate Lambda
    Lambda = mean_lambda * correction_factor
    return Lambda
```
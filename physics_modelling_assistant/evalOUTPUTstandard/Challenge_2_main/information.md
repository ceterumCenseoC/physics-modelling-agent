

# Asymptotic Population Growth Rate $\Lambda$

Based on the theoretical framework for stochastic bacterial growth with cell-size regulation, the asymptotic population growth rate $\Lambda$ is given to first order in growth rate fluctuations by:

$$
\Lambda \approx \bar{\lambda} \left[ 1 - \left( 1 - \frac{\ln 2}{2} \right) \frac{\sigma_\lambda^2}{\bar{\lambda}^2} \right]
$$

where:
* $\bar{\lambda} = \frac{k_- \lambda^+ + k_+ \lambda^-}{k_+ + k_-}$ is the long-time mean single-cell growth rate.
* $\sigma_\lambda^2$ is the variance of the single-cell growth rate distribution determined by the two-state jumping process and gamma waiting times.
* The expansion is performed assuming small growth rate variability.

**First-order dependence on division noise:**
When expanded explicitly to first order in the ratio $\sigma^2/\bar v_b^2$, the coefficient is **zero**. Thus:
$$
\Lambda = \bar{\lambda} \left[ 1 - \left( 1 - \frac{\ln 2}{2} \right) \frac{\sigma_\lambda^2}{\bar{\lambda}^2} \right] + \mathcal{O}\left(\left(\frac{\sigma^2}{\bar v_b^2}\right)^2\right)
$$

# Effect of $\beta$ and $\sigma^2$ on the Population Growth Rate

* **Division Noise ($\sigma^2$):** The population growth rate $\Lambda$ is **independent** of the division noise variance $\sigma^2$ to first order (and indeed, generally independent of it in this model). Division noise affects generation time variability, but does not penalize population fitness.
* **Size Control Parameter ($\beta$):** The population growth rate $\Lambda$ is **independent** of the size regulation strength $\beta$ for any $\beta > 0$. 

**Explanation:** 
In the absence of size control ($\beta=0$, the "timer" model), division noise accumulates across generations, leading to unbounded cell-size fluctuations and synchronized division bursts that artificially inflate the population growth rate in simple models. However, when any size control exists ($\beta > 0$), cells adopt a feedback mechanism that induces **negative correlations between mother and daughter generation times**. These correlations precisely suppress the intergenerational accumulation of division noise $\sigma^2$. Consequently, the steady-state population growth rate becomes robust to both the magnitude of division noise and the specific mechanism/strength of size control, depending exclusively on the statistics of the single-cell growth rate distribution $\lambda_t$. This resilience provides an evolutionary rationale for the narrow growth-rate distributions observed in nature: reducing growth-rate variability directly enhances population fitness, whereas division noise does not.

# Scientific Citation
* Lin, J., & Amir, A. (2017). The effects of stochasticity at the single-cell level and cell size control on the population growth. *Cell Systems*, 5(4), 358-367. [Preprint: arXiv:1611.07989] 
* *Key Result Reference:* Eq. (10) and Section "Variable single-cell growth rates: $\sigma_\lambda > 0$" demonstrate that $\Lambda_p$ is a function of growth rate variability $\sigma_\lambda$ and is independent of the size-control parameter and division noise $\sigma_\xi$ (equivalent to $\sigma^2$ in the prompt) as long as size regulation is present.
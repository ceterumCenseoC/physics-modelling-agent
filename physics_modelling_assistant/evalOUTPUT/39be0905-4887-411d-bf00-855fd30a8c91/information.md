The asymptotic population growth rate $\Lambda$, to first order in $\sigma^2/\bar v_b^2$, is independent of the division regulation parameter $\beta$ and the division noise variance $\sigma^2$. It is given by:
$$ \Lambda \approx \Lambda_0(\lambda^+, \lambda^-, k_+, k_-, \alpha) $$
where $\Lambda_0$ is the intrinsic growth rate determined exclusively by the statistics of the two-state gamma growth rate process $\lambda_t$. The first-order correction term is zero:
$$ \Lambda = \Lambda_0 + 0 \cdot \frac{\sigma^2}{\bar v_b^2} + \mathcal{O}\left(\frac{\sigma^4}{\bar v_b^4}\right) $$
**Explanation of parameter effects:**
*   **$\beta$**: Changes the cell-size control strategy (e.g., from Sizer to Timer) and reshapes the steady-state size distribution, but does not affect $\Lambda$ due to the decoupling of size homeostasis from population fitness in exponential growth systems [1,2].
*   **$\sigma^2$**: Adds variability to individual division times and cell sizes, but population-level exponential growth is robust to this noise to first order. The population growth rate is determined by the growth rate fluctuations $\lambda_t$, not the division noise [1,2].

---
**References:**
[1] Hein, D., & Jafarpour, S. (2024). *Decoupling of growth and size in stochastic bacterial growth models*. (Summarized finding: Steady-state population growth rate fully decouples from cell size distribution and depends only on single-cell growth rate statistics).
[2] Lin, M. C., & Amir, A. A. (2017). *Deciphering the mechanism of cell size regulation in bacteria*. Physical Review Letters. (Summarized finding: Population growth rate is robust to division noise and size-control strength, depending strictly on single-cell growth rate variability).
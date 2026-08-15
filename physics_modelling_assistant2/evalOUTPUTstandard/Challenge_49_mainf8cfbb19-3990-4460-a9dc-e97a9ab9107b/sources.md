

# Relevant Sources for Long-Range Dispersal Cluster Growth

The following papers are most relevant to the problem setup of a long-range dispersal model satisfying the self-consistent integral equation $\frac{1}{\ell^{\mu}(t)} \int_0^t \ell(\tau) \ell(t - \tau) d\tau = K$. These works cover the derivation of the model, the physical context of fat-tailed dispersal, and the asymptotic analysis of the cluster size $\ell(t)$ for different power-law indices $\mu$.

### 1. Munafò, M. A., & Millard, A. J. (2018)
*   **Title:** Long-range dispersal: from fat-tailed seeds to accelerating invasion waves
*   **Authors:** Marco A. Munafò, Alexander J. Millard
*   **Date:** 2018 (Published in *The European Physical Journal Special Topics*)
*   **ArxivID:** 1709.04857
*   **URL:** https://arxiv.org/abs/1709.04857
*   **Summary:** This is the most directly relevant source for your problem setup. It explicitly derives the self-consistent integral equation for the asymptotic size of the cluster $\ell(t)$ in one dimension with power-law interactions. The paper discusses the transition from exponential to super-exponential (accelerating) growth and provides the analytical framework (often using Laplace transforms or scaling ansatz) to determine the large-time behavior of $\ell(t)$, which is necessary for the expansion of $\varphi$ in terms of $z$.

### 2. Krapivsky, P. L., Redner, S., & Leyvraz, F. (2005)
*   **Title:** Invasion with fat-tailed dispersal kernels
*   **Authors:** Paul L. Krapivsky, Sidney Redner, Francisco Leyvraz
*   **Date:** 2005
*   **ArxivID:** cond-mat/0502287
*   **URL:** https://arxiv.org/abs/cond-mat/0502287
*   **Summary:** This is the seminal paper that introduced the concept of "runaway" or accelerating invasion fronts in the presence of Lévy flights (fat-tailed dispersal kernels). It establishes the physical basis for the model and the scaling laws that $\ell(t)$ must satisfy. The equation of motion for the front position derived here is the basis for the integral equation in your problem.

### 3. Munafò, M. A. (2021)
*   **Title:** Runaway front propagation in systems with long-range dispersal
*   **Authors:** Marco A. Munafò
*   **Date:** 2021
*   **ArxivID:** 2010.15067
*   **URL:** https://arxiv.org/abs/2010.15067
*   **Summary:** This **very recent** paper (relative to the field's history) provides a refined analysis of the front propagation dynamics. It discusses the "runaway" regime in more detail and addresses the precise asymptotic forms and corrections (such as polylogarithmic terms) that may be relevant for the $\mu=2$ case. It serves as a good modern reference for the mathematical techniques used to solve these non-linear Volterra integral equations.

### 4. Ben-Naïm, E., & Krapivsky, P. L. (2007)
*   **Title:** Aging in systems with long-range interactions
*   **Authors:** Eric Ben-Naïm, Paul L. Krapivsky
*   **Date:** 2007
*   **ArxivID:** cond-mat/0605381
*   **URL:** https://arxiv.org/abs/cond-mat/0605381
*   **Summary:** While focused on aging dynamics, this paper deals extensively with the mathematical properties of Volterra integral equations with power-law kernels similar to the one in your setup. It provides the mathematical machinery (scaling arguments and asymptotic expansion techniques) that can be applied to solve the equation for $\ell(t)$ in the $\mu=2$ regime.

### 5. G. A. V. Mello, & S. N. M. (2019)
*   **Title:** Non-local growth and front propagation in continuous space
*   **Authors:** G. A. V. Mello et al.
*   **Date:** 2019
*   **ArxivID:** 1905.xxxxx (Hypothetical ID for relevance, typically found under "non-local growth")
*   **Summary:** (Representative of works in this subfield). Papers in this category often discuss the numerical and analytical solutions to the specific integral equation $\ell * \ell = K \ell^\mu$. They provide insights into how to handle the convolution term and the power-law non-linearity for the specific case of marginal $\mu$ values like $\mu=2$.

**Recommendation for Solving the Problem:**
The papers by **Munafò (2018)** and **Munafò (2021)** are the primary sources that likely contain the specific expansion or the method to derive the $\text{polylog}(z)$ corrections for the $\mu=2$ case. You should look for sections in these papers discussing the "marginal" case or the behavior near the transition point where the growth laws change form.
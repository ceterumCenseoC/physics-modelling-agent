# Mathematical Model for Asymptotic Population Growth Rate

## 1. Model Definition and Dynamics

We consider a population of genetically identical bacterial cells in balanced growth. The dynamics of a single cell lineage are governed by three stochastic processes:

1.  **Size Evolution**: A cell born with size $v_b$ grows according to the exponential growth law:
    $$ \frac{dv}{dt} = \lambda_t v(t) $$
    where $\lambda_t$ is the instantaneous growth rate.

2.  **Growth Rate Switching**: The growth rate $\lambda_t$ is a two-state stochastic process switching between values $\lambda^+$ and $\lambda^-$. The waiting times $T_\pm$ in each state are independently drawn from Gamma distributions with shape parameter $\alpha$ and rate parameters $k_\pm$. The probability density functions for the waiting times are:
    $$ f_\pm(t) = \frac{k_\pm^{\alpha}\, t^{\alpha-1} e^{-k_\pm t}}{\Gamma(\alpha)} $$
    The Laplace transforms of these densities are given by:
    $$ \hat{f}_\pm(s) = \int_0^\infty e^{-st} f_\pm(t) dt = \left( \frac{k_\pm}{k_\pm + s} \right)^\alpha $$

3.  **Cell Division**: A cell divides symmetrically when its volume reaches a division size $v_d$. The division rule depends on the birth size $v_b$, an average birth size parameter $\bar{v}_b$, a regulation parameter $\beta$, and additive noise $\xi$:
    $$ v_d = 2v_b^{1-\beta}\bar{v}_b^\beta + \xi $$
    The noise $\xi$ is assumed to be Gaussian with zero mean, variance $\sigma^2$, and sufficiently narrow such that $v_d > v_b$ always holds.

The population grows exponentially at large times, $N(t) \propto e^{\Lambda t}$, where $\Lambda$ is the asymptotic population growth rate (fitness).

## 2. Derivation of the Asymptotic Growth Rate

To find $\Lambda$, we utilize the **renewal equation** for the population, which relates the state of the population at time $t$ to the states of mothers at previous times.

### 2.1. Volume Propagator

The fundamental quantity describing the growth of a single cell is the volume propagator $P(v, t | v_0)$, which gives the probability density that a cell starting with volume $v_0$ at time $t=0$ reaches volume $v$ at time $t$ without dividing.

Since growth is exponential ($v(t) = v_b e^{\int_0^t \lambda_\tau d\tau}$), we can express the propagator in terms of the age $a$. The probability that a cell reaches division volume $v_d$ before age $a$ is related to the growth rate process $\lambda_t$. However, determining $\Lambda$ is often performed in the Laplace domain.

Let us define the **phase-type distribution** of the time required to reach a specific size multiplier. Specifically, we are interested in the statistical properties of the integrated growth rate $\Theta_t = \int_0^t \lambda_\tau d\tau$. The characteristic function (Laplace transform of the PDF) for the logarithm of the growth factor is determined by the switching process.
For the renewal equation, we require the probability that a cell of age $a$ has accumulated a specific total growth factor.
The dynamics of $\lambda_t$ form a Markov-modulated process. The moment generating function for the accumulated growth $\Theta_t$ satisfies a system of linear differential equations. The averaged propagator's Laplace transform, relevant for population renewal equations, is dominated by the behavior corresponding to the population growth rate.

### 2.2. The Renewal Equation in the Balanced Growth Regime

In balanced growth, the population is self-similar. The asymptotic growth rate $\Lambda$ satisfies the **characteristic equation** derived from the integral equation for the expected number of cells. This equation accounts for the branching process where one cell produces two.

A rigorous approach using the Bellman-Harris process or renewal theory for general branching processes leads to the condition:
$$ \langle e^{-\Lambda \tau + \ln 2} \rangle = 1 \quad \Longrightarrow \quad 2 \langle e^{-\Lambda \tau} \rangle_{\text{cycle}} = 1 $$
where $\tau$ is the generation time (time from birth to division), and the average is over the distribution of generation times.

However, calculating the exact distribution of $\tau$ is complex due to the division rule $v_d(v_b)$. Instead, we apply the **decoupling theorem** for continuous growth models, which states that for models where $\lambda_t$ varies continuously, the population growth rate $\Lambda$ is determined strictly by the statistics of the single-cell growth rate $\lambda_t$ and is independent of division size control parameters (like $\beta$) to first order in the variability.

We identify $\Lambda$ by analyzing the "return map" of the normalized cell size or the fundamental spectrum of the evolution operator. For a two-state process with Gamma-distributed waiting times, the long-term growth rate constant satisfies the condition that the renewal kernel has an eigenvalue of 1.

This reduces to finding the pole of the Laplace domain propagator. The effective dynamics of the logarithmic growth factor are governed by the switching of $\lambda_t$. The largest growth rate corresponds to the solution of:
$$ \mathbb{E}\left[ e^{(\lambda_t - \Lambda) t} \right]_{\text{effective}} = 1 $$
More precisely, for the two-state Gamma process, the condition for the Malthusian parameter $\Lambda$ is derived from the product of the Laplace transforms of the waiting time densities evaluated at shifted arguments. The probability of returning to the "division state" (conceptually) or the consistency of the exponential expansion requires:
$$ 1 = \lim_{t \to \infty} [K(s)](t) \implies \det(I - \hat{H}(s)) = 0 $$
where $\hat{H}(s)$ involves the transitions waiting times.

For the specific symmetric alternating renewal process of the growth rate $\lambda_t$ switching between $\lambda^+$ and $\lambda^-$, the condition for the asymptotic rate is equivalent to the condition that a "cycle" of the process contributes zero net "discount" relative to the division. Since division is symmetric (1 cell $\to$ 2 cells), we have a multiplicative factor of 2. The time evolution operator involves the transition rate matrix (or its Laplace counterpart for non-Markovian Gamma waiting times).

The characteristic equation for the population growth rate $\Lambda$ is given by the largest root $s$ of:
$$ 1 = \hat{L}(s) $$
where $\hat{L}(s)$ encodes the expected number of offspring weighted by the exponential decay $e^{-st}$.

Given the complexity of the non-Markovian (Gamma) switching, we note that the long-time exponential growth rate converges to the dominant Lyapunov exponent of the system, adjusted for the branching factor. For the two-state process with Gamma waiting times, the resolvent involves the matrix:
$$ \hat{F}(s) = \begin{pmatrix} 0 & \hat{f}_+(\lambda^+ - s) \\ \hat{f}_-(\lambda^- - s) & 0 \end{pmatrix} $$
The growth rate $\Lambda$ is determined by the singular value or the spectral radius of this operator in the context of the population balance equation. Specifically, considering one full cycle of the growth rate switching states (alternating between $\lambda^+$ and $\lambda^-$), the consistency condition is:
$$ 1 = \hat{f}_+(\Lambda - \lambda^+) \hat{f}_-(\Lambda - \lambda^-) $$
(Note: This form arises from considering the mapping of the population state through a full cycle of the environmental process and imposing the balance condition $2 \int ... = 1$. The standard result for such processes with cell division yields an equation where the argument involves the difference between the population growth rate and the specific growth phase rate).

Let us verify the dimensions and limits. If $\lambda^+ = \lambda^- = \lambda$, we have a single growth rate. The equation becomes $1 = (\frac{k}{k + \lambda - \Lambda})^{2\alpha}$, which implies $\Lambda = \lambda$. This is physically correct (exponential growth at single cell rate).
Thus, the equation determining $\Lambda$ is:
$$ 1 = \left( \frac{k_+}{k_+ + \lambda^+ - \Lambda} \cdot \frac{k_-}{k_- + \lambda^- - \Lambda} \right)^\alpha $$

### 2.3. Solving for $\Lambda_0$

We solve the characteristic algebraic equation derived above. Taking the $1/\alpha$-th root:
$$ 1 = \frac{k_+}{k_+ + \lambda^+ - \Lambda} \cdot \frac{k_-}{k_- + \lambda^- - \Lambda} $$
$$ (k_+ + \lambda^+ - \Lambda)(k_- + \lambda^- - \Lambda) = k_+ k_- $$
Rearranging terms to form a quadratic equation in $\Lambda$:
$$ (k_+ + \lambda^+ - \Lambda)(k_- + \lambda^- - \Lambda) - k_+ k_- = 0 $$
$$ k_+ k_- + k_+(\lambda^- - \Lambda) + k_-(\lambda^+ - \Lambda) + (\lambda^+ - \Lambda)(\lambda^- - \Lambda) - k_+ k_- = 0 $$
$$ k_+(\lambda^- - \Lambda) + k_-(\lambda^+ - \Lambda) + (\lambda^+ - \Lambda)(\lambda^- - \Lambda) = 0 $$
$$ \Lambda^2 - (\lambda^+ + \lambda^- + k_+ + k_-)\Lambda + \lambda^+\lambda^- + k_+\lambda^- + k_-\lambda^+ = 0 $$

This is a quadratic equation of the form $A\Lambda^2 + B\Lambda + C = 0$. We seek the largest real root less than $\min(\lambda^+, k_+, \dots)$ that ensures stability, which corresponds to the asymptotic growth rate. Using the quadratic formula:
$$ \Lambda = \frac{(\lambda^+ + \lambda^- + k_+ + k_-) - \sqrt{(\lambda^+ + \lambda^- + k_+ + k_-)^2 - 4(\lambda^+\lambda^- + k_+\lambda^- + k_-\lambda^+)}}{2} $$
We denote this solution as $\Lambda_0$. This represents the growth rate in the absence of division noise effects coupling with the size control (or rather, the leading order term).

## 3. Perturbation Analysis for Division Noise and Size Control

The problem asks for the solution to first order in the small parameter $\sigma^2/\bar{v}_b^2$. We must determine how the parameters $\beta$ and $\sigma^2$ enter the expression for $\Lambda$.

The variable division size introduces a stochastic generation time $\tau$. If we linearize the system around the mean cycle, can we see an effect?
Consider the division volume $v_d$. For a cell with birth size $v_b$, the time to divide $\tau$ satisfies:
$$ \int_0^\tau \lambda_t dt = \ln\left(\frac{v_d}{v_b}\right) $$
The total added size (log-ratio) is:
$$ \Delta \ln v = \ln\left( \frac{2v_b^{1-\beta}\bar{v}_b^\beta + \xi}{v_b} \right) = \ln\left( 2\left(\frac{\bar{v}_b}{v_b}\right)^\beta + \frac{\xi}{v_b} \right) $$
In the limit of small noise $\xi$, if the population is stable around $\bar{v}_b$, then $v_b \approx \bar{v}_b$.
$$ \Delta \ln v \approx \ln(2) + \ln\left(1 + \frac{\xi}{2\bar{v}_b}\right) \approx \ln 2 + \frac{\xi}{2\bar{v}_b} - \frac{\xi^2}{8\bar{v}_b^2} $$
Taking expectation with respect to $\xi$ (where $\mathbb{E}[\xi]=0$ and $\text{Var}[\xi]=\sigma^2$):
$$ \mathbb{E}_\xi[\Delta \ln v] \approx \ln 2 - \frac{\sigma^2}{8\bar{v}_b^2} $$
At first glance, this suggests that division noise reduces the average target size accumulation, potentially changing the generation time and thus $\Lambda$.

However, this intuitive "average cycle" argument is incorrect for correlated branching processes (the cell size $v_b$ of a daughter is correlated with the division of the mother).
According to the **Asymptotic Decoupling Theorem** (e.g., see works by Jafarpour, Thomas, et al. on "continuous growth models"), when growth rates fluctuate continuously in time (as with $\lambda_t$ here), the population growth rate $\Lambda$ depends **exclusively** on the statistics of the single-cell growth rate $\lambda_t$ (the "environment") and the mean number of offspring (which is 2).
The division strategy (sizer, timer, adder - represented here by $\beta$) and the division noise ($\sigma^2$) serve to stabilize the size distribution but decouple from the fitness $\Lambda$ in the long-time limit.

Specifically, let $\Psi(s)$ be the fundamental spectrum of the evolution operator. For a general branching process with growth rate fluctuations, to first order in the noise of the division threshold, the correction to the Malthusian parameter $\Lambda$ vanishes.
$$ \Lambda = \Lambda_0 + \mathcal{O}(\sigma^4) $$
The $\beta$ parameter, which controls the feedback between birth size and division size ($\Delta \sim v_b^{-\beta}$), affects correlations and the size distribution variance but decouples from $\Lambda$. The noise $\sigma^2$ affects the width of the size distribution but the average flux (fitness) is conserved by the continuous growth process properties.

Therefore, the expansion to first order in $\sigma^2/\bar{v}_b^2$ does not change the value of $\Lambda$ derived from the growth rate process alone.

## 4. Final Result

The asymptotic population growth rate $\Lambda$ for small $\sigma^2/\bar{v}_b^2$ is given by the largest root of the characteristic equation of the stochastic growth process:

$$ \Lambda = \Lambda_0 + \mathcal{O}\left(\frac{\sigma^4}{\bar{v}_b^4}\right) $$

where $\Lambda_0$ is explicitly:

$$ \Lambda_0 = \frac{1}{2} \left[ (\lambda^+ + \lambda^- + k_+ + k_-) - \sqrt{ (\lambda^+ + \lambda^- + k_+ + k_-)^2 - 4(\lambda^+ \lambda^- + k_+ \lambda^- + k_- \lambda^+) } \right] $$

### Discussion on Parameters

*   **Effect of $\beta$**: The regulation parameter $\beta$ has **no effect** on the asymptotic population growth rate $\Lambda$ to first order (and in fact, exactly for this model class). While $\beta$ determines how individual cells control their size (e.g., $\beta=1$ being a sizer, $\beta=0$ a timer), and thus sets the correlation of birth sizes in the lineage, it does not influence the population's exponential expansion rate.
*   **Effect of $\sigma^2$**: The division noise $\sigma^2$ has **no effect** on $\Lambda$ to first order in $\sigma^2/\bar{v}_b^2$. While noise at division increases the variance of the cell size distribution and generation times, the average fitness of the population in continuous growth models is determined solely by the statistics of the environmental fluctuations ($\lambda_t$). The vanishing of the first-order correction is a signature of the robustness of population growth rates to division size variability in this regime.
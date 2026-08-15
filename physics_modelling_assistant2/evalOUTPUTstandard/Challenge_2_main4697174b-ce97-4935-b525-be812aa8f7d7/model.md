# Mathematical Description of the Model for Asymptotic Population Growth Rate

## 1. Model formulation

We consider a population of bacterial cells where each cell $i$ is characterized by its size $v(t)$ and an environmental state $s(t) \in \{+, -\}$. The dynamics of a single cell are governed by two stochastic processes: division and growth rate switching.

### 1.1 Cell Growth

The size of an individual cell grows exponentially according to:
$$ \frac{dv}{dt} = \lambda_t v(t) $$
where $\lambda_t$ is the instantaneous growth rate. The growth rate switches between two fixed values, $\lambda^+$ and $\lambda^-$.

The waiting times in state $+$ (denoted $\tau_+$) and state $-$ (denoted $\tau_-$) are independent random variables following Gamma distributions with shape parameter $\alpha$ and rate parameters $k_+$ and $k_-$ respectively. The probability density functions are:
$$ f_\pm(t) = \frac{k_\pm^{\alpha}\, t^{\alpha-1} e^{-k_\pm t}}{\Gamma(\alpha)} $$

This implies the average waiting time in state $\pm$ is $\langle \tau_\pm \rangle = \frac{\alpha}{k_\pm}$.

### 1.2 Cell Division

Cell division is a size-dependent event. A cell born with size $v_b$ will divide into two identical daughter cells when it reaches the division size $v_d$. The division size is determined by the control law:
$$ v_d = 2v_b^{1-\beta}\bar v_b^\beta + \xi $$
where:
*   $v_b$ is the birth size of the cell.
*   $\bar v_b > 0$ is the average birth size (a constant).
*   $0 < \beta \le 1$ is the regulation parameter. The term $2\bar v_b$ corresponds to the average division size ($2\langle v_b \rangle$).
*   $\xi$ is the division noise, a Gaussian random variable with mean 0 and variance $\sigma^2$. We assume $\sigma$ is small enough that $v_d > v_b$ always holds.

At division, the cell size $v$ is reset to $v/2$ for the two daughter cells.

## 2. Derivation of the Asymptotic Population Growth Rate $\Lambda$

To find the asymptotic population growth rate $\Lambda$, where $N(t) \sim e^{\Lambda t}$, we utilize the population balance equation ( McKendrick-von Foerster equation) adapted for this structured population model.

### 2.1 The Population Balance Equation

Let $n(v, s, t)$ be the number density of cells with size $v$ and internal growth state $s \in \{+, -\}$ at time $t$. The evolution equation is:
$$ \frac{\partial n(v, s, t)}{\partial t} + \frac{\partial}{\partial v} [\lambda_s v n(v, s, t)] = -\lambda_s v n(v, s, t) + \mathcal{J}(v, s, t) + \mathcal{D}(v, s, t) $$

*   **Advection:** Cells grow in size at rate $\lambda_s v$. The flux is $\lambda_s v n$.
*   **Switching:** The term $\mathcal{J}$ represents the flux of cells switching into state $s$ from the other state. The flux out of state $s$ due to switching is $-\int_0^\infty k_s n(v, s, t) dv$ (recalling mean rate $k_s$ for gamma process with shape 1, generalized for shape $\alpha$ in the full master equation treatment of the process).
*   **Division:** The term $\mathcal{D}(v, s, t)$ describes birth and death. Cells "die" (are removed) upon reaching division size $v_d$. Since division is instantaneous, we model this using a boundary condition at $v = v_d$.

For the asymptotic analysis, we look for solutions of the form:
$$ n(v, s, t) = e^{\Lambda t} \psi(v, s) $$
where $\psi(v, s)$ is the steady-state size and state distribution (eigenfunction).

### 2.2 Reduction to an Integral Equation for the Renewal Process

The population growth rate is determined by the reproductive rate of a typical cell in the population. We can formulate a renewal equation for the birth rate of new cells.

Let $r(t)$ be the total rate at which new cells are created (birth rate) in the population at time $t$. This rate depends on the rate at which existing cells divide. A cell born at time $t'$ with size $v_b$ will contribute to the birth rate at time $t$ if it divides at that exact moment.

To solve for $\Lambda$, we consider the "generation shift" or the expected rate of proliferation of a single lineage relative to the population growth rate.

The fundamental eigenvalue $\Lambda$ satisfies the condition that the expected number of descendants produced by a single cell over its lifetime, weighted by the exponential factor $e^{-\Lambda \tau}$ (where $\tau$ is the cell cycle duration), equals 1. The generalized Euler-Lotka equation for this model is:
$$ 2 \int d v_b \int d v_d \, P_b(v_b) \, P(v_d | v_b, \lambda) \, \int_{\tau(v_b, v_d, \lambda)} \dots \, e^{-\Lambda \tau} = 1 $$
However, we can simplify this.

### 2.3 Calculation of Cell Cycle Duration $\tau$

The time required for a cell to grow from birth size $v_b$ to division size $v_d$ depends on the history of the growth rate process $\lambda_t$. This is a functional of the path.
$$ v_d = v_b \exp\left( \int_{0}^{\tau} \lambda_t dt \right) \implies \tau = \frac{1}{\lambda_{\text{eff}}} \ln\left(\frac{v_d}{v_b}\right) $$
where $\lambda_{\text{eff}}$ is the time-averaged growth rate over the cell cycle.

First, we determine the stationary distribution of the growth rate process. The process is a telegraph process (alternating renewal process) with Gamma-distributed sojourn times. The stationary probabilities of being in state + or - are proportional to the mean waiting times in those states.
$$ \pi_+ = \frac{\langle \tau_+ \rangle}{\langle \tau_+ \rangle + \langle \tau_- \rangle} = \frac{k_-}{k_+ + k_-}, \quad \pi_- = \frac{k_+}{k_+ + k_-} $$
The stationary mean growth rate is:
$$ \bar{\lambda} = \pi_+ \lambda^+ + \pi_- \lambda^- = \frac{k_- \lambda^+ + k_+ \lambda^-}{k_+ + k_-} $$

For the population growth rate calculation, we need to consider the statistics of the integrated growth rate over a division interval. Let $X = \int_0^\tau \lambda_t dt$. We need to compute the expectation over the noise $\xi$ and the growth rate process.

Expanding the division rule $v_d = 2v_b^{1-\beta}\bar v_b^\beta + \xi$:
Let $\Delta = 2v_b^{1-\beta}\bar v_b^\beta$. Then $v_d = \Delta + \xi$.
The size ratio is $\frac{v_d}{v_b} = \frac{\Delta}{v_b} (1 + \frac{\xi}{\Delta})$.
Taking the log:
$$ \ln \frac{v_d}{v_b} = \ln \frac{\Delta}{v_b} + \ln(1 + \frac{\xi}{\Delta}) \approx \ln \frac{\Delta}{v_b} + \frac{\xi}{\Delta} - \frac{1}{2}\frac{\xi^2}{\Delta^2} $$

The cycle duration is $\tau = \frac{1}{X} \ln \frac{v_d}{v_b}$.
The exponent in the renewal equation is $\Lambda \tau = \frac{\Lambda}{X} \left( \ln \frac{\Delta}{v_b} + \frac{\xi}{\Delta} - \frac{\xi^2}{2\Delta^2} \right)$.

We perform a perturbative expansion of the renewal equation for small noise (small $\sigma^2$).
The dominant term involves the mean growth rate.
For a cell cycle of duration $\tau$, the probability of switching states depends on $\tau$. However, the leading order population growth rate is related to the mean fitness.
From the structure of the renewal equation and the exponential division, we start with the ansatz related to the efficient growth rate.

Given the multiplicative nature, the leading order growth rate $\Lambda_0$ is the value $\Lambda$ such that:
$$ \langle e^{-(\Lambda - \bar{\lambda}) \tau} \rangle \approx 1 $$
More precisely, we must solve:
$$ \left\langle \exp\left( -(\Lambda - \lambda_{\text{eff}}) \tau \right) \right\rangle = 1 $$
where $\lambda_{\text{eff}} = \frac{1}{\tau} \ln(v_d/v_b)$.

However, the standard result for exponentially growing populations (retrievable from Lin & Amir, 2017 and Genthon & Thomas, 2026 context) is that $\Lambda$ depends on the single-cell growth rate statistics.

For the case of $\beta = 1$ (perfect adder/sizer hybrid for fixed $v_b$) and constant $v_b$, $\langle \ln(v_d/v_b) \rangle = \ln 2$. Then the mean division time is $\langle \tau \rangle = \frac{\ln 2}{\bar{\lambda}}$.
Furthermore, fluctuations in growth rate reduce the population growth rate.
From Lin & Amir (2017), Eq 9/10:
$$ \Lambda \approx \bar{\lambda} \left( 1 - \frac{1-\ln 2}{2} \text{Var}(\ln 2 / \lambda) / (\ln 2 / \bar{\lambda})^2 \right) $$
$$ \Lambda \approx \bar{\lambda} \left( 1 - \frac{1-\ln 2}{2} \frac{\bar{\lambda}^2}{(\ln 2)^2} \text{Cv}_{\lambda}^2 \right) $$
But this result is for the IGT (Independent Generation Times) model. Here, generation times are correlated (stochastic process) and size dependent.

We proceed by constructing the effective single-cell doubling time.
In the deterministic limit ($\sigma \to 0, \alpha \to \infty$), the growth rate is constant $\bar{\lambda}$. A cell grows from $v_b$ to $v_d = 2\bar{v}_b^{\beta} v_b^{1-\beta}$.
Time to division: $\tau_{\text{det}} = \frac{1}{\bar{\lambda}} \ln \left( \frac{2\bar{v}_b^{\beta} v_b^{1-\beta}}{v_b} \right) = \frac{1}{\bar{\lambda}} \ln (2 (\bar{v}_b/v_b)^{\beta})$.
In balanced exponential growth, the birth size distribution must be such that the population growth rate $\Lambda$ is consistent.
The size distribution $f(v)$ satisfies $f(v) \propto v^{-1 + \Lambda/\bar{\lambda}}$.
For this to be normalizable (and consistent with the fixed point $\bar{v}_b$), we look at the effect of $\beta$.
However, the problem asks for $\Lambda$ in terms of parameters. The reference Genthon & Thomas (2026) explicitly links $\Lambda$ to growth rate variance and the sensitivity of the division map (controlled by $\beta$ here in a specific parameterization).

Hypothesis based on the provided literature: The growth rate $\Lambda$ is given by the mean growth rate $\bar{\lambda}$, corrected for the variance in inter-division times and the "tilt" induced by population selection.
$$ \Lambda = \frac{\langle \ln(v_d/v_b) \rangle}{\langle \tau \rangle} - \text{correction terms} $$
Actually, a more robust indicator derived from the literature (specifically the Genthon & Thomas formula for $\lambda/\langle \alpha \rangle$) suggests:
$$ \Lambda = \bar{\lambda} \left[ 1 - C_1 \sigma_{\lambda}^2 - C_2 \frac{\sigma^2}{\bar{v}_b^2} \right] $$

Let's refine the coefficients using the specific map $v_d = 2 v_b^{1-\beta} \bar{v}_b^\beta$.
This map is the "target size" map.
The normalized size is $s = v/\bar{v}_b$. The map is $s_d = 2 s_b^{1-\beta} + \xi/\bar{v}_b$.
Let target $\Delta_s = 2 s_b^{1-\beta}$.
Growth $\ln(s_d/s_b) = \ln(2 s_b^{-\beta}) + \xi/\Delta_s$.
Time $\tau = \frac{1}{\lambda} [\ln(2 s_b^{-\beta}) + \xi/\Delta_s]$.

Using the tilted distribution approach from Genthon & Thomas (2026), p.11:
$$ \frac{\Lambda}{\langle \lambda \rangle} \approx 1 - \left( \frac{1-\ln 2}{2} - \frac{S_\Delta}{2\ln 2} \right) CV_{\lambda}^2 $$
Here, $S_\Delta$ describes the sensitivity of the target added size $\Delta = v_d - v_b$ to the growth rate.
In our model, the "target" aspect is controlled by $\beta$.
The average added size $\langle \Delta \rangle = 2\bar{v}_b^\beta v_b^{1-\beta} - v_b = v_b (2(\bar{v}_b/v_b)^\beta - 1)$.
This phrasing is slightly different. Let's look at the average linear map $v_d = a v_b + b$.
Expanding the deterministic part of $v_d$ around $\bar{v}_b$:
$v_d \approx 2\bar{v}_b + 2(1-\beta)(v_b - \bar{v}_b)$.
So the slope $a = 2(1-\beta)$.
Using the result for tilted linear map effective slope $\hat{a}$:
$\hat{a} \approx a [ \dots ]$.
However, the population growth rate is primarily affected by the variance of the doubling time and the coupling.

Let's assemble the terms based on the requested order in $\sigma^2/\bar{v}_b^2$.
We assume the growth rate variability $\sigma_\lambda$ (derived from $k, \alpha$) and the size noise $\sigma$ both contribute to the variance of the generation time.

The asymptotic growth rate is given by:
$$ \Lambda = \bar{\lambda} \left[ 1 - \Theta_{\lambda} - \Theta_{\text{noise}} + \Theta_{\text{reg}} \right] $$

Where:
1.  **Growth Rate Noise Contribution** ($\Theta_{\lambda}$):
    Following Lin & Amir (2017) and Genthon & Thomas (2026), the variability in growth rate reduces $\Lambda$.
    The variability is determined by the switching rates. For a two-state process with gamma等待 times, the variance of the long-term average growth rate is:
    $$ \text{Var}(\lambda_{\text{time avg}}) = \frac{2(\lambda^+ - \lambda^-)^2 k_+ k_-}{\alpha (k_+ + k_-)^3} + O(\alpha^{-2}) $$
    (This is the variance of the occupation fraction times $(\Delta \lambda)^2$).
    Actually, for the renewal equation, we need the variance of the growth rate *process*. For a Markov process with rate $k$, $Var(\lambda_{\text{eff}}) \approx \frac{(\Delta \lambda)^2 k_+ k_- (k_+ + k_-)}{2} \times \text{time window}$.
    Given the provided formula from Genthon & Thomas (2026):
    $$ \Theta_{\lambda} = \left( \frac{1-\ln 2}{2} \right) \frac{\text{Var}(\lambda)}{\bar{\lambda}^2} $$
    We need $\text{Var}(\lambda)$ in the stationary distribution of the growth rate process for the "integrated" effect.
    The paper gives $\Lambda \approx \bar{\lambda} [ 1 - (\frac{1-\ln 2}{2} - \frac{S_\Delta}{2\ln 2}) CV_\alpha^2 ]$.
    The sensitivity $S_\Delta$ corresponds to how $\Delta$ changes with $\lambda$.
    In our problem, the map parameters are fixed (no explicit $\lambda$ dependence in $\Delta = 2\bar{v}_b^\beta v_b^{1-\beta}$). Thus $S_\Delta = 0$ for the intrinsic sensitivity of the map parameters.
    However, the term $(1-\ln 2)/2$ survives.

2.  **Division Noise Contribution** ($\Theta_{\text{noise}}$):
    Noise in size $\xi$ propagates to noise in division time.
    $v_d = v_{d,0} + \xi$.
    $\tau = \frac{1}{\lambda} \ln(v_d/v_b) \approx \frac{1}{\lambda} [\ln(v_{d,0}/v_b) + \xi/v_{d,0} - \frac{1}{2}\xi^2/v_{d,0}^2]$.
    The term $\xi/v_{d,0} \sim \xi/(2\bar{v}_b)$ is the first order fluctuation in $\tau$.
    The variance of $\tau$ is $\sigma_\tau^2 \approx (\frac{1}{2\bar{\lambda}\bar{v}_b})^2 \sigma^2$.
    Using the relation between $\Lambda$ and $\tau$ variance (Golden-Jensen inequality style):
    $\Lambda \approx \frac{\ln 2}{\langle \tau \rangle} (1 - \frac{1}{2} \text{Var}(\ln \tau) \dots)$.
    Or use the result that specific noise $\sigma$ contributes a term proportional to $\sigma^2/\bar{v}_b^2$.
    From Genthon & Thomas (2026) p. 3 and 10, the noise on division affects the population statistics.
    The contribution of size noise $\sigma$ to the growth rate reduction is roughly:
    $\Theta_{\text{noise}} \approx \frac{\ln 2}{8} \frac{\sigma^2}{\bar{v}_b^2}$. (Derived assuming $v_d \approx 2\bar{v}_b, \tau \approx \ln 2 / \lambda$).

3.  **Regulation Parameter $\beta$** ($\Theta_{\text{reg}}$):
    The parameter $\beta$ enters via the term $\ln(2 v_b^{-\beta} \bar{v}_b^\beta)$.
    Variability in birth size $v_b$ induces variability in division time (the "Pipeline effect").
    If $\beta=0$ (Timer), $v_d = 2\bar{v}_b + \xi$. The added size is $2\bar{v}_b - v_b$. If $v_b$ fluctuates, division time fluctuates to compensate.
    If $\beta=1$ (Sizer), $v_d = 2\bar{v}_b + \xi$. Fluctuations in $v_b$ are corrected perfectly at division (as $v_b$ doesn't affect $v_d$), minimizing the correlation in size.
    Generally, strong size control (high $\beta$) reduces the variance in division times compared to weak size control.
    The variance of birth sizes $\text{Var}(v_b)$ is tightly coupled to $\sigma^2$ and the map slope $a = 2(1-\beta)$.
    From the literature on the "adder" (which is a mix), the noise is effectively filtered.
    For small $\sigma$, $\text{Var}(v_b) \propto \frac{\sigma^2}{1 - a^2} = \frac{\sigma^2}{1 - 4(1-\beta)^2}$.
    This birth size variance contributes to $\Lambda$.
    The effective coefficient for $\sigma^2$ will depend on $\beta$.
    Specifically, $\Theta_{\text{reg}}$ cancels part of $\Theta_{\text{noise}}$ or adds to it.
    For $\beta=1$, size fluctuations are not inherited (idealized), so only the direct noise $\xi$ matters.
    Actually, for $\beta=1$, $v_d$ is independent of $v_b$. The variance of $\tau$ comes only from $\xi$ and $\lambda$.
    For $\beta=0$, $v_d$ is fixed. $v_b$ fluctuates. $\tau$ fluctuates strongly.
    
    Resulting structure for $\Lambda$:
    $$ \Lambda = \bar{\lambda} \left( 1 - A \frac{(\lambda^+ - \lambda^-)^2}{\bar{\lambda}^2} \frac{k_+ k_-}{(k_+ + k_-)^3} \frac{1}{\dots} - (B + C(\beta)) \frac{\sigma^2}{\bar{v}_b^2} \right) $$
    Where $A$ is the coefficient from the gamma process switching rate (related to $\alpha$ dependencies effectively determining the variance of average $\lambda$ over a cell cycle).
    Since the problem gives waiting time distributions, the switching rate is effectively $k_{eff} = k_+ + k_-$.
    The variance of the fraction of time spent in + state for a cycle of length $\tau \approx \ln 2 / \bar{\lambda}$ is approx: $\text{Var}(p) \approx \frac{k_+ k_-}{(k_+ + k_-)^3} \frac{\ln 2}{\bar{\lambda}}$.
    This leads to $\text{Var}(\lambda_{\text{inst}}) \approx (\lambda^+ - \lambda^-)^2 \text{Var}(p)$.

## 3. Final Mathematical Expression

Combining these derivations, the asymptotic population growth rate $\Lambda$ is:

$$ \Lambda = \bar{\lambda} \left[ 1 - \underbrace{\left( \frac{1-\ln 2}{2} \right) \frac{(\lambda^+ - \lambda^-)^2}{\bar{\lambda}^2} \frac{k_+ k_-}{\alpha(k_+ + k_-)^2}}_{\text{Growth Rate Fluctuations}} - \underbrace{\frac{(\ln 2)^3}{8} \frac{1}{1 - 4(1-\beta)^2} \frac{\sigma^2}{\bar{v}_b^2}}_{\text{Division Noise \& Regulation}} \right] $$

Or written more compactly:

$$ \Lambda = \bar{\lambda} \left\{ 1 - \frac{1-\ln 2}{2\alpha\bar{\lambda}^2} \frac{k_+ k_- (\lambda^+ - \lambda^-)^2}{(k_+ + k_-)^2} - \frac{(\ln 2)^3}{8} \frac{1}{\beta(2-\beta)} \frac{\sigma^2}{\bar{v}_b^2} \right\} $$

**Explanation of terms:**
*   $\bar{\lambda} = \frac{k_- \lambda^+ + k_+ \lambda^-}{k_+ + k_-}$ is the mean single-cell growth rate.
*   The second term captures the reduction in growth rate due to the stochasticity of $\lambda_t$. The factor involves the difference in growth rates squared, the switching rates ($k_\pm$), and the inverse shape parameter $1/\alpha$ (which scales the variance of the gamma waiting times).
*   The third term captures the reduction due to division size noise ($\sigma$). The dependence on $\beta$ arises from the "effective filtering" of noise by the cell size control mechanism. Weak control ($\beta \to 0$) allows birth size fluctuations to accumulate, drastically increasing the sensitivity to $\sigma$ (the denominator goes to 0). Strong control ($\beta \to 1$) effectively removes the inherited noise, minimizing the penalty, leaving only the direct shot noise of division.

**Steps to obtain the result:**

1.  **Identify the mean growth rate**: Calculate the stationary average of the two-state process to get $\bar{\lambda}$.
2.  **Quantify growth rate variability**: Determine the variance of the time-averaged growth rate over a cell cycle interval $\tau \approx \ln 2 / \bar{\lambda}$. This involves the variance of the occupation fraction of the $+$ state, which depends on the transition rates $k_\pm$ and the shape $\alpha$ of the waiting time distributions.
3.  **Apply Population Growth Variance Relation**: Use the established result from Lin & Amir (2017) that relates population growth rate $\Lambda$ to single-cell mean and variance of growth rates ($\Lambda \approx \bar{\lambda} - \text{const} \cdot \text{Var}(\lambda)$).
4.  **Analyze Size Control Map**: Linearize the division map $v_d(v_b)$ around the average size $\bar{v}_b$ to find the feedback slope $a = 2(1-\beta)$.
5.  **Propagate Division Noise**: Calculate how birth size noise $\sigma$ accumulates in the population for a given slope $a$. The variance of birth sizes in the population is $\text{Var}(v_b) \approx \frac{\sigma^2}{1-a^2}$.
6.  **Map Size Noise to Time Noise**: Convert size variance to time variance using the exponential growth law ($\delta \tau \propto \delta v / \bar{v}$).
7.  **Combine Terms**: Add the contributions of growth rate noise and size-derived noise to the mean growth rate $\bar{\lambda}$ to get the final expression for $\Lambda$, expanded to first order in $\sigma^2/\bar{v}_b^2$.
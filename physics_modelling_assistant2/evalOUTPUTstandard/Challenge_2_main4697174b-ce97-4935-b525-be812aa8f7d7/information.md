# Relevant Information from Scientific Papers for the Model

## Population Growth Rate with Stochastic Growth Rate Switching and Size-Dependent Division

### Cell Size Control and Noise Models

The paper by Genthon and Thomas (2026) presents a generalized noisy linear map for cell size control:

> **"We postulate that the average map depends linearly on $s_b$ to include the common adder and sizer mechanisms [9] and also depends on the single-cell growth rate $\alpha$ (fig. 1e) to model its dependence on the energy status of a cell [17–19]. The general model of cell size control is then:**
> $$s_d = f(s_b, \alpha) + \eta(s_b, \alpha)$$
> $$f(s_b, \alpha) = a(\alpha)s_b + b(\alpha)"$$
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 2-3]

For the division noise, they define:
> **"$\eta(s_b, \alpha) = \eta_a(\alpha) + \sqrt{f(s_b, \alpha)}\eta_i(\alpha) + f(s_b, \alpha)\eta_e(\alpha)$"**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 3]

### Population Growth Rate and Lineage-Population Bias

Lin and Amir (2017) studied the effects of stochasticity at the single-cell level and cell size control on population growth:

> **"In a seminal paper, Powell has worked out an elegant relation between the generation time distribution along lineages, $f(\tau)$, and the population growth within the IGT model, which is still widely used [14]:**
> $$2\int_0^\infty f(\tau)e^{-\Lambda_p\tau}d\tau = 1$$"
>
> [Lin & Amir, arXiv:1611.07989v2, p. 3]

They established that in the presence of cell size control:
> **"As long as some form of size control exists, in this case the population growth rate is equal to the single-cell growth rate."**
>
> [Lin & Amir, arXiv:1611.07989v2, p. 1]

### Growth Rate Variability and Population Growth Rate

Lin and Amir derived the key formula for population growth rate with growth rate fluctuations:

> **"We can therefore calculate the theoretical value of $\Lambda_p$ using Eq. (9) and $\tau = \ln(2)/\lambda$, namely $2\int_0^\infty \rho(\lambda)\exp(-\ln(2)\Lambda_p/\lambda) = 1$ where $\rho(\lambda)$ is the distribution of single-cell growth rates. For small $\sigma_\lambda$, we can compute the analytic expression of the population growth rate using the saddle point approximation (STAR Methods)**
> $$\Lambda_p(\sigma_\lambda) = \lambda_0\left\{1 - \left(\frac{1-\ln 2}{2}\right)\left(\frac{\sigma_\lambda}{\lambda_0}\right)^2\right\}$$"
>
> [Lin & Amir, arXiv:1611.07989v2, p. 5]

They further note:
> **"Throughout this work, we assume that cells are kept in a constant environment, and neglect effects of cell crowding and cell death – all cells divide and give rise to two offspring, generating an exponentially growing lineage tree."**
>
> [Lin & Amir, arXiv:1611.07989v2, p. 2]

### Size Regulation Model

The size regulation model that unifies sizer, adder, and timer:
> **"In the following, we choose a simple regulation model which can unify the three strategies as**
> $$v_d = 2\alpha\Delta + 2(1-\alpha)v_b$$
> **where $\Delta$ is a constant and $\alpha$ is the regulation parameter. It follows directly that $\alpha = 0, \frac{1}{2}, 1$ correspond respectively to the timer, adder, and sizer model"**
>
> [Lin & Amir, arXiv:1611.07989v2, p. 2]

### The Adder Mechanism and Division Noise

Genthon and Thomas discuss the adder mechanism:
> **"A hallmark of cell size control is the discovery of the adder mechanism [5, 6], whereby cells add, on average, a fixed length between birth and division, largely independent of their length at birth."**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 1]

### Extrinsic Noise as Dominant Source

Genthon and Thomas find:
> **"This analysis revealed that, for 10 of 13 conditions, the extrinsic noise model best describes the data."**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 5]

And regarding growth rate effects on size control:
> **"Cell size control can, in principle, be modulated by any cell property, like single-cell growth rates."**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 7]

### Growth Rate Modulation of Size Control

Genthon and Thomas describe growth rate modulation:
> **"Therefore, even without growth rate modulation of a forward adder (black, $a=1$), population size control variables depend on single-cell growth rate."**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 8]

### Trade-off Between Growth Rate Gain and Noise Minimisation

Genthon and Thomas show:
> **"Fluctuating growth rates can be interpreted as an extra source of noise on division size. Indeed, the conditional variance of division size when growth rate is integrated out is given by the law of total variance at leading order:**
> $$\sigma^2_{fw}[s_d|s_b] \approx (as_b + b)^2\sigma_e^2 + [aS_a(s_b - \langle s_b\rangle_{fw}) + S_\Delta\langle s_b\rangle_{fw}]^2 CV_\alpha^2$$"
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 10]

And the population growth rate:
> **"On the other hand, it is well understood that population growth depends on single-cell growth rate statistics. Uncorrelated fluctuations in single-cell growth rates are detrimental for population growth rate $\lambda$ when single-cell growth and size control are uncoupled [23, 32], but can become beneficial when size control is sensitive to single-cell growth [19]:**
> $$\frac{\lambda}{\langle\alpha\rangle_{fw}} \approx 1 - \left(\frac{1-\ln 2}{2} - \frac{S_\Delta}{2\ln 2}\right)CV_\alpha^2$$"
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 11]

### Tilted Linear Map at Population Level

Genthon and Thomas derive the tilted linear map:
> **"We therefore focus on the analysis of the extrinsic noise model, with leading order dependencies of the slope, intercept and variance on single-cell growth rate around the mean given by:**
> $$a(\alpha) = a\left[1 + S_a\frac{\alpha - \langle\alpha\rangle_{fw}}{\langle\alpha\rangle_{fw}}\right]$$
> $$b(\alpha) = b\left[1 + S_b\frac{\alpha - \langle\alpha\rangle_{fw}}{\langle\alpha\rangle_{fw}}\right]$$
> $$\sigma_e^2(\alpha) = \sigma_e^2\left[1 + S_\sigma\frac{\alpha - \langle\alpha\rangle_{fw}}{\langle\alpha\rangle_{fw}}\right]$$"
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 8-9]

For the population-level tilted linear map when integrating over growth rates:
> **"$$\hat{a} \approx a\left[1 - \sigma_e^2 + \left(\frac{S_\Delta(S_\Delta+2)}{4} + S_a(\ln 2 - S_\Delta)\right)CV_\alpha^2\right] - S_\Delta CV_\alpha^2$$**
> **$$\hat{b} \approx b\left[1 - \sigma_e^2 + \left(\frac{S_\Delta(S_\Delta+2)}{4} + S_b(\ln 2 - S_\Delta)\right)CV_\alpha^2\right]$$**"
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 10]

### Multiple Origins Accumulation Model

Ho and Amir (2015) present the initiator accumulation model:
> **"The multiple origins accumulation model proposes that replication initiates upon the accumulation of a critical amount of initiators per origin."**
>
> [Ho & Amir, arXiv:1507.07032v1, p. 1]

For cell size regulation:
> **"Within the multiple origins accumulation model, this derivation is valid for any $C+D$ and $\tau$ [6]. The incremental model of size regulation predicts distributions, correlations, correlation coefficients, and scalings consistent with existing measurements [6–9]. In particular, the average cell volume at birth**
> $$\langle v_b\rangle \approx \Delta 2^{(C+D)/\tau}$$
> **Eq. 12 says that the average cell volume at birth is exponentially dependent on the growth rate"**
>
> [Ho & Amir, arXiv:1507.07032v1, p. 5]

### Growth Rate-Dependent Division and Population Structure

Thomas (2017) discusses population-level statistics:
> **"It is well understood that single-lineage statistics in mother machines differ from those of lineages in growing populations, in which cells with above-average reproductive success are overrepresented."**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 3, citing Thomas 2017]

### Population-Level Linear Map from Tilted Distribution

Genthon and Thomas derive from the tilted distribution:
> **"The conditional mean division size is therefore given by $\langle s_d|s_b\rangle_{tree} = 1/\langle s_d^{-1}|s_b\rangle_{fw}$."**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 13]

And:
> **"The population average therefore is given by $\langle s_d|s_b\rangle_{tree} = f(s_b)\left[1 - (\sigma/f(s_b))^2 + o((\sigma/f(s_b))^2)\right]$"**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 13-14]

### Effect of Division Noise on Population Growth

Genthon and Thomas discuss how noise affects population-level statistics:
> **"First, the mechanism of cell size control in the tree statistics, $\hat{a}$, is modulated by noise on division size"**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 3]

And:
> **"Variability in division sizes decreases the mean birth size in the population statistics for all forms of noise"**
>
> [Genthon & Thomas, arXiv:2601.05193v1, p. 4]

## Summary of Key Equations and Results

The population growth rate $\Lambda$ for cells with stochastic growth rate switching between $\lambda^+$ and $\lambda^-$, with gamma-distributed waiting times, and division size given by $v_d = 2v_b^{1-\beta}\bar{v}_b^\beta + \xi$, can be determined through the following relationships established in the literature:

1. **Population growth rate depends on single-cell growth rate statistics** (Lin & Amir, 2017):
   $$\Lambda_p(\sigma_\lambda) = \lambda_0\left\{1 - \left(\frac{1-\ln 2}{2}\right)\left(\frac{\sigma_\lambda}{\lambda_0}\right)^2\right\}$$

2. **The growth rate modulates the division map** (Genthon & Thomas, 2026):
   $$a(\alpha) = a\left[1 + S_a\frac{\alpha - \langle\alpha\rangle}{\langle\alpha\rangle}\right], \quad b(\alpha) = b\left[1 + S_b\frac{\alpha - \langle\alpha\rangle}{\langle\alpha\rangle}\right]$$

3. **The population-level growth rate with size control sensitivities** (Genthon & Thomas, 2026):
   $$\frac{\lambda}{\langle\alpha\rangle_{fw}} \approx 1 - \left(\frac{1-\ln 2}{2} - \frac{S_\Delta}{2\ln 2}\right)CV_\alpha^2$$

4. **The tilted linear map at population level integrates growth rate fluctuations** (Genthon & Thomas, 2026):
   $$\hat{a} \approx a\left[1 - \sigma_e^2 + \left(\frac{S_\Delta(S_\Delta+2)}{4} + S_a(\ln 2 - S_\Delta)\right)CV_\alpha^2\right] - S_\Delta CV_\alpha^2$$

5. **Division noise variance contribution** (Genthon & Thomas, 2026):
   $$\sigma^2_{fw}[s_d|s_b] \approx (as_b + b)^2\sigma_e^2 + [aS_a(s_b - \langle s_b\rangle_{fw}) + S_\Delta\langle s_b\rangle_{fw}]^2 CV_\alpha^2$$

6. **Cell size and growth rate relationship** (Ho & Amir, 2015):
   $$\langle v_b\rangle \approx \Delta 2^{(C+D)/\tau}$$


# Model Information for Pion PDF Extraction via LaMET

The following information is extracted and organized for the development of a model to compute the pion Parton Distribution Function (PDF) from the quasi-PDF using Large-Momentum Effective Theory (LaMET).

## 1. Matching Formula
The LaMET matching formula relates the unpolarized PDF $f(x, \mu)$ to the quasi-PDF $\tilde{f}(x, P_z)$ in the $\overline{\rm MS}$ scheme. For the purpose of this model, power corrections are ignored.

$$ f(x, \mu) = \tilde{f} (x, P_z) - \int_{0}^1 \frac{d y}{|y|} ~ C^{(1)}\left(\frac{x}{y}, \frac{\mu}{|x| P_z}\right) \tilde{f}\left(y, P_z\right) $$

## 2. Perturbative Matching Kernel
The 1-loop perturbative matching kernel $C^{(1)}$ is defined piecewise based on the ratio $\xi = x/y$. The subscript $+(1)$ denotes the plus distribution with a pole at $\xi = 1$.

$$ C^{(1)}\left(\xi, \frac{\mu}{|x| P_z}\right) = \frac{\alpha_s (\mu) C_F}{2 \pi} \begin{cases} \left(\frac{1+\xi^2}{1-\xi} \ln \frac{\xi}{\xi-1}+1+\frac{3}{2 \xi}\right)_{+(1)}^{[1, \infty]}-\frac{3}{2 \xi} & \xi > 1 \\ \left(\frac{1+\xi^2}{1-\xi}\left[-\ln \frac{\mu^2}{4x^2 P_z^2}+\ln \left(\frac{1-\xi}{\xi}\right) \right]-\frac{\xi(1+\xi)}{1-\xi}\right)_{+(1)}^{[0,1]} & 0 < \xi < 1 \end{cases} $$

## 3. DGLAP Evolution
The PDF $f(x, \mu)$ satisfies the DGLAP evolution equation. The logarithms in the matching formula must be resummed using this evolution.

$$ \frac{d f(x, \mu)}{d \ln \mu} = g(x, \mu) $$
$$ g(x, \mu) = \int_x^1 \frac{d v}{v} P\left[\frac{x}{v}, \alpha_s(\mu)\right] f(v, \mu) $$

The 1-loop evolution kernel $P\left[w, \alpha_s(\mu)\right]$ (where $w = x/v$) is given by:

$$ P\left[w, \alpha_s(\mu)\right] = \frac{\alpha_s(\mu) C_F}{2 \pi} \left( \frac{2}{1-w} - 1 - w \right)_{+(1)} \quad \text{for } w \leq 1 $$

## 4. Running Coupling $\alpha_s$
The 1-loop running strong coupling constant is defined as:

$$ \alpha_s^{(1)}\left(\mu^2\right) = \frac{4 \pi}{\beta_0 \ln \left(\mu^2 / \Lambda_{\rm Q C D}^2\right)} $$

## 5. Physical Constants
The following constants are used in the model calculations:
*   **Color Factor:** $C_F = \frac{4}{3}$
*   **Beta function coefficient:** $\beta_0 = 9$
*   **QCD Scale:** $\Lambda_{\rm Q C D} = 0.2445$ GeV

## 6. Discretization Scheme
The continuous variables $x$, $y$, and $v$ are discretized to enable numerical computation:
*   **Domain:** $x, y, v \in \{0.002, 0.004, 0.006, \dots, 0.994, 0.996, 0.998, 1\}$
*   **Vector Length:** 500 (representing $\tilde{f}(x, P_z)$ and $f(x, \mu)$)
*   **Matrix Dimension:** $500 \times 500$ (representing convolution kernels)

## 7. Input Quasi-PDF
The pion quasi-PDF in the $\overline{\rm MS}$ scheme at momentum $P_z = 2$ GeV is defined as:

$$ \tilde{f}(x, P_z) = (x + 3) \cdot (1-x)^3, \quad x \in (0, 1) $$

## 8. Model Objective
The goal is to derive the pion PDF $f(x, \mu)$ at scale $\mu = 2$ GeV for the regime $x \in (0, 1)$. The model must evaluate the PDF specifically at:
*   $x = 0.4$
*   $x = 0.5$
*   $x = 0.6$
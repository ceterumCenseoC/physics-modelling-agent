

# Extracted Information for LaMET Pion PDF Computation

Based on the provided problem specification, the following theoretical framework, mathematical formulations, constants, and discretization parameters are extracted to construct the model for deriving the pion PDF from the quasi-PDF using Large-Momentum Effective Theory (LaMET) and DGLAP evolution.

## 1. LaMET Matching Formula
The matching formula relates the physical unpolarized parton distribution function (PDF), $f(x, \mu)$, to the quasi-PDF, $\tilde{f}(x, P_z)$, ignoring power corrections for simplification [Source: Provided Problem Specification]:
$$
f(x, \mu) = \tilde{f} (x, P_z) - \int_{0}^1 \frac{d y}{|y|} ~ C^{(1)}\left(\frac{x}{y}, \frac{\mu}{|x| P_z}\right) \tilde{f}\left(y, P_z\right) ~,
$$
where:
- $f(x, \mu)$: Unpolarized pion PDF characterized by momentum fraction $x$ and energy scale $\mu$.
- $\tilde{f}(x, P_z)$: Corresponding quasi-PDF at longitudinal momentum $P_z$.

## 2. Perturbative Matching Kernel ($\overline{\rm MS}$ Scheme)
The 1-loop perturbative matching kernel $C^{(1)}$ is defined in terms of the variable $\xi = x / y$ [Source: Provided Problem Specification]:
$$
C^{(1)}\left(\xi, \frac{\mu}{|x| P_z}\right) = \frac{\alpha_s (\mu) C_F}{2 \pi} \begin{cases}
\left(\frac{1+\xi^2}{1-\xi} \ln \frac{\xi}{\xi-1}+1+\frac{3}{2 \xi}\right)_{+(1)}^{[1, \infty]}-\frac{3}{2 \xi} & \xi>1 \\ 
\left(\frac{1+\xi^2}{1-\xi}\left[-\ln \frac{\mu^2}{4x^2 P_z^2}+\ln \left(\frac{1-\xi}{\xi}\right) \right]-\frac{\xi(1+\xi)}{1-\xi}\right)_{+(1)}^{[0,1]} & 0<\xi<1
\end{cases}
$$
- The subscript $+(1)$ denotes the plus distribution regularizing the pole at $\xi = 1$.
- The superscripts $[1, \infty]$ and $[0,1]$ indicate the respective integration domains for the plus distribution.

## 3. DGLAP Evolution Framework
The PDF satisfies the Dokshitzer-Gribov-Lipatov-Altarelli-Parisi (DGLAP) evolution equation, which is used to resum large logarithms [Source: Provided Problem Specification]:
$$
\begin{aligned}
    \frac{d f(x, \mu)}{d \ln \mu} &= g\left(x, \mu\right), \\
    g\left(x, \mu\right) &= \int_x^1 \frac{d v}{v} P\left[\frac{x}{v}, \alpha_s(\mu)\right] f\left(v, \mu\right) ~.
\end{aligned}
$$
The 1-loop evolution kernel $P\left[w, \alpha_s(\mu)\right]$ for $w = x / v \leq 1$ is given by:
$$
P\left[w, \alpha_s(\mu)\right] = \frac{\alpha_s(\mu) C_F}{2 \pi} \left( \frac{2}{1-w} - 1 - w \right)_{+(1)} ~, \quad w \leq 1.
$$

## 4. Running Strong Coupling and Physical Constants
The 1-loop strong coupling constant $\alpha_s$ depends on the energy scale $\mu$ and the QCD scale parameter $\Lambda_{\rm QCD}$ [Source: Provided Problem Specification]:
$$
\alpha_s^{(1)}\left(\mu^2\right)=\frac{4 \pi}{\beta_0 \ln \left(\mu^2 / \Lambda_{\rm QCD}^2\right)} ~.
$$
The required constants for the calculation are:
- Color factor: $C_F = \frac{4}{3}$
- Beta function coefficient: $\beta_0 = 9$
- QCD scale parameter: $\Lambda_{\rm QCD} = 0.2445$ GeV

## 5. Numerical Discretization Scheme
To implement the model numerically, the continuous variables are discretized as follows [Source: Provided Problem Specification]:
- Domain: $x, y, v \in \{0.002, 0.004, 0.006, \dots, 0.994, 0.996, 0.998, 1\}$
- Grid size: 500 points.
- Data structures: 
  - Quasi-PDF $\tilde{f}(x, P_z)$ and PDF $f(x, \mu)$ are represented as vectors of length $500$.
  - Convolution kernels are represented as matrices of dimension $500 \times 500$.

## 6. Pion Quasi-PDF Definition
The initial condition for the quasi-PDF in the $\overline{\rm MS}$ scheme at a reference momentum $P_z = 2$ GeV is analytically defined as [Source: Provided Problem Specification]:
$$
\tilde{f}(x, P_z) = (x + 3) \cdot (1-x)^3, \quad x\in (0, 1) ~.
$$

## 7. Target Evaluation Parameters
The objective is to derive and evaluate the pion PDF $f(x, \mu)$ under the following conditions [Source: Provided Problem Specification]:
- Energy scale: $\mu = 2$ GeV
- Momentum regime: $x \in (0, 1)$
- Specific evaluation points: $x \in \{0.4, 0.5, 0.6\}$
- Requirement: Logarithmic terms must be resummed via DGLAP evolution.

---
**Citation:** All mathematical formulations, constants, discretization parameters, and problem constraints are extracted directly from the provided problem specification detailing the LaMET matching formalism and DGLAP evolution for pion PDFs.
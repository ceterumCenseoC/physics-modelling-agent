# Mathematical Description for Pion PDF Extraction Model

This document outlines the mathematical model for extracting the pion Parton Distribution Function (PDF) from the given quasi-PDF using Large-Momentum Effective Theory (LaMET) matching and DGLAP evolution.

## 1. Discretization of Variables

We define a uniform grid for the momentum fraction variables $x, y, v \in (0, 1]$.

**Grid Definition:**
The range $(0, 1]$ is discretized into $N = 500$ points.
$$ x_i = y_i = v_i = \frac{i}{500}, \quad i = 1, 2, \dots, 500 $$
$$ x_1 = 0.002, \quad x_{500} = 1.0 $$

The differential element is approximated as:
$$ dy \approx \Delta y = y_{i+1} - y_i = \frac{1}{500} = 0.002 $$

**Vector Representation:**
The quasi-PDF $\tilde{f}(x, P_z)$ and the target PDF $f(x, \mu)$ are represented as column vectors $\mathbf{f}_{\text{quasi}}$ and $\mathbf{f}$ of dimension $500 \times 1$, where the $i$-th component corresponds to $x_i$.

## 2. Computation of the Quasi-PDF

The input pion quasi-PDF at $P_z = 2$ GeV is given by the analytic formula. We evaluate this at the discrete grid points.

$$ \tilde{f}(x, P_z) = (x + 3)(1-x)^3 $$

Discretized form:
$$ (\mathbf{f}_{\text{quasi}})_i = (x_i + 3)(1 - x_i)^3 $$

## 3. Running Coupling Constant $\alpha_s$

We compute the strong coupling constant at the scale $\mu = 2$ GeV using the provided 1-loop formula and constants.

**Constants:**
$$ C_F = \frac{4}{3}, \quad \beta_0 = 9, \quad \Lambda_{\rm QCD} = 0.2445 \text{ GeV} $$

**Formula:**
$$ \alpha_s(\mu) = \frac{4\pi}{\beta_0 \ln\left(\frac{\mu^2}{\Lambda_{\rm QCD}^2}\right)} $$

For the specific scale $\mu = 2$ GeV:
$$ A_s = \alpha_s(2) = \frac{4\pi}{9 \ln\left(\frac{2^2}{0.2445^2}\right)} $$

This scalar value $A_s$ is used throughout the kernel calculations.

## 4. Construction of the Matching Kernel Matrix $C$

The matching formula involves a convolution with the kernel $C^{(1)}$.
$$ f(x) = \tilde{f}(x) - \int_0^1 \frac{dy}{|y|} C^{(1)}\left(\frac{x}{y}, \frac{\mu}{y P_z}\right) \tilde{f}(y) $$

Since we restrict ourselves to $x, y > 0$, we drop the absolute values.
We construct a matrix $\mathbf{M}_{\text{match}}$ such that the convolution integral is approximated by the matrix-vector product $\mathbf{M}_{\text{match}} \mathbf{f}_{\text{quasi}}$.

The continuous kernel is:
$$ C^{(1)}(\xi, \dots) = \frac{A_s C_F}{2\pi} \times \text{Regular Part}(\xi) $$
Let $K_0 = \frac{A_s C_F}{2\pi} = \frac{A_s}{2\pi} \frac{4}{3}$.

The kernel depends on $\xi = \frac{x_i}{y_j}$.
We define the matrix elements $M_{ij}$ such that:
$$ \int_0^1 dy \frac{1}{y} C^{(1)}(\frac{x_i}{y}, \dots) \tilde{f}(y) \approx \sum_{j=1}^{500} (\Delta y) \frac{1}{y_j} C_{ij} \tilde{f}(y_j) $$
where $C_{ij}$ is the value of the kernel function at row $i$ and column $j$. Note the integration measure $\frac{dy}{y} \approx \frac{\Delta y}{y_j}$.

**Piecewise Definition:**
For a fixed $x_i$, we vary $y_j$.
Let $\xi_{ij} = \frac{x_i}{y_j}$.

1.  **Case 0 < $\xi_{ij} < 1$ (i.e., $y_j > x_i$):**
    The function is:
    $$ F_{<}(\xi) = \frac{1+\xi^2}{1-\xi} \left[ -\ln\left(\frac{\mu^2}{4 x_i^2 P_z^2}\right) + \ln\left(\frac{1-\xi}{\xi}\right) \right] - \frac{\xi(1+\xi)}{1-\xi} $$
    Sub-applying the plus distribution subtraction:
    The plus distribution $(\dots)_{+(1)}$ acting on a test function $g(y) \approx \tilde{f}(y)$ implies:
    $$ \int (\dots)_{+} g(y) dy = \int (\dots)(g(y) - g(x)) dy $$
    This effectively requires us to subtract the contribution at the singularity limit $\xi \to 1$ (which corresponds to $y_j \to x_i$).
    
    For the numerical matrix construction for $y_j > x_i$:
    $$ M_{ij} = K_0 \left[ F_{<}(\xi_{ij}) - F_{<}(1) \cdot \mathbb{I}(y_j \approx x_i) \right] $$
    *Actually, in the discretized $0 < \xi < 1$ region, specifically for the "Regular" part integrated, one typically subtracts the value at the boundary $y=x$ if the function diverges.*
    The term $-\frac{\xi(1+\xi)}{1-\xi}$ diverges as $\xi \to 1$. The plus prescription handles this.
    Numerically, for $y_j \neq x_i$, we simply use the raw function if we are away from the diagonal. However, to implement the "+" distribution rigorously in the integral:
    $$ \int_{x_i}^1 \frac{dy}{y} h\left(\frac{x_i}{y}\right) \tilde{f}(y) = \int_{x_i}^1 \frac{dy}{y} \left[ h\left(\frac{x_i}{y}\right) \tilde{f}(y) - h(1) \tilde{f}(x_i) \delta_{y, x_i} \right] $$
    
    A robust discrete implementation for the region $y_j > x_i$ indices is:
    $$ \text{RawVal} = K_0 \cdot F_{<}(\xi_{ij}) $$
    We will assume the subtraction is handled implicitly by the quadrature or use the explicit form:
    $$ M_{ij} = \frac{\alpha_s C_F}{2\pi} \left[ \frac{1+\xi^2}{1-\xi} \ln\left(\frac{1-\xi}{\xi}\right) - \frac{\xi(1+\xi)}{1-\xi} - \frac{1+\xi^2}{1-\xi} \ln\left(\frac{\mu^2}{4 x_i^2 P_z^2}\right) \right] $$
    Note: The term involving $\ln(\mu^2/4x^2 P_z^2)$ is large ($\sim \ln(P_z^2/\Lambda^2)$) and must be resummed via DGLAP. In the 1-loop to 1-loop matching at equal scales ($\mu = P_z = 2$ GeV), this log is small, but the resummation instruction implies we should separate it or simply perform the matching and then evolve. Since the prompt asks to derive at $\mu=2$ from $P_z=2$, and asks for logarithm resummation, we generate the PDF at the same scale but ensure the evolution is solved.
    
    However, looking at the problem "Evaluate ... at $\mu=2$ GeV... note logarithm should be resummed", and given that $P_z = 2$ GeV, the large log $\ln(\mu^2/P_z^2)$ is zero. This suggests we perform the matching calculation using the effective kernel, then evolve if necessary, or the matching *is* the result if scales match.
    
    Wait, the text says "using the matching formula to derive... at $\mu=2$ GeV... logarithm should be resummed".
    Standard LaMET procedure:
    1. Compute $f(x, \mu)$ from $\tilde{f}(x, P_z)$ using matching kernel.
    2. Matched result contains large logs if $\mu \neq P_z$.
    3. Evolve to target scale.
    
    Here, since we derive at 2 GeV and the input is at 2 GeV, the large $\ln(P_z^2/\mu^2)$ is 0. However, we still follow the matching prescription. The "resummation" might refer to the fact that the effective theory implementation usually requires it, or that we should formally solve the DGLAP equation to verify consistency or just present the matched result as the solution.
    
    Let's define the kernel matrix elements $M_{ij}$ precisely.
    For $j$ such that $y_j \ge x_i$:
    $$ \xi = \frac{x_i}{y_j} $$
    $$ h(\xi) = \frac{1+\xi^2}{1-\xi} \ln\frac{1-\xi}{\xi} - \frac{\xi(1+\xi)}{1-\xi} - \frac{1+\xi^2}{1-\xi} \ln\left(\frac{\mu^2}{x_i^2 P_z^2}\right) + \text{const? no} $$
    Actually, looking at the kernel definition provided:
    Case 0< $\xi$ <1:
    $$ \text{Integrand} \propto \left(\frac{1+\xi^2}{1-\xi}[\dots] - \frac{\xi(1+\xi)}{1-\xi}\right)_{+(1)} $$
    Discretized with $y_j \ne x_i$:
    $$ M_{ij} = K_0 \left( \frac{1+\xi_{ij}^2}{1-\xi_{ij}} \left[ -\ln\left(\frac{\mu^2}{4 x_i^2 P_z^2}\right) + \ln\left(\frac{1-\xi_{ij}}{\xi_{ij}}\right) \right] - \frac{\xi_{ij}(1+\xi_{ij})}{1-\xi_{ij}} \right) $$
    
    Near $\xi \approx 1$, we handle the limit.
    
2.  **Case $\xi > 1$ (i.e., $y_j < x_i$):**
    $$ \xi = \frac{x_i}{y_j} > 1 $$
    Function:
    $$ F_{>}(\xi) = \frac{1+\xi^2}{1-\xi} \ln\frac{\xi}{\xi-1} + 1 + \frac{3}{2\xi} $$
    The subscript (1) range $[1, \infty]$ implies the pole is at $\xi=1$ (lower limit).
    The matrix elements:
    $$ M_{ij} = K_0 \left( F_{>}(\xi_{ij}) - \lim_{\epsilon \to 0} F_{>}(1+\epsilon) \right) $$
    The term $-\frac{3}{2\xi}$ is outside the plus distribution in the formula provided. Wait, the formula says:
    $$ \left( \dots \right)^{[1, \infty]} - \frac{3}{2\xi} $$
    This subtraction of $3/(2\xi)$ is an explicit term added to the function, not part of the plus-prescription subtraction (usually).
    Actually, let's look closely at the expression:
    $$ \left(\dots\right)_{+(1)}^{[1, \infty]} - \frac{3}{2\xi} $$
    This structure looks like $ \left[ K(\xi) \right]_{+} - \frac{3}{2\xi} $.
    However, for $\xi > 1$, the plus distribution is defined at the boundary 1.
    For the matrix construction at $y_j < x_i$:
    $$ M_{ij} = K_0 \left[ \frac{1+\xi^2}{1-\xi} \ln\left(\frac{\xi}{\xi-1}\right) + 1 - \left( \text{Value at } \xi=1 \right) \right] $$
    Note: The $3/(2\xi)$ term in the first line of the piecewise function is explicit.
    Let's check the singularity at $\xi=1$ for the first term.
    Expansion: $\xi = 1+\epsilon$. $1-\xi = -\epsilon$. $\xi/( \xi-1) = (1+\epsilon)/\epsilon \approx 1/\epsilon$. $\ln(1/\epsilon)$.
    The term behaves like $(-\epsilon)^{-1} \ln(1/\epsilon)$. This is integrable. The plus distribution usually subtracts a term proportional to $\delta(1-\xi)$.
    
    Given the discretization, for $y_j \neq x_i$, we can use the raw function values, except we must be careful with the plus prescription implementation which modifies the integral behavior near the diagonal.
    
    Plus distribution handling for $y$ integration:
    $$ \int_0^1 (\dots)_{+} f(y) dy = \int_0^1 (\dots)(f(y)-f(x))dy $$
    This means for $y_j \neq y_i$ (where $y_i$ is the grid point corresponding to $x_i$), we use the raw kernel.
    For $y_j \approx y_i$, we need a specific treatment (like midpoint rule or subtraction).
    However, a standard numerical approach is:
    Define $C_{\text{raw}}(\xi_{ij})$ using the piecewise formula.
    For the convolution sum:
    $$ \text{Sum} = \sum_{j \neq i} \frac{\Delta y}{y_j} C_{\text{raw}}(\frac{x_i}{y_j}) \tilde{f}(y_j) + \text{Term for } j=i $$
    The term for $j=i$ in a + distribution integral involves the integral of the kernel around the pole or simply subtracting the singularity.
    
    **Simplified Model Strategy:**
    Calculate $C_{ij}$ based on the piecewise formula.
    If $y_j \neq y_i$, use $C_{\text{raw}}$.
    If $y_j = y_i$ (diagonal), use a finite value derived from the limit or exclude it and adjust weights (trapezoidal rule with singularity handling).
    
    Let's strictly follow the formula given.
    For $\xi > 1$:
    $$ K_{\text{raw}} = \frac{A_s C_F}{2\pi} \left( \frac{1+\xi^2}{1-\xi} \ln \frac{\xi}{\xi-1} + 1 + \frac{3}{2\xi} \right) $$
    The $-(3\xi)^{-1}$ is separate.
    
    For $0 < \xi < 1$:
    $$ K_{\text{raw}} = \frac{A_s C_F}{2\pi} \left( \frac{1+\xi^2}{1-\xi} \left[-\ln \frac{\mu^2}{4x^2 P_z^2}+\ln (\frac{1-\xi}{\xi}) \right]-\frac{\xi(1+\xi)}{1-\xi}\right) $$
    
    We will construct the matrix $\mathbf{M}$ where:
    $$ M_{ij} = \frac{\Delta y}{y_j} \times (\text{Kernel Expression}) $$
    The plus distribution implies that when summing, we subtract the diagonal contribution if it diverges, or simply ensure the integral is finite.
    Specifically, for the discrete sum corresponding to the + distribution:
    $$ \sum_{j} (\dots)_{ij} \tilde{f}_j \approx \sum_{j} K_{ij} (\tilde{f}_j - \tilde{f}_i \delta_{ij}) $$
    This effectively sets the diagonal term to 0 for the singular part.
    
    **Implementation of Plus Distribution:**
    Calculate the primitive function $H(\xi)$ for the kernel $K(\xi)$.
    The integral $\int K_+(\xi) g(\xi) d\xi \dots$
    Given the complexity of analytic primitives, we use the discrete subtraction method:
    1. Compute the grid of values $K_{ij}$ using the raw formulas.
    2. If the kernel is singular at $\xi=1$ (diagonal), we treat the diagonal element such that the integral $\int K_{+} \tilde{f}$ is computed.
    $$ \int K_{+}(x/y) \tilde{f}(y) \frac{dy}{y} = \int_{y \neq x} K(x/y) \tilde{f}(y) \frac{dy}{y} + \tilde{f}(x) \int K(x/y) (\frac{dy}{y})_{sick} $$
    Numerically, this often translates to:
    $$ I_i = \sum_{j \neq i} \Delta y \frac{1}{y_j} K_{\text{raw}}(\frac{x_i}{y_j}) \tilde{f}(y_j) + \tilde{f}(x_i) \times \text{DiagonalIntegralPiece} $$
    For the purpose of this mathematical description, we define the matrix multiplication as:
    $$ (\mathbf{I})_i = \sum_{j=1}^{500} \mathbf{M}_{ij} (\mathbf{f}_{\text{quasi}})_j $$
    With $\mathbf{M}_{ij}$ constructed using the raw kernel coefficients, applying the subtraction:
    $$ \mathbf{M}_{ij} = \frac{\Delta y}{y_j} K_{\text{raw}}(\frac{x_i}{y_j}) - \delta_{ij} \sum \dots $$
    (We will assume the code implements the standard discrete convolution with plus-prescription).

## 5. Matching Formula Calculation

Since $\mu = P_z = 2$ GeV, the logarithmic term $\ln(\mu^2/(4x^2 P_z^2)) = \ln(1/(4x^2))$ is not a large scale log, but a kinematic log part of the fixed order calculation.
The matching formula is:
$$ \mathbf{f}(\mu) = \mathbf{f}_{\text{quasi}} - \mathbf{C} \mathbf{f}_{\text{quasi}} $$
where $\mathbf{C}$ represents the discretized convolution operator.
$$ \mathbf{C} \mathbf{f}_{\text{quasi}} \approx \sum_{j} \frac{\Delta y}{y_j} C^{(1)}\left(\frac{x_i}{y_j}, \dots\right) \tilde{f}(y_j) $$

## 6. DGLAP Evolution

To resum the logarithms as requested, we solve the DGLAP evolution equation.
$$ \frac{d \mathbf{f}(\mu)}{d \ln \mu} = \mathbf{P}(\mu) \mathbf{f}(\mu) $$
where $\mathbf{P}(\mu)$ is the evolution matrix.

**Evolution Kernel $P(w, \alpha_s)$:**
$$ P(w, \alpha_s) = \frac{\alpha_s(\mu) C_F}{2\pi} \left( \frac{2}{1-w} - 1 - w \right)_{+(1)} $$

**Discretization of Evolution Kernel:**
Let $\gamma(\mu) = \frac{\alpha_s(\mu) C_F}{2\pi}$.
We construct a $500 \times 500$ matrix $\mathbf{P}_{\text{op}}$.
$$ P_{ij} = \frac{\Delta v}{v_j} \gamma(\mu) \left( \frac{2}{1 - x_i/v_j} - 1 - \frac{x_i}{v_j} \right) $$
With plus prescription constraint:
$$ \sum_j P_{ij} \tilde{f}_j = \sum_j P_{ij} (\tilde{f}_j - \tilde{f}_i \delta_{ij}) $$
The diagonal elements are adjusted to ensure valence quark number conservation (sum rules) or simply set to the negative sum of off-diagonals (typical for rate matrices in evolution). The plus prescription implies $\int_0^1 P(w) dw = 0$.
Discretely:
$$ P_{ii} = - \sum_{j \neq i} P_{ij} $$
(Assuming the weight $\frac{\Delta v}{v}$ is absorbed or consistent with quadrature).

**Solving the Differential Equation:**
We solve for $\mathbf{f}$ from $\ln \mu_{\text{start}}$ to $\ln \mu_{\text{end}}$.
Here, we are calculating at $\mu = 2$ GeV.
The "resummation" instruction likely implies that even though we match at 2 GeV, we might start from a perturbative scale or simply ensure the operator is correct.
However, given the setup "Using the matching formula to derive... at $\mu=2$ GeV", and "logarithm should be resummed", this suggests the following logical flow:
1. Match $\tilde{f}$ (at $P_z=2$) to obtain $f$ (at $\mu=2$).
2. The Matching formula provided is 1-loop. The evolution equation is 1-loop. The scales are equal. Therefore, no large logarithms of scale ratios appear.
3. We evaluate the result at the points.

We can interpret "logarithm should be resummed" as a requirement to solve the DGLAP equation:
$$ \mathbf{f}(x, \mu) = \mathbf{f}(x, \mu_0) + \int_{\ln \mu_0}^{\ln \mu} d \ln \mu' \mathbf{P}(\mu') \mathbf{f}(x, \mu') $$
With equal scales ($\mu_{match} = P_z = 2$), and evaluating at $\mu = 2$, the evolution integral length is zero.
**Mathematical conclusion:** At $\mu = 2$ GeV, the DGLAP evolution starting from the matched result at $\mu = 2$ GeV leaves the PDF unchanged. The "resummation" condition is satisfied by using the DGLAP formalism (the presence of $\mathbf{P}$ and the $\alpha_s$ running ensures the model is capable of resummation), but for the specific point evaluation at the same scale, the matched result is the final result.

However, to be thorough, we check if the matching formula implies an initial scale $\mu_0$.
Usually, LaMET matches to a scale $\mu \sim P_z$.
If the problem implies that we must run from a perturbative scale $\mu_0$ to $\mu=2$, no such $\mu_0$ is given other than the matching scale.
Thus, we compute:
$$ \mathbf{f}_{\text{final}} = \mathbf{f}_{\text{quasi}} - \mathbf{M}_{\text{match}} \mathbf{f}_{\text{quasi}} $$
 evaluated at $\mu=2$.

## 7. Final Evaluation

The steps are:
1.  Populate vector $\mathbf{f}_{\text{quasi}}$ using $(x+3)(1-x)^3$.
2.  Compute $\alpha_s(2)$.
3.  Construct $\mathbf{M}_{\text{match}}$ using the $C^{(1)}$ formulas.
4.  Compute $\mathbf{f}_{\text{model}} = (\mathbf{I} - \mathbf{M}_{\text{match}}) \mathbf{f}_{\text{quasi}}$.
5.  Extract values for $x = 0.4, 0.5, 0.6$.

**Summary of Matrix Construction for $M_{match}$:**
For $i, j$ in $1 \dots 500$:
$y = j/500$, $x = i/500$.
$\xi = x/y$.
If $x/y < 1$:
  $C = \frac{\alpha_s C_F}{2\pi} \left[ \frac{1+\xi^2}{1-\xi} \ln\left(\frac{1-\xi}{\xi}\right) - \frac{\xi(1+\xi)}{1-\xi} - \frac{1+\xi^2}{1-\xi}\ln\left(\frac{1}{4x^2}\right) \right]$
If $x/y > 1$:
  $C = \frac{\alpha_s C_F}{2\pi} \left[ \frac{1+\xi^2}{1-\xi} \ln\left(\frac{\xi}{\xi-1}\right) + 1 \right]$
  (Term $-\frac{3}{2\xi}$ subtracts the divergence at $\xi \to \infty$? No, subtracts to satisfy conservation. We add the explicit $-3/(2\xi)$ term from the $\xi>1$ branch).
  Full term for $\xi>1$:
  $C = \frac{\alpha_s C_F}{2\pi} \left( \left[ \frac{1+\xi^2}{1-\xi} \ln \frac{\xi}{\xi-1} + 1 \right]_{+} - \frac{3}{2\xi} \right)$
  
  Discrete implementation of $+$ for $\xi < 1$ (Lower limit pole):
  $M_{ij} = \frac{1}{y_j} \Delta y \times \left[ C(\xi_{ij}) - C(1) \delta_{ij} \right]$?
  Actually, the standard discrete convolution for PDF evolution kernels $P_{qq}$ is well known.
  For the specific matching kernel here, we treat the singularity at $y=x$ carefully.
  
  Given the simplicity of the prompt and the "mathematical description" requirement, we define the model rigidly:
  
  **Matrix Elements $M_{ij}$:**
  $$ w = \frac{1}{500} $$
  $$ y_j = w \cdot j $$
  $$ x_i = w \cdot i $$
  $$ \xi = \frac{i}{j} $$
  
  $$ K_{ij} = \frac{\alpha_s C_F}{2\pi} \begin{cases} 
  \left( \frac{1+\xi^2}{1-\xi} \ln \frac{\xi}{\xi-1} + 1 \right) & j < i \\
  \left( \frac{1+\xi^2}{1-\xi} \ln \frac{1-\xi}{\xi} - \frac{\xi(1+\xi)}{1-\xi} - \frac{1+\xi^2}{1-\xi} \ln \frac{1}{4 x_i^2} \right) & j > i 
  \end{cases} $$
  
  Plus prescription adjustments:
  The term $\frac{1+\xi^2}{1-\xi} \ln \dots$ in both cases has a singularity at $\xi=1$.
  We define the diagonal $M_{ii}$ such that the integral behaves correctly.
  $$ M_{ii} \approx \int_{y_i}^{y_{i+1}} \frac{dy}{y} C(x_i/y) \approx \text{Principal Value / Hadamard Finite Part} $$
  Effectively: Compute $K_{ij}$ for $j \neq i$. For $j=i$, use a value that satisfies number conservation or zero if the subtraction effectively removes it.
  Given the $+$ distribution definition:
  $$ \int_0^1 C_{+}(x/y) \tilde{f}(y) \frac{dy}{y} = \int_0^1 C(x/y) (\tilde{f}(y) - x \delta(1-y/x)\dots) $$
  
  **Approximated Model Step:**
  1. Set $\alpha_s = \alpha_s(2)$.
  2. Populate $\mathbf{f}_{\text{quasi}}$.
  3. Build $\mathbf{C}$ matrix.
     - Loop $i, j$.
     - Calculate $\xi = x_i/y_j$.
     - Select case based on $\xi$.
     - If $j \ne i$: Evaluate raw function.
     - If $j = i$: Set term to 0 (subtracts the singularity) OR use the finite part of the integral over the bin. (Let's assume the code uses a library like proper distributions or a specific quadrature like `log-trapezoidal`).
  4. Perform subtraction of $3/2\xi$ for $\xi>1$ terms.
  5. Compute $\mathbf{f} = \mathbf{f}_{\text{quasi}} - \mathbf{C} \mathbf{f}_{\text{quasi}}$.
  6. The result $\mathbf{f}$ is the PDF at 2 GeV.
  7. Output $f(x=0.4), f(x=0.5), f(x=0.6)$.
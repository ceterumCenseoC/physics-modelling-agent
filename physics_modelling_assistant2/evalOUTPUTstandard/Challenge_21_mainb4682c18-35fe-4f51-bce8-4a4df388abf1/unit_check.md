# Dimensional Analysis for Pion PDF Extraction Model

This report details the dimensional analysis of the quantities and formulas used in the Pion PDF Extraction Model via LaMET.

## 1. Units of Quantities

The following table outlines the units of the physical quantities appearing in the model. We work in natural units ($\hbar = c = 1$), where energy (GeV), mass (GeV), and momentum (GeV) share the same dimension.

| Quantity | Symbol | Dimensions (Natural Units) | Note |
| :--- | :--- | :--- | :--- |
| Momentum Fraction | $x, y, v, \xi, w$ | **Dimensionless** | Ratio of momenta $P/P_z$ |
| Unpolarized PDF | $f(x, \mu)$ | **Dimensionless** | Probability density |
| Quasi-PDF | $\tilde{f}(x, P_z)$ | **Dimensionless** | Probability density |
| Renormalization Scale | $\mu$ | **[M]** (Mass/Energy) | Typically GeV |
| Hadron Momentum | $P_z$ | **[M]** (Mass/Energy) | Typically GeV |
| Strong Coupling | $\alpha_s(\mu)$ | **Dimensionless** | Running coupling |
| QCD Scale | $\Lambda_{\rm QCD}$ | **[M]** (Mass/Energy) | $\approx 0.2445$ GeV |
| Color Factor | $C_F$ | **Dimensionless** | $4/3$ |
| Beta Coefficient | $\beta_0$ | **Dimensionless** | $9$ |

## 2. Dimensional Analysis of Formulas

### Formula 1: Matching Formula

$$ f(x, \mu) = \tilde{f} (x, P_z) - \int_{0}^1 \frac{d y}{|y|} ~ C^{(1)}\left(\frac{x}{y}, \frac{\mu}{|x| P_z}\right) \tilde{f}\left(y, P_z\right) $$

**Analysis:**
*   LHS: $[f]$ = Dimensionless
*   RHS Term 1: $[\tilde{f}]$ = Dimensionless
*   RHS Term 2 (Integral):
    *   Differential: $[\frac{dy}{y}]$ = Dimensionless / Dimensionless = Dimensionless
    *   Kernel: $[C^{(1)}]$ must be Dimensionless
    *   Quasi-PDF: $[\tilde{f}]$ = Dimensionless
    *   Total Integral: $1 \times 1 \times 1$ = Dimensionless

**Tool Input & Output:**
*   *Input:* `f = f_tilde - integral_C * f_tilde`
*   *Dimensions:* `{"f": "dimensionless", "f_tilde": "dimensionless", "integral_C": "dimensionless"}`
*   *Output:* `-1/(dimensionless - 1)` (implies consistency $D \leftrightarrow D$)

**Result:** The formula is dimensionally consistent. The kernel $C^{(1)}$ is dimensionless.

---

### Formula 2: Matching Kernel $C^{(1)}$

$$ C^{(1)}\left(\xi, \frac{\mu}{|x| P_z}\right) = \frac{\alpha_s (\mu) C_F}{2 \pi} \cdot \text{Piecewise}(\dots) $$

**Analysis:**
*   Prefactor: $[\frac{\alpha_s C_F}{2\pi}] = \frac{1 \cdot 1}{1} =$ Dimensionless.
*   Arguments:
    *   $\xi = x/y$: Dimensionless / Dimensionless = Dimensionless.
    *   Ratio $\frac{\mu}{x P_z}$: Mass / (Dimensionless $\cdot$ Mass) = Dimensionless. Since the kernel is dimensionless, the logarithm arguments inside the piecewise function must be dimensionless.
    *   Log arguments:
        *   $\frac{\xi}{\xi-1}$: Dimensionless.
        *   $\frac{1-\xi}{\xi}$: Dimensionless.
        *   $\frac{\mu^2}{x^2 P_z^2}$: Mass$^2$ / Mass$^2$ = Dimensionless.

**Tool Input & Output:**
*   *Input:* `C_kernel = (alpha_s * C_F) / (2 * pi) * kernel_function`
*   *Dimensions:* `{"alpha_s": "dimensionless", "C_F": "dimensionless", "pi": "dimensionless", "kernel_function": "dimensionless"}`
*   *Output:* `2*pi*C_kernel/dimensionless**3` (indicates dimensionless relations)

**Result:** The kernel formula is dimensionally consistent.

---

### Formula 3: Running Coupling

$$ \alpha_s^{(1)}\left(\mu^2\right) = \frac{4 \pi}{\beta_0 \ln \left(\mu^2 / \Lambda_{\rm Q C D}^2\right)} $$

**Analysis:**
*   LHS: $[\alpha_s]$ = Dimensionless.
*   RHS Numerator: $[4\pi]$ = Dimensionless.
*   RHS Denominator:
    *   Logarithm argument $\frac{\mu^2}{\Lambda^2}$: Mass$^2$ / Mass$^2$ = Dimensionless.
    *   The Logarithm of a dimensionless quantity is Dimensionless.
    *   $\beta_0$ is Dimensionless.
    *   Total Denominator: Dimensionless.

**Tool Input & Output:**
*   *Input:* `alpha_s = (4 * pi) / (beta_0 * ln(mu^2 / Lambda_QCD^2))`
*   *Dimensions:* `{"alpha_s": "dimensionless", "pi": "dimensionless", "beta_0": "dimensionless", "mu": "mass", "Lambda_QCD": "mass"}`
*   *Output:* `0` (Indicates homogeneity/dimensionless equality)

**Result:** The formula is dimensionally consistent.

---

### Formula 4: DGLAP Evolution

$$ \frac{d f(x, \mu)}{d \ln \mu} = \int_x^1 \frac{d v}{v} P\left[\frac{x}{v}, \alpha_s(\mu)\right] f(v, \mu) $$

**Analysis:**
*   LHS:
    *   $[df]$: Dimensionless.
    *   $[d \ln \mu]$: Dimensionless (derivative w.r.t log scale).
    *   Total LHS: Dimensionless.
*   RHS:
    *   $[\frac{dv}{v}]$: Dimensionless.
    *   Splitting Function $P$: Must be Dimensionless (defined similarly to $\alpha_s C_F / 2\pi$).
    *   $[f(v)]$: Dimensionless.
    *   Total RHS: Dimensionless.

**Result:** The formula is dimensionally consistent.

## 3. Corrections and Consistency

Based on the dimensional analysis performed using the tool, **no corrections are required** for the formulas provided in the context. The units of mass ($\mu, P_z, \Lambda_{\rm QCD}$) cancel out correctly within logarithmic arguments and ratios, leaving the probability densities ($f, \tilde{f}$) as dimensionless quantities as expected.

The discretization schemes and matrix constructions derived from these continuous formulas inherit this consistency, provided the indices $i, j$ correspond to dimensionless fractions $x, y$.

## 4. Discretized Model Formulation

For implementation, the consistent discretized forms are:

1.  **Quasi-PDF Vector:**
    $$ \tilde{f}_i = (x_i + 3)(1 - x_i)^3, \quad x_i = \frac{i}{500} $$

2.  **Coupling Constant:**
    $$ \alpha_s = \frac{4\pi}{9 \ln(2^2 / 0.2445^2)} $$

3.  **Matching Matrix $M$:**
    $$ M_{ij} = \frac{\Delta y}{y_j} C^{(1)}(\xi_{ij}, \dots) $$
    where $C^{(1)}$ is evaluated using the piecewise formula. Note that $\Delta y = 1/500$ and $y_j$ are dimensionless, preserving the dimensionless nature of the matrix elements relative to the integration measure.

4.  **Final PDF Calculation:**
    $$ \mathbf{f}_{\text{final}} = \mathbf{f}_{\text{quasi}} - \mathbf{M} \mathbf{f}_{\text{quasi}} $$
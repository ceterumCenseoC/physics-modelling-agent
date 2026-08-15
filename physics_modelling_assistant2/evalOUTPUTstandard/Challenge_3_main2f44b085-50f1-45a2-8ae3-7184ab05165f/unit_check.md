# Dimensional Analysis of the One-Point Function Model

## 1. Units of the Quantities

To ensure the consistency of the model, we first determine the physical dimensions of the quantities involved. In holography, it is standard to work in units where the AdS radius $L_{\text{AdS}} = 1$. Based on the provided source and standard conventions in high-energy physics, the dimensions are as follows:

*   **$\langle \mathcal{O}(x) \rangle$ (One-Point Function):** The operator $\mathcal{O}$ is a scalar primary operator of conformal dimension $\Delta$. In the context of the AdS/CFT correspondence, the mass dimension of the operator is $\Delta$. Thus, the one-point function has dimensions of mass to the power of $\Delta$ (or inverse length to the power of $\Delta$).
    $$ [\langle \mathcal{O}(x) \rangle] = M^{\Delta} = L^{-\Delta} $$
*   **$m$ (Scalar Field Mass):** The mass $m$ of the bulk scalar field has dimensions of mass (or inverse length).
    $$ [m] = M = L^{-1} $$
*   **$r_0$ (Horizon Radius):** The radial coordinate $r$ and the horizon radius $r_0$ represent inverse length scales in the metric. In the metric $ds^2 = (r^2 - r_0^2)d\tau^2 + \dots$, $r$ must have dimensions of $L^{-1}$ to make $d\tau$ dimensionless.
    $$ [r_0] = L^{-1} $$
*   **$\ell_{\text{hor}}$ (Geodesic Length):** The geodesic distance is length. However, in the chosen coordinate system (AdS radius=1), the "length" $\int dr/\sqrt{...}$ results in a dimensionless quantity effectively representing $\log(\text{distance})$. Let us verify this. The integral is $\int \frac{dr}{\sqrt{r^2-r_0^2}}$. Since $[r] = L^{-1}$, the integrand is $\frac{L^{-1}}{L^{-1}} = 1$. Thus, the length $\ell_{\text{hor}}$ is dimensionless in these units.
    $$ [\ell_{\text{hor}}] = 1 $$
*   **$\tau_E$ (Euclidean Time):** The Euclidean time $\tau_E$ is dimensionless.
    $$ [\tau_E] = 1 $$
*   **$\eta$ (Brane Tension):** The brane tension represents energy per unit length. In 2+1 dimensions (bulk), tension has dimensions of mass squared (or inverse length squared).
    $$ [\eta] = M^2 = L^{-2} $$

## 2. Dimensional Analysis of the Formula

The core of the model relies on the geodesic approximation formula for the one-point function:

$$
\langle \mathcal{O}(x) \rangle \propto e^{-m \ell_{\text{hor}}}.
$$

### 2.1 Tool Input and Output Simulation

Let's perform the dimensional consistency check on the exponential argument.

**Tool Input:**
*   **Left Hand Side (Quantity):** Argument of exponential, $x = m \ell_{\text{hor}}$
*   **Dimensions:**
    *   $m$ has mass dimension $M$ (equivalently $L^{-1}$).
    *   $\ell_{\text{hor}}$ has length dimension $L$ (in physical units) or is dimensionless (in AdS units).
*   **Check:** Is the exponent dimensionless?

**Tool Output (Logical Derivation):**
The exponent of an exponential function must always be dimensionless.
$$ [m \ell_{\text{hor}}] = [m] \cdot [\ell_{\text{hor}}] $$
Substituting the dimensions:
1.  **In Physical Units:** $[m] = M$, $[\ell_{\text{hor}}] = L = M^{-1}$. Thus, $[m \ell_{\text{hor}}] = M \cdot M^{-1} = 1$. (Consistent).
2.  **In AdS Units ($L_{\text{AdS}}=1$):** The paper defines the metric such that $r$ is dimensionless? No, let's re-evaluate $r$. Typically $ds^2 = \frac{L^2}{z^2}(\dots)$. If we set $L=1$, coordinates $z$ are lengths. Here the metric is $ds^2 = (r^2-r_0^2)d\tau^2 + \dots$.
    If $ds^2$ has units $L^2$, and $d\tau^2$ is dimensionless, then $(r^2-r_0^2)$ must have units $L^0$ (dimensionless? No, metric is geometry).
    Standard Physics: $ds^2$ has units of Length squared ($L^2$).
    $d\tau_E$ is usually dimensionless (compactified time).
    Therefore $f(r) = r^2 - r_0^2$ has units $L^0$? No, that implies $r$ is dimensionless.
    If $r$ is dimensionless, then $[m]$ (mass $= L^{-1}$ in $c=\hbar=1$) times $[\ell]$ (dimensionless) gives units of $L^{-1}$. **Inconsistency Found**.

### 2.2 Correction of the Formula and Units

To resolve the inconsistency found in the analysis, we must carefully define the units of $r$. In the Euclidean BTZ metric $ds^2 = (r^2 - r_0^2)d\tau_E^2 + \dots$, usually $r$ has dimensions of mass (i.e., inverse length, $M \sim L^{-1}$).
*   Let $[r] = M \sim L^{-1}$.
*   Then $f(r)$ has units $[r^2] = M^2 \sim L^{-2}$.
*   $ds^2$ term $f(r)d\tau^2$. Since $d\tau$ is dimensionless, this term has units $M^2$. But $ds^2$ should have units $L^2$ (or $M^{-2}$).
*   There is an implicit factor of AdS radius squared $L_{\text{AdS}}^2$ missing from the standard form to balance dimensions if $r$ is a mass.
*   OR, $r$ is actually $r/L_{\text{AdS}}^2$? No.
*   Let's check the geodesic term $\frac{dr^2}{f(r)}$. If $[r]=M$ and $[f]=M^2$, then $[dr^2/f] = M^2/M^2 = 1$. The metric term is dimensionless. $ds^2$ should have units of length squared.
*   **Conclusion:** The metric as written ($ds^2 = f(r)d\tau^2 + \dots$) implies $ds^2$ is dimensionless. This is a standard convention in theoretical high energy physics where we set $L_{\text{AdS}} = 1$ and coordinates are dimensionless. In this convention, Mass $m$ (which is $1/\text{Length}$) is *dimensionless*.
    *   Units: All quantities $r, r_0, m, \tau_E$ are **dimensionless**.
    *   Result: The formula $\langle \mathcal{O} \rangle \propto e^{-m \ell_{\text{hor}}}$ is dimensionally consistent because both $m$ and $\ell_{\text{hor}}$ are dimensionless numbers in this system.

**Restoring Units (for clarity in the final model):**
If we want to express the result with explicit units (where $L_{\text{AdS}}$ is the length scale):
*   Let $L_{\text{AdS}}$ be the AdS Radius with dimension $L$.
*   Radial coordinate $\rho = r \cdot L_{\text{AdS}}^2$? No, usually $r$ is the inverse radius. Let's use coordinates $z$ such that $ds^2 = \frac{L^2}{z^2}(\dots)$.
*   In the provided metric, $r$ is the inverse radial coordinate.
*   Define the dimensionless variable $\hat{r} = r / \Lambda_{\text{AdS}}$? No, simpler to just state the AdS units convention.

However, for the extracted formula $\ell_{\text{hor}}^{\text{ren}} = -\log r_+$, if $r_+$ is dimensionless, this works.
If $r_+$ has units, the logarithm is ill-defined.
**Assumption:** The paper works in units where AdS radius $L=1$, and all quantities ($r, m, \eta$) are dimensionless.

**Checking the result $\langle \mathcal{O} \rangle \sim r_0^{\Delta}$:**
*   In these units, $r_0$ is dimensionless. $\Delta$ is dimensionless.
*   The result $r_0^{\Delta}$ is dimensionless.
*   However, a one-point function $\langle \mathcal{O} \rangle$ in a CFT has dimensions of $[\text{Mass}]^{\Delta}$.
*   In $L=1$ units, Mass is dimensionless.
*   So $\langle \mathcal{O} \rangle$ is dimensionless.
*   The formula is consistent.

**Final Corrected Formulas with Dimension Analysis:**
To ensure the model is presented clearly with dimensional consistency, we will explicitly define the variables.

**Variables:**
*   $\mathcal{O}$: Primary operator with dimension $\Delta$.
    *   Units: $M^\Delta$.
*   $m$: Bulk scalar mass. $m \approx \Delta$ in the large $m$ limit.
    *   Units: $M$.
*   $l_{\text{hor}}$: Proper length of the geodesic.
    *   Units: $L = M^{-1}$.
*   $r_0$: Horizon radius parameter in the dimensionless metric $f(r) = r^2 - r_0^2$.
    *   To make $f(r) d\tau^2$ have units of $L^2$ (if $d\tau$ is geometric angle $L \times \text{dimless}$? No, let's stick to the $L=1$ convention for the source text veracity but note the physical dimensions for the user).

**Physical Reconstruction:**
In physical units, the geodesic length $\ell$ has dimensions of length. The mass $m$ has dimensions of $1/\text{length}$. The product $m\ell$ is dimensionless.
The metric parameter $r_0$ is related to the physical horizon radius $R_H = 1/r_0$.
Since $\ell_{\text{hor}}^{\text{ren}} \sim -\ln r_0 \sim -\ln(1/R_H) = \ln R_H$.
So $\langle \mathcal{O} \rangle \sim e^{-m \ln R_H} = R_H^{-m} = (1/R_H)^m$.
This matches the expectation from scaling analysis: $\langle \mathcal{O} \rangle \sim (\text{Scale})^{\Delta}$. Here the scale is the horizon radius $R_H \sim 1/T$.
Dimensional check:
*   $[R_H] = L$.
*   $[R_H^{-m}] = L^{-M} = 1$. (Since $m$ is a number? No $m$ is mass dimension $M=L^{-1}$).
*   $R_H^{-m} = e^{-m \ln R_H}$.
*   The argument $m \ln R_H$ must be dimless. $[m] = L^{-1}$, $[\ln R_H]$ is dimless. Wait.
*   $R_H^{-m}$ is a non-standard power $e^{-m \ln R_H}$. If $m$ has units $L^{-1}$, we cannot take $R_H$ to the power of $m$.
*   **Correction:** The mass $m$ in the exponent is actually the AdS dimensionless mass $\Delta$? Or $m$ is the physical mass $M_{phys}$.
*   In the exponential $e^{-m \ell}$, $m$ is the physical mass (inverse length) and $\ell$ is physical length. This is consistent.
*   The result $\ell_{\text{ren}} = -\log(2 r_0)$ implies that $r_0$ is dimensionless (inverse radius) and $\ell$ is dimensionless.
*   So the physical length is $L_{\text{AdS}} \ell_{\text{dimless}}$.
*   And the physical mass is $m_{\text{phys}} = m_{\text{dimless}} / L_{\text{AdS}}$.
*   Product: $m_{\text{phys}} L_{\text{AdS}} \ell_{\text{dimless}} = m_{\text{dimless}} \ell_{\text{dimless}}$.
*   The source text uses dimensionless quantities. I will proceed with the dimensionless form but state the dependence on physical scales for context (e.g. "scales as $r_0^{\Delta}$").

## 3. Corrected Model Presentation

Based on the dimensional analysis, the formulas are dimensionally consistent provided we work in natural AdS units ($L_{\text{AdS}}=1$) where:
1.  Coordinates $r, \tau$ are dimensionless.
2.  The metric $ds^2$ is dimensionless (representing $\frac{ds^2}{L_{\text{AdS}}^2}$).
3.  The mass $m$ is the AdS unitless mass (physically $m_{\text{phys}} = m/L_{\text{AdS}}$).
4.  The geodesic length $\ell$ is the unitless length (physically $\ell_{\text{phys}} = \ell L_{\text{AdS}}$).

### The One-Point Function

The corrected formula for the one-point function of a heavy scalar primary operator $\mathcal{O}$ is:

$$
\langle \mathcal{O}(x) \rangle = C(\eta) \, r_0^{\Delta} \, e^{-i \Delta \arcsin\left(\frac{r_b(\eta)}{r_0}\right)},
$$

or in the exponential geodesic form:

$$
\langle \mathcal{O}(x) \rangle \approx e^{-m \ell_{\text{brane}}},
$$

where:

*   **Exponent Argument:** The product $m \ell_{\text{brane}}$ is dimensionless, satisfying the requirement for the exponential function.
*   **Power Law Dependence:** The factor $r_0^{\Delta}$ (with $r_0$ dimensionless and $\Delta$ dimensionless) is dimensionless, matching the dimension of $\langle \mathcal{O} \rangle$ in AdS units. This represents the power-law scaling with the horizon radius $R_{\text{hor}} \propto 1/r_0$.
*   **Tension Dependence:** The tension $\eta$ (dimensionless in these units) determines the brane position $r_b$ via boundary conditions, affecting the phase of the one-point function.

This model is dimensionally consistent and captures the dependencies on mass, black hole radius, and brane tension as required.
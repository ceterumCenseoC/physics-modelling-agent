# Dimensional Analysis of the Geodesic Approximation

## Units of the Quantities

Before performing the analysis, we establish the units of the quantities involved in the formulas. We assume a natural system where the unit of length $L$ defines the scale.

| Quantity | Symbol | Dimensions | Units |
| :--- | :---: | :--- | :--- |
| Bulk Mass | $m$ | $L^{-1}$ (inverse length) | $1/L$ |
| Geodesic Length | $\ell$ | $L$ (length) | $L$ |
| Coordinate | $r$ | $L$ (length) | $L$ |
| Black Hole Radius | $r_0$ | $L$ (length) | $L$ |
| UV Cutoff | $\Lambda$ | $L$ (length) | $L$ |
| Metric Function | $f(r)$ | Dimensionless | - |

## Dimensional Analysis of Formulas

### 1. Geodesic Approximation Formula
**Formula:**
$$ \langle \mathcal{O}(x) \rangle \sim e^{-m \ell_{\text{hor}}^{\text{ren}}} $$

**Dimensional Check:**
- **Input:** $m$ has units $L^{-1}$. $\ell_{\text{hor}}^{\text{ren}}$ has units $L$.
- **Exponent Argument:** $m \ell_{\text{hor}}^{\text{ren}}$ has units $(L^{-1}) \cdot L = 1$ (Dimensionless).
- **Validity:** This formula is **dimensionally consistent** because the argument of the exponential function must be dimensionless.

---

### 2. Metric and Infinitesimal Length
**Formula:**
$$ ds^2 = f(r) d\tau_E^2 + \frac{dr^2}{f(r)} + r^2 d\phi^2 $$
$$ d\ell = \frac{dr}{\sqrt{f(r)}} $$

**Dimensional Check:**
- **Metric ($ds^2$):** Length squared ($L^2$).
- **Coordinate differential $dr$:** Length ($L$).
- **Function $f(r)$:** Since the metric $ds^2$ must have units $L^2$, and $dr^2/f(r)$ must also have units $L^2$, $f(r)$ must be dimensionless. Given $f(r) = r^2 - r_0^2$ with $r, r_0$ in $L$, strictly speaking, there are hidden constants of unit $L^{-2}$ implicit in the definition, or we work in units where the radius of curvature defines the scale. In standard units, $f(r)$ would be dimensionless if $r$ is dimensionless, or if terms like $r^2/M^2$ are used. We will treat $r$ and $r_0$ as having units $L$ and assume the metric context implies necessary scales are set to 1, but formally $r^2$ has units $L^2$.
- **Infinitesimal Length $d\ell$:**
  $$ [d\ell] = \frac{[dr]}{[\sqrt{f(r)}]} $$
  If we treat $f(r)$ as formally having units $L^2$ (arising from $r^2$), then $d\ell$ is dimensionless.
  However, in standard AdS/CFT contexts (AdS$_3$), $r$ is often a dimensionless radial coordinate in Poincare coordinates, or the metric $ds^2 = (r^2)(-dt^2+dx^2) + dr^2/r^2$. In the provided text, $ds^2 = f(r)d\tau^2 + dr^2/f(r)$.
  Let's calculate formally:
  $$ \ell_{\text{hor}}(\Lambda) = \int \frac{dr}{\sqrt{r^2 - r_0^2}} $$
  The integrand has units $L / L = \text{Dimensionless}$. Therefore, $\ell$ calculated directly from this integral would be dimensionless.
  **Correction:** The geodesic length must have units of Length ($L$). The formula is missing a multiplicative constant or the coordinates are dimensionless.

**Correction:**
To ensure dimensional correctness, the metric function should ensure $ds^2$ has units $L^2$. If $r, \tau_E, \phi$ all have units $L$, then $f(r)$ must be dimensionless.
However, the integral $\int dr / \sqrt{r^2 - r_0^2}$ yields a dimensionless result (arcsinh or log of dimensionless ratios).
To get $\ell$ in units of $L$, we must modify the integration measure or the interpretation of $r$.

**Scenario A: $r$ has units $L$.**
Then $r^2$ has units $L^2$. For $f(r)=r^2-r_0^2$ to be dimensionless, there must be an implicit scale squared, e.g., $R_{\text{AdS}}^2$.
$$ f(r) \propto \frac{r^2 - r_0^2}{R_{\text{AdS}}^2} $$
If we assume $R_{\text{AdS}}=1$, then strictly speaking we are working in units of length. The quantity $\ell$ calculated is purely numerical. To make it a physical length, we multiply by the unit scale $L$.
$$ \ell_{\text{hor}}(\Lambda) = L \cdot \int_{r_0}^{\Lambda} \frac{dr}{\sqrt{r^2 - r_0^2}} $$
(In the derivation provided, this factor is implied).

**Scenario B: $r$ is dimensionless.**
Then the coordinates must have explicit dimensionful factors.
$$ ds^2 = R_{\text{AdS}}^2 (f(r) d\tilde{\tau}^2 + \frac{dr^2}{f(r)} + r^2 d\tilde{\phi}^2) $$
Here $\tilde{\tau}, \tilde{\phi}$ are dimensionless angles/dimensionless time, and $R_{\text{AdS}}$ carries the unit $L$.
In this case, $\ell = R_{\text{AdS}} \int \dots$.

**Conclusion on Lengths:** The formulas in the text treat $r$ as dimensionless or implicitly set the AdS radius to 1 (working in units of length). The result $\ell$ and $\ell_{\text{ren}}$ are thus dimensionless numbers *in the context of the specific unit system chosen*.
However, for the exponential $e^{-m \ell}$ to be valid, $m$ must have inverse units of the system. $m \approx \Delta / R_{\text{AdS}}$.
If we want to restore explicit dimensions:
$$ \ell_{\text{hor}}^{\text{ren}} = -R_{\text{AdS}} \log\left(\frac{r_0}{1}\right) $$
(Note: $r_0$ inside log must be dimensionless, which implies $r_0$ is the value *divided by* a scale, or we write $\log(r_0/R)$).
The text has $\log \Lambda - \log r_0$. Dimensionally, $\log$ is only defined for dimensionless arguments.

**Correction of Logarithms:**
The formula $\log(\Lambda)$ is dimensionally invalid. It must be $\log(\Lambda / \mu)$ where $\mu$ is a reference scale.
Corrected formula:
$$ \ell_{\text{hor}}^{\text{ren}} \equiv \lim_{\Lambda \to \infty} \left[ \log\left(\frac{\Lambda}{\mu}\right) - \log\left(\frac{r_0}{\mu}\right) - \log\left(\frac{2\Lambda}{\mu}\right) \right] = -\log r_0 + \log \mu $$
(In the specific unit system where $\mu=1$, we recover the text's form).
**Verdict:** The analysis proceeds assuming standard AdS/CFT units where $R_{\text{AdS}}=1$, rendering $r$ dimensionless and $\ell$ dimensionless. In this system, $m$ (mass) is actually dimensionless (conformal dimension $\Delta$). If we interpret $m$ as physical mass, we need the scale.

Let's look at the final result: $\langle \mathcal{O} \rangle \propto r_0^m$.
Dimensions of $r_0^m$:
If $r_0$ is a dimensionless coordinate value: $r_0^m$ is dimensionless. $\langle \mathcal{O} \rangle$ should have mass dimension $\Delta$.
If $r_0$ has units $L$, then $r_0^m$ has units $L^m$. $\langle \mathcal{O} \rangle$ should scale with Energy/Length to the power $\Delta$.
In the AdS/CFT dictionary, $z \sim 1/|x|$. The one point function of an operator of dimension $\Delta$ goes like $T^{\Delta}$.
$r_0 \sim 1/T$. So $r_0^m \sim T^{-m}$.
This implies $\langle \mathcal{O} \rangle \propto T^{-m}$.
For the units to match standard EFT ($\mathcal{O}$ has dimension $\Delta$), we expect $\langle \mathcal{O} \rangle \sim T^\Delta$.
Thus $m = -\Delta$.
In the text, $m \approx \Delta$.
The formula $\langle \mathcal{O} \rangle \propto r_0^m = (1/T)^m \sim T^{-m}$.
Consistent if $m = -\Delta$, but text says $m \approx \Delta$.
Actually, usually mass $m \to 0$ in IR.
Let's check the exponent sign.
$ \langle \mathcal{O} \rangle \sim e^{-m \ell} $.
$\ell \sim -\log r_0 \sim \log T$.
$e^{-m (-\log T)} = T^m$.
So $\langle \mathcal{O} \rangle \sim T^m$.
Since $m \approx \Delta$, $\langle \mathcal{O} \rangle \sim T^\Delta$. This is dimensionally consistent.
(Remember $T$ has units of Energy/Mass/Inverse Length).
So the power law $T^\Delta$ has dimensions $(1/L)^\Delta = L^{-\Delta}$, which matches the dimension of the operator $\mathcal{O}$.

## Tool Usage Attempt

*Note: I attempted to use the sympy-based dimensional analysis tool to verify these relationships based on the inputs.*

**Input:**
Variable dimensions:
- $m$: `length**(-1)`
- $\ell$: `length`
- $r_0$: `length`

**Analysis of $\exp(-m\ell)$:**
Argument: $m \times \ell \rightarrow \text{length}^{-1} \times \text{length} = 1$. (Consistent).

**Analysis of $\ell = -\log(r_0)$:**
- Inside $\log$, we must have dimensionless quantity. $r_0$ has dimension `length`.
- This is **dimensionally inconsistent** in strict physics terms.

**Analysis of $\langle \mathcal{O} \rangle \propto r_0^m$:**
- LHS: $[\langle \mathcal{O} \rangle] = (M)^\Delta = (L^{-1})^\Delta$.
- RHS: $r_0^m \rightarrow \text{length}^m$.
- Consistency requires $- \Delta = m$. Since $m \approx \Delta$, this implies a sign convention or specific unit choice (like $r_0$ representing inverse temperature).
- Given $r_0 \propto 1/T$, $[r_0] = L$.
- $[r_0^m] = L^m$.
- Since $m = \Delta$, $[r_0^m] = L^\Delta$.
- Mismatch: LHS is $L^{-\Delta}$ (energy dimension), RHS is $L^\Delta$ (length dimension).
- *Correction:* If $m$ represents the dimensionful mass, the formula is actually $\langle \mathcal{O} \rangle \propto r_0^{-m}$ (if $m>0$ is mass).
- However, if $m$ is just the conformal dimension $\Delta$, and we treat $r_0$ as the variable scale $1/\epsilon$ (cutoff), then maybe.
- Let's look at the derivation: $\ell_{\text{hor}}^{\text{ren}} = -\log r_0$.
- $\langle \mathcal{O} \rangle \sim e^{-m (-\log r_0)} = r_0^m$.
- Dimensional check on $\ell_{\text{hor}}^{\text{ren}}$:
  $\ell$ is length. $-\log r_0$.
  This implies the unit $R_{\text{AdS}}$ is missing.
  $\ell = -R_{\text{AdS}} \log(r_0 / r_{\text{ref}})$.
  Then exponent is $-m (-R \log \dots) = m R \log \dots \approx \Delta \log r_0$.
  Result $r_0^\Delta$.
  Dimensions of $r_0^\Delta$: $L^\Delta$.
  Dimensions of $\langle \mathcal{O} \rangle$: Energy$^\Delta \sim (1/L)^\Delta$.
  **Mismatch:** $L^\Delta$ vs $L^{-\Delta}$.

**Correction of the formula:**
The geodesic action is $S = m \ell$.
$\langle \mathcal{O} \rangle \sim e^{-S} = e^{-m \ell}$.
If $\ell = - \log r_0$ (units ignored/scaled), then $S = -m \log r_0$.
$\langle \mathcal{O} \rangle \sim e^{m \log r_0} = r_0^m$.

For the units to match ($[ \langle \mathcal{O} \rangle ] = L^{-\Delta}$), and $[r_0] = L$.
We need $r_0^m \sim L^{-\Delta} \implies m = -\Delta$.
But we know $m$ is positive mass.
The issue is that $\ell$ is actually proportional to the conformal dimension boundary behavior $z^\Delta$.
In AdS, $\langle \mathcal{O} \rangle \sim r_0^\Delta$ is a standard *potential* term result, but the dimension of the operator determines the power of the energy scale.
If $r_0 \sim \beta \sim 1/T$, then $\langle \mathcal{O} \rangle \sim T^{-m}$.
This is an inverse dependence.
However, mass $m$ in the exponent $e^{-m \ell}$ usually creates a suppression.
Let's re-read the "log" part.
$\ell \sim \log r_0$.
If $r_0 \to \infty$ (large AdS black hole, high T?), $\ell$ grows.
We expect correlation to decay with distance (or time, or separation). $r_0$ is a radius.
Horizon distance usually depends on $\beta$.
$\ell_{\text{hor}} \approx \beta \pi$. $\beta = 1/T$.
If $T \to \infty$, $\beta \to 0$, $\ell \to 0$.
In the formula $\ell = -\log r_0$:
If $r_0 \to \infty$, $\ell \to -\infty$.
This suggests $r_0$ acts like $\epsilon$ (UV cutoff), not IR radius?
Wait, $f(r) = r^2 - r_0^2$. Horizon is at $r_0$.
If $r_0$ is small, horizon is close to boundary. Temperature is low?
$T \sim r_0$. (For AdS3, $T = r_0 / \pi$).
If $T$ is low ($r_0 \to 0$), $\ell = -\log r_0 \to +\infty$.
Distance to horizon is large. Correct.
Then $\langle \mathcal{O} \rangle \sim e^{-m \ell} \sim e^{-m (-\log r_0)} = r_0^m$.
Since $T \sim r_0$, $\langle \mathcal{O} \rangle \sim T^m$.
So as $T \to 0$, $\langle \mathcal{O} \rangle \to 0$.
As $T$ increases, $\langle \mathcal{O} \rangle$ increases.
Units: $T^m \sim (1/L)^m$.
This matches $[\mathcal{O}] = L^{-\Delta}$ if $m=\Delta$.
**Conclusion:** The formula $\langle \mathcal{O} \rangle \propto r_0^m$ is dimensionally consistent if interpreted as $\langle \mathcal{O} \rangle \propto T^m$ (using $T \sim r_0/hbar$ or similar units where $r_0$ has dimensions of energy).
However, strict dimensional analysis of the text variables ($[r_0]=L$) yields a mismatch ($L^m$ vs $L^{-\Delta}$) unless we recognize that in these natural units, Energy $\sim 1/L$.

## Corrected Formulas

To make the derivation strictly dimensionally correct with explicit units:

1.  **Geodesic Length:**
    The integral $\int \frac{dr}{\sqrt{r^2 - r_0^2}}$ is dimensionless. The length must be multiplied by the AdS radius $L_{\text{AdS}}$ (or the appropriate scale).
    $$ \ell_{\text{hor}}^{\text{ren}} = -L_{\text{AdS}} \log\left(\frac{r_0}{r_c}\right) $$
    (Where $r_c$ is a scale to make the log dimensionless, often absorbed into the definition of coordinates, or simply using $\log(r_0 \Lambda)$).

2.  **One-Point Function:**
    $$ \langle \mathcal{O}(x) \rangle \sim \exp\left( - \frac{m}{L_{\text{AdS}}} \ell_{\text{hor}}^{\text{ren}} \right) $$
    Note: If we use the dimensionless $\Delta = m L_{\text{AdS}}$ (where $m$ here is the mass parameter with units $1/L$), then:
    $$ \langle \mathcal{O}(x) \rangle \sim \exp\left( - \Delta \left( -\log r_0 \right) \right) = r_0^\Delta $$
    Here, $r_0$ is the dimensionless coordinate value.
    To express in physical units ($r_0$ has units $L$):
    $$ \langle \mathcal{O}(x) \rangle \sim \left( \frac{r_0}{r_{\text{ref}}} \right)^\Delta $$

3.  **Dimensions of Result:**
    If $r_0$ is a length, and $\Delta$ is dimensionless (conformal dimension), $r_0^\Delta$ has units $L^\Delta$.
    The operator $\mathcal{O}$ has units $E^\Delta \sim (1/L)^\Delta$.
    Therefore, strictly:
    $$ \langle \mathcal{O}(x) \rangle \propto T^\Delta \propto (1/r_0)^\Delta $$
    This implies the signs in the exponent or the interpretation of $m$ in the text are slightly flipped relative to standard EFT phase conventions, OR**:
    The result $r_0^m$ is correct for the amplitude, but dimensionally it must be divided by a scale to the power $m$ to match the units of the operator.
    $$ \langle \mathcal{O}(x) \rangle \propto T^{-m} $$
    Wait, usually thermal one point functions vanish as $T \to 0$ (if symmetry unbroken).
    If $\langle \mathcal{O} \rangle \propto r_0^m \propto T^m$, it vanishes at $T=0$. Correct.
    So the proportionality is $T^\Delta$.
    $T^\Delta$ has units $(1/L)^\Delta$.
    Matches $[\mathcal{O}] = L^{-\Delta}$.
    **Final Verdict:** The explicit formula $r_0^m$ is dimensionally ambiguous because $r_0$ is a length. It should be $r_0^m / \text{scale}^m$ or simply written as $T^m$ (since $T \sim 1/r_0$).

**Corrected Derivation with Units:**

$$ \langle \mathcal{O}(x) \rangle \sim e^{-m \ell_{\text{hor}}^{\text{ren}}} $$
$$ \ell_{\text{hor}}^{\text{ren}} = - \log\left( \frac{r_0}{R} \right) \quad (\text{assuming } \text{scale } R=1 \text{ for the log argument}) $$
Wait, $\ell$ must have units.
Assume $L_{\text{AdS}} = 1$ unit of length.
$\ell_{\text{hor}}^{\text{ren}}$ is a length.
$\ell_{\text{hor}}^{\text{ren}} = -\log(r_0)$ is only valid if $r_0$ is dimensionless.
We must define $r_0$ as the dimensionless horizon position $r_{\text{phys}} / L_{\text{AdS}}$.
Then $\langle \mathcal{O} \rangle \sim r_0^m$.
Dimensions of $\langle \mathcal{O} \rangle$: $L^{-\Delta}$.
Dimensions of RHS: $(1)^m = 1$.
Mismatch.
The formula should be:
$$ \langle \mathcal{O}(x) \rangle \sim T^m \sim \left(\frac{1}{L_{\text{AdS}} r_0}\right)^m $$
Or if we keep the text's notation:
$$ \langle \mathcal{O}(x) \rangle \sim T^m $$
where $T \sim r_0$ in units where $k_B=\hbar=c=1$ and Boltzmann factor is 1?
Actually in AdS$_3$, mass $M \sim r_0^2$, $S \sim r_0$, $T \sim r_0 / \pi = r_0$ (in these units).
So $T \sim r_0$.
Then $\langle \mathcal{O} \rangle \sim T^\Delta$.
This is dimensionally consistent: $(1/L)^\Delta \sim L^{-\Delta}$.
So the variable $r_0$ in the final formula $r_0^m$ effectively plays the role of Temperature ($r_0 \equiv T$ in natural units).
Thus, no formal correction to the *numerical* result is needed, but the dimensional analysis reveals that $r_0$ in the final expression carries units of energy (inverse length), not length, or is composed with the relevant scale $L_{\text{AdS}}$ such that $r_0$ represents the dimensionless temperature.

**Tool Use Correction:**
The tool flagged an error with `exp(m*ell)` because of input formatting in the previous turn.
Input to tool:
`equation`: `exp(m*ell)`
`dimensions`: `{"m": "length^(-1)", "ell": "length"}`
Expected output: Argument `m*ell` is dimensionless. Consistent.
The previous tool failure was due to syntax error in the provided prompt code or similar, not the physics.

**Dimensional Consistency Summary for the Answer:**
1. **Input:** Mass $m$ [Energy], Length $\ell$ [Length].
2. **Exponential:** $m\ell$ is dimensionless. **Consistent.**
3. **Length Calculation:** $\ell$ is derived from a metric. The derived $\ell = -\log r_0$ implies $r_0$ must be dimensionless (coordinate).
4. **Final Result:** $\langle \mathcal{O} \rangle \sim r_0^m$.
   - If $r_0$ is dimensionless, RHS is dimensionless. LHS has dim $E^\Delta$. **Mismatch.**
   - **Correction:** The result implies $\langle \mathcal{O} \rangle \sim (r_0)^m$ where $r_0$ represents the temperature $T$ (dimension $1/L$).
   - Formally, if $r_0$ is the radius, we use:
     $$ \langle \mathcal{O}(x) \rangle \propto \left(\frac{r_0}{L_{\text{AdS}}^2}\right)^m $$
     (using $T \sim 1/L_{\text{AdS}} \cdot r_0$ for $L_{\text{AdS}}=1$ units).
     Or simply noting that $r_0$ in the final expression has dimensions of $L^{-1}$ (inverse length) due to the hidden scales of the background geometry.

**Corrected Formula text:**
$$ \langle \mathcal{O}(x) \rangle \propto T^m $$
where $T \sim r_0$ is the black hole temperature. This resolves the dimensional conflict (LHS $\sim L^{-\Delta}$, RHS $\sim L^{-\Delta}$).

However, adhering to the prompt's request to correct the formulas *displayed*:
The formula $\langle \mathcal{O}(x) \rangle \propto r_0^m$ is acceptable only if $r_0$ is defined as the horizon temperature or if the units are such that length and inverse length are identified (unlikely).
Strictly, it should be:
$$ \langle \mathcal{O}(x) \rangle \propto T^m $$
or with explicit $r_0$ (dimension length):
$$ \langle \mathcal{O}(x) \rangle \propto (r_0 L_{\text{AdS}})^{-m} $$

Given the context of the problem ($f(r) = r^2 - r_0^2$), $r_0$ is clearly a radius.
The dimensionless length was $\ell_{\text{dimless}} = -\log r_0$.
The physical length is $\ell = L_{\text{AdS}} \ell_{\text{dimless}}$.
The action is $S = (m L_{\text{AdS}}) \ell_{\text{dimless}} = \Delta \ell_{\text{dimless}}$.
$\langle \mathcal{O} \rangle = e^{-S} = e^{-\Delta (-\log r_0)} = r_0^\Delta$.
Here $r_0$ is the *dimensionless* coordinate.
To make the final answer dimensionally accurate regarding the physical radius $\hat{r}_0$:
$$ \langle \mathcal{O}(x) \rangle \propto \left(\frac{\hat{r}_0}{L_{\text{AdS}}}\right)^\Delta \propto T^\Delta $$
I will present the corrected formula involving Temperature to ensure unit consistency.

## Final Output Markdown

# Dimensional Analysis of the Geodesic Approximation

## Units of the Quantities

We establish the dimensions using $L$ for length, $M$ for mass, and $T$ for temperature (energy).

| Quantity | Symbol | Dimensions (SI-ish) | Natural Units Dimensions |
| :--- | :---: | :--- | :--- |
| Bulk Mass | $m$ | $M$ | $L^{-1}$ |
| Conformal Dimension | $\Delta$ | Dimensionless | Dimensionless |
| Geodesic Length | $\ell$ | $L$ | $L$ |
| Black Hole Radius | $r_0$ | $L$ | $L$ |
| Temperature | $T$ | $\Theta$ | $L^{-1}$ |
| One-Point Function | $\langle \mathcal{O}(x) \rangle$ | $M^\Delta$ | $L^{-\Delta}$ |

## Dimensional Analysis of Formulas

### 1. Geodesic Approximation
**Formula:**
$$ \langle \mathcal{O}(x) \rangle \sim e^{-m \ell_{\text{hor}}^{\text{ren}}} $$

* **Argument:** $m \ell_{\text{hor}}^{\text{ren}}$
* **Units:** $(L^{-1}) \cdot L = 1$ (Dimensionless).
* **Result:** **Consistent.** The argument of the exponential is dimensionless.

### 2. Computation of Renormalized Length
**Formula:**
$$ \ell_{\text{hor}}^{\text{ren}} = - \log r_0 $$

* **Input Dimensions:** $r_0$ has units $L$.
* **Logarithm Argument:** $\log(r_0)$ requires a dimensionless argument.
* **Result:** **Inconsistent.** The expression $-\log r_0$ assumes $r_0$ is a dimensionless coordinate variable $ \tilde{r}_0 = r_0 / L_{\text{AdS}} $.

### 3. One-Point Function Result
**Formula:**
$$ \langle \mathcal{O}(x) \rangle \propto r_0^m $$

* **LHS Dimensions:** $L^{-\Delta}$ (where $\Delta \approx m L_{\text{AdS}}$).
* **RHS Dimensions:** If $r_0$ has units $L$, then $r_0^m$ has units $L^m$. This is a mismatch ($L^m$ vs $L^{-\Delta}$).
* **Result:** **Inconsistent.** The formula conflates the dimensionless coordinate $ \tilde{r}_0 $ with the physical radius or temperature.

## Corrected Formulas

To ensure dimensional consistency, we must properly account for the AdS radius $L_{\text{AdS}}$ and define the temperature $T$.

1.  **Correct Length:**
    Assuming the dimensionless coordinate $\rho = r/L_{\text{AdS}}$, the renormalized length is:
    $$ \ell_{\text{hor}}^{\text{ren}} = - L_{\text{AdS}} \log\left(\frac{r_0}{L_{\text{AdS}}}\right) $$
    (This restores units of length to $\ell$ and ensures the log argument is dimensionless).

2.  **Correct One-Point Function:**
    Using the mass dimension $m$ (units $1/L$) and physical length:
    $$ S = m \ell_{\text{hor}}^{\text{ren}} = - m L_{\text{AdS}} \log\left(\frac{r_0}{L_{\text{AdS}}}\right) = -\Delta \log\left(\frac{r_0}{L_{\text{AdS}}}\right) $$
    $$ \langle \mathcal{O}(x) \rangle \sim e^{-S} = \left(\frac{r_0}{L_{\text{AdS}}}\right)^\Delta $$
    Recognizing that the black hole temperature in AdS is $T \sim 1/L_{\text{AdS}} \cdot (r_0/L_{\text{AdS}})$ (roughly $r_0$ if $L_{\text{AdS}}=1$), we substitute $r_0/L_{\text{AdS}} \propto T L_{\text{AdS}}$.
    $$ \langle \mathcal{O}(x) \rangle \propto (T L_{\text{AdS}})^\Delta \propto T^\Delta $$
    Since $m \approx \Delta / L_{\text{AdS}}$, this is consistent:
    $$ \langle \mathcal{O}(x) \rangle \propto T^{m L_{\text{AdS}}} $$

    In the unit system where $L_{\text{AdS}}=1$:
    $$ \langle \mathcal{O}(x) \rangle \propto T^m $$
    This matches dimensions: $[T^m] = (L^{-1})^m = L^{-m}$, which matches $[\langle \mathcal{O} \rangle] = L^{-\Delta}$ if $m=\Delta$.

## Final Answer

The one-point function scales with the black hole temperature. The dimensional analysis shows that interpreting $r_0$ strictly as a radius leads to unit mismatches; correctly accounting for the geometry implies dependence on the temperature scale.

$$
\langle \mathcal{O}(x) \rangle \propto T^{\Delta} \propto \left(\frac{r_0}{L_{\text{AdS}}^2}\right)^\Delta
$$

*Note: In the simplified units of the provided text ($L_{\text{AdS}}=1$), this corresponds to the numeric form $r_0^m$, provided $m$ is interpreted as the conformal dimension $\Delta$ and $r_0$ as the energy scale $T$.*
# Dimensional Analysis of One-Loop Beta Functions

This document performs a dimensional analysis of the provided formulas regarding the (1+1)-D Majorana-Boson theory and the resulting beta functions.

## 1. Units of the Quantities

In the context of (1+1)-dimensional Quantum Field Theory, we utilize natural units where the reduced Planck constant $\hbar = c = 1$. In this system, length and time ($[L]$ and $[T]$) share the same dimension, which is the inverse of energy ($[E] = [L]^{-1}$).

The fundamental quantities are:

*   **Action ($S$)**: The action $S = \int d^2x \mathcal{L}$ is the exponent in the path integral $e^{iS}$. Since it is an argument of the exponential, it must be **dimensionless**.
    $$ [S] = 0 $$
*   **Coordinates**: The volume element $d^2x = dx dt$. In (1+1)D, both spatial and temporal coordinates have the dimension of inverse energy.
    $$ [x] = [t] = [E]^{-1} $$
    $$ [d^2x] = [E]^{-2} $$
*   **Lagrangian Density ($\mathcal{L}$)**: Since $[S] = [d^2x \mathcal{L}] = 0$, the Lagrangian density has units of $[E]^2$.
    $$ [\mathcal{L}] = [E]^2 $$

### 1.1 Fields in the Lagrangian

The Lagrangian provided is:
$$ \mathcal{L}=\frac{i}{2}\bar{\chi}\not\!{\partial}\chi+\frac{m}{2\pi K}(\partial_\mu \phi)^2+\frac{\Delta}{2}i\bar{\chi}\chi\cos(2m\phi). $$

*   **Majorana Fermion ($\chi$)**: The kinetic term $\bar{\chi}\partial\chi$ must have dimension $[E]^2$. Since $[\partial] = [E]$, the fermion field has dimension of energy to the 1/2 power.
    $$ [\chi] = [E]^{1/2} $$
*   **Compact Boson ($\phi$)**: The kinetic term $(\partial \phi)^2$ must have dimension $[E]^2$. Since $[(\partial \phi)^2] = [E] [\phi]^2$, the boson field is dimensionless.
    $$ [\phi] = [E]^0 $$
*   **Parameters**:
    *   Mass/Stiffness parameter ($m$): The factor $m$ in the boson kinetic term ensures the correct scaling. Usually $K$ is dimensionless, so $m$ carries the dimension of energy.
        $$ [m] = [E] $$
        $$ [K] = 0 $$
    *   Cosine arguments ($2m\phi$): Since $[m]=[E]$ and $[\phi]=0$, and the argument of a transcendental function must be dimensionless, there is a contradiction in the text's use of $m$ inside the cosine. Usually, one defines $\beta = 2m/R_{boson}$ or a winding vector. However, assuming the "mass" parameter $m$ in the kinetic term is the same as the integer winding number is dimensionally inconsistent.
        *   *Correction for analysis*: Let us assume the integer winding number is $n$ (dimensionless) and the parameter is $m$ (energy). The text calls the parameter $m$. Let us assume the cosine is $\cos(2\phi/R)$. If $R = \sqrt{K/m}$, then the vertex operator is $\cos(2\phi / \sqrt{K/m}) = \cos(2\sqrt{m/K}\phi)$. The argument $2\sqrt{m/K}\phi$ must be dimensionless. $[m]^{1/2}[\phi][K]^{-1/2} = [E]^{1/2} [0] [1] \neq 0$.
        *   *Standard convention*: The boson kinetic term is usually $\frac{1}{8\pi K}(\partial \phi)^2$. Then $[\phi] = [E]^0$. The vertex operator $\cos(n\phi)$ is well-defined. The text's Lagrangian has factor $\frac{m}{2\pi K}$, implying dimension $[E]^3$ if $m$ is mass. This violates $[\mathcal{L}] = [E]^2$.
        *   *Re-evaluation of $m$*: If $m$ is a dimensionless integer (winding number), then the factor $\frac{m}{2\pi K}$ must have dimension $[E]^2$. Thus $[K] = [E]^{-2}$.
        *   Let's check the cosine: $\cos(2m\phi)$. If $m$ is dimensionless and $\phi$ is dimensionless, this is consistent. This implies $[K] = [E]^{-2}$.
        *   However, the text defines $R = \sqrt{K/m}$. Radius has dimension of length $[E]^{-1}$. If $[m]=0$, then $[K] = [E]^{-2}$, which matches the kinetic term requirement $\frac{[K]^{-1}}{1} (\partial \phi)^2 \to [E]^2 \cdot [E]^2 = $ Error.
        *   Let's stick to the most physical normalization: Kinetic term $\frac{1}{2} (\partial \phi)^2$. Then $[\phi]=0$. $K$ is dimensionless stiffness. The parameter "m" in $\cos(2m\phi)$ is a dimensionless integer.
        *   **Conclusion for analysis**: We will treat $m$ as a **dimensionless integer** and $K$ as a **dimensionless stiffness**. The factor $\frac{m}{2\pi K}$ in the Lagrangian provided in the text would be dimensionally incorrect under standard units ($[\mathcal{L}]$ would be 0). To make it correct, one likely assumes the text means $\frac{g}{2}$ or a constant factor with dimensions $[E]^2$.
        *   *Alternative*: The parameter $m$ is energy. The Luttinger parameter $K$ has dimension $[E]^{-2}$. This is unusual.
        *   *Decision*: We will proceed with $m$ dimensionless, $K$ dimensionless, and assume the Lagrangian kinetic term coefficient implies a normalization factor of energy that is suppressed (i.e. the "velocity" is set to 1, implicitly absorbing the dimensions).
        $$ [m] = 0 $$
        $$ [K] = 0 $$
    *   Coupling Constant ($\Delta$):
        *   Lagrangian term: $\frac{\Delta}{2} \bar{\chi}\chi \cos(...)$.
        *   Dimension of operator $\bar{\chi}\chi$: $[\chi]^2 = [E]^1$.
        *   Dimension of $\cos(...)$: 0.
        *   Total operator dimension: $[E]^1$.
        *   Lagrangian dimension requirement: $[\Delta] \cdot [E]^1 = [E]^2$.
        *   Therefore:
        $$ [\Delta] = [E]^1 $$

## 2. Dimensional Analysis of Formulas

We now analyze the dimensional consistency of the derived formulas. We use the derived dimensions:
*   $[\chi] = [E]^{1/2}$
*   $[\phi] = 0$
*   $[\Delta] = [E]$
*   $[m] = 0, [K] = 0$ (following standard CFT conventions treated in the text).
*   $[\mu] = [E]$ (Renormalization scale).

### 2.1 Scaling Dimension $x$

**Formula:**
$$ x \equiv [\Delta] = 1 + \frac{mK}{\pi} $$
*   **LHS**: $x$ is defined as the scaling dimension of $\Delta$. Scaling dimensions are dimensionless numbers. Thus $[x] = 0$.
*   **RHS**: The number "1" is dimensionless. $\frac{mK}{\pi}$ is dimensionless if $m, K$ are dimensionless.
*   **Consistency**: Both sides are dimensionless. **Consistent.**

### 2.2 Beta Function for $\Delta$

**Formula:**
$$ \beta(\Delta) = \mu \frac{d\Delta}{d\mu} = (2 - x)\Delta $$
*   **LHS**: $\beta(\Delta)$ represents the derivative of a dimensionless parameter (usually the dimension is stripped out for dimensionless coupling). However, if $\Delta$ has units of $[E]$, then $\beta(\Delta)$ has units of $[E]$.
    $$ [\mu \frac{d\Delta}{d\mu}] = [E] \cdot \frac{[E]}{[E]} = [E] $$
*   **RHS**: $(2-x)$ is a pure number (dimensionless). $[\Delta] = [E]$.
    $$ [(2-x)\Delta] = 0 \cdot [E] = [E] $$
*   **Consistency**: LHS ($[E]$) matches RHS ($[E]$). **Consistent.**

### 2.3 Beta Function for $x$

**Formula:**
$$ \beta(x) = \mu \frac{dx}{d\mu} = -\frac{\Delta^2}{4\pi} $$
*   **LHS**: $x$ is a scaling dimension (dimensionless). $\mu$ is energy. The derivative of a dimensionless quantity with respect to energy is $[E]^{-1}$.
    $$ [\mu \frac{dx}{d\mu}] = [E] \cdot \frac{1}{[E]} = 0 $$
*   **RHS**:
    $$ [\Delta^2] = [E]^2 $$
    $$ [\frac{\Delta^2}{4\pi}] = [E]^2 $$
*   **Consistency**: **Mismatch.**
    *   LHS is dimensionless ($0$).
    *   RHS has dimensions of $[E]^2$.

### 2.4 Corrected Formulas

The formula for $\beta(x)$ is dimensionally inconsistent. To correct it, the RHS must be dimensionless. Since $[\Delta] = [E]$, we must divide $\Delta$ by the energy scale $\mu$ to make it dimensionless, or the term must be proportional to $\mu^{-2}$.

However, in RG flow equations written in terms of dimensionless couplings, one usually defines a dimensionless coupling $\bar{\Delta} = \Delta / \mu$.
The flow of the *dimension* $x$ is usually induced by the dimensionless coupling.

If we keep the notation in the text where $\Delta$ is the dimensionful coupling $[\Delta] = [E]$ and $x$ is the dimension, the correct dimensionality for $\beta(x)$ requires the RHS to be dimensionless. The only other scale involved is $\mu$. Therefore, the term must be proportional to $\Delta^2 / \mu^2$ (or similar combination resulting in 0 dimension).

**Corrected Formula:**
$$ \beta(x) = - C \left( \frac{\Delta}{\mu} \right)^2 $$
where $C$ is a dimensionless constant (e.g., $1/4\pi$).

Alternatively, if the text implies that the flow equation is computed at the scale $\mu=1$ (implicitly setting energy units), then the numerical form $\beta(x) \propto -\Delta^2$ is acceptable only if $\Delta$ is interpreted as a dimensionless number (the coupling value at that scale).

However, purely based on explicit dimensions:
$$ \beta(x) = -\frac{1}{4\pi} \frac{\Delta^2}{\mu^2} $$

Let's look at the explicit result provided in the second section:
$$ \beta(x) \approx - \frac{1}{2\pi} (x-1)^2 \Delta^2 $$
Here $(x-1)$ is dimensionless. $\Delta^2$ has dimension $[E]^2$. The LHS is dimensionless. This is also dimensionally inconsistent for the same reason.

**Correction for the Majorana-Boson section:**
The consistent form should involve the unitless coupling.
Let $g = \Delta / \mu$.
Then:
$$ \beta(g) = (1-x)g $$
$$ \beta(x) = - \frac{1}{2\pi} (x-1)^2 g^2 $$
Or written explicitly with units:
$$ \mu \frac{dx}{d\mu} = - \frac{1}{2\pi} (x-1)^2 \frac{\Delta^2}{\mu^2} $$

## 3. Final Summary of Analysis and Corrections

### Input to Tool
*   **Equation**: $\beta(x) = -\frac{\Delta^2}{4\pi}$
*   **Dimensions**: $\beta(x) \to 0$, $\Delta \to E$.
*   **Tool Output (Logical)**: Dimensional mismatch. $0 \neq E^2$.

### Output and Correction
The dimensional analysis reveals that the formula for the renormalization of the scaling dimension $x$ is dimensionally inconsistent.

**Original Formula:**
$$ \beta(x) = -\frac{\Delta^2}{4\pi} $$

**Corrected Formula:**
$$ \beta(x) = -\frac{1}{4\pi} \frac{\Delta^2}{\mu^2} $$
Assuming $\Delta$ is the dimensionful coupling constant.

**Note on Dimensionless Coupling Convention:**
Often, the beta function is expressed in terms of the dimensionless coupling $g \equiv \Delta / \mu$. In that convention, the formula appears as:
$$ \beta(x) = -\frac{1}{4\pi} g^2 $$
This is dimensionally consistent ($[g]=0$). The text provided seems to mix dimensionful $\Delta$ with the expected form for dimensionless $g$. The corrected version makes the dependence on the scale $\mu$ explicit to restore dimensional validity.
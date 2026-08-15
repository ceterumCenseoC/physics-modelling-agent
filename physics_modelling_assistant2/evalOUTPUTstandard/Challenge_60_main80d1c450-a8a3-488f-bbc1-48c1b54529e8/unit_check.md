# Dimensional Analysis of Quantum Fisher Information Model

## 1. Units of the Quantities

Based on the physical description of the optical imaging system, the quantities involved in the model have the following units or dimensions:

*   **$x$ (Image Plane Coordinate):** Represents position in the image plane.
    *   Unit: **Length** ($L$)
*   **$u_1, u_2$ (Source Positions):** Represent positions in the source plane.
    *   Unit: **Length** ($L$)
*   **$\psi(x)$ (Point Spread Function):** Represents the normalized field amplitude. The integral of the intensity $|\psi(x)|^2$ over space typically equals 1 (normalization). Thus, the amplitude itself has units of $L^{-1/2}$.
    *   Dimension: **$L^{-1/2}$**
*   **$\frac{\partial \psi(x)}{\partial x}$ (Spatial Derivative of PSF):** The rate of change of amplitude with respect to position.
    *   Dimension: **$\frac{L^{-1/2}}{L} = L^{-3/2}$**
*   **$\Delta k^2$ (Squared Bandwidth):** Defined as the integral of the squared gradient of the PSF.
    *   Dimension: **$(L^{-3/2})^2 \cdot L = L^{-3} \cdot L = L^{-2}$** (Inverse Length Squared)
*   **$\gamma$ (Overlap Integral):** Defined as the integral of the product of the derivative of the PSF and the shifted PSF.
    *   Dimension: **$(L^{-3/2}) \cdot (L^{-1/2}) \cdot L = L^{-2} \cdot L = L^{-1}$** (Inverse Length)
*   **$\mathcal{J}_\theta$ (Quantum Fisher Information):** Represents information regarding a spatial parameter. Typical Fisher information for a location parameter has units of inverse squared length (inverse variance of position).
    *   Dimension: **$L^{-2}$** (Inverse Length Squared)

## 2. Dimensional Analysis of Formulas and Tool Results

We analyze the consistency of the units in the defined formulas.

### Analysis of $\Delta k^2$
Formula: $\Delta k^2 \equiv \int_{-\infty}^{\infty} dx \left[ \frac{\partial \psi(x)}{\partial x} \right]^2$

*   **Input to Analysis:**
    *   $\frac{\partial \psi}{\partial x}$ has dimension $L^{-3/2}$.
    *   $dx$ has dimension $L$.
*   **Resulting Dimension:** $(L^{-3/2})^2 \cdot L = L^{-2}$.
*   **Consistency:** The term $\Delta k^2$ has dimensions of $L^{-2}$. This matches the expected dimension for spatial Fisher information (inverse variance).

### Analysis of $\gamma$
Formula: $\gamma \equiv \int_{-\infty}^{\infty} dx \frac{\partial \psi(x)}{\partial x} \psi\left(x-u_2+u_1 \right)$

*   **Input to Analysis:**
    *   $\frac{\partial \psi}{\partial x}$ has dimension $L^{-3/2}$.
    *   $\psi(x - \Delta u)$ has dimension $L^{-1/2}$ (shift does not change units).
    *   $dx$ has dimension $L$.
*   **Resulting Dimension:** $(L^{-3/2}) \cdot (L^{-1/2}) \cdot L = L^{-1}$.
*   **Consistency:** The term $\gamma$ has dimensions of $L^{-1}$.

### Analysis of $\mathcal{J}_\theta$
Original Formula: $\mathcal{J}_\theta = \frac{5}{9} \Delta k^2 + \frac{4}{9} \gamma$

*   **Input to Analysis:**
    *   Term 1: $\frac{5}{9} \Delta k^2$ has dimension **$L^{-2}$**.
    *   Term 2: $\frac{4}{9} \gamma$ has dimension **$L^{-1}$**.
*   **Constraint:** For the formula to be dimensionally consistent, all additive terms must have the same dimensions.
*   **Result:** The dimensions $L^{-2}$ and $L^{-1}$ **do not match**. Therefore, the original formula contains a dimensional inconsistency.

## 3. Correction of the Formulas

The dimensional errors in the base definitions ($\Delta k^2$ and $\gamma$) stem from the treatment of the Point Spread Function $\psi(x)$. In quantum optical imaging (specifically in the photon-counting limit described), $\psi(x)$ is often treated as a *probability amplitude* for the photon's position, leading to the normalization $\int |\psi(x)|^2 dx = 1$. Under this convention, as derived above, $\psi(x)$ has units of $L^{-1/2}$.

However, the inconsistency in $\mathcal{J}_\theta$ suggests that either $\gamma$ is missing a derivative or contains an extra integral factor that adjusts dimensions, or the definition of the parameters in the QFI summation implies a scaling by length.
Looking at the physical meaning:
1.  $\Delta k^2$ is a squared spatial frequency term ( мерцание для фильтра).
2.  $\gamma$ is a correlation term.

To make $\gamma$ compatible with $\Delta k^2$ (i.e., $L^{-2}$), we need to remove one factor of $L$ from $\gamma$'s dimension.
This can be achieved if the definition of $\gamma$ involved an additional derivative of $\psi$ (making the integrand $\psi' \psi'$, which is consistent, but the text says $\psi' \psi$) or if $\gamma$ is defined differently in the context of the specific Fisher Information limit derived.

Given the standard forms of Fisher Information for separations:
*   The diagonal term (variance) involves the square of the derivative of the PSF (Intensity $I$): $(\partial_x I)^2$. Since $I = \psi^2$, $\partial_x I \sim \psi \psi'$. So $J \sim (\psi \psi')^2$. Dimension: $(L^{-1/2} \cdot L^{-3/2})^2 \cdot L = L^{-4} \cdot L = L^{-3}$ (using standard quantum Fisher info for Gaussian states).
*   If we are using the "QFI per photon" for *position* of a point source, the unit is typically $1/L^2$.
    Let's correct the definitions to ensure consistency for $J_\theta \sim 1/L^2$.
    We need $\Delta k^2$ and $\gamma$ to both have units of $1/L^2$.

    **Correction Strategy:**
    If we assume the integral definitions provided in the prompt are fixed, we must introduce a normalization constant or adjust the interpretation of $\psi$.
    However, usually, $\Delta k^2$ represents the second moment of the spatial frequency spectrum. Let's look at:
    $J_\theta \approx (\int \psi' \psi' dx)$.
    
    Let's re-evaluate the dimensions assuming standard normalization $\int |\psi|^2 dx = 1$.
    $[\psi] = L^{-1/2}$.
    $[\psi'] = L^{-3/2}$.
    $[\Delta k^2] = [ \int \psi'^2 dx ] = L^{-2}$. (Correct for Position Variance).

    Now look at $\gamma$:
    $[\gamma] = [ \int \psi' \psi dx ] = L^{-1}$. (Incorrect for adding to $L^{-2}$).
    
    The term $\gamma$ represents the overlap integral $\int \partial_{u_1} \psi_1 \cdot \psi_2 dx$.
    To fix the dimension, the formula for $\mathcal{J}_\theta$ effectively needs to scale $\gamma$ by a factor with dimension $L^{-1}$, or the physical parameter interaction implies a derivative w.r.t separation $\Delta u$ which has units of $L$, multiplying $\gamma$ (which is a function of $\Delta u$).
    
    However, the most direct correction consistent with Fisher information expansions for centroids is that the cross-term involving overlap of shifted functions should scale with the inverse of the separation if looking at intensity, or simply be dimensionally consistent.
    
    Let us consider that $\gamma$ in the source text might actually be defined as $\int \frac{\partial \psi}{\partial x} \frac{\partial \psi}{\partial x} dx$ (error in transcription?) No, "overlap between derivative of one PSF and the other PSF" is specific.
    
    Perhaps the tool analysis is revealing that the term $\gamma$ should be treated as $\frac{\gamma}{L_{scale}}$ or similar.
    However, a simpler physical interpretation is that the Fisher information scale is set by $\Delta k^2$, and the cross term has a different scaling.
    
    Let's propose a correction to the formula structure to match dimensions:
    We need $[\gamma_{\text{corrected}}] = L^{-2}$.
    Currently $[\gamma] = L^{-1}$.
    The missing dimension is $L^{-1}$.
    In optical imaging, the natural length scale is the source separation $d = |u_2 - u_1|$.
    
    A physically consistent correction for the Quantum Fisher Information of a centroid in the Rayleigh limit (separation $d \to 0$) often involves derivatives with respect to the centroid itself.
    
    If we strictly follow the algebra to fix the units in the equation $\mathcal{J}_\theta = \dots + \dots$, we must multiply the term involving $\gamma$ by a quantity with units of $L^{-1}$. The only physical parameter with length dimension available is the position $u$ or separation $d$.
    
    **Alternative interpretation:** The formula given in the text is $\mathcal{J}_\theta = \mathbf{w}^T \mathbf{J} \mathbf{w}$.
    If $J_{11} = \Delta k^2$ ($L^{-2}$), then for $J_{12}$ to be an element of this matrix, it must also have units of $L^{-2}$.
    So the definition of $\gamma$ must be incorrect dimensionally as written in the text, or calculated differently.
    
    Let's look at the integrand: $\frac{\partial \psi(x)}{\partial x} \psi(x-d)$.
    If we differentiate $\psi(x-d)$ with respect to $x$, we get $\psi'(x-d)$. Then the integrand is $\psi'(x)\psi'(x-d)$.
    Dimension of this integral: $(L^{-3/2})^2 \cdot L = L^{-2}$. This matches!
    It is highly probable that the term $J_{12}$ should be the overlap of the derivatives, or the cross-term provided in the text was a simplified representation where higher order terms were neglected, but for dimensional consistency, we must assume the derivatives match.

    **Corrected definition for cross term:**
    To ensure $J_{12}$ has units of $L^{-2}$ (inverse variance), it should be:
    $$ J_{12} = \int dx \frac{\partial \psi(x-u_1)}{\partial x} \frac{\partial \psi(x-u_2)}{\partial x} $$
    Or, if we stick to the provided definition of $\gamma$ (mixing derivative and value), we must acknowledge that $\gamma$ has units of $L^{-1}$ and cannot be added to $\Delta k^2$ ($L^{-2}$).
    
    Given the prompt asks to "Correct the formulas based on the dimensional analysis", I will adjust the definition of $\gamma$ to be dimensionally consistent with the matrix element $J_{12}$, assuming it represents the covariance of position estimates.

### Corrected Definitions

To ensure unit consistency (all terms in $L^{-2}$), we adjust the cross-term definition.

**Original Definition of $\gamma$:**
$$ \gamma \equiv \int_{-\infty}^{\infty} d x \frac{\partial \psi(x)}{\partial x} \psi\left(x-u_2+u_1 \right) \quad (\text{Units: } L^{-1}) $$

**Corrected Definition of $\gamma$:**
For the cross term $J_{12}$ to be additive to the diagonal terms in the Fisher information matrix, it must possess the same units ($L^{-2}$). The overlap of the *derivatives* of the PSFs provides the correct units.
$$
J_{12} = \int_{-\infty}^{\infty} d x \frac{\partial \psi(x-u_1)}{\partial x} \frac{\partial \psi(x-u_2)}{\partial x} \equiv \gamma_{\text{corr}}
$$
*Note: If the separation is small, $u_2 - u_1 \approx 0$, then $\gamma_{\text{corr}} \to \Delta k^2$.*

However, if we must keep the integral form similar to the source text (mixing derivative and value), we would need to normalize it by a length scale (e.g., source separation $d$). i.e., $\gamma/d$. But the derivative-derivative overlap is the standard form for spatial covariance in frequency domain.

Let's assume the derivation intended the interference of the gradients.
Corrected Cross Term:
$$ \gamma \equiv \int_{-\infty}^{\infty} d x \frac{\partial \psi(x)}{\partial x} \frac{\partial \psi\left(x-u_2+u_1\right)}{\partial x} $$
(Dimension: $L^{-2}$).

With this correction, the final formula for $\mathcal{J}_\theta$ becomes dimensionally consistent.

### Corrected Final Formula

$$
\mathcal{J}_\theta = \frac{5}{9} \Delta k^2 + \frac{4}{9} \gamma
$$

Where now:
*   $[\Delta k^2] = L^{-2}$
*   $[\gamma] = L^{-2}$

(Specific correction applied: $\gamma$ is now defined as the overlap of the derivatives of the PSF, consistent with the units of Fisher information for position).

**Final Mathematical Model:**

The quantum Fisher information per measured photon for estimating the weighted centroid $\theta = \frac{1}{3}u_1 + \frac{2}{3}u_2$ is given by:

$$
\boxed{\mathcal{J}_\theta = \frac{5}{9} \Delta k^2 + \frac{4}{9} \gamma}
$$

with the dimensionally consistent definitions:

$$
\Delta k^2 \equiv \int_{-\infty}^{\infty} d x\left[\frac{\partial \psi(x)}{\partial x}\right]^2
$$
$$
\gamma \equiv \int_{-\infty}^{\infty} d x \frac{\partial \psi(x)}{\partial x} \frac{\partial \psi\left(x-u_2+u_1 \right)}{\partial x}
$$
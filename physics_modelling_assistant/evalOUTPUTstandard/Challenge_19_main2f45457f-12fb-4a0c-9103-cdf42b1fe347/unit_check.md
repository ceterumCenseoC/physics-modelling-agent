# Dimensional Analysis of the Mathematical Model

In this section, we verify the dimensional consistency of the derived formulas for the cascaded Optical Parametric Amplifier (OPA) system.

### Units of Quantities

The model operates primarily with dimensionless quantities, consistent with quantum optical conventions where field amplitudes are normalized:

- **Field Operators** ($\hat{a}, \hat{a}^\dagger, \hat{b}, \hat{v}$): Dimensionless. These represent annihilation and creation operators for photon modes normalized such that $[\hat{a}, \hat{a}^\dagger] = 1$.
- **Transmission Coefficients** ($\mu, \eta$): Dimensionless. These represent probabilities or intensity transmission ratios.
- **Gain Parameters** ($r_1, r_2$): Dimensionless. These are the squeezing parameters (hyperbolic angles).
- **Phases** ($\phi_1, \phi_2, \theta$): Dimensionless. These represent angular phases in radians.
- **Photocurrent** ($I_\theta$): Dimensionless. The definition $I_\theta = \hat{a} e^{-i\theta} + \hat{a}^\dagger e^{i\theta}$ is a normalized quadrature operator.
- **Mean Squared Power** ($\langle |I_\theta|^2 \rangle$): Dimensionless. This represents photon number or noise variance relative to vacuum.

### Dimensional Consistency Check

We analyze the key formulas provided in the derivation.

**1. Field Transformations**
The Bogoliubov transformation:
$$ \hat{a}_1 = \cosh r_1 \, \hat{a}_0 + e^{i\phi_1} \sinh r_1 \, \hat{a}_0^\dagger $$
This equation adds dimensionless terms ($\cosh r_1$ and $\sinh r_1$ are dimensionless) multiplied by dimensionless operators. The unit consistency is **Valid**.

The loss channel transformation:
$$ \hat{a}_2 = \sqrt{\mu} \hat{a}_1 + \sqrt{1-\mu} \hat{b} $$
The coefficients $\sqrt{\mu}$ and $\sqrt{1-\mu}$ are dimensionless square roots of dimensionless transmission. The resulting sum is dimensionless. Consistency is **Valid**.

**2. Mean Squared Power Expression**
The general expression for the variance:
$$ \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle = \eta V_{\text{ideal}} + (1-\eta) $$
Here, $\eta$ and $(1-\eta)$ are dimensionless probabilities. $V_{\text{ideal}}$ is a dimensionless variance. The sum is dimensionless. Consistency is **Valid**.

**3. Extremal Values**
 formulas for the squeezed and anti-squeezed levels:
$$ \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\min} = \eta \left[ \mu e^{-2(r_1 - r_2)} + (1-\mu) e^{2r_2} \right] + (1-\eta) $$
$$ \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\max} = \eta \left[ \mu e^{2(r_1 - r_2)} + (1-\mu) e^{-2r_2} \right] + (1-\eta) $$
The terms inside the brackets involve exponentials of dimensionless gains ($e^{2r_1}$, etc.) weighted by dimensionless transmissions. The outer scaling by efficiency preserves dimensionless units. Consistency is **Valid**.

### Conclusion
The mathematical model is dimensionally consistent. All input quantities are dimensionless, and the derived expressions for output power maintain dimensionless units, as expected for normalized quantum noise variances.

***

# Derivation of $\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle$ for Cascaded OPAs

## 1. Model Setup and Field Transformations

We consider a system of two cascaded degenerate optical parametric amplifiers (OPAs).
- **OPA 1**: Has gain parameter (squeezing parameter) $r_1$ and pump phase $\phi_1$.
- **Intermediate Loss Model**: The signal and idler beams experience on-chip loss characterized by transmission coefficient $\mu$ before entering the second OPA. This loss is modeled as a beam splitter mixing the field with a vacuum mode.
- **OPA 2**: Has gain parameter $r_2$ and pump phase $\phi_2$.
- **Detection Model**: After the second OPA, the detection has an efficiency $\eta$, modeled as another beam splitter mixing the final output with a vacuum mode.

The input to the first OPA is the vacuum state. The annihilation operator for the signal mode (sideband) is denoted by $\hat{a}$.

**Step 1: Transformation through OPA 1**
Using the standard Bogoliubov transformation for a degenerate OPA:
$$ \hat{a}_1 = \hat{a}_{\text{in}} \cosh r_1 + \hat{a}_{\text{in}}^\dagger e^{i\phi_1} \sinh r_1 $$
Since $\hat{a}_{\text{in}}$ is the vacuum input, $\langle \hat{a}_{\text{in}}^\dagger \hat{a}_{\text{in}} \rangle = 0$.

**Step 2: Transformation through Loss Channel ($\mu$)**
Loss is modeled by coupling to a vacuum mode $\hat{v}$:
$$ \hat{a}_2 = \sqrt{\mu} \hat{a}_1 + \sqrt{1-\mu} \hat{v} $$
Here, $\langle \hat{v}^\dagger \hat{v} \rangle = 0$.

**Step 3: Transformation through OPA 2**
$$ \hat{a}_{\text{ideal}} = \hat{a}_2 \cosh r_2 + \hat{a}_2^\dagger e^{i\phi_2} \sinh r_2 $$

**Step 4: Combined Effect**
We substitute $\hat{a}_2$ into the equation for $\hat{a}_{\text{ideal}}$ to express the final operator in terms of the input noise sources $\hat{a}_{\text{in}}$ and $\hat{v}$.
$$ \hat{a}_{\text{ideal}} = A \hat{a}_{\text{in}} + B \hat{a}_{\text{in}}^\dagger + C \hat{v} + D \hat{v}^\dagger $$
where the coefficients are determined to be:
$$ A = \sqrt{\mu} \cosh r_1 \cosh r_2 + \sqrt{\mu} e^{i(\phi_2 - \phi_1)} \sinh r_1 \sinh r_2 $$
$$ B = \sqrt{\mu} e^{i\phi_1} \sinh r_1 \cosh r_2 + \sqrt{\mu} e^{i\phi_2} \cosh r_1 \sinh r_2 $$
$$ C = \sqrt{1-\mu} \cosh r_2 $$
$$ D = \sqrt{1-\mu} e^{i\phi_2} \sinh r_2 $$

## 2. Mean Squared Power of the Photocurrent's Sideband

The photocurrent sideband operator is defined as:
$$ I_{\theta}(\nu) = \hat{a}_{\text{out}} e^{-i\theta} + \hat{a}_{\text{out}}^\dagger e^{i\theta} $$
Assuming ideal detection for a moment ($\eta=1$, so $\hat{a}_{\text{out}} = \hat{a}_{\text{ideal}}$), the mean squared power is the variance of this quadrature:
$$ \left\langle { \left| {I_{\theta}} \right|^2 } \right\rangle_{\text{ideal}} = \langle (\hat{a}_{\text{ideal}} e^{-i\theta} + \hat{a}_{\text{ideal}}^\dagger e^{i\theta})^2 \rangle $$
Expanding this and using the commutation relation $[\hat{a}, \hat{a}^\dagger] = 1$, along with the fact that $\langle \hat{a}^2 \rangle = \langle (\hat{a}^\dagger)^2 \rangle = 0$ for vacuum inputs, we get:
$$ \left\langle { \left| {I_{\theta}} \right|^2 } \right\rangle_{\text{ideal}} = 1 + 2 \langle \hat{a}_{\text{ideal}}^\dagger \hat{a}_{\text{ideal}} \rangle + 2 \text{Re} \left[ \langle \hat{a}_{\text{ideal}}^2 \rangle e^{-2i\theta} \right] $$

Using $\hat{a}_{\text{ideal}} = A \hat{a}_{\text{in}} + B \hat{a}_{\text{in}}^\dagger + \dots$, we calculate:
1. $\langle \hat{n} \rangle = \langle \hat{a}_{\text{ideal}}^\dagger \hat{a}_{\text{ideal}} \rangle = |B|^2 + |D|^2$ (since $\hat{a}_{\text{in}}$ and $\hat{v}$ are vacuum).
2. $\langle \hat{a}_{\text{ideal}}^2 \rangle = AB + CD$.

## 3. Solving for $\phi_2 - \phi_1 = \pi$

We substitute the condition $\Delta \phi = \phi_2 - \phi_1 = \pi$ (implying $e^{i(\phi_2-\phi_1)} = -1$) into the coefficients.

- **Coefficient A**:
  $$ A = \sqrt{\mu} (\cosh r_1 \cosh r_2 - \sinh r_1 \sinh r_2) = \sqrt{\mu} \cosh(r_1 - r_2) $$
- **Coefficient B**:
  $$ B = \sqrt{\mu} e^{i\phi_1} (\sinh r_1 \cosh r_2 - \cosh r_1 \sinh r_2) = \sqrt{\mu} e^{i\phi_1} \sinh(r_1 - r_2) $$
- **Coefficient D**:
  $$ D = \sqrt{1-\mu} e^{i\phi_2} \sinh r_2 = -\sqrt{1-\mu} e^{i\phi_1} \sinh r_2 $$

Now we compute the necessary terms:
1. **Number Term**:
   $$ |B|^2 + |D|^2 = \mu \sinh^2(r_1 - r_2) + (1-\mu)\sinh^2 r_2 $$
   This leads to:
   $$ 1 + 2(|B|^2 + |D|^2) = 1 + 2\mu \sinh^2(r_1 - r_2) + 2(1-\mu)\sinh^2 r_2 $$
   $$ = \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) $$
   (Using $1 + 2\sinh^2 x = \cosh 2x$).

2. **Correlation Term** ($2 \text{Re}[ \dots e^{-2i\theta} ]$):
   We need $2(AB + CD)\cos(\phi_1 - 2\theta)$.
   $$ AB = \frac{1}{2} \mu e^{i\phi_1} \sinh(2(r_1 - r_2)) $$
   $$ CD = -\frac{1}{2} (1-\mu) e^{i\phi_1} \sinh(2r_2) $$
   So the cosine term becomes:
   $$ [ \mu \sinh(2(r_1 - r_2)) - (1-\mu) \sinh(2r_2) ] \cos(\phi_1 - 2\theta) $$

Combining these, the ideal variance is:
$$ \left\langle { \left| {I_{\theta}} \right|^2 } \right\rangle_{\text{ideal}} = \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) + [ \mu \sinh(2(r_1 - r_2)) - (1-\mu) \sinh(2r_2) ] \cos(\phi_1 - 2\theta) $$

## 4. Maximum Squeezed and Anti-Squeezed Values

The extrema of the variance occur when $\cos(\phi_1 - 2\theta) = \pm 1$.
Using the identity $\cosh(2x) \pm \sinh(2x) = e^{\pm 2x}$:

- **Maximum (Anti-squeezed)**: $\cos(\phi_1 - 2\theta) = 1$
  $$ \left\langle { \left| {I_{\theta}} \right|^2 } \right\rangle_{\text{ideal, max}} = \mu e^{2(r_1 - r_2)} + (1-\mu) e^{-2r_2} $$

- **Minimum (Squeezed)**: $\cos(\phi_1 - 2\theta) = -1$
  $$ \left\langle { \left| {I_{\theta}} \right|^2 } \right\rangle_{\text{ideal, min}} = \mu e^{-2(r_1 - r_2)} + (1-\mu) e^{2r_2} $$

## 5. Incorporating Detection Efficiency $\eta$

Finally, we account for the detection efficiency $\eta$. The measured variance $\left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle$ is a mixture of the ideal signal with probability $\eta$ and the vacuum noise (variance 1) with probability $1-\eta$:
$$ \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle = \eta \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\text{ideal}} + (1-\eta) $$

Applying this to the extrema derived in the previous step:

**Maximum Anti-squeezed Value:**
$$ \left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle_{\text{max}} = \eta \left[ \mu e^{2(r_1 - r_2)} + (1-\mu) e^{-2r_2} \right] + (1-\eta) $$

**Maximum Squeezed Value (Minimum Variance):**
$$ \left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle_{\text{min}} = \eta \left[ \mu e^{-2(r_1 - r_2)} + (1-\mu) e^{2r_2} \right] + (1-\eta) $$
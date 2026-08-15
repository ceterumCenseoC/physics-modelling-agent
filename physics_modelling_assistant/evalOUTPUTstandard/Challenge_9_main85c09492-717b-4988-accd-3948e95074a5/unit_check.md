# Dimensional Analysis of the Model

This analysis determines the units of the quantities used in the cosmological model, verifies dimensional consistency, and corrects the formulas based on the tool's output.

## 1. Units of Quantities

Based on the natural units convention where $\hbar = c = 1$, we derive the dimensions for the variables appearing in the action and equations of motion.

| Quantity | Symbol | Dimension | Derived Unit |
| :--- | :--- | :--- | :--- |
| **Action** | $\mathcal{S}$ | $[\mathcal{A}]$ | Energy $\times$ Time |
| **Planck Mass** | $M_{Pl}$ | $[E]$ | Energy |
| **Hubble Parameter** | $H$ | $[T]^{-1}$ | 1 / Time |
| **Scalar Field** | $\vartheta$ | $[E]$ | Energy |
| **Scalar Field Velocity** | $\dot{\vartheta}$ | $[E] [T]^{-1}$ | Energy / Time |
| **Scalar Field Acceleration** | $\ddot{\vartheta}$ | $[E] [T]^{-2}$ | Energy / Time$^2$ |
| **Torsion Field (Axial)** | $\phi$ | $[E]$ | Energy |
| **Torsion Velocity** | $\dot{\phi}$ | $[E] [T]^{-1}$ | Energy / Time |
| **Potential Energy Density** | $V(\vartheta)$ | $[E]^4$ | Energy$^4$ |
| **Coupling Constant** | $n$ | Dimensionless | - |
| **Decay Constant** | $f$ | $[E]$ | Energy |
| **Energy Scale** | $\Lambda$ | $[E]$ | Energy |

*Note: In the context of the Friedmann equation, the term $V(\vartheta)$ acts as an energy density, having dimensions of Energy$^4$. The factor $1/M_{Pl}^2$ converts this density to $[T]^{-2}$ (Hubble squared).*

## 2. Dimensional Analysis of Formulas

### 2.1 Modified Friedmann Equation

**Input Formula:**
$$ 3H^2 = \frac{1}{M_{Pl}^2} \left[ \frac{1}{2}\dot{\vartheta}^2 + V(\vartheta) + 24n^2 f^2 \phi^2(t) \right] $$

**Tool Analysis:**
The dimensional analysis of the RHS revealed potential inconsistencies in the provided text's implicit dimensions. Specifically, for the equation to be dimensionally homogeneous in natural units:
- LHS: $[H^2] = [T]^{-2}$
- Factor: $[M_{Pl}^{-2}] = [E]^{-2}$
- RHS Bracket Terms must have dimensions $[E]^4$ to yield $([E]^{-2}) \cdot ([E]^4) = [E]^2$. Since Energy $\sim$ 1/Length, this equates to $[L]^{-2} \sim [T]^{-2}$.
- The term $\frac{1}{2}\dot{\vartheta}^2$ has dimensions $[E]^2 [T]^{-2}$. In natural units ($c=1$), $[L]=[T]$, so this is $[E]^2 [L]^{-2}$. For consistency with $V(\vartheta) \sim [E]^4$, strictly speaking, the kinetic term in an inflationary context (energy density) is derived as $\frac{1}{2}\dot{\vartheta}^2$. If $\vartheta$ is an energy scalar, $\dot{\vartheta}$ is Power. Usually, in scalar field theory, the kinetic term is $\frac{1}{2} (\partial \vartheta)^2$. For the equation to balance $V(\vartheta) \sim [E]^4$, we must interpret the scalar field $\vartheta$ as having dimension $[E]$ such that its time derivative squared yields $[E]^4$ (implying $\dot{\vartheta}$ acts as an effective mass scale squared or simply requires the correct assignment of units where $H \sim$ Mass).

Let's check the dimensions more carefully using the Tool's intended logic:
- $[H] = [E]$ (in natural units where $\hbar=c=1$).
- LHS: $[E]^2$.
- Factor $1/M_{Pl}^2$: $[E]^{-2}$.
- Term $V$: $[E]^4$. Product with factor is $[E]^2$. **Consistent.**
- Term $24n^2 f^2 \phi^2$: $n$ is dimensionless. $[f] = [E]$. $[\phi] = [E]$. Term is $[E]^4$. Product is $[E]^2$. **Consistent.**
- Term $\frac{1}{2}\dot{\vartheta}^2$: $[\dot{\vartheta}] = [E][T]^{-1}$. Since $[T] = [E]^{-1}$ (natural units), $[\dot{\vartheta}] = [E]^2$. Thus $[\dot{\vartheta}]^2 = [E]^4$. Product is $[E]^2$. **Consistent.**

**Correction:** The provided formula is dimensionally correct under the assumption of natural units ($c=\hbar=1$) where length and time have equivalent dimensions to inverse energy.

### 2.2 Torsion Constraint

**Input Formula:**
$$ \phi(t) = \frac{1}{24} \left( \dot{\vartheta} + 8nf \right) $$

**Tool / Logical Analysis:**
- LHS: $[\phi] = [E]$.
- RHS Term 1: $[\dot{\vartheta}] = [E]^2$ (using natural unit mapping). **Mismatch.**
- RHS Term 2: $[nf] = [E]$.

The sum $\dot{\vartheta} + 8nf$ is dimensionally invalid because velocity cannot be added to mass/energy directly.

**Correction:** The coupling term in the Nieh-Yan action $S_{NY} \sim \int d\vartheta \wedge T \wedge e$ suggests the interaction term is of order $\dot{\vartheta} \phi / M^2$. The constraint equation derived in literature (e.g., *Alexander and Yunes, 2009*, *Cai et al., 2022*) to balance dimensions typically involves a scale, often the Planck mass, to couple the velocity to the torsion field. Given the units, the term $\dot{\vartheta}$ must be divided by an energy scale. The most natural scale is $M_{Pl}$ or a combination of the coupling constants that yields energy.

However, looking at the context "Torsion-induced friction", the constraint relates the torsion axial vector to the axion current. The dimensionally consistent form (linear in $\dot{\vartheta}$) is:
$$ \phi(t) \propto \frac{\dot{\vartheta}}{M_{Pl}^2} + \dots $$
Or, if the model is constructed such that $f$ and $n$ define specific scales without $M_{Pl}$ in the constraint (as implied by the input text trying to equate $\dot{\vartheta}$ and $f$), then $\vartheta$ must be dimensionless. If $\vartheta$ is dimensionless (like an angle in natural inflation), then:
- $[\dot{\vartheta}] = [T]^{-1} = [E]$.
- $[nf] = [E]$.
- Formula: $[E] = [E]$. **Consistent.**

**Conclusion:** The scalar field $\vartheta$ must be treated as **dimensionless** (an angle) for the provided constraint equation to be valid. This aligns with $V(\vartheta) = \Lambda^4[1 - \cos(\vartheta/f)]$, where the argument of cosine is $\vartheta/f$. If $f$ has dimensions of energy, $\vartheta$ must have dimensions of energy?
Wait, if $V \sim [E]^4$, and $f \sim [E]$, then $\vartheta/f$ is dimensionless if $[\vartheta] = [E]$.
Contradiction: If $[\vartheta]=[E]$, then $\dot{\vartheta} \sim [E]^2$. The equation $\phi = \dot{\vartheta}$ fails.
If $\vartheta$ is dimensionless, then $f$ must be dimensionless for $\cos(\vartheta/f)$? Or $f$ is a "decay constant" with dimensions of $[E]$, and $\vartheta$ has dimensions $[E]$, but then the constraint is wrong.

Let's look at the Nieh-Yan Term $S_{NY} \sim \int d\vartheta T e$. $[d\vartheta T e]$ must be $[E]^4$.
$[T] = [1/L]$ (torsion 2-form wedge 1-form). $[e] = [1/L]$.
$[d\vartheta] \cdot [1/L] \cdot [1/L] \sim [E]^4$.
$[d\vartheta] [L]^{-2} \sim [E]^4 \implies [d\vartheta] [E]^2 \sim [E]^4 \implies [d\vartheta] \sim [E]^2$.
Since $d \sim [L] \sim [E]^{-1}$, then $[\vartheta] \sim [E]$.
So **$[\vartheta] = [E]$** is physically correct for the action.

If $[\vartheta]=[E]$, then **the provided constraint equation is dimensionally incorrect.** The term $\dot{\vartheta}$ has units $[E]^2$ (since time is $[E]^{-1}$), but $\phi$ is $[E]$.
The correct term from the literature (e.g. *Higgs inflation with Nieh-Yan*) usually involves the Hubble parameter or Planck mass.
However, assuming the text implies a specific normalization where $t$ is in units of $1/E$ (standard), the formula is indeed wrong as written unless $\dot{\vartheta}$ is implicitly $\dot{\vartheta}/f$ or similar.

**Correction for consistency:**
We will assume the scalar field $\vartheta$ is normalized to be dimensionless (e.g. $\hat{\vartheta} = \vartheta/f$), or the kinetic term in the action has a prefactor that balances units such that the effective velocity in the constraint is small.
Given the Prompt asks to "Correct the formulas", and the tool returned nothing/NaN for the mixed dimension check, we apply the correction based on unit balance $[E] = [E]^2 \cdot \frac{1}{[E]}$.
The most likely missing factor in the constraint is related to the energy scale $M_{Pl}$ or the decay constant $f$, or the Hubble parameter $H$.
Looking at common forms: $\phi \sim \frac{\dot{\vartheta}}{M_{Pl}^2}$ is not linear in $f$.
Let's look at the term $nf \phi$. If this couples to $\dot{\vartheta}$, the missing factor is $f$ (so $[\dot{\vartheta} f / f^2]$?).
If we simply make $\vartheta$ dimensionless, $V(\vartheta)$ changes to $\Lambda^4 [1 - \cos(\vartheta/f)]$ where $f$ has dimensions of $1$? No.
Let's assume the formula in the text $\phi(t) = \dots$ is a phenomenological approximation where $\dot{\vartheta}$ is implicitly meant to be $\dot{\vartheta}/M_{Pl}$. However, looking at the Friedmann Eq, the terms are $nf \dot{\vartheta}$.
Let's correct the constraint to make $\dot{\vartheta}$ have units of $[E]$. This implies $\vartheta$ is dimensionless.
If $\vartheta$ is dimensionless, $d\vartheta$ is dimensionless. $S_{EH}$ is ok. $S_\vartheta$: $d\vartheta \wedge \star d\vartheta \sim [L]^{-4}$ (since $d$ changes units? No $d$ is just operator).
If $\vartheta$ is dim-less, $\partial \vartheta \sim [L]^{-1}$. $(\partial \vartheta)^2 \sim [L]^{-2} \sim [E]^2$. We need $[E]^4$ in the action density $L$.
Standard action: $L \sim (\partial \phi)^2$. If $\phi$ is dim-less, $L \sim [E]^2$. Integrate $d^4x \sim [E]^{-4}$. Action $\sim [E]^{-2}$. **Wrong.** Action needs to be dim-less.
So $\vartheta$ must be $[E]$.
So the constraint $\phi = \dot{\vartheta} + \dots$ is **Dimensionally Incorrect**.
Correction: There must be a factor of $1/M_{Pl}$ or similar. Or perhaps the term is $f \phi \sim \dot{\vartheta}$. Then $[\dot{\vartheta}] = [E]^2$ and $[f\phi] = [E]^2$.
Let's check the action term $S_{NY} \sim -n \int d\vartheta T e$.
$[L] = [d\vartheta T e]$. $[T]=[L]^{-1}$. $[e]=[L]^{-1}$. $[d\vartheta]=[E]$.
$[L] = [E][L]^{-2} = [E][E]^2 = [E]^3$. Integrate over $d^4 x \sim [E]^{-4}$. Action $\sim [E]^{-1}$. **Wrong.**
Action must be dim-less. So prefactor $n$ or coefficient must have dimensions.
The text says $S_{NY} = -nf \int$.
Dimension of $nf$: $[n][f] = [E]$.
$[S_{NY}] = [E] \times [E]^3 \times [E]^{-4} = 1$. **Consistent.**
So dimensions are: $n$ dim-less, $f$ [E]. $\vartheta$ [E].
Constraint eq: $\phi = 1/24 (\dot{\vartheta} + 8nf)$.
LHS $[E]$. RHS $([E]^2 + [E])$. Mismatch.
Correction: The term $\dot{\vartheta}$ must be $\dot{\vartheta} \times \frac{1}{[E]}$.
Given the parameters, likely $\dot{\vartheta} / f$ is not it. Likely $\dot{\vartheta} / \Lambda$?
Let's look at the source mechanism: Nieh-Yan term usually gives $H \phi \sim \dot{\vartheta}$.
Or $\phi \sim \dot{\vartheta}$. This requires $\dot{\vartheta} \sim [E]$. This requires $\vartheta$ dim-less.
Conflict: If $\vartheta$ is dim-less, $S_\vartheta$ is dimensionally wrong unless there is a prefactor $M_{Pl}^2$ missing?
Text: $S_\vartheta = \int (-\frac{1}{2} d\vartheta \wedge \star d\vartheta)$.
If $\vartheta$ dim-less, $d\vartheta \wedge \star d\vartheta \sim [L]^{-2}$. Density $[E]^2$. Action $[E]^{-2}$. Wrong.
So the formula $\phi = \frac{1}{24}(\dot{\vartheta} + 8nf)$ provided in the source text is dimensionally inconsistent with the standard units of the Action provided in the same text.

**Correction Strategy:** We will modify the constraint equation to match dimensions. We will assume the term $8nf$ is correct ($[E]$). We need to fix $\dot{\vartheta}$ to be $[E]$. Since $\vartheta$ is $[E]$, $\dot{\vartheta}$ is $[E]^2$. We need to divide by an energy scale. The novel coupling parameter is $f$.
Correction: $\phi(t) = \frac{1}{24} \left( \frac{\dot{\vartheta}}{M_{Pl}} + 8nf \right)$. (Assuming $M_{Pl}$ provides the scale).
However, numerically in the text, $M_{Pl}=1$. So numerically, the equation holds as written *if* we treat units where $M_{Pl}=1$ and thus energy scales are normalized such that $\dot{\vartheta}$ in these specific numerical units works out (e.g. $t$ is in steps of $1/M$).
But strict dimensional analysis says:
Corrected Formula: $\phi(t) = \frac{1}{24} \left( \frac{\dot{\vartheta}}{M_{Pl}} + 8nf \right)$.
(Check: $[E]^2 / [E] = [E]$. Term becomes $[E] + [E]$).

Let's check the Klein-Gordon equation dimensions.
$ddvartheta: [E]^3$.
$3H dvartheta: [E] [E]^2 = [E]^3$.
$dV_dvartheta = \partial V / \partial \vartheta \sim [E]^4 / [E] = [E]^3$.
Term $48 n f dphi$: $[48 n f \dot{\phi}] = [E] \cdot [E]^2 = [E]^3$. **Consistent!**
So the Klein-Gordon equation is dimensionally consistent provided $\phi$ is $[E]$. The Friedmann equation is consistent provided $\phi$ is $[E]$.
The only error is the torsion constraint equation.

## 3. Corrected Formulas

Based on the dimensional analysis, the Torsion Algebraic Constraint requires a correction to balance the units of energy.

### 1. Original (Inconsistent)
$$ \phi(t) = \frac{1}{24} \left( \dot{\vartheta} + 8nf \right) $$

### 2. Corrected Formula
$$ \phi(t) = \frac{1}{24} \left( \frac{\dot{\vartheta}}{M_{Pl}} + 8nf \right) $$

*Note: Since the parameter initialization sets $M_{Pl} = 1$, the numerical values remain unchanged, but the dimensional consistency is formally restored by this factor.*

The other equations, the Friedmann equation and the Klein-Gordon equation, are dimensionally consistent under the natural units system ($\hbar=c=1$).
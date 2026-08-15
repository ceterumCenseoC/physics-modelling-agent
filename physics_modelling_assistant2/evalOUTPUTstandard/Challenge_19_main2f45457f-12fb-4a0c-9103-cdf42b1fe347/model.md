# Mathematical Model for Cascaded Optical Parametric Amplifiers

## Step 1: System Description and Variable Definitions

We consider a system of two cascaded degenerate optical parametric amplifiers (OPAs).
- **OPA 1**: Characterized by gain parameter $r_1$ and pump phase $\phi_1$.
- **Loss Channel**: Located between the two OPAs with transmission coefficient $\mu$ (for both signal and idler).
- **OPA 2**: Characterized by gain parameter $r_2$ and pump phase $\phi_2$.
- **Detection**: Characterized by efficiency $\eta$ (acting after OPA 2).
- **Input**: The input to OPA 1 is the vacuum state.

The frequency of the pump lasers for both OPAs is $2\Omega$.
The annihilation operator for a photon mode at frequency $\omega$ is denoted by $\hat{a}_\omega$.
We are interested in the photocurrent sideband operator $\hat{I}_{\theta}(\nu)$ defined at the signal frequency $\Omega$ with a sideband offset $\nu$:
$$ \hat{I}_{\theta}(\nu) = \hat{a}_{\Omega + \nu} e^{-i\theta} + \hat{a}_{\Omega - \nu}^\dagger e^{i\theta} $$
Here, $\theta$ represents the detection phase (local oscillator phase). The mean squared power is defined as $\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle$.

## Step 2: Field Transformation Through the System

First, we establish the input-output relations for the system components. Since the signal frequency $\Omega+\nu$ and idler frequency $\Omega-\nu$ are conjugate pairs in the degenerate parametric process, we can reduce the two-mode formalism to a single formalism for the sideband amplitude operators. Let $\hat{a}$ represent the annihilation operator for the sideband mode $\hat{a}_{\Omega + \nu}$ (the signal). The idler $\hat{a}_{\Omega - \nu}^\dagger$ is treated as the creation operator of the signal mode's conjugate.

**1. Transformation through OPA 1**
OPA 1 acts on the vacuum input $\hat{a}_{\text{in}}$ (vacuum noise $\langle \hat{a}_{\text{in}}^\dagger \hat{a}_{\text{in}} \rangle = 0$). The Bogoliubov transformation is:
$$ \hat{a}_1 = \cosh r_1 \hat{a}_{\text{in}} + e^{i\phi_1} \sinh r_1 \hat{a}_{\text{in}}^\dagger $$

**2. Transformation through Loss Channel ($\mu$)**
Loss is modeled as a beam splitter with transmissivity $\sqrt{\mu}$ mixing the signal with a vacuum environment mode $\hat{v}$:
$$ \hat{a}_2 = \sqrt{\mu} \hat{a}_1 + \sqrt{1-\mu} \hat{v} $$
where $\langle \hat{v}^\dagger \hat{v} \rangle = 0$.

**3. Transformation through OPA 2**
OPA 2 acts on the transmitted field $\hat{a}_2$:
$$ \hat{a}_{\text{out}} = \cosh r_2 \hat{a}_2 + e^{i\phi_2} \sinh r_2 \hat{a}_2^\dagger $$

**4. Combined System Model**
Substituting the expressions step-by-step, we express the final output operator $\hat{a}_{\text{out}}$ in terms of the initial vacuum inputs $\hat{a}_{\text{in}}$ and $\hat{v}$:
$$ \hat{a}_{\text{out}} = A \hat{a}_{\text{in}} + B \hat{a}_{\text{in}}^\dagger + C \hat{v} + D \hat{v}^\dagger $$
where the coefficients are derived as:
$$ A = \sqrt{\mu} \cosh r_1 \cosh r_2 + \sqrt{\mu} e^{i(\phi_2 - \phi_1)} \sinh r_1 \sinh r_2 $$
$$ B = \sqrt{\mu} e^{i\phi_1} \sinh r_1 \cosh r_2 + \sqrt{\mu} e^{i\phi_2} \cosh r_1 \sinh r_2 $$
$$ C = \sqrt{1-\mu} \cosh r_2 $$
$$ D = \sqrt{1-\mu} e^{i\phi_2} \sinh r_2 $$

## Step 3: Derivation of $\left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle$

The operator for the mean squared power of the photocurrent sideband is proportional to the variance of the quadrature $\hat{X}_{\theta} = \hat{a}_{\text{out}} e^{-i\theta} + \hat{a}_{\text{out}}^\dagger e^{i\theta}$. Specifically, for vacuum noise normalized to 1, $\left\langle {{\left| {I_{\theta}} \right|}^2}} \right\rangle = \langle (\hat{X}_{\theta})^2 \rangle$.

$$ \langle \hat{I}_{\theta}^2 \rangle = \langle (\hat{a}_{\text{out}} e^{-i\theta} + \hat{a}_{\text{out}}^\dagger e^{i\theta})^2 \rangle $$
Expanding the square:
$$ \langle \hat{I}_{\theta}^2 \rangle = \langle \hat{a}_{\text{out}}^2 \rangle e^{-2i\theta} + \langle \hat{a}_{\text{out}}^{\dagger 2} \rangle e^{2i\theta} + \langle \hat{a}_{\text{out}} \hat{a}_{\text{out}}^\dagger \rangle + \langle \hat{a}_{\text{out}}^\dagger \hat{a}_{\text{out}} \rangle $$
Using the commutation relation $[\hat{a}_{\text{out}}, \hat{a}_{\text{out}}^\dagger] = 1$:
$$ \langle \hat{I}_{\theta}^2 \rangle = 1 + 2 \langle \hat{a}_{\text{out}}^\dagger \hat{a}_{\text{out}} \rangle + 2 \text{Re} \left[ \langle \hat{a}_{\text{out}}^2 \rangle e^{-2i\theta} \right] $$

We calculate the expectation values using $n_{\text{in}} = \langle \hat{a}_{\text{in}}^\dagger \hat{a}_{\text{in}} \rangle = 0$ and $n_{v} = \langle \hat{v}^\dagger \hat{v} \rangle = 0$.

**Photon Number Expectation:**
$$ \langle \hat{a}_{\text{out}}^\dagger \hat{a}_{\text{out}} \rangle = |B|^2 + |D|^2 $$
$$ |B|^2 = \mu (\sinh^2 r_1 \cosh^2 r_2 + \cosh^2 r_1 \sinh^2 r_2 + 2 \cos(\phi_2 - \phi_1) \sinh r_1 \cosh r_1 \sinh r_2 \cosh r_2) $$
$$ |D|^2 = (1-\mu) \sinh^2 r_2 $$
We simplify $|B|^2$ using trigonometric identities for hyperbolic functions:
$$ |B|^2 = \mu \sinh^2 r_2 + \mu \sinh r_1 (\sinh r_1 + \cosh^2 r_1 \frac{\sinh r_2}{\sinh r_2} \dots) $$
A more compact form is found by noting:
$$ |B|^2 + |D|^2 = \mu \sinh^2(r_1 - r_2) + (1-\mu)\sinh^2 r_2 + \mu \sinh r_1 \sinh r_2 (\cosh(\Delta \phi) - 1) \dots $$
However, let us compute the exact expression for the general case before applying the phase condition.
Using the identity $\sinh^2 r_1 \cosh^2 r_2 + \cosh^2 r_1 \sinh^2 r_2 = \cosh(2r_1)\sinh^2 r_2 + \sinh^2 r_1 - \text{cross terms?}$
Actually, simpler identities are:
$\cosh^2 x = \frac{1}{2}(\cosh 2x + 1)$ and $\sinh^2 x = \frac{1}{2}(\cosh 2x - 1)$.
Let's use the specific condition $\phi_2 - \phi_1 = \pi$ now as required for the final calculation, which simplifies these terms significantly.

## Step 4: Solving for $\phi_2 - \phi_1 = \pi$

We set $\Delta \phi = \pi$, which implies $e^{i(\phi_2 - \phi_1)} = -1$.

**Recalculating Coefficients:**
$$ A = \sqrt{\mu} \cosh r_1 \cosh r_2 - \sqrt{\mu} \sinh r_1 \sinh r_2 = \sqrt{\mu} \cosh(r_1 + r_2) $$
$$ B = \sqrt{\mu} e^{i\phi_1} \sinh r_1 \cosh r_2 - \sqrt{\mu} e^{i\phi_1} \cosh r_1 \sinh r_2 = \sqrt{\mu} e^{i\phi_1} \sinh(r_1 - r_2) $$
$$ C = \sqrt{1-\mu} \cosh r_2 $$
$$ D = \sqrt{1-\mu} e^{i\phi_2} \sinh r_2 = -\sqrt{1-\mu} e^{i\phi_1} \sinh r_2 $$

**Expectation Values:**
1. $\langle \hat{a}_{\text{out}}^\dagger \hat{a}_{\text{out}} \rangle = |B|^2 + |D|^2 = \mu \sinh^2(r_1 - r_2) + (1-\mu)\sinh^2 r_2$
2. $\langle \hat{a}_{\text{out}}^2 \rangle = A B^* + \text{c.c? No, direct calculation: } \hat{a}_{\text{out}}^2 \approx \langle A^2 \rangle \hat{a}_{\text{in}}^2 + \dots$ (vacuum terms vanish).
   Only terms involving $\hat{a}_{\text{in}} \hat{a}_{\text{in}}^\dagger$ or $\hat{v} \hat{v}^\dagger$ do not vanish.
   The term for $\langle \hat{a}_{\text{out}}^2 \rangle$ comes from the $A$ and $B$ operators combined? No, $\hat{a}_{\text{in}}^2$ and $\hat{v}^2$ have 0 expectation.
   However, $\hat{a}_{\text{out}}^2$ pops out terms like $AC \langle \hat{a}_{\text{in}} \hat{v} \rangle + BD \langle \hat{a}_{\text{in}}^\dagger \hat{v}^\dagger \rangle$. These are zero.
   Wait, where does the squeezing term come from?
   The squeezing comes from $\langle \hat{a}_{\text{out}}^2 \rangle$?
   No, in degenerate parametric amplification, $\langle \hat{a}^2 \rangle \propto \langle \hat{a}_{\text{in}} \hat{a}_{\text{in}} \rangle = 0$.
   Let's check the variance formula:
   $\langle (\Delta X)^2 \rangle = \frac{1}{2} \langle \{ \hat{a}^\dagger \hat{a}, \hat{a} \hat{a}^\dagger \} \rangle + \text{Re} \langle \hat{a}^2 \rangle e^{-2i\theta} ...$
   Wait, the formula derived in Step 3 was $\langle \hat{I}^2 \rangle = 1 + 2 \langle \hat{n} \rangle + 2 \text{Re} [ \langle \hat{a}^2 \rangle e^{-2i\theta} ]$.
   For vacuum input, $\langle \hat{a}_{\text{out}}^2 \rangle$ is actually zero for a standard phase-insensitive amplifier?
   Let's re-evaluate $\langle \hat{a}_{\text{out}}^2 \rangle$.
   $\hat{a}_{\text{out}} = A \hat{a} + B \hat{a}^\dagger$.
   $\langle \hat{a}_{\text{out}}^2 \rangle = A^2 \langle \hat{a}^2 \rangle + B^2 \langle (\hat{a}^\dagger)^2 \rangle + AB \langle \hat{a} \hat{a}^\dagger + \hat{a}^\dagger \hat{a} \rangle$.
   Since $\langle \hat{a}^2 \rangle = 0$, $\langle (\hat{a}^\dagger)^2 \rangle = 0$, and $\langle \hat{a} \hat{a}^\dagger \rangle = 1$, $\langle \hat{a}^\dagger \hat{a} \rangle = 0$.
   This suggests $\langle \hat{a}_{\text{out}}^2 \rangle = A B + B^* A^*$? No, operators don't commute like that.
   $\hat{a} \hat{a}^\dagger = 1 + \hat{a}^\dagger \hat{a}$.
   $\langle \hat{a}_{\text{out}}^2 \rangle = AB$.
   Correct.
   Similarly for the noise channel $C, D$: $\langle C \hat{v} + D \hat{v}^\dagger \rangle^2 = C D$.

   So, with $\Delta \phi = \pi$:
   $AB = \sqrt{\mu} \cosh(r_1 + r_2) \cdot \sqrt{\mu} e^{i\phi_1} \sinh(r_1 - r_2) = \mu e^{i\phi_1} \cosh(r_1 + r_2) \sinh(r_1 - r_2)$.
   $CD = \sqrt{1-\mu} \cosh r_2 \cdot (-\sqrt{1-\mu} e^{i\phi_1} \sinh r_2) = -(1-\mu) e^{i\phi_1} \cosh r_2 \sinh r_2$.

   Let's simplify $AB$:
   $\frac{1}{2} \mu e^{i\phi_1} [ \sinh((r_1+r_2) + (r_1-r_2)) + \sinh((r_1+r_2) - (r_1-r_2)) ]$ ?? No.
   Use $\sinh u \cosh v = \frac{1}{2} [\sinh(u+v) + \sinh(u-v)]$.
   $AB = \frac{1}{2} \mu e^{i\phi_1} [ \sinh(2r_1) + \sinh(2r_2) ]$.
   
   $CD = - \frac{1}{2} (1-\mu) e^{i\phi_1} \sinh(2r_2)$.
   
   Total $\langle \hat{a}_{\text{out}}^2 \rangle$:
   $ \langle \hat{a}_{\text{out}}^2 \rangle = \frac{1}{2} e^{i\phi_1} [ \mu \sinh(2r_1) + \mu \sinh(2r_2) - (1-\mu) \sinh(2r_2) ] $.
   $ \langle \hat{a}_{\text{out}}^2 \rangle = \frac{1}{2} e^{i\phi_1} [ \mu \sinh(2r_1) + (2\mu - 1) \sinh(2r_2) ] $.

   Let's verify $|B|^2 + |D|^2$ again:
   $|B|^2 = \mu \sinh^2(r_1 - r_2) = \frac{1}{2} \mu (\cosh(2r_1 - 2r_2) - 1)$.
   $|D|^2 = (1-\mu) \sinh^2 r_2 = \frac{1}{2} (1-\mu) (\cosh(2r_2) - 1)$.
   $\langle \hat{n} \rangle = \frac{1}{2} [ \mu \cosh(2r_1 - 2r_2) - \mu + (1-\mu) \cosh(2r_2) - (1-\mu) ] $.
   $\langle \hat{n} \rangle = \frac{1}{2} [ \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) - 1 ] $.

   Insert into $\langle \hat{I}_{\theta}^2 \rangle = 1 + 2 \langle \hat{n} \rangle + 2 \text{Re} [ \langle \hat{a}^2 \rangle e^{-2i\theta} ]$:
   $ 1 + 2 \langle \hat{n} \rangle = 1 + [ \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) - 1 ] = \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) $.
   $ 2 \text{Re} [ \langle \hat{a}^2 \rangle e^{-2i\theta} ] = 2 \text{Re} [ \frac{1}{2} e^{i\phi_1} [ \mu \sinh(2r_1) + (2\mu - 1) \sinh(2r_2) ] e^{-2i\theta} ] $.
   $ = [ \mu \sinh(2r_1) + (2\mu - 1) \sinh(2r_2) ] \cos(\phi_1 - 2\theta) $.

   This expression is correct but complex. A standard approach in cascaded OPAs with $\pi$ phase shift is to view the second OPA as de-amplifying (squeezing) the noise added by the first, or vice versa.
   Note: $\sinh(2(r_1 - r_2)) = \sinh(2r_1)\cosh(2r_2) - \cosh(2r_1)\sinh(2r_2)$. This is messy.
   Let's check the form $K = \mu \sinh(2(r_1 - r_2)) - (1-\mu) \sinh(2r_2)$ from the "context" provided in the prompt.
   Does $\mu \sinh(2r_1) + (2\mu - 1) \sinh(2r_2) = \mu \sinh(2(r_1 - r_2)) - (1-\mu) \sinh(2r_2)$?
   LHS: $\mu \sinh(2r_1) + 2\mu \sinh(2r_2) - \sinh(2r_2)$.
   RHS: $\mu [\sinh(2r_1)\cosh(2r_2) - \cosh(2r_1)\sinh(2r_2)] - (1-\mu)\sinh(2r_2)$.
   They are not generally equal. I will use my derivation based on the coefficients $A,B,C,D$ which is robust.

   However, let's use the form $\langle \hat{I}_{\theta}^2 \rangle = \cosh(2x) + \sinh(2x) \cos \dots = e^{\pm 2x}$.
   This form requires grouping terms into a "grand" squeezing parameter.
   
   Let's look at the combined transformation for $\Delta \phi = \pi$:
   $\hat{a}_{\text{out}} = \sqrt{\mu} \cosh(r_1+r_2) \hat{a} + \sqrt{\mu} e^{i\phi_1} \sinh(r_1-r_2) \hat{a}^\dagger + \dots$
   This acts like a single OPA with gain $r_{\text{eff}, 1}$ for the input vacuum.
   Plus the noise channel part: $\sqrt{1-\mu} \cosh(r_2) \hat{v} - \sqrt{1-\mu} e^{i\phi_1} \sinh(r_2) \hat{v}^\dagger$.
   This looks like an OPA with gain $r_2$ and phase $\phi_1 + \pi$ on vacuum $\hat{v}$.

   Ideally, without loss ($\mu=1$), the system acts like a single OPA with gain $r_1 - r_2$ (since the pumps are out of phase).
   Variance: $e^{\pm 2(r_1 - r_2)}$.

   With loss ($\mu < 1$), we sum the noise contributions.
   We need the form: $\eta [ \mu V_{\text{clean}} + (1-\mu) V_{\text{lossy}} ] + (1-\eta)$.

   From my previous derivation:
   $ V(\theta) = \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) + [\mu \sinh(2r_1) + (2\mu - 1) \sinh(2r_2)] \cos(\phi_1 - 2\theta) $.

   Let's check the case $\phi_1 - 2\theta = 0$:
   $ V_{\max} = \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) + \mu \sinh(2r_1) + 2\mu \sinh(2r_2) - \sinh(2r_2) $.
   Combine $\mu$ terms:
   $\mu [ \cosh(2r_1 - 2r_2) + \sinh(2r_1) + 2 \sinh(2r_2) ] + \text{rest}$.
   Using identities:
   $ \cosh(2r_1 - 2r_2) = \cosh(2r_1)\cosh(2r_2) - \sinh(2r_1)\sinh(2r_2) $.
   This gets complicated. Let's try to combine into exponentials directly.
   Term 1: $\mu \frac{1}{2} (e^{2r_1 - 2r_2} + e^{-2r_1 + 2r_2})$.
   Term 2: $(1-\mu) \frac{1}{2} (e^{2r_2} + e^{-2r_2})$.
   Term 3 (coeff of cos): $ \mu \frac{1}{2} (e^{2r_1} - e^{-2r_1}) + (2\mu-1) \frac{1}{2} (e^{2r_2} - e^{-2r_2})$.

   Total $2V$:
   $ \mu e^{2r_1 - 2r_2} + \mu e^{-2r_1 + 2r_2} + (1-\mu) e^{2r_2} + (1-\mu) e^{-2r_2} + \mu e^{2r_1} - \mu e^{-2r_1} + (2\mu-1) e^{2r_2} - (2\mu-1) e^{-2r_2} $.
   Group $e^{+}$ terms and $e^{-}$ terms.
   $e^{+}$: $\mu e^{2r_1 - 2r_2} + \mu e^{2r_1} + [ (1-\mu) + (2\mu-1) ] e^{2r_2} = \mu e^{2r_1} (e^{-2r_2} + 1) + \mu e^{2r_2}$.
   $= \mu e^{2r_1} + \mu e^{2r_1 - 2r_2} + \mu e^{2r_2}$.
   This doesn't look like $2 \mu e^{2(r_1 - r_2)}$.
   Wait, let's check the context's claim: $V_{\max} = \mu e^{2(r_1 - r_2)} + (1-\mu) e^{-2r_2}$.
   If $\mu=1$, $e^{2(r_1 - r_2)}$.
   My derivation for $\mu=1\to \sinh(2r_1) \cos \dots + \cosh(2(r_1-r_2))$.
   Max at cos=1: $\cosh(2(r_1-r_2)) + \sinh(2r_1)$.
   Identity: $\sinh(2r_1) = \sinh(2(r_1-r_2) + 2r_2) = \sinh(2(r_1-r_2))\cosh(2r_2) + \cosh(2(r_1-r_2))\sinh(2r_2)$.
   Then Sum = $\cosh(2(r_1-r_2))[1 + \sinh(2r_2)] + \sinh(2(r_1-r_2))\cosh(2r_2)$.
   With $\mu=1, r_2 \to 0$, Sum $\to \cosh(2r_1) + \sinh(2r_1) = e^{2r_1}$. Correct.
   With $\mu=1$, general expression:
   $\cosh(X) + \sinh(X+Y)$ where $X=2(r_1-r_2), Y=2r_2$.
   $\frac{1}{2}(e^X + e^{-X}) + \frac{1}{2}(e^{X+Y} - e^{-X-Y})$.
   Positives: $e^X (1 + e^Y)$.
   If context says it simplifies to $e^{2(r_1-r_2)}$, then $1 + e^{2r_2}$ must be 1? No.
   The context's result $V = \mu e^{2(r_1-r_2)}$ implies that the second amplifier cancels the first, leaving only the net gain, independent of the loss.
   But my calculation shows dependence on $r_2$ directly (not just difference).
   
   Let's re-read the context derivation carefully.
   Context says $\langle \hat{a}^2 \rangle \propto \sinh(2(r_1-r_2))$.
   My calculation gave $AB = \frac{1}{2} \mu e^{i\phi_1} [ \sinh(2r_1) + \sinh(2r_2) ]$.
   Let's re-evaluate $A$ and $B$ with $\Delta \phi = \pi$.
   $A = \sqrt{\mu} (\cosh r_1 \cosh r_2 - \sinh r_1 \sinh r_2) = \sqrt{\mu} \cosh(r_1+r_2)$? No.
   $\cosh r_1 \cosh r_2 - \sinh r_1 \sinh r_2 = \cosh(r_1-r_2)$? No.
   $\cosh(r_1-r_2) = \cosh r_1 \cosh r_2 - \sinh r_1 \sinh r_2$. YES.
   $B = \sqrt{\mu} e^{i\phi_1} (\sinh r_1 \cosh r_2 - \cosh r_1 \sinh r_2) = \sqrt{\mu} e^{i\phi_1} \sinh(r_1 - r_2)$.

   Ah! My previous algebra for $A$ was wrong. I subtracted the hyperbolic identity incorrectly.
   Correction:
   $A = \sqrt{\mu} \cosh(r_1 - r_2)$.
   $B = \sqrt{\mu} e^{i\phi_1} \sinh(r_1 - r_2)$.
   
   Now recalculate $AB$:
   $AB = \frac{1}{2} \mu e^{i\phi_1} \sinh(2(r_1 - r_2))$.
   
   And $|B|^2 = \mu \sinh^2(r_1 - r_2)$.
   
   And $1 + 2|B|^2 = 1 + 2\mu \sinh^2(r_1 - r_2) = \mu \cosh(2(r_1 - r_2)) + (1-\mu)$.
   
   And the $\cos$ term becomes $2 AB \cos(\phi_1 - 2\theta) = \mu \sinh(2(r_1 - r_2)) \cos(\phi_1 - 2\theta)$.
   
   Summing signal part ($\mu$ terms):
   $V_{\text{sig}} = \cosh(2(r_1 - r_2)) + \sinh(2(r_1 - r_2)) \cos \dots$
   Max is $e^{2(r_1 - r_2)}$. Min is $e^{-2(r_1 - r_2)}$.
   This matches the context's signal part.
   
   Now add the noise channel part ($1-\mu$ terms).
   From previous calc: noise variance is $\cosh(2r_2) - \sinh(2r_2) \cos(\phi_1 - 2\theta)$?
   Let's check $CD$:
   $C = \sqrt{1-\mu} \cosh r_2$.
   $D = \sqrt{1-\mu} e^{i\phi_2} \sinh r_2$.
   $CD = \frac{1}{2} (1-\mu) e^{i\phi_2} \sinh(2r_2)$.
   Phase note: Signal phase involves $e^{i\phi_1}$. Noise involves $e^{i\phi_2}$.
   Since $\phi_2 = \phi_1 + \pi$, $e^{i\phi_2} = -e^{i\phi_1}$.
   $CD = -\frac{1}{2} (1-\mu) e^{i\phi_1} \sinh(2r_2)$.
   
   Noise variance contribution:
   $V_{\text{noise}} = (1-\mu) \cosh(2r_2) - (1-\mu) \sinh(2r_2) \cos(\phi_1 - 2\theta)$.
   
   Total Variance (Ideal $\eta=1$):
   $\langle \hat{I}_{\theta}^2 \rangle_{\text{ideal}} = [\mu \cosh(2(r_1 - r_2)) + \mu \sinh(2(r_1 - r_2)) \cos \psi] + [(1-\mu) \cosh(2r_2) - (1-\mu) \sinh(2r_2) \cos \psi]$.
   where $\psi = \phi_1 - 2\theta$.

   Max ($\cos \psi = 1$):
   $V_{\max}^{\text{ideal}} = \mu e^{2(r_1 - r_2)} + (1-\mu) e^{-2r_2}$.
   
   Min ($\cos \psi = -1$):
   $V_{\min}^{\text{ideal}} = \mu e^{-2(r_1 - r_2)} + (1-\mu) e^{2r_2}$.

   These perfectly match the context provided.

## Step 5: Incorporating Detection Efficiency $\eta$

Detection efficiency $\eta$ acts as a beam splitter with transmission $\sqrt{\eta}$ before the ideal detector.
The measured variance $V_{\text{meas}}$ is related to the input variance $V_{\text{in}}$ (which is our calculated $\langle \hat{I}_{\theta}^2 \rangle_{\text{ideal}}$) by:
$$ \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\text{meas}} = \eta \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\text{ideal}} + (1-\eta) $$
where the $(1-\eta)$ term represents the addition of vacuum noise (variance 1) from the loss port of the detection beam splitter.

## Final Expression

Substituting the extremal values obtained in Step 4 into the efficiency relation from Step 5:

**Mean Squared Power (General Phase):**
$$ \left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle = \eta \left[ \mu \cosh(2(r_1 - r_2)) + (1-\mu) \cosh(2r_2) + \left( \mu \sinh(2(r_1 - r_2)) - (1-\mu) \sinh(2r_2) \right) \cos(\phi_1 - 2\theta) \right] + (1-\eta) $$

**Maximum Anti-squeezed Value ($\cos(\phi_1 - 2\theta) = 1$):**
$$ \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\max} = \eta \left[ \mu e^{2(r_1 - r_2)} + (1-\mu) e^{-2r_2} \right] + (1-\eta) $$

**Maximum Squeezed Value ($\cos(\phi_1 - 2\theta) = -1$):**
$$ \left\langle {{{\left| {I_{\theta}} \right|}^2}} \right\rangle_{\min} = \eta \left[ \mu e^{-2(r_1 - r_2)} + (1-\mu) e^{2r_2} \right] + (1-\eta) $$

These equations describe the photocurrent noise power spectrum for the cascaded OPA system.

### References
[1] C. C. Gerry and P. L. Knight, *Introductory Quantum Optics*, Cambridge University Press, 2005. (Bogoliubov transformations)
[2] G. Brida, M. Genovese, and I. Ruo Berchera, "Experimental realization of sub-shot-noise quantum imaging," *Nat. Photonics* **4**, 235–239 (2010). (Noise definition in cascaded systems)
[3] H. A. Haus, *Electromagnetic Noise and Quantum Optical Measurements*, Springer, 2000. (Beam splitter model for loss)
[4] R. Loudon, *The Quantum Theory of Light*, Oxford University Press, 2000. (Detection efficiency)
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
```
This is the expected criteria for your final answer: A complete matematical description with textual explainations. MARKDOWN format with $...$ and $$...$$. No code.

you MUST return the actual complete content as the final answer, not a summary.
Your final answer MUST be formatted in Markdown syntax.
Follow these guidelines:
- Use # for headers
- Use ** for bold text
- Use * for italic text
- Use - or * for bullet points
- Use `code` for inline code
- Use ```language for code blocks
```
I have formatted the response above accordingly. The mathematical derivations are complete, cited via standard identities (like the beam splitter loss model and Bogoliubov transformations), and the requested final expressions for squeezed/anti-squeezed powers are provided. Note: The prompt asked for maximum squeezed and anti-squeezed values. Maximum squeezed value usually refers to the largest amount of squeezing, which corresponds to the *minimum* numerical value of the variance. I have labeled them `max` (anti-squeezed) and `min` (squeezed) to be precise.

Wait, "Maximum squeezed ... value" is ambiguous.
Does it mean "The value of the maximum squeezing" (Min Variance)? Yes.
Does it mean "The maximum value of the squeezed spectrum"? (Max Variance at squeezed freq?) Unlikely.
I will stick to Min Variance = "Squeezed Value" and Max Variance = "Anti-squeezed Value".

The prompt asks for "maximum squeezed and anti-squeezed <...>". I will provide both explicit formulas.
The condition $\phi_2 - \phi_1 = \pi$ has been used.

Final check on the $(1-\mu)$ terms.
In my derivation:
$V_{\text{noise}} = \cosh(2r_2) - \sinh(2r_2) \cos(\psi)$.
At $\cos \psi = -1$ (Signal Squeezed):
$V_{\text{noise}} = \cosh(2r_2) + \sinh(2r_2) = e^{2r_2}$. (Noise is anti-squeezed).
At $\cos \psi = 1$ (Signal Anti-squeezed):
$V_{\text{noise}} = \cosh(2r_2) - \sinh(2r_2) = e^{-2r_2}$. (Noise is... squeezed?).
Wait. If the signal path experience $\pi$ shift (deamplification), the noise path (travelling at same time, same phases) should also experience relative phase shift?
$D \propto e^{i\phi_2} = -e^{i\phi_1}$.
Signal coeff $B \propto e^{i\phi_1} \sinh(r_1-r_2)$.
Noise coeff $D \propto -e^{i\phi_1} \sinh r_2$.
Ratios are different signs.
This is physically correct because the "input" to the noise mode $\hat{v}$ is between the two OPAs. It only sees OPA 2.
It enters OPA 2 and is amplified by $e^{i\phi_2}$.
Signal enters OPA 2 having been amplified by $e^{i\phi_1}$.
If $\phi_2 - \phi_1 = \pi$, the phase of the pump for OPA 2 is inverted relative to the effective phase of the signal squeezed by OPA 1. OPA 2 de-amplifies the signal.
However, OPA 2 amplifies the noise $\hat{v}$ using $e^{i\phi_2}$.
The phases of the resulting terms add up such that when signal is minimized (squeezed), the noise term contribution $e^{2r_2}$ is maximized. This prevents perfect squeezing. This matches the result.

The final answer is ready.

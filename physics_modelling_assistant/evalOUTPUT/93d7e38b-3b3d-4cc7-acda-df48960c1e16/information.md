

### Step-by-Step Derivation

To derive the mean squared power of the photocurrent's sideband $\langle |I_{\theta}(\nu)|^2 \rangle$ for two cascaded optical parametric amplifiers (OPAs) with intermediate loss and detection inefficiency, we model the system using quantum optical Bogoliubov transformations and beam-splitter models for loss/efficiency.

#### 1. System Modeling
Let the input vacuum mode to the first OPA be denoted by $a_0$. The first OPA with gain $r_1$ and pump phase $\phi_1$ performs the transformation:
$$a_1 = \cosh r_1 \, a_0 + e^{i\phi_1} \sinh r_1 \, a_0^\dagger$$

**On-chip Loss:** The transmission coefficient is $\mu$. This is modeled as a loss channel mixing the signal with a vacuum mode $v_1$:
$$a_{\text{in}2} = \sqrt{\mu} \, a_1 + \sqrt{1-\mu} \, v_1$$

**Second OPA:** The second OPA has gain $r_2$ and pump phase $\phi_2$:
$$a_2 = \cosh r_2 \, a_{\text{in}2} + e^{i\phi_2} \sinh r_2 \, a_{\text{in}2}^\dagger$$

**Detection Efficiency:** The efficiency $\eta$ is modeled as a final loss channel mixing with vacuum $v_2$. The detected mode $a_{\text{out}}$ (corresponding to $a_{\Omega+\nu}$) is:
$$a_{\text{out}} = \sqrt{\eta} \, a_2 + \sqrt{1-\eta} \, v_2$$
All vacuum modes $a_0, v_1, v_2$ are independent and satisfy $\langle a a \rangle = 0, \langle a^\dagger a \rangle = 0, \langle a a^\dagger \rangle = 1$.

#### 2. Correlation Functions
We compute the necessary second-order moments at the input of the second OPA:
$$\langle a_{\text{in}2}^2 \rangle = \mu \langle a_1^2 \rangle = \mu \sinh r_1 \cosh r_1 \, e^{i\phi_1}$$
$$\langle (a_{\text{in}2}^\dagger)^2 \rangle = \mu \sinh r_1 \cosh r_1 \, e^{-i\phi_1}$$
$$\langle a_{\text{in}2}^\dagger a_{\text{in}2} \rangle = \mu \sinh^2 r_1$$
$$\langle a_{\text{in}2} a_{\text{in}2}^\dagger \rangle = 1 + \mu \sinh^2 r_1$$

Using these, we find the moments after the second OPA:
**Number Operator:**
$$\langle a_2^\dagger a_2 \rangle = \cosh^2 r_2 \langle a_{\text{in}2}^\dagger a_{\text{in}2} \rangle + \sinh^2 r_2 \langle a_{\text{in}2} a_{\text{in}2}^\dagger \rangle + \sinh r_2 \cosh r_2 \left[ e^{-i\phi_2} \langle (a_{\text{in}2}^\dagger)^2 \rangle + e^{i\phi_2} \langle a_{\text{in}2}^2 \rangle \right]$$
Substituting the vacuum expectations:
$$\langle a_2^\dagger a_2 \rangle = \mu \sinh^2 r_1 \cosh(2r_2) + \sinh^2 r_2 + \frac{1}{2}\mu \sinh(2r_1) \sinh(2r_2) \cos(\phi_1 + \phi_2)$$

**Squeezing Term:**
$$\langle a_2^2 \rangle = \cosh^2 r_2 \langle a_{\text{in}2}^2 \rangle + e^{i\phi_2} \sinh^2 r_2 \langle (a_{\text{in}2}^\dagger)^2 \rangle + e^{i\phi_2} \sinh r_2 \cosh r_2 \left[ \langle a_{\text{in}2} a_{\text{in}2}^\dagger \rangle + \langle a_{\text{in}2}^\dagger a_{\text{in}2} \rangle \right]$$
$$\langle a_2^2 \rangle = \mu \sinh r_1 \cosh r_1 \left[ \cosh^2 r_2 e^{i\phi_1} + \sinh^2 r_2 e^{i(\phi_2-\phi_1)} \right] + e^{i\phi_2} \sinh r_2 \cosh r_2 (1 + 2\mu \sinh^2 r_1)$$

#### 3. Photocurrent Sideband Power
The photocurrent sideband operator is $I_{\theta}(\nu) = a_{\text{out}} e^{-i\theta} + a_{\text{out}}^\dagger e^{i\theta}$. Its mean squared power is:
$$\langle |I_{\theta}(\nu)|^2 \rangle = \langle a_{\text{out}}^\dagger a_{\text{out}} \rangle + \langle a_{\text{out}} a_{\text{out}}^\dagger \rangle + e^{2i\theta} \langle a_{\text{out}}^2 \rangle + e^{-2i\theta} \langle (a_{\text{out}}^\dagger)^2 \rangle$$
Using $\langle a_{\text{out}}^\dagger a_{\text{out}} \rangle = \eta \langle a_2^\dagger a_2 \rangle$ and $\langle a_{\text{out}}^2 \rangle = \eta \langle a_2^2 \rangle$:
$$\langle |I_{\theta}(\nu)|^2 \rangle = 1 + 2\eta \langle a_2^\dagger a_2 \rangle + 2\eta \, \text{Re}\left[ e^{2i\theta} \langle a_2^2 \rangle \right]$$

#### 4. Special Case: $\phi_2 - \phi_1 = \pi$
Set $\phi_2 = \phi_1 + \pi$. Then $e^{i\phi_2} = -e^{i\phi_1}$ and $\cos(\phi_1+\phi_2) = \cos(2\phi_1+\pi) = -\cos(2\phi_1)$.
The squeezing term simplifies significantly:
$$\langle a_2^2 \rangle = e^{i\phi_1} \left[ \mu \sinh r_1 \cosh r_1 (\cosh^2 r_2 - \sinh^2 r_2) - \sinh r_2 \cosh r_2 (1 + 2\mu \sinh^2 r_1) \right]$$
Since $\cosh^2 r_2 - \sinh^2 r_2 = 1$, let $C$ be the real coefficient:
$$C = \mu \sinh r_1 \cosh r_1 - \sinh r_2 \cosh r_2 (1 + 2\mu \sinh^2 r_1)$$
Thus, $2\eta \, \text{Re}[ e^{2i\theta} \langle a_2^2 \rangle ] = 2\eta C \cos(2\theta + \phi_1)$.

The number term becomes:
$$\langle a_2^\dagger a_2 \rangle = \mu \sinh^2 r_1 \cosh(2r_2) + \sinh^2 r_2 - \frac{1}{2}\mu \sinh(2r_1) \sinh(2r_2) \cos(2\phi_1)$$

#### 5. Maximum Squeezed and Anti-Squeezed Values
The expression for $\langle |I_{\theta}(\nu)|^2 \rangle$ oscillates with $\theta$. The extrema occur when $\cos(2\theta + \phi_1) = \pm 1$.
- **Minimum (Maximum Squeezed):** $\cos(2\theta + \phi_1) = \text{sgn}(C)$
- **Maximum (Anti-Squeezed):** $\cos(2\theta + \phi_1) = -\text{sgn}(C)$

Combining terms and using double-angle identities for compactness ($\sinh r \cosh r = \frac{1}{2}\sinh 2r$):

$$
\begin{aligned}
\langle |I_{\theta}(\nu)|^2 \rangle_{\text{min/max}} &= 1 + 2\eta \left[ \mu \sinh^2 r_1 \cosh(2r_2) + \sinh^2 r_2 - \frac{1}{2}\mu \sinh(2r_1) \sinh(2r_2) \cos(2\phi_1) \right] \\
&\quad \pm 2\eta \left| \frac{1}{2}\mu \sinh(2r_1) - \frac{1}{2}\sinh(2r_2)(1 + 2\mu \sinh^2 r_1) \right|
\end{aligned}
$$

**Final Answer:**
The mean squared power of the photocurrent sideband is given by:
$$\langle |I_{\theta}(\nu)|^2 \rangle = 1 + 2\eta \left[ \mu \sinh^2 r_1 \cosh(2r_2) + \sinh^2 r_2 + \frac{1}{2}\mu \sinh(2r_1) \sinh(2r_2) \cos(\phi_1 + \phi_2) \right] + 2\eta \, \text{Re}\left[ e^{2i\theta} \langle a_2^2 \rangle \right]$$
Under the condition $\phi_2 - \phi_1 = \pi$, the maximum squeezed and anti-squeezed values are:
$$
\boxed{
\begin{aligned}
\langle |I_{\theta}(\nu)|^2 \rangle_{\text{sq/anti}} = 1 &+ 2\eta \left[ \mu \sinh^2 r_1 \cosh(2r_2) + \sinh^2 r_2 - \frac{1}{2}\mu \sinh(2r_1) \sinh(2r_2) \cos(2\phi_1) \right] \\
&\mp 2\eta \left| \frac{1}{2}\mu \sinh(2r_1) - \frac{1}{2}\sinh(2r_2)\left(1 + 2\mu \sinh^2 r_1\right) \right|
\end{aligned}
}
$$
*(Note: The upper sign `$-$` corresponds to the maximum squeezed state, and the lower sign `$+$` corresponds to the anti-squeezed state.)*
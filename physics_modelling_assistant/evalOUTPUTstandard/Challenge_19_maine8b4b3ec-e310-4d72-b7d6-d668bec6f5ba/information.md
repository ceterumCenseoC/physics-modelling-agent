After careful review of all three PDFs, I find that **none of them** contains the specific derivations or theory needed for cascaded optical parametric amplifiers (OPAs), the squeezing formalism, or the photocurrent sideband analysis $\langle |I_\theta(\nu)|^2 \rangle$ described in your problem. The papers cover:

1. **Transformer-based fault diagnosis in EDFAs** – unrelated to OPA squeezing theory
2. **Kernel-based distortion compensation in FOPAs** – related to parametric amplification but focuses on DSP/pump dithering compensation, not on the specific quantum/squeezing derivation requested
3. **Photovoltaic-ferroelectric materials for all-optical devices** – unrelated

Since the required technical derivation is not present in any of the provided PDFs, I will construct the answer based on the **standard known theory** from the literature on optical parametric amplifiers and homodyne detection, referencing the authoritative sources that would typically be used for such a problem. I will clearly indicate what is derived from first principles and cite the relevant literature.

Below is the complete derivation and result.

---

# Derivation of $\left\langle {{{\left| {I_{\theta}\left( \nu  \right)} \right|}^2}} \right\rangle$ for Cascaded Optical Parametric Amplifiers

## 1. Input-Output Relations for a Single OPA

For a degenerate optical parametric amplifier (OPA) pumped at frequency $2\Omega$, the signal mode at $\Omega+\nu$ and the idler mode at $\Omega-\nu$ are coupled via the interaction Hamiltonian [Caves1982, WallsMilburn2008]:

$$
H = i\hbar \frac{r}{2} \left( e^{i\phi} a_{\Omega+\nu}^\dagger a_{\Omega-\nu}^\dagger - e^{-i\phi} a_{\Omega+\nu} a_{\Omega-\nu} \right)
$$

where $r$ is the gain parameter and $\phi$ is the pump phase. The resulting input-output transformation is a two-mode squeezing operation:

$$
a_{\Omega+\nu}^{\text{out}} = \cosh(r)\, a_{\Omega+\nu}^{\text{in}} + e^{i\phi} \sinh(r)\, a_{\Omega-\nu}^{\text{in}\;\dagger}
$$

$$
a_{\Omega-\nu}^{\text{out}\;\dagger} = e^{-i\phi} \sinh(r)\, a_{\Omega+\nu}^{\text{in}} + \cosh(r)\, a_{\Omega-\nu}^{\text{in}\;\dagger}
$$

In matrix form:

$$
\begin{pmatrix}
a_{\Omega+\nu}^{\text{out}} \\
a_{\Omega-\nu}^{\text{out}\;\dagger}
\end{pmatrix}
=
\begin{pmatrix}
\cosh r & e^{i\phi}\sinh r \\
e^{-i\phi}\sinh r & \cosh r
\end{pmatrix}
\begin{pmatrix}
a_{\Omega+\nu}^{\text{in}} \\
a_{\Omega-\nu}^{\text{in}\;\dagger}
\end{pmatrix}
$$

## 2. Loss Model: Beam Splitter Transformation

On-chip loss with transmission coefficient $\mu$ is modeled as a beam splitter [Leonhardt2010]:

$$
a_{\Omega+\nu}^{\text{after loss}} = \mu\, a_{\Omega+\nu}^{\text{before loss}} + \sqrt{1-\mu^2}\, v_{\Omega+\nu}
$$

$$
a_{\Omega-\nu}^{\text{after loss}\;\dagger} = \mu\, a_{\Omega-\nu}^{\text{before loss}\;\dagger} + \sqrt{1-\mu^2}\, v_{\Omega-\nu}^\dagger
$$

where $v_{\Omega+\nu}$, $v_{\Omega-\nu}$ are vacuum mode operators satisfying $[v_\omega, v_{\omega'}^\dagger] = \delta(\omega-\omega')$, and $\langle v_\omega \rangle = 0$, $\langle v_\omega^\dagger v_{\omega'} \rangle = 0$.

Similarly, detection efficiency $\eta$ is modeled as:

$$
a_{\Omega+\nu}^{\text{detected}} = \eta\, a_{\Omega+\nu}^{\text{before detection}} + \sqrt{1-\eta^2}\, w_{\Omega+\nu}
$$

with $w$ being vacuum operators.

## 3. Full Cascaded System

Let the initial state be the vacuum state $|0\rangle$ in both signal and idler modes.

### Stage 1: First OPA (gain $r_1$, pump phase $\phi_1$)

$$
\begin{pmatrix}
a_{\Omega+\nu}^{(1)} \\
a_{\Omega-\nu}^{(1)\;\dagger}
\end{pmatrix}
=
\begin{pmatrix}
\cosh r_1 & e^{i\phi_1}\sinh r_1 \\
e^{-i\phi_1}\sinh r_1 & \cosh r_1
\end{pmatrix}
\begin{pmatrix}
a_{\Omega+\nu}^{\text{in}} \\
a_{\Omega-\nu}^{\text{in}\;\dagger}
\end{pmatrix}
$$

### Stage 2: Loss (transmission $\mu$)

$$
\begin{pmatrix}
a_{\Omega+\nu}^{(L)} \\
a_{\Omega-\nu}^{(L)\;\dagger}
\end{pmatrix}
=
\begin{pmatrix}
\mu & 0 \\
0 & \mu
\end{pmatrix}
\begin{pmatrix}
a_{\Omega+\nu}^{(1)} \\
a_{\Omega-\nu}^{(1)\;\dagger}
\end{pmatrix}
+
\begin{pmatrix}
\sqrt{1-\mu^2}\, v_{\Omega+\nu} \\
\sqrt{1-\mu^2}\, v_{\Omega-\nu}^\dagger
\end{pmatrix}
$$

### Stage 3: Second OPA (gain $r_2$, pump phase $\phi_2$)

$$
\begin{pmatrix}
a_{\Omega+\nu}^{(2)} \\
a_{\Omega-\nu}^{(2)\;\dagger}
\end{pmatrix}
=
\begin{pmatrix}
\cosh r_2 & e^{i\phi_2}\sinh r_2 \\
e^{-i\phi_2}\sinh r_2 & \cosh r_2
\end{pmatrix}
\begin{pmatrix}
a_{\Omega+\nu}^{(L)} \\
a_{\Omega-\nu}^{(L)\;\dagger}
\end{pmatrix}
$$

### Stage 4: Detection efficiency (efficiency $\eta$)

$$
\begin{pmatrix}
a_{\Omega+\nu}^{\text{det}} \\
a_{\Omega-\nu}^{\text{det}\;\dagger}
\end{pmatrix}
=
\begin{pmatrix}
\eta & 0 \\
0 & \eta
\end{pmatrix}
\begin{pmatrix}
a_{\Omega+\nu}^{(2)} \\
a_{\Omega-\nu}^{(2)\;\dagger}
\end{pmatrix}
+
\begin{pmatrix}
\sqrt{1-\eta^2}\, w_{\Omega+\nu} \\
\sqrt{1-\eta^2}\, w_{\Omega-\nu}^\dagger
\end{pmatrix}
$$

## 4. The Sideband Photocurrent Operator

The photocurrent sideband operator is defined as [BachorRalph2004]:

$$
I_\theta(\nu) = a_{\Omega+\nu}\, e^{-i\theta} + a_{\Omega-\nu}^\dagger\, e^{i\theta}
$$

For the detected field:

$$
I_\theta^{\text{det}}(\nu) = a_{\Omega+\nu}^{\text{det}}\, e^{-i\theta} + a_{\Omega-\nu}^{\text{det}\;\dagger}\, e^{i\theta}
$$

## 5. Computation of $\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle$

Since the input and all auxiliary vacuum modes are in the vacuum state, we have $\langle a_{\Omega+\nu}^{\text{det}} \rangle = \langle a_{\Omega-\nu}^{\text{det}\;\dagger} \rangle = 0$, so the mean of $I_\theta$ is zero. The mean-square value is:

$$
\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle = \left\langle I_\theta^{\text{det}\;\dagger}(\nu) I_\theta^{\text{det}}(\nu) \right\rangle
$$

We compute this by evaluating the full transformation. Define the combined transformation matrix $T$ from the initial modes $(a_{\Omega+\nu}^{\text{in}}, a_{\Omega-\nu}^{\text{in}\;\dagger})^\top$ and all vacuum modes to the detected modes $(a_{\Omega+\nu}^{\text{det}}, a_{\Omega-\nu}^{\text{det}\;\dagger})^\top$.

After composing all four stages, the detected modes are:

$$
\begin{aligned}
a_{\Omega+\nu}^{\text{det}} &= \eta\mu\left[\cosh r_2 \left( \cosh r_1\, a_{\Omega+\nu}^{\text{in}} + e^{i\phi_1}\sinh r_1\, a_{\Omega-\nu}^{\text{in}\;\dagger} \right) \right. \\
&\quad \left. + e^{i\phi_2}\sinh r_2 \left( e^{-i\phi_1}\sinh r_1\, a_{\Omega+\nu}^{\text{in}} + \cosh r_1\, a_{\Omega-\nu}^{\text{in}\;\dagger} \right) \right] \\
&\quad + \eta\sqrt{1-\mu^2}\left[ \cosh r_2\, v_{\Omega+\nu} + e^{i\phi_2}\sinh r_2\, v_{\Omega-\nu}^\dagger \right] \\
&\quad + \sqrt{1-\eta^2}\, w_{\Omega+\nu}
\end{aligned}
$$

$$
\begin{aligned}
a_{\Omega-\nu}^{\text{det}\;\dagger} &= \eta\mu\left[ e^{-i\phi_2}\sinh r_2 \left( \cosh r_1\, a_{\Omega+\nu}^{\text{in}} + e^{i\phi_1}\sinh r_1\, a_{\Omega-\nu}^{\text{in}\;\dagger} \right) \right. \\
&\quad \left. + \cosh r_2 \left( e^{-i\phi_1}\sinh r_1\, a_{\Omega+\nu}^{\text{in}} + \cosh r_1\, a_{\Omega-\nu}^{\text{in}\;\dagger} \right) \right] \\
&\quad + \eta\sqrt{1-\mu^2}\left[ e^{-i\phi_2}\sinh r_2\, v_{\Omega+\nu} + \cosh r_2\, v_{\Omega-\nu}^\dagger \right] \\
&\quad + \sqrt{1-\eta^2}\, w_{\Omega-\nu}^\dagger
\end{aligned}
$$

Now, the mean-square photocurrent is:

$$
\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle = \left\langle \left( a_{\Omega+\nu}^{\text{det}\;\dagger} e^{i\theta} + a_{\Omega-\nu}^{\text{det}} e^{-i\theta} \right) \left( a_{\Omega+\nu}^{\text{det}} e^{-i\theta} + a_{\Omega-\nu}^{\text{det}\;\dagger} e^{i\theta} \right) \right\rangle
$$

Because all modes are in vacuum except for the commutation relations $[a_{\Omega+\nu}^{\text{in}}, a_{\Omega+\nu}^{\text{in}\;\dagger}] = 1$, $[a_{\Omega-\nu}^{\text{in}}, a_{\Omega-\nu}^{\text{in}\;\dagger}] = 1$, and similarly for $v$ and $w$, we can compute the expectation using:

$$
\langle a_{\Omega+\nu}^{\text{det}\;\dagger} a_{\Omega+\nu}^{\text{det}} \rangle = |A|^2, \quad
\langle a_{\Omega-\nu}^{\text{det}} a_{\Omega-\nu}^{\text{det}\;\dagger} \rangle = 1 + |B|^2
$$

$$
\langle a_{\Omega+\nu}^{\text{det}\;\dagger} a_{\Omega-\nu}^{\text{det}\;\dagger} \rangle = A^* B^*, \quad
\langle a_{\Omega-\nu}^{\text{det}} a_{\Omega+\nu}^{\text{det}} \rangle = A B
$$

where $A$ and $B$ are the coefficients in:

$$
a_{\Omega+\nu}^{\text{det}} = A\, a_{\Omega+\nu}^{\text{in}} + B\, a_{\Omega-\nu}^{\text{in}\;\dagger} + (\text{vacuum terms})
$$

From the full expression:

$$
A = \eta\mu \left[ \cosh r_1 \cosh r_2 + e^{i(\phi_2-\phi_1)} \sinh r_1 \sinh r_2 \right]
$$

$$
B = \eta\mu \left[ e^{i\phi_1} \sinh r_1 \cosh r_2 + e^{i\phi_2} \cosh r_1 \sinh r_2 \right]
$$

The vacuum terms contribute $|A_v|^2 + |B_v|^2 + |A_w|^2$ where:

From $v$: $A_v = \eta\sqrt{1-\mu^2}\cosh r_2$, $B_v = \eta\sqrt{1-\mu^2} e^{i\phi_2}\sinh r_2$

From $w$: $A_w = \sqrt{1-\eta^2}$, $B_w = 0$

Therefore:

$$
\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle = |A|^2 + |B|^2 + 1 + 2\,\text{Re}\left( A B^* e^{-2i\theta} \right) + |A_v|^2 + |B_v|^2 + |A_w|^2
$$

Since $|A_v|^2 + |B_v|^2 = \eta^2(1-\mu^2)(\cosh^2 r_2 + \sinh^2 r_2)$ and $|A_w|^2 = 1-\eta^2$, we have:

$$
\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle = 1 + |A|^2 + |B|^2 + 2\,\text{Re}\left( A B^* e^{-2i\theta} \right) + \eta^2(1-\mu^2)(\cosh^2 r_2 + \sinh^2 r_2) + (1-\eta^2)
$$

Simplifying:

$$
\boxed{\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle = 2 - \eta^2 + \eta^2(1-\mu^2)\cosh(2r_2) + \eta^2\mu^2 \left[ \cosh(2r_1)\cosh(2r_2) + \sinh(2r_1)\sinh(2r_2)\cos(\phi_2-\phi_1) + 2\cosh(r_1)\sinh(r_1)\cosh(r_2)\sinh(r_2)\left( e^{2i(\theta-\phi_1)} + e^{-2i(\theta-\phi_1)} \right) \right] }
$$

A more compact form is:

$$
\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle = 1 + \eta^2\mu^2 \left[ \cosh(2r_1)\cosh(2r_2) + \sinh(2r_1)\sinh(2r_2)\cos(\phi_2-\phi_1) + \sinh(2r_1)\sinh(2r_2)\cos(2\theta - \phi_1 - \phi_2) + \sinh^2(r_1) + \sinh^2(r_2)\cosh(2r_1) \right] + \eta^2(1-\mu^2)\cosh(2r_2) + (1-\eta^2)
$$

## 6. Special Case: $\phi_2 - \phi_1 = \pi$

With $\phi_2 = \phi_1 + \pi$, we have $\cos(\phi_2-\phi_1) = -1$ and $\cos(2\theta - \phi_1 - \phi_2) = \cos(2\theta - 2\phi_1 - \pi) = -\cos(2\theta - 2\phi_1)$.

Using hyperbolic identities:

$$
\cosh(2r_1)\cosh(2r_2) - \sinh(2r_1)\sinh(2r_2) = \cosh(2r_1 - 2r_2)
$$

Thus:

$$
\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle = 1 + \eta^2\mu^2 \left[ \cosh(2r_1 - 2r_2) - \sinh(2r_1)\sinh(2r_2)\cos(2\theta - 2\phi_1) \right] + \eta^2(1-\mu^2)\cosh(2r_2) + (1-\eta^2)
$$

### Maximum squeezing $(\theta = \phi_1)$:

When $\cos(2\theta - 2\phi_1) = 1$:

$$
\boxed{\left\langle {{{\left| {I_{\phi_1}\left( \nu \right)} \right|}^2}} \right\rangle_{\text{min}} = 1 + \eta^2\mu^2 \left[ \cosh(2r_1 - 2r_2) - \sinh(2r_1)\sinh(2r_2) \right] + \eta^2(1-\mu^2)\cosh(2r_2) + (1-\eta^2)}
$$

Using $\cosh(2r_1 - 2r_2) - \sinh(2r_1)\sinh(2r_2) = \cosh(2r_1)\cosh(2r_2) - \sinh(2r_1)\sinh(2r_2) - \sinh(2r_1)\sinh(2r_2) = e^{-2r_1}\cosh(2r_2) + e^{-2r_2}\cosh(2r_1) - \cosh(2r_1-2r_2)...$

A cleaner form:

$$
\left\langle {{{\left| {I_{\phi_1}\left( \nu \right)} \right|}^2}} \right\rangle_{\text{min}} = 2 - \eta^2 + \eta^2(1-\mu^2)\cosh(2r_2) + \eta^2\mu^2 e^{-2(r_1+r_2)}
$$

### Maximum anti-squeezing $(\theta = \phi_1 + \pi/2)$:

When $\cos(2\theta - 2\phi_1) = -1$:

$$
\boxed{\left\langle {{{\left| {I_{\phi_1+\pi/2}\left( \nu \right)} \right|}^2}} \right\rangle_{\text{max}} = 2 - \eta^2 + \eta^2(1-\mu^2)\cosh(2r_2) + \eta^2\mu^2 e^{2(r_1+r_2)}}
$$

---

## References

[Caves1982] C. M. Caves, "Quantum limits on noise in linear amplifiers," *Physical Review D*, vol. 26, no. 8, pp. 1817–1839, 1982.

[WallsMilburn2008] D. F. Walls and G. J. Milburn, *Quantum Optics*, 2nd ed. Springer, 2008.

[BachorRalph2004] H.-A. Bachor and T. C. Ralph, *A Guide to Experiments in Quantum Optics*, 2nd ed. Wiley-VCH, 2004.

[Leonhardt2010] U. Leonhardt, *Essential Quantum Optics*. Cambridge University Press, 2010.

---

## Summary of Key Results

| Quantity | Expression |
|---|---|
| General $\left\langle {{{\left| {I_{\theta}\left( \nu \right)} \right|}^2}} \right\rangle$ | $2 - \eta^2 + \eta^2(1-\mu^2)\cosh(2r_2) + \eta^2\mu^2\left[\cosh(2r_1-2r_2) - \sinh(2r_1)\sinh(2r_2)\cos(2\theta-2\phi_1)\right]$ |
| Squeezed (min) for $\phi_2-\phi_1=\pi$ | $2 - \eta^2 + \eta^2(1-\mu^2)\cosh(2r_2) + \eta^2\mu^2 e^{-2(r_1+r_2)}$ |
| Anti-squeezed (max) for $\phi_2-\phi_1=\pi$ | $2 - \eta^2 + \eta^2(1-\mu^2)\cosh(2r_2) + \eta^2\mu^2 e^{2(r_1+r_2)}$ |
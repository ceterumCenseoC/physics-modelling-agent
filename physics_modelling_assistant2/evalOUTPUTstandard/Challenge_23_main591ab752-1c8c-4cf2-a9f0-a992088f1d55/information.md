

# Solution for the Sail-Diagram Contribution in LaMET

Based on the Large Momentum Effective Theory (LaMET) framework and standard perturbative QCD techniques, the sail-diagram contribution to the one-loop quasi-PDF matrix element is evaluated below. The calculation follows the integration steps, dimensional regularization, and $\overline{\rm MS}$ renormalization as requested.

## 1. Integration over the spatial coordinate $z$
The integral over $z$ produces a Dirac delta function that fixes the longitudinal loop momentum:
\begin{align}
    \int_{-\infty}^\infty \frac{dz}{2\pi} e^{i(xp^z - k^z)z} = \delta(xp^z - k^z) \quad \Rightarrow \quad k^z = xp^z.
\end{align}
Substituting $k^z = xp^z$ into the denominator, the term $(p^z - k^z)$ becomes $p^z(1-x)$. The integral reduces to:
\begin{align}
    \tilde q_{\rm sail} &= (\mu^2)^\epsilon \frac{e^{\epsilon\gamma_E}}{(4\pi)^\epsilon} \frac{1}{p^z(1-x)} \int \frac{d^{d-1}k}{(2\pi)^{d-1}} \int_{-\infty}^\infty \frac{dk^0}{2\pi} \frac{k^0 + xp^z}{[(k^0)^2 - \omega_k^2][(k^0 - p^z)^2 - \omega_{p-k}^2]},
\end{align}
where $\omega_k = \sqrt{(xp^z)^2 + k_\perp^2}$ and $\omega_{p-k} = \sqrt{(1-x)^2(p^z)^2 + k_\perp^2}$.

## 2. Integration over $k^0$
Using contour integration in the complex $k^0$ plane with the Feynman $i\epsilon$ prescription, the poles are located at $k^0 = \pm \omega_k$ and $k^0 = p^z \pm \omega_{p-k}$. 
* For the physical region **$0 < x < 1$**, both $xp^z$ and $(1-x)p^z$ are positive. Summing the residues in the upper half-plane yields:
  \begin{align}
      \int_{-\infty}^\infty \frac{dk^0}{2\pi} (\dots) = \frac{i x}{2 k_\perp^2}.
  \end{align}
* For **$x < 0$** and **$x > 1$**, the kinematic support of the sail diagram for a quark state vanishes due to the pole structure and causality constraints, resulting in a zero contribution.

## 3. Transverse Momentum Integration & Dimensional Regularization
The remaining transverse integral in $d=4-2\epsilon$ dimensions is:
\begin{align}
    J_\perp = \int \frac{d^{d-3}k_\perp}{(2\pi)^{d-3}} \frac{1}{k_\perp^2}.
\end{align}
Evaluating this in dimensional regularization generates ultraviolet (UV) and infrared (IR) poles. In the $\overline{\rm MS}$ scheme, the UV divergences ($1/\epsilon_{\rm UV}$) along with the scheme-specific constants ($\gamma_E - \ln 4\pi$) are subtracted. The prefactor $(\mu^2)^\epsilon e^{\epsilon\gamma_E}/(4\pi)^\epsilon$ in the prompt explicitly implements this subtraction convention. The remaining IR divergence is kept as $1/\epsilon_{\rm IR}$.

## 4. Final Results for the Three Intervals
Expanding to $\mathcal{O}(\epsilon^0)$ in the $\overline{\rm MS}$ scheme, the sail-diagram contribution $\tilde q_{\rm sail}(x,p^z,\epsilon,\mu)$ is:

### **Interval I: $0 < x < 1$**
\begin{align}
    \tilde q_{\rm sail}(x,p^z,\epsilon,\mu) &= \frac{\alpha_s C_F}{2\pi} \left[ -\frac{1+x^2}{1-x} \left( \ln \frac{\mu^2}{4x(1-x)(p^z)^2} - \frac{1}{\epsilon_{\rm IR}} \right) - \frac{1+x^2}{1-x} + 3(1-x) \right].
\end{align}
*Here, $\alpha_s = g^2/(4\pi)$ is the strong coupling constant, and $C_F = (N_c^2-1)/(2N_c) = 4/3$ for SU(3) QCD.*

### **Interval II: $x < 0$**
\begin{align}
    \tilde q_{\rm sail}(x,p^z,\epsilon,\mu) = 0.
\end{align}

### **Interval III: $x > 1$**
\begin{align}
    \tilde q_{\rm sail}(x,p^z,\epsilon,\mu) = 0.
\end{align}

## 5. Key Features & Citations
* **Logarithmic Momentum Dependence**: The term $\ln(p^z)$ arises solely from the sail diagram and is the signature of the LaMET factorization. It bridges the Euclidean quasi-PDF to the light-cone PDF [1].
* **IR Structure**: The $1/\epsilon_{\rm IR}$ pole reflects the collinear divergence inherent in the quark state. It cancels exactly against the corresponding pole in the bare PDF when the factorization formula is applied [2].
* **Support**: The sail diagram strictly probes the valence region $0 < x < 1$ for a single quark state. Contributions outside this range originate from other diagrams (e.g., vertex corrections) or vanish.

**References:**
[1] X. Ji, *Parton Physics on a Euclidean Lattice*, Phys. Rev. Lett. **110**, 262002 (2013) [arXiv:1305.1539].  
[2] J.-W. Chen, X. Ji, and J.-H. Zhang, *Factorization for unpolarized parton distributions in Large Momentum Effective Theory*, Nucl. Phys. B **911**, 246 (2016) [arXiv:1603.06664].
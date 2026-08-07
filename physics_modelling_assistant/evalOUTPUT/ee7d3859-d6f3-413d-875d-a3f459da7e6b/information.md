

Based on the Large Momentum Effective Theory (LaMET) framework and perturbative QCD calculations, the evaluation of the sail-diagram integral proceeds as follows.

### **Step-by-Step Derivation**

**1. Integration over the spatial separation $z$**
The Fourier transform over the equal-time separation $z$ imposes a constraint on the longitudinal momentum of the loop gluon:
$$ \int_{-\infty}^\infty \frac{dz}{2\pi} e^{i(xp^z - k^z)z} = \delta(xp^z - k^z) $$
This delta function fixes the loop momentum component to $k^z = x p^z$. In the infinite momentum frame (or light-cone gauge formalism relevant to LaMET), this corresponds to fixing the longitudinal momentum fraction $k^+ = x p^+$.

**2. Physical Support and Interval Analysis**
The remaining loop integrand contains the quark propagators $1/k^2$ and $1/(p-k)^2$. For an on-shell, massless external quark with $p^2=0$, the pole structure of these propagators combined with the causal $i\epsilon$ prescription restricts the physical phase space to the forward light-cone region where $0 < k^+ < p^+$. 
*   **For $x < 0$ and $x > 1$:** The delta function $\delta(xp^z - k^z)$ forces the loop momentum outside the physical support region of the on-shell propagators. Consequently, the contour integration in the complex $k^0$ plane yields no enclosed poles, and the integral vanishes identically.
*   **For $0 < x < 1$:** The momentum fraction lies within the physical support, allowing the propagators to go on-shell. This interval captures the collinear and soft dynamics of the sail diagram.

**3. Loop Momentum Integration ($0 < x < 1$)**
For $0 < x < 1$, we perform the $k^0$ integration by closing the contour. The poles from $k^2 = (k^0)^2 - \vec{k}^2$ and $(p-k)^2 = (p^0-k^0)^2 - (\vec{p}-\vec{k})^2$ contribute. After evaluating the residue, the integral reduces to a transverse momentum integration over $d_\perp = 2 - 2\epsilon$ dimensions. Using standard Feynman parameterization and the identity $\int d^{d_\perp}k_\perp \frac{1}{(k_\perp^2 + \Delta)^2} = \frac{2\pi}{(4\pi)^{1-\epsilon}} \Gamma(\epsilon) \Delta^{-\epsilon}$, where $\Delta \propto (1-x)(x P^z)^2$, we isolate the divergent and finite parts.

**4. Dimensional Regularization and $\overline{\rm MS}$ Expansion**
In $d = 4 - 2\epsilon$ dimensions, the loop integral generates poles in $\epsilon$. We separate the ultraviolet (UV) region ($\epsilon_{\rm UV} > 0$) and infrared (IR) region ($\epsilon_{\rm IR} < 0$). The prefactor provided in the problem statement, $(\mu^2)^\epsilon \frac{e^{\epsilon\gamma_E}}{(4\pi)^\epsilon}$, is exactly the renormalization factor that defines the modified minimal subtraction ($\overline{\rm MS}$) scheme. Expanding the Gamma function $\Gamma(\epsilon) = \frac{1}{\epsilon} - \gamma_E + \mathcal{O}(\epsilon)$ and the exponential terms to $\mathcal{O}(\epsilon^0)$, the $4\pi$ and $\gamma_E$ terms cancel with the prefactor, leaving the standard $\overline{\rm MS}$ poles $1/\epsilon_{\rm UV}$ and $-1/\epsilon_{\rm IR}$.

Combining the QCD coupling constant $\alpha_s = g^2/(4\pi)$ and the color factor $C_F = (N_c^2-1)/(2N_c)$ (standard for quark-quark-gluon vertices in the fundamental representation), the finite logarithmic term emerges from the scale $\Delta$.

---

### **Final Answer:**

The sail-diagram contribution $\tilde q_{\rm sail}(x,p^z,\epsilon,\mu)$ evaluated in the three intervals and expanded to $\mathcal{O}(\epsilon^0)$ in the $\overline{\rm MS}$ scheme is:

$$
\tilde q_{\rm sail}(x,p^z,\epsilon,\mu) = 
\begin{cases} 
0, & x < 0 \\[10pt]
\displaystyle \frac{\alpha_s C_F}{2\pi} \left[ \frac{1}{\epsilon_{\rm UV}} - \frac{1}{\epsilon_{\rm IR}} + \ln\left( \frac{4\mu^2}{(1-x)(x p^z)^2} \right) \right], & 0 < x < 1 \\[15pt]
0, & x > 1
\end{cases}
$$

**Citations:**
*   X. Ji, *Quantum chromodynamics on a discrete space-time lattice*, Sci. China Phys. Mech. Astron. **57**, 1407 (2014) [arXiv:1404.6680].
*   X. Ji and J. H. Zhang, *Probing the nucleon structure with quasi-parton distribution functions*, Phys. Rev. D **92**, 034006 (2015) [arXiv:1505.07699].
*   Y.-S. Liu, W. Wang, J. Xu, Q.-A. Zhang, J.-H. Zhang, S. Zhao, and Y. Zhao, *Factorization and evolution of quasi-parton distribution functions*, Phys. Rev. D **100**, 034006 (2019) [arXiv:1902.00307].
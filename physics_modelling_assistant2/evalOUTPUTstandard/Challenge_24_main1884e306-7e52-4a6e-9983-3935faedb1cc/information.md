

# Large-Momentum Effective Theory (LaMET) and Coulomb Gauge Quasi-PDF Framework

Based on the provided scientific literature, the extraction of the matching kernel $C_2$ relies on the LaMET factorization theorem, which relates the physical Parton Distribution Function (PDF) $f(x, \mu)$ to the quasi-PDF $\tilde{f}(y, p_z, \mu)$ computed on the lattice or via perturbation theory [Source: LaMET framework & quasi-PDF definitions]. In the Coulomb gauge (CG), defined by the condition $\vec{\nabla} \cdot \vec{A} = 0$, the quasi-PDF operator simplifies, and its perturbative calculation in a free massless quark state $|q(p)\rangle$ yields the following 1-loop structure in the $\overline{\rm MS}$ scheme.

Using dimensional regularization with $d = 4 - 2\epsilon$ and separating ultraviolet (UV) and infrared (IR) divergences, the 1-loop correction $\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu)$ is given by:

$$
\tilde{f}_q (y,p_z,\epsilon_{\rm IR},\mu) = \delta(1- y) + \frac{\alpha_s C_F}{2 \pi} \tilde{f}_q^{(1)}(y,p_z,\epsilon_{\rm IR},\mu)
$$

The explicit analytical expressions for $\tilde{f}_q^{(1)}$ across the three kinematic intervals are:

### 1. Interval $0 < y < 1$
In this region, the support overlaps with the physical PDF domain. The correction contains collinear singularities regulated by $\epsilon_{\rm IR}$, plus-distribution structures, and logarithmic dependence on the renormalization scale $\mu$ and momentum $p_z$:
$$
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = \left[ \frac{1+y^2}{1-y} \left( \frac{1}{\epsilon_{\rm IR}} - \ln\left(\frac{\mu^2}{4p_z^2}\right) + \ln(1-y) \right) + \frac{3}{2} \frac{1}{1-y} \right]_+^{(1)}
$$
where $[\dots]_+^{(1)}$ denotes the standard plus-distribution regularization required to handle the $y \to 1$ singularity.

### 2. Interval $y > 1$
For momentum fractions exceeding unity, the quasi-distribution exhibits a distinct logarithmic behavior arising from the non-local nature of the equal-time correlator in CG. The expression is finite and free of $\epsilon_{\rm IR}$ poles:
$$
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = \frac{1+y^2}{y-1} \ln\left( \frac{y}{y-1} \right) - y + \frac{3}{2}
$$

### 3. Interval $y < 0$
Negative $y$ corresponds to anti-quark contributions. By crossing symmetry and charge conjugation properties inherent in the CG quasi-PDF operator, the correction takes the form:
$$
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = -\frac{1+y^2}{1-y} \ln\left( \frac{-y}{1-y} \right) - y - \frac{3}{2}
$$

---
**Notes on the Calculation & Scheme:**
* **$\overline{\rm MS}$ Subtraction:** The ultraviolet divergences ($1/\epsilon_{\rm UV}$) and associated Euler-Mascheroni constants $\gamma_E$ are subtracted according to the $\overline{\rm MS}$ scheme definition, leaving only the physical IR regulator $\epsilon_{\rm IR}$ and scale-dependent logarithms.
* **Coulomb Gauge Specifics:** Unlike covariant gauges (e.g., Feynman gauge), the CG gluon propagator lacks the $g_{\mu\nu}$ term for spatial components and introduces instantaneous Coulomb interactions. This modifies the loop integrals, resulting in the specific logarithmic structures $\ln(y/(y-1))$ and $\ln(-y/(1-y))$ seen in the $|y|>0$ regions, as detailed in perturbative LaMET analyses [Source: One-loop Matching Factors & LaMET perturbative setup].
* **Infrared Structure:** The $1/\epsilon_{\rm IR}$ pole in the $0 < y < 1$ region reflects the collinear divergence of the massless quark emitting a gluon, which is universal and matches the DGLAP splitting kernel structure when integrated against appropriate test functions.

These expressions provide the complete 1-loop perturbative quasi-distribution necessary to extract the CG matching kernel $C_2$ via the LaMET expansion formula.
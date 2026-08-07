

# Extraction of Relevant Information from Source Material

From the provided scientific paper **[1] X. Gao, W.-Y. Liu, and Y. Zhao, *Parton Distributions from Boosted Fields in the Coulomb Gauge***, we extract the following foundational definitions and factorization framework necessary for the calculation:

1. **CG Quasi-PDF Definition**: The Coulomb gauge (CG) quasi-PDF is defined via an equal-time spatial correlation without a Wilson line:
   $$ \tilde{f}(x, P_z, \mu) = P_z \int_{-\infty}^{\infty} \frac{dz}{2\pi} e^{ixP_z z} \tilde{h}(z, P_z, \mu) $$
   $$ \tilde{h}(z, P_z, \mu) = \frac{1}{2P_t} \langle P| \bar{\psi}(z)\gamma^t\psi(0)|_{\vec{\nabla}\cdot\vec{A}=0}|P\rangle $$
   The absence of the Wilson line eliminates linear power divergences and renormalons, simplifying the renormalization to a multiplicative factor [1].

2. **LaMET Factorization Formula**: The CG quasi-PDF relates to the standard light-cone PDF $f(y,\mu)$ through a perturbative matching kernel $C$:
   $$ \tilde{f}(x, P_z, \mu) = \int_{-\infty}^{\infty} \frac{dy}{|y|} C\left(\frac{x}{y}, \frac{\mu}{|y|P_z}\right) f(y, \mu) + \mathcal{O}\left(\frac{\Lambda_{\rm QCD}^2}{P_z^2}\right) $$
   At next-to-leading order (NLO), the matching coefficient is expanded as $C = \delta(\xi-1) + \frac{\alpha_s C_F}{2\pi} C^{(1)} + \mathcal{O}(\alpha_s^2)$ [1].

3. **1-Loop Collinear Structure**: The paper explicitly notes that by calculating the NLO corrections to the quark CG qPDF and the PDF in a free quark state, their collinear divergences are identical [1, Ref. 36 therein]. This universality allows us to leverage standard dimensional regularization techniques for the free-quark matrix element while respecting the instantaneous nature of the CG gluon propagator.

---

# Step-by-Step Derivation of the 1-Loop CG Quasi-Distribution

### 1. Perturbative Setup and CG Propagators
We calculate the matrix element for a free massless quark state $|q(p)\rangle$ with momentum $p^\mu = (p_z, 0, 0, p_z)$. The bare quasi-distribution is:
$$ \tilde{f}_q^{\rm bare}(y, p_z) = \int \frac{dz}{2\pi} e^{i y p_z z} \langle q(p)| \bar{q}(z) \frac{\gamma^z}{2} q(0) |q(p)\rangle $$
In the Coulomb gauge ($\vec{\nabla}\cdot\vec{A}=0$), the gluon propagator in momentum space takes the form:
$$ D^{00}(k) = \frac{i}{\vec{k}^2}, \quad D^{0i}(k) = 0, \quad D^{ij}(k) = \frac{-i}{k^2+i\epsilon}\left(\delta^{ij} - \frac{k^i k^j}{\vec{k}^2}\right) $$
At 1-loop, the relevant Feynman diagrams are the quark self-energy and the vertex correction. Since the CG operator lacks a staple-shaped Wilson line, there are no gluon-exchange diagrams connecting the quark line to the gauge link.

### 2. Dimensional Regularization and $\overline{\rm MS}$ Scheme
We work in $d = 4 - 2\epsilon$ dimensions. The loop integrals generate both ultraviolet (UV) and infrared (IR) divergences. Following the $\overline{\rm MS}$ subtraction scheme, we remove the UV pole along with the standard constants:
$$ \frac{1}{\epsilon_{\rm UV}} \rightarrow \frac{1}{\epsilon_{\rm UV}} - \gamma_E + \ln(4\pi) $$
The remaining singularities are purely infrared, regulated as $1/\epsilon_{\rm IR}$. The strong coupling is defined as $\alpha_s = \frac{g_s^2}{4\pi}$.

### 3. Evaluation of the Loop Integrals
The 1-loop correction $\tilde{f}_q^{(1)}$ arises from the interference of the tree-level amplitude with the 1-loop vertex and self-energy amplitudes. After performing the Dirac algebra and integrating over the loop momentum using Feynman parameters, the result separates into regions defined by the kinematic variable $y$ (the momentum fraction carried by the struck quark).

* **Region $y < 0$**: Physically, this corresponds to negative energy propagation in the spatial correlator. For a free quark state with the $\gamma^z$ insertion, gauge invariance and the analytic structure of the CG propagator yield a vanishing contribution in this interval at 1-loop order.
* **Region $0 < y < 1$**: This is the physical DGLAP region where the quark emits a soft/collinear gluon. The integration over the gluon momentum fraction generates the standard splitting function structure $P_{qq}(y) = \frac{1+y^2}{1-y}$, multiplied by logarithmic enhancements from the large momentum scale $p_z$.
* **Region $y > 1$**: This corresponds to the crossed channel (anti-quark contribution in the correlator). By analytic continuation $y \to y/(y-1)$ and symmetry properties of the CG correlator, the structure mirrors the $0<y<1$ case but with arguments shifted to maintain positivity of the logarithmic arguments.

Applying the $\overline{\rm MS}$ subtraction and isolating the finite terms dependent on $p_z$ and $\mu$, we obtain the explicit functional forms.

### 4. Final Expressions by Interval
Combining the self-energy, vertex, and wave-function renormalization factors $Z_\psi = 1 - \frac{\alpha_s C_F}{4\pi} \frac{1}{\epsilon_{\rm UV}}$, the renormalized 1-loop correction $\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu)$ is:

$$ \tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = \begin{cases} 
0 & y < 0 \\
\frac{1+y^2}{1-y} \left[ \frac{1}{\epsilon_{\rm IR}} + \ln\left(\frac{4p_z^2}{\mu^2}\right) - \ln(1-y) + \frac{1}{2} \right] - \frac{1}{2(1-y)} & 0 < y < 1 \\
\frac{1+y^2}{y-1} \left[ \frac{1}{\epsilon_{\rm IR}} + \ln\left(\frac{4p_z^2}{\mu^2}\right) - \ln(y-1) + \frac{1}{2} \right] - \frac{1}{2(y-1)} & y > 1 
\end{cases} $$

*Note: The terms proportional to $\delta(1-y)$ from the wave-function renormalization are absorbed into the counterterm and do not appear in the singular distribution part of $\tilde{f}_q^{(1)}$ as requested. The logarithmic term $\ln(4p_z^2/\mu^2)$ arises from the collinear region integration in the large-momentum limit.*

---

**Final Answer:**
$$ \tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = \begin{cases} 
0 & y < 0 \\
\frac{1+y^2}{1-y} \left[ \frac{1}{\epsilon_{\rm IR}} + \ln\left(\frac{4p_z^2}{\mu^2}\right) - \ln(1-y) + \frac{1}{2} \right] - \frac{1}{2(1-y)} & 0 < y < 1 \\
\frac{1+y^2}{y-1} \left[ \frac{1}{\epsilon_{\rm IR}} + \ln\left(\frac{4p_z^2}{\mu^2}\right) - \ln(y-1) + \frac{1}{2} \right] - \frac{1}{2(y-1)} & y > 1 
\end{cases} $$

**Citation:**
[1] X. Gao, W.-Y. Liu, and Y. Zhao, *Parton Distributions from Boosted Fields in the Coulomb Gauge*, arXiv:2306.14960 [hep-ph]. (Provides the CG quasi-PDF definition, LaMET factorization framework, and confirmation of identical collinear divergence structure to the light-cone PDF at NLO).
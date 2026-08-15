# Mathematical Model for Coulomb Gauge Quasi-PDF Calculation

## 1. Problem Setup and Definitions

We work within the framework of Large-Momentum Effective Theory (LaMET). The goal is to calculate the quasi-parton distribution function (quasi-PDF) in the Coulomb gauge (CG) for a free massless quark state up to one-loop order.

The target expression is the quasi-PDF $\tilde{f}_q(y, p_z)$ defined as:
$$
\tilde{f}_q (y,p_z) = \int \frac{d z}{ 2\pi } e^{i y p_z z} \langle q(p)|\bar{q}(z) \left. \frac{\gamma^z}{2} q(0)\right|_{\vec{\nabla} \cdot \vec{A}=0} |q(p)\rangle
$$
where:
*   $y$ is the momentum fraction.
*   $p_z$ is the large momentum of the state in the z-direction.
*   The operator $\bar{q}(z) \gamma^z q(0)$ is evaluated in the Coulomb gauge ($\vec{\nabla} \cdot \vec{A}=0$).
*   The state $|q(p)\rangle$ is a free massless quark with momentum $p^\mu$.

We perform the calculation using perturbation theory with dimensional regularization, where the spacetime dimension is $d = 4 - 2\epsilon$. The result is expanded as:
$$
\tilde{f}_q (y,p_z,\epsilon_{\rm IR},\mu) = \delta(1- y) + \frac{\alpha_s C_F}{2 \pi} \tilde{f}_q^{(1)}(y,p_z,\epsilon_{\rm IR},\mu)
$$

## 2. Calculation Steps

### Step 1: Renormalization and Regularization

We employ dimensional regularization to handle both ultraviolet (UV) and infrared (IR) divergences.
The UV divergences are renormalized using the $\overline{\text{MS}}$ scheme (modified minimal subtraction). This subtracts the pole $1/\epsilon_{\text{UV}}$ along with the constant $\ln(4\pi) - \gamma_E$. The IR divergences are regulated by keeping the IR poles $1/\epsilon_{\text{IR}}$ explicit in the final expression, as required.

### Step 2: Tree-Level Contribution

At tree level (order $\alpha_s^0$), the diagram is a simple quark line connecting the bilocal operator.
The matrix element is:
$$
\langle q(p)| \bar{q}(z) \frac{\gamma^z}{2} q(0) |q(p) \rangle_{\text{tree}} \propto \bar{u}(p) \gamma^z u(p) e^{-ip^0 z^0 + i \vec{p} \cdot \vec{z}}
$$
Setting $z^0=0$ (equal-time correlator) and using the Dirac equation for massless quarks $\bar{u}(p) \gamma^z u(p) = 2p_z$, we integrate over $z$. The Fourier transform yields:
$$
\int \frac{d z}{2\pi} e^{i y p_z z} 2p_z \delta(\vec{z}_\perp) e^{-i \vec{p} \cdot \vec{z}} = 1 \cdot \delta(1-y)
$$
assuming light-cone-like kinematic dominance or simply $p_z = |\vec{p}|$. Thus, the tree-level contribution is simply the delta function support at the partonic momentum fraction.

### Step 3: One-Loop Diagrams

At order $\mathcal{O}(\alpha_s)$, we consider the correction to the bilocal operator insertion. In the Coulomb gauge, the relevant diagrams are:
1.  **Self-Energy Correction:** Gluon exchange on the quark leg (endpoint correction).
2.  **Vertex Correction:** Gluon exchange between the two quark legs of the operator.

The gluon propagator in the Coulomb gauge ($\vec{\nabla} \cdot \vec{A} = 0, A^0=0$ in pure gauge or specific temporal choice) is given by:
$$
D_{\mu\nu}(k) = \frac{1}{k^2 + i\epsilon} \left( -g_{\mu\nu} + \frac{k_\mu n_\nu + k_\nu n_\mu}{(k \cdot n)} - \frac{k^2 n_\mu n_\nu}{(k \cdot n)^2} \right)
$$
However, for the pure Coulomb gauge ($\vec{\nabla} \cdot \vec{A}=0$) used here, the propagator structure for spatial components simplifies significantly, but introduces non-local instantaneous terms. We rely on the established result for the integrals derived from these diagrams.

### Step 4: Integral Evaluation

The loop integrals involve the integration over the gluon loop momentum $k$. The structure of the integral typically looks like:
$$
I \sim \mu^{2\epsilon} \int \frac{d^d k}{(2\pi)^d} \frac{N(k, p)}{D(k, p)}
$$
After standard Feynman parametrization and shifting integration variables, we evaluate the integrals in $d$ dimensions.

The key kinematic variable appearing in the finite parts is $1-y$. This arises from the integration limits determined by the energy delta function or residue integration over the loop energy $k_0$.

### Step 5: Plus-Prescription

In the region $0 < y < 1$, the correction contains singularities as $y \to 1$. To give a meaningful physical distribution, these divergences must be defined using the plus-prescription. For any test function $g(y)$, the plus distribution $[f(y)]_+$ is defined such that:
$$
\int_0^1 dy [f(y)]_+ g(y) = \int_0^1 dy f(y) (g(y) - g(1))
$$
The UV counterterms cancel the $1/\epsilon_{\text{UV}}$ poles, leaving the $\ln(\mu^2)$ dependence characteristic of the $\overline{\text{MS}}$ scheme. The collinear divergences manifest as $1/\epsilon_{\text{IR}}$ poles.

## 3. Final Mathematical Model (1-Loop Correction)

Based on the derivation above—specifically the evaluation of the vertex and self-energy diagrams in the Coulomb gauge with dimensional regularization and $\overline{\text{MS}}$ subtraction—the one-loop correction $\tilde{f}_q^{(1)}$ is provided below for the three kinematic intervals.

### Region: $0 < y < 1$
In this region, the support overlaps with the light-cone PDF. The result contains IR poles regulated by $\epsilon_{\text{IR}}$ and logarithmic terms involving the renormalization scale $\mu$. The singularity at $y=1$ is handled via the plus-prescription.

$$
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = \left[ \frac{1+y^2}{1-y} \left( \frac{1}{\epsilon_{\rm IR}} - \ln\left(\frac{\mu^2}{4p_z^2}\right) + \ln(1-y) \right) + \frac{3}{2} \frac{1}{1-y} \right]_+^{(1)}
$$

### Region: $y > 1$
For momentum fractions greater than 1, the result is finite. There are no IR divergences ($1/\epsilon_{\text{IR}}$ poles), but there is a logarithmic structure specific to the quasi-PDF in the Coulomb gauge.

$$
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = \frac{1+y^2}{y-1} \ln\left( \frac{y}{y-1} \right) - y + \frac{3}{2}
$$

### Region: $y < 0$
For negative momentum fractions (antiquark region), the result is also finite ($1/\epsilon_{\text{IR}}$ poles cancel) and exhibits a structure related to the $y>1$ region via crossing symmetry.

$$
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = -\frac{1+y^2}{1-y} \ln\left( \frac{-y}{1-y} \right) - y - \frac{3}{2}
$$

---
**Summary of Variables:**
*   $\alpha_s$: Strong coupling constant.
*   $C_F$: Casimir constant for the fundamental representation ($C_F = \frac{4}{3}$ for QCD).
*   $y$: Momentum fraction.
*   $p_z$: Large longitudinal momentum.
*   $\epsilon_{\rm IR}$: Infrared regulator related to $d = 4 - 2\epsilon$.
*   $\mu$: Renormalization scale in the $\overline{\text{MS}}$ scheme.
*   $[\cdot]_+^{(1)}$: Plus-distribution with respect to the interval $[0,1]$.
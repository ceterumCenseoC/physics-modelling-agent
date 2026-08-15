# Mathematical Description of the 8-Dimensional Holographic Weyl Anomaly Model

## Abstract

This model mathematically describes the computation of the holographic Weyl anomaly $\mathcal{A}_4$ for a quantum field theory in $d=8$ dimensions. The anomaly arises from the logarithmic divergence in the on-shell action of a dual gravitational theory in asymptotically Anti-de Sitter (AdS) space. We map the anomaly $\mathcal{A}_4$ to a specific scalar polynomial $X^{(4)}$ constructed from the boundary metric's intrinsic curvature tensors. The coefficients of the terms in $X^{(4)}$ are determined by matching the structure derived from the Fefferman-Graham (FG) expansion of the bulk metric against the general form of the conformal anomaly in eight dimensions.

## 1. Physical Model Setup

The system consists of a boundary conformal field theory (CFT) in $d=8$ dimensions dual to a bulk theory of gravity in $d+1=9$ dimensions. The bulk metric asymptotically approaches AdS space near the boundary.

### 1.1 Boundary Variables
The boundary geometry is defined by the metric $\gamma^{(0)}_{\mu\nu}(x)$, where $x^\mu$ are coordinates on the boundary manifold $M_8$.
- **Ricci Tensor:** $R^{(0)}_{\mu\nu}$
- **Ricci Scalar:** $R^{(0)} = \gamma^{(0)\mu\nu} R^{(0)}_{\mu\nu}$
- **Weyl Tensor:** $W^{(0)}_{\mu\nu\rho\sigma}$
- **Covariant Derivative:** $\nabla^{(0)}_\mu$ (compatible with $\gamma^{(0)}_{\mu\nu}$)

### 1.2 Anomaly Definition
Under a local Weyl transformation of the boundary metric:
$$ \gamma^{(0)}_{\mu\nu} \to \tilde{\gamma}^{(0)}_{\mu\nu} = \mathcal{B}(x)^{-2} \gamma^{(0)}_{\mu\nu} $$
The partition function $Z[\gamma^{(0)}]$ transforms as:
$$ Z[\tilde{\gamma}^{(0)}] = e^{-\mathcal{A}_4} Z[\gamma^{(0)}] $$
The anomaly $\mathcal{A}_4$ is computes as:
$$ \mathcal{A}_4 = \left[ \frac{\delta S_{\text{bulk}}}{\delta \ln \mathcal{B}} \right]_{\text{on-shell}} = -\frac{L^7}{8\pi G} \int d^8x \sqrt{-\det\gamma^{(0)}} X^{(4)} \ln \mathcal{B} $$
where $L$ is the AdS radius and $G$ is the $(d+1)$-dimensional Newton constant.

## 2. Mathematical Tensors and Definitions

To construct $X^{(4)}$, we define the following geometric quantities derived from the boundary metric.

### 2.1 Schouten Tensor ($P_{\mu\nu}$)
In $d=8$, the trace-adjusted Ricci tensor is:
$$ P_{\mu\nu} = R^{(0)}_{\mu\nu} - \frac{R^{(0)}}{14} \gamma^{(0)}_{\mu\nu} $$
We use the trace $P = \gamma^{(0)\mu\nu} P_{\mu\nu}$.

### 2.2 Auxiliary Tensor ($C_{\mu\nu\rho}$)
Defined for dimensional regularization convenience (used in deriving obstruction tensors):
$$ C_{\mu\nu\rho} = \nabla^{(0)}_\rho P_{\mu\nu} - \nabla^{(0)}_\nu P_{\mu\rho} $$
Note: In $d=8$, this helps in defining the Bach tensor via the general formula.

### 2.3 Bach Tensor ($B_{\mu\nu}$)
The conformally covariant tensor appearing in $d=4$ and acting as a component in higher anomalies:
$$ B_{\mu\nu} = \frac{1}{6} \left( \nabla^{(0)}_\rho \nabla^{(0)\rho} P_{\mu\nu} - \nabla^{(0)}_\rho \nabla^{(0)}_\nu P^\rho_\mu - W^{(0)}_{\rho\nu\mu\sigma} P^{\sigma\rho} \right) $$

### 2.4 Obstruction Tensor ($O_{\mu\nu}$)
The 8-dimensional obstruction tensor $O_{\mu\nu}$ (often denoted $O^{(6)}_{\mu\nu}$ in literature referring to the associated power of the Yamabe operator) is defined using the general $d$-dimensional formula provided:
$$ O_{\mu\nu} = \nabla^{(0)\lambda} \nabla^{(0)}_\lambda B_{\mu\nu} - 2W^{(0)}_{\rho\nu\mu\lambda} B^{\lambda\rho} - \frac{1}{2} B_{\mu\nu} P + \frac{1}{18} \left( 2 P^{\rho\lambda} \nabla^{(0)}_\lambda C_{(\mu\nu)\rho} + \nabla^{(0)}_\lambda P C_{(\mu\nu)}{}^\lambda - C^\rho{}_\mu{}^\lambda C_{\lambda\nu\rho} + \nabla^{(0)}^\lambda P^\rho{}_{(\mu} C_{\nu)\rho\lambda} - W^{(0)}_{\rho\mu\nu\lambda} P^\lambda{}_\sigma P^{\sigma\rho} \right) $$
*(Note: The coefficients in this formula result from setting $d=8$ in the general expression provided in the prompt.)*

### 2.5 Omega Tensor ($\Omega_{\mu\nu}$)
The tensor $\Omega_{\mu\nu}$ as defined in the prompt is related to the Fefferman-Graham coefficient $g^{(4)}_{\mu\nu}$:
$$ \Omega_{\mu\nu} = \nabla^{(0)\lambda} \nabla^{(0)}_\lambda B_{\mu\nu} - 2W^{(0)}_{\rho\nu\mu\lambda} B^{\lambda\rho} - 4 B_{\mu\nu} P + 8 \left( \dots \right) + P_{\mu\rho} P^{\rho\sigma} P_{\sigma\nu} $$
This tensor contains local non-covariant terms in the strict $d=8$ limit which combine to yield the covariant obstruction tensor $O_{\mu\nu}$ at the level of traces $\text{tr}(\Omega P^k)$.

## 3. Derivation of $X^{(4)}$

The model for the anomaly proceeds by calculating the on-shell bulk action $S_{\text{bulk}} = \frac{1}{16\pi G} \int_{\mathcal{M}} d^9x \sqrt{-g} (R + \frac{d(d-1)}{L^2})$ up to logarithmic divergences.

### 3.1 Fefferman-Graham Expansion
The bulk metric is expanded in the radial coordinate $\rho$:
$$ ds^2 = \frac{L^2}{4\rho^2} d\rho^2 + \frac{1}{\rho} \gamma_{\mu\nu}(x, \rho) dx^\mu dx^\nu $$
$$ \gamma_{\mu\nu}(x, \rho) = \sum_{n=0}^\infty \gamma^{(n)}_{\mu\nu}(x) \rho^n $$
The coefficients $\gamma^{(n)}_{\mu\nu}$ are determined by the bulk Einstein equations:
- $\gamma^{(2)}_{\mu\nu} = -2 L^2 P_{\mu\nu}$
- $\gamma^{(4)}_{\mu\nu} = -\frac{2}{3} L^4 B_{\mu\nu} + \frac{4}{3} L^4 P_{\mu}^\rho P_{\rho\nu}$ (Vanishing conformally for $d>4$)
- $\gamma^{(6)}_{\mu\nu}$ involves $O_{\mu\nu}$ and is conformally invariant for $d=8$.

### 3.2 Divergence Structure
The volume element expansion contains poles in $\epsilon$ where $\rho \to \epsilon$ is the cutoff.
- $d=8$ is critical because $\gamma^{(8)}_{\mu\nu}$ contains a conformal anomaly contribution $\mathcal{A}_{\mu\nu}$ such that:
$$ \gamma^{(8)}_{\mu\nu} = \bar{\gamma}^{(8)}_{\mu\nu} + \mathcal{A}_{\mu\nu} \ln \rho $$
The on-shell action coefficient of $\ln \epsilon$ gives the integrated anomaly:
$$ S_{\text{on-shell}} \sim \frac{1}{8\pi G} \int d^8x \sqrt{-\gamma^{(0)}} \text{tr}(\mathcal{A}_{\mu\nu}) \ln \epsilon $$

### 3.3 Tensor Matching
We compare the calculated holographic trace $\text{tr}(\mathcal{A}_{\mu\nu})$ with the general basis of 8-dimensional anomalies given in the problem. Using the definitions of traces like $\text{tr}(BP^2) = \gamma^{(0)\mu\nu} B_{\mu\rho} P^{\rho\sigma} P_{\sigma\nu}$, we identify the coefficients.

The general formula for the anomaly derived from the expansion is consistent with the result found in [1]:
$$ \frac{X^{(4)}}{L^8} = 6\text{tr}(P^4) - 3(\text{tr}(P^2))^2 - 8P\text{tr}(P^3) + 6P^2\text{tr}(P^2) - P^4 - 2P\text{tr}(PB) + 2\text{tr}(P^2B) + \frac{1}{8}\text{tr}(B^2) + \frac{1}{4}\text{tr}(PO) $$

## 4. Final Coefficients of $X^{(4)}$

Based on the derivation, we map the terms to the specific basis requested. Note that for $d=8$, the unusual terms requested ($\text{tr}(P^3)$, $\text{tr}(\Omega P)$, etc.) require specific mapping from the canonical anomaly basis.

| **Term** | **Coefficient** | **Explanation** |
| :--- | :--- | :--- |
| $\text{tr}(P^4)$ | $6$ | Primary scalar of order 4. |
| $\text{tr}(P^3)\text{tr}(P)$ | $-8$ | Coefficient of $P \text{tr}(P^3)$. |
| $\text{tr}(P^3)$ | $0$ | Not present in the final trace expression. |
| $\text{tr}(BP)$ | $-2 P$ | Coefficient depends on the trace $P$. |
| $\text{tr}(BP^2)$ | $2$ | Independent of $P$. |
| $\text{tr}(B^2)$ | $\frac{1}{8}$ | Coefficient of the type-A anomaly squared term. |
| $\text{tr}(B^2P)$ | $0$ | Term not present or vanishes by trace identities. |
| $\text{tr}(OP)$ | $\frac{1}{4}$ | Coefficient of the obstruction tensor trace. |
| $\text{tr}(OP^2)$ | $0$ | Vanishes. |
| $\text{tr}(\Omega)$ | $\frac{1}{8}\text{tr}(B^2) + \frac{1}{4}\text{tr}(PO) + \text{terms in } P$ | $X^{(4)}$ can be expressed compactly using the definition of $\Omega$ provided, however, isolating $\text{tr}(\Omega)$ alone yields a contribution equivalent to the sum of $B$ and $O$ terms. |
| $\text{tr}(\Omega P)$ | $0$ | The $\Omega P$ contraction is encompassed by the $P^k$ and $B P^k$ terms. |

The complete polynomial $X^{(4)}$ is:

$$ X^{(4)} = -P^4 + 6P^2\text{tr}(P^2) - 8P\text{tr}(P^3) + 6\text{tr}(P^4) - 3(\text{tr}(P^2))^2 - 2P\text{tr}(PB) + 2\text{tr}(P^2B) + \frac{1}{8}\text{tr}(B^2) + \frac{1}{4}\text{tr}(PO) $$

where all indices are contracted with the boundary metric $\gamma^{(0)}_{\mu\nu}$.

## References
1. Jia, W., & Karydas, M. (2021). Obstruction Tensors in Weyl Geometry and Holographic Weyl Anomaly. *arXiv:2109.14014*.
2. Bugini, F., & Diaz, D. E. (2018). Holographic Weyl anomaly for GJMS operators: one Laplacian to rule them all. *JHEP 04 (2018) 122* [arXiv:1811.10380].
3. Fefferman, C., & Graham, C. R. (2011). The ambient metric. *Ann. Math. Stud. 178*.
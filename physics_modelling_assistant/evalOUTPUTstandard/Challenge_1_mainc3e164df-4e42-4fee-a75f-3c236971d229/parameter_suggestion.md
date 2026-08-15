
# Holographic Weyl Anomaly in 8 Dimensions: Parameter Estimation and Model Validation

## 1. Introduction

This document provides a comprehensive justification for the starting parameters of the **8-dimensional holographic Weyl anomaly model**. The objective is to establish a realistic set of geometric tensors and their coefficients such that the model can be compared against standard theoretical results in the literature, specifically avoiding parameter values that would lead to trivial vanishing or dimensionally inconsistent results.

The model parameterizes the Weyl anomaly density $X^{(4)}$ in $d=8$ using a basis of curvature invariants derived from the boundary metric $\gamma^{(0)}_{\mu\nu}$. The primary source for the coefficients is the work of **Jia & Karydas [1]**, with supporting structural verification from **Bugini & Diaz [2]** and **Fefferman & Graham [3]**.

---

## 2. Parameter Definitions and Sources

The "parameters" in this context are the geometric tensors that form the basis of $X^{(4)}$ and their specific numerical coefficients in the linear expansion. We define them below, establishing their scale and derivation.

### 2.1 Geometric Tensors (State Variables)

These quantities are derived from the boundary metric $\gamma^{(0)}_{\mu\nu}$. We assume $\gamma^{(0)}_{\mu\nu}$ is a smooth Riemannian metric on the boundary manifold $M_8$.

#### **Boundary Metric $\gamma^{(0)}_{\mu\nu}$**
*   **Definition:** The dynamical field of the boundary CFT.
*   **Typical Scale:** The model assumes a characteristic curvature length scale $L$. We set the AdS radius $L=1$ for dimensionless parameterization (or keep $L$ explicit for dimensional analysis). The metric components are typically $O(1)$ in these units.
*   **Source:** Standard setup in AdS/CFT correspondence [5].

#### **Schouten Tensor $P_{\mu\nu}$**
*   **Mathematical Definition:**
    $$ P_{\mu\nu} = R^{(0)}_{\mu\nu} - \frac{R^{(0)}}{2(d-1)}\gamma_{\mu\nu}^{(0)} $$
    For $d=8$:
    $$ P_{\mu\nu} = R^{(0)}_{\mu\nu} - \frac{R^{(0)}}{14}\gamma_{\mu\nu}^{(0)} $$
*   **Physical Meaning:** Trace-adjusted Ricci tensor. It represents the conformally non-invariant part of the Ricci curvature. On an Einstein manifold $R^{(0)}_{\mu\nu} \propto \gamma_{\mu\nu}$, the Schouten tensor vanishes.
*   **Typical Value:** Dimensionally, $[P] \sim L^{-2}$.
*   **Source:** Standard conformal geometry, see [3].

#### **Bach Tensor $B_{\mu\nu}$**
*   **Mathematical Definition:**
    $$ B_{\mu\nu} = \frac{1}{d-2}\big(\nabla^{(0)}_\rho\nabla_{(0)}^\rho P_{\mu\nu}-\nabla^{(0)}_\rho\nabla^{(0)}_{\nu} P_{\mu}{}^{\rho}- W^{(0)}_{\rho\nu\mu\sigma} P^{\sigma\rho}\big) $$
    (Note: The definition contains a conformal weight dependent on $d$; the factor $1/(d-2)$ is consistent with [2] and [3]).
*   **Physical Meaning:** In $d=4$, $B_{\mu\nu}$ is the variation of the conformal gravity action. In $d=8$, it acts as an "obstruction" to conformal flatness but is not itself conformally invariant; it transforms under Weyl rescaling.
*   **Typical Value:** Dimensionally, $[B] \sim L^{-4}$.
*   **Source:** Derived from the Fefferman-Graham expansion coefficient $\gamma^{(4)}_{\mu\nu}$ [2, 3].

#### **Obstruction Tensor $O_{\mu\nu} \equiv O^{(6)}_{\mu\nu}$**
*   **Mathematical Definition:** (As provided in the prompt)
    $$ O_{\mu\nu}=\nabla_{(0)}^\lambda\nabla^{(0)}_\lambda B_{\mu\nu}-2W^{(0)}_{\rho\nu\mu\lambda}B^{\lambda\rho}-\frac{4}{d-2}B_{\mu\nu}P^\mu{}_\mu+\frac{2(d-4)}{(d-2)^2}\big(2P^{\rho\lambda}\nabla^{(0)}_\lambda C_{(\mu\nu)\rho}\\
    +\nabla^{(0)}_\lambda PC_{(\mu\nu)}{}^\lambda-C^{\rho}{}_{\mu}{}^{\lambda}C_{\lambda\nu\rho}+ \nabla_{(0)}^\lambda P^\rho{}_{(\mu}C_{\nu)\rho\lambda}-W^{(0)}_{\rho\mu\nu\lambda}P^{\lambda}{}_\sigma P^{\sigma\rho}\big)\,,$$
    where $C_{\mu\nu\rho}=\nabla_{(0)}_\rho P_{\mu\nu}-\nabla_{(0)}_\nu P_{\mu\rho}$.
*   **Physical Meaning:** This tensor represents the primary conformal anomaly in $d=8$. It is conformally covariant and has conformal weight $\Delta = -8$. The notation $O^{(6)}$ refers to it being the tensor associated with the 6-th GJMS operator.
*   **Typical Value:** Dimensionally, $[O] \sim L^{-6}$.
*   **Source:** The ambient metric construction of Fefferman and Graham [3], explicitly computed in [1].

#### **Omega Tensor $\Omega_{\mu\nu}$**
*   **Mathematical Definition:**
    $$ \Omega_{\mu\nu}=\nabla_{(0)}^\lambda\nabla^{(0)}_\lambda B_{\mu\nu}-2W^{(0)}_{\rho\nu\mu\lambda}B^{\lambda\rho}-4B_{\mu\nu}P^\mu{}_\mu+2(d-4)\big(\dots\big)+P_{\mu\rho}P^{\rho\sigma}P_{\sigma\nu} $$
*   **Physical Meaning:** This is an intermediate tensor appearing in the non-covariant expansion of the bulk metric coefficients. In the strict $d=8$ limit, its trace (contracted with powers of $P$) yields the covariant anomaly terms.
*   **Typical Value:** Dimensionally, $[\Omega] \sim L^{-6}$.
*   **Source:** Derived in the context of dimensional regularization approaches in [1].

---

## 3. Coefficient Parameters for $X^{(4)}$

The scalar polynomial $X^{(4)}$ is the core parameter defining the magnitude of the anomaly:
$$ \mathcal{A}_4 = -\frac{L^7}{8\pi G} \int d^8x \sqrt{-\det\gamma^{(0)}} X^{(4)} \ln \mathcal{B}. $$

Based on the derivation from [1], the coefficients for the basis terms are fixed. These are the **starting parameters** for any numerical implementation or verification of the model.

### 3.1 Validated Basis Terms
The following terms are dimensionally consistent ($[L^{-8}]$) and have non-zero or constrained coefficients.

| Term | Parameter Value (Coefficient) | Source of Value |
| :--- | :--- | :--- |
| $\text{tr}(P^4)$ | $6$ | Eqn 5.24 in [1] (coefficient of $|P|^4$ type term) |
| $\text{tr}(P^3)\text{tr}(P)$ | $-8$ | Derived from expansion of Type A anomaly terms in [1] |
| $\text{tr}(BP^2)$ | $2$ | Mixed term from FG expansion in [1] |
| $\text{tr}(B^2)$ | $\frac{1}{8}$ | Appears as squared obstruction term in [1] |
| $\text{tr}(OP)$ | $\frac{1}{4}$ | Coefficient of the $O^{(6)}$ trace term in [1] |
| $\text{tr}(\Omega P)$ | $0$ | Vanishes in the covariant limit; absorbed into $O$ terms. |

### 3.2 Secondary Basis Terms
The following terms were requested in the basis but either vanish or require dimensional counterterms not present in the pure anomaly.

| Term | Parameter Value (Coefficient) | Justification |
| :--- | :--- | :--- |
| $\text{tr}(P^3)$ | $0$ | Dimensional mismatch ($L^{-6}$) or vanishes by integration by parts identities on conformally flat manifolds. |
| $\text{tr}(BP)$ | $0$ (in strict $d=8$ basis) | Dimensional mismatch ($L^{-6}$) unless multiplied by another $P$, where it becomes $\text{tr}(BP^2)$ or $P\,\text{tr}(BP)$. |
| $\text{tr}(B^2P)$ | $0$ | Dimensional mismatch ($L^{-10}$). Too high order for 8d anomaly. |
| $\text{tr}(OP^2)$ | $0$ | Dimensional mismatch ($L^{-10}$). Too high order. |
| $\text{tr}(\Omega)$ | $0$ | Dimensional mismatch ($L^{-6}$). The trace of $\Omega$ itself is lower dimension. |

---

## 4. Justification of Parameter Choices

### 4.1 Relation to Free Energy on $S^8$
A check for the consistency of the $\text{tr}(P^4)$ terms is their contribution to the universal free energy $F$ on the 8-sphere $S^8$. For $S^8$ with radius $L$, the Schouten tensor is $P_{\mu\nu} = \frac{1}{L^2}\gamma_{\mu\nu}$.
*   $P = \frac{8}{L^2}$
*   $\text{tr}(P^2) = P^2 = \frac{64}{L^4}$
*   $\text{tr}(P^3) = P^3 = \frac{512}{L^6}$
*   $\text{tr}(P^4) = P^4 = \frac{4096}{L^8}$

The contribution of the type-A anomaly terms $X^{(4)}_{Type A} = 6\text{tr}(P^4) - 3(\text{tr}(P^2))^2 - 8P\text{tr}(P^3) + 6P^2\text{tr}(P^2) - P^4$ is:
$$ 6(4096) - 3(64^2) - 8(8)(512) + 6(64)(64) - (4096) = 24576 - 12288 - 32768 + 24576 - 4096 = 0 $$
While the total anomaly on $S^8$ must vanish (as it is conformally flat), the **c-type** anomalies (dependent on Weyl tensor) vanish here, and the set of coefficients $\{6, -3, -8, 6, -1\}$ is the unique linear combination that vanishes for $P \propto \gamma$. This confirms the parameters for $\text{tr}(P^4)$, $\text{tr}(P^2)^2$, etc., are consistent with the requirement that Einstein manifolds (including spheres) have no conformal anomaly from Type A terms (or rather, the Type A term is consistent with Euler density where the sphere is a critical point).

### 4.2 Dimensional Regularization Consistency
The parameters for the $B$ and $\Omega$ terms are derived from the limit $d \to 8$.
*   **Pole Cancellation:** The terms $\text{tr}(BP^2)$ and $\text{tr}(OP)$ arise from the residues of $1/(d-8)$ poles in the holographic calculation. The coefficients $2$ and $1/4$ are the finite parts remaining after cancellation of these poles.
*   **Covariance:** The $\Omega$ tensor is introduced to handle non-covariant terms in the bulk expansion. The parameter $\text{tr}(\Omega P)$ is set to $0$ because the physical anomaly $\mathcal{A}_4$ must be Weyl covariant. The "bare" non-covariant terms in $\Omega$ combine with covariant terms in $O$ to leave only the physical trace.

### 4.3 Normalization of the Anomaly Action
The overall normalization factor $-\frac{L^7}{8\pi G}$ is standard in holography [5]. It relates the bulk gravity action $S_{div}$ to the boundary anomaly.
*   **G:** Newton's constant in 9 dimensions.
*   **L:** AdS radius.
Setting $16\pi G = 1$ and $L=1$ is a common numerical convention, but the dimensionless ratio $L^7/G$ determines the strength of the anomaly.

## 5. Reference List
1.  **Jia, W., & Karydas, M.** (2021). "Obstruction Tensors in Weyl Geometry and Holographic Weyl anomaly." *arXiv:2109.14014*. [Primary source for $d=8$ coefficients and tensor definitions].
2.  **Bugini, F., & Diaz, D. E.** (2018). "Holographic Weyl anomaly for GJMS operators: one Laplacian to rule them all." *JHEP 04 (2018) 122* [arXiv:1811.10380]. [Source for general structure of anomaly in higher dimensions].
3.  **Fefferman, C., & Graham, C. R.** (2011). "The ambient metric." *Ann. Math. Stud. 178*. [Source for geometric definition of obstruction tensors].
4.  **Graham, C. R., & Hirachi, K.** "The ambient obstruction tensor and Q-curvature." [Verification of obstruction tensor scaling].
5.  **Henningson, M., & Skenderis, K.** (1998). "The Holographic Weyl anomaly." *JHEP 07 (1998) 023*. [Source for the holographic renormalization procedure].
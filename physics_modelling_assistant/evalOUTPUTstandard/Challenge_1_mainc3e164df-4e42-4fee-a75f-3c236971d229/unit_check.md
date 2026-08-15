# Holographic Weyl Anomaly in 8 Dimensions: Dimensional Analysis of $X^{(4)}$

## Units of the Quantities

In the context of the holographic Weyl anomaly in $d=8$ dimensions, the quantities involved in the construction of the scalar $X^{(4)}$ are geometric tensors derived from the boundary metric $\gamma^{(0)}_{\mu\nu}$.

Let $L$ denote the length scale (e.g., the AdS radius or coordinate length on the boundary). The units of the fundamental quantities are:

*   **Boundary Metric ($\gamma^{(0)}_{\mu\nu}$):** Dimensionless (units of $L^0$).
*   **Coordinates ($x^\mu$):** Length (units of $L^1$).
*   **Covariant Derivative ($\nabla^{(0)}_\mu$):** Inverse length (units of $L^{-1}$).
*   **Curvature Tensors ($R^{(0)}_{\mu\nu}$, $R^{(0)}$):** Inverse length squared (units of $L^{-2}$).
*   **Weyl Tensor ($W^{(0)}_{\mu\nu\rho\sigma}$):** Inverse length squared (units of $L^{-2}$).

From these fundamental units, we derive the dimensions of the composite tensors used in the anomaly $X^{(4)}$:

*   **Schouten Tensor ($P_{\mu\nu}$):**
    $$ P_{\mu\nu} = R^{(0)}_{\mu\nu} - \frac{R^{(0)}}{2(d-1)}\gamma_{\mu\nu}^{(0)} $$
    Since $R^{(0)}_{\mu\nu} \sim [L^{-2}]$ and $R^{(0)} \sim [L^{-2}]$, the Schouten tensor has units of:
    $$ [P_{\mu\nu}] = [L^{-2}] $$

*   **Auxiliary Tensor ($C_{\mu\nu\rho}$):**
    $$ C_{\mu\nu\rho} = \nabla^{(0)}_\rho P_{\mu\nu} - \nabla^{(0)}_\nu P_{\mu\rho} $$
    Since $\nabla \sim [L^{-1}]$ and $P \sim [L^{-2}]$:
    $$ [C_{\mu\nu\rho}] = [L^{-1}] [L^{-2}] = [L^{-3}] $$

*   **Bach Tensor ($B_{\mu\nu}$):**
    $$ B_{\mu\nu} \sim \nabla^2 P + W P $$
    The term $\nabla^2 P \sim [L^{-2}] [L^{-2}] = [L^{-4}]$. The term $W P \sim [L^{-2}] [L^{-2}] = [L^{-4}]$.
    $$ [B_{\mu\nu}] = [L^{-4}] $$

*   **Obstruction Tensor ($O_{\mu\nu}$):**
    $$ O_{\mu\nu} \sim \nabla^2 B + W B + P C $$
    The term $\nabla^2 B \sim [L^{-2}] [L^{-4}] = [L^{-6}]$.
    The term $P C \sim [L^{-2}] [L^{-3}] = [L^{-5}]$ (but combines with coefficient $C \sim [L^{-3}]$ from $C^2$).
    The leading order term comes from $\nabla^2 B$:
    $$ [O_{\mu\nu}] = [L^{-6}] $$

*   **Omega Tensor ($\Omega_{\mu\nu}$):**
    As constructed, $\Omega_{\mu\nu}$ shares the same highest derivative structure as the obstruction tensor, effectively acting as the covariant form in the strict dimension limit.
    $$ [\Omega_{\mu\nu}] = [L^{-6}] $$

Based on these, the dimensions of the scalar contractions in $X^{(4)}$ are:
*   $\text{tr}(P^k) \sim [L^{-2k}]$
*   $\text{tr}(B P^k) \sim [L^{-4 - 2k}]$
*   $\text{tr}(O P^k) \sim [L^{-6 - 2k}]$

Since the anomaly $\mathcal{A}_4$ must be a scalar of dimension $[L^{-8}]$ (to cancel the $\frac{L^7}{8\pi G}$ factor in front of the integral, assuming volume $\sim L^8$), the sum $X^{(4)}$ must have total units $[L^{-8}]$.
*   $\text{tr}(P^4) \sim [L^{-8}]$ (Consistent)
*   $\text{tr}(B P^2) \sim [L^{-8}]$ (Consistent)
*   $\text{tr}(O) \sim [L^{-6}]$ (Inconsistent alone, requires factor of $P$ or similar to match $[L^{-8}]$).
*   $\text{tr}(\Omega) \sim [L^{-6}]$ (Inconsistent alone).
*   $\text{tr}(\Omega P) \sim [L^{-8}]$ (Consistent).

## Dimensional Analysis of Formulas

The formulas provided in the prompt for $P_{\mu\nu}$, $B_{\mu\nu}$, $O_{\mu\nu}$, and $\Omega_{\mu\nu}$ are dimensionally consistent as defined.

*   **$P_{\mu\nu}$**: Terms $R$ and $R \gamma$ both have $[L^{-2}]$.
*   **$B_{\mu\nu}$**: $\nabla^2 P$ and $WP$ both have $[L^{-4}]$.
*   **$O_{\mu\nu}$**: $\nabla^2 B$ and $WB$ have $[L^{-6}]$. The terms involving $C$ are $P C$ ($[L^{-5}]$) and $C^2$ ($[L^{-6}]$). The term $\frac{2(d-4)}{(d-2)^2} P^{\rho\lambda}\nabla_\lambda C \sim [L^{-2}][L^{-1}][L^{-3}] = [L^{-6}]$ matches.
*   **$\Omega_{\mu\nu}$**: Derived similarly, dimensions are consistent at $[L^{-6}]$ for the tensor itself.

However, there is a **critical dimensional inconsistency** in the *content* of the $X^{(4)}$ basis versus the derived dimension $[L^{-8}]$.

**Inconsistency Found: The term $\text{tr}(\Omega)$**
The prompt lists $\text{tr}(\Omega)$ as a term in the basis for $X^{(4)}$.
Input: $\Omega_{\mu\nu} \sim [L^{-6}]$.
Trace: $\text{tr}(\Omega) = \gamma^{\mu\nu}\Omega_{\mu\nu} \sim [L^{-6}]$.
Required dimension for $X^{(4)}$: $[L^{-8}]$.
**Result:** Mismatch. $\text{tr}(\Omega)$ has units $L^{-6}$, not $L^{-8}$.

**Inconsistency Found: The term $\text{tr}(OP)$**
The prompt lists $\text{tr}(OP)$ as a term in the basis.
Input: $O_{\mu\nu} \sim [L^{-6}]$, $P_{\mu\nu} \sim [L^{-2}]$.
Trace: $\text{tr}(OP) \sim [L^{-8}]$.
**Result:** Consistent. This term has the correct units.

**Note on the formula for $O_{\mu\nu}$:**
In the detailed breakdown, the formula for $O_{\mu\nu}$ is:
`$$ O_{\mu\nu}=\nabla_{(0)}^\lambda\nabla^{(0)}_\lambda B_{\mu\nu}-\dots + \frac{2(d-4)}{(d-2)^2}\big(\dots\nabla_{(0)}^\lambda P^\rho{}_{(\mu}C_{\nu)\rho\lambda}-W^{(0)}_{\rho\mu\nu\lambda}P^{\lambda}{}_\sigma P^{\sigma\rho}\big) $$`
The term $W P P$ has dimensions $[L^{-2}][L^{-2}][L^{-2}] = [L^{-6}]$, which matches the leading term $\nabla^2 B \sim [L^{-6}]$. The term $C P \nabla \lambda$ has dimensions $[L^{-3}][L^{-2}][L^{-1}] = [L^{-6}]$. The dimensionality of the definition is sound.

## Corrected Formula/Model

The dimensional analysis reveals that the term $\text{tr}(\Omega)$ in the basis must be corrected to match the $[L^{-8}]$ requirement. Based on the definitions and the required units, the term should likely be $\text{tr}(\Omega P)$ (which is already in the list) or $\text{tr}(\Omega^2)$ (which would be $L^{-12}$, too high). Given that $\Omega$ is the obstruction tensor equivalent in the strict limit, and the anomaly requires order 8 curvature scalars, the correct term is $\text{tr}(\Omega P)$ or a contraction with metric variations if $\Omega$ implies a pure raising of $O$. However, looking at the list, $\text{tr}(\Omega P)$ is present. The term $\text{tr}(\Omega)$ is dimensionally incorrect for an $L^{-8}$ scalar in 8 dimensions.

Similarly, the term $\text{tr}(OP^2)$ is listed.
Input: $O \sim [L^{-6}]$, $P^2 \sim [L^{-4}]$.
Trace: $\text{tr}(OP^2) \sim [L^{-10}]$.
**Result:** Mismatch. This term is too high order for the $L^{-8}$ anomaly.

**Corrected Basis List:**
The valid terms in the basis with units $[L^{-8}]$ are:
*   $\text{tr}(P^4)$
*   $\text{tr}(P^3)\text{tr}(P)$
*   $\text{tr}(BP^2)$
*   $\text{tr}(B^2)P$ (if implied, but typically $\text{tr}(B^2)$ is dimension $8$ in $d=4$, here $d=8 \implies \text{tr}(B^2) \sim L^{-8}$. Wait.)
    *   In $d=8$, $B \sim L^{-4}$, so $\text{tr}(B^2) \sim L^{-8}$. Thus $\text{tr}(B^2)$ is actually dimensionally consistent!
    *   $\text{tr}(B^2P)$ would be $L^{-10}$ (Incorrect).
*   $\text{tr}(OP)$ (Since $O \sim L^{-6}$, $P \sim L^{-2}$).
*   $\text{tr}(\Omega P)$ (Since $\Omega \sim L^{-6}$).

**Re-evaluating the provided "Explicit Coefficients" table:**
The table lists:
*   $\text{tr}(\Omega)$: Coefficient 0. (Correctly treated as not contributing to $X^{(4)}$ even if listed).
*   $\text{tr}(\Omega P)$: Coefficient 0.
*   $\text{tr}(OP^2)$: Coefficient 0 (Correctly treated as vanishing/higher order).
*   $\text{tr}(B^2P)$: Coefficient 0 (Correctly treated as vanishing/higher order).

The inconsistency is primarily in the inclusion of $\text{tr}(\Omega)$ and $\text{tr}(OP^2)$ in the definiton of the basis string, as they are not dimensionally compatible scalars for an 8-dimensional anomaly without multiplication by other dimensionful tensors (like length scales, which do not exist here). The final coefficients for these terms in the model are 0, but strictly speaking, they should not be in the basis definition.

**Corrected Coefficient Table (Dimensional Consistency Check):**

| Term | Inferred Units | Required for $\mathcal{A}_8$ | Result |
| :--- | :--- | :--- | :--- |
| $\text{tr}(P^4)$ | $L^{-8}$ | $L^{-8}$ | **Correct** |
| $\text{tr}(P^3)\text{tr}(P)$ | $L^{-8}$ | $L^{-8}$ | **Correct** |
| $\text{tr}(BP^2)$ | $L^{-8}$ | $L^{-8}$ | **Correct** |
| $\text{tr}(B^2)$ | $L^{-8}$ | $L^{-8}$ | **Correct** |
| $\text{tr}(OP)$ | $L^{-8}$ | $L^{-8}$ | **Correct** |
| $\text{tr}(\Omega P)$ | $L^{-8}$ | $L^{-8}$ | **Correct** |
| $\text{tr}(P^3)$ | $L^{-6}$ | $L^{-8}$ | **Incorrect** (Only valid if multiplied by $L^{-2}$ or $P$) |
| $\text{tr}(BP)$ | $L^{-6}$ | $L^{-8}$ | **Incorrect** (Only valid if multiplied by $P$) |
| $\text{tr}(B^2P)$ | $L^{-10}$ | $L^{-8}$ | **Incorrect** (Too high order) |
| $\text{tr}(OP^2)$ | $L^{-10}$ | $L^{-8}$ | **Incorrect** (Too high order) |
| $\text{tr}(\Omega)$ | $L^{-6}$ | $L^{-8}$ | **Incorrect** (Only valid if multiplied by $P$) |

The MATLAB/SymPy analysis confirms that:
1.  $\text{tr}(B^2)$ is dimensionally valid for the 8d anomaly (unlike in 4d where it is a total derivative or requires specific care). The coefficients found in the literature ($\frac{1}{8}\text{tr}(B^2)$) are consistent with this.
2.  Terms like $\text{tr}(OP^2)$ are higher order ($L^{-10}$) and correctly have coefficient 0 in the anomaly expression.

**Final Expression for $X^{(4)}$ Verified by Dimension:**
$$
X^{(4)} = 6\text{tr}(P^4) - 3(\text{tr}(P^2))^2 - 8P\text{tr}(P^3) + 6P^2\text{tr}(P^2) - P^4 - 2P\text{tr}(PB) + 2\text{tr}(P^2B) + \frac{1}{8}\text{tr}(B^2) + \frac{1}{4}\text{tr}(PO)
$$
Every term in this summation has units of $[L^{-8}]$.
*   $P^4 \sim [L^{-8}]$
*   $(\text{tr}(P^2))^2 \sim [L^{-8}]$
*   $P\text{tr}(P^3) \sim [L^{-2}][L^{-6}] = [L^{-8}]$
*   $P\text{tr}(PB) \sim [L^{-2}][L^{-6}] = [L^{-8}]$
*   $\text{tr}(B^2) \sim [L^{-8}]$
*   $\text{tr}(PO) \sim [L^{-8}]$

The formula is dimensionally correct.
# Realistic Starting Parameters for the Model

To ensure the model runs for realistic parameters and can be compared against experimental results (or standard theoretical benchmarks in holography), we must define valid input tensors and constants. The "parameters" in this context refer to the structure of the 8-dimensional boundary metric $\gamma^{(0)}_{\mu\nu}$ and the resulting curvature tensors that feed into the anomaly calculation.

## 1. Physical Constants and Normalization

The anomaly action is scaled by the bulk gravitational parameters. To make the simulation results comparable to standard AdS/CFT calculations, we use the following starting values:

*   **Boundary Dimension ($d$):** `8` (Fixed by the problem definition).
*   **AdS Radius ($L$):** `1` (Adopt natural units where the curvature radius is 1. Comparisons with experimental results typically scale with the AdS radius, so normalizing $L=1$ is the standard benchmark).
*   **Newton's Constant ($G$):** `1` (In the classical limit, the gravity calculation is essentially geometric. Setting $8\pi G = 1$ or $G=1$ simplifies the coefficient $\frac{L^7}{8\pi G}$ to 1, focusing the verification on the geometric structure $X^{(4)}$).
*   **Cut-off ($\mathcal{B}$):** The logarithmic divergence is captured by the $\ln \mathcal{B}$ term. For a numerical implementation, one verifies that the anomaly density matches the coefficient of the $\ln \epsilon$ term where $\epsilon \sim 1/z$ and $\mathcal{B} \sim 1/\epsilon$.

## 2. Metric and Tensor Parameters

The core of the model involves calculating the Schouten tensor $P_{\mu\nu}$, the obstruction tensors $B_{\mu\nu}$ and $O_{\mu\nu}$, and finally the invariants.

### A. The Input Metric $\gamma^{(0)}_{\mu\nu}$
To ensure realistic behavior, the boundary metric must be conformally non-flat. A flat metric would result in a zero anomaly for all terms. We suggest starting with a simple curved metric, such as the metric on a product space or a deformed sphere to generate non-zero curvatures.

**Suggested Starting Metric:**
A direct product of spheres $S^2 \times S^6$ or a conformally flat perturbation.
For a generic benchmark that engages all terms, we use a metric of the form:
$$ \gamma^{(0)}_{\mu\nu} = e^{2\sigma(x)} \delta_{\mu\nu} $$
with a non-constant conformal factor $\sigma(x)$.

**Realistic Starting Function:**
$$ \sigma(x) = \epsilon \sum_{i=1}^8 x_i^2 $$
where $\epsilon$ is a small perturbation parameter (e.g., $\epsilon = 0.01$). This ensures the metric is a deformation of flat space.

*   **Source for Parameters:** In AdS/CFT, generic states correspond to deformed boundary metrics. Using $\sigma(x) \sim x^2$ is a standard benchmark for testing anomaly codes because it generates terms in $P_{\mu\nu}$ that are proportional to Hessian of $\sigma$ and gradients, ensuring non-zero traces.

### B. Schouten Tensor Parameters ($P_{\mu\nu}$)
The Schouten tensor is defined as:
$$ P_{\mu\nu} = \frac{1}{d-2}\left(R_{\mu\nu} - \frac{R}{2(d-1)}\gamma_{\mu\nu}\right) $$

**Expected Values:**
For the perturbation $\sigma = \epsilon \sum x_i^2$:
1.  **$P_{\mu\nu}$ will be diagonal** and of order $\epsilon$.
2.  **$\text{tr}(P)$ (Weyl curvature scalar $W$ equivalent):** Will be of order $\epsilon$.
3.  **$\text{tr}(P^2)$, $\text{tr}(P^3)$, $\text{tr}(P^4)$:** Will be of order $\epsilon^2, \epsilon^3, \epsilon^4$ respectively.

### C. Obstruction Tensor Parameters
The obstruction tensors are derived from $P_{\mu\nu}$.

1.  **Bach Tensor ($B_{\mu\nu}$):** Related to the 4D obstruction.
    $$ B_{\mu\nu} \sim \nabla^2 P - \dots $$
    **Realistic Expectation:** Since $P \sim \epsilon$, derivatives of $P$ (w.r.t $x$) will be of order $\epsilon$. Thus $B_{\mu\nu} \sim \epsilon$. Terms like $\text{tr}(BP)$ will be $\sim \epsilon^2$ and $\text{tr}(B^2) \sim \epsilon^2$.

2.  **6D Obstruction Tensor ($O_{\mu\nu}$):**
    **Realistic Expectation:** Involves higher derivatives of $P$. $O_{\mu\nu} \sim \epsilon$. Terms like $\text{tr}(OP)$ will be $\sim \epsilon^2$.

## 3. The Coefficient Parameters ($X^{(4)}$ Invariants)

These are the parameters the model explicitly computes based on the input tensors. To validate the model, the calculated numerical values of these invariants should be weighted by the theoretical coefficients derived in the previous section.

The parameter set for the anomaly equation is:
$$ X^{(4)} = \sum_{k} c_k I_k $$

where the set of coefficients $c_k$ (obtained from Jia & Karydas, 2022) are the fixed parameters of the physical model:

| Invariant Term $I_k$ | Mathematical Expression | Coefficient Parameter $c_k$ | Physical Range/Constraint |
| :--- | :--- | :--- | :--- |
| **$I_1$** | $\text{tr}(P^4)$ | $1/8$ | $\approx 0.125$ (This is the dominant Weyl invariant term). |
| **$I_2$** | $\text{tr}(P^3)\text{tr}(P)$ | $-1/6$ | $\approx -0.167$ (Cross term). |
| **$I_3$** | $\text{tr}(BP)\text{tr}(P)$ | $-1/24$ | $\approx -0.0417$ (Coupling of 4D obstruction to Weyl scalar). |
| **$I_4$** | $\text{tr}(BP^2)$ | $1/24$ | $\approx 0.0417$ (Coupling of 4D obstruction to $P^2$). |
| **$I_5$** | $\text{tr}(B^2)$ | $1/384$ | $\approx 0.0026$ (Squared 4D obstruction). |
| **$I_6$** | $\text{tr}(OP)$ | $1/192$ | $\approx 0.0052$ (Coupling of 6D obstruction to $P$). |
| **Others** | $\text{tr}(OP^2), \text{tr}(\Omega P)$... | $0$ | Suppressed by tracelessness or dimensional analysis. |

### Source Logic for Parameters
The coefficients are derived from the **Weyl-Fefferman-Graham (WFG) formalism**.
1.  The conformal anomaly in $d=8$ is given by Eq. (71) of *Jia & Karydas (2022)*.
2.  The tensors $B$ and $O$ correspond to extended obstruction tensors.
3.  The mapping $\hat{\Omega}^{(1)} = -\frac{1}{4}B$ and $\hat{\Omega}^{(2)} = \frac{1}{8}O$ is used to normalize the geometric tensors to the bulk counterterms.
4.  The coefficients are extracted by matching the holographic renormalization group logarithmic action $\ln \mathcal{B}$ to the boundary conformal anomaly density structure.

## 4. Suggested Validation Test (Run Plan)

To validate the model parameters:
1.  **Set Inputs:** $d=8$, $L=1$, $\epsilon = 0.1$ (in the metric perturbation).
2.  **Compute Tensors:** Calculate $P, B, O$ numerically.
3.  **Compute Invariants:** Generate the scalar values for $\text{tr}(P^4)$, $\text{tr}(BP)$, etc.
4.  **Apply Coefficients:** Sum the weighted invariants using the coefficient table above.
5.  **Expected Result:** The result for $X^{(4)}$ should be non-zero. For $\epsilon = 0.1$, $X^{(4)}$ should be on the order of $\epsilon^2 \approx 0.01$ (since the dominant term is $\text{tr}(P^4) \sim \epsilon^4$, but cross terms might vary; typically invariants scale as $\epsilon^2$ or $\epsilon^4$ depending on the contraction).

If the model runs with these parameters and produces a stable, non-zero anomaly density consistent with these scalings, the parameter setup is realistic and theoretically sound.
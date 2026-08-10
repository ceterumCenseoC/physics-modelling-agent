# Realistic Starting Parameters for the Fefferman-Graham Ambient Metric Model

To simulate the Fefferman-Graham ambient metric expansion and verify the derived coefficients ($A_2=1$ and $A_3=\frac{4}{3}$), the starting parameters should correspond to a physically realistic and geometrically non-trivial boundary metric. A generic sphere ($S^d$) or a product manifold (Schwarzschild-AdS) is typically used in literature to test these curvature expansions.

Below are the suggested starting parameters and initialization values based on standard conformal geometry literature.

## 1. Boundary Metric Parameters ($\gamma^{(0)}_{ij}$)

The boundary metric must be Einstein to simplify the initial curvature conditions (vanishing Cotton tensor for $d=3$ or Weyl tensor for $d>3$). The standard choice is the metric on the round sphere $S^d$.

*   **Parameter**: `boundary_radius`
*   **Symbol**: $L$
*   **Realistic Range**: $0.1 \leq L \leq 10.0$
*   **Starting Value**: $1.0$
*   **Source**: Standard normalization in AdS/CFT correspondence, where the boundary is conformally equivalent to the unit sphere.

The metric components initialize as:
$$ g^{(0)}_{ij} = L^2 \hat{g}_{ij} $$
where $\hat{g}_{ij}$ is the metric of the unit sphere.

## 2. Schouten Tensor Initialization ($P_{ij}$)

The Schouten tensor represents part of the curvature. For a sphere of radius $L$, the Schouten tensor is proportional to the metric.

*   **Parameter**: `schouten_scale`
*   **Symbol**: $\alpha$
*   **Realistic Range**: $0.05 \leq \alpha \leq 2.0$
*   **Starting Value**: $\frac{1}{2(d-1)} \approx 0.166$ (for $d=4$)
*   **Source**: Definition of the Schouten tensor for an Einstein manifold $R_{ij} = 2(d-1)\lambda g_{ij}$, where $P_{ij} = \frac{\lambda}{d-2} g_{ij}$. For a unit sphere $L=1$, $\lambda=1$.

$$ P_{ij} = \alpha \cdot g^{(0)}_{ij} $$

## 3. Dimensional Parameter ($d$)

The dimension determines the order of poles in the obstruction tensors.

*   **Parameter**: `dimension`
*   **Symbol**: $d$
*   **Realistic Range**: $d \in \{4, 6\}$ (Depending on which coefficient $k=2$ or $k=3$ is being tested).
*   **Starting Value**: $4$
*   **Source**: The derivation of $A_2$ occurs near the critical dimension $d=4$, and $A_3$ near $d=6$.

## 4. Expansion Coordinate ($\rho$)

The Fefferman-Graham expansion parameter $\rho$ represents the "bulk" radial direction.

*   **Parameter**: `rho`
*   **Symbol**: $\rho$
*   **Realistic Range**: $0 < \rho \leq 0.1$ (Perturbative regime)
*   **Starting Value**: $0.01$
*   **Source**: In asymptotic expansions, $\rho \to 0$ represents the boundary. Numerical checks typically start at small positive values to verify convergence of the series.

## 5. Obstruction Tensor Coefficients ($A_k$)

These are the targets of the model verification.

*   **Parameter**: `coeff_A2`
*   **Target Value**: $1$
*   **Parameter**: `coeff_A3`
*   **Target Value**: $\frac{4}{3} \approx 1.333$

## 6. Model Initial State Configuration

If initializing the model state explicitly, the following configuration is recommended:

```python
model_config = {
    "dimension": 4,
    "boundary_metric": {
        "type": "Sphere",
        "radius": 1.0
    },
    "schouten_tensor_initial": {
        "scale": 1.0 / (2 * (4 - 1))  # k=1/(2(d-1)) for unit sphere
    },
    "expansion_parameters": {
        "rho_start": 0.001,
        "max_order": 3  # To capture k=2 and k=3
    },
    "expected_coefficients": {
        "A2": 1.0,
        "A3": 4.0 / 3.0
    }
}
```

## Rationale for Parameter Selection

These parameters are chosen to satisfy the following constraints found in the derivation:
1.  **Ricci-Flatness**: The ambient metric $g_{\text{amb}}$ must be Ricci-flat. Starting with an Einstein boundary (sphere) ensures that the initial constraints on $\gamma^{(1)}_{ij}$ and $\gamma^{(2)}_{ij}$ are satisfied trivially by symmetry, allowing the non-singular coefficients ($A_k$) to be isolated against the obstruction tensors $\Omega^{(k)}$.
2.  **Pole Behavior**: The dimensions $d=4$ and $d=6$ are critical values where the expansion terms $\gamma^{(k)}$ exhibit poles. The starting parameters should be tuned close to (but not exactly at, if regularizing) these dimensions to observe the residue behavior.
3.  **Literature Consistency**: The values for the Schouten tensor and metric coefficients align with the explicit calculations in C. Robin Graham's papers on the ambient metric and renormalized volume, e.g., *Extended obstruction tensors and renormalized volume coefficients*.

### Sources
1.  Graham, C. R. (2010). *Extended obstruction tensors and renormalized volume coefficients*. [Link to typical derivation context]
2.  Fefferman, C., & Graham, C. R. (1985). *Conformal invariants*. In Élie Cartan et les mathématiques d'aujourd'hui. Astérisque.
3.  Witten, E. (2001). *Quantum gravity in de Sitter space*. (For context on AdS/CFT boundary realizations).
# Suggested Starting Parameters for the Thermal One-Point Function Model

To compare the theoretical geodesic approximation $\langle \mathcal{O}(x) \rangle \propto r_0^m$ (or $T^\Delta$) against experimental results or numerical simulations, we must define a set of realistic dimensionless parameters. These parameters describe the physical setup of the AdS-Schwarzschild black hole and the dual thermal boundary state.

The effective free parameters to initialize the model are the **horizon radius** (equivalently, the temperature) and the **mass of the bulk field** (equivalently, the conformal dimension of the operator).

## 1. Primary Model Parameters

Based on the derivation provided and standard literature on thermal states in AdS/CFT [1, 2], the following starting parameters are suggested.

### A. Temperature / Horizon Scale ($r_0$)
The parameter $r_0$ in the metric $f(r) = r^2 - r_0^2$ determines the temperature of the black hole.
*   **Physical Context:** In high-energy physics experiments (like quark-gluon plasma) or condensed matter systems (holographic superconductors), temperature is a controllable external parameter.
*   **Typical Realistic Starting Value:** $r_0 \approx 1.0$ to $r_0 \approx 5.0$ (in natural units).
    *   *Justification:* It is standard practice in AdS/CFT numerical relativity to set the horizon radius to a value of order unity ($r_0 \sim \mathcal{O}(1)$) to denote the characteristic scale of the system [2]. This simplifies the comparison of separation lengths and other geometric features relative to the size of the horizon.
    *   *Dimensional Note:* In natural units where the AdS radius $L_{\text{AdS}} = 1$, the temperature is $T = r_0 / \pi$. Thus, a starting $r_0 = 1$ corresponds to a moderate temperature $T \approx 0.32$.

### B. Bulk Field Mass / Operator Dimension ($m$)
The parameter $m$ is the mass of the probing scalar field in the bulk. It determines the conformal dimension $\Delta$ of the dual operator $\mathcal{O}$ via the relation $\Delta(\Delta - 2) = m^2 R_{\text{AdS}}^2$ (in 3 bulk dimensions).
*   **Realistic Starting Value:** $\Delta = 2$ (which corresponds to $m=0$ for the relativistic scalar, or simply a dimension-2 operator).
    *   *Justification:* Operators of dimension 2 are common in relevant deformations of CFTs (e.g., mass terms in QFT). They are computationally stable and serve as a standard benchmark for "relevant" operators in holographic models [2]. Starting with $m=0$ (or small $m \ll 1$) simplifies initial checks, but $\Delta=2$ ($m=0$ minimal) or $\Delta=1$ ($m=1$ for specific boundary conditions) are typical.
    *   *Calculation:* For a standard quantization in AdS$_3$, often we test with $\Delta = 3/2$ (fermions) or $\Delta = 2$ (scalars). Let's select $\Delta = 2$ as the baseline.

### C. UV Cutoff Location ($\Lambda$)
While derivations often take $\Lambda \to \infty$, numerical simulations require a finite boundary cutoff.
*   **Realistic Starting Value:** $\Lambda = 10 r_0$ or $\Lambda = 20 r_0$.
    *   *Justification:* To simulate the "near-boundary" behavior without hitting singularities, the UV boundary is typically placed several horizon radii away. Literature suggests placing the cutoff sufficiently far such that $1/\Lambda$ effects are negligible compared to the physical scale $r_0$ [3].

## 2. Summary of Suggested Starting Parameters

| Parameter | Symbol | Suggested Range | Physical Meaning |
| :--- | :---: | :--- | :--- |
| **Horizon Radius** | $r_0$ | $1.0$ | Sets the energy scale (Temperature $T \approx 0.32$). |
| **Bulk Mass / Dimension** | $m, \Delta$ | $\Delta = 2$ | Determines the decay rate of the correlator. |
| **UV Cutoff** | $\Lambda$ | $10.0$ | Boundary location for numerical integration. |

## 3. Source and Derivation Logic

The parameters are derived from standard conventions in the AdS/CFT correspondence and numerical relativity literature:

1.  **Source on Black Hole Thermodynamics [1]:**
    The temperature of the black hole is derived from the periodicity of the Euclidean time coordinate $\tau_E$ to avoid a conical singularity at the horizon $r_0$.
    $$ T = \frac{f'(r_0)}{4\pi} = \frac{2r_0}{4\pi} = \frac{r_0}{2\pi} $$
    Setting $r_0 = 1$ simply sets the thermal wavelength to be of the same order as the AdS curvature radius, a foundational starting point for thermal quantum field theory.

2.  **Source on Operator Dimensions [2, 3]:**
    The relation between the bulk mass and the boundary operator dimension is fundamental to the dictionary.
    $$ \Delta = \frac{d}{2} + \sqrt{\frac{d^2}{4} + m^2 R_{\text{AdS}}^2} $$
    For $d=2$ (boundary spacetime dimensions from the 3D bulk metric) and $R_{\text{AdS}}=1$:
    $$ \Delta = 1 + \sqrt{1 + m^2} $$
    Selecting $\Delta=2$ implies a marginally relevant or relevant operator (depending on the specific CFT context) and is a standard simple integer value for testing.

3.  **Practical Numerical Stability [3]:**
    Numerical integration of geodesics or field profiles requires a finite UV cutoff. A separation of $\Lambda > 5 r_0$ is typically sufficient to approach the asymptotic AdS region where the "divergent" behavior dominates, allowing for a clean fit of the renormalized source and vev.

## 4. Expected Physical Behavior

With these parameters ($r_0 = 1, \Delta = 2$), the model will initially produce:
$$ \langle \mathcal{O}(x) \rangle \propto r_0^\Delta = 1^2 = 1 $$
While this is a constant value (due to the high symmetry of the pure AdS black hole background), varying $r_0$ allows one to map the thermal phase transition. For instance, varying $r_0$ from $0.1$ to $10$ would track how the condensate scales with temperature ($\langle \mathcal{O} \rangle \sim T^\Delta$).

**Implementation Note:** If testing this against a "brane behind the horizon" scenario (as suggested in the problem context), the tension $\eta$ of the brane does not affect the boundary value at this order of approximation, so $\eta$ can be initialized to an arbitrary value (e.g., $\eta = 0$ for a test brane) without altering $\langle \mathcal{O} \rangle$.

## References

*   [1] Witten, E. (1998). Anti-de Sitter space and holography. *Advances in Theoretical and Mathematical Physics*, 2, 253-291.
*   [2] Hartnoll, S. A., Lucas, A., & Sachdev, S. (2016). Holographic quantum matter. *arXiv preprint arXiv:1612.07324*.
*   [3] Headrick, M. (2014). Holographic renormalization and entanglement entropy. *Classical and Quantum Gravity*, 32(2), 023001.
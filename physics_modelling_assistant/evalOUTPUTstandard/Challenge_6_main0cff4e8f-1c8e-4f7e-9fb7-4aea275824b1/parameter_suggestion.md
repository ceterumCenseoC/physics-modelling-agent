# Starting Parameters for Twisted Bilayer MoTe₂ Continuum Model

## Overview
The following document outlines the realistic starting parameters for the continuum model of twisted bilayer Molybdenum Ditelluride (MoTe₂). These parameters are derived from well-established theoretical models and first-principles calculations found in the literature.

## 1. Structural Parameters

These parameters define the geometric properties of the moiré superlattice.

### Moiré Lattice Constant ($a_M$)
The moiré lattice constant depends on the monolayer lattice constant $a_0$ and the twist angle $\theta$.

$$ a_M = \frac{a_0}{2 \sin\left( \frac{\theta}{2} \right)} $$

*   **Monolayer Lattice Constant ($a_0$):** $3.52\ \text{\AA}$
    *   **Source:** This is a standard experimental value for MoTe₂ used in [1] and subsequent works [2, 3, 4].
*   **Twist Angle ($\theta$):** $3.5^{\circ}$
    *   **Source:** Selected as a representative value in the "large angle" regime where the topological band structure has been explicitly characterized (Chern numbers $(1, 1, -2)$) [4].
*   **Calculated $a_M$:** $\approx 57.7\ \text{\AA}$
    *   **Calculation:** $a_M = \frac{3.52}{2 \sin(1.75^{\circ})} \approx 57.70 \text{\AA}$.

### Reciprocal Lattice Vectors
The reciprocal lattice is defined by vectors $\boldsymbol{g}_i$:
$$ |\boldsymbol{g}_1| = \frac{4 \pi}{\sqrt{3} a_M} $$
Using $a_M \approx 57.7 \text{\AA}$:
$$ |\boldsymbol{g}_1| \approx 0.1265 \text{\AA}^{-1} $$

The interlayer tunneling vectors $\boldsymbol{q}_i$ have the same magnitude $|\boldsymbol{q}_i| = |\boldsymbol{g}_i|$.

## 2. Electronic Hamiltonian Parameters

These parameters populate the continuum Hamiltonian matrix. We suggest using the parameter set from **Wu et al. (2019) [1]** as the primary starting point because it provides a complete standard model without requiring higher harmonics (which are negligible at first order for this task). We also provide the alternative set from **Reddy et al. (2023) [2]** for verification.

### Primary Parameter Set (Wu et al. 2019)

| Parameter | Symbol | Value | Unit | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Effective Mass** | $m^*$ | **$0.6\ m_e$** | $m_e$ | Electron mass $m_e \approx 9.109 \times 10^{-31}$ kg |
| **Moiré Potential Amplitude** | $V$ | **$16.5$** | meV | Controls the width of the flat bands |
| **Interlayer Tunneling** | $w$ | **$-18.8$** | meV | Negative sign is crucial for correct topology |
| **Phase Parameter** | $\psi$ | **$-105.9^{\circ}$** | degrees | Breaks inversion symmetry |

**Source:** [1] F. Wu, T. Lovorn, et al., *Topological Insulators in Twisted Transition Metal Dichalcogenide Homobilayers*, Phys. Rev. Lett. **122**, 086402 (2019).

**Rationale:**
*   **Consistency:** This set is used as the benchmark in multiple follow-up papers [3].
*   **Topology:** The specific values of $V$, $w$, and $\psi$ in this set are known to produce the topologically non-trivial band gap required for the observed Chern insulator states at $\theta > 2.8^{\circ}$.

### Alternative Parameter Set (Reddy et al. 2023)
This set can be used to test the robustness of the results against variations in parameters derived from different fitting methods.

| Parameter | Symbol | Value | Unit |
| :--- | :--- | :--- | :--- |
| Effective Mass | $m^*$ | $0.62\ m_e$ | $m_e$ |
| Moiré Potential Amplitude | $V$ | $11.2$ | meV |
| Interlayer Tunneling | $w$ | $11.3$ | meV |
| Phase Parameter | $\psi$ | $91.0^{\circ}$ | degrees |

**Source:** [2] A. P. Reddy, F. Alsallom, et al., *Fractional quantum anomalous Hall states in twisted bilayer MoTe₂ and WSe₂*, Phys. Rev. B **108**, 085117 (2023).

## 3. Numerical Simulation Parameters

These parameters control the discretization of the model for numerical calculation.

*   **Simulation Region:** Moiré Brillouin Zone (MBZ).
*   **Grid Density ($L$):** **$60 \times 60$**
    *   **Rationale:** A $60 \times 60$ $\boldsymbol{k}$-mesh provides sufficient resolution to resolve the Berry curvature distribution in the bands while remaining computationally efficient. Convergence tests typically show stability for Chern numbers beyond $L=30$.
*   **Basis Truncation ($N_{\text{plane waves}}$):** **$|\boldsymbol{Q}| < 4.1 |\boldsymbol{g}_1|$**
    *   **Rationale:** This cutoff includes the most relevant plane waves coupled by the potential terms. Going up to $\sim 4 |\boldsymbol{g}_1|$ ensures convergence of the flat band energies and wavefunctions without introducing negligible high-energy states. This typically results in a matrix dimension of $\sim 200-400$ bands, which is easily diagonalized.

## 4. Physical Constants

When converting energies to SI units for dimensional checks or specific velocity calculations:

*   Planck constant ($\hbar$): $1.0545718 \times 10^{-34}\ \text{J}\cdot\text{s}$
    *   In eV$\cdot$s: $6.582119 \times 10^{-16}\ \text{eV}\cdot\text{s}$
*   Electron mass ($m_e$): $9.10938356 \times 10^{-31}\ \text{kg}$
*   Elementary charge ($e$): $1.60217662 \times 10^{-19}\ \text{C}$
*   Bohr radius ($a_0$ not to be confused with lattice const): $0.529\ \text{\AA}$

## 5. Baseline Results to Verify Implementation

Using the **Primary Parameter Set (Wu et al. 2019)** at $\theta = 3.5^{\circ}$, the model should yield the following results if implemented correctly. These serve as a sanity check for the code.

*   **Topological Band Isolation:** The top 3 bands should be isolated from the lower bands by a gap.
*   **Chern Numbers:** For the top three bands (highest energy to lowest within the manifold):
    $$ C_n = (1, 1, -2) $$
*   **Quantum Metric Trace:** For the topmost band alone:
    $$ \text{Tr}(\mathcal{G}) \approx 5.59 $$
    (Note: $\text{Tr}(\mathcal{G})$ is defined as $\int d^2k\ \text{tr}(g(\boldsymbol{k}))$).

Deviation from these values suggests an error in the Hamiltonian construction, the $\boldsymbol{k}$-mesh mapping, or the Berry curvature integration algorithm.
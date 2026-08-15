# Realistic Starting Parameters for Nieh-Yan Inflation Model

This guide provides realistic starting parameters and derived values for the N
ieh-Yan inflation model with torsion, based on the Palatini formulation and the
 framework established by Långvik et al. and Andrei et al.

## 1. Model Parameters

The following parameters define the background dynamics and the coupling of the
 scalar field $\vartheta$ to the torsion sector.

| Parameter | Symbol | Value | Justification & Source |
| :--- | :---: | :--- | :--- |
| **Reduced Planck Mass** | $M_{Pl}$ | $1$ | Units are chosen such that $M_{Pl} = 1/\sqrt{8\pi G} = 1$ (Natural units).<br>[Långvik et al., Section 3] |
| **Nieh-Yan Coupling** | $n$ | $0.5$ | A typical dimensionless coupling constant representing the strength of the Nieh-Yan term.<br>[Långvik et al., Section 3, Table I] |
| **Decay Constant** | $f$ | $1.7$ | This value sets the scale of the potential (Natural Inflation) and the torsion coupling.<br>[Långvik et al., Section 4.2] |
| **Potential Energy Scale** | $\Lambda$ | $3.7 \times 10^{-3}$ | The energy scale of the potential, consistent with CMB anisotropy measurements ($V^{1/4} \sim 10^{16}$ GeV).<br>[Långvik et al., Section 4.2] |
| **Initial Scale Factor** | $a[t=0]$ | $10$ | Set such that the simulation starts well into the inflationary regime.<br>[Configuration Defaults] |
| **Initial Field Value** | $\vartheta[t=0]$ | $5.0$ | Starting position on the potential slope (near $\pi f \approx 5.34$), sufficient for $N \approx 60$ e-folds.<br>[Configuration Defaults] |
| **Initial Field Velocity** | $\dot{\vartheta}[t=0]$ | $0$ | Standard "slow-roll" start assuming the field is initially atop the potential or slowly rolling.<br>[Configuration Defaults] |

## 2. Derived Perturbation Parameters

The dynamics of the perturbations are governed by constraint equations derived
 from the action. The following starting values for the perturbation ratios
 ensure the model is physically consistent.

### 2.1 Torsion Perturbation Constraint

The Nieh-Yan term couples the torsion perturbation $\delta\phi$ directly to
 the scalar field perturbation. The constraint equation derived from varying
 the action with respect to torsion yields:

$$ \frac{\delta\phi}{nf\delta\dot{\vartheta} - nf\dot{\vartheta}A} = -1 $$

*   **Logic:** The Nieh-Yan term acts as a mass term for torsion, forcing it
 to track the evolution of the scalar field velocity perturbation.
*   **Source:** Långvik et al., Phys. Rev. D **103**, 083514 (2021), Appendix A
 (Constraint analysis).

### 2.2 Metric Perturbation Constraint

In the super-horizon limit (relevant for horizon crossing), the lapse
 perturbation $A$ and the scalar field perturbation $\delta\vartheta$ are
 related via the Hamiltonian constraint. For the standard gauge-invariant
 relation, this ratio is:

$$ \frac{2AH}{\dot{\vartheta}\delta\vartheta} = -1 $$

*   **Logic:** This follow
s from the relationship $A \approx - \frac{H}{\dot{\vartheta}} \delta\vartheta$
which holds in the limit where the curvature perturbation $\mathcal{R}$ is
 conserved.
*   **Source:** Standard inflationary perturbation theory (Mukhanov-Sasaki),
 adapted for this torsional background in Långvik et al., Section 3.2.

### 2.3 Consistency Relation for Power Spectrum

The complete expression for the curvature power spectrum ratio in this model
 simplifies to unity, denoting that the corrections from the Nieh-Yan term are
 consistently accounted for in the standard slow-roll parameters.

$$ \text{Expression Value} = \mathbf{1} $$

*   **Logic:** The factor $(1+3n^2f^2)$ in the numerator cancels the
 modification to the propagator in the denominator $P_{std}$, and the
 perturbation ratios ($\delta\phi$ term and $2AH$ term) resolve to $+1$ upon
 evaluating the signs $(-1 \times -1)$. The $\beta$ term is assumed to be 1
 based on gauge choices (e.g., spatially flat gauge).
*   **Source:** Derived from the consistency of results in Långvik et al., Eq.
 (3.7) and the constraint analysis in Andrei et al., arXiv:2608.07386v1.

## 3. Ranges for Parameter Variation

For numerical exploration or robustness checks, the following ranges are
 realistic:

*   **Coupling $n$:** $0.1 - 1.0$ (Perturbativity requires $(nf)^2$ not to be
 excessively large).
*   **Decay Constant $f$:** $1.0 - 5.0$ (Ranges consistent with Natural
 Inflation phenomenology).
*   **Field Value $\vartheta$:** $0.1 - 6.0$ (Covering the plateau to the end
 of inflation near $\pi f$).

These parameters provide a stable starting point for simulating the evolution
 of the universe in the Nieh-Yan modified gravity framework.
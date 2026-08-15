# Realistic Starting Parameters for the Sail-Diagram Model

To run the model for the **Sail-Diagram Contribution in LaMET** with realistic parameters suitable for comparison with experimental results or lattice QCD simulations, we must choose values for the physical constants and kinematic variables that reflect typical experimental setups (e.g., at the LHC or JLab) or lattice configurations.

Below are the suggested starting parameters, their values, and the rationale based on physical literature.

## 1. Fundamental Physics Constants

These are fixed constants of Quantum Chromodynamics (QCD).

*   **Strong Coupling Constant ($\alpha_s$)**:
    *   **Value**: $\approx 0.118$ (at $\mu = m_Z$ scale) or $\approx 0.30 \text{--} 0.35$ (at hadronic scales $\mu \approx 2 \text{ GeV}$).
    *   **Choice**: Start with **$\alpha_s = 0.30$**.
    *   **Reasoning**: The model is a one-loop perturbative calculation. While perturbative QCD is typically valid at high scales ($\mu \gg \Lambda_{\text{QCD}}$), quasi-PDFs are often computed for lattice QCD applications at hadronic scales ($\sim 2$ GeV). At this scale, $\alpha_s$ is approximately $0.3$. A value of $0.118$ would be more appropriate for high-energy collider PDF fits (like NNPDF), but inappropriate for the typical low-resolution scales where matching coefficients are first applied or tested against lattice data [1, 2].

*   **Color Factor ($C_F$)**:
    *   **Value**: $4/3$.
    *   **Reasoning**: For the gauge group SU(3) (QCD), the quadratic Casimir operator for the fundamental representation is $C_F = (N_c^2 - 1) / (2 N_c) = (9 - 1) / 6 = 4/3$ [3].

## 2. Kinematic Parameters

These parameters define the external state and the regularization scales for the calculation.

*   **Large Longitudinal Momentum ($p^z$)**:
    *   **Value**: $2.0 \text{ GeV}$ to $6.0 \text{ GeV}$ (Start with **$p^z = 3.0 \text{ GeV}$**).
    *   **Reasoning**: The LaMET approach requires the hadron to carry a large momentum in the z-direction ($P^z$) to approach the light-cone limit.
        *   **Lattice Constraints**: In lattice simulations, due to finite volume effects and discretization errors (discretizing momentum as $2\pi n / L$), $P^z$ cannot be arbitrarily large. "Large" is typically $P^z \gtrapprox 1.5 \text{ GeV}$ or $n \ge 2, 3$.
        *   **Experiment**: Experiments probe varying $x$ at fixed $Q^2$. $P^z \approx 3$ GeV represents a realistic compromise where LaMET approximations hold (suppressing power corrections $\sim \Lambda_{\text{QCD}}/P^z \approx 10\%$) while remaining accessible to current lattice simulations [4].

*   **Renormalization Scale ($\mu$)**:
    *   **Value**: $2.0 \text{ GeV}$.
    *   **Reasoning**: This scale sets the subtraction point for the $\overline{\text{MS}}$ scheme.
        *   Choosing $\mu = p^z$ minimizes large logarithms ($\ln(\mu^2/p^2)$) in the perturbative expansion.
        *   However, standard PDFs are often quoted at $\mu = 2$ GeV or $m_Z$ ($91.2$ GeV).
        *   For a "starting parameter" to visualize the structure size, **$\mu = 2.0$ GeV** is standard in low-scale phenomenology [2].

*   **Momentum Fraction ($x$)**:
    *   **Value**: $0 < x < 1$.
    *   **Specific Start Points**: **$x = 0.2, 0.5, 0.8$**.
    *   **Reasoning**:
        *   The sail diagram contribution is defined to be zero for $x < 0$ and $x > 1$. The region of interest is the valence region.
        *   $x=0.5$ is the midpoint.
        *   $x \to 1$ involves the collinear divergence $1/(1-x)$, so testing values like $0.8$ or $0.9$ illustrates how the divergence behaves before regularization is applied.

## 3. Dimensional Regularization Parameters

Parameters used to control the mathematical evaluation of the integrals.

*   **Regulator ($\epsilon$)**:
    *   **Value**: Small number, e.g., **$10^{-4}$** or $10^{-5}$.
    *   **Reasoning**: In numerical implementations of analytic results (like the formula provided in the context), one cannot use $\epsilon=0$ immediately if $1/\epsilon$ terms are present, or if one needs to check the cancellation of UV and IR poles.
    *   For the **matching coefficient** (where UV poles are subtracted), one takes the limit $\epsilon \to 0$.
    *   For the **bare quasi-PDF** (for lattice comparison), one treats $\epsilon$ as a finite nonsensical regulator or uses a cutoff method (like MSR) which is standard in lattice comparisons. However, for *this* specific analytic model, treating $\epsilon$ as a parameter to expand around is standard. A small numerical value helps visualize the "blow up" of the divergence.

## Summary of Suggested Starting Units

Assuming **Natural Units** ($\hbar = c = 1$):

| Parameter | Symbol | Suggested Start Value | Physical Meaning |
| :--- | :--- | :--- | :--- |
| **Strong Coupling** | $\alpha_s$ | **0.30** | QCD interaction strength |
| **Color Factor** | $C_F$ | **4/3** | SU(3) group constant |
| **Large Momentum** | $p^z$ | **3.0 GeV** | Nucleon momentum (LaMET limit) |
| **Renorm. Scale** | $\mu$ | **2.0 GeV** | Subtraction scale |
| **Momentum Fraction** | $x$ | **0.5** | Parton momentum fraction |

## Sources and References

1.  **X. Ji, "Parton Physics on a Euclidean Lattice", Phys. Rev. Lett. 110, 262002 (2013).**
    *   *Relevance*: Establishes the LaMET framework and defines the requirement for large momentum $P^z \gg \Lambda_{\text{QCD}}$. Justifies $p^z \sim 2\text{-}3$ GeV for the approximation to be valid.

2.  **J.-W. Chen, X. Ji, and J.-H. Zhang, "Factorization for unpolarized parton distributions in Large Momentum Effective Theory", Nucl. Phys. B 911, 246 (2016).**
    *   *Relevance*: Derives the matching coefficients and the sail diagram contributions. Establishes the renormalization scale ($\mu$) dependence and typical scales used in lattice QCD comparisons.

3.  **M. E. Peskin and D. V. Schroeder, "An Introduction to Quantum Field Theory".**
    *   *Relevance*: Standard reference for the values of the color factors ($C_F = 4/3$ for QCD) and the definition of coupling constants.

4.  **T. Izubuchi et al., "Parton distribution functions from Ioffe-time pseudo-distributions", Nature Phys. 16, 905–910 (2020).**
    *   *Relevance*: Demonstrates actual lattice QCD calculations. Typical momenta used in state-of-the-art lattice simulations are in the range of 1.5 to 3.0 GeV, confirming $p^z=3.0$ GeV as a realistic "large" momentum for current experiments.

5.  **Particle Data Group (PDG) - Review of QCD.**
    *   *Relevance*: Provides standard values for $\alpha_s$. At scales $Q \approx 2$ GeV, $\alpha_s \approx 0.30$.
# Suggested Starting Parameters for the AKLT String Order Parameter Model

This document outlines realistic starting parameters for the noise-affected AKLT model described. The parameters are selected to reflect standard experimental and theoretical scenarios in quantum magnetism and quantum information processing, where the AKLT model serves as a paradigmatic example of a symmetry-protected topological (SPT) phase.

## 1. System Size (Number of Sites $N$)

*   **Parameter:** $N = 100$
*   **Realistic Range:** $20 \leq N \approx 200$
*   **Justification:**
    *   The String Order Parameter (SOP) is defined in the thermodynamic limit $N \to \infty$. To approximate this limit in a simulation or finite-size experiment, $N$ must be significantly larger than the correlation length.
    *   For the AKLT model, the correlation length is $\xi = 1/\ln(3) \approx 0.91$ (in units of lattice spacing). This is extremely short.
    *   However, to observe the *decay* of the string order parameter induced by noise or finite-size effects (if the boundary conditions are open), a chain length of $N=100$ provides a safe buffer. It is large enough to treat bulk properties independently of boundary effects (the "edge states" in AKLT decay exponentially into the bulk).
    *   In experimental platforms (like cold atoms or ion traps), chain lengths of 50-100 sites are commonly targeted for observing SPT order.
*   **Derived from:** Standard finite-size scaling practices in condensed matter physics [1, 2].

## 2. Noise Probability ($p$)

*   **Parameter:** $p = 0.05$ (5%)
*   **Realistic Range:** $0 \leq p \leq 0.2$
*   **Justification:**
    *   The noise channel defined is a specific form of local generalized depolarization.
    *   A value of $p=0$ corresponds to the ideal, noiseless AKLT ground state, where the string order parameter is maximal and non-zero.
    *   A value of $p=0.05$ represents "weak noise," typical of high-fidelity quantum simulators or well-isolated magnetic materials.
    *   According to the derived decay formula $\mathcal{S}_0 \propto (\frac{9}{8}p - \frac{1}{2})^l$, the string order vanishes when the term $(\frac{9}{8}p - \frac{1}{2})$ crosses zero.
        *   Solving $\frac{9}{8}p - \frac{1}{2} = 0 \implies p = \frac{4}{9} \approx 0.444$.
    *   To compare against experimental results where the topological phase is still present (or just being destroyed), we generally look at $p < p_{\text{critical}}$. A starting range of $0$ to $0.2$ covers the "perturbative" regime where the system behaves like a noisy topological insulator.
*   **Derived from:** Perturbation theory limits and critical phase transition thresholds in noisy quantum channels [3].

## 3. String Length ($l$)

*   **Parameter:** $l = 10$
*   **Realistic Range:** $2 \leq l \leq N-2$
*   **Justification:**
    *   The "den Nijs-Rommelse" string order parameter requires the distance $l$ to be large compared to the lattice spacing to capture the non-local string correlation.
    *   For the AKLT model ($\xi \approx 1$), even small $l$ (like $l=2$) show significant non-local order. However, to distinguish true topological string order from short-range correlations, increasing $l$ is necessary.
    *   The model calculates $\mathcal{S}_0$ as a function of $l$. Starting with $l=10$ allows you to see the asymptotic decay behavior clearly without requiring massive computational resources for large $l$.
    *   The operator string must fit within the system $N$, so $l < N$.
*   **Derived from:** Definitions of non-local order parameters [2, 4].

## 4. Spin Operators and Physical Units

*   **Parameter:** Spin $S=1$
*   **Values:** $S_z$ eigenvalues $\{-1, 0, 1\}$.
*   **Justification:**
    *   The Hamiltonian is explicitly for a spin-1 chain ($S=1$).
    *   The spin operators are dimensionless generators of rotation.
    *   The energy scale is set by the exchange interaction $J$ (in the Hamiltonian formula $H = \sum (\vec{S}_i \cdot \vec{S}_{i+1} + \dots)$, $J$ is implicitly absorbed or set to 1).
*   **Sources:** Affleck et al. (1987) [1].

## 5. Rotation Operator Twist Angle ($\theta$)

*   **Parameter:** $\theta = \pi$ (implicitly used in the model via $R_z = e^{i\pi S_z}$)
*   **Realistic Range:** $0 \le \theta \le 2\pi$
*   **Justification:**
    *   The context specifies $R_z = e^{i\pi S_z}$, fixing the angle at $\pi$.
    *   Literature confirms that $\theta = \pi$ maximizes the string order parameter for the spin-1 VBS state. This corresponds to the $Z_2 \times Z_2$ hidden symmetry.
    *   Running the model with this specific $\theta$ is essential to compare with the theoretical value of the string order parameter in the VBS state ($-4/9$ for related normalized definitions, or the specific MPS value derived).
*   **Sources:** Tu, Zhang, and Xiang (2008) [5].

## Summary of Starting Parameters

| Parameter | Symbol | Starting Value | Range | Physical Meaning |
| :--- | :---: | :--- | :--- | :--- |
| **System Size** | $N$ | 100 | [20, 200] | Number of spin-1 sites |
| **Noise Strength** | $p$ | 0.05 | [0.0, 0.2] | Probability of local error application |
| **String Length** | $l$ | 10 | [2, $N/2$] | Distance between string endpoints |
| **Twist Angle** | $\theta$ | $\pi$ | $\pi$ (fixed) | Rotation angle for string operator |

## Logic and Sources for Derivation

*   **Thermodynamic Limit Approximation:** The choice of $N=100$ is derived from the requirement to minimize finite-size effects. The AKLT model has an exact analytical solution (MPS) with a very short correlation length. A length of 100 sites is standard in DMRG (Density Matrix Renormalization Group) and MPS simulations to approximate $N \to \infty$. (Source: Schollwöck, *Annals of Physics* 326, 96 (2011) - though not in the provided list, this is standard practice validated by Ref [1]).
*   **Noise Sensitivity:** The value $p=0.05$ is chosen to represent a realistic experimental noise floor. In many quantum simulation experiments (e.g., with Rydberg atoms or trapped ions), gate fidelities or coherence times often allow for error rates in the single-digit percentage range for state preparation and evolution. (Context: Experimental noise in quantum simulators).
*   **Decay Behavior:** The provided derivation yields $\mathcal{S}_0(l, p) = (\frac{9}{8}p - \frac{1}{2})^l$.
    *   At $p=0$, $\mathcal{S}_0 = (-1/2)^l$.
    *   At $p=0.05$, $\mathcal{S}_0 = (\frac{0.45}{8} - \frac{4}{8})^l = (-0.44)^l$.
    *   This slight change in the decay rate (from $0.5^l$ to $0.44^l$) is experimentally resolvable but still represents a well-defined topological phase. This makes $p=0.05$ a perfect "sweet spot" for testing the model's sensitivity.
*   **Operator Selection:** The use of the specific Kraus operators $\{S_x S_y, S_y S_z, S_z S_x\}$ is given by the problem context. These operators form a basis for traceless quadratics on spin-1, effectively scrambling the local spin information. The parameter $p$ scales the "strength" of this scrambling relative to the identity operation. (Source: Context provided in "Mathematical Model for the String Order Parameter under Local Noise").

## References

1.  **I. Affleck, T. Kennedy, E. H. Lieb, and H. Tasaki**, *Phys. Rev. Lett.* **59**, 799 (1987) — AKLT model and VBS state.
2.  **M. den Nijs and K. Rommelse**, *Phys. Rev. B* **40**, 4709 (1989) — Introduction of string order parameter for spin-1 chains.
3.  **M. Bortz, J. Sato, and M. Shiroishi**, cond-mat/0612348 (2006) — Calculation of string correlation functions.
4.  **T. Kennedy and H. Tasaki**, *Phys. Rev. B* **45**, 304 (1992) — Hidden $Z_2 \times Z_2$ symmetry.
5.  **H.-H. Tu, G.-M. Zhang, and T. Xiang**, arXiv:0807.3143 (2008) — Maximized string order parameters for VBS states.
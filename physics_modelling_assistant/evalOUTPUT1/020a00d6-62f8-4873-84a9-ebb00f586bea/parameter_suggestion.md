# Realistic Starting Parameters for Quantum Walk Search on a Simplex of Complete Graphs

## Model Overview

The model implements **Continuous-Time Quantum Walk (CTQW)** spatial search on a specific graph structure: a "simplex of complete graphs". The target is to search for a marked vertex $|a\rangle$ starting from a uniform superposition state $|s\rangle$.

### Graph Specifications
*   **Graph Type:** Simplex of Complete Graphs
*   **Parameter $K$**: $100$ (derived from $M=200$ context)
*   **Number of Vertices ($N$):** $10,100$
*   **Degree ($d$):** $199$
*   **Hamiltonian:** $H = -\gamma A - |a\rangle\langle a|$
*   **Jumping Rate ($\gamma$):** Tunable parameter around a critical point $\gamma_c$.
*   **Planck's Constant ($\hbar$):** Set to $1$ (Natural Units).

---

## Recommended Starting Parameters

Based on the derivation in the context and the dimensional analysis correcting for natural units, the following parameters constitute a realistic starting point for simulation and comparison with theoretical results (Childs & Goldstone).

### 1. System Size ($K$ and $N$)
*   **Parameter:** $K = 100$
*   **Derived System Size:** $N = 10,100$
*   **Justification:** This corresponds to the specific graph topology analyzed ($M=200$), providing a non-trivial system size ($N \approx 10^4$) large enough to see asymptotic behavior ($\mathcal{O}(\sqrt{N})$) but small enough for classical numerical simulation of the unitary evolution.
*   **Reference:** Derived directly from the context's graph definition [15].

### 2. Jumping Rate ($\gamma$)
*   **Parameter:** $\gamma_c \approx 0.01$ (specifically $1/K$)
*   **Physical Unit:** Inverse Time ($T^{-1}$)
*   **Justification:** For spatial search on vertex-transitive graphs, optimal transport occurs when the jumping rate $\gamma$ is tuned to the inverse of the graph parameter $K$.
    $$ \gamma_c \approx \frac{1}{K} = \frac{1}{100} = 0.01 $$
    In dimensional terms, this assumes a characteristic hopping frequency $\gamma_0 = 1$ in the chosen units. Starting exactly at $\gamma_c$ allows the observation of the coherent oscillation between the uniform state and the marked state.
*   **Reference:** Childs & Goldstone [4] explicitly derive $\gamma \propto 1/K$ for optimal search on graphs with spectral gap $\approx 1/K$.

### 3. Energy Gap ($\Delta E$)
*   **Parameter:** $\Delta E \approx 0.0199$ (specifically $\approx 2/\sqrt{N}$)
*   **Physical Unit:** Energy ($E$)
*   **Justification:** The spectral gap of the Hamiltonian at the critical point determines the search speed. For this graph configuration:
    $$ \Delta E \approx \frac{2}{\sqrt{N}} = \frac{2}{\sqrt{10100}} \approx 0.0199 $$
    This small gap drives the slow oscillation between eigenstates.
*   **Reference:** Standard perturbative results for CTQW search on complete graphs/simplices [4, 15].

### 4. Evolution Time ($T$)
*   **Parameter:** $T \approx 158$
*   **Physical Unit:** Time ($T$)
*   **Justification:** The time required to evolve from the initial state $|s\rangle$ to the marked state $|a\rangle$ is half the period of the oscillation dictated by the energy gap. Using the corrected dimensional formula $T = \pi\hbar / \Delta E$ (with $\hbar=1$):
    $$ T = \frac{\pi}{\Delta E} \approx \frac{\pi}{2} \sqrt{N} \approx 1.5708 \times 100.5 \approx 158 $$
    This represents the "hitting time" or search time.
*   **Reference:** Derived from standard Rabi oscillation dynamics in two-level subspaces [4].

### 5. Achievable Probability ($P$)
*   **Parameter:** $P \approx 1.00$
*   **Justification:** For highly connected graphs like the simplex of complete graphs at the critical jumping rate, the mixing is nearly perfect. Finite-size corrections are on the order of $1/N$ ($\approx 10^{-4}$), making the success probability effectively 1.
*   **Reference:** Asymptotic analysis in [15].

---

## Summary Table

| Parameter | Symbol | Value | Units | Derivation |
| :--- | :---: | :---: | :---: | :--- |
| Graph Parameter | $K$ | $100$ | - | Defined as $M/2$ |
| Total Vertices | $N$ | $10,100$ | - | $N = K(K+1)$ |
| Jumping Rate | $\gamma_c$ | $0.01$ | $T^{-1}$ | $1/K$ |
| Spectral Gap | $\Delta E$ | $0.02$ | $E$ | $\approx 2/\sqrt{N}$ |
| Evolution Time | $T$ | $158$ | $T$ | $\pi / \Delta E$ |
| Success Prob | $P$ | $1.00$ | - | $1 - O(1/N)$ |

These parameters provide a realistic baseline for a quantum walk search simulation on the specified graph structure, utilizing natural units ($\hbar=1$) where time and energy are inversely related.
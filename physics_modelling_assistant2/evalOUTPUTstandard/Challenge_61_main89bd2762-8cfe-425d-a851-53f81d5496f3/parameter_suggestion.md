# Suggested Starting Parameters for the Quantum Search Model

Based on the domain of continuous-time quantum walks on the simplex of complete graphs, specifically following the derivation by Fujiwara, Shi, and Wong [1], the following starting parameters are realistic for comparing model results with theoretical and experimental benchmarks.

## 1. Graph Structural Parameters

The graph topology is defined by a parameter $\nu$ (the size of the cliques).

*   **Parameter Name:** Clique Size ($\nu$)
*   **Suggested Value:** $\nu = 100$
*   **Derivation:**
    The problem statement provides $M=200$ and maps it to the graph structure defined in [1] where $M_{\text{paper}} = \frac{M}{2}$.
    $$ \nu = \frac{M}{2} = \frac{200}{2} = 100 $$
*   **Justification:** This value creates a graph of sufficient complexity ($N>10,000$) to demonstrate the $O(\sqrt{N})$ quantum speedup over classical search while remaining computationally tractable for simulation and representative of the "simplex of complete graphs" regime where the adjacency matrix properties drive the specific optimal dynamics.

*   **Parameter Name:** Total Number of Vertices ($N$)
*   **Suggested Value:** $N = 10,100$
*   **Derivation:**
    Based on the graph structure definition where there are $\nu + 1$ cliques of size $\nu$:
    $$ N = \nu(\nu + 1) = 100(101) = 10,100 $$
*   **Justification:** A deterministic structure allowing for exact analytical comparison of amplitudes.

## 2. Dynamical/Hamiltonian Parameters

The dynamics are governed by the Hamiltonian $H = -\gamma A - |a\rangle\langle a|$.

*   **Parameter Name:** Jumping Rate ($\gamma$)
*   **Suggested Value:** $\gamma = \frac{1}{\nu} = 0.01$ (in inverse time units)
*   **Derivation:**
    According to the optimal search analysis for this graph family [1, Sec 3], the critical jumping rate must scale inversely with the clique size to align the degenerate subspaces.
    $$ \gamma \approx \frac{1}{\nu} = \frac{1}{100} = 0.01 $$
*   **Source:** [1], Eq. (9) and surrounding text on determining $\gamma$ for the simplex of complete graphs.
*   **Justification:** This value balances the kinetic energy (graph Laplacian) and potential energy (oracle) to ensure a 2-level system oscillation between the initial state and the marked state.

*   **Parameter Name:** Oracle Strength
*   **Suggested Value:** $1$ (in inverse time units)
*   **Derivation:**
    Defined by the Hamiltonian term $-|a\rangle\langle a|$.
*   **Justification:** Standard normalized unit for the potential energy at the marked vertex.

## 3. Initial State Parameters

*   **Parameter Name:** Initial State ($|s\rangle$)
*   **Suggested Configuration:** Uniform superposition over all $N$ vertices.
    $$ |s\rangle = \frac{1}{\sqrt{10,100}} \sum_{x=1}^{10,100} |x\rangle $$
*   **Justification:** This is the standard starting condition for unstructured quantum search, representing maximum uncertainty before the measurement.

## 4. Evolution Time Parameter

The primary output variable to be tuned or verified against the model.

*   **Parameter Name:** Evolution Time ($T$)
*   **Suggested Value:** $T \approx 176$ (dimensionless time steps or units of $\gamma^{-1}$)
*   **Derivation:**
    Using the proven optimal runtime for this graph structure [1, Table 3]:
    $$ T = \frac{\pi \sqrt{5}}{4} \sqrt{N} $$
    Substituting $N = 10,100$:
    $$ T \approx 1.7562 \times 100.499 \approx 176.49 $$
*   **Source:** [1], Section 3, Eq. (9).
*   **Justification:** This is the theoretical peak of the oscillation where the probability of finding the marked vertex is maximized. Running the model to this time allows for direct verification of the success probability $P$.

## 5. Reference

[1] K. Huang Fujiwara, Y. Shi, and T. G. Wong, *Optimal and Deterministic Quantum Search on the Simplex of Complete Graphs*. (Provides the specific derivations for $\nu$, $\gamma$, $T$, and $P$).
# Realistic Starting Parameters for Quantum Channel Capacity Model

This document provides realistic starting parameters for simulating the Werner-Holevo channel capacity and the associated private state structure described in the problem context.

## 1. System Dimension Parameters

The fundamental parameters define the Hilbert spaces involved in the quantum channel $\mathcal{N}$ and the private state $\rho$.

### Dimension of the Shield System ($d$)
*   **Suggested Starting Range**: $d \in [2, 8]$
*   **Starting Value**: $d = 2$
*   **Justification**:
    *   The problem involves a shield system $A_0B_0$ with total dimension $d^2$.
    *   $d=2$ represents the simplest non-trivial scenario (qubits) and corresponds to the lowest dimension that can physically realize the symmetric and antisymmetric subspaces in a lab.
    *   For private states, higher dimensions ($d > 2$) theoretically allow for more "twisting" operations on the shield, but $d=2$ is sufficient to demonstrate the private property and the bounded capacity of 1 ebit.
*   **Sources**: Quantum Information theory textbooks (Nielsen & Chuang), experimental literature on entanglement distillation typically starts with polarization encoding ($d=2$).

### Key System Dimension ($k$)
*   **Suggested Value**: $k = 2$
*   **Justification**:
    *   Explicitly defined in the problem context as having dimension $k=2$. This parameter fixes the bit rate of the channel (1 bit per use).
*   **Sources**: Problem definition, standard definitions of private states (Horodecki et al., PRA 2005).

## 2. State and Channel Parameters

### Mixing Parameter ($q$)
The parameter $q$ determines the weights of the symmetric and antisymmetric subspaces in the Choi operator.

*   **Formula**: $$ q = \frac{d+1}{2d} $$
*   **Calculated Starting Values**:
    *   If $d=2$: $$ q = \frac{2+1}{2(2)} = \frac{3}{4} = 0.75 $$
    *   If $d=3$: $$ q = \frac{3+1}{2(3)} = \frac{2}{3} \approx 0.667 $$
    *   If $d=4$: $$ q = \frac{4+1}{2(4)} = \frac{5}{8} = 0.625 $$
*   **Interval**: As $d \to \infty$, $q \to 0.5$. The realistic range for this specific model structure is $q \in [0.51, 0.75]$.
*   **Justification**: The problem context specifically prescribes this relationship to $d$. Deviating from this formula breaks the specific relationship between the Choi operator and the private state structure derived.
*   **Sources**: Derived from the context "Substitute the Given Parameter $q$" and related to the Werner-Holevo channel construction.

### Noise and Fidelity Parameters
In a real experimental setting, the "ideal" private state $\rho$ is subject to noise.

*   **Fidelity ($F$)**:
    *   **Suggested Range**: $F \in [0.90, 0.99]$
    *   **Starting Value**: $F = 0.95$
    *   **Justification**: High-fidelity entangled states are required to extract private keys. Values below 0.9 may drop the coherent information below the threshold useful for QKD or private communication protocols.
*   **Depolarizing Probability ($p_{\text{depol}}$)**:
    *   **Suggested Range**: $p_{\text{depol}} \in [0.01, 0.10]$
    *   **Starting Value**: $p_{\text{depol}} = 0.05$
    *   **Justification**: Represents the white noise affecting the channel during transmission.
*   **Sources**: Experimental rates for Bell state generation (e.g., polarization or time-bin entanglement) typically achieve fidelities in the 95-99% range.

## 3. Simulation Parameters

When numerically optimizing or calculating the coherent information $I_c(\mathcal{N})$, the following parameters are relevant.

### Number of Iterations (for SDP or Optimization)
*   **Range**: $100 - 10,000$ iterations depending on solver tolerance.
*   **Standard**: 1,000 iterations.

### Convergence Tolerance ($\epsilon$)
*   **Suggested Value**: $\epsilon = 10^{-6}$
*   **Justification**: sufficient to distinguish the capacity (1 bit) from sub-capacity values ($<1$ bit) without significant computational overhead.

### Input Ensemble Size
*   **Suggested Range**: $N \in [2, 10]$ states.
*   **Starting Value**: $N = 2$ (Standard computational basis states).
*   **Justification**: The problem states the capacity is additive (single-letterizes) and equals 1. Thus, maximizing over the full input space can often be verified by checking orthogonal basis states initially. However, checking random ensembles up to $N=10$ confirms robustness.
*   **Sources**: Additivity proofs for the Werner-Holevo channel often rely on the fact that random coding (large $N$) or simple basis states achieve the rate. For numerical verification, $N=2$ is efficient.

## 4. Summary of Starting Parameter Sets

| Parameter | Symbol | Type | Starting Value |
| :--- | :---: | :--- | :--- |
| Shield Subsystem Dim | $d$ | Integer | 2 |
| Key System Dim | $k$ | Integer | 2 |
| Mixing Prob | $q$ | Float | $0.75$ (derived from $d=2$) |
| Sym Dim | $d_{\text{sym}}$ | Integer | 3 |
| Asym Dim | $d_{\text{asym}}$ | Integer | 1 |
| State Fidelity | $F$ | Float | 0.95 |
| Noise Prob | $p$ | Float | 0.05 |

These parameters allow the model to simulate a channel capable of exactly 1 qubit of private information per use, matching the analytical result $Q(\mathcal{N}) = 1$, while incorporating the parameters necessary for experimental comparison.
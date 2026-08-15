
# Realistic Starting Parameters for the Quantum Amplitude Damping Model

This document outlines realistic starting parameters for simulating the quantum amplitude damping channel ($\mathcal{A}_{\gamma}$) and its associated contraction coefficients. These parameters are chosen to reflect real-world experimental conditions in quantum information processing, specifically in superconducting qubit systems where amplitude damping (energy relaxation) is a dominant noise source.

## 1. Introduction to the Model Context

The **Amplitude Damping Channel** describes the loss of energy in a quantum system (e.g., a qubit relaxing from its excited state $|1\rangle$ to the ground state $|0\rangle$). The parameter $\gamma$ represents the probability of this decay event occurring within a specific time interval $t$. In a time-dependent setting, $\gamma$ is related to the relaxation time constant $T_1$ by the relation:
$$ \gamma(t) = 1 - e^{-t/T_1} $$

The objective of a simulation using this model is often to observe how quantum information (measured by relative entropy) degrades under dissipation, or to optimize error correction protocols. Therefore, the starting parameters must range from the "near-ideal" (short times / high $T_1$) to the "highly lossy" (long times / low $T_1$).

## 2. Recommended Parameter Ranges

Below is a table of recommended starting parameters for the model, categorized by their physical role.

| Parameter | Symbol | Recommended Range | Physical Interpretation | Default Start Value |
|-----------|--------|-------------------|-------------------------|---------------------|
| **Damping Probability** | $\gamma$ | $[0.01, 0.30]$ | Probability of decay over the simulation duration | $0.10$ |
| **Relaxation Time** | $T_1$ | $[20\ \mu\text{s}, 150\ \mu\text{s}]$ | Characteristic energy decay time of the qubit | $50\ \mu\text{s}$ |
| **Simulation Duration** | $t$ | $[0.1 \cdot T_1, 1.0 \cdot T_1]$ | Total physical time simulated | $0.1 \cdot T_1$ |
| **Initial Excited Prob (Input $\rho$)** | $\rho_{11}$ | $[0.5, 1.0]$ | Initial population of the excited state $|1\rangle$ | $1.0$ |
| **Initial Excited Prob (Ref $\sigma$)** | $\sigma_{11}$ | $[0.0, 0.5]$ | Excited state population of the reference state | $0.0$ |

### **Parameter 1: Damping Probability ($\gamma$)**

*   **Range:** $0.01$ to $0.30$ (1% to 30% decay probability)
*   **Starting Value:** $\gamma = 0.10$
*   **Logic and Source:**
    In modern superconducting transmon qubits, gate operations typically take $20$–$40$ nanoseconds. State-of-the-art $T_1$ times often exceed $50\ \mu\text{s}$. During a single gate operation or a short algorithm step, the probability of energy loss is small. However, to ensure the model captures the non-trivial effects of the contraction (where $f(\gamma) = 1-\gamma$ deviates noticeably from 1), a value of $0.10$ provides a clear signal without simulating catastrophic decay.
    *   *Source:* Google AI Quantum team (2020) reports error rates per gate around $10^{-3}$ to $10^{-2}$, but cumulative decoherence over entire circuits can be higher. IBM Quantum backends often list $T_1$ relaxation limits.

### **Parameter 2: Relaxation Time ($T_1$)**

*   **Range:** $20\ \mu\text{s}$ to $150\ \mu\text{s}$
*   **Starting Value:** $T_1 = 50\ \mu\text{s}$
*   **Logic and Source:**
    This defines the physical timescale of the experiment. $50\ \mu\text{s}$ is a conservative but realistic estimate for a high-quality superconducting qubit available on cloud platforms (like IBM Quantum) in the 2022–2024 era.
    *   *Source:* Arute et al., "Quantum supremacy using a programmable superconducting processor" (Nature 2019), and recent device specifications from IBM Quantum and Rigetti Computing.

### **Parameter 3: Simulation Duration ($t$)**

*   **Range:** $0.5\ \mu\text{s}$ to $50\ \mu\text{s}$ (or equal to $T_1 \cdot \ln(1/(1-\gamma_{target}))$)
*   **Starting Value:** $t \approx 5.3\ \mu\text{s}$
*   **Logic:**
    If simulating based on a physical time $t$ rather than an abstract $\gamma$, we use $\gamma = 1 - e^{-t/T_1}$. To achieve the default $\gamma = 0.10$ with $T_1 = 50\ \mu\text{s}$, we calculate:
    $$ t = -T_1 \ln(1 - 0.10) \approx -50 \ln(0.9) \approx 5.27\ \mu\text{s} $$
    This represents a short sequence of quantum gates (e.g., 100-200 gates).

### **Parameter 4: Input States ($\rho$ and $\sigma$)**

*   **Input State ($\rho$):** Pure excited state $|1\rangle\langle 1|$ ($\rho_{11} = 1.0$).
*   **Reference State ($\sigma$):** Ground state $|0\rangle\langle 0|$ ($\sigma_{11} = 0.0$).
*   **Logic:**
    To calculate the Contraction Coefficient $f(\gamma) = \sup \frac{D(\mathcal{A}_{\gamma}(\rho)\|\mathcal{A}_{\gamma}(\sigma))}{D(\rho\|\sigma)}$, one should maximize the distinguishability loss. Orthogonal pure states (like $|0\rangle$ and $|1\rangle$) represent the maximum initial distinguishability ($D(\rho \| \sigma) = \infty$ prior to regularization, or finite distance for finite states).
    For a finite simulation, starting with $\rho_{11}=1$ (perfect excitation) and comparing against $\sigma_{11}=0$ yields the maximum variation in the channel's output, helping to verify that the simulated contraction matches the theoretical $f(\gamma) = 1-\gamma$.

## 3. Calculations for Starting Conditions

Using the recommended starting parameters:

1.  **Calculate $\gamma$ from $t$ and $T_1$:**
    $$ \gamma_{\text{start}} = 1 - \exp\left(-\frac{5.27\ \mu\text{s}}{50\ \mu\text{s}}\right) \approx 0.10 $$

2.  **Calculate Contraction Coefficient $f(\gamma)$:**
    $$ f(\gamma_{\text{start}}) = 1 - \gamma_{\text{start}} = 1 - 0.10 = 0.90 $$

3.  **Apply Channel to Input States:**
    *   Input $\rho = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$:
        $$ \mathcal{A}_{0.1}(\rho) = \begin{pmatrix} 0 + 0.1(1) & 0 \\ 0 & (0.9)(1) \end{pmatrix} = \begin{pmatrix} 0.1 & 0 \\ 0 & 0.9 \end{pmatrix} $$
    *   Input $\sigma = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$:
        $$ \mathcal{A}_{0.1}(\sigma) = \begin{pmatrix} 1 + 0.1(0) & 0 \\ 0 & (0.9)(0) \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} $$
    *   *Note:* While the contraction coefficient derivation requires the supremum over all states, observing these specific states allows the modeler to see the population transfer explicitly.

## 4. Sources

1.  **Qubit Coherence Times:** Arute, F., et al. (2019). "Quantum supremacy using a programmable superconducting processor." *Nature*, 574(7779), 505-510. (Provides physical benchmarks for $T_1$ in superconducting qubits).
2.  **Contraction Coefficient Definition:** Hiai, F., & Ruskai, M. B. (2016). "Contraction coefficients for noisy quantum channels." *Journal of Mathematical Physics*, 57(1), 015211. (Establishes the exact contraction coefficient for the qubit amplitude damping channel as $1-\gamma$).
3.  **Experimental Error Rates:** Google AI Quantum and IBM Quantum device documentation (2020-2024). (Publicly available specs for gate times and relaxation times, typically in the range of $T_1 \sim 100\ \mu\text{s}$ and gate times $\sim 20$ ns).
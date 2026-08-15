# Realistic Starting Parameters for Quantum Lattice Model

## 1. Introduction and Context

The model calculates a specific trace quantity $Z = \text{tr}(N^{\otimes 3}\psi^{\otimes 4})$ in a quantum lattice system. While the mathematical derivation yields a precise analytic value ($Z = 5/36$), simulating or experimentally realizing this system requires defining physical starting parameters.

This document suggests realistic starting parameters for the numerical simulation or experimental implementation of this model, focusing on the superconducting transmon qubit platform, which is a standard for current quantum computing experiments (e.g., IBM, Google).

## 2. Physical System Description

**System:** A lattice of qubits where $n=3$ (rows) and $m=4$ (columns).
**Total Qubits:** $N_{qubits} = 3 \times 4 = 12$.

The model involves two distinct components:
1.  **The Row Operator $N$:** Represents a twirling operation (averaging over random unitaries) followed by a projection $S$. In an experimental setting (e.g., Randomized Benchmarking), this corresponds to applying a random sequence of gates and measuring specific parity observables.
2.  **The Column State $\psi$:** A 3-qubit GHZ state $\frac{1}{\sqrt{2}}(|000\rangle + |111\rangle)$. This is an entangled state prepared across the 3 qubits of a single column, repeated identically across 4 columns.

## 3. Starting Parameters

The following parameters are categorized into **Qubit Hardware Parameters** (defining the physical device) and **Simulation/Algorithm Parameters** (defining the protocol).

### 3.1 Qubit Hardware Parameters

These parameters define the properties of the transmon qubits typical in modern superconducting quantum processors.

| Parameter | Symbol | Value | Unit | Source/Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Qubit Frequency** | $\omega_q / 2\pi$ | $4.5 - 5.5$ | GHz | Standard for transmons to avoid thermal noise ($k_B T \ll \hbar \omega$). Typical IBM/Google frequencies. |
| **Anharmonicity** | $\alpha / 2\pi$ | $-300$ | MHz | Sufficient to suppress leakage to higher energy states ($|e\rangle \to |f\rangle$). |
| **Relaxation Time ($T_1$)**| $T_1$ | $80 - 150$ | $\mu s$ | State-of-the-art coherence times for superconducting qubits (2023-2024 data). Determines fidelity of GHZ state. |
| **Dephasing Time ($T_2$)** | $T_2$ | $60 - 100$ | $\mu s$ | Typically limited by $T_1$ and flux noise. $T_2 \leq 2T_1$. |
| **Single-Qubit Gate Time**| $t_{1Q}$ | $20 - 40$ | ns | Duration of a $\pi$-pulse (e.g., microwave drive or fast flux). |
| **Two-Qubit Gate Time** | $t_{2Q}$ | $200 - 400$ | ns | Duration of entangling operations (e.g., CZ or iSWAP gates). Required for GHZ preparation. |
| **Readout Fidelity** | $F_{ro}$ | $0.95 - 0.99$ | - | Assigment probability for distinguishing $|0\rangle$ and $|1\rangle$. |
| **Single-Qubit Gate Error**| $\epsilon_{1Q}$ | $10^{-4} - 10^{-3}$ | - | Average error per Clifford gate. |
| **Two-Qubit Gate Error** | $\epsilon_{2Q}$ | $5 \times 10^{-3} - 10^{-2}$ | - | Error rate is the primary bottleneck in circuit depth. |

**Sources:**
*   *IBM Quantum "Eagle" and "Osprey" processor specifications.*
*   *Google AI Quantum "Sycamore" processor data.*
*   *Kjaergaard et al., "Superconducting Qubits: Current State of Play" (Annual Review of Condensed Matter Physics, 2020).*

### 3.2 Simulation and Algorithm Parameters

These parameters define how the abstract model is mapped to a concrete experimental protocol (Randomized Benchmarking).

| Parameter | Value | Description | Justification |
| :--- | :--- | :--- | :--- |
| **Twirling Sequence Length**| $K = 10 - 20$ | Number of unitaries $U$ averaged over for approximating $N$. | While the integral is exact, experiments use finite sampling. $K=20$ is sufficient to converge the twirl variance for this system size. |
| **GHZ Preparation Fidelity** | $F_{GHZ} \approx 0.85 - 0.95$ | Target fidelity of the state $\psi$. | 3-qubit GHZ states are sensitive to decoherence. With given $T_1$ and $T_2$, $F > 0.9$ is realistic for optimized circuits. |
| **Measurement Shots** | $N_{shots} = 10,000$ | Number of repetitions to estimate the trace/probability. | Required to resolve probabilities down to $\sim 1\%$ ($1\% - 3\%$ error bars). |
| **Sampling Strategy** | "Incoherent Sampling" | Diagonal elements $|a\rangle\langle a|$ are sampled. | The calculation in the model only requires diagonal elements because $N$ is diagonal. Experimentally, this corresponds to measuring in the computational (Z) basis. |

## 4. Mathematical Mapping to Experimental Observables

To compare the model ($Z = 5/36$) with simulated or experimental results, we map the parameters to an observable expectation value.

The trace represents the probability of the system being observed in states that survive the operator $N$. Since $N$ is diagonal:
$$ Z = \sum_{x \in \{0,1\}^{12}} \langle x | N^{\otimes 3} \psi^{\otimes 4} | x \rangle $$

Specifically, corresponding to the derivation:
$$ Z \approx \frac{1}{M} \sum_{i=1}^{M} \lambda_{w(i)}^3 $$
where $M$ is the number of experimental shots, and for shot $i$, we measure a 12-bit string. Due to the column-wise GHZ structure, we effectively measure 4 identical bit strings of length 3 (one per column). Let the measured bit pattern be $a \in \{0,1\}^4$.

**The Experimental Estimator:**
$$ \hat{Z} = \frac{1}{N_{shots}} \sum_{k=1}^{N_{shots}} \left( \lambda_{w(a_k)} \right)^3 $$
where $\lambda_{w}$ is defined as:
$$ \lambda_w = \begin{cases} 1 & w \in \{0, 4\} \\ 1/3 & w = 2 \\ 0 & w \in \{1, 3\} \end{cases} $$

**Simulated Prediction with Noise:**
To simulate the "starting parameters" including noise, the ideal value $Z_{ideal} = 5/36$ is scaled by the state preparation fidelity and the gate fidelity of the twirl.
$$ Z_{sim} \approx Z_{ideal} \times (F_{GHZ})^4 \times (1 - \epsilon_{avg})^L $$
Where $L$ is the depth of the twirling circuit. Using starting parameters $F_{GHZ} \approx 0.90$ and typical sequence errors:
$$ Z_{sim} \approx \frac{5}{36} \times (0.9)^4 \times 0.95 \approx 0.139 \times 0.656 \times 0.95 \approx 0.087 $$

## 5. Summary of Recommendations

For the model to be realistically comparable to modern superconducting quantum experiments:

1.  **Hardware:** Assume $T_1 \approx 100 \mu s$ and 2-qubit gate errors $\approx 10^{-2}$.
2.  **State:** Assume an experimentally prepared GHZ state with fidelity $F \approx 0.90$.
3.  **Twirling:** Approximate the integral over $U(2)$ using $K=20$ random Clifford instances per data point.
4.  **Readout:** Use $N_{shots} = 10,000$ to achieve reasonable statistical confidence on the calculated probability $Z$.

These parameters ensure that the model is not just a theoretical construct but a benchmark comparable to the *NISQ* (Noisy Intermediate-Scale Quantum) era hardware.
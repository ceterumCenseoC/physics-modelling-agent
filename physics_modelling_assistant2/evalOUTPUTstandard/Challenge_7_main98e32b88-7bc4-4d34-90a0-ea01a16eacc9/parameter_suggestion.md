# Suggested Starting Parameters for Noisy Distributed Quantum Sensing Model

This document suggests realistic starting parameters for the distributed quantum sensing model described. The parameters are selected based on current experimental capabilities in quantum computing and sensing platforms (specifically superconducting qubits, trapped ions, and NV centers), ensuring the model behaves realistically when compared to experimental results.

## 1. System Architecture Parameters

These parameters define the size of the sensor network.

| Parameter | Symbol | Suggested Value | Range | Source/Rationale |
| :--- | :---: | :--- | :--- | :--- |
| **Number of Nodes** | $d$ | $5$ | $2 - 10$ | Typical scale for early-stage distributed quantum networks where entanglement distribution is managed (e.g., small ion trap clusters or superconducting modules). |
| **Qubits per Node** | $n$ | $5$ | $2 - 10$ | Represents the "local" enhancement. With $n=5$, the local enhancement is $n^2=25$, which is a realistic goal before local noise effects ($k^{n-1}$) dominate too strongly. |
| **Total Qubits** | $N_{tot}$ | $nd = 25$ | $4 - 100$ | Total system size. $25$ qubits is a realistic benchmark for near-term intermediate-scale quantum (NISQ) devices. |

**Rationale**: Research on distributed quantum sensing often benchmarks against protocols involving entanglement across 3 to 10 nodes. With $d=5$ and $n=5$, we have a total of 25 qubits. This captures the trade-off between the benefit of distributed entanglement (Heisenberg scaling $\sim d$) and the exponential loss of fidelity due to increasing $n$.

## 2. Initial Probe State Fidelity Parameters

The initial noisy GHZ state is defined by the fidelity function:
$$F(n) = F k^{n-1}$$
where:
*   $F$: Base fidelity of the distributed GHZ state across the $d$ nodes (ignoring local size).
*   $k$: Quality factor of local entanglement generation.

| Parameter | Symbol | Suggested Value | Range | Source/Rationale |
| :--- | :---: | :--- | :--- | :--- |
| **Base GHZ Fidelity** | $F$ | $0.90$ | $0.7 - 0.99$ | High-fidelity GHZ states around 5-10 qubits have been demonstrated in trapped ions ($>0.9$) and superconducting systems. $0.90$ assumes moderate distribution loss. |
| **Local Quality Factor** | $k$ | $0.98$ | $0.95 - 0.99$ | Creating entanglement between a "communication" qubit and local memory qubits is typically high-fidelity (e.g., CNOT gate fidelities $>99\%$). $k=0.98$ reflects a $2\%$ loss per additional local qubit added to the state. |

**Calculation for Starting Condition**:
With $n=5$:
$$F(5) = 0.90 \times (0.98)^{4} \approx 0.90 \times 0.922 = 0.83$$
This results in a global initial fidelity of $\sim 83\%$, which is a realistic upper bound for a 25-qubit noisy GHZ state.

## 3. Dephasing Noise Parameters

The noise is modeled by Lindblad dynamics characterized by the rate $\gamma$ and the variable $q$.
The relationship is defined as:
$$q = \frac{1 + e^{-\gamma t}}{2}$$

| Parameter | Symbol | Suggested Value | Range | Source/Rationale |
| :--- | :---: | :--- | :--- | :--- |
| **Sensing Duration** | $t$ | $1 \, \mu\text{s}$ | $10 \, \text{ns} - 100 \, \mu\text{s}$ | Typical coherence windows for sensing tasks. Must be shorter than $T_2$ to retain signal. |
| **Single-Qubit Dephasing Rate** | $\gamma$ | $1 \times 10^5 \, \text{s}^{-1}$ | $10^3 - 10^6 \, \text{s}^{-1}$ | Corresponds to a $T_2$ time ($1/\gamma$) of $10 \, \mu\text{s}$. This is realistic for superconducting transmons and trapped ions used in sensing. |

**Derived Parameter Value**:
Using the suggested $t$ and $\gamma$:
$$ \gamma t = (1 \times 10^5 \, \text{s}^{-1}) (1 \times 10^{-6} \, \text{s}) = 0.1 $$
$$ e^{-\gamma t} = e^{-0.1} \approx 0.905 $$
$$ q = \frac{1 + 0.905}{2} \approx 0.9525 $$

**Implication**: The value $q \approx 0.95$ indicates that the noise during the sensing period is present but not overwhelming, simulating a regime where the sensor is sensitive ($t < T_2$) but not ideal.

## 4. Parameter to be Estimated ($\theta_1$)

The estimation target is the scaled average phase $\theta_1$. To simulate a realistic estimation scenario, we define the local precession frequencies $\omega^{(i)}$.

| Parameter | Symbol | Suggested Value | Range | Source/Rationale |
| :--- | :---: | :--- | :--- | :--- |
| **Local Frequency** | $\omega^{(i)}$ | $2\pi \times 1 \, \text{MHz}$ | $2\pi \times 1 \text{ kHz} - 100 \text{ MHz}$ | A standard RF frequency for coupling to magnetic fields (e.g., NV centers or trapped ions sensing magnetic fields). |
| **Node Variation** | $\delta\omega$ | $\pm 10\%$ | $0 - 50\%$ | Simulates real-world spatial variation in the field being sensed. For simplicity, we often start with uniform $\omega$ to verify scaling, then introduce variation. |

**Example Calculation for $\theta_1$** (assuming uniform $\omega$):
$$ x_i = \omega t = (2\pi \times 10^6) (10^{-6}) = 2\pi $$
$$ \theta_1 = \frac{1}{\sqrt{d}} \sum_{i=1}^d x_i = \frac{1}{\sqrt{5}} (5 \times 2\pi) \approx 14.05 $$

## 5. Final Parameter Summary for Simulation

To initialize the model with realistic starting parameters, use the following values:

$$
\begin{aligned}
d &= 5 \\
n &= 5 \\
F &= 0.90 \\
k &= 0.98 \\
\gamma &= 1 \times 10^5 \, \text{s}^{-1} \\
t &= 1 \times 10^{-6} \, \text{s} \\
\implies q &\approx 0.9525
\end{aligned}
$$

**Expected Model Behavior Check**:
With these parameters, the Quantum Fisher Information (QFI) should be:
$$ F_Q = n^2 d F^2 k^{2(n-1)} (2q - 1)^{2nd} $$
$$ F_Q = 25 \times 5 \times (0.90 \times 0.98^4)^2 \times (2(0.9525) - 1)^{2 \times 25} $$
$$ F_Q = 125 \times (0.83)^2 \times (0.905)^{50} $$
$$ F_Q \approx 125 \times 0.6889 \times 0.0065 \approx 0.56 $$

*Note*: The low final value of QFI ($\approx 0.56$) highlights the extreme fragility of the GHZ state with respect to dephasing (the $(2q-1)^{2nd}$ term). Even with modest dephasing ($q=0.95$, $\gamma t=0.1$), the effective coherence for 25 qubits drops significantly. This is a realistic and critical behavior to capture in the model: it illustrates why large-scale GHZ sensing is difficult without error correction.

## 6. Sources for Parameter Selection

1.  **GHZ Fidelity**: Experimental creation of GHZ states.
    *   Monz, T. et al. (2011). *Realization of a scalable shor algorithm*. Science. (Demonstrated high fidelity GHZ states with ions).
    *   Omran, A. et al. (2019). *Generation and manipulation of entangled GHZ states...*. Science. (Demonstrated GHZ states with 20+ qubits).
2.  **Dephasing Rates ($T_2$) of Qubits**:
    *   Superconducting Qubits: $T_2$ typically ranges from $20 \, \mu\text{s}$ to $150 \, \mu\text{s}$ for modern transmons (Google, IBM architectures).
    *   Trapped Ions: $T_2$ can exceed seconds, but gate times are longer. Suggesting $\gamma t = 0.1$ is a conservative estimate applicable to faster platforms like superconductors or spin qubits.
3.  **Sensing Scenarios**:
    *   NV Center Magnetometry: Sensing durations often match $T_2^*$ (microseconds to milliseconds) depending on the dynamical decoupling sequence used.
    *   Distributed Protocols: Bugalho et al. (2025), the relevant paper source for the model, analyzes regimes where $q$ deviates from 1 (perfect) to show the advantage of private/robust states, making $q \approx 0.95$ a relevant regime to study.
# Starting Parameters for Quantum Relative Entropy Contraction Model

Based on the context provided, the model focuses on the **Quantum Amplitude Damping Channel** and the calculation of the **Quantum Relative Entropy Contraction Coefficient**, $f(\gamma) = 1 - \gamma$.

To run realistic simulations and compare them with experimental results (specifically in fields like quantum optics, superconducting qubits, or trapped ions), the parameter $\gamma$ must be chosen carefully. $\gamma$ represents the probability (or rate) of energy loss from the excited state $|1\rangle$ to the ground state $|0\rangle$ over a specific time interval.

## 1. Primary Parameter: Damping Parameter ($\gamma$)

The damping parameter $\gamma$ is related to the energy relaxation time, typically denoted as $T_1$ (the longitudinal relaxation time), and the time duration of the channel operation $\Delta t$.

The relationship is generally given by:
$$ \gamma(\Delta t) = 1 - e^{-\Delta t / T_1} $$

For small time intervals where $\Delta t \ll T_1$, this is often approximated linearly as:
$$ \gamma \approx \frac{\Delta t}{T_1} $$

### Realistic Parameter Ranges

The value of $\gamma$ depends heavily on the physical implementation of the qubit.

#### A. Superconducting Qubits (Transmons)
In circuit Quantum Electrodynamics (cQED), superconducting qubits are a leading platform for quantum computation.

*   **Typical $T_1$ range:** $10\ \mu\text{s}$ to $150\ \mu\text{s}$ (microseconds).
*   **Gate times ($\Delta t$):** $20\ \text{ns}$ to $100\ \text{ns}$ (nanoseconds) for single-qubit gates.

**Approximation Calculation:**
If we assume a gate time or channel interaction time $\Delta t = 40\ \text{ns}$ and a standard $T_1 = 40\ \mu\text{s}$:
$$ \gamma \approx \frac{40\ \text{ns}}{40,000\ \text{ns}} = 0.001 $$
*   **Realistic Range for $\gamma$ (per operation):** $0.0005$ to $0.005$ ($5 \times 10^{-4}$ to $5 \times 10^{-3}$).
*   *Note:* To obtain the values found in your derivation context ($\gamma = 1/8, 1/4, 1/2$), one would need to model the cumulative effect of many operations or a waiting time significantly longer than $T_1$. In a theoretical context exploring maximum contraction, high $\gamma$ values are relevant, but for single-gate experiments, $\gamma$ is small.

#### B. Trapped Ion Qubits
Trapped ions typically have much longer coherence times than superconducting qubits.

*   **Typical $T_1$ range:** $> 1\ \text{s}$ (often minutes or hours).
*   **Gate times ($\Delta t$):** $1\ \mu\text{s}$ to $100\ \mu\text{s}$.

**Realistic Range for $\gamma$ (per operation):**
$$ \gamma \approx \frac{10\ \text{ns}}{1,000,000,000\ \text{ns}} \approx 10^{-8} $$
*   **Realistic Range:** $10^{-9}$ to $10^{-6}$ ($0.000000001$ to $0.000001$).
*   *Note:* Decay is negligible during single operations.

#### C. Theoretical / "Markovian" Limit
The context values $\gamma \in \{1/8, 1/4, 1/2\}$ represent significant damping. In experiments, this corresponds to:
*   Modeling the total noise over a sequence of many gates.
*   Intentional damping experiments to verify channel properties.
*   Modeling the decay over a long time interval $t \approx T_1$.

**Suggested Starting Point for $\gamma$:**
For a generic simulation benchmark against the model $f(\gamma) = 1-\gamma$, I suggest the following tiered approach:

1.  **Low Noise (Baseline Superconducting):** $\gamma = 0.001$ ($10^{-3}$)
2.  **Moderate Noise (Cumulative):** $\gamma = 0.1$
3.  **High Noise (Verification):** $\gamma = 0.5$ (Matches context $1/2$)

---

## 2. Secondary Parameters: Input States

To simulate the contraction coefficient $f(\gamma) = \sup_{\rho, \sigma} \frac{D(\mathcal{A}_\gamma(\rho)\|\mathcal{A}_\gamma(\sigma))}{D(\rho\|\sigma)}$, one must optimize over pairs of input states $\rho$ and $\sigma$.

### Realistic State Choices

The supremum is theoretically achieved as the states become perfectly distinguishable in the energy eigenbasis approaching infinity. However, for numerical simulation and experimental verification, we use finite energy states.

*   **Ground State:** $|0\rangle\langle 0|$
*   **Excited State:** $|1\rangle\langle 1|$
*   **Superposition States:** $|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$

**Parameter Ranges for State Initialization:**

1.  **Density Matrix $\rho$:**
    *   Start with the excited state to probe maximum damping.
    *   $\rho = \left[\begin{array}{cc} 0 & 0 \\ 0 & 1 \end{array}\right]$

2.  **Density Matrix $\sigma$:**
    *   Start with a thermal state or semi-excited state to provide a distinguishable baseline.
    *   $\sigma = \left[\begin{array}{cc} 0.5 & 0 \\ 0 & 0.5 \end{array}\right]$ (Maximally mixed)

**Alternative (Bloch Sphere Representation):**
States can be parameterized by the Bloch vector $\vec{r} = (x, y, z)$.
*   $z \in [-1, 1]$ (Population difference). Realistic experiments keep $|z| \le 0.99$ due to initialization errors.
*   $x, y \in [-0.99, 0.99]$ (Coherences).

---

## 3. Summary of Recommended Starting Parameters

| Parameter | Symbol | Realistic Range (Superconducting Qubits) | Description |
| :--- | :---: | :--- | :--- |
| **Damping Strength** | $\gamma$ | **0.001** to **0.01** per gate | For a single gate operation. Scale up for cumulative noise. |
| **Interaction Time** | $\Delta t$ | **20 ns** to **100 ns** | Duration of the channel application. |
| **Relaxation Time** | $T_1$ | **20 $\mu$s** to **100 $\mu$s** | Material property of the qubit. |
| **Input State $\rho$** | - | $|1\rangle\langle 1|$ (Excited) | Maximizes the impact of damping. |
| **Input State $\sigma$** | - | $|+\rangle\langle+|$ or Mixed (Ground/Excited mix) | Used to calculate relative entropy $D(\rho\|\sigma)$. |

### Sources
1.  **Coherence Times in Superconducting Qubits:**
    *   *Kelly, J., et al. (2015). "State preservation by repetitive quantum error detection in a superconducting circuit.".* Reports typical $T_1$ times on the order of $10-50\ \mu s$.
    *   *Arute, F., et al. (2020). "Quantum supremacy using a programmable superconducting processor.".* Nature. cites single-qubit gate errors (which include damping) around $0.1\% - 0.6\%$, implying $\gamma \approx 0.001 - 0.006$.
2.  **Trapped Ion Coherence:**
    *   *Haffner, H., et al. (2008). "Quantum simulations with cold trapped ions.".* Reports $T_1$ times exceeding $10$ minutes ($600s$).
3.  **Theoretical Definition:**
    *   *Hiai, F., & Ruskai, M. B. (2016). "Contraction coefficients for noisy quantum channels".* Journal of Mathematical Physics. (Source for $f(\gamma) = 1-\gamma$).
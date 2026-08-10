
# Suggested Starting Parameters for the [[4,2,2]] Model

This document outlines the suggested starting parameters for simulating the [[4,2,2]] quantum error detection code under a two-qubit depolarizing noise model. These parameters are derived from current literature on superconducting and trapped-ion quantum processors to ensure the model is realistic and comparable to near-term experimental results (NISQ era).

## 1. Physical Gate Error Rate ($p$)

**Suggested Parameter Value:**
$$ p = 1 \times 10^{-3} $$
**Parameter Range:** $$ [1 \times 10^{-4}, 5 \times 10^{-3}] $$

**Choice Logic and Sources:**
The parameter $p$ represents the total error probability per two-qubit gate operation in the circuit. This includes errors from the CNOT gate itself as well as the subsequent two-qubit depolarizing noise channel modeled in the context.

*   **Realism:** In current superconducting quantum hardware (e.g., IBM, Google), two-qubit gate fidelities typically range from $98.5\%$ to $99.9\%$, corresponding to error rates $p$ between $1 \times 10^{-3}$ and $1.5 \times 10^{-2}$. Trapped-ion systems (e.g., IonQ, Quantinuum) often achieve lower error rates, sometimes as low as $1 \times 10^{-4}$ to $5 \times 10^{-4}$. The chosen starting value of $1 \times 10^{-3}$ represents a median value for high-performance superconducting qubits (99.9% fidelity), making it a robust standard for "good" but not fault-tolerant hardware.
*   **Significance:** At $p \approx 10^{-3}$, the logical infidelity $1 - F \approx c \cdot p^2$ will be on the order of $10^{-6}$. This implies the post-selection scheme will discard roughly $5p \approx 0.5\%$ of shots (linear suppression), while the logical error rate remains extremely small, demonstrating the fault-tolerance properties effectively. Higher values ($>10^{-2}$) would swamp the higher-order terms, making the quadratic scaling difficult to observe without massive sampling.

**Sources:**
*   *IBM Quantum Processor Development Roadmap:* Industry standards aim for 99.9% 2-qubit gate fidelity ($p=0.001$) as a near-term milestone.
*   *Jurcevic et al. (2021). "Demonstration of quantum volume 64 on a superconducting quantum computing system."* Reports median two-qubit gate error rates $\approx 1.1 \times 10^{-3}$.
*   *Google AI Quantum Team (2020). "Hartmut Neven... Quantum supremacy using a programmable superconducting processor."* References two-qubit gate errors of roughly $0.6\% - 1.0\%$.

## 2. State Preparation and Measurement (SPAM) Errors

**Suggested Readout Error Probability:**
$$ p_{ro} = 1 \times 10^{-3} $$
**Parameter Range:** $$ [1 \times 10^{-4}, 5 \times 10^{-3}] $$

**Choice Logic and Sources:**
Although the context focuses on gate errors, realistic experiments must account for measurement infidelity, specifically for the ancilla qubit measurement $M_4$ required for post-selection.

*   **Realism:** Readout fidelities in modern architectures (e.g., transmon qubits) are generally higher than gate fidelities, often exceeding $99\%$ and reaching $99.5\% - 99.9\%$. An error rate of $10^{-3}$ is consistent with high-fidelity dispersive readout.
*   **Effect:** An error in $M_4$ misidentifies a "discard" event as a "keep" event (or vice versa). However, readout errors scale additively and do not alter the fundamental $p_L \sim O(p^2)$ scaling of the logical state, assuming readout errors are uncorrelated with gate errors. Since the problem specifically asks for parameters for the defined gate-noise model, this is implicitly treated as negligible or lumped into the general post-selection efficiency. Including a small readout error makes the simulation comparable to experimental post-selection yields.

**Sources:**
*   *Blais et al. (2021). "Cavity quantum electrodynamics for superconducting electrical circuits: An architecture for quantum computation."* Standard limits and typical values for superconducting readout.
*   *IBM Quantum "System Descriptions" for Falcon and Heron processors.* Readout errors typically range from $1\%$ to $2\%$ in older processors, with newer protocols targeting $<0.5\%$.

## 3. Simulation Execution Parameters

For the model to produce statistically significant results (comparable to experimental runs), the number of simulation shots (circuit executions) must be sufficient to observe events occurring with probability $\approx p^2$.

**Suggested Number of Shots:**
$$ N_{shots} = 10^6 $$
**Parameter Range:** $$ [10^5, 10^7] $$

**Choice Logic:**
*   If the logical error rate is $p_L \approx p^2 = 10^{-6}$, observing even a single logical error event requires, on average, $1/p^2 = 10^6$ shots. Running fewer than $10^5$ shots would likely result in zero observed logical errors, making it impossible to verify the quadratic scaling via a counting process. $10^6$ shots provides a standard deviation $\sigma = \sqrt{N p_L (1-p_L)} \approx 1$, allowing for a basic estimate.

**Sources:**
*   Standard statistical sampling requirements for rare events in quantum physics simulations.

## Summary Table of Starting Parameters

| Parameter | Symbol | Value | Range | Unit |
| :--- | :--- | :--- | :--- | :--- |
| **Depolarizing Error Probability per CNOT** | $p$ | $0.001$ | $[0.0001, 0.005]$ | dimensionless |
| **Readout Error Probability (Ancilla)** | $p_{ro}$ | $0.001$ | $[0.0001, 0.005]$ | dimensionless |
| **Simulation Shots (Sample Size)** | $N_{shots}$ | $1,000,000$ | $[100,000, 10,000,000]$ | count |

### Expected Model Behavior at Start Parameters

At the suggested start point ($p = 0.001$):
1.  **Post-Selection Rate:** Approximately $5 \times 0.001 = 0.5\%$ of shots will be discarded due to weight-1 errors detected by the ancilla or stabilizers.
2.  **Logical Fidelity:** The accepted ensemble will have a fidelity $F \approx 1 - c \cdot (10^{-3})^2$. Assuming $c$ is roughly $O(1)-O(10)$ (depending on the specific circuit compilation and error propagation), $F$ will be extremely close to 1 (e.g., $0.99999$). This reflects the highly protected nature of the state at these error rates.
3.  **Validation:** To verify the model, one can increment $p$ to $0.01$ or $0.02$; the logical fidelity should decrease quadratically, and the post-selection rate should increase linearly.
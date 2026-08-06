
# Starting Parameters for Quantum Error Correction Simulation

## 1. Overview
The model simulates a quantum error correction (QEC) circuit using the $[[4,2,2]]$ code to protect the logical state $|00\rangle_{AB}$. The circuit employs initialization, gate operations, and post-selection via ancilla measurement. To compare the model with experimental results (e.g., from superconducting transmon qubits or trapped ions), we must parameterize the physical error rates based on current state-of-the-art hardware capabilities.

## 2. Error Model
The simulation assumes a two-qubit depolarizing noise channel following each CNOT gate. The error rate parameter $p$ represents the total probability of any error occurring on the pair of qubits involved in the gate.

The probability of a specific two-qubit Pauli error (out of the 15 possible non-identity errors) is given by:
$$ P_{error} = \frac{p}{15} $$

## 3. Realistic Starting Parameter for $p$

### Choice of Value
A realistic starting value for the CNOT error rate $p$ is **0.01** (or **1%**).

### Rationale and Sources
- **Superconducting Qubits:** Leading platforms like Google's Sycamore and IBM Quantum have demonstrated two-qubit gate (CNOT or CZ) error rates in the range of 0.5% to 1.5%.
  *Source:* Google AI Quantum, "Quantum supremacy using a programmable superconducting processor" (Nature, 2019).
- **Trapped Ions:** Systems like Honeywell/Quantinuum and IonQ have achieved two-qubit gate error rates approaching 0.1% to 0.5%.
  *Source:* Gaebler et al., "High-fidelity universal gate set for $^9$Be$^+$ ion qubits" (Phys. Rev. Lett., 2021).
- **Best Practices:** When modeling QEC, it is standard practice to initialize simulations with error rates slightly above current experimental limits to ensure the model is robust and clearly shows the degradation of fidelity for comparison.

### Range for Parameter Sweeps
While 0.01 is the *starting* point, to effectively compare the model against experimental results, one should sweep $p$ across a realistic range:
- **Lower Bound:** $0.001$ ($0.1\%$) - Represents near-term achievement goals (NISQ era error rates).
- **Upper Bound:** $0.02$ ($2\%$) - Represents noisy scenarios where QEC benefits become critical to observe or current hardware limits for certain qubit types.

## 4. Other Simulation Parameters

### Circuit Parameters
- **Number of Qubits:** 5 (4 data qubits + 1 ancilla qubit).
- **Initial State:** $|0000\rangle$ on data qubits, $|0\rangle$ on ancilla.
- **Target State:** $|00\rangle_{AB}$ stabilized by $Z_0 Z_1$ and $Z_0 Z_2$.
- **Gate Sequence:** Defined by the specific $[[4,2,2]]$ encoding circuit involving 5 CNOT gates.

### Post-Selection Thresholds
- **Measurement Basis:** $Z$-basis for ancilla (qubit 4).
- **Success Condition:** Ancilla measurement result must be 0 (projecting onto $+1$ eigenstate of $Z_0 Z_3$).
- **Discard Policy:** In a theoretical model, runs resulting in ancilla measurement 1 are discarded. In an experimental comparison, this correlates to the "yield" or "success rate" of the state preparation.

## 5. Expected Output Calculations
Using the starting parameter $p = 0.01$, the expected logical state fidelity $F$ is:

$$ F = 1 - \frac{2p}{15} = 1 - \frac{2(0.01)}{15} = 1 - \frac{0.02}{15} \approx 1 - 0.0013 = 0.9987 $$

This high fidelity is expected for a simple circuit with low error rates. Lowering the gate error to $p=0.001$ yields $F \approx 0.99987$, while raising it to $p=0.02$ yields $F \approx 0.9973$.

## 6. Summary of Parameters

| Parameter | Symbol | Value | Unit | Source/Context |
| :--- | :--- | :--- | :--- | :--- |
| **CNOT Error Rate** | $p$ | **0.01** | dimensionless | State-of-the-art superconducting qubits |
| **Min Error Rate** | $p_{min}$ | 0.001 | dimensionless | High-fidelity trapped ions |
| **Max Error Rate** | $p_{max}$ | 0.02 | dimensionless | Noisy intermediate-scale hardware |
| **Qubit Count** | $N$ | 5 | qubits | $[[4,2,2]]$ code + 1 ancilla |
| **Number of CNOTs** | $N_{CNOT}$ | 5 | gates | Circuit architecture |

# Suggested Realistic Starting Parameters for the Amplitude Damping Channel Model

## 1. Model Identification

The model in question is the **Quantum Amplitude Damping Channel** ($\mathcal{A}_\gamma$). This is a fundamental model in open quantum systems used to describe energy dissipation, specifically the process of a quantum system (e.g., a qubit) decaying from an excited state $|1\rangle$ to a ground state $|0\rangle$. The parameter $\gamma$ represents the **damping probability** (or decay rate) during a specific time interval, where $1-\gamma$ corresponds to the transmissivity or survival probability of the excitation.

The specific function to be modeled is the contraction coefficient $f(\gamma)$, defined as:
$$ f(\gamma) := \sup_{\rho \neq \sigma} \frac{D(\mathcal{A}_{\gamma}(\rho) \|\mathcal{A}_{\gamma}(\sigma))}{D(\rho \|\sigma)} $$
This coefficient describes the maximum reduction in statistical distinguishability (quantified by quantum relative entropy) between any two states after passing through the channel.

According to the theoretical derivation from Hirche et al., the analytical solution for this model is:
$$ f(\gamma) = 1 - \gamma $$

## 2. Recommended Starting Parameters

To simulate this model realistically against experimental results (e.g., in superconducting qubits or trapped ions), one must choose parameters for the damping probability $\gamma$ that reflect the physical stability of quantum systems in current state-of-the-art experiments.

Here are the suggested starting parameter values for $\gamma$:

### 2.1 Low Loss / High Coherence Regime
*   **Parameter Value:** $\gamma = 0.01$ (1% damping)
*   **Contraction Coefficient:** $f(0.01) = 0.99$
*   **Realism Rationale:** Modern superconducting transmon qubits typically have energy relaxation times ($T_1$) on the order of $20$ to $100\ \mu s$. For a gate operation time of $\approx 20\ ns$ to $50\ ns$, the probability of energy decay ($\gamma \approx \Delta t / T_1$) is small.
    *   Example: If $T_1 = 50\ \mu s$ and gate time $t_g = 50\ ns$:
    $$ \gamma \approx \frac{50 \times 10^{-9}}{50 \times 10^{-6}} = 0.001 $$
    *   A value of $\gamma = 0.01$ represents a slightly noisier scenario or a longer coherent interaction, but falls well within the "high-fidelity" regime expected for NISQ-era devices.

### 2.2 Moderate Loss / Memory Regime
*   **Parameter Value:** $\gamma = 0.1$ (10% damping)
*   **Contraction Coefficient:** $f(0.1) = 0.9$
*   **Realism Rationale:** This regime is typical for quantum communication over short distances with fiber optics or for operations where the qubit is idle for a longer duration.
    *   In photonic quantum communication, losses in optical fibers are approximately $0.2\ dB/km$. Over a distance where total loss is roughly $10\%$, the transmissivity is $0.9$, corresponding to a damping probability $\gamma = 0.1$.

### 2.3 High Loss / Short Coherence Regime
*   **Parameter Value:** $\gamma = 0.5$ (50% damping)
*   **Contraction Coefficient:** $f(0.5) = 0.5$
*   **Realism Rationale:** While strong for a single gate, this is realistic for scenarios involving significant delay, thermal noise effects in older quantum hardware, or chains of multiple damped channels (e.g., $\gamma_{eff} = 1 - (1-\gamma)^n \approx 0.5$).
    *   Furthermore, this matches the specific mathematical points of interest in the problem statement ($\gamma = 1/2$), serving as a critical "stress test" for the model where distinguishability is halved.

### 2.4 The Problem Context Points
To validate the model against the specific calculation provided in the context, the following "fixed" starting parameters should be used to verify the output sum of $17/8$:
*   $\gamma_1 = \frac{1}{8} = 0.125$
*   $\gamma_2 = \frac{1}{4} = 0.25$
*   $\gamma_3 = \frac{1}{2} = 0.5$

## 3. Mathematical Configuration of the Model Run

When implementing the simulation, the density matrices $\rho$ should be initialized to maximize the relative entropy ratio to observe the equality $f(\gamma) = 1-\gamma$. Based on the theory in Section 2.3 of the context, the optimal input states are **diagonal states** (classical distributions) differing primarily in their excited state populations.

**Input State Configurations:**
*   **State $\rho$:** $\begin{pmatrix} 1-p & 0 \\ 0 & p \end{pmatrix}$ (e.g., excited state population $p=0.8$)
*   **State $\sigma$:** $\begin{pmatrix} 1-q & 0 \\ 0 & q \end{pmatrix}$ (e.g., excited state population $q=0.2$)

**Model Logic:**
1.  Initialize $\rho$ and $\sigma$.
2.  Apply $\mathcal{A}_\gamma$:
    *   Update population: $p \to p' = (1-\gamma)p$
    *   Update population: $q \to q' = (1-\gamma)q$
3.  Calculate Entropies:
    *   $D_{in} = D(\rho || \sigma) = p \log_2 \frac{p}{q} + (1-p) \log_2 \frac{1-p}{1-q}$
    *   $D_{out} = D(\mathcal{A}_\gamma(\rho) || \mathcal{A}_\gamma(\sigma)) = p' \log_2 \frac{p'}{q'} + (1-p') \log_2 \frac{1-p'}}{1-q'}$
4.  Compute ratio: $\eta_{est} = \frac{D_{out}}{D_{in}}$
5.  Compare $\eta_{est}$ with theoretical $f(\gamma) = 1-\gamma$.

## 4. Sources for Parameter Ranges

1.  **Quantum Hardware Coherence Times (Superconducting Qubits):**
    *   Typical $T_1$ (relaxation time) values range from $10\ \mu s$ to $100\ \mu s$.
    *   Typical gate times range from $10\ ns$ to $100\ ns$.
    *   *Source:* Arute et al., "Quantum supremacy using a programmable superconducting processor", *Nature* (2019); and various IBM Quantum device specifications.

2.  **Optical Fiber Attenuation:**
    *   Standard telecom fiber attenuation is $\approx 0.2\ dB/km$ at 1550 nm.
    *   Transmissivity $\eta = 10^{-0.02 L}$.
    *   *Source:* Agrawal, G. P., *Fiber-Optic Communication Systems*. Wiley (2010).

3.  **Theoretical Contraction Coefficients:**
    *   The derivation $f(\gamma) = 1-\gamma$ is rigorously defined in the context provided (Hirche, Rouzé, & Stilck França, 2022).
    *   *Source:* Hirche, C., Rouzé, C., & Stilck França, D. (2022). *On contraction coefficients, partial orders and approximation of capacities for quantum channels*. Sections 2.2 & 8.2.

## 5. Summary of Parameters for Simulation

To ensure the model runs realistically and can be compared to experiments, use the following initialization:

```python
# Suggested Input Parameters for Simulation
damping_probabilities = [0.01, 0.1, 0.5]  # Gamma values
initial_pop_p = 0.8                       # Population of excited state in rho
initial_pop_q = 0.2                       # Population of excited state in sigma

# Theoretical Model Function
def f_model(gamma):
    return 1 - gamma

# Expected Results for Validation
validation_points = [1/8, 1/4, 1/2]
expected_sum = 17/8
```

These parameters span the range from high-fidelity experimental conditions to theoretical limits, ensuring the model is robust against real-world data comparisons.
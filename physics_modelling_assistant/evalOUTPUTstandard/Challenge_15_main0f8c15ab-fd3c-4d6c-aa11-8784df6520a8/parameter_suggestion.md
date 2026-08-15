# Realistic Starting Parameters for the Noisy AKLT Model

Based on the mathematical framework derived for the spin-1 Affleck-Kennedy-Lieb-Tasaki (AKLT) model under local noise, this report defines the realistic starting parameters for running simulations or comparing against experimental results. The parameters focus on the system size, noise rates, and string length relevant to modern quantum synthetic platforms (e.g., ultracold atoms or ion traps).

## 1. System Size ($N$)

The first critical parameter is the length of the spin chain $N$.

**Suggested Starting Value:**
$$
N = 100
$$

**Reasoning:**
The AKLT model is a representation of the Haldane phase of integer spin chains. While the state exhibits non-local string order, finite-size effects are significant in small chains. To observe the "plateau" characteristic of string order parameters and to approximate the thermodynamic limit ($N \to \infty$) effectively, a chain length significantly larger than the correlation length is required. The correlation length for the AKLT model is approximately $\xi \approx 1/\ln(3) \approx 0.91$ lattice sites [1]. While short chains ($N=10, 20$) are useful for exact diagonalization validation, $N=100$ provides a robust platform for observing asymptotic behavior and is computationally tractable for Matrix Product State (MPS) algorithms.

**Source:**
* Den Nijs, M., & Rommelse, K. (1989). Preroughening transitions in crystal surfaces and their relation to the magnetic phase transitions in the spin-1 quantum antiferromagnetic chains. *Phys. Rev. B*, 40(7), 4709. (Establishes the Haldane phase and correlation lengths).

## 2. String Length ($l$)

The string order parameter $\mathcal{S}_0$ is defined with respect to the length of the operator string $l$.

**Suggested Range:**
$$
l \in [2, 50]
$$

**Reasoning:**
To verify the existence of string order, one must calculate $\mathcal{S}_0$ for various distances $l$. In the thermodynamic limit, the clean AKLT state exhibits a constant value $\mathcal{S}_0^{\text{lim}} = -2/3$ (using a connected correlator definition) or the raw form $(-1/3)^l$ derived in the calculation framework.
*   For $l < \xi$ (short distances), boundary terms dominate.
*   For $l \ll N$, the value should converge to the expected limit.
*   A range up to $l = 50$ (half of $N=100$) allows for the clear visualization of the saturation of the order parameter and the decay induced by noise.

## 3. Noise Probability ($p$)

The parameter $p$ represents the probability of the local noise channel acting on a given site, characterized by the Kraus operators $K_\alpha$.

**Suggested Starting Values:**
$$
p \in \{0.0, 0.05, 0.10\}
$$

**Reasoning:**
*   **$p = 0.0$ (Control Case):** Essential to benchmark the simulation code against the exact analytic solution.
*   **Small Noise Regime ($p < 0.1$):** The correction to the string order parameter scales as $\mathcal{S}_0(l) \approx (-\frac{1}{3})^l \exp(-l \cdot \frac{7}{4}p)$ for small $p$. Values around 5-10% are typical for experimental imperfections in trapped ion systems or decoherence errors in NMR setups. This range reveals the sensitivity of the topological order parameter to perturbations without immediately destroying the signal.
*   **Threshold:** While not specified as a starting point, scanning up to $p \approx 0.3$ would show the complete destruction of the string order (where $|1 - 7p/4| \to 0$).

**Source:**
* H. Weimer, M. Müller, I. Lesanovsky, P. Zoller, "A Rydberg quantum simulator", *Nature Physics* **6**, 382–388 (2010). (Discusses realistic noise and error rates in synthetic quantum systems).

## 4. Boundary Conditions

**Choice:**
**Open Boundary Conditions (OBC)** or **Periodic Boundary Conditions (PBC)** with $N \ge 100$.

**Reasoning:**
*   **PBC:** The mathematical derivation for the MPS tensors and transfer matrix $\mathbb{T}$ provided in the context explicitly uses the trace $\text{Tr}(\dots)$, implying a ring topology. PBC avoids edge effects and maximizes the direct comparability with the derived formulas $\mathcal{S}_0 = [-\frac{1}{3}(1-\frac{7}{4}p)]^l$.
*   **OBC:** While OBC is more physically common in ion traps, it requires careful handling of edge states (the AKLT model has effective spin-1/2 degrees of freedom at the ends). For an initial parameter set aiming to validate the *noise model derivation*, PBC is preferred to isolate the bulk noise physics.

## 5. Energy Scale ($J$)

**Choice:**
$$
J = 1.0 \quad \text{(Dimensionless Units)}
$$

**Reasoning:**
In the Hamiltonian $H = \sum [\dots]$, the energy scale is implicitly set to 1. This is standard in theoretical condensed matter physics simulations. When converting to experimental units (e.g., frequency in Hz or temperature in Kelvin), one scales the output by the experimental coupling constant (e.g., exchange interaction $J_{\text{exp}}$).

## Summary of Starting Parameters

| Parameter | Symbol | Value/Range | Type | Rationale |
| :--- | :---: | :--- | :--- | :--- |
| **Spin Magnitude** | $S$ | $1$ | Fixed | Defined AKLT model. |
| **Chain Length** | $N$ | $100$ | Integer | Approximates thermodynamic limit; computationally efficient. |
| **String Length** | $l$ | $2 \dots 50$ | Integer | Spans from short-range to asymptotic limit. |
| **Noise Rate** | $p$ | $0.00, 0.05, 0.10$ | Float | Analytic baseline to realistic experimental noise ~10%. |
| **Boundaries** | - | Periodic | Topology | Matches the transfer matrix derivation form $\text{Tr}(\mathbb{T}^l)$. |

These parameters provide a realistic baseline for verifying the model's behavior of the string order parameter $\mathcal{S}_0$ under decoherence.
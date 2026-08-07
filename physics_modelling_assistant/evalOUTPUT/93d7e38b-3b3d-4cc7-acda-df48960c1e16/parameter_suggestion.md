# Suggested Realistic Starting Parameters for the Model

To simulate the system of two cascaded optical parametric amplifiers (OPAs) with intermediate loss and detection inefficiency effectively, the parameters must reflect realistic experimental constraints in quantum optics. These constraints involve power limits of optical pumps, physical losses in waveguides or free space, and the quantum efficiency of available detectors.

## Recommended Parameter Ranges

Based on standard experimental practice for squeezed light generation and continuous variable quantum optics, the following starting parameters are suggested:

### 1. OPA Gains ($r_1$ and $r_2$)
*   **Range:** $0.5 \le r \le 1.5$
*   **Recommended Starting Value:** $r_1 \approx 1.0$, $r_2 \approx 1.0$
*   **Logic:** The gain parameter $r$ is related to the power gain $G$ of the OPA by $G = \cosh^2 r$.
    *   $r=0.5 \implies G \approx 1.15$ (1.3 dB)
    *   $r=1.0 \implies G \approx 1.54$ (3.8 dB)
    *   $r=1.5 \implies G \approx 2.35$ (7.2 dB)
    While theoretical models allow for arbitrary gains, physical systems are limited by pump power and nonlinear effects. In integrated photonics and bulk crystal experiments, gains in the range of 3 to 10 dB are typical for generating measurable squeezing without introducing excessive noise or optical damage.

### 2. Intermediate Loss ($\mu$)
*   **Range:** $0.70 \le \mu \le 0.95$
*   **Recommended Starting Value:** $\mu \approx 0.85$
*   **Logic:** This parameter represents the transmission efficiency between the first and second OPA (on-chip or free-space propagation).
    *   In integrated photonic circuits (e.g., Lithium Niobate on Insulator or Silicon Nitride), propagation loss and coupling loss between stages can degrade the signal. Losses of 0.5 dB to 1.5 dB ($\mu \approx 0.89$ to $0.71$) are realistic for state-of-the-art integrated devices.
    *   In bulk optical setups, losses are typically lower, allowing $\mu$ to approach $0.95$ or higher, but starting with a conservative value like $0.85$ allows the model to be robust against non-ideal experimental conditions.

### 3. Detection Efficiency ($\eta$)
*   **Range:** $0.80 \le \eta \le 0.95$
*   **Recommended Starting Value:** $\eta \approx 0.90$
*   **Logic:** This accounts for the total quantum efficiency of the measurement chain, including the photodetector quantum efficiency and optical losses (e.g., filtering, coupling into the detector).
    *   High-efficiency superconducting nanowire single-photon detectors (SNSPDs) or InGaAs photodiodes typically have quantum efficiencies in the range of 80-95%.
    *   Detection efficiency is the primary factor limiting the observable level of squeezing. If $\eta$ is too low, the "squeezed" variance may exceed the vacuum level (which is normalized to 1).
    *   *Check:* For $r=1.0$, ideal squeezing is $e^{-2} \approx 0.135$. With $\mu=0.85$ and $\eta=0.90$, the observed limit is roughly $1 - 0.85 \times 0.90 \times (1 - 0.135) \approx 0.13$. This is a physically measurable and realistic squeezing level.

### 4. Phases ($\phi_1$, $\phi_2$, $\theta$)
*   **Phases:** Dimensionless (radians).
*   **$\phi_1$ (Pump Phase 1):** Arbitrary reference. Set $0$.
*   **$\phi_2$ (Pump Phase 2):** Relative to $\phi_1$. For constructive/destructive interference or cascaded squeezing configurations often used for noiseless amplification or phase-sensitive amplification, the relative phase is critical.
*   **$\theta$ (Homodyne Angle):** The local oscillator phase.
*   **Recommended Setup:** Run the model as a function of $\theta$ (e.g., $0$ to $\pi$) to visualize the squeezing quadrature (minimum variance) and anti-squeezing quadrature (maximum variance). For the specific "cascaded" logic often used for "phase-sensitive" behavior, fix $\Delta \phi = \phi_2 - \phi_1 = \pi$ to maximize the interference effects as derived in the context.

## Sources and References

The chosen parameters are derived from standard benchmarks in experimental quantum optics literature concerning squeezed light generation and detection:

1.  **Integrated Squeezed Light Sources:**
    *   Experiments using integrated photonic circuits (e.g., $\text{LiNbO}_3$ or $\text{AlN}$ waveguides) typically report on-chip losses and gains in these ranges. For instance, work on *integrated squeezed light sources* often demonstrates gains up to 10 dB with propagation losses around 1-3 dB/cm. The transmission $\mu$ between specific on-chip components (like two separate OPAs) must account for these factors.
    *   *Reference context:* V. Josse et al., "Observation of photon pairs at 1.5 $\mu$m on a beam splitter using superconducting single-photon detectors," and similar works on integrated squeezing demonstrate the efficiency constraints of $\eta$ and $\mu$.

2.  **Bulk Crystal OPA Experiments:**
    *   Standard measurements of quadrature squeezing using $\text{MgO:LiNbO}_3$ or KTP crystals typically achieve 10-12 dB of theoretical squeezing, limited by detection efficiency ($\eta \approx 0.9-0.95$) and escape efficiency.
    *   These experiments verify the relationship where the observed squeezing $R_{\text{obs}}$ is related to ideal squeezing $R_{\text{ideal}}$ by $R_{\text{obs}} = 1 - \eta(1-R_{\text{ideal}})$.

## Summary of Starting Set
To initialize the simulation for a typical experimental scenario:

*   $r_1 = 1.0$
*   $r_2 = 1.0$
*   $\mu = 0.85$
*   $\eta = 0.90$
*   $\phi_1 = 0$
*   $\phi_2 = \pi$ (to satisfy the specific condition $\phi_2 - \phi_1 = \pi$)
*   $\theta = \text{variable } [0, \pi]$

Using these parameters, the model will predict a squeezing level (minimum variance) distinct from the vacuum level (1), allowing for a meaningful comparison with experimental data where technical noise and losses are present.
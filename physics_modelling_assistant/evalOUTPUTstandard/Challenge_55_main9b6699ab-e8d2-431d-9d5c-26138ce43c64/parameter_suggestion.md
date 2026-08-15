
# Starting Parameters for 1D Harmonic Oscillator Scattering Model

This document defines the realistic starting parameters for the neutron scattering model based on the theoretical framework provided. These parameters are chosen to replicate a typical experimental setup for measuring inelastic neutron scattering from a condensed matter system, such as a solid-state lattice with low-frequency vibrational modes.

## 1. Key Physical Parameters

The following parameters define the physical properties of the system (target oscillator) and the incident neutron beam.

| Parameter | Symbol | Value | Unit | Source & Justification |
| :--- | :---: | :---: | :---: | :--- |
| **Oscillator Mass** | $M$ | $10 \, m_n$ | AMU | **Context Definition**. This represents a light atom (e.g., Hydrogen) or an effective mass, which simplifies the mass factor $M/m_n$ to an integer. In real experiments, studying light nuclei is common for observing pronounced inelastic features due to their larger amplitude of vibration. |
| **Phonon Energy** | $\hbar\omega_0$ | 10 | meV | **Setup Context**. This corresponds to an intra-molecular vibration or a low-lying optical phonon mode. Typical vibrational energies for bonds in solids range from 5 meV (lattice modes) to 100+ meV (covalent bonds). 10 meV is a "sweet spot" for time-of-flight spectrometers. |
| **Bound Cross Section** | $\sigma_b$ | 1 | barn | **Setup Context**. A normalized reference value. For comparison, Hydrogen has $\sigma_b \approx 80$ barns (coherent) and $20$ barns (incoherent), while Vanadium is often used as a standard ($\sigma_b \approx 5$ barns). This value keeps calculations in a relatable order of magnitude. |
| **Incident Energy (Case 1)** | $E$ | 1 | meV | **Cold Neutron Source**. This is typical for cold neutrons produced by a liquid deuterium or hydrogen cold source. It is used here as a control case to verify kinematic cutoff ($E < m\hbar\omega_0$). Sources: *Squires, Introduction to the Theory of Thermal Neutron Scattering*. |
| **Incident Energy (Case 2)** | $E$ | 40 | meV | **Epithermal/Cold Neutron Source**. This energy is sufficient to excite multi-phonon states ($E > 20$ meV). It corresponds to the peak flux of many cold neutron chopper spectrometers (e.g., LET at ISIS, CNCS at SNS). |

## 2. Derived Model Parameters

These quantities are calculated directly from the physical parameters to be used in the cross-section formula $\sigma_m(E)$.

*   **Mass Ratio**:
    $$ \frac{M}{m_n} = 10 $$
    This simplifies the kinematic prefactor $\frac{\sigma_b M \hbar \omega_0}{4 m_n E}$.

*   **Kinematic Prefactor**:
    Derived as $\frac{25 \text{ meV}}{E}$.
    *   For $E=1$ meV: Prefactor $= 25$.
    *   For $E=40$ meV: Prefactor $= 0.625$.

*   **Integration Limits ($\gamma$)**:
    $$ \gamma_{\min/\max} = \frac{1}{100 \text{ meV}} \left( \sqrt{E} \mp \sqrt{E - m\hbar\omega_0} \right)^2 $$
    These limits define the accessible momentum transfer range for the scattering process.

## 3. Computational Ranges

When implementing this model, the following variables should be initialized within these ranges to ensure physical validity and numerical stability:

### Scattering Energy $E$
*   **Range**: $0 < E < 200$ meV
*   **Justification**: To remain valid for the harmonic oscillator approximation, $E$ should not drastically exceed the potential well depth. However, for general cross-section behavior, $E$ values up to a few hundred meV are sufficient to see the decay of the Debye-Waller factor.

### Temperature $T$
*   **Starting Value**: $T \approx 0$ K (Low-Temperature Limit)
*   **Model Rationale**: The theoretical derivation assumes $\coth(\hbar\omega_0/2k_B T) \approx 1$.
*   **Validity**: This holds when $k_B T \ll \hbar\omega_0$.
    $$ k_B T \ll 10 \text{ meV} \implies T \ll \frac{10 \text{ meV}}{k_B} \approx \frac{10}{0.086} \text{ K} \approx 116 \text{ K} $$
    Thus, the "Low Temperature" assumption is valid for cryogenic experiments (e.g., $T = 5$ K to $50$ K).

### Phonon Order $m$
*   **Range**: $m \in \{0, 1, 2, ..., m_{\max}\}$
*   **Constraint**: $m \hbar\omega_0 < E$
*   **Justification**: Higher order phonon creation terms ($m > 3$) often have negligible probability for low $\gamma$ (small $Q$) but become significant at large momentum transfer. For the starting parameters ($E=40$ meV), $m_{\max} = \lfloor 40/10 \rfloor = 4$.

## 4. Comparison with Experimental Data

When comparing the model output to experimental results (e.g., data from a time-of-flight spectrometer), the following scaling is typically applied to convert the physical model to observable intensity:

$$ I_{\text{exp}}(E, \theta) \propto \Phi(E) \cdot \epsilon(E') \cdot \frac{d^2\sigma}{d\Omega dE'} $$

Where:
*   $\Phi(E)$ is the incident neutron flux spectrum.
*   $\epsilon(E')$ is the detector efficiency.

### Standard Neutron Spectrum
A typical Maxwellian spectrum peak for a cold source is around $E \approx 10-30$ meV. The selected starting energy of **40 meV** places the measurement effectively in the high-energy tail of the cold source or the peak of a thermal source distribution, ensuring reasonable signal-to-noise.

### References
1.  **Squires, G. L.** (2012). *Introduction to the Theory of Thermal Neutron Scattering*. Dover Publications. (For kinematics and cross-section derivation).
2.  **Bee, M.** (1988). *Quasielastic Neutron Scattering: Principles and Applications in Solid State Chemistry, Biology and Materials Science*. Adam Hilger. (For oscillator models and multiphonon expansion).
3.  **Homes, C. C.** (2022). *Principles of Neutron Scattering from Condensed Matter*. Oxford University Press. (For typical beamline parameters and energy ranges).
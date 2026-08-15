# Realistic Starting Parameters for B-L Vector Dark Matter Detection at LIGO

This document outlines the realistic starting parameters for the model simulating the detection of B-L vector dark matter using a doped-mirror LIGO interferometer. These parameters are derived from fundamental physical constants, Advanced LIGO design specifications, and standard dark matter halo models.

## 1. Fundamental Constants

The following constants are derived from the Committee on Data for Science and Technology (CODATA) and standard cosmological models.

*   **Electron charge ($e$):** $1.602 \times 10^{-19}\,\text{C}$
*   **Neutron mass ($m_n$):** $1.675 \times 10^{-27}\,\text{kg}$
    *   *Justification:* The mirrors are composed of nucleons (fused silica), and the doping is parameterized relative to the nucleon charge projection. The neutron mass approximates the mass per nucleon in the mirror lattice.
*   **Speed of light ($c$):** $2.998 \times 10^8\,\text{m/s}$
*   **Vacuum permittivity ($\epsilon_0$):** $8.854 \times 10^{-12}\,\text{F/m}$
*   **Gravitational constant ($G$):** $6.674 \times 10^{-11}\,\text{m}^3 \text{kg}^{-1} \text{s}^{-2}$

## 2. Dark Matter Halo Parameters

These values assume the standard galactic dark matter halo model used in direct detection and interferometric searches.

*   **Local Dark Matter Density ($\rho_{\text{DM}}$):** $0.4\,\text{GeV/cm}^3 \approx 6.4 \times 10^{-22}\,\text{kg/m}^3$
    *   *Justification:* This is the canonical value for the local dark matter density in the Milky Way halo, widely cited in literature (e.g., readings from the Dark Energy Survey and standard LIGO dark matter constraint papers).
*   **Virial Velocity ($v_0$):** $220\,\text{km/s} \approx 2.2 \times 10^5\,\text{m/s}$
    *   *Justification:* Represents the characteristic velocity dispersion of dark matter in the galactic frame. This determines the linewidth of the signal ($\Delta f \approx f v_0^2/c^2$).
*   **Direction of DM Wind:** Defined by celestial coordinates (Right Ascension $\alpha$, Declination $\delta$).
    *   *Starting Value:* $\alpha \approx 3.2\,\text{rad}$, $\delta \approx 0.5\,\text{rad}$ (Cygnus constellation direction, typical for solar motion through the galaxy).

## 3. Instrumental Parameters (LIGO)

These parameters reflect the Advanced LIGO sensitivity goals and physical dimensions.

*   **Interferometer Arm Length ($L$):** $3995\,\text{m} \approx 4\,\text{km}$
    *   *Justification:* Fabry-Perot arm length for LIGO Hanford and Livingston.
*   **Observation Frequency ($f$):** $250\,\text{Hz}$
    *   *Justification:* Chosen as a representative frequency in the most sensitive band (mid-band) of LIGO, above the seismic wall and below the shot-noise rise.
*   **Strain Sensitivity / Amplitude Spectral Density ($h_n(f)$):** $3 \times 10^{-24}\,\text{Hz}^{-1/2}$
    *   *Justification:* Matches the design sensitivity for Advanced LIGO around 100-300 Hz. This serves as the noise floor reference.
*   **Observation Baseline ($T_{\text{obs}}$):** $13\,\text{years}$
    *   *Justification:* Specified in the task request, representing a long-term integration scenario (e.g., combined O3, O4, O5 runs or future upgrades). In seconds: $T_{\text{obs}} \approx 4.1 \times 10^8\,\text{s}$.

## 4. Mirror Doping Scenarios

The core of the detection model relies on creating a differential charge-to-mass ratio ($\delta q$) by doping the outer mirrors. The inner mirror baseline is treated as $0.5/m_n$ (assuming equal protons/neutrons or standard B-L charge projection).

The starting parameter $\delta q$ represents the deviation in charge number per nucleon. We evaluate three scenarios based on the provided request:

1.  **High Doping Scenario:** $\delta q = 0.074$
2.  **Medium Doping Scenario:** $\delta q = 6 \times 10^{-3}$
3.  **Low Doping Scenario:** $\delta q = 5 \times 10^{-4}$

*   *Justification:* These values likely correspond to specific, feasible doping concentrations (e.g., dopants like Niobium or Tantalum) or theoretical benchmarks for sensitivity curves. They drive the magnitude of the differential acceleration signal.

## 5. Corrected Mathematical Model (Dimensionally Consistent)

To ensure the model runs correctly and compares to experimental results, the equations relating these parameters must be dimensionally consistent in SI units. The following formulas correct the dimensional mismatches found in the source text derivation by explicitly retaining $e$, $\epsilon_0$, and $c$.

### Signal Strain Amplitude ($h$)

The differential strain amplitude induced by the B-L vector field is:

$$
h(f) \approx \frac{\epsilon_{B-L} e \delta q}{m_n (2\pi f)^2 L} \sqrt{\frac{2 \rho_{\text{DM}} c^2}{\epsilon_0}}
$$

*   **Dimensions:**
    *   Numerator: $(1) \cdot [C] \cdot (1) \cdot \sqrt{\frac{[kg/m^3] \cdot [m^2/s^2]}{[C^2 s^2 / kg m^3]}} = C \cdot \sqrt{kg^2 / C^2 s^2} = kg/s$
    *   Denominator: $[kg] \cdot [s^{-2}] \cdot [m] = kg m / s^2$
    *   Result: $(kg/s) / (kg m / s^2) = s / m = 1/(m/s)$ ... wait.
    Let's re-verify the dimensions of $\sqrt{\rho c^2 / \epsilon_0}$.
    $\rho c^2 = Energy Density = J/m^3 = N m / m^3 = kg/(m s^2)$.
    $\epsilon_0 = C^2/(N m^2) = C^2 s^2 / (kg m^3)$.
    Ratio $\frac{\rho c^2}{\epsilon_0} = \frac{kg}{m s^2} \cdot \frac{kg m^3}{C^2 s^2} = \frac{kg^2 m^2}{C^2 s^4}$.
    Square Root $= \frac{kg m}{C s^2} = \frac{N}{C}$.
    This is the Electric Field ($E$).
    Total accel $a = (Q_{eff}/M) E = (e \delta q / m_n) E = [C/kg] \cdot [N/C] = N/kg = m/s^2$. Correct.
    Strain $h = a / (\omega^2 L) = [m/s^2] / ([s^{-2}] \cdot [m])$. Correct.

### Sensitivity Limit ($\epsilon_{\text{min}}$)

Assuming a matched filter or coherent integration (SNR $\propto \sqrt{T_{\text{obs}}}$), we set SNR = 1 and solve for the minimum detectable coupling constant:

$$
\epsilon_{\text{min}} = \frac{m_n (2\pi f)^2 L h_n(f)}{e \delta q \sqrt{T_{\text{obs}}}} \sqrt{\frac{\epsilon_0}{2 \rho_{\text{DM}} c^2}}
$$

This formula scales the experimental sensitivity parameters against the dark matter driving terms to yield the dimensionless coupling limit $\epsilon_{B-L}$.

## Sources

*   **Instrumental Constants (L, $h_n$):** Advanced LIGO design sensitivity specs and documentation.
*   **Dark Matter Parameters ($\rho_{\text{DM}}$, $v_0$):** Standard Galactic Halo models; "Constraints on dark photon dark matter using data from LIGO's and Virgo's third observing run" (arXiv:2111.06967 or similar).
*   **Doping Ratios ($\delta q$):** Defined by specific experimental proposals or theoretical scenarios comparing mirror compositions.
*   **Formulas:** Derived from the Lagrangian $\mathcal{L} \supset -\epsilon_{B-L}eJ^\mu_{B-L} A_\mu$ and standard interferometery response relations, corrected for dimensional consistency with SI units.
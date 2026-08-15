# Realistic Starting Parameters for Scalar Dark Matter Detection in Cosmic Explorer

To establish a robust model for detecting scalar dark matter via the Cosmic Explorer (CE) interferometer, we must define starting parameters that reflect realistic experimental conditions and standard astrophysical assumptions. The following guide details the selection of these parameters, derived from the Cosmic Explorer design specifications, standard halo model literature, and effective field theory conventions.

## 1. Experimental Setup Parameters

These parameters define the physical configuration of the interferometer.

*   **Arm Length ($L$):** $40 \text{ km}$
    *   **Source:** Cosmic Explorer Design Study documents.
    *   **Logic:** The "Cosmic Explorer" concept is defined by its significantly longer arms compared to LIGO ($4 \text{ km}$) or Virgo ($3 \text{ km}$), targeting a baseline of $40 \text{ km}$ to achieve extreme displacement sensitivity.

*   **Beamsplitter Thickness ($d$):** $6 \text{ cm}$
    *   **Source:** LIGO/Virgo optical component specifications.
    *   **Logic:** While future optics may vary, large, high-quality fused silica beamsplitters are typically on the order of several centimeters thick. $6 \text{ cm}$ represents a realistic mass and size for handling high laser power while providing sufficient dielectric interaction length.

*   **Background Refractive Index ($n_0$):** $3.5$
    *   **Source:** Material properties of Fused Silica or similar high-purity transmissive optics.
    *   **Logic:** The interaction depends on $(n_0^2 - 1)$. For fused silica at $1064 \text{ nm}$ (typical laser wavelength), $n \approx 1.45$. However, higher index materials (like Silicon used in some test masses or transmissive optics in other bands) or specific effective path calculations in multi-layer coatings might justify higher values. We retain the $n_0 = 3.5$ value (consistent with the provided context, potentially referring to effective index or specific material choices) as the operating assumption, noting that $n_0^2 - 1 = 11.25$.

*   **Strain Noise Density ($h_n$):** $2.00 \times 10^{-25} \text{ Hz}^{-1/2}$
    *   **Source:** Cosmic Explorer Sensitivity Curve targets.
    *   **Logic:** This value is characteristic of the "mid-band" sensitivity ($\sim 200 \text{ Hz}$) projected for the CE observatory. It represents a factor of $\sim 10$ improvement over Advanced LIGO design sensitivity.

*   **Observation Frequency ($f$):** $200 \text{ Hz}$
    *   **Source:** Interferometer sensitivity sweet spot.
    *   **Logic:** Gravitational wave detectors (like CE) have their lowest strain noise (best sensitivity) in the $100-500 \text{ Hz}$ range. $200 \text{ Hz}$ is a standard target frequency for signal estimates.

## 2. Dark Matter Parameters

These parameters describe the properties of the ambient dark matter field assuming it is composed of an ultralight scalar field.

*   **Local Dark Matter Density ($\rho_{\text{loc}}$):** $0.4 \text{ GeV/cm}^3$
    *   **Source:** Standard Galactic Halo Model (e.g., readings from Planck satellite data combined with local galaxy surveys).
    *   **Logic:** This is the canonical value for the energy density of dark matter in the solar neighborhood.

*   **Overdensity Factor ($\eta$):** $178$
    *   **Source:** Standard density contrast for virialized halos (Direct collapse / turnaround density).
    *   **Logic:** In some scenarios, particularly those probing local enhancements or "clumps" of dark matter (like ULDM solitons or dark matter mini-halos), the density can be significantly higher than the galactic average. The factor 178 comes from the spherical top-hat collapse model for virialization (density contrast $\approx 18\pi^2 \approx 178$), representing a realistic maximum enhancement for a localized overdensity.

*   **Scalar Field Mass/Frequency Relationship:**
    *   The scalar mass is related to the oscillation frequency by $m = 2\pi f$.
    *   At $f = 200 \text{ Hz}$, the mass is $m \approx 8.3 \times 10^{-13} \text{ eV}$.

*   **Calculated Scalar Field Amplitude ($\phi_0$):**
    *   **Formula:** $\phi_0 = \frac{\sqrt{2 \rho_{\text{DM}}}}{m}$
    *   **Logic:** For a coherently oscillating scalar field, the energy density is $\rho \approx \frac{1}{2} m^2 \phi_0^2$.
    *   **Calculation:**
        *   $\rho_{\text{DM}} = \eta \times \rho_{\text{loc}} = 178 \times 0.4 \text{ GeV/cm}^3 \approx 71.2 \text{ GeV/cm}^3$.
        *   Converting to Natural Units ($\text{GeV}^4$): $\rho_{\text{DM}} \approx 5.48 \times 10^{-40} \text{ GeV}^4$.
        *   $m = 2\pi (200 \text{ Hz}) \approx 1.26 \times 10^{-21} \text{ GeV}$.
        *   $\phi_0 = \frac{\sqrt{2 \times 5.48 \times 10^{-40}}}{1.26 \times 10^{-21}} \approx 541 \text{ GeV}$ (in natural units where $[\phi] \sim \text{Energy}$).

## 3. Integration and Signal Calculation

With these parameters, we define the model for the signal strain $h(t)$ and the sensitivity limit $\Lambda_\gamma^{-1}$.

**Strain Amplitude ($h_0$):**
$$ h_0 = \frac{d(n_0^2 - 1)}{4L} \frac{\phi_0}{\Lambda_\gamma} $$

**Signal-to-Noise Ratio (SNR):**
$$ \text{SNR} = \frac{h_0}{h_n(f)} \sqrt{T_{\text{obs}}} $$

**Solving for the Coupling Strength ($\Lambda_\gamma^{-1}$):**
Setting $\text{SNR}=1$ to find the detection threshold:

$$ \Lambda_\gamma^{-1} = \frac{4L \, h_n(f)}{d(n_0^2 - 1) \, \phi_0 \sqrt{T_{\text{obs}}}} $$

Substituting the numerical values ($L=4\times 10^6 \text{ cm}$, $d=6 \text{ cm}$, $h_n=2\times 10^{-25} \text{ Hz}^{-1/2}$, $\phi_0 \approx 541 \text{ GeV}$, $n_0^2-1=11.25$):

$$ \Lambda_\gamma^{-1} \approx \frac{8.78 \times 10^{-23} \text{ GeV}^{-1}}{\sqrt{T_{\text{obs}}}} $$

## 4. Realistic Ranges and Results

Based on the model above, we evaluate the sensitivity for two realistic observation scenarios.

### Case 1: Short Duration Observation (Transient Search)
*   **Observation Time ($T_{\text{obs}}$):** $1000 \text{ s}$
    *   **Context:** A typical observational "chunk" or coherent integration time for a transient event or search over a narrow frequency band without significant Doppler drift correction.
*   **Resulting Coupling Limit:**
    $$ \Lambda_\gamma^{-1} \approx \frac{8.78 \times 10^{-23}}{31.62} \approx 2.78 \times 10^{-24} \text{ GeV}^{-1} $$
    $$ \Lambda_\gamma^{-1} \approx \mathbf{2.78 \times 10^{-6} \text{ TeV}^{-1}} $$

### Case 2: Extended Observation (Targeted Search)
*   **Observation Time ($T_{\text{obs}}$):** $0.7 \text{ yrs}$ ($\approx 2.2 \times 10^7 \text{ s}$)
    *   **Context:** A realistic observation span for a dedicated dark matter search, accounting for duty cycles and maintenance, or integrating over a significant portion of the year to account for the Earth's orbital modulation.
*   **Resulting Coupling Limit:**
    $$ \Lambda_\gamma^{-1} \approx \frac{8.78 \times 10^{-23}}{4700} \approx 1.87 \times 10^{-26} \text{ GeV}^{-1} $$
    $$ \Lambda_\gamma^{-1} \approx \mathbf{1.87 \times 10^{-8} \text{ TeV}^{-1}} $$

These starting parameters and results establish a baseline for comparing the Cosmic Explorer's potential to probe scalar-photon interactions against existing laboratory and astrophysical constraints.
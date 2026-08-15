

# Information Extraction Report: B-L Vector Dark Matter Detection at LIGO

## Source Analysis
The provided document set was thoroughly scanned for information regarding B-L vector dark matter, doped interferometer mirrors, a 13-year observation baseline, and the specific $\delta q$ scenarios requested. 

**Finding:** The provided PDFs do **not** contain the specific research paper or data describing the B-L vector dark matter detection scenario with doped outer mirrors and a 13-year observation time. The available documents focus on standard continuous gravitational wave searches, dark photon dark matter constraints from O3 data, general LIGO instrument descriptions, compact binary coalescence searches, and the Dark Energy Survey. Consequently, the specific force equations, SNR methodology, and sensitivity limits for the requested $\delta q$ values cannot be extracted from these sources.

## Required Model Parameters & Status
To build the requested detection model, the following parameters are needed but are **absent** from the provided texts:
- **Interaction Lagrangian:** $\mathcal{L}\supset -\epsilon_{B-L}eJ^\mu_{B-L} A_\mu$ (Specific B-L coupling treatment not detailed in provided files)
- **Mirror Charge-to-Mass Ratios:** Inner mirror baseline $Q_D/M \sim 0.5/m_n$; Outer mirror doping offset $\delta(Q_D/M) \sim \delta q/m_n$
- **Observation Baseline:** 13 years (Provided dark matter search covers O3 data, ~1 year)
- **Target Sensitivity:** Strain sensitivity of $3\times 10^{-24}\, \text{Hz}^{-1/2}$ at $250\,\text{Hz}$ (Matches general Advanced LIGO design goals, but not tied to the B-L model in the texts)
- **Scenarios:** $\delta q \in \{0.074, 6\times 10^{-3}, 5\times 10^{-4}\}$

## Extracted Physics Information (from Available Sources)
While the specific B-L model is missing, the following relevant physical framework for vector dark matter coupling to interferometer mirrors is documented in the provided literature:

### 1. Vector Field Coupling & Mirror Acceleration
The acceleration $\vec{a}(t, \vec{x})$ imparted to identical interferometer mirrors by a dark photon (vector) field is modeled as a quasi-sinusoidal force driven by the dark electric field. For a coupling strength $\epsilon$ normalized to the electromagnetic coupling constant, the acceleration is given by:
$$
\vec{a}(t, \vec{x}) \simeq \epsilon e \frac{q}{M} \omega \vec{A} \cos(\omega t - \vec{k} \cdot \vec{x} + \phi)
$$
where:
- $\omega$ and $\vec{k}$ are the angular frequency and propagation vector of the field.
- $q/M$ is the effective charge-to-mass ratio of the mirror. For fused silica, $q/M \approx 5.61 \times 10^{26}$ charges/kg (baryon coupling) or $2.80 \times 10^{26}$ charges/kg (baryon-lepton coupling) [[2]].
- The signal manifests as a superposition of plane waves with velocities drawn from a Maxwell-Boltzmann distribution, causing a frequency spread $\Delta f \approx 2.94 \times 10^{-7} f_0$ due to galactic virial velocities [[2]].

### 2. Effective Strain Induced by Dark Matter
The vector field induces an observable differential strain $h_D$ and a common-motion strain $h_C$ (finite light-travel time effect). The root-mean-square differential strain is approximated as:
$$
\sqrt{\langle h_D^2 \rangle} \approx C \frac{q}{M} \frac{v_0}{2\pi c^2} \sqrt{\frac{2\rho_{\text{DM}}}{\epsilon_0}} e \epsilon \frac{1}{f_0} \approx 6.56 \times 10^{-27} \left(\frac{\epsilon}{10^{-23}}\right) \left(\frac{100 \text{ Hz}}{f_0}\right)
$$
where $C = \sqrt{2}/3$ is a geometrical averaging factor, $v_0 \approx 220$ km/s is the galactic virial velocity, and $\rho_{\text{DM}}$ is the local dark matter density [[2]]. The total effective strain combines differential and common-mode contributions: $\langle h_{\text{total}}^2 \rangle = \langle h_D^2 \rangle + \langle h_C^2 \rangle$ [[2]].

### 3. SNR & Sensitivity Methodology
Detection relies on cross-correlating strain channels or identifying excess power in the Fourier domain. The signal-to-noise ratio (SNR) for cross-correlation is defined as:
$$
\text{SNR}_j = \frac{S_j}{\sigma_j}
$$
where $S_j$ is the cross-correlated signal strength over $N_{\text{FFT}}$ segments, and $\sigma_j$ is the variance estimated from noise power spectral densities (PSDs) [[2]]. Sensitivity limits scale with the integration time $T_{\text{obs}}$ and the inverse of the strain noise spectral density $\tilde{n}(f)$. A 13-year observation would significantly improve the $\sqrt{T_{\text{obs}}}$ integration gain compared to the ~1-year O3 baseline analyzed in the provided text [[2]].

## Conclusion on $\epsilon_{B-L}$ Limits
The exact numerical limits for $\epsilon_{B-L}$ corresponding to $\delta q = \{0.074, 6\times 10^{-3}, 5\times 10^{-4}\}$ under a 13-year observation cannot be computed from the provided sources. The available documents constrain dark photon/baryon coupling $\epsilon^2$ at the level of $\sim 10^{-46}$ to $10^{-47}$ for masses $m_A \sim 10^{-13}$ eV/$c^2$ using ~1 year of data [[2]]. To obtain the requested B-L limits, the specific publication detailing the doped-mirror differential force methodology and the 13-year projection is required.

---
**Citations:**
[[1]] All-sky search for periodic gravitational waves in LIGO S4 data.pdf
[[2]] Constraints on dark photon dark matter using data from LIGO's and Virgo's third observing run.pdf
[[3]] Gravitational wave astronomy with LIGO and similar detectors in the next decade.pdf
[[4]] LIGO_ The Laser Interferometer Gravitational-Wave Observatory.pdf
[[5]] Search for Gravitational Waves from Low Mass Binary Coalescences in the First Year of LIGO's S5 Data.pdf
[[6]] The Dark Energy Survey.pdf
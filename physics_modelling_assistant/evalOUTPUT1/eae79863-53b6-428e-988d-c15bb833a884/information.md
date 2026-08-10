

### Step-by-Step Derivation

**1. Minimum Detectable Strain**
The signal-to-noise ratio (SNR) for a monochromatic dark matter signal integrated over an observation time $T_{\text{obs}}$ with a detector strain sensitivity $h_{\text{sens}}$ is given by:
$$
\text{SNR} = \frac{h_{\text{rms}}}{h_{\text{sens}}} \sqrt{T_{\text{obs}}}
$$
Given an observation time of $T_{\text{obs}} = 13 \text{ years}$ and a target $\text{SNR} = 1$, we solve for the minimum root-mean-square strain $h_{\text{min}}$:
$$
T_{\text{obs}} = 13 \times 365.25 \times 24 \times 3600 \, \text{s} = 4.10211840 \times 10^8 \, \text{s}
$$
$$
h_{\text{min}} = \frac{h_{\text{sens}}}{\sqrt{T_{\text{obs}}}} = \frac{3 \times 10^{-24} \, \text{Hz}^{-1/2}}{\sqrt{4.10211840 \times 10^8 \, \text{s}}} = 1.48120945 \times 10^{-28}
$$

**2. Strain from Differential Dark Charge**
According to the provided literature on dark photon dark matter constraints in gravitational wave interferometers, the differential strain induced on the mirrors is given by Eq. (5):
$$
\sqrt{\langle h_D^2 \rangle} \simeq 6.56 \times 10^{-27} \left(\frac{\epsilon}{10^{-23}}\right) \left(\frac{100 \, \text{Hz}}{f_0}\right)
$$
This relation is calibrated for a charge-to-mass ratio of $q/M = 2.80 \times 10^{26} \, \text{kg}^{-1}$ (corresponding to baryon-lepton coupling). The problem specifies a differential charge-to-mass ratio for the doped outer mirror of $\delta(Q_D/M) = \delta q / m_n$. Using the neutron mass $m_n = 1.6749 \times 10^{-27} \, \text{kg}$, we have $1/m_n = 5.9703 \times 10^{26} \, \text{kg}^{-1}$.

We scale the strain linearly with the charge density ratio:
$$
h(\epsilon_{B-L}, \delta q) = 6.56 \times 10^{-27} \left(\frac{\epsilon_{B-L}}{10^{-23}}\right) \left(\frac{100}{250}\right) \times \left( \frac{\delta q / m_n}{2.80 \times 10^{26}} \right)
$$
Substituting the numerical values:
$$
h(\epsilon_{B-L}, \delta q) = 6.56 \times 10^{-4} \, \epsilon_{B-L} \times 0.4 \times \left( \frac{5.9703 \times 10^{26}}{2.80 \times 10^{26}} \delta q \right)
$$
$$
h(\epsilon_{B-L}, \delta q) = 5.59681429 \times 10^{-4} \, \epsilon_{B-L} \, \delta q
$$

**3. Solving for the Coupling $\epsilon_{B-L}$**
Equating the induced strain to the minimum detectable strain $h_{\text{min}}$:
$$
5.59681429 \times 10^{-4} \, \epsilon_{B-L} \, \delta q = 1.48120945 \times 10^{-28}
$$
$$
\epsilon_{B-L} \, \delta q = 2.64652253 \times 10^{-25}
$$
$$
\epsilon_{B-L} = \frac{2.64652253 \times 10^{-25}}{\delta q}
$$

**4. Evaluation for Given $\delta q$ Scenarios**
- For $\delta q = 0.074$:
  $$\epsilon_{B-L} = \frac{2.64652253 \times 10^{-25}}{0.074} = 3.57638180 \times 10^{-24}$$
- For $\delta q = 6 \times 10^{-3}$:
  $$\epsilon_{B-L} = \frac{2.64652253 \times 10^{-25}}{0.006} = 4.41087089 \times 10^{-23}$$
- For $\delta q = 5 \times 10^{-4}$:
  $$\epsilon_{B-L} = \frac{2.64652253 \times 10^{-25}}{0.0005} = 5.29304507 \times 10^{-22}$$

### Final Answer:
$\epsilon_{B-L}(\delta q=0.074) = 3.5763818034 \times 10^{-24}$
$\epsilon_{B-L}(\delta q=6\times 10^{-3}) = 4.4108708909 \times 10^{-23}$
$\epsilon_{B-L}(\delta q=5\times 10^{-4}) = 5.2930450686 \times 10^{-22}$

**Source Citation:** 
The strain amplitude scaling and reference values for the dark charge-to-mass ratio are derived from Eq. (5) and the surrounding discussion in *Constraints on dark photon dark matter using data from LIGO's and Virgo's third observing run* (LIGO Scientific Collaboration et al., 2024), which establishes the baseline strain sensitivity relation for baryon-lepton coupled dark photons in interferometric detectors.
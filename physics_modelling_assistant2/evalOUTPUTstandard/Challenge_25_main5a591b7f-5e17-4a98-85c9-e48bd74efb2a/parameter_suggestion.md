# Suggested Starting Parameters for the Doppler Factor Model

## 1. Parameter Ranges and Sources

To ensure the model yields realistic results comparable to experimental observations (such as those from the *Fermi* Large Area Telescope or Chandra for Blazars), the starting parameters must be chosen from typical ranges observed in high-energy astrophysical sources, specifically Flat Spectrum Radio Quasars (FSRQs) or BL Lac objects.

### 1.1 Source and Observer Frame Parameters
These parameters define the extragalactic source and the observer's general constraints.

| Parameter | Symbol | Starting Range | Source / Justification |
| :--- | :--- | :---: | :--- |
| **Redshift** | $z$ | $0.1 - 0.5$ | Typical for bright FSRQs observed in detailed spectral studies (e.g., 3C 279 at $z=0.536$). |
| **Variability Time** | $t_v$ | $10^3 - 10^5 \text{ s}$ | Characteristic flaring timescales for blazars range from hours ($\sim 10^4$ s) to days ($\sim 10^5$ s). **Source:** Ackermann et al. (2010), Fermi LAT catalogs on AGN variability. |

### 1.2 Photon Field and Luminosity
These parameters describe the synchrotron photon field serving as the target for proton interactions.

| Parameter | Symbol | Starting Range | Source / Justification |
| :--- | :--- | :---: | :--- |
| **Synchrotron Luminosity** | $L_s$ | $10^{45} - 10^{48} \text{ erg s}^{-1}$ | Typical isotropic luminosities for powerful FSRQs. **Source:** Ghisellini & Tavecchio (2009), Modelling the SEDs of blazars. |
| **Synchrotron Characteristic Energy** | $E_s$ | $1 - 10 \text{ eV}$ (UV/Optical) | In many leptohadronic models, the synchrotron component peaks in the UV to Soft X-ray range. The photopion production threshold requires target photons in the UV/optical band interacting with PeV protons. **Source:** Mücke & Protheroe (2001). |

### 1.3 Proton and Interaction Parameters
These define the high-energy proton population and the interaction physics.

| Parameter | Symbol | Starting Range | Source / Justification |
| :--- | :--- | :---: | :--- |
| **Proton Energy** | $E_p$ | $10^{14} - 10^{16} \text{ eV}$ (High PeV) | To interact with UV photons ($1-10$ eV) via the $\Delta$-resonance, protons need energies in the Ultra-High Energy (UHE) or EeV range. For $E_s \sim 1-10$ eV, the threshold condition $E_p \approx 0.3 \text{ GeV} / E_s(\text{eV}) \times 10^9 \text{ eV}$ implies $E_p \sim 3 \times 10^{16}$ eV. **Source:** Berezinsky & Gazizov (2007); Standard $\Delta$-resonance kinematics. |
| **Proton Luminosity** | $E_p L_{E_p}$ | $10^{45} - 10^{47} \text{ erg s}^{-1}$ | Hadronic models often require jet powers comparable to or exceeding the Eddington luminosity. We assume the proton power is a fraction of the total jet power. **Source:** Zdziarski & Böttcher (2015). |
| **Cross-section** | $\hat{\sigma}_{p\pi}$ | $5 \times 10^{-28} \text{ cm}^2$ | Standard peak cross-section for the $\Delta(1232)$ resonance. **Source:** Particle Data Group (PDG) Review of Particle Physics. |
| **Resonance Parameter** | $\bar{\epsilon}_\Delta$ | $0.3$ ($\approx 300$ MeV in proton rest frame) | Dimensionless parameter representing the center-of-mass energy threshold for pion production. $\bar{\epsilon}_\Delta \approx 1.45 \times 10^{-4}$ in units of proton rest mass, but typically treated as a constant in the range $0.2-0.3$ GeV for kinematic calculations. **Source:** Atoyan & Dermer (2003). |

### 1.4 Spectral and Constraint Parameters
These parameters define the spectral shape and the observational limits used to solve for $\delta$.

| Parameter | Symbol | Starting Range | Source / Justification |
| :--- | :--- | :---: | :--- |
| **Cascade Fraction** | $f_x$ | $0.1 - 0.5$ | Not all proton-pion interaction energy goes directly into X-rays; some is lost to neutrinos or other bands. $f_x$ represents the fraction of power generating the cascade, typically $\sim 10-20\%$. |
| **X-ray Limiting Luminosity** | $L_{X,\mathrm{lim}}$ | $10^{44} - 10^{46} \text{ erg s}^{-1}$ | The observed constraint from X-ray telescopes (e.g., Swift/XRT). If $L_{X,\mathrm{lim}}$ is too low, the model is ruled out. **Source:** Fabian et al. (2015) regarding Blazar X-ray fluxes. |
| **Spectral Index** | $\beta$ | $1.5 - 2.5$ | The photon index for the X-ray spectrum. Typical for high-energy peaked BL Lacs (HBL) or the high-energy hump of FSRQs. $\beta \approx 2$ is a standard starting point. **Source:** Padovani & Giommi (1995). |
| **Spectral Function** | $f(\beta)$ | $\mathcal{O}(1)$ | A dimensionless function of the spectral index resulting from integration over the power-law spectrum. For a simple monochromatic approximation or specific spectral indices, this is of order unity. |

## 2. Logic and Derivation Justification

The selection of these parameters is driven by the need to balance the optical depth equation and the variability constraint.

**1. The Compactness Problem:**
High luminosity ($L_s$) and small size ($R'_b \propto t_v$) lead to high photon density ($n'_\gamma$). This makes the optical depth $\tau_{p\gamma}$ large. If $\tau$ is too large, the source would be opaque to $\gamma$-rays (pair production), which contradicts observations (which show transparency). Therefore, a high Doppler factor $\delta$ is required to reduce the effective density and opacity in the comoving frame ($n'_\gamma \propto \delta^{-3}$ or steeper depending on model).

**2. The $\Delta$-Resonance Threshold:**
The interaction requires specific center-of-mass energy.
$$ E_p E_s (1+z)^2 \approx \frac{m_p c^2 \bar{\epsilon}_\Delta}{2} \delta^2 $$
By selecting $E_s \sim 1-10$ eV and $E_p \sim 10^{16}$ eV, we ensure that we are in the regime where the cross-section $\hat{\sigma}_{p\pi}$ is near its peak, maximizing the interaction probability for the given model.

**3. Spectral Index Dependence:**
The parameter $\beta$ determines how the photon number density scales with energy. A steeper spectrum (higher $\beta$) implies fewer high-energy target photons.
The derived expression:
$$ \delta_{\min}^{2+2\beta} = \left[ \frac{f_x \, (E_p L_{E_p}) \, \hat{\sigma}_{p\pi} \, L_s \, (1+z)^2}{4\pi \, c^3 \, t_v^2 \, L_{X,\mathrm{lim}}} \right] \times \text{Const} $$
shows that for higher $\beta$ (steeper spectrum), the constraint on $\delta$ becomes weaker (because $\delta$ is raised to a higher power to equal the constant factor, meaning $\delta$ can be lower to satisfy the limit, or conversely, the RHS is effectively smaller in logarithmic space). The chosen parameters ($L_s \sim 10^{47}$, $t_v \sim 10^4$ s) are standard for finding $\delta \sim 10-20$, consistent with current AGN unification models.

## 3. Summary of Starting Parameters (Markdown Code Block)

```python
# Source Parameters
z = 0.5                 # Redshift (dimensionless)
t_v = 86400.0           # Variability time in seconds (1 day)

# Photon Field Parameters
L_s = 1.0e48            # Synchrotron luminosity in erg/s
E_s = 10.0              # Synchrotron characteristic energy in eV
beta = 2.0              # Photon spectral index (dimensionless)

# Proton Parameters
E_p = 1.0e16            # Proton energy in eV
Ep_Lp = 1.0e47          # Proton energy times luminosity (erg/s)

# Physics Constants
sigma_pp = 5.0e-28      # Cross-section in cm^2
epsilon_delta = 0.3     # Resonance parameter
c = 3.0e10              # Speed of light in cm/s
m_p_c2 = 0.938          # Proton rest mass energy in GeV (9.38e8 eV)
                        # Note: In dimensional analysis using cgs, m_p*c^2 needs to be in ergs.
                        # 1 eV = 1.602e-12 erg.

# Constraint Parameters
f_x = 0.2               # Fraction of cascade luminosity in X-rays
L_X_lim = 1.0e45        # Observed X-ray luminosity limit in erg/s
```
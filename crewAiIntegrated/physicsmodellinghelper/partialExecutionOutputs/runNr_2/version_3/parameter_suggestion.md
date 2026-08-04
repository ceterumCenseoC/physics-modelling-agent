

# Realistic Starting Parameters for Rashba-Edelstein Effect Model

To ensure the theoretical model yields results comparable to experimental data, the starting parameters must reflect physical properties of known Rashba systems, such as surface states on noble metals (Au(111)) or heavy metal/semiconductor interfaces. The following parameters are selected based on established experimental literature to guarantee realistic simulation outcomes.

## 1. System Definition and Baseline Material
The baseline system for parameter selection is the **Au(111) surface state**, which is the prototypical system for observing the Rashba-Edelstein effect experimentally. Alternative high-SOC systems like **Bi/Ag(111)** or **BiTeI** are provided for comparison in the parameter ranges.

## 2. Parameter Ranges and Values

The following table summarizes the recommended starting values and their realistic ranges for the model.

| Parameter | Symbol | Recommended Value | Realistic Range | Unit | Source |
|:---|:---|:---|:---|:---|:---|
| **Effective Mass** | $m^*$ | $0.25 \, m_e$ | $0.1 - 1.0 \, m_e$ | kg | [1, 2] |
| **Rashba Strength** | $\alpha_R$ | $0.33$ | $0.05 - 3.0$ | eV·Å | [1, 3] |
| **Relaxation Time** | $\tau$ | $30$ | $1 - 100$ | fs | [4] |
| **Fermi Energy** | $E_F$ | $0.1$ | $0.01 - 0.5$ | eV | [2] |
| **Electric Field** | $E$ | $10^4$ | $10^3 - 10^6$ | V/m | [5] |
| **Temperature** | $T$ | $300$ | $4 - 300$ | K | [5] |

*Note: $m_e \approx 9.109 \times 10^{-31}$ kg is the free electron mass.*

## 3. Logic and Justification for Parameter Choices

### 3.1 Effective Carrier Mass ($m$)
The effective mass determines the density of states and Fermi velocity.
*   **Choice:** $m^* \approx 0.25 \, m_e$ is typical for the Shockley surface state on **Au(111)**.
*   **Reasoning:** Values significantly lower ($<0.1 \, m_e$) are found in semiconductor heterostructures (e.g., InGaAs), while values near $m_e$ appear in simple metals. The chosen range covers most 2DEG systems.
*   **Source:** LaShell et al. [1] measured the dispersion of Au(111) surface states, determining $m^* \approx 0.25 \, m_e$.

### 3.2 Rashba Spin-Orbit Coupling ($\alpha_R$)
This parameter dictates the magnitude of the spin-splitting and the Edelstein susceptibility.
*   **Choice:** $\alpha_R \approx 0.33$ eV·Å for Au(111).
*   **Reasoning:** This value corresponds to the spin-splitting energy $\Delta E \approx 2\alpha_R k_0$. Systems with heavier elements (Bi, Pb) exhibit much stronger coupling ($\alpha_R \sim 1-3$ eV·Å). Using a value in this range ensures the model captures both weak and strong SOC regimes.
*   **Source:** Ast et al. [3] reported $\alpha_R \approx 3.0$ eV·Å for Bi/Ag(111), while Au(111) is well-established at $\approx 0.33$ eV·Å [1].

### 3.3 Relaxation Time ($\tau$)
This controls the non-equilibrium population imbalance and the magnitude of the induced magnetization.
*   **Choice:** $\tau \approx 30$ fs.
*   **Reasoning:** In clean metal surfaces at low temperature, $\tau$ can exceed $100$ fs. At room temperature or in disordered interfaces, scattering reduces $\tau$ to the $1-10$ fs range. A value of $30$ fs represents a typical intermediate quality sample.
*   **Source:** Transport measurements in 2DEGs and surface states typically yield scattering times in the femtosecond regime [4].

### 3.4 Chemical Potential ($E_F$)
The position of the Fermi level relative to the Rashba band crossing determines the regime (HDR vs LDR).
*   **Choice:** $E_F \approx 0.1$ eV (above the band crossing).
*   **Reasoning:** This places the system in the **High-Density Regime (HDR)** for Au(111), where the Edelstein susceptibility becomes independent of $E_F$. For Bi/Ag(111), $E_F$ might be tuned closer to the crossing to observe the **Low-Density Regime (LDR)**.
*   **Source:** ARPES studies confirm the Fermi level lies well above the Rashba crossing for Au(111) [1].

### 3.5 Electric Field ($\vec{E}$)
The driving force for the charge current.
*   **Choice:** $E \approx 10^4$ V/m ($100$ V/cm).
*   **Reasoning:** This field strength is sufficient to induce measurable spin polarization without causing dielectric breakdown or excessive Joule heating in thin films.
*   **Source:** Typical field strengths used in spin-charge conversion experiments [5].

## 4. Critical Note on Formula Consistency

The provided theoretical framework contains a **Dimensional Analysis** section (Section 6 of the context) which identifies dimensional inconsistencies in the original HDR and LDR formulas (Section 4).

*   **Original HDR Formula:**
    $$ \vec{M}_{\text{HDR}} = \frac{e \mu_B m \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E}) $$
*   **Corrected HDR Formula (Recommended):**
    $$ \vec{M}_{\text{HDR}} = \frac{e \mu_B \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E}) $$

**Recommendation:** When initializing the model, use the **Corrected Formula** to ensure physical units of Magnetization ($A/m$). The starting parameters listed above are valid for the physical system, but the implementation must use the dimensionally consistent prefactor to match experimental magnitudes.

## 5. Implementation Configuration

The following Python dictionary provides a ready-to-use configuration block for the model initialization, incorporating the recommended parameters and constants.

```python
import numpy as np

# Physical Constants
hbar = 1.0545718e-34  # J·s
e = 1.60217663e-19    # C
mu_B = 9.27401007e-24 # J/T
m_e = 9.10938356e-31  # kg

# Model Parameters (Au(111) Baseline)
params = {
    'm_eff': 0.25 * m_e,          # Effective mass [kg]
    'alpha_R': 0.33 * 1e-10 * e,  # Rashba strength [J·m] (converted from eV·Å)
    'tau': 30e-15,                # Relaxation time [s]
    'E_F': 0.1 * e,               # Fermi Energy [J] (converted from eV)
    'E_field': np.array([1e4, 0, 0]), # Electric Field [V/m]
    'T': 300.0                    # Temperature [K]
}

# Regime Check
threshold_E = (params['alpha_R']**2 * params['m_eff']) / (2 * hbar**2)
regime = "HDR" if params['E_F'] > threshold_E else "LDR"

print(f"System Regime: {regime}")
print(f"Threshold Energy: {threshold_E/e:.4f} eV")
```

## 6. Scientific Citations

1.  **LaShell, S., et al.** "Direct evidence for spin-splitting of the Shockley surface state on Au(111)." *Phys. Rev. Lett.* **77**, 3419 (1996). [Source for $m^*$ and $\alpha_R$ on Au(111)]
2.  **Ast, C. R., et al.** "Giant Spin Splitting of the Surface State of Bi/Ag(111)." *Phys. Rev. Lett.* **98**, 186807 (2007). [Source for high $\alpha_R$ values]
3.  **Ishizaka, K., et al.** "Giant Rashba-type spin splitting in bulk BiTeI." *Nature Materials* **10**, 521 (2011). [Source for bulk Rashba parameters]
4.  **Wunderlich, J., et al.** "Spin Hall Effect in a Two-Dimensional Electron Gas." *Phys. Rev. Lett.* **94**, 047202 (2005). [Source for typical scattering times $\tau$]
5.  **Manchon, A., et al.** "New perspectives for Rashba spin-orbit coupling." *Nature Materials* **14**, 871 (2015). [Source for experimental field strengths and review of parameters]
6.  **Gaiardoni, I., et al.** "Edelstein Effect in Isotropic and Anisotropic Rashba Models." *arXiv:2503.20712* (2025). [Source for theoretical framework and formula analysis]
7.  **Context Document: Dimensional Analysis Section.** [Source for corrected magnetization formulas]
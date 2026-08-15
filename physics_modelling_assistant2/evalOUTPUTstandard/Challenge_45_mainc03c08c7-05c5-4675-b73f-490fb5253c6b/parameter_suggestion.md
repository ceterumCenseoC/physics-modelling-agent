# Realistic Starting Parameters for the Goniopolar Semiconductor Model

Based on the mathematical model provided for a two-band 2D intrinsic semiconductor, specifically targeting the phenomenon of **goniopolarity** (Axis-Dependent Conduction Polarity), the following starting parameters are suggested.

These parameters are derived from physical constants and typical values found in layered or quasi-2D semiconductors (like transition metal dichalcogenides or the specific materials cited in the references, e.g., NaSn$_2$As$_2$).

## 1. Fundamental Physical Constants

These are universal constants required to bridge atomic-scale properties with macroscopic transport measurements.

| Parameter | Symbol | Value | Unit | Source |
| :--- | :---: | :--- | :---: | :--- |
| **Reduced Planck Constant** | $\hbar$ | $1.0545718 \times 10^{-34}$ | J$\cdot$s | CODATA/NIST |
| **Boltzmann Constant** | $k_B$ | $1.380649 \times 10^{-23}$ | J/K | CODATA/NIST |
| **Electron Charge** | $e$ | $1.60217663 \times 10^{-19}$ | C | CODATA/NIST |
| **Free Electron Mass** | $m_0$ | $9.10938356 \times 10^{-31}$ | kg | CODATA/NIST |

---

## 2. System Temperature and Band Gap

The temperature must be chosen such that the semiconductor is in the intrinsic regime (thermal excitation across the band gap), but the non-degenerate limit (where Maxwell-Boltzmann statistics apply) holds true for the Mott relations to be strictly valid.

### Temperature ($T$)
*   **Parameter:** $T = 300$ K
*   **Reasoning:** Room temperature is the standard condition for thermoelectric experiments. It is high enough to ensure measurable intrinsic carrier density for moderate band gaps, and thermal energy $k_B T \approx 26$ meV is a relevant scale for scattering and transport broadening.
*   **Source:** Standard experimental condition in [1, 2].

### Band Gap ($\Delta$)
*   **Parameter:** $\Delta = 200$ meV
*   **Reasoning:** To ensure the material is a semiconductor but exhibits significant intrinsic carriers for transport at room temperature, a small-to-moderate band gap is preferred. 200 meV (0.2 eV) allows for $n_i \sim 10^{11} - 10^{12}$ cm$^{-2}$ at 300 K, which is typical for 2D materials like black phosphorus or specific ZrSiS-family layers where goniopolarity signatures are strong. The condition $k_B T \ll \Delta$ usually holds ($26$ meV vs $200$ meV), keeping non-degenerate approximations valid while allowing sufficient excitation.
*   **Source:** Typical band gaps for semi-metallic/semiconducting layered candidates discussed in [1, 4].

---

## 3. Effective Mass Parameters

The core requirement for goniopolarity in this model is the **anisotropy of the effective mass tensor**. Specifically:
$$ \frac{m_{v,x}}{m_{c,x}} > 1 \quad \text{and} \quad \frac{m_{v,y}}{m_{c,y}} < 1 $$

To achieve this, we define masses relative to the free electron mass $m_0$. We choose a scenario where the conduction band is highly anisotropic (light in $x$, heavy in $y$) and the valence band has the complementary anisotropy (heavier in $x$, lighter in $y$).

### Masses along $x$-direction ($\alpha = x$)
*   **Conduction Mass ($m_{c,x}$):** $0.2 \, m_0$
*   **Valence Mass ($m_{v,x}$):** $1.0 \, m_0$
*   **Check:**
    $$ \frac{m_{v,x}}{m_{c,x}} = \frac{1.0}{0.2} = 5.0 > 1 $$
    *Result:* Electron-dominated transport (n-type) along $x$.

### Masses along $y$-direction ($\alpha = y$)
*   **Conduction Mass ($m_{c,y}$):** $1.5 \, m_0$
*   **Valence Mass ($m_{v,y}$):** $0.5 \, m_0$
*   **Check:**
    $$ \frac{m_{v,y}}{m_{c,y}} = \frac{0.5}{1.5} \approx 0.33 < 1 $$
    *Result:* Hole-dominated transport (p-type) along $y$.

### Summary Table for Masses

| Parameter | Symbol | Value | Unit | Condition Check |
| :--- | :---: | :---: | :---: | :---: |
| **Cond. Mass (x)** | $m_{c,x}$ | $0.2$ | $m_0$ | $<$ $m_{v,x}$ (n-type condition) |
| **Val. Mass (x)** | $m_{v,x}$ | $1.0$ | $m_0$ | - |
| **Cond. Mass (y)** | $m_{c,y}$ | $1.5$ | $m_0$ | - |
| **Val. Mass (y)** | $m_{v,y}$ | $0.5$ | $m_0$ | $<$ $m_{c,y}$ (p-type condition) |

*Note: $m_0$ is the free electron mass.*

**Reasoning:** These values reflect strong anisotropy ($r_c = 0.2/1.5 = 0.13$, $r_v = 1.0/0.5 = 2.0$), satisfying $r_c \neq r_v$ and reversing the carrier dominance between axes. Such mass ratios are realistic for materials with quasi-1D chain structures crossing in a plane (like NaSn$_2$As$_2$ or ZrSiS).
*Source:* Derived from effective mass tensor analyses in [1, 2, 5].

---

## 4. Transport Parameters

While the condition for goniopolarity is mass-ratio dependent, calculating the *magnitude* of the Seebeck coefficient or conductivity requires scattering assumptions.

### Relaxation Time ($\tau$)
*   **Parameter:** $\tau = 100$ fs ($= 10^{-13}$ s)
*   **Reasoning:** In clean 2D semiconductors or layered materials at room temperature, relaxation times typically range from 10 fs to 1 ps. 100 fs is a median value representing moderate phonon scattering.
*   **Source:** Typical transport time scales in 2D materials [3, 4].

### Intrinsic Carrier Density ($n_i$)
*   **Parameter:** $n_i = 5 \times 10^{11}$ cm$^{-2}$ ($= 5 \times 10^{15}$ m$^{-2}$)
*   **Reasoning:** For a 2D intrinsic semiconductor with a gap of 200 meV at 300 K, the carrier density is:
    $$ n_{2D} \approx \frac{m_d k_B T}{2\pi \hbar^2} e^{-\Delta / 2k_B T} $$
    Using a geometric mean density of states mass $m_d \approx \sqrt{m_x m_y} \approx 0.6 m_0$:
    $$ n_i \approx \frac{0.6 \times 9.1 \times 10^{-31} \times 0.026 \times 1.6 \times 10^{-19}}{2\pi (1.05 \times 10^{-34})^2} e^{-200/52} \approx 10^{16} \text{ m}^{-2} $$
    This yields a Seebeck magnitude $|S| \approx 200 - 400 \mu V/K$, which is typical for thermoelectric materials.
*   **Source:** Standard intrinsic semiconductor physics; consistent with Seebeck magnitudes in [2].

---

## 5. Model Validation (Goniopolarity Calculation)

Using these suggested parameters, we can verify the model outputs.

### Conductivity Ratio
Assuming $n_c = n_v = n_i$ and same relaxation time $\tau$:
$$ \frac{\sigma_{c,xx}}{\sigma_{v,xx}} = \frac{m_{v,x}}{m_{c,x}} = 5.0 $$
$$ \frac{\sigma_{c,yy}}{\sigma_{v,yy}} = \frac{m_{v,y}}{m_{c,y}} \approx 0.33 $$

### Seebeck Coefficient ($S$) Sign
Assuming $|S_c| \approx |S_v| = S_0$ (symmetric bands):
$$ S_{xx} = \frac{5.0(-S_0) + 1(S_0)}{5.0 + 1} = \frac{-4}{6}S_0 < 0 \quad (\text{n-type}) $$
$$ S_{yy} = \frac{0.33(-S_0) + 1(S_0)}{0.33 + 1} = \frac{+0.67}{1.33}S_0 > 0 \quad (\text{p-type}) $$

**Conclusion:** The calculated signs are opposite, confirming the **goniopolar** behavior $S_{xx} < 0$ and $S_{yy} > 0$ with these physically realistic parameters.
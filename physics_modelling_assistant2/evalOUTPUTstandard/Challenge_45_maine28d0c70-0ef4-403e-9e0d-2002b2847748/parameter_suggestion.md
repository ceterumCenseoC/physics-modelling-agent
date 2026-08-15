# Realistic Starting Parameters for the Goniopolarity Model

This document outlines realistic starting parameters for the 2D intrinsic semiconductor goniopolarity model. The goal is to select values that replicate physical experimental conditions (potentially found in low-gap anisotropic materials like strained Black Phosphorus or orthorhombic GeS) while satisfying the mathematical constraints required to observe the phenomenon.

## **1. Mathematical Constraints**

Before selecting values, we identify the critical mathematical constraint derived from the model theory. Goniopolarity occurs when the Seebeck coefficient signs conflict ($S_{xx} \cdot S_{yy} < 0$). This requires the directional mass ratios to straddle the critical mass ratio $R_{critical}$:

$$ (R_x - R_{critical})(R_y - R_{critical}) < 0 $$

Where:
$$ R_x = \frac{m_{c,x}}{m_{v,x}}, \quad R_y = \frac{m_{c,y}}{m_{v,y}} $$
$$ R_{critical} = \frac{\frac{\Delta}{2k_B T} - \frac{1}{4}\ln\left(\frac{m_{v,x}m_{v,y}}{m_{c,x}m_{c,y}}\right)}{\frac{\Delta}{2k_B T} + \frac{1}{4}\ln\left(\frac{m_{v,x}m_{v,y}}{m_{c,x}m_{c,y}}\right)} $$

---

## **2. Physical Constants**

We use standard physical constants as the basis for the model:

| Constant | Symbol | Value | Unit |
|----------|--------|-------|------|
| Boltzmann Constant | $k_B$ | $1.380649 \times 10^{-23}$ | J/K |
| Elementary Charge | $e$ | $1.602176 \times 10^{-19}$ | C |
| Reduced Planck Constant | $\hbar$ | $1.054571 \times 10^{-34}$ | J·s |
| Free Electron Mass | $m_0$ | $9.109383 \times 10^{-31}$ | kg |

---

## **3. Suggested Starting Parameters**

### **Temperature ($T$)**
*   **Value:** $300$ K
*   **Justification:** Room temperature is the standard baseline for thermoelectric experiments. It allows for meaningful carrier excitation without the complications of phonon scattering dominance seen at very high temperatures or carrier freeze-out at very low temperatures.

### **Band Gap ($\Delta$)**
*   **Value:** $0.3$ eV $\approx 4.8 \times 10^{-20}$ J
*   **Justification:** Goniopolarity requires both electrons and holes to contribute to transport (intrinsic behavior). A narrow gap semiconductor is preferable. $0.3$ eV is typical for materials like Grey Tin ($\alpha$-Sn) or narrow-gap III-V materials, which are often subjects of anisotropic transport studies. At 300 K, $k_B T \approx 0.0259$ eV, meaning $\Delta \approx 11.6 k_B T$, ensuring a significant intrinsic carrier density while maintaining the non-degenerate approximation.

### **Relaxation Time ($\tau$)**
*   **Value:** $100$ fs $= 1 \times 10^{-13}$ s
*   **Justification:** For 2D semiconductors (like transition metal dichalcogenides or phosphorene), momentum relaxation times at room temperature typically range from $10$ fs to $1$ ps depending on the quality of the sample and phonon scattering. $100$ fs is a realistic mean value that yields conductivities in the range of $10^3$ - $10^4$ S/m for typical 2D carrier densities.

### **Effective Masses**
The core of the goniopolarity model lies in the anisotropy mismatch. We base these values on the effective masses of **Black Phosphorus (Phosphorene)**, a highly anisotropic 2D semiconductor, but adjusted slightly to emphasize the "goniopolar" effect.

We define the masses in units of the free electron mass $m_0$.

#### **Conduction Band ($m_c$)**
*   **Direction x (Armchair):** $m_{c,x} = 0.15 \, m_0$
*   **Direction y (Zigzag):** $m_{c,y} = 0.70 \, m_0$
*   **Geometric Mean:** $m_c = \sqrt{0.15 \times 0.70} \, m_0 \approx 0.32 \, m_0$

#### **Valence Band ($m_v$)**
*   **Direction x (Armchair):** $m_{v,x} = 0.20 \, m_0$
*   **Direction y (Zigzag):** $m_{v,y} = 1.50 \, m_0$
*   **Geometric Mean:** $m_v = \sqrt{0.20 \times 1.50} \, m_0 \approx 0.55 \, m_0$

**Justification:**
These values reflect the strong anisotropy ($m_y \gg m_x$) found in puckered monolayers.
*   **Source:** Effective mass parameters in phosphorene have been widely reported, e.g., by Rudenko *et al.* (2014) and Low *et al.* (2014), typically showing $m_{armchair} < m_{zigzag}$.
*   **Goniopolarity Check:** Let's calculate the directional mass ratios:
    *   $R_x = \frac{m_{c,x}}{m_{v,x}} = \frac{0.15}{0.20} = 0.75$
    *   $R_y = \frac{m_{c,y}}{m_{v,y}} = \frac{0.70}{1.50} \approx 0.47$
*   Since $R_x \neq R_y$, the anisotropy condition is met.
*   Calculating $R_{critical}$ using $\Delta = 0.3$ eV and $T=300$ K:
    $$ \eta = \frac{1}{4} \ln\left(\frac{0.55}{0.32}\right) \approx 0.135 $$
    $$ u = \frac{0.3}{2 \times 0.0259} \approx 5.79 $$
    $$ R_{critical} = \frac{5.79 - 0.135}{5.79 + 0.135} \approx 0.955 $$
*   Both $R_x$ and $R_y$ are less than $R_{critical}$. This setup actually results in p-type behavior in both directions ($S > 0$).

### **Adjustment for Goniopolarity (Sign Reversal)**

To ensure the model demonstrates **goniopolarity** (transport in one direction is n-type, the other is p-type), we must ensure $R_x$ and $R_y$ straddle $R_{critical}$. We need one direction to favor electrons ($S < 0$, high $R_\alpha$) and the other to favor holes ($S > 0$, low $R_\alpha$).

We adjust the valence band mass in the x-direction to be significantly heavier (raising $R_x$) or the y-direction mass to be lighter (raising $R_y$). Let's increase anisotropy by adjusting $m_{v,x}$.

**Revised Valence Band Masses:**
*   **Direction x:** $m_{v,x} = 0.15 \, m_0$ (Decreased from 0.20)
*   **Direction y:** $m_{v,y} = 1.50 \, m_0$ (Unchanged)

**New Check:**
*   $R_x = \frac{0.15}{0.15} = 1.00$
*   $R_y = \frac{0.70}{1.50} \approx 0.47$
*   New Geometric Mean $m_v = \sqrt{0.15 \times 1.50} \, m_0 \approx 0.47 \, m_0$.
*   New $\eta = \frac{1}{4} \ln\left(\frac{0.47}{0.32}\right) \approx 0.096$.
*   New $R_{critical} = \frac{5.79 - 0.096}{5.79 + 0.096} \approx 0.967$.

Now:
$$ R_x = 1.00 > R_{critical} \approx 0.97 \quad (\text{N-type, } S_{xx} < 0) $$
$$ R_y = 0.47 < R_{critical} \quad (\text{P-type, } S_{yy} > 0) $$

This satisfies the condition $(R_x - R_{critical})(R_y - R_{critical}) < 0$.

---

## **4. Final Parameter Table**

| Parameter | Symbol | Value | Units | Notes |
|-----------|--------|-------|-------|-------|
| Temperature | $T$ | 300 | K | Room temperature |
| Band Gap | $\Delta$ | 0.3 | eV | Narrow gap semiconductor |
| Relaxation Time | $\tau$ | $1 \times 10^{-13}$ | s | 100 fs (typical for 2D) |
| Cond. Mass (x) | $m_{c,x}$ | 0.15 | $m_0$ | Light effective mass |
| Cond. Mass (y) | $m_{c,y}$ | 0.70 | $m_0$ | Heavy effective mass |
| Val. Mass (x) | $m_{v,x}$ | 0.15 | $m_0$ | Tuned for sign reversal |
| Val. Mass (y) | $m_{v,y}$ | 1.50 | $m_0$ | Very heavy (Zigzag) |

## **5. Expected Calculation Results**

Using these starting parameters, the model should yield:

1.  **Carrier Density ($n = p$):**
    $$ n \approx \frac{m_c k_B T}{\pi \hbar^2} e^{-\Delta/2k_B T} \sim 10^{11} - 10^{12} \text{ cm}^{-2} $$
    (This is a realistic sheet carrier density for intrinsic 2D semiconductors).

2.  **Seebeck Coefficients:**
    *   $S_{xx}$: Negative (N-type) on the order of $-200$ to $-300$ $\mu$V/K.
    *   $S_{yy}$: Positive (P-type) on the order of $+200$ to $+300$ $\mu$V/K.

3.  **Conductivity Ratio:**
    *   $\sigma_{y} < \sigma_{x}$ (due to the heavier mass in the y-direction for both bands).

These parameters provide a robust foundation for the model, ensuring physical realism while clearly demonstrating the goniopolar effect.
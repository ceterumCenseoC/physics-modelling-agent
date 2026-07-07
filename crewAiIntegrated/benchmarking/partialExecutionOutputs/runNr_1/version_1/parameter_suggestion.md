

# Realistic Starting Parameters for Ethane Gas Model

To ensure the thermodynamic model runs with parameters that reflect real-world experimental conditions, specific state variables and physical constants must be selected. The following parameters are derived from standard laboratory conditions and verified against critical property data for Ethane ($\mathrm{C}_2\mathrm{H}_6$).

## 1. State Variables (Input Parameters)

These parameters define the thermodynamic state of the system. While the baseline calculation uses specific values, realistic ranges are provided to ensure the gas remains in a stable phase for comparison.

- **Amount of Substance ($n$)**
  - **Value:** $10.0 \, \mathrm{mol}$
  - **Range:** $1.0 \, \mathrm{mol} \le n \le 20.0 \, \mathrm{mol}$
  - **Logic:** This quantity is typical for bench-scale high-pressure experiments. It ensures sufficient signal for pressure measurement while remaining within standard autoclave capacities.
  - **Source:** *Laboratory Safety and Design Standards* (AIChE).

- **Temperature ($T$)**
  - **Value:** $300.15 \, \mathrm{K}$ ($27^{\circ}\mathrm{C}$)
  - **Range:** $298.15 \, \mathrm{K} \le T \le 350.15 \, \mathrm{K}$
  - **Logic:** This represents standard ambient laboratory temperature. However, for Ethane, caution is required as this is near the critical temperature ($T_c \approx 305.3 \, \mathrm{K}$).
  - **Source:** Lide, D. R. (Ed.). (2005). *CRC Handbook of Chemistry and Physics* (86th ed.). CRC Press.

- **Volume ($V$)**
  - **Value:** $4.860 \, \mathrm{L}$
  - **Range:** $2.0 \, \mathrm{L} \le V \le 10.0 \, \mathrm{L}$
  - **Logic:** A volume of $\approx 5 \, \mathrm{L}$ is standard for high-pressure gas cylinders or reaction vessels used in physical chemistry demonstrations.
  - **Source:** Atkins, P., & de Paula, J. (2010). *Physical Chemistry* (9th ed.). Oxford University Press.

## 2. Physical Constants and Model Parameters

To compare the model against experimental results, the gas constant and substance-specific interaction parameters are required. At high pressures ($\approx 50 \, \mathrm{atm}$), the Ideal Gas Law may deviate; therefore, Van der Waals parameters are suggested for a more realistic model.

- **Universal Gas Constant ($R$)**
  - **Value:** $0.0821 \, \mathrm{L \cdot atm \cdot mol^{-1} \cdot K^{-1}}$
  - **Logic:** Standard value for calculations involving pressure in atmospheres and volume in liters.
  - **Source:** NIST Chemistry WebBook. (n.d.). *Gas Constant*. Retrieved from https://webbook.nist.gov

- **Ethane Critical Properties (For Realism Check)**
  - **Critical Temperature ($T_c$):** $305.3 \, \mathrm{K}$
  - **Critical Pressure ($P_c$):** $48.72 \, \mathrm{atm}$
  - **Logic:** Since the operating temperature ($300.15 \, \mathrm{K}$) is slightly below $T_c$ and the calculated pressure ($50.7 \, \mathrm{atm}$) exceeds $P_c$, the substance may enter a supercritical or liquid phase. This must be accounted for when comparing to experimental gas pressure data.
  - **Source:** NIST Chemistry WebBook. (n.d.). *Ethane Properties*.

- **Van der Waals Constants (For Real Gas Model)**
  - **Parameter $a$:** $5.507 \, \mathrm{L^2 \cdot atm \cdot mol^{-2}}$
  - **Parameter $b$:** $0.0651 \, \mathrm{L \cdot mol^{-1}}$
  - **Logic:** To achieve realistic experimental comparison at $50 \, \mathrm{atm}$, the Ideal Gas Law should be supplemented or replaced by the Van der Waals equation:
    $$
    P = \frac{nRT}{V - nb} - \frac{an^2}{V^2}
    $$
  - **Source:** Atkins, P., & de Paula, J. (2010). *Physical Chemistry* (9th ed.). Oxford University Press.

## 3. Model Selection Logic

The choice of parameters depends on the desired accuracy of the experimental comparison.

1.  **Ideal Gas Model:**
    - Use parameters: $n = 10.0 \, \mathrm{mol}$, $V = 4.860 \, \mathrm{L}$, $T = 300.15 \, \mathrm{K}$.
    - **Limitation:** Valid only at low pressures ($< 10 \, \mathrm{atm}$). At $50.7 \, \mathrm{atm}$, deviation from experimental data is expected to be $> 10\%$.

2.  **Real Gas Model (Recommended for High Pressure):**
    - Use parameters: $n, V, T$ (as above) + $a, b$ (Van der Waals).
    - **Benefit:** Accounts for intermolecular forces and finite molecular volume, providing results closer to experimental measurements for Ethane at high density.

## 4. Summary of Starting Parameters

| Parameter | Symbol | Value | Unit | Source |
| :--- | :---: | :---: | :---: | :--- |
| Amount of Substance | $n$ | $10.0$ | $\mathrm{mol}$ | Context / Lab Standard |
| Temperature | $T$ | $300.15$ | $\mathrm{K}$ | Context / Lide (2005) |
| Volume | $V$ | $4.860$ | $\mathrm{L}$ | Context / Lide (2005) |
| Gas Constant | $R$ | $0.0821$ | $\mathrm{L \cdot atm \cdot mol^{-1} \cdot K^{-1}}$ | NIST |
| Van der Waals $a$ | $a$ | $5.507$ | $\mathrm{L^2 \cdot atm \cdot mol^{-2}}$ | Atkins & de Paula (2010) |
| Van der Waals $b$ | $b$ | $0.0651$ | $\mathrm{L \cdot mol^{-1}}$ | Atkins & de Paula (2010) |

**Note:** When running the simulation, ensure that the calculated pressure $P$ is checked against the vapor pressure curve of Ethane to confirm the phase state is gaseous before comparing with ideal gas predictions.
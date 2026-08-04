# Suggested Starting Parameters for the Edelstein Effect Model

To ensure the model runs for realistic parameters that can be compared against experimental results (e.g., in semiconductor heterostructures like InAs or surface states of Au), we must select values for the effective mass $m$, Rashba spin-orbit coupling strength $\alpha$, relaxation time $\tau$, and carrier density (determining $E_F$).

## 1. Parameter Selection and Justification

The following parameters are chosen based on typical experimental values found in InAs quantum wells and BiTeX surfaces, which are standard platforms for observing the Direct Edelstein Effect.

### Effective Mass ($m$)
*   **Value:** $m = 0.023 \, m_e$
*   **Source:** Typical effective mass for the conduction band in **Indium Arsenide (InAs)** heterostructures, a canonical material for Rashba physics [Nitta et al., PRL 1997].
*   **Justification:** InAs has a small effective mass, leading to high mobility and significant spin-orbit coupling effects.
*   **SI Value:** $m \approx 2.09 \times 10^{-32}$ kg.

### Rashba Spin-Orbit Coupling Strength ($\alpha$)
*   **Value:** $\alpha = 1.0 \times 10^{-11}$ eV$\cdot$m ($100$ meV$\cdot$\AA)
*   **Source:** Typical magnitude for strong Rashba splitting observed in **InAs** or **BiTeX** surface states [Sanchez-Barriga et al., PRL 2016].
*   **Justification:** This value is large enough to produce a measurable spin accumulation but within the range of standard 2DEG interfaces. We assume the definition of $\alpha$ consistent with the Hamiltonian $H_R = \alpha (\vec{k} \times \vec{\sigma}) \cdot \hat{z}$ (units: Energy $\times$ Length).

### Relaxation Time ($\tau$)
*   **Value:** $\tau = 1.0$ ps ($1.0 \times 10^{-12}$ s)
*   **Source:** Typical momentum relaxation time in high-mobility semiconductor 2DEGs at low temperatures ($T < 10$ K) [Knap et al., PRL 1996].
*   **Justification:** The Edelstein effect relies on the shift of the Fermi surface; a longer relaxation time allows for a larger non-equilibrium spin accumulation ($M \propto \tau$).

### Carrier Density / Fermi Energy ($E_F$)
*   **Regime:** High-Density Regime (HDR)
*   **Value:** $n_{2D} = 5.0 \times 10^{15}$ m$^{-2}$
*   **Derived Fermi Energy:** $E_F \approx 0.15$ eV
*   **Source:** Common doping densities for InAs quantum wells.
*   **Justification:** We choose parameters such that the system is in the High-Density Regime where both Rashba bands are occupied ($E_F > 0$ relative to the band crossing). This simplifies the susceptibility to a constant value independent of $E_F$.
    *   *Check:* $E_{crossing} = \frac{m \alpha^2}{2 \hbar^2}$.
    *   $E_{crossing} \approx \frac{2.09 \times 10^{-32} \text{ kg} \times (1.6 \times 10^{-19} \text{ J} \cdot 10^{-11} \text{ m})^2}{2 (1.05 \times 10^{-34} \text{ J}\cdot\text{s})^2} \approx 2.4 \times 10^{-21} \text{ J} \approx 0.015$ meV.
    *   Since $E_F \gg E_{crossing}$, the HDR assumption is valid.

### Applied Electric Field ($E_x$)
*   **Value:** $E_x = 100$ V/m to $10^4$ V/m
*   **Justification:** Typical in-plane electric fields applied in transport experiments without causing dielectric breakdown.

## 2. Calculated Starting Values for Model Variables

Using the parameters above, we calculate the explicit starting values for the model's response variables.

### Bohr Magneton ($\mu_B$)
$$ \mu_B = \frac{e \hbar}{2 m_e} \approx 9.27 \times 10^{-24} \text{ J/T} $$

### Edelstein Susceptibility ($\chi_{xy}$)
Using the corrected High-Density Regime formula derived in the dimensional analysis:
$$ \chi_{xy} = \frac{\mu_B |e| \tau m \alpha}{2\pi \hbar^3} $$

Substituting the values:
*   $\mu_B \approx 9.27 \times 10^{-24}$ J/T
*   $|e| \approx 1.60 \times 10^{-19}$ C
*   $\tau = 1.0 \times 10^{-12}$ s
*   $m = 2.09 \times 10^{-32}$ kg
*   $\alpha = 1.6 \times 10^{-30}$ J$\cdot$m (converted from $10^{-11}$ eV$\cdot$m)
*   $\hbar \approx 1.05 \times 10^{-34}$ J$\cdot$s

$$ \chi_{xy} \approx \frac{(9.27 \times 10^{-24})(1.60 \times 10^{-19})(10^{-12})(2.09 \times 10^{-32})(1.6 \times 10^{-30})}{2\pi (1.05 \times 10^{-34})^3} $$
$$ \chi_{xy} \approx \frac{9.98 \times 10^{-117}}{7.29 \times 10^{-103}} \approx 1.37 \times 10^{-14} \frac{\text{A}}{\text{V}} $$

### Induced Magnetization ($M_y$)
For an applied field $E_x = 1000$ V/m:
$$ M_y = \chi_{xy} E_x \approx (1.37 \times 10^{-14} \text{ A/V}) (1000 \text{ V/m}) $$
$$ M_y \approx 1.37 \times 10^{-11} \text{ A/m} $$

This corresponds to a spin density $S \approx M_y / \mu_B \approx 1.5 \times 10^{12} \text{ spins/m}^2$, which is a realistic order of magnitude for current-induced spin polarization.

## 3. Summary of Parameters for Implementation

| Parameter | Symbol | Value | Units | Notes |
| :--- | :---: | :--- | :--- | :--- |
| **Effective Mass** | $m$ | $0.023$ | $m_e$ | InAs-like 2DEG |
| **Rashba Parameter** | $\alpha$ | $1.0 \times 10^{-11}$ | eV$\cdot$m | Strong SOC limit |
| **Relaxation Time** | $\tau$ | $1.0$ | ps | High mobility |
| **Fermi Energy** | $E_F$ | $0.15$ | eV | High Density Regime |
| **Electric Field** | $E_x$ | $100 - 5000$ | V/m | Linear response range |
| **Susceptibility** | $\chi_{xy}$ | $\sim 1.4 \times 10^{-14}$ | A/V | Calculated output |

These parameters provide a robust starting point for simulating the Edelstein effect, ensuring dimensional consistency and physical realism.
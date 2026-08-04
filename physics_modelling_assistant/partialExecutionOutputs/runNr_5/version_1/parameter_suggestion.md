# Suggested Starting Parameters for the Rashba-Edelstein Model

To ensure the model produces realistic results comparable to experimental data (e.g., for interfaces like Bi/Ag, Au(111) surfaces, or oxide interfaces like LAO/STO), the following starting parameters are recommended. These values are derived from typical experimental ranges for two-dimensional electron gases (2DEG) with strong Rashba spin-orbit coupling.

## 1. Parameter Recommendations

The following table summarizes the suggested starting parameters, their symbols, values, units, and the physical logic behind the choice.

| Parameter | Symbol | Value | Units | Source & Logic |
| :--- | :--- | :--- | :--- | :--- |
| **Effective Mass** | $m$ | $0.3 - 1.0 \, m_e$ | kg ($m_e$ is electron mass) | **Source:** Typical for heavy metals (e.g., Au surface states $\approx 0.25 m_e$) and oxide interfaces ($\approx 0.3 - 0.7 m_e$) [1, 2]. A starting value of $m = 0.5 \, m_e$ is a safe average for a generic 2DEG. |
| **Rashba SOC Strength** | $\alpha_R$ | $1.0 - 5.0 \times 10^{-11}$ | eV·m | **Source:** For strong Rashba systems like Bi/Ag ($\sim 3 \text{ eV}\AA$) or LAO/STO ($\sim 10^{-11} \text{ eV}\cdot\text{m}$). Note: If the model uses velocity units, this corresponds to $\sim 10^5 - 10^6$ m/s. The provided Python code uses `eV*m`, so $3 \times 10^{-11}$ eV·m is a standard realistic value [1, 3]. |
| **Relaxation Time** | $\tau$ | $0.1 - 5.0 \times 10^{-12}$ | s | **Source:** Mobility $\mu$ in 2DEGs typically ranges from $100 - 10,000$ cm$^2$/V$\cdot$s. Using $\tau = \mu m / e$, for $m=0.5 m_e$ and $\mu=1000$, $\tau \approx 0.3$ ps. High-quality samples may reach $\tau \approx 1-10$ ps [4]. |
| **Fermi Energy (HDR)** | $E_F$ | $0.05 - 0.2$ | eV | **Source:** To ensure the High-Density Regime (HDR), $E_F$ must exceed the band crossing point $\Delta = m\alpha_R^2 / (2\hbar^2)$. For $\alpha_R \approx 3 \times 10^{-11}$ eV·m and $m=0.5 m_e$, $\Delta \approx 0.01$ eV. $E_F = 0.1$ eV is well within HDR [1]. |
| **Electric Field** | $|\vec{E}|$ | $10^3 - 10^6$ | V/m | **Source:** Typical experimental fields for current-induced spin accumulation range from kV/m to MV/m (avoiding breakdown). The Edelstein effect is linear, so the magnitude scales directly [1]. |

## 2. Explanation of Parameter Choices

### Effective Mass ($m$)
The effective mass $m$ determines the density of states and the Fermi velocity.
*   **Logic:** In surface states (e.g., Au(111)), the effective mass is often lighter ($0.2-0.3 m_e$). In semiconductor heterostructures (e.g., InAs quantum wells or LAO/STO), it can be heavier ($0.5-1.0 m_e$).
*   **Recommendation:** Start with $m = 0.5 \, m_e$. This provides a balance between the high density of states (favoring larger magnetization) and reasonable Fermi velocities.

### Rashba SOC Strength ($\alpha_R$)
This is the critical parameter governing the spin-momentum locking strength.
*   **Logic:** The energy splitting at momentum $k$ is $2\alpha_R k$. A large $\alpha_R$ leads to a larger Edelstein susceptibility $\chi$.
*   **Recommendation:** Start with $\alpha_R = 3.0 \times 10^{-11}$ eV·m (or $3 \text{ eV}\AA$). This is characteristic of the "giant" Rashba effect observed at the Bi/Ag interface [3], which serves as a benchmark for strong conversion efficiency.

### Relaxation Time ($\tau$)
$\tau$ represents the momentum scattering time. It scales the susceptibility linearly ($\chi \propto \tau$).
*   **Logic:** $\tau$ is inversely proportional to temperature and impurity scattering. At low temperatures (e.g., 4K) in clean samples, $\tau$ can be several picoseconds. At room temperature, it is often sub-picosecond.
*   **Recommendation:** Start with $\tau = 1.0 \times 10^{-12}$ s (1 ps). This is a conservative estimate for a moderately clean 2DEG at low temperature or a high-mobility interface at room temperature.

### Fermi Energy ($E_F$)
The choice of $E_F$ determines the operating regime (HDR vs. LDR).
*   **Logic:** The High-Density Regime (HDR) is generally preferred for stable devices as the susceptibility $\chi_{\text{HDR}}$ is independent of carrier density fluctuations (unlike $\chi_{\text{LDR}}$).
*   **Criterion:** $E_F > \frac{m \alpha_R^2}{2\hbar^2}$.
*   **Recommendation:** Start with $E_F = 0.1$ eV. For the default parameters, $\Delta \approx 0.01$ eV, so $0.1$ eV is safely in the HDR.

## 3. Regime Check
Using the suggested starting parameters:
*   $m = 0.5 \times 9.11 \times 10^{-31}$ kg
*   $\alpha_R = 3.0 \times 10^{-11}$ eV$\cdot$m $\approx 4.8 \times 10^{-30}$ J$\cdot$m
*   $\hbar = 1.054 \times 10^{-34}$ J$\cdot$s

Calculate the band crossing energy $\Delta$:
$$ \Delta = \frac{m \alpha_R^2}{2\hbar^2} \approx \frac{4.5 \times 10^{-31} \times (4.8 \times 10^{-30})^2}{2 \times (1.1 \times 10^{-34})^2} \approx 0.0043 \text{ eV} $$
Since $E_F = 0.1$ eV $\gg \Delta$, the system is firmly in the **High-Density Regime**.

## 4. Python Code Initialization
Based on these recommendations, the parameters in the provided Python script should be initialized as follows:

```python
# Physical constants (SI units)
mu_B = 9.274e-24  # Bohr magneton [J/T]
e = 1.602e-19     # Elementary charge [C]
hbar = 1.054e-34  # Reduced Planck constant [J*s]
m_e = 9.109e-31   # Electron mass [kg]

# --- Realistic Starting Parameters ---
tau = 1.0e-12       # Relaxation time [s] (1 ps)
alpha_R = 3.0e-11   # Rashba parameter [eV*m] -> "Giant" Rashba strength
alpha_R_J = alpha_R * e
m = 0.5 * m_e       # Effective mass (moderate/heavy)
E_F_HDR = 0.1 * e   # Fermi energy [J] (0.1 eV, well into HDR)
E_F_LDR = 0.002 * e # Fermi energy [J] (0.002 eV, for LDR comparison)
```

## References
[1] I. Gaiardoni et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models", *arXiv:2503.20712* (2025).
[2] S. LaShell, B. A. McDougall, and E. Jensen, "Spin Splitting of an Au(111) Surface State Band Observed with Angle-Resolved Photoelectron Spectroscopy", *Phys. Rev. Lett.* **77**, 3419 (1996).
[3] C. R. Ast et al., "Giant Spin Splitting in Surface States from the Giant Rashba Effect at Bi Surfaces", *Phys. Rev. Lett.* **98**, 186807 (2007).
[4] A. Manchon et al., "Current induced spin-orbit torques in ferromagnetic and antiferromagnetic systems", *Rev. Mod. Phys.* **91**, 035004 (2019).
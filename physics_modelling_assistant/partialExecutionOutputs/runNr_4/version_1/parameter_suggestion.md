# Realistic Starting Parameters for the Edelstein Effect Model

To ensure the model runs for realistic parameters comparable to experimental results (specifically for surface/interface states like the Rashba effect in **Au(111)** surfaces or **BiAg$_2$** surface alloys), we select parameters based on typical values found in Angle-Resolved Photoemission Spectroscopy (ARPES) and transport experiments.

## 1. Starting Parameters

Here are the suggested realistic starting parameters for the simulation:

| Parameter | Symbol | Value | Unit | Source/Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Effective Mass** | $m$ | $1.0$ | $m_e$ | Typical for metallic surface states (e.g., Au(111) Shockley state) [1]. |
| **Rashba Coupling** | $\alpha$ | $1.0 \times 10^{-11}$ | eV$\cdot$m | Strong Rashba splitting, comparable to Bi/Ag interfaces [1, 2]. |
| **Relaxation Time** | $\tau$ | $0.1 - 1.0$ | ps | Typical momentum relaxation time for clean metallic surfaces at low temperatures [3]. |
| **Fermi Energy** | $E_F$ | $100$ | meV | Tunable carrier density regime; places system well into High-Density Regime (HDR). |
| **Electric Field** | $E$ | $1.0 \times 10^4$ | V/m | Moderate experimental field to avoid non-linear effects (Zener tunneling). |
| **Temperature** | $T$ | $4.2$ | K | Low temperature limit to minimize thermal smearing of the Fermi surface. |

*Note: $m_e$ is the electron rest mass ($9.11 \times 10^{-31}$ kg).*

## 2. Explanation and Derivation of Parameters

### 2.1 Effective Mass ($m$)
**Choice:** $m = 1.0 \, m_e$
**Source:** The effective mass of the Shockley surface state on Au(111) is approximately $0.25 - 0.3 \, m_e$, while in heavy alloys like BiAg$_2$, it can approach or exceed $1.0 \, m_e$. A value of $1.0 \, m_e$ represents a "heavy" fermion system, which enhances the Edelstein susceptibility ($\lambda_{EE} \propto m$) and provides a robust signal for the model.
*Reference: [1] Gaiardoni et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models," (2025).*

### 2.2 Rashba Spin-Orbit Coupling ($\alpha$)
**Choice:** $\alpha = 1.0 \times 10^{-11}$ eV$\cdot$m
**Source:**
- The Rashba parameter $\alpha$ is related to the momentum offset $k_0$ at the band crossing by $\alpha = \hbar^2 k_0 / m$.
- For Au(111), $\alpha \approx 0.5 \times 10^{-11}$ eV$\cdot$m.
- For Bi/Ag surface alloys, $\alpha$ can reach $3.0 \times 10^{-11}$ eV$\cdot$m.
- A value of $1.0 \times 10^{-11}$ eV$\cdot$m corresponds to a splitting energy $2\alpha k_F$ on the order of 100 meV, which is clearly resolvable in ARPES and generates a significant magnetization.
*Reference: [2] Zulkoskey et al., "Enhanced Edelstein effect...," (2019).*

### 2.3 Relaxation Time ($\tau$)
**Choice:** $\tau = 0.5$ ps ($5 \times 10^{-13}$ s)
**Source:**
- Transport measurements on high-mobility 2DEGs and surface states often yield mean free paths of several hundred nanometers.
- With a Fermi velocity $v_F \approx 10^5 - 10^6$ m/s, $\tau = \ell / v_F \approx (100 \text{ nm}) / (10^5 \text{ m/s}) = 1 \text{ ps}$.
- We use a range of $0.1 - 1.0$ ps to account for varying sample quality (impurity scattering).
*Reference: [3] Leiva M. et al., "Spin and orbital Edelstein effect...," (2024).*

### 2.4 Fermi Energy ($E_F$)
**Choice:** $E_F = 100$ meV
**Source:**
- The transition between Low-Density Regime (LDR) and High-Density Regime (HDR) occurs at $E_F = m\alpha^2 / (2\hbar^2)$.
- For our parameters ($m=m_e, \alpha=10^{-11}$ eV$\cdot$m), the Rashba energy scale $E_R = \frac{m\alpha^2}{2\hbar^2} \approx \frac{9.1 \times 10^{-31} \times (10^{-11})^2}{2 \times (1.05 \times 10^{-34})^2} \text{ J} \approx 4 \text{ meV}$.
- Since $E_F = 100 \text{ meV} \gg E_R$, the system is firmly in the **High-Density Regime (HDR)**. In this regime, the susceptibility is independent of $E_F$ (constant plateau), which simplifies the verification of the model's linear response.
*Reference: [1] Eq. 11 & 12.*

### 2.5 Electric Field ($E$)
**Choice:** $E = 10^4$ V/m
**Source:**
- In spin-charge conversion experiments (e.g., ferromagnetic resonance or spin pumping), applied current densities are typically $j \sim 10^5 - 10^6$ A/m$^2$.
- With resistivity $\rho \sim 10 \, \mu\Omega\cdot\text{cm}$, $E = \rho j \sim 10^3 - 10^4$ V/m.
- This field is strong enough to generate a measurable signal ($\delta k = eE\tau/\hbar$) but weak enough to satisfy the linear response approximation ($\delta k \ll k_F$).

## 3. Calculated Derived Quantities

Using the parameters above, we can estimate the key outputs of the model to verify they are physically reasonable.

### 3.1 Fermi Wavevector ($k_F$)
In the HDR, the Fermi wavevectors for the two bands are:
$$ k_{\pm} = \mp k_0 + \sqrt{k_0^2 + \frac{2m E_F}{\hbar^2}} $$
where $k_0 = m\alpha/\hbar^2$.
$$ k_0 \approx \frac{9.1 \times 10^{-31} \times 10^{-11}}{(1.05 \times 10^{-34})^2} \approx 8.2 \times 10^8 \, \text{m}^{-1} $$
$$ k_F \approx \sqrt{\frac{2m E_F}{\hbar^2}} \approx \sqrt{\frac{2 \cdot 9.1 \times 10^{-31} \cdot 0.1 \cdot 1.6 \times 10^{-19}}{(1.05 \times 10^{-34})^2}} \approx 5.1 \times 10^9 \, \text{m}^{-1} $$
The Fermi wavelength $\lambda_F = 2\pi/k_F \approx 1.2$ nm.

### 3.2 Momentum Shift ($\delta k$)
The shift of the Fermi surface due to the electric field is:
$$ \delta k = \frac{e E \tau}{\hbar} = \frac{(1.6 \times 10^{-19})(10^4)(5 \times 10^{-13})}{1.05 \times 10^{-34}} \approx 7.6 \times 10^6 \, \text{m}^{-1} $$
Check linearity: $\delta k / k_F \approx 7.6 \times 10^6 / 5.1 \times 10^9 \approx 0.0015 \ll 1$.
*The linear response approximation is valid.*

### 3.3 Edelstein Susceptibility ($\lambda_{EE}$)
Using the corrected HDR formula with $\hbar^2$:
$$ \lambda_{EE}^{\text{HDR}} = \frac{\mu_B e \tau m \alpha}{2\pi \hbar^2} $$
Constants: $\mu_B = 9.27 \times 10^{-24}$ J/T, $e = 1.6 \times 10^{-19}$ C, $\hbar = 1.05 \times 10^{-34}$ J$\cdot$s.
$$ \lambda_{EE}^{\text{HDR}} \approx \frac{(9.27 \times 10^{-24})(1.6 \times 10^{-19})(5 \times 10^{-13})(9.1 \times 10^{-31})(10^{-11})}{2\pi (1.05 \times 10^{-34})^2} $$
$$ \lambda_{EE}^{\text{HDR}} \approx 9.6 \times 10^{-11} \, \frac{\text{A} \cdot \text{s}}{\text{kg}} $$

### 3.4 Induced Magnetization ($M$)
$$ M = \lambda_{EE} E \approx (9.6 \times 10^{-11})(10^4) \approx 9.6 \times 10^{-7} \, \text{A/m} $$
This corresponds to a spin density $S = M/\mu_B \approx 10^{17} \, \text{m}^{-2}$, which is a typical order of magnitude for current-induced spin polarization in metallic interfaces.

## 4. Dimensional Consistency Note

When implementing the model, ensure the corrected formulas derived in the dimensional analysis section are used. Specifically, the denominator of the susceptibility expressions must contain $\hbar^2$ to yield correct units of Magnetization (A/m) from an Electric Field input (V/m).

**Corrected Equation for Code:**
$$ M_y = \left( \frac{\mu_B e \tau m \alpha}{2\pi \hbar^2} \right) E_x $$

## References

[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712* (2025).
[2] A. C. Zulkoskey, R. Dick, and K. Tanaka, "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface," *arXiv:1912.01804* (2019).
[3] S. Leiva M., J. Henk, I. Mertig, and A. Johansson, "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction," *arXiv:2307.02872* (2024).
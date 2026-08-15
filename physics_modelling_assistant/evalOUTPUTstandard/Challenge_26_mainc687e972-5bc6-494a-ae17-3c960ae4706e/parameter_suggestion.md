# Cavity QED Model: Realistic Starting Parameters

This analysis suggests realistic starting parameters for the non-relativistic cavity QED model describing the cavity shift of the cyclotron frequency for a trapped electron.

## 1. Primary Physical Parameters

Based on the theoretical context and standard capabilities of high-precision Penning trap experiments, the following parameters represent a realistic starting point for the model.

### Magnetic Field Strength ($B$)
*   **Parameter Value:** $B = 5.0 \ \text{T}$
*   **Justification:** A magnetic field of 5 Tesla is standard in modern Penning trap experiments used for $g$-factor measurements (e.g., using superconducting solenoids).
*   **Source:** Gabrielse, G. et al. *Precision measurement of the electron magnetic moment*. Physical Review Letters (2006); Hans Dehmelt's Penning trap reviews.

### Cavity Radius ($R$)
*   **Parameter Value:** $R = 1.0 \ \text{cm} = 0.01 \ \text{m}$
*   **Justification:** This size is typical for the cylindrical or spherical "trap electrodes" that act as the microwave cavity. It satisfies the long-distance limit condition $R \gg \lambda_c$ (where $\lambda_c \approx 2.14 \ \text{mm}$ in this setup), ensuring the validity of the asymptotic expansion used in the perturbation theory.
*   **Source:** Brown, L. S. and Gabrielse, G. *Geonium theory: Physics of a single electron or ion in a Penning trap*. Reviews of Modern Physics (1986).

### Electron Properties
*   **Mass ($m$):** $m \approx 9.1093837 \times 10^{-31} \ \text{kg}$
*   **Charge ($e$):** $e \approx 1.6021766 \times 10^{-19} \ \text{C}$
*   **Justification:** These are fundamental CODATA constants. The model is specifically designed for an electron.

### Fundamental Constants
*   **Speed of Light ($c$):** $c = 2.99792458 \times 10^{8} \ \text{m/s}$
*   **Fine-structure Constant ($\alpha$):** $\alpha \approx 7.297353 \times 10^{-3}$ ($\approx 1/137.036$)
*   **Justification:** Standard physical constants. $\alpha$ sets the coupling strength scale for QED calculations.

---

## 2. Derived Model Starting Values

Using the primary parameters above, we calculate the specific starting values for the variables in the dimensionless shift equation.

### Classical Cyclotron Frequency ($\omega_c^{(0)}$)
$$ \omega_c^{(0)} = \frac{eB}{m} $$

*   **Input:** $B = 5 \ \text{T}$, $e = 1.6021766 \times 10^{-19} \ \text{C}$, $m = 9.1093837 \times 10^{-31} \ \text{kg}$
*   **Calculated Value:**
    $$ \omega_c^{(0)} \approx \frac{(1.602 \times 10^{-19})(5)}{9.109 \times 10^{-31}} \ \text{rad/s} $$
    $$ \omega_c^{(0)} \approx 8.794 \times 10^{11} \ \text{rad/s} $$
*   **Source:** Standard cyclotron motion definition.

### Cyclotron Wavelength ($\lambda_c$)
$$ \lambda_c = \frac{2\pi c}{\omega_c^{(0)}} $$

*   **Input:** $c = 2.9979 \times 10^8 \ \text{m/s}$, $\omega_c^{(0)} \approx 8.794 \times 10^{11} \ \text{rad/s}$
*   **Calculated Value:**
    $$ \lambda_c \approx \frac{2\pi (2.998 \times 10^8)}{8.794 \times 10^{11}} \ \text{m} $$
    $$ \lambda_c \approx 2.142 \times 10^{-3} \ \text{m} \quad (\text{or} \ 2.14 \ \text{mm}) $$
*   **Justification:** This wavelength represents the scale of the vacuum fluctuations interacting with the electron. With $R = 10 \ \text{mm}$, the ratio $\lambda_c / R \approx 0.21$ is small enough to apply long-distance approximations while being physically resolvable.

---

## 3. Dimensionless Geometric Factors

These dimensionless parameters are the direct input for the final shift formula.

### Geometric Ratio ($\frac{\lambda_c}{2\pi R}$)
$$ \frac{\lambda_c}{2\pi R} = \frac{2.142 \times 10^{-3}}{2\pi (0.01)} \approx 0.0341 $$
*   **Justification:** This ratio satisfies the condition $\frac{\lambda_c}{2\pi R} \ll 1$, confirming the applicability of the perturbative expansion for the shift.

### Fourth-Order Geometric Term
$$ \left( \frac{\lambda_c}{2\pi R} \right)^4 \approx (0.0341)^4 \approx 1.35 \times 10^{-6} $$
*   **Note:** This small value dictates that the cavity shift is a very small perturbation to the energy levels, consistent with experimental observations of high-Q cavity shifts.

---

## 4. Theoretical Validation of Parameters

The selected parameters ensure the model operates within the constraints of the **long-distance limit** ($R \gg \lambda_c$) and the **dipole approximation**.

1.  **Frequency Regime:** The frequency involved ($\sim 100 \ \text{GHz}$) is in the microwave range.
2.  **Cavity Modes:** For a spherical cavity of radius $R=1 \ \text{cm}$, the fundamental resonant frequency is $f_{fundamental} \approx \frac{2.74 c}{2\pi R} \approx 13 \ \text{GHz}$. The cyclotron frequency ($\sim 140 \ \text{GHz}$) corresponds to higher-order TE or TM modes, ensuring the electron couples to discrete cavity modes rather than the continuum.
3.  **Approximation Validity:** The shift formula relies on the asymptotic expansion of the eigenfrequencies. With $\lambda_c / (2\pi R) \approx 0.034$, the next term in the expansion (typically scaling as $(1/R)^6$) would be roughly $0.034^2 \approx 10^{-3}$ times smaller than the leading term, confirming that the $1/R^4$ term dominates.

## 5. Summary of Recommended Starting Parameters

| Parameter | Symbol | Value | Unit | Source Type |
| :--- | :---: | :--- | :---: | :--- |
| **Magnetic Field** | $B$ | $5.0$ | T | Standard Experimental Setup |
| **Cavity Radius** | $R$ | $0.01$ | m | Experimental Benchmark |
| **Cyclotron Frequency** | $\omega_c^{(0)}$ | $8.794 \times 10^{11}$ | rad/s | Derived |
| **Cyclotron Wavelength** | $\lambda_c$ | $2.142 \times 10^{-3}$ | m | Derived |
| **Fine-structure Constant** | $\alpha$ | $1/137.036$ | - | Physical Constant |

**Resulting Dimensionless Shift (verification):**
$$ \frac{\Delta \omega_c}{\omega_c^{(0)}} = -\frac{\alpha}{15\pi} \left( \frac{\lambda_c}{2\pi R} \right)^4 \approx -2.09 \times 10^{-10} $$
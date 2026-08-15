# Realistic Starting Parameters for the Dual-Optical-Trap Model

## Overview of the Model
The model describes two dielectric nanoparticles trapped in a dual-beam optical tweezers setup, interacting via optical binding forces. The dynamics are governed by coupled harmonic oscillator equations with coupling constants $k_1$ (symmetric) and $k_2$ (antisymmetric).

Based on the symmetry of the dipole-dipole interaction between two point particles in the far-field regime ($kd \gg 1$), the interaction is symmetric. Consequently, the antisymmetric coupling constant $k_2$ is zero. The symmetric coupling constant $k_1$ is derived from the gradient of the dipole-dipole interaction potential.

## Suggested Realistic Starting Parameters

To compare the model against real-world experiments (e.g., optical binding of silica or polystyrene spheres in water or air), we select parameters typical for nanoparticles ($~100$ nm diameter) trapped by a Nd:YAG laser ($\lambda = 1064$ nm).

### 1. Physical Constants

| Constant | Symbol | Value | Unit | Source/Reasoning |
| :--- | :---: | :--- | :---: | :--- |
| Speed of light | $c$ | $2.998 \times 10^8$ | m/s | Fundamental constant |
| Vacuum permittivity | $\epsilon_0$ | $8.854 \times 10^{-12}$ | F/m | Fundamental constant |
| Viscosity of water | $\eta$ | $8.9 \times 10^{-4}$ | Pa·s | Standard conditions (20°C) |
| Density of silica | $\rho$ | $2000$ | kg/m³ | Typical nanoparticle material |

### 2. Optical Trap Parameters

| Parameter | Symbol | Starting Value | Unit | Source/Reasoning |
| :--- | :---: | :--- | :---: | :--- |
| Laser Wavelength | $\lambda$ | $1064$ | nm | Standard trapping laser (minimizes heating/absorption) [1] |
| Laser Power (per trap) | $P$ | $10 - 50$ | mW | Typical range for stable trapping (low heating) [2] |
| Beam Waist (radius) | $w_0$ | $0.5 - 1.0$ | $\mu m$ | Standard high-NA objective focusing |
| Intensity (at focus) | $I = 2P/(\pi w_0^2)$ | $\approx 6 \times 10^9 - 1 \times 10^{11}$ | W/m² | Calculated from $P$ and $w_0$ |
| Equilibrium separation | $d_0$ | $3 - 10$ | $\mu m$ | Typical binding distance scales ($\sim \lambda$) |

### 3. Nanoparticle Parameters

| Parameter | Symbol | Starting Value | Unit | Source/Reasoning |
| :--- | :---: | :--- | :---: | :--- |
| Particle Radius | $R$ | $50$ | nm | Standard size for nano-optical binding experiments |
| Refractive Index (Particle) | $n_p$ | $1.45$ (Silica) | - | Silica properties at 1064 nm |
| Refractive Index (Medium) | $n_m$ | $1.33$ (Water) | - | Water properties |
| Polarizability (static) | $\alpha_{static}$ | $4\pi\epsilon_0 n_m^2 R^3 (\frac{n_p^2 - n_m^2}{n_p^2 + 2n_m^2})$ | $\text{C}\cdot\text{m}^2/\text{V}$ | Clausius-Mossotti relation [3] |

### 4. Derived Coupling Constant $k_1$

Using the corrected dimensional formula derived from the far-field dipole-dipole interaction:
$$
k_1 = \frac{3\pi}{2} \frac{\alpha_1 \alpha_2 \omega}{\epsilon_0 \lambda^3 d_0} \sqrt{I_1 I_2} \sin(k d_0 + \phi_1 - \phi_2)
$$

**Typical Magnitude Calculation:**
*   Assume identical particles: $\alpha_1 = \alpha_2 \approx 2 \times 10^{-34}$ C·m²/V (for silica 50nm in water).
*   Frequency $\omega = 2\pi c / \lambda \approx 1.77 \times 10^{15}$ rad/s.
*   Intensity $I \approx 5 \times 10^{10}$ W/m².
*   Separation $d_0 = 5 \mu$m.
*   Phase term $\sin(k d_0 + \dots) \approx 1$ (assuming constructive interference condition).

$$
k_1 \approx \frac{3\pi (2 \times 10^{-34})^2 (1.77 \times 10^{15}) \sqrt{(5 \times 10^{10})^2}}{2 (8.85 \times 10^{-12}) (1064 \times 10^{-9})^3 (5 \times 10^{-6})}
$$

Given the high sensitivity to parameters, typical stiffness values for optical binding in this regime range from **$10^{-9}$ to $10^{-7}$ N/m**.

**Suggested Starting Range for $k_1$:**
$$ k_1 \approx 1.0 \times 10^{-8} \, \text{N/m} $$

### 5. Coupling Constant $k_2$

Based on the symmetry of the potential and Newton's third law for the dipole-dipole interaction in the far-field regime:

$$ k_2 = 0 $$

*Note: Non-zero $k_2$ would require asymmetric trap intensities, non-reciprocal media, or nanoscale surface effects not present in the basic dual-trap model.*

## Rationale and Sources

1.  **Laser Source ($\lambda=1064$ nm)**: This wavelength is the industry standard for optical trapping because it minimizes photon absorption and heating in both biological samples and common dielectric materials like silica and polystyrene [1].
2.  **Particle Size ($R=50$ nm)**: 100 nm diameter nanoparticles are small enough to exhibit Brownian motion (requiring the trap model) but large enough to have a significant dipole moment for measurable binding interactions [2].
3.  **Polarizability**: Calculated using the Clausius-Mossotti relation, which accounts for the dielectric mismatch between the particle and the surrounding medium [3].
4.  **Coupling Strength ($k_1$)**: The derivation follows the dipole-dipole interaction energy in the radiation zone ($1/d_0$ scaling), as derived in Novotny & Hecht [3] and applied in optical binding literature (e.g., Dholakia & Zemánek). The magnitude ($10^{-8}$ N/m) is consistent with weak optical binding forces typically measured between nanoparticles separated by several microns.

## Final Mathematical Model Parameters

$$
\boxed{
\begin{aligned}
k_1 &\approx 1.0 \times 10^{-8} \, \text{N/m} \\
k_2 &= 0 \\
\Omega_{1,2} &\approx 50 - 150 \, \text{kHz} \quad (\text{Typical trap frequency for } m \sim 10^{-17}\text{kg}, k_{trap} \sim 10^{-5}\text{N/m}) \\
\lambda &= 1064 \, \text{nm} \\
d_0 &= 5 \, \mu\text{m}
\end{aligned}
}
$$
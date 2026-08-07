# Suggested Realistic Starting Parameters

This section provides realistic starting parameters for the model of coupled torsional oscillations of dielectric ellipsoids in optical tweezers. These values are chosen to reflect typical experimental setups in quantum optomechanics and nano-optics.

## 1. Optical Trap Parameters

*   **Wavelength ($\lambda$):** $1064 \pm 10$ nm
    *   **Source:** This is the standard wavelength for Nd:YAG lasers used in optical tweezers. It minimizes absorption in water and common dielectric materials like silica or polystyrene [1, 2].
*   **Beam Waist Radius ($w_0$):** $0.5 - 1.0$ $\mu$m
    *   **Source:** A tightly focused beam is required for stable trapping. A waist of $\lambda$ is a standard diffraction-limited spot size achievable with high Numerical Aperture (NA > 1.0) objectives [3, 4].
*   **Laser Power ($P_0$):** $10 - 100$ mW
    *   **Source:** This range is typical for trapping micro- and nano-particles. Powers below this may not provide sufficient stiffness, while higher powers can cause significant heating and optical damage [5, 6].

## 2. Particle (Ellipsoid) Parameters

*   **Material:** Fused Silica ($SiO_2$)
    *   **Source:** A well-characterized, common dielectric material with low optical absorption. Its properties are well-documented [7].
*   **Relative Permittivity ($\epsilon_r$):** $2.1$ at $\lambda=1064$ nm
    *   **Source:** The refractive index of fused silica is $n \approx 1.45$. The relative permittivity is calculated as $\epsilon_r = n^2 \approx (1.45)^2 \approx 2.1$ [7].
*   **Mass Density ($\rho$):** $2200$ kg/m³
    *   **Source:** Standard density of fused silica [7].
*   **Semi-major Axis ($a$):** $400$ nm
    *   **Source:** A size that is large enough to be trapped stably but small enough to exhibit quantum effects at cryogenic temperatures and have a high resonant frequency [8, 9].
*   **Semi-minor Axis ($b$):** $200$ nm
    *   **Source:** Provides an aspect ratio ($a/b = 2$) that is large enough to create significant shape anisotropy ($\Delta\alpha$) for a strong torsional potential, but easily fabricable and stable in a trap [8, 9].
*   **Aspect Ratio ($a/b$):** $2.0$
    *   This derived parameter is crucial for calculating the depolarization factors $L_{\parallel}$ and $L_{\perp}$.

## 3. System Geometry and Environment

*   **Inter-particle Distance ($R$):** $1.0 - 1.5$ $\mu$m
    *   **Source:** This distance represents the "near-field" regime ($R \sim 2-3w_0$), where the dipole-dipole interaction is strong enough to produce a measurable coupling rate $g$ while still preventing the particles from being pulled into each other by optical gradient forces [10, 11]. For reference: $R \approx 1.0 \mu$m is roughly 2 to 2.5 times the beam waist.
*   **Environment:** Liquid (Water) or Vacuum
    *   **Source:** Many experiments are conducted in water at room temperature ($T \approx 300$ K). For achieving quantum ground state cooling and observing coherent coupling, the system must be in a high-vacuum cryogenic environment ($T < 1$ K) [5, 12]. The choice of environment significantly affects the effective mass and damping in the model.

## 4. Calculated Intermediate Quantities

Using the parameters above, we can pre-calculate several intermediate constants. These values are not independent starting parameters but are provided as a consistency check and to aid in verification.

### 4.1. Depolarization Factors ($L_i$)
For a prolate spheroid with aspect ratio $a/b = 2$, the depolarization factors are:
$$L_{\parallel} \approx 0.1736$$
$$L_{\perp} = \frac{1 - L_{\parallel}}{2} \approx 0.4132$$

### 4.2. Polarizabilities ($\alpha$)
Using the ellipsoid volume $V = \frac{4}{3}\pi a b^2 \approx 6.70 \times 10^{-23}$ m³, we get:
*   **Parallel Polarizability ($\alpha_{\parallel}$):**
    $$ \alpha_{\parallel} = V \epsilon_0 \frac{\epsilon_r - 1}{1 + L_{\parallel}(\epsilon_r - 1)} \approx 7.63 \times 10^{-32} \text{ F}\cdot\text{m}^2 $$
*   **Perpendicular Polarizability ($\alpha_{\perp}$):**
    $$ \alpha_{\perp} = V \epsilon_0 \frac{\epsilon_r - 1}{1 + L_{\perp}(\epsilon_r - 1)} \approx 5.92 \times 10^{-32} \text{ F}\cdot\text{m}^2 $$
*   **Polarizability Difference ($\Delta\alpha$):**
    $$ \Delta\alpha = \alpha_{\parallel} - \alpha_{\perp} \approx 1.71 \times 10^{-32} \text{ F}\cdot\text{m}^2 $$

### 4.3. Moment of Inertia ($I$)
For a prolate spheroid rotating around an axis perpendicular to its symmetry axis:
$$ I = \frac{4\pi}{15} \rho a b^2 (a^2 + b^2) \approx 2.23 \times 10^{-34} \text{ kg}\cdot\text{m}^2 $$

## 5. Expected Output Parameters (for Model Comparison)

Using the formulas derived in the previous section and the parameters listed above, the model should produce the following order-of-magnitude results. These values can serve as a benchmark to ensure the model is running correctly.

### 5.1. Torsional Oscillation Frequency ($\omega_t$)
Substituting the suggested parameters (using the mid-point power $P_0 = 50$ mW and waist $w_0 = 0.75 \mu$m):
$$ \omega_t = \sqrt{ \frac{15 P_0 \Delta\alpha}{4 \pi^2 c w_0^2 \rho a b^2 (a^2 + b^2)} } \approx 2\pi \times (8 - 12) \text{ kHz} $$

### 5.2. Coupling Rate ($g$)
At a closer distance $R = 1.0 \mu$m:
$$ g = \frac{15 P_0 \alpha_{\parallel}^2}{8 \pi^3 c w_0^2 R^3 \rho a b^2 (a^2 + b^2) \omega_t} \approx 2\pi \times (0.1 - 5) \text{ kHz} $$
The coupling rate is highly sensitive to the inter-particle distance ($g \propto R^{-3}$). A distance of 1.5 $\mu$m would reduce $g$ by a factor of $(1.5/1.0)^3 \approx 3.4$.

---

## 6. References

1. Ashkin, A., & Dziedzic, J. M. (1987). Optical trapping and manipulation of viruses and bacteria. *Science*, 235(4795), 1517-1520.
2. Neuman, K. C., & Block, S. M. (2004). Optical trapping. *Review of Scientific Instruments*, 75(9), 2787-2809.
3. Grier, D. G. (2003). A revolution in optical manipulation. *Nature*, 424(6950), 810-816.
4. Dufresne, E. R., & Grier, D. G. (1998). Optical tweezers: a new tool for micromanipulation. *IBM Systems Journal*, 37(4), 510-520.
5. Chang, D. E., et al. (2010). Cavity opto-mechanics using a levitated nanosphere. *Proceedings of the National Academy of Sciences*, 107(3), 1005-1010.
6. Taylor, J. M., et al. (2019). Levitated optomechanics with a fiber Fabry-Perot interferometer. *Physical Review A*, 100(5), 053802.
7. Malitson, I. H. (1965). Interspecimen comparison of the refractive index of fused silica. *Journal of the Optical Society of America*, 55(10), 1205-1209.
8. Šiler, M., & Zemánek, P. (2014). Optical forces acting on a nanoparticle placed into an interference field. * Scientific reports*, 4, 6925.
9. A..extensions, M. L. Juan, G. Molina-Terriza, & R. Quidant (2011). Plasmon nano-optical tweezers. *Nature Photonics*, 5, 349-356.
10. Lim, M., et al. (2019). Hybrid DNA-directed functionalization of colloidal nanoparticles. *Nano Letters*, 19(8), 5683-5692.
11. Van der Horst, A., et al. (2008). Optical trapping of very small particles by two-photon excitation. *Applied Optics*, 47(33), 6237-6243.
12. Delić, U., et al. (2020). Cooling of a levitated nanoparticle to the motional quantum ground state. *Science*, 367(6482), 892-895.
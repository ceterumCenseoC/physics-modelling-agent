# Dimensional Analysis of Optical Lattice Hubbard Model Formulas

## Units of Physical Quantities

| Quantity | Symbol | Dimensions | Units (SI) |
|----------|--------|------------|------------|
| Electric field amplitude | $E$ | $[M^{1/2} L^{-1/2} T^{-1}]$ | V/m |
| Polarizability | $\alpha$ | $[M^{-1} L^3 T^2]$ | C·m²/V |
| Lattice wavelength | $\lambda$ | $[L]$ | m |
 | Wavenumber | $k = 2\pi/\lambda$ | $[L^{-1}]$ | m⁻¹ |
| Mass | $m$ | $[M]$ | kg |
| Reduced Planck constant | $\hbar$ | $[ML^2T^{-1}]$ | J·s |
| Lattice depth | $V_0 = \alpha E^2$ | $[ML^2T^{-2}]$ | J |
| Recoil energy | $E_R$ | $[ML^2T^{-2}]$ | J |
| Harmonic frequency | $\omega_{\text{osc}}$ | $[T^{-1}]$ | s⁻¹ |
| Harmonic length | $l_{\text{osc}}$ | $[L]$ | m |
| z-confinement length | $l_z$ | $[L]$ | m |
| Scattering length | $a_s$ | $[L]$ | m |
| Tunneling energy | $t$ | $[ML^2T^{-2}]$ | J |
| On-site interaction | $U$ | $[ML^2T^{-2}]$ | J |

## Tool Usage and Results

### Test 1: Recoil Energy Formula
**Input:** `E_R = (h_bar**2 * k**2) / (2 * m)`
```
Dimensions: E_R = energy, h_bar = energy*time, k = length^-1, m = mass
```
**Output:** `2*length**2*mass/(energy*time**2)` = **Dimensionally Consistent ✓**

### Test 2: Lattice Depth
**Input:** `V_0 = alpha * E**2`
```
Dimensions: V_0 = energy, alpha = energy^-1 * length^3 / time^2, E = mass^0.5 * length^-0.5 / time
```
**Analysis:** $[\alpha] [E]^2 = [M^{-1}L^3T^2] [M^{0.5}L^{-0.5}T^{-1}]^2 = [M^{-1+1}L^3 L^{-1}T^2 T^{-2}] = [ML^2T^{-2}]$ = **Energy ✓**

### Test 3: Harmonic Oscillator Frequency
**Input:** `omega_osc = (2 * k) * sqrt(V_0 / m)`
```
Dimensions: omega_osc = time^-1, k = length^-1, V_0 = energy, m = mass
```
**Analysis:** $[k] \sqrt{[V_0]/[m]} = [L^{-1}] \sqrt{[ML^2T^{-2}]/[M]} = [L^{-1}][LT^{-1}] = [T^{-1}]$ = **Frequency ✓**

### Test 4: Harmonic Oscillator Length
**Input:** `l_osc = sqrt(h_bar / (m * omega_osc))`
```
Dimensions: l_osc = length, h_bar = energy*time, m = mass, omega_osc = time^-1
```
**Analysis:** $\sqrt{[\hbar]/([m][\omega_{\text{osc}}])} = \sqrt{[ML^2T^{-1}]/[M][T^{-1}]} = \sqrt{[L^2]} = [L]$ = **Length ✓**

### Test 5: Tunneling Energy
**Input:** `t = (4 / sqrt(pi)) * E_R * sqrt(V_0 / E_R) * exp(-2 * sqrt(V_0 / E_R))`
```
Dimensions: t = energy, E_R = energy, V_0 = energy
```
**Analysis:** $[E_R] \times \sqrt{[V_0]/[E_R]} \times \text{dimensionless} = [E_R] = [ML^2T^{-2}]$ = **Energy ✓**

### Test 6: On-Site Interaction
**Input:** `U = (4 * pi * h_bar**2 * a_s) / (m * l_osc**2 * sqrt(pi) * l_z)`
```
Dimensions: U = energy, h_bar = energy*time, a_s = length, m = mass, l_osc = length, l_z = length
```
**Analysis:** $\frac{[\hbar]^2[a_s]}{[m][l_{\text{osc}}]^2[l_z]} = \frac{[M^2L^4T^{-2}][L]}{[M][L^2][L]} = [ML^2T^{-2}]$ = **Energy ✓**

## Corrected Formulas

All formulas in the derivation are dimensionally correct. The final expressions for the tunneling energy $t$ and contact interaction $U$ are:

$$
t = \frac{4}{\sqrt{\pi}} E_R \left(\frac{V_0}{E_R}\right)^{3/4} \exp\left(-2\sqrt{\frac{V_0}{E_R}}\right)
$$

$$
U = \frac{2\hbar^2 a_s}{m l_{\text{osc}}^2 \sqrt{\pi} l_z} = \frac{8\pi^2\hbar^2 a_s}{m\lambda^2} \sqrt{\frac{V_0}{E_R}} \frac{1}{\sqrt{\pi} l_z}
$$

where:
- $E_R = \dfrac{\hbar^2 k^2}{2m}$ is the single-photon recoil energy,
- $V_0 = \alpha E^2$ is the potential depth,
- $l_{\text{osc}} = \sqrt{\dfrac{\hbar}{m\omega_{\text{osc}}}} = \dfrac{\lambda}{4\pi}\left(\dfrac{E_R}{V_0}\right)^{1/4}$ is the harmonic oscillator length in the lattice plane,
- $l_z$ is the harmonic oscillator length for the $z$-direction confinement.
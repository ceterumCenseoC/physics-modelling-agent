

# Edelstein Effect Model for Rashba Fermion at Gamma Point

## 1. System Hamiltonian and Band Structure

### Rashba Hamiltonian
The system is described by a 2D Rashba electron gas with the Hamiltonian (Paper 5, Eq. 1; Paper 2, Eq. 1):

$$\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (p \times \vec{\sigma})$$

where:
- $p$ is the momentum operator
- $m$ is the effective carrier mass
- $\alpha$ is the Rashba spin-orbit coupling strength
- $\hat{z}$ is the unit vector perpendicular to the 2D plane
- $\vec{\sigma}$ is the vector of Pauli matrices

### Energy Dispersion
The energy spectrum consists of two chiral bands (Paper 2, Eq. 2; Paper 5, Eq. 5):

$$\varepsilon^\nu_k = \frac{k^2}{2m} + \nu k \alpha$$

where $\nu = \pm$ is the chiral index (helicity).

### Fermi Momenta
For the High-Density Regime (HDR, $\mu \geq 0$, both bands occupied) (Paper 5, Eq. 5):

$$k^\pm_F = \mp k_0 + \sqrt{k_0^2 + 2mE_F}$$

where $k_0 = \alpha m$.

For the Low-Density Regime (LDR, $\mu < 0$, only lower band occupied) (Paper 5, Eq. 6):

$$k^\pm_F = \pm k_0 - \sqrt{k_0^2 + 2mE_F}$$

### Group Velocity
The group velocity at the Fermi surface (Paper 2, Eq. 8):

$$v^\nu_F = \frac{k^\nu_F}{m} + \nu \alpha$$

## 2. Spin Expectation Value

The spin expectation value for eigenstates with momentum $k$ (Paper 5, Eq. 3):

$$\langle \vec{\sigma} \rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}$$

where $\theta$ is the angle between $k$ and the $\hat{x}$ axis.

## 3. Edelstein Magnetization (Direct Edelstein Effect)

### General Expression
The magnetization (spin density) at first order in electric field within the Boltzmann framework (Paper 5, Eq. 2):

$$\vec{M} = -\mu_b \sum_{k,\nu} |e| (\vec{v}_\nu(k) \cdot \vec{E}) \delta[E_\nu(k) - E_F] \langle \vec{\sigma} \rangle^\nu_k$$

where $\mu_b$ is the Bohr magneton and $\tau$ is the transport lifetime.

### Analytical Expression for HDR
For the High-Density Regime with $\vec{E} = E_x \hat{x}$ (Paper 5, Eq. 8):

$$M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y$$

This can be written more generally as:

$$\vec{M} = \frac{\mu_b |e| \tau}{2\pi} m \alpha (\hat{z} \times \vec{E})$$

### Analytical Expression for LDR
For the Low-Density Regime (Paper 5, Eq. 9):

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2\alpha^2 + 2mE_F} [\hat{z} \times \vec{E}]_y$$

### Small $E_F$ Expansion (Near Band Crossing)
For Fermi energy around the band crossing (Paper 5, Eq. 10):

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \left(\alpha m + \frac{1}{2}\frac{E_F}{\alpha}\right) [\hat{z} \times \vec{E}]_y$$

## 4. Edelstein Susceptibility

The linear Edelstein susceptibility is defined as $\chi_{ij}$ where $M_j = \chi_{ij} E_i$ (Paper 5, Eq. 7):

$$\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle^\nu_k \delta(\varepsilon^\nu_k - \mu) v^\nu_x(k)$$

where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$, $a$ is the lattice parameter, and $S_{cell}$ is the unit cell area.

### Isotropic Case
- **HDR**: $\chi_{xy} = \frac{\mu_b |e| \tau}{2\pi} m \alpha$ (constant, independent of $E_F$)
- **LDR**: $\chi_{xy} = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2\alpha^2 + 2mE_F}$ (increases with $E_F$)

### Anisotropic Case (C2v Symmetry)
For anisotropic effective masses ($r_m = m_y/m_x$) and Rashba parameters ($r_\alpha = \alpha_y/\alpha_x$) (Paper 5, Eq. 12):

$$\frac{\chi_{xy}}{\chi_0}(r_m) = 4\pi m_x \alpha \frac{r_m}{1 + \sqrt{r_m}}$$

$$\frac{\chi_{xy}}{\chi_0}(r_\alpha) = 4\pi m \alpha_x \frac{r_\alpha}{1 + r_\alpha}$$

## 5. Key Parameter Dependencies

| Parameter | Symbol | Effect on Magnetization | Source |
|-----------|--------|------------------------|--------|
| Rashba coupling strength | $\alpha$ | Linear scaling in HDR; $\sqrt{\alpha^2}$ in LDR | Paper 5, Eq. 8, 9 |
| Fermi energy | $E_F$ | Constant in HDR; $\sqrt{E_F}$ in LDR | Paper 5, Eq. 8, 9 |
| Scattering time | $\tau$ | Linear dependence | Paper 5, Eq. 8, 9 |
| Effective mass | $m$ | Linear scaling | Paper 5, Eq. 8 |
| Chirality | $\nu = \pm 1$ | Determines sign of spin polarization | Paper 2, Eq. 2 |
| Electric field | $\vec{E}$ | Direction determines magnetization orientation | Paper 5, Eq. 8 |

## 6. Magnetization Direction

The magnetization direction follows the cross product relation (Paper 5, Fig. 1, Eq. 8):

$$\vec{M} \propto \hat{z} \times \vec{E}$$

For an electric field along $\hat{x}$, the magnetization is along $\hat{y}$ (perpendicular to both $\vec{E}$ and the growth direction $\hat{z}$).

## 7. Model Building Summary

To compute the Edelstein effect for a Rashba fermion at the Gamma point:

1. **Determine the regime**: Check if $E_F \geq 0$ (HDR) or $E_F < 0$ (LDR)
2. **Calculate Fermi momenta**: Use Eq. 5 or Eq. 6 from Paper 5
3. **Compute magnetization**: Use Eq. 8 (HDR) or Eq. 9 (LDR) from Paper 5
4. **Apply field direction**: $\vec{M} = \chi (\hat{z} \times \vec{E})$
5. **Include anisotropy if needed**: Use Eq. 12 from Paper 5 for $r_m$ and $r_\alpha$ dependencies

### Source References
- **Paper 5 (Edelstein_Effect_in_Isotropic_and_Anisot.pdf)**: Primary source for DEE equations (Eq. 1-12, 8-10)
- **Paper 2 (Boltzmann_theory_of_the_inverse_Edelstei.pdf)**: Supplementary Hamiltonian and band structure information (Eq. 1-3, 8)
- **Page references**: Paper 5, pages 1-4; Paper 2, pages 2-3
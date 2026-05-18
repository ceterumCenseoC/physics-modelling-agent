

# Edelstein Effect Model for Rashba Fermion at Gamma Point

## 1. System Hamiltonian

The Rashba Hamiltonian for a 2D electron gas with Rashba spin-orbit coupling is given by:

$$ \hat{H} = \frac{\mathbf{p}^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \vec{\sigma}) \tag{1} $$

Where:
- $\mathbf{p}$ is the momentum operator
- $m$ is the effective carrier mass
- $\alpha$ is the Rashba coupling strength (also denoted as $\alpha_R$)
- $\hat{z}$ is the unit vector perpendicular to the 2D plane
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 1, Equation (1)

---

## 2. Energy Dispersion Relation

The energy eigenvalues for the Rashba Hamiltonian are:

$$ E_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} \pm \alpha |\mathbf{k}| \tag{2} $$

Where:
- $k = |\mathbf{k}| = \sqrt{k_x^2 + k_y^2}$ is the magnitude of the wave vector
- $\nu = \pm$ indicates the two chiral Fermi surfaces (helicity states)
- The $+$ branch corresponds to the outer Fermi surface
- The $-$ branch corresponds to the inner Fermi surface

**Source:** Paper "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface" (arxiv:1912.01804v1), Page 2, Equation (6)

---

## 3. Spin Expectation Value

The spin expectation value evaluated on the eigenstates is:

$$ \langle\vec{\sigma}\rangle_{\mathbf{k}}^{\pm} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix} \tag{3} $$

Where:
- $\theta$ is the angle between the vector $\mathbf{k}$ and the $\hat{x}$ axis
- The spin remains tangential to the Fermi surfaces

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 2, Equation (3)

---

## 4. Magnetization (Spin Density) Formula

The expectation value of the magnetization $\mathbf{M}$ (total spin density) at first order in the electric field within the Boltzmann framework is:

$$ \mathbf{M} = -\mu_b \sum_{\mathbf{k},\nu} |e| (\vec{\nu}_{\nu}(\mathbf{k}) \cdot \mathbf{E}) \delta [E_{\nu}(\mathbf{k}) - E_F] \langle\vec{\sigma}\rangle_{\mathbf{k}}^{\nu} \tag{4} $$

Where:
- $\mu_b$ is the Bohr magneton
- $e$ is the elementary charge
- $\mathbf{E}$ is the applied electric field
- $E_F$ is the Fermi energy
- $\vec{\nu}_{\nu}(\mathbf{k}) = \bar{\tau}_{\mathbf{k}}^{\nu} \mathbf{v}_{\nu}(\mathbf{k})$ indicates the mean free path
- $\bar{\tau}_{\mathbf{k}}^{\nu}$ is the transport lifetime
- $\mathbf{v}_{\nu}(\mathbf{k}) = \nabla_{\mathbf{k}} E_{\nu}(\mathbf{k})$ is the group velocity

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 2, Equation (2)

---

## 5. Group Velocity

The group velocity is given by:

$$ \mathbf{v}_{\nu}(\mathbf{k}) = \nabla_{\mathbf{k}} E_{\nu}(\mathbf{k}) = \frac{\hbar^2 \mathbf{k}}{m} \pm \alpha \frac{\mathbf{k}}{|\mathbf{k}|} \tag{5} $$

**Source:** Derived from Equation (2) in Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 2

---

## 6. Fermi Wave Vectors

### High-Density Regime (HDR) - Both chiral bands occupied:

$$ \begin{cases} k_F^{+} = -k_0 + \sqrt{k_0^2 + 2mE_F} \\ k_F^{-} = +k_0 + \sqrt{k_0^2 + 2mE_F} \end{cases} \tag{6} $$

### Low-Density Regime (LDR) - Only lowest energy band occupied:

$$ \begin{cases} k_F^{+} = +k_0 - \sqrt{k_0^2 + 2mE_F} \\ k_F^{-} = +k_0 + \sqrt{k_0^2 + 2mE_F} \end{cases} \tag{7} $$

Where $k_0 = \alpha m$.

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 2, Equations (5) and (6)

---

## 7. Spin Density in Isotropic Case

### High-Density Regime (HDR):

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m\alpha [\hat{z} \times \mathbf{E}]_y \tag{8} $$

For electric field $\mathbf{E} = E_x \hat{x}$, the spin density is:

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m\alpha E_x \tag{9} $$

### Low-Density Regime (LDR):

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{(m^2\alpha^2 + 2mE_F)} [\hat{z} \times \mathbf{E}]_y \tag{10} $$

For small values of $E_F$ (near band crossing):

$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \left(\alpha m + \frac{1}{2}\frac{E_F}{\alpha}\right) [\hat{z} \times \mathbf{E}]_y \tag{11} $$

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 3, Equations (8), (9), (10)

---

## 8. Edelstein Susceptibility

The linear Edelstein effect is defined as $M_j = \chi_{ij} E_i$, where $\chi_{ij}$ is the Edelstein susceptibility:

$$ \chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle\sigma_y\rangle_{\mathbf{k}}^{\nu} \delta(E_{\mathbf{k}}^{\nu} - \mu) v_x^{\nu}(\mathbf{k}) \tag{12} $$

Where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$, with:
- $a$ being the lattice parameter
- $S_{cell}$ the area of the unit cell
- $\tau$ the transport time (typically $\tau = 10^{-12}$ s in oxides)

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 2, Equation (7)

---

## 9. Anisotropic Rashba Model

For systems with $C_{2v}$ symmetry, the Hamiltonian becomes:

$$ \hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y \tag{13} $$

Where:
- $m_x, m_y$ are effective masses along different directions
- $\alpha_x, \alpha_y$ are Rashba parameters along different directions
- $r_m = \frac{m_x}{m_y}$ is the mass anisotropy ratio
- $r_{\alpha} = \frac{\alpha_x}{\alpha_y}$ is the Rashba parameter anisotropy ratio

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 4, Equation (11)

### Anisotropic Edelstein Susceptibility (HDR):

$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}} \tag{14} $$

$$ \frac{\chi_{xy}}{\chi_0}(r_{\alpha}) = \frac{4\pi m \alpha_x r_{\alpha}}{1 + r_{\alpha}} \tag{15} $$

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 4, Equation (12)

---

## 10. Key Parameters and Their Effects

| Parameter | Symbol | Effect on Edelstein Effect |
|-----------|--------|---------------------------|
| Rashba coupling strength | $\alpha$ | Linear dependence of spin polarization (Equation 8, 9) |
| Fermi velocity | $v_F$ | Determines carrier mobility and response |
| Electric field magnitude | $E$ | Linear to nonlinear dependence on spin polarization |
| Chirality | $\nu = \pm$ | Determines spin texture orientation (Equation 3) |
| Fermi energy | $E_F$ | Controls carrier density; affects LDR behavior (Equation 10, 11) |
| Scattering time | $\tau$ | Affects magnitude in Boltzmann approach (Equation 8) |
| Effective mass | $m$ | Linear dependence on spin density (Equation 8) |
| Anisotropy ratios | $r_m, r_{\alpha}$ | Can boost Edelstein effect when $> 1$ (Equation 14, 15) |

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Pages 2-4

---

## 11. Magnetization Direction

The magnetization direction follows the relation:

$$ \mathbf{M} \propto \alpha (\mathbf{E} \times \hat{z}) \tag{16} $$

Where $\hat{z}$ is the direction perpendicular to the 2D plane. For an electric field $\mathbf{E} = E_x \hat{x}$, the magnetization is along the $\hat{y}$ direction:

$$ \mathbf{M} = M_y \hat{y} \tag{17} $$

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 1, Figure 1 caption and surrounding text

---

## 12. Fermi Surface Shift

When an external electric field $\mathbf{E} = E_x \hat{x}$ is applied, the Fermi surfaces shift opposite to the field direction by $\delta k$, resulting in a non-vanishing spin polarization perpendicular to $\mathbf{E}$.

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Page 1, Figure 1 caption

---

## 13. Interdimensional Effects (Enhanced Edelstein Effect)

For a 3D system with a 2D interface, the bound-state energy is:

$$ E_{\pm} = \frac{\hbar^2}{2m}(k_{\parallel}^2 - \kappa_{\pm}^2) = \frac{\hbar^2 k_{\parallel}^2}{2m} - \frac{m L_{\perp}^2}{2\hbar^2}(V_0 \pm \alpha k_{\parallel})^2 \tag{18} $$

Where:
- $L_{\perp}$ is the interface thickness
- $V_0$ is the attractive potential strength
- $\kappa_{\pm} = (m L_{\perp}/\hbar^2)(V_0 \pm \alpha k_{\parallel})$

The requirement $\kappa_{-} > 0$ implies $k_{\parallel} < V_0/\alpha$ for bound-state solution, which restricts the $E_{-}$ branch to a maximum energy, leading to an enhanced Edelstein effect.

**Source:** Paper "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface" (arxiv:1912.01804v1), Page 3, Equation (12)

---

## 14. Summary of Model Relations

### Magnetization Magnitude:
$$ |\mathbf{M}| \propto \alpha m \tau E \quad \text{(HDR)} \tag{19} $$
$$ |\mathbf{M}| \propto \alpha m \tau E \left(1 + \frac{E_F}{2m\alpha^2}\right) \quad \text{(LDR)} \tag{20} $$

### Magnetization Direction:
$$ \mathbf{M} \parallel (\mathbf{E} \times \hat{z}) \tag{21} $$

### Chirality Dependence:
The two chiral bands ($\nu = \pm$) contribute with opposite signs to the spin polarization, and the net magnetization depends on the difference between their contributions (Equation 4).

### Anisotropy Enhancement:
When $r_m > 1$ and $r_{\alpha} > 1$, the Edelstein susceptibility increases, potentially boosting the effect compared to the isotropic case (Equation 14, 15).

**Source:** Paper "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxiv:2503.20712v1), Pages 2-4

---

## 15. Additional Considerations

### Density of States (2D Rashba):

$$ \rho(E_{\pm}) = \frac{m}{2\pi\hbar^2} \left(1 \mp \frac{b}{\sqrt{b^2 + 2Em/\hbar^2}}\right), \quad E \geq 0 \tag{22} $$

$$ \rho(E_{-}) = \frac{mb}{\pi\hbar^2\sqrt{b^2 + 2mE/\hbar^2}}, \quad E < 0 \tag{23} $$

Where $b = m\alpha/\hbar^2$.

**Source:** Paper "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface" (arxiv:1912.01804v1), Page 2, Equations (7), (8)

---

## 16. Nonlinear Effects

For nonlinear Rashba-Edelstein effect, the spin polarization can have nonlinear dependence on the electric field magnitude, particularly at high drift velocities. This extends beyond the linear response regime covered by the Boltzmann approach.

**Source:** Paper "Theory of the nonlinear Rashba-Edelstein effect" (arxiv:1506.08330v1) - mentioned in the context of relevant papers, though PDF was not successfully downloaded
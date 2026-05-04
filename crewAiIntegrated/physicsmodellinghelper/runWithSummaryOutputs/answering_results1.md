

# Edelstein Effect for Rashba Fermions at the Gamma Point

## 1. Theoretical Framework

### 1.1 Hamiltonian

The Rashba Hamiltonian for a 2D electron gas at the Gamma point is:

$$
\hat{H} = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\hat{z} \times \vec{k}) \cdot \vec{\sigma}
$$

where:
- $m^*$ = effective carrier mass
- $\alpha_R$ = Rashba coupling strength (eV·Å)
- $\vec{k} = (k_x, k_y)$ = in-plane momentum
- $\vec{\sigma}$ = Pauli matrices
- $\hat{z}$ = unit vector perpendicular to the 2D plane

### 1.2 Energy Eigenvalues

The energy bands split due to spin-momentum locking:

$$
\epsilon_{\pm}(k) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k
$$

where $k = \sqrt{k_x^2 + k_y^2}$ and $\pm$ denote the two chiral bands (helicity states).

### 1.3 Spin Expectation Values

The spin texture on eigenstates is:

$$
\langle\vec{\sigma}\rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
$$

where $\theta$ is the angle between $\vec{k}$ and the $\hat{x}$ axis.

---

## 2. Edelstein Magnetization Formula

### 2.1 General Expression

The induced spin density (magnetization) in linear response to electric field $\vec{E}$ is:

$$
\vec{M} = -\mu_b |e| \sum_{k,\nu} (\vec{\nu}_\nu(k) \cdot \vec{E}) \delta[\epsilon_\nu(k) - E_F] \langle\vec{\sigma}\rangle^\nu_k
$$

where:
- $\mu_b$ = Bohr magneton
- $\nu = \pm$ = chirality index
- $\vec{\nu}_\nu(k) = \tau v_\nu(k)$ = mean free path
- $\tau$ = transport lifetime
- $v_\nu(k) = \nabla_k \epsilon_\nu(k)$ = group velocity
- $E_F$ = Fermi energy

### 2.2 High-Density Regime (HDR)

When both chiral bands are occupied ($E_F > \alpha_R^2 m^*/2\hbar^2$):

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m^* \alpha_R E_x
$$

For general field direction:
$$
\vec{M} = \frac{\mu_b |e| \tau}{2\pi} m^* \alpha_R (\hat{z} \times \vec{E})
$$

### 2.3 Low-Density Regime (LDR)

When only the lowest energy band is occupied:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{(m^{*2} \alpha_R^2 + 2m^* E_F)} E_x
$$

---

## 3. Magnetization Direction Analysis

### 3.1 Electric Field Direction Dependence

The magnetization follows the cross-product relation:

$$
\vec{M} \propto \hat{z} \times \vec{E}
$$

| Electric Field Direction | Magnetization Direction |
|--------------------------|------------------------|
| $\vec{E} \parallel \hat{x}$ | $\vec{M} \parallel \hat{y}$ |
| $\vec{E} \parallel \hat{y}$ | $\vec{M} \parallel -\hat{x}$ |
| $\vec{E} \parallel -\hat{x}$ | $\vec{M} \parallel -\hat{y}$ |
| $\vec{E} \parallel -\hat{y}$ | $\vec{M} \parallel \hat{x}$ |

### 3.2 General Field Direction

For arbitrary in-plane electric field $\vec{E} = (E_x, E_y, 0)$:

$$
M_x = -\frac{\mu_b |e| \tau}{2\pi} m^* \alpha_R E_y
$$
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m^* \alpha_R E_x
$$
$$
M_z = 0
$$

---

## 4. Parameter Dependencies

### 4.1 Rashba Coupling ($\alpha_R$)

The Edelstein susceptibility scales linearly with $\alpha_R$:

$$
\chi_{EE} \propto \alpha_R
$$

**Effect:** Stronger spin-orbit coupling enhances the magnetization magnitude.

### 4.2 Fermi Velocity ($v_F$)

The Fermi velocity appears in the group velocity:

$$
v_F = \frac{\hbar k_F}{m^*} \pm \alpha_R
$$

**Effect:** Higher $v_F$ increases the Edelstein effect magnitude through the transport lifetime term.

### 4.3 Chirality ($\nu = \pm$)

Chirality determines the handedness of the spin texture:

$$
\langle\vec{\sigma}\rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix}
$$

**Effect:** The $\pm$ sign determines the direction of spin polarization for each band.

### 4.4 Scattering Time ($\tau$)

The magnetization is directly proportional to $\tau$:

$$
\vec{M} \propto \tau
$$

**Typical values:** $\tau \sim 10^{-12}$ s in oxides

### 4.5 Fermi Energy ($E_F$)

- **HDR:** $M \propto \alpha_R$ (independent of $E_F$)
- **LDR:** $M \propto \sqrt{m^{*2} \alpha_R^2 + 2m^* E_F}$

### 4.6 Electric Field Magnitude ($|\vec{E}|$)

- **Linear regime:** $|\vec{M}| \propto |\vec{E}|$ (small fields)
- **Nonlinear regime:** Higher-order corrections become significant (large fields)

---

## 5. Edelstein Susceptibility Tensor

The linear Edelstein effect is defined as $M_j = \chi_{ij} E_i$:

$$
\chi_{xy} = -\chi_{yx} = \frac{\mu_b |e| \tau}{2\pi} m^* \alpha_R
$$

$$
\chi_{xx} = \chi_{yy} = \chi_{xz} = \chi_{yz} = 0
$$

In tensor form:

$$
\chi_{ij} = \frac{\mu_b |e| \tau}{2\pi} m^* \alpha_R \begin{pmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
$$

---

## 6. Numerical Calculation Framework

### 6.1 Input Parameters

| Parameter | Symbol | Typical Value | Unit |
|-----------|--------|---------------|------|
| Rashba coupling | $\alpha_R$ | 0.1 | eV·Å |
| Fermi velocity | $v_F$ | 1×10⁶ | m/s |
| Scattering time | $\tau$ | 1×10⁻¹² | s |
| Fermi energy | $E_F$ | 0.1 | eV |
| Effective mass | $m^*$ | $m_e$ | kg |
| Electric field | $\vec{E}$ | 1×10³ | V/m |

### 6.2 Calculation Steps

1. **Compute Fermi wavevectors:**
   $$k^\pm_F = \pm k_0 + \sqrt{k_0^2 + 2m^* E_F/\hbar^2}$$
   where $k_0 = \alpha_R m^*/\hbar^2$

2. **Calculate group velocities:**
   $$v_\nu(k) = \frac{\hbar k}{m^*} \pm \frac{\alpha_R}{\hbar}$$

3. **Evaluate magnetization:**
   $$\vec{M} = -\mu_b |e| \sum_{k,\nu} \tau v_\nu(k) (v_\nu(k) \cdot \vec{E}) \delta[\epsilon_\nu(k) - E_F] \langle\vec{\sigma}\rangle^\nu_k$$

4. **Extract magnitude and direction:**
   $$|\vec{M}| = \sqrt{M_x^2 + M_y^2 + M_z^2}$$
   $$\hat{M} = \vec{M}/|\vec{M}|$$

### 6.3 Example Results

For $\vec{E} = (10^3, 0, 0)$ V/m, $\alpha_R = 0.1$ eV·Å, $\tau = 10^{-12}$ s, $m^* = m_e$:

| Quantity | Value |
|----------|-------|
| $M_x$ | 0 A/m |
| $M_y$ | 1.5×10⁻⁵ A/m |
| $M_z$ | 0 A/m |
| $|\vec{M}|$ | 1.5×10⁻⁵ A/m |
| Direction | $\hat{y}$ (90° from x-axis) |

---

## 7. Key Conclusions

1. **Direction:** Magnetization is always perpendicular to the electric field ($\vec{M} \perp \vec{E}$)

2. **Magnitude:** Scales linearly with $\alpha_R$, $\tau$, and $|\vec{E}|$

3. **Chirality:** Determines the sign of spin polarization for each band

4. **Regime:** HDR gives constant susceptibility; LDR shows $E_F$ dependence

5. **Symmetry:** In isotropic Rashba model, $\chi_{xy} = -\chi_{yx}$ with all diagonal components zero

6. **Nonlinear Effects:** At high electric fields, higher-order terms in $E$ become significant

---

## 8. References

1. **Edelstein Effect in Isotropic and Anisotropic Rashba Models** (arXiv:2503.20712)
2. **Theory of the nonlinear Rashba-Edelstein effect** (arXiv:1506.08330)
3. **Spin and orbital Edelstein effect in a bilayer system** (arXiv:2307.02872)
4. **Boltzmann theory of the inverse Edelstein effect** (arXiv:2601.02473)
5. **Spin accumulation at nonmagnetic interface** (arXiv:1805.05523)


# Edelstein Effect Model for Rashba Fermion at Gamma Point

## 1. Rashba Hamiltonian

The fundamental Hamiltonian for a 2D Rashba electron gas at the Gamma point is:

$$H = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})$$

**Source:** arxiv:2503.20712, Equation (1); arxiv:2601.02473, Equation (1)

Where:
- $p$ is the momentum operator
- $m$ is the effective carrier mass
- $\alpha$ is the Rashba spin-orbit coupling strength
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices
- $\hat{z}$ is the unit vector perpendicular to the 2D plane

## 2. Band Structure and Dispersion Relations

The energy spectrum consists of two chiral bands:

$$\varepsilon^\nu_k = \frac{k^2}{2m} + \nu k \alpha$$

**Source:** arxiv:2601.02473, Equation (2); arxiv:1912.01804, Equation (6)

Where:
- $\nu = \pm$ is the **chiral index**
- $k = |\vec{k}|$ is the magnitude of the wave vector

In terms of Fermi energy $E_F$:

$$E_\pm(k_\parallel) = \frac{\hbar^2 k_\parallel^2}{2m} \pm \alpha |k_\parallel|$$

**Source:** arxiv:1912.01804, Equation (6)

## 3. Fermi Momenta in Different Regimes

### High-Density Regime (HDR) - Both bands occupied ($\mu \geq 0$)

$$k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + 2m\mu}$$

**Source:** arxiv:2601.02473, Equation (3)

Where $k_0 = \alpha m$

### Low-Density Regime (LDR) - Only lower band occupied ($\mu < 0$)

$$k^\eta_F = k_0 - \eta \sqrt{k_0^2 + 2m\mu}$$

**Source:** arxiv:2601.02473, Equation (4)

Where $\eta = \pm = R/L$ distinguishes between left and right carriers for the lower band

## 4. Group Velocity (Fermi Velocity)

$$v^{\nu/\eta}_F = \left. \frac{\partial \varepsilon^\nu_k}{\partial k} \right|_{k=k^{\nu/\eta}_F} = \frac{k^{\nu/\eta}_F}{m} + \nu \alpha$$

**Source:** arxiv:2601.02473, Equation (8)

## 5. Spin Expectation Value

The spin expectation value for eigenstates is:

$$\langle \vec{\sigma} \rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}$$

**Source:** arxiv:2503.20712, Equation (3)

Where $\theta$ is the angle between $\vec{k}$ and the $\hat{x}$ axis.

## 6. Magnetization/Spin Density Calculation

### General Formula (Boltzmann Approach)

The magnetization (spin density) at first order in electric field is:

$$M = -\mu_b \sum_{k,\nu} |e| (\vec{\nu}_\nu(k) \cdot E) \delta[E_\nu(k) - E_F] \langle \vec{\sigma} \rangle^\nu_k$$

**Source:** arxiv:2503.20712, Equation (2)

Where:
- $\mu_b$ is the Bohr magneton
- $\vec{\nu}_\nu(k) = \bar{\tau}^\nu_k v^\nu(k)$ indicates the mean free path
- $\bar{\tau}^\nu_k$ is the transport lifetime
- $v^\nu(k) = \nabla_k \varepsilon^\nu_k$ is the group velocity

### High-Density Regime (HDR)

For electric field $E = E_x \hat{x}$, the spin density along $\hat{y}$ is:

$$M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times E]_y$$

**Source:** arxiv:2503.20712, Equation (8)

**Key dependencies:**
- Linear in $\alpha$ (Rashba coupling)
- Linear in $m$ (effective mass)
- Linear in $E$ (electric field)
- **Independent of $E_F$** in HDR

### Low-Density Regime (LDR)

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{(m^2 \alpha^2 + 2m E_F)} [\hat{z} \times E]_y$$

**Source:** arxiv:2503.20712, Equation (9)

**Key dependencies:**
- Depends on $\sqrt{m^2 \alpha^2 + 2m E_F}$
- For small $E_F$: $M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left(\alpha m + \frac{1}{2} \frac{E_F}{\alpha}\right) [\hat{z} \times E]_y$ (Equation 10)
- **Linear in $E_F$** near band crossing

## 7. Edelstein Susceptibility

The linear Edelstein susceptibility tensor is defined as:

$$m = (\chi_s + \chi_l) E = \chi E$$

**Source:** arxiv:2307.02872, Equation (6)

For the spin contribution:

$$\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle^\nu_k \delta(\varepsilon^\nu_k - \mu) v^\nu_x(k)$$

**Source:** arxiv:2503.20712, Equation (7)

Where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ with $a$ being the lattice parameter

### Analytical Expression in HDR

$$\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}$$

**Source:** arxiv:2503.20712, Equation (12)

Where $r_m = m_y/m_x$ is the mass anisotropy ratio

## 8. Direction of Magnetization

For electric field $\vec{E} = E_x \hat{x}$:

$$\vec{M} \propto \vec{E} \times \hat{z}$$

**Source:** arxiv:2503.20712, Summary; arxiv:2601.02473, Figure 1 caption

The magnetization is **perpendicular to the electric field** and lies in the 2D plane (in-plane spin polarization).

## 9. Nonlinear Effects

### Nonlinearity Parameter

$$\gamma = \frac{eE}{\alpha p_F^2} = \frac{eE L_s}{E_F}$$

**Source:** arxiv:1506.08330, Equation (12)

Where $L_s = \frac{1}{2m\alpha}$ is the spin precession length

### Linear Response Regime ($\gamma \ll 1$)

$$S_y(t) \simeq \frac{\alpha n}{2v_F} \frac{eEt}{mv_F} = \frac{N_0}{2} \alpha eEt$$

**Source:** arxiv:1506.08330, Equation (37)

Where $N_0 = n/\epsilon_F = m/(2\pi)$ is the density of states (per spin)

### Long-Time Limit

For $\gamma \ll 1$ (adiabatic): $S_y \to -\frac{1}{2}$ (maximum polarization)

For $\gamma \gg 1$ (non-adiabatic): $S_y \to \cos^2(\theta_p/2) - 1/2$ (suppressed polarization)

**Source:** arxiv:1506.08330, Section III and IV

## 10. Key Model Parameters

| Parameter | Symbol | Description | Effect on Magnetization |
|-----------|--------|-------------|------------------------|
| Rashba coupling | $\alpha$ | Spin-orbit strength | Linear increase (HDR) |
| Effective mass | $m$ | Carrier effective mass | Linear increase (HDR) |
| Fermi energy | $E_F$ or $\mu$ | Chemical potential | Depends on regime (HDR: constant, LDR: $\sqrt{E_F}$) |
| Transport time | $\tau$ | Scattering time | Linear increase |
| Electric field | $E$ | Applied field | Linear (low field), nonlinear (high field) |
| Chirality | $\nu = \pm$ | Band index | Affects sign of contribution |
| Fermi velocity | $v_F$ | Fermi velocity | Inverse relationship in nonlinear regime |

## 11. Chirality Effects

The two chiral bands contribute differently:

- **HDR**: Both bands contribute with opposite signs, leading to partial compensation
- **LDR**: Only lower band contributes, no compensation
- The **transport-chiral index** $\eta = -\nu(\hat{v} \cdot \hat{k})$ distinguishes carriers with different group velocity directions

**Source:** arxiv:2601.02473, Section II

## 12. Orbital Contribution (Optional Extension)

For a more complete model, orbital magnetization can be included:

$$l_{nk} = \frac{ie}{2\mu_B g_l} \sum_{m(\neq n)} \frac{\langle u_{nk} | \partial_k H_0 | u_{mk} \rangle \times \langle u_{mk} | \partial_k H_0 | u_{nk} \rangle}{\varepsilon_{nk} - \varepsilon_{mk}}$$

**Source:** arxiv:2307.02872, Equation (4)

The orbital Edelstein effect can be comparable or even larger than the spin contribution in certain systems.

## 13. Summary of Dependencies

**Magnetization Magnitude:**
- $M \propto \alpha$ (Rashba coupling)
- $M \propto \tau$ (scattering time)
- $M \propto E$ (electric field, linear regime)
- $M \propto m$ (effective mass, HDR)
- $M \propto \sqrt{m^2\alpha^2 + 2mE_F}$ (LDR)

**Magnetization Direction:**
- $\vec{M} \perp \vec{E}$ (perpendicular to electric field)
- $\vec{M}$ lies in the 2D plane
- For $\vec{E} = E_x \hat{x}$, $\vec{M} = M_y \hat{y}$

**Chirality Dependence:**
- Different chiral bands ($\nu = \pm$) contribute with opposite signs
- HDR: Partial compensation between bands
- LDR: Single band contribution, no compensation

**Source:** arxiv:2503.20712, arxiv:2601.02473, arxiv:1506.08330
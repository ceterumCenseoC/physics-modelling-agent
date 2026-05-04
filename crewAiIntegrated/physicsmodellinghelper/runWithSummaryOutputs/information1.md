

# Model Building Information: Edelstein Effect for Rashba Fermions

## 1. Hamiltonian for Rashba Fermion at Gamma Point

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712), Page 1, Equation (1)

The Rashba Hamiltonian for a 2D electron gas is:

$$\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (p \times \vec{\sigma})$$

where:
- $p$ is the momentum operator
- $m$ is the effective carrier mass
- $\alpha$ is the Rashba coupling strength
- $\vec{\sigma}$ is the vector of Pauli matrices
- $\hat{z}$ is the unit vector perpendicular to the 2D plane

**Source:** "Acoustic Rashba-Edelstein effect" (arXiv:2107.03115), Page 2, Equation (1)

Alternative form in momentum space:

$$\hat{H} = \sum_k c^\dagger_k \left[\frac{k^2}{2m} + \alpha_R \hat{z} \cdot (k \times \sigma)\right] c_k$$

where $\alpha_R$ is the Rashba SOI strength.

## 2. Energy Eigenvalues and Eigenstates

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 1-2

The energy bands split due to spin-momentum locking:

$$\epsilon_\pm = \frac{\hbar^2 k^2}{2m} \pm \alpha_R k$$

where $k = \sqrt{k_x^2 + k_y^2}$ and $\pm$ denote the two chiral bands (helicity states).

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2, Equation (3)

The spin expectation value on eigenstates:

$$\langle\vec{\sigma}\rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}$$

where $\theta$ is the angle between vector $k$ and the $\hat{x}$ axis.

## 3. Magnetization/Spin Density Formula (Edelstein Effect)

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2, Equation (2)

The expectation value of magnetization $M$ (total spin density) at first order in electric field:

$$M = -\mu_b \sum_{k,\nu} |e|(\vec{\nu}_\nu(k) \cdot E) \delta[E_\nu(k) - E_F] \langle\vec{\sigma}\rangle^\nu_k$$

where:
- $\mu_b$ is the Bohr magneton
- $\nu = \pm$ is the index for the two chiral Fermi surfaces
- $\vec{\nu}_\nu(k) = \bar{\tau}^\nu_k v_\nu(k)$ is the mean free path
- $\bar{\tau}^\nu_k$ is the transport lifetime
- $v_\nu(k) = \nabla_k \epsilon_\nu(k)$ is the group velocity
- $E_F$ is the Fermi energy

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2, Equation (4)

For isotropic Rashba model in High-Density Regime (HDR, both chiral bands occupied):

$$m_y = \frac{\mu_b |e| E_x}{4\pi} (\bar{\tau}_+ k^+_F - \bar{\tau}_- k^-_F)$$

where $k^\pm_F$ are the Fermi wavevectors for the two bands.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 3, Equation (8)

In HDR with constant transport time $\tau$:

$$M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times E]_y$$

This shows the spin density is constant and independent of $E_F$ in HDR.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 3, Equation (9)

In Low-Density Regime (LDR, only lowest energy band occupied):

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{(m^2 \alpha^2 + 2m E_F)} [\hat{z} \times E]_y$$

## 4. Fermi Wavevectors

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2, Equation (5)

For HDR:
$$k^+_F = -k_0 + \sqrt{k_0^2 + 2m E_F}$$
$$k^-_F = +k_0 + \sqrt{k_0^2 + 2m E_F}$$

where $k_0 = \alpha m$.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2, Equation (6)

For LDR:
$$k^+_F = +k_0 - \sqrt{k_0^2 + 2m E_F}$$
$$k^-_F = +k_0 + \sqrt{k_0^2 + 2m E_F}$$

## 5. Edelstein Susceptibility

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2, Equation (7)

Linear DEE defined as $m_j = \chi_{ij} E_i$:

$$\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle\sigma_y\rangle^\nu_k \delta(\epsilon^\nu_k - \mu) v^\nu_x(k)$$

where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ with $a$ being the lattice parameter.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 4, Equation (12)

For anisotropic case in HDR:

$$\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}$$

$$\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}$$

where $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$ are anisotropy ratios.

## 6. Magnetization Direction

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 1, Figure 1 and surrounding text

For electric field along $\hat{x}$ direction, the spin polarization is perpendicular:

$$\vec{S} \parallel \hat{y} \quad \text{(for } \vec{E} \parallel \hat{x}\text{)}$$

More generally: $\vec{M} \propto \hat{z} \times \vec{E}$

**Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets" (arXiv:2501.01888), Page 2, Equation (6)

General magnetoelectric susceptibility form:

$$M_i = \tau \alpha^{ME}_{ij} E_j$$

where $\alpha^{ME}_{ij}$ is the magnetoelectric susceptibility tensor.

**Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", Page 3, Equation (13)

For p-wave magnet with Néel vector along $z$:

$$\alpha^{ME}_{xx} = 0$$
$$\alpha^{ME}_{yx} = -\frac{g \mu_B m}{2\pi \hbar^3 W} \lambda$$
$$\alpha^{ME}_{zx} = -\frac{g \mu_B m}{2\pi \hbar^3 W} J$$

where $\lambda$ is Rashba interaction magnitude and $J$ is p-wave Néel vector magnitude.

## 7. Parameter Dependencies

### Fermi Velocity ($v_F$)

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2

Fermi velocity appears in group velocity $v_\nu(k) = \nabla_k \epsilon_\nu(k)$. Higher $v_F$ increases the Edelstein effect magnitude through the transport lifetime term.

### Rashba Coupling ($\alpha_R$)

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 3

The susceptibility linearly increases with $\alpha$ (Rashba coupling parameter). Stronger coupling enhances spin-orbit interaction.

### Chirality

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2, Equation (3)

Chirality determines the handedness of the spin texture through the $\pm$ sign in:

$$\langle\vec{\sigma}\rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix}$$

**Source:** "Acoustic Rashba-Edelstein effect", Page 2, Equation (8)

Eigenenergies with chirality index $s = \pm$:

$$\epsilon_s = \frac{k^2}{2m} + s \alpha_R k_t$$

where $k_t = (k_x^2 + k_y^2)^{1/2}$.

### Electric Field Magnitude

**Source:** "Theory of the nonlinear Rashba-Edelstein effect" (arXiv:1506.08330), Page 1

The paper covers both linear and nonlinear regimes. Linear response for small fields, nonlinear effects at higher fields.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2

Linear response regime: $M \propto E$ at first order in electric field.

### Scattering Time ($\tau$)

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2

The transport lifetime $\tau$ appears directly in the magnetization formula. Typical order of magnitude in oxides: $\tau \sim 10^{-12}$ s.

### Anisotropy Parameters

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 4

For C$_{2v}$ symmetry with anisotropic effective masses and Rashba parameters:

- Mass anisotropy: $r_m = m_y/m_x \neq 1$
- Rashba anisotropy: $r_\alpha = \alpha_y/\alpha_x \neq 1$

When $r_m, r_\alpha > 1$, the susceptibility increases (boosted Edelstein effect).

## 8. Boltzmann Transport Equation Framework

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 2

Within Boltzmann framework, the stationary and homogeneous case:

$$\frac{\partial f}{\partial t} + \vec{v} \cdot \nabla_r f + \vec{F} \cdot \nabla_k f = \left(\frac{\partial f}{\partial t}\right)_{coll}$$

For the DEE calculation, the distribution function is perturbed by electric field:

$$f = f_0 + f^{(1)}$$

**Source:** "Out-of-plane spin polarization from in-plane electric and magnetic fields" (arXiv:cond-mat/0609078), Page 2, Equation (3)

Kinetic equation for $E = E\hat{x}$:

$$\frac{\partial \hat{\Phi}}{\partial t} + \sigma \cdot \left[b \times \Phi - \frac{n}{4v_\epsilon} b \times \frac{\partial b}{\partial k}\right] + \frac{eE}{(2\pi)^2} \frac{\partial f_0}{\partial \epsilon} \times \left[k_x + \frac{1}{2v_\epsilon} \frac{\partial}{\partial \phi}(b \cdot \sigma \sin \phi)\right] = \left(\frac{\partial \hat{\Phi}}{\partial t}\right)_{coll}$$

## 9. Magnetization Magnitude Calculation

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 3, Equation (10)

For Fermi energy around band crossing (small $E_F$):

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \left(\alpha m + \frac{1}{2} \frac{E_F}{\alpha}\right) [\hat{z} \times E]_y$$

**Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", Page 3, Equation (7)

Magnetoelectric susceptibility component:

$$\alpha^{ME}_{ix} = \frac{g \mu_B}{(2\pi)^2 W} \sum_{\pm} \int d\phi \frac{k v_x S_i(k)}{\left|\frac{\partial \epsilon}{\partial k}\right|}\bigg|_{k=k_\pm(\phi)}$$

## 10. Key Model Parameters Summary

| Parameter | Symbol | Physical Meaning | Effect on Edelstein Effect |
|-----------|--------|------------------|---------------------------|
| Rashba coupling | $\alpha$ or $\alpha_R$ | Spin-orbit coupling strength | Linear increase with $\alpha$ |
| Fermi velocity | $v_F$ | Velocity at Fermi surface | Higher $v_F$ increases magnitude |
| Effective mass | $m$ | Carrier effective mass | Appears in $k_0 = \alpha m$ |
| Scattering time | $\tau$ | Transport lifetime | Directly proportional |
| Fermi energy | $E_F$ or $\mu$ | Chemical potential | Different behavior in HDR vs LDR |
| Anisotropy ratio | $r_m, r_\alpha$ | Mass/SOC anisotropy | $>1$ boosts effect |
| Chirality | $\nu = \pm$ | Band helicity | Determines spin texture handedness |

## 11. Electric Field Direction Dependence

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", Page 1, Figure 1

The spin polarization direction follows:

$$\vec{M} \propto \hat{z} \times \vec{E}$$

- For $\vec{E} \parallel \hat{x}$: $\vec{M} \parallel \hat{y}$
- For $\vec{E} \parallel \hat{y}$: $\vec{M} \parallel -\hat{x}$

**Source:** "Out-of-plane spin polarization from in-plane electric and magnetic fields", Page 1

For combined electric and magnetic fields, out-of-plane spin polarization can be generated:

$$\Gamma_z = \frac{1}{2} \nu \alpha e E_x \tau \Delta_x \tilde{\gamma}_0$$

where $\Delta_x = g^* \mu_B B$ is Zeeman splitting.

## 12. Additional Considerations for Model Building

**Source:** "Acoustic Rashba-Edelstein effect", Page 3, Equation (14)

For acoustic/mechanical Edelstein effect (related mechanism):

$$\langle\hat{\sigma}_\alpha\rangle^k_{surf} = i\omega \alpha_R m \nu_0 \tilde{a}_2 \tau [\hat{z} \times u_{q,\omega}]_\alpha$$

**Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", Page 2, Equation (4)

At zero temperature:

$$M = \frac{e \tau g \mu_B}{(2\pi)^3} \int d^3k S(k) (E \cdot v) \delta(\epsilon_k - \mu)$$

where $S(k) = \langle\psi_k|\sigma|\psi_k\rangle$ is the spin expectation value.

**Source:** "Spin accumulation at nonmagnetic interface induced by direct Rashba Edelstein effect", Page 9

Spin polarization orientation for Rashba bands:

$$P_\pm(k) = \pm \frac{\alpha_R}{|\alpha_R|} \frac{(-k_y, k_x, 0)}{|k|}$$

Both orientation and spin accumulation depend on Rashba parameter $\alpha_R$ and sign of effective mass $m^*$.
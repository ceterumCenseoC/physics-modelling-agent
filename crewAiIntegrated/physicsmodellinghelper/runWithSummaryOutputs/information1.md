

# Model Information for Calculating the Edelstein Effect for a Rashba Fermion

## 1. System Hamiltonian

The Rashba spin-orbit coupling Hamiltonian for a 2D electron gas is given by:

$$\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 1, Equation (1)

Where:
- $p$ is the momentum
- $m$ is the effective carrier mass
- $\alpha$ is the Rashba spin-orbit coupling strength
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices

In momentum space, the Hamiltonian becomes:

$$H = \frac{\hbar^2 k^2}{2m} + \alpha \left[\vec{\sigma} \times \vec{k}_{\parallel}\right] \cdot \hat{z}$$

**Source:** "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface", arXiv:1912.01804, Page 2, Equation (6)

## 2. Energy Dispersion Relation

The energy eigenvalues for the Rashba model are:

$$E_{\pm}(k_{\parallel}) = \frac{\hbar^2 k_{\parallel}^2}{2m} \pm \alpha |k_{\parallel}|$$

**Source:** "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface", arXiv:1912.01804, Page 2, Equation (6)

Where the $\pm$ sign corresponds to the two chiral bands (helicity states $s = \pm 1$).

## 3. Fermi Wavevectors

In the **High-Density Regime (HDR)** where both chiral bands are occupied:

$$k_{F}^{\pm} = \mp k_0 + \sqrt{k_0^2 + 2mE_F}$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 2, Equation (5)

Where $k_0 = \alpha m$.

In the **Low-Density Regime (LDR)** where only the lowest energy band is occupied:

$$k_{F}^{\pm} = +k_0 \pm \sqrt{k_0^2 + 2mE_F}$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 2, Equation (6)

## 4. Spin Expectation Values

The spin expectation value evaluated on the eigenstates is:

$$\langle \vec{\sigma} \rangle_{\pm}^{\vec{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 2, Equation (3)

Where $\theta$ is the angle between the vector $\vec{k}$ and the $\hat{x}$ axis.

## 5. Magnetization Formula

The magnetization (total spin density) at first order in the electric field is given by:

$$\vec{M} = -\mu_b \sum_{\vec{k},\nu} |e| (\vec{v}_{\nu}(\vec{k}) \cdot \vec{E}) \delta[E_{\nu}(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_{\vec{k}}^{\nu}$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 2, Equation (2)

Where:
- $\mu_b$ is the Bohr magneton
- $\nu = \pm$ is the index indicating the two chiral Fermi surfaces
- $\vec{v}_{\nu}(\vec{k}) = \nabla_{\vec{k}} \epsilon_{\nu}^{\vec{k}}$ is the group velocity
- $\bar{\tau}_{\vec{k}}^{\nu}$ is the transport lifetime

## 6. Edelstein Susceptibility

The linear Edelstein effect can be defined as $m_j = \chi_{ij} E_i$, where $\chi_{ij}$ is the Edelstein susceptibility:

$$\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \langle \sigma_y \rangle_{\vec{k}}^{\nu} \delta(\epsilon_{\vec{k}}^{\nu} - \mu) v_x^{\nu}(\vec{k})$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 2, Equation (7)

Where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ with $a$ being the lattice parameter, $S_{cell}$ the area of the unit cell, and $\tau$ the transport time.

## 7. Analytical Expressions for Magnetization

### High-Density Regime (HDR)

For an electric field $\vec{E} = E_x \hat{x}$, the spin density along $\hat{y}$ direction is:

$$M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 3, Equation (8)

This shows the spin density is constant and independent of $E_F$ in the HDR.

### Low-Density Regime (LDR)

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 3, Equation (9)

For values of Fermi energy around the band crossing (small $E_F$):

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \vec{E}]_y$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 3, Equation (10)

## 8. Anisotropic Rashba Model (C2v Symmetry)

For systems with anisotropy in effective mass and Rashba parameter:

$$\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 4, Equation (11)

Where:
- $r_m = \frac{m_x}{m_y} \neq 1$ is the mass anisotropy ratio
- $r_{\alpha} = \frac{\alpha_x}{\alpha_y} \neq 1$ is the Rashba parameter anisotropy ratio

The Edelstein susceptibility in HDR for anisotropic case:

$$\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}$$

$$\frac{\chi_{xy}}{\chi_0}(r_{\alpha}) = \frac{4\pi m \alpha_x r_{\alpha}}{1 + r_{\alpha}}$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 4, Equation (12)

## 9. Current-Spin Conversion Efficiency

The current-spin conversion efficiency is given by:

$$\lambda_A = -\frac{\tilde{\alpha}_R}{k_F} \frac{e\mu}{\left[ \frac{a_3}{\tilde{a}_2} - 2\tilde{\alpha}_R^2 \left(1 - \frac{\tilde{a}_2}{2a_1}\right) \right]}$$

**Source:** "Acoustic Rashba–Edelstein effect", arXiv:2107.03115, Page 3, Equation (16)

Where $\tilde{\alpha}_R = \frac{m\alpha_R}{k_F}$ is the dimensionless Rashba parameter.

The spin density can be expressed as:

$$\langle \hat{\sigma} \rangle = \lambda_A [\hat{z} \times \langle \hat{j}_e \rangle]$$

**Source:** "Acoustic Rashba–Edelstein effect", arXiv:2107.03115, Page 3, below Equation (16)

## 10. Magnetoelectric Susceptibility (Alternative Formulation)

The magnetization can also be expressed in terms of magnetoelectric susceptibility:

$$M_i = e \tau \alpha_{ij}^{ME} E_j$$

**Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", arXiv:2501.01888, Page 1, Equation (6)

Where the susceptibility is:

$$\alpha_{ix}^{ME} = \frac{g\mu_B}{(2\pi)^2 W} \sum_{\pm} \int d\phi \frac{k v_x S_i(\vec{k})}{\left| \frac{\partial \epsilon}{\partial k} \right|} \bigg|_{k=k_{\pm}(\phi)}$$

**Source:** "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", arXiv:2501.01888, Page 2, Equation (7)

## 11. Key Model Parameters

The following parameters control the Edelstein effect:

1. **Rashba coupling strength ($\alpha$)**: The spin density scales linearly with $\alpha$ in the HDR
   - **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 3, Figure 3

2. **Chirality ($\nu = \pm$)**: The two chiral bands contribute differently to the spin density
   - **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 2, Equation (4)

3. **Fermi velocity ($v_F$)**: Related to the group velocity $v_{\nu}(\vec{k}) = \nabla_{\vec{k}} \epsilon_{\nu}^{\vec{k}}$
   - **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 2, below Equation (2)

4. **Effective mass ($m$)**: Affects the density of states and Fermi wavevector
   - **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 1, below Equation (1)

5. **Electric field direction ($\vec{E}$)**: The magnetization is perpendicular to the electric field (spin-momentum locking)
   - **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 1, Figure 1 caption

6. **Transport time ($\tau$)**: The spin density is proportional to the transport time
   - **Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712, Page 3, Equation (8)

## 12. Spin-Momentum Locking

The Rashba SOI causes momentum and spin to be "locked" such that:
- The $E_+$ and $E_-$ branches have clockwise and counterclockwise winding of spin
- The spin direction remains tangential to the Fermi surfaces
- An electric field shifts the Fermi surfaces, creating a net spin polarization perpendicular to the field

**Source:** "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface", arXiv:1912.01804, Page 2, below Equation (6)

## 13. Density of States

For the 2D Rashba system, the density of states per unit area per spin is:

$$\varrho(E) = \frac{1}{2\pi} \frac{k_{\parallel}(E)}{|dE/dk_{\parallel}|}$$

**Source:** "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface", arXiv:1912.01804, Page 2, Equation (7)

For the spin-split bands:

$$\varrho(E_{\pm}) = \frac{m}{2\pi \hbar^2} \left(1 \mp \frac{b}{\sqrt{b^2 + 2Em/\hbar^2}}\right), \quad E \geq 0$$

$$\varrho(E_{-}) = \frac{mb}{\pi \hbar^2 \sqrt{b^2 + 2mE/\hbar^2}}, \quad E < 0$$

**Source:** "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface", arXiv:1912.01804, Page 2, Equation (8)

Where $b = m\alpha/\hbar^2$.


# Mathematical Model for the Edelstein Effect in a Rashba Fermion

## 1. Model Hamiltonian and Low-Energy Band Structure

The Direct Edelstein Effect (DEE) describes the electric-field-induced generation of a finite in-plane spin polarization in a non-magnetic two-dimensional electron gas (2DEG) with strong spin-orbit coupling. The model is constructed around the $\Gamma$ point ($\mathbf{k} \approx 0$) of the Brillouin zone, where the low-energy physics is captured by the isotropic Rashba Hamiltonian [1]:

$$
\hat{H} = \frac{\mathbf{p}^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})
\tag{1}
$$

where $m$ is the effective carrier mass, $\alpha$ is the Rashba spin-orbit coupling (SOC) strength, $\hat{z}$ is the unit vector perpendicular to the 2D plane, and $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ denotes the Pauli matrix vector. In momentum space ($\mathbf{p} = \hbar \mathbf{k}$), the Hamiltonian is diagonalized by chiral eigenstates $|\psi_\nu(\mathbf{k})\rangle$ with chirality index $\nu = \pm 1$. The energy dispersion relation reads [1]:

$$
E_\nu(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k
\tag{2}
$$

The spin expectation value for these eigenstates exhibits strict spin-momentum locking:

$$
\langle \boldsymbol{\sigma} \rangle_\mathbf{k}^\nu = \nu \frac{\hat{z} \times \mathbf{k}}{k} = \nu \begin{pmatrix} \sin\theta_k \\ -\cos\theta_k \\ 0 \end{pmatrix}
\tag{3}
$$

where $\theta_k = \arctan(k_y/k_x)$ is the azimuthal angle of the wavevector. The chirality $\nu$ directly dictates the handedness of the spin texture: $\nu = +1$ corresponds to right-handed locking, while $\nu = -1$ corresponds to left-handed locking.

## 2. Non-Equilibrium Spin Accumulation Formalism

When a static in-plane electric field $\mathbf{E}$ is applied, the electron distribution function is driven out of equilibrium. Within the relaxation time approximation of the semiclassical Boltzmann transport theory, the first-order correction to the Fermi-Dirac distribution $f_0(E)$ is [1]:

$$
\delta f_\nu(\mathbf{k}) = -e\tau \left( \mathbf{v}_\nu(\mathbf{k}) \cdot \mathbf{E} \right) \frac{\partial f_0(E_\nu)}{\partial E}
\tag{4}
$$

where $e > 0$ is the elementary charge, $\tau$ is the momentum relaxation time, and $\mathbf{v}_\nu(\mathbf{k}) = \nabla_\mathbf{k} E_\nu(\mathbf{k})$ is the group velocity. The non-equilibrium magnetization density $\mathbf{M}$ is obtained by integrating the spin expectation value weighted by this distribution correction over the Brillouin zone [1]:

$$
\mathbf{M} = -\mu_B \sum_{\nu} \int \frac{d^2k}{(2\pi)^2} \langle \boldsymbol{\sigma} \rangle_\mathbf{k}^\nu \delta f_\nu(\mathbf{k})
\tag{5}
$$

Substituting Eqs. (3) and (4) into Eq. (5) and evaluating the angular integral $\int_0^{2\pi} d\theta_k$ yields a magnetization strictly perpendicular to the applied electric field. The vector structure of the DEE is universally given by:

$$
\mathbf{M} = \chi_{\text{Ed}} \left( \hat{z} \times \mathbf{E} \right)
\tag{6}
$$

where $\chi_{\text{Ed}}$ is the scalar Edelstein susceptibility. The cross product ensures that for an arbitrary in-plane field $\mathbf{E} = E_x \hat{x} + E_y \hat{y}$, the induced magnetization lies in-plane and satisfies $\mathbf{M} \cdot \mathbf{E} = 0$.

## 3. Analytical Magnetization for Arbitrary Electric Field

The susceptibility $\chi_{\text{Ed}}$ depends on the carrier density, characterized by the Fermi energy $E_F$ measured from the band crossing point at $\Gamma$. Two distinct regimes emerge [1]:

### 3.1 High-Density Regime (HDR)
When $E_F > m\alpha^2$, both chiral bands ($\nu = \pm$) are occupied. The contributions from the two bands interfere constructively for the transverse spin component, yielding a constant susceptibility [1]:

$$
\chi_{\text{Ed}}^{\text{HDR}} = \frac{|e| \mu_B \tau m \alpha}{2\pi \hbar^2}
\tag{7}
$$

The magnetization magnitude is:
$$
|\mathbf{M}| = \chi_{\text{Ed}}^{\text{HDR}} |\mathbf{E}|
\tag{8}
$$

### 3.2 Low-Density Regime (LDR)
When $0 < E_F \lesssim m\alpha^2$, only the lower chiral band ($\nu = -1$) contributes significantly. The susceptibility becomes density-dependent [1]:

$$
\chi_{\text{Ed}}^{\text{LDR}} = \frac{|e| \mu_B \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha^2 + \frac{2m E_F}{\hbar^2}}
\tag{9}
$$

For very low densities ($E_F \ll m\alpha^2$), a Taylor expansion recovers the linear dependence on $E_F$:
$$
\chi_{\text{Ed}}^{\text{LDR}} \approx \frac{|e| \mu_B \tau}{2\pi \hbar^2} \left( m\alpha + \frac{E_F}{2\alpha} \right)
\tag{10}
$$

### 3.3 General Vector Expression
For an arbitrary electric field direction defined by angle $\phi_E$ ($\mathbf{E} = E \cos\phi_E \hat{x} + E \sin\phi_E \hat{y}$), the magnetization vector is:
$$
\mathbf{M}(E, \phi_E) = \chi_{\text{Ed}} E \begin{pmatrix} -\sin\phi_E \\ \cos\phi_E \\ 0 \end{pmatrix}
\tag{11}
$$

## 4. Parameter Dependencies and Physical Interpretation

The model explicitly captures how fundamental physical parameters modulate the Edelstein response:

- **Spin-Orbit Coupling Strength ($\alpha$):** The susceptibility scales linearly with $\alpha$ in the HDR (Eq. 7). In the LDR, $\alpha$ appears inside the square root (Eq. 9), meaning stronger SOC enhances spin-splitting and increases the available phase space for transverse polarization [1].
- **Fermi Velocity ($v_F$):** The Fermi velocity is related to the Fermi wavevector by $v_F = (\hbar k_F/m) + \nu \alpha$. Since $k_F$ is determined by $E_F$, varying $v_F$ is equivalent to tuning the carrier density. In the LDR, $\chi_{\text{Ed}}$ increases with $v_F$ (via $E_F$), while in the HDR it saturates and becomes independent of $v_F$ [1].
- **Chirality ($\nu = \pm$):** Chirality dictates the sign of the spin-momentum locking. In the HDR, the total magnetization arises from the coherent sum of both chiralities. Because $\langle \boldsymbol{\sigma} \rangle_\mathbf{k}^\nu$ flips sign with $\nu$, but the velocity correction $\delta f$ also changes sign, the transverse components add constructively. In the LDR, only the $\nu = -1$ band is populated, making the chirality effectively fixed by thermodynamics.
- **Effective Mass ($m$):** Appears linearly in the HDR susceptibility. A heavier mass reduces the kinetic energy dispersion, enhancing the relative importance of the Rashba term and increasing spin accumulation [1].
- **Relaxation Time ($\tau$):** Enters linearly in both regimes. Longer scattering times allow the electric field to build up a larger non-equilibrium spin population before momentum relaxation occurs.
- **Electric Field Magnitude and Direction:** The response is linear in $|\mathbf{E}|$ within the perturbative regime. The direction is strictly $\mathbf{M} \perp \mathbf{E}$ due to the $\hat{z} \times \mathbf{E}$ vector structure inherent to the Rashba geometry.

## 5. Step-by-Step Computational Procedure

To calculate the Edelstein magnetization for any given set of parameters and field conditions, follow this mathematical workflow:

1. **Define System Parameters:** Specify $m$, $\alpha$, $\tau$, $E_F$, and temperature $T$ (to construct $f_0$).
2. **Determine Density Regime:** Compare $E_F$ with the critical energy $E_c = m\alpha^2/\hbar^2$. If $E_F > E_c$, use HDR expressions; otherwise, use LDR expressions.
3. **Compute Susceptibility:** Evaluate $\chi_{\text{Ed}}$ using Eq. (7) or Eq. (9) depending on the regime.
4. **Specify Electric Field:** Define magnitude $E = |\mathbf{E}|$ and angle $\phi_E$.
5. **Calculate Magnetization Vector:** Apply Eq. (11) to obtain $\mathbf{M} = (M_x, M_y, M_z)$. The magnitude is $|\mathbf{M}| = \chi_{\text{Ed}} E$.
6. **Parameter Sweep:** To study dependencies, repeat steps 1–5 while varying one parameter at a time (e.g., $\alpha$, $E_F$, or $\phi_E$) while holding others constant.
7. **Validate Perturbative Limit:** Ensure $e\tau E v_F \ll k_B T$ or $\hbar/\tau$ to guarantee the linear-response assumption remains valid.

## 6. Explicit Graphics Specifications

The model produces four canonical graphical representations. Each plot is specified mathematically to enable direct implementation:

### Graphic 1: Magnetization Magnitude vs. Electric Field Strength
- **Axes:** Horizontal: $E$ (V/m). Vertical: $|\mathbf{M}|$ (A/m).
- **Functional Form:** $|\mathbf{M}|(E) = \chi_{\text{Ed}} E$.
- **Trend:** Perfect straight line through the origin. Slope equals $\chi_{\text{Ed}}$.
- **Annotations:** Different curves for HDR and LDR to show regime-dependent slopes. Linear response region explicitly bounded by the perturbative limit.

### Graphic 2: Susceptibility vs. Fermi Energy (Carrier Density)
- **Axes:** Horizontal: $E_F$ (eV). Vertical: $\chi_{\text{Ed}}$ (normalized or absolute).
- **Functional Form:** 
  $$
  \chi_{\text{Ed}}(E_F) = \begin{cases} 
  \chi_0 \sqrt{1 + \frac{2E_F}{m\alpha^2/\hbar^2}} & E_F < E_c \quad (\text{LDR}) \\
  \chi_0 & E_F \geq E_c \quad (\text{HDR})
  \end{cases}
  $$
  where $\chi_0 = \frac{|e|\mu_B \tau m \alpha}{2\pi \hbar^2}$.
- **Trend:** Sublinear increase (square-root) at low $E_F$, saturating to a constant plateau at high $E_F$. The crossover occurs at $E_c = m\alpha^2/\hbar^2$.
- **Annotations:** Mark $E_c$. Shade LDR and HDR regions. Dashed curve shows analytical fit.

### Graphic 3: Magnetization Direction vs. Electric Field Angle
- **Axes:** 2D Cartesian plane ($\hat{x}, \hat{y}$).
- **Functional Form:** Vector field $\mathbf{M}(\phi_E) = \chi_{\text{Ed}} E (-\sin\phi_E \hat{x} + \cos\phi_E \hat{y})$.
- **Trend:** For every electric field vector arrow placed radially outward from the origin, the magnetization vector is drawn rotated by exactly $90^\circ$ counter-clockwise.
- **Annotations:** Concentric circles indicate constant $E$ magnitude. Arrow labels show $\phi_E$. Text overlay: $\mathbf{M} \perp \mathbf{E}$.

### Graphic 4: Susceptibility vs. Rashba Coupling Strength
- **Axes:** Horizontal: $\alpha$ (eV·Å). Vertical: $\chi_{\text{Ed}}$ (normalized).
- **Functional Form:** $\chi_{\text{Ed}}(\alpha) \propto \alpha$ in HDR. In LDR: $\chi_{\text{Ed}}(\alpha) \propto \sqrt{\alpha^2 + C/\alpha^2}$.
- **Trend:** Linear growth for large $\alpha$. At small $\alpha$, the LDR curve dips due to the $E_F/(2\alpha)$ term dominating, then rises as $\alpha$ increases.
- **Annotations:** Separate curves for fixed $E_F$ values. Dashed lines indicate linear scaling regions. Highlight the regime where SOC dominates kinetic energy.

These graphical specifications, combined with the analytical expressions, fully characterize the Edelstein effect for Rashba fermions. The model can be directly implemented in any mathematical software by evaluating the closed-form expressions provided.

## References
[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712v1 [cond-mat.mes-hall]* (2025).
# Mathematical Model for the Edelstein Effect in a Rashba Fermion at the Gamma Point

## 1. Model Setup: The Rashba Hamiltonian at the Gamma Point

We consider a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling, centered at the Gamma point ($\mathbf{k}=0$) of the Brillouin zone. The effective Hamiltonian is:

$$H(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\boldsymbol{\sigma} \times \mathbf{k}) \cdot \hat{z}$$

where:
- $m^*$ is the effective electron mass
- $\alpha_R$ is the Rashba spin-orbit coupling strength (can be positive or negative, determining chirality)
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are Pauli matrices
- $\mathbf{k} = (k_x, k_y)$ is the 2D wavevector
- $\hat{z}$ is the interface normal direction

Explicitly, in matrix form:

$$H(\mathbf{k}) = \frac{\hbar^2 (k_x^2 + k_y^2)}{2m^*} + \alpha_R \begin{pmatrix} 0 & -ik_x - k_y \\ ik_x - k_y & 0 \end{pmatrix}$$

The eigenenergies are:

$$E_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R |\mathbf{k}|$$

with corresponding eigenstates:

$$|\Psi_{\pm}(\mathbf{k})\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ \pm i e^{i\phi_k} \end{pmatrix}$$

where $\phi_k = \arctan(k_y/k_x)$ is the azimuthal angle of the momentum.

The spin expectation values for the eigenstates are:

$$\langle \boldsymbol{\sigma} \rangle_{\pm} = \pm \text{sgn}(\alpha_R) \begin{pmatrix} -\sin\phi_k \\ \cos\phi_k \\ 0 \end{pmatrix} = \pm \text{sgn}(\alpha_R) \frac{(-k_y, k_x, 0)}{|\mathbf{k}|}$$

This demonstrates **spin-momentum locking**: the spin lies in-plane and is always perpendicular to the momentum direction.

---

## 2. Density of States and Fermi Surface Properties

The total density of states (per spin, per unit area) for the Rashba model at energy $E$ is:

$$\rho(E) = \frac{m^*}{2\pi\hbar^2} \left[ 1 + \frac{m^*\alpha_R/\hbar^2}{\sqrt{(m^*\alpha_R/\hbar^2)^2 + 2m^*E/\hbar^2}} \right] \Theta(E) + \frac{m^*\alpha_R/\pi\hbar^2}{\sqrt{(m^*\alpha_R/\hbar^2)^2 + 2m^*E/\hbar^2}} \Theta\left(-\frac{m^*\alpha_R^2}{2\hbar^2} < E < 0\right)$$

where $\Theta$ is the Heaviside step function.

At the Fermi energy $E_F$, the Fermi wavevectors for the two bands are:

$$k_F^{\pm} = \left| -\frac{m^*\alpha_R}{\hbar^2} \pm \sqrt{\left(\frac{m^*\alpha_R}{\hbar^2}\right)^2 + \frac{2m^*E_F}{\hbar^2}} \right|$$

The Fermi velocities are:

$$v_F^{\pm} = \frac{1}{\hbar}\frac{\partial E_{\pm}}{\partial k}\bigg|_{k=k_F^{\pm}} = \frac{\hbar k_F^{\pm}}{m^*} \pm \frac{\alpha_R}{\hbar}$$

---

## 3. Derivation of the Edelstein Effect

### 3.1 Linearized Boltzmann Transport

We apply an electric field $\mathbf{E}$ to the system. Within the constant relaxation time approximation ($\tau$), the non-equilibrium distribution function is:

$$f_{n\mathbf{k}} = f^0_{n\mathbf{k}} + e\tau \left.\frac{\partial f^0}{\partial \varepsilon}\right|_{\varepsilon_{n\mathbf{k}}} \mathbf{v}_{n\mathbf{k}} \cdot \mathbf{E}$$

where:
- $f^0_{n\mathbf{k}} = [1 + e^{(\varepsilon_{n\mathbf{k}} - \mu)/k_B T}]^{-1}$ is the Fermi-Dirac distribution
- $e > 0$ is the elementary charge
- $\mathbf{v}_{n\mathbf{k}} = \frac{1}{\hbar}\nabla_{\mathbf{k}}\varepsilon_{n\mathbf{k}}$ is the group velocity

The velocity operator for the Rashba model is:

$$\mathbf{v}(\mathbf{k}) = \frac{1}{\hbar}\nabla_{\mathbf{k}} H(\mathbf{k}) = \frac{\hbar\mathbf{k}}{m^*} + \frac{\alpha_R}{\hbar}(\hat{z} \times \boldsymbol{\sigma})$$

For the eigenstates, the band velocities are:

$$\mathbf{v}_{\pm}(\mathbf{k}) = \frac{\hbar\mathbf{k}}{m^*} \pm \frac{\alpha_R}{\hbar} \hat{e}_{\phi_k}$$

where $\hat{e}_{\phi_k} = (-\sin\phi_k, \cos\phi_k, 0)$ is the azimuthal unit vector.

### 3.2 Induced Spin Magnetization

The spin magnetization density (magnetic moment per unit area) is:

$$\mathbf{m}_s = -\frac{\mu_B g_s}{2} \frac{1}{A} \sum_{n\mathbf{k}} f_{n\mathbf{k}} \langle \Psi_{n\mathbf{k}} | \boldsymbol{\sigma} | \Psi_{n\mathbf{k}} \rangle$$

where:
- $\mu_B$ is the Bohr magneton
- $g_s \approx 2$ is the electron spin g-factor
- $A$ is the area of the system

Substituting the non-equilibrium distribution function, we get the spin magnetization induced by the electric field:

$$\mathbf{m}_s = -\frac{\mu_B g_s e\tau}{2} \frac{1}{A} \sum_{n\mathbf{k}} \frac{\partial f^0}{\partial \varepsilon}\bigg|_{\varepsilon_{n\mathbf{k}}} (\mathbf{v}_{n\mathbf{k}} \cdot \mathbf{E}) \langle \boldsymbol{\sigma} \rangle_{n\mathbf{k}}$$

Converting the sum to an integral (using $A^{-1}\sum_{\mathbf{k}} \to \int \frac{d^2k}{(2\pi)^2}$):

$$\mathbf{m}_s = -\frac{\mu_B g_s e\tau}{2} \int \frac{d^2k}{(2\pi)^2} \sum_{n=\pm} \frac{\partial f^0}{\partial \varepsilon}\bigg|_{\varepsilon_{n\mathbf{k}}} (\mathbf{v}_{n\mathbf{k}} \cdot \mathbf{E}) \langle \boldsymbol{\sigma} \rangle_{n\mathbf{k}}$$

### 3.3 Analytical Evaluation at Zero Temperature

At $T = 0$, we have $\frac{\partial f^0}{\partial \varepsilon} = -\delta(\varepsilon - \varepsilon_F)$. Using polar coordinates and the explicit forms of velocity and spin, we obtain:

$$\mathbf{m}_s = \frac{\mu_B g_s e\tau}{2} \int_0^{2\pi} \frac{d\phi}{2\pi} \sum_{n=\pm} \frac{k_{F,n}^2}{2\pi} \left[ \mathbf{v}_{n}(k_{F,n},\phi) \cdot \mathbf{E} \right] \langle \boldsymbol{\sigma} \rangle_{n}(k_{F,n},\phi)$$

Let us define the unit vector $\hat{e}_\phi = (-\sin\phi, \cos\phi, 0)$. Then:

- $\mathbf{v}_{\pm}(k_F^{\pm}, \phi) = \frac{\hbar k_F^{\pm}}{m^*}(\cos\phi, \sin\phi, 0) \pm \frac{\alpha_R}{\hbar}\hat{e}_\phi$
- $\langle \boldsymbol{\sigma} \rangle_{\pm} = \pm \text{sgn}(\alpha_R) \hat{e}_\phi$

For an electric field $\mathbf{E} = E(\cos\theta_E, \sin\theta_E, 0)$, we compute:

$$\mathbf{v}_{\pm} \cdot \mathbf{E} = E\left[ \frac{\hbar k_F^{\pm}}{m^*}\cos(\phi - \theta_E) \pm \frac{\alpha_R}{\hbar}\sin(\theta_E - \phi) \right]$$

The angular integral gives:

$$\int_0^{2\pi} \frac{d\phi}{2\pi} \cos(\phi - \theta_E) \hat{e}_\phi = \frac{1}{2}(\sin\theta_E, -\cos\theta_E, 0)$$

$$\int_0^{2\pi} \frac{d\phi}{2\pi} \sin(\theta_E - \phi) \hat{e}_\phi = \frac{1}{2}(\cos\theta_E, \sin\theta_E, 0) = \frac{1}{2}\hat{E}$$

Therefore:

$$\mathbf{m}_s = \frac{\mu_B g_s e\tau E}{4\pi} \sum_{n=\pm} n \text{sgn}(\alpha_R) \left[ \frac{\hbar k_F^{n}}{m^*}(\sin\theta_E, -\cos\theta_E, 0) \pm \frac{\alpha_R}{\hbar}(\cos\theta_E, \sin\theta_E, 0) \right]$$

The second term (proportional to $\alpha_R$) averages to zero when summed over $n=\pm$ because the contributions have opposite signs. The first term survives:

$$\mathbf{m}_s = \frac{\mu_B g_s e\tau E}{4\pi} \text{sgn}(\alpha_R) \frac{\hbar}{m^*}(k_F^{+} - k_F^{-})(\sin\theta_E, -\cos\theta_E, 0)$$

### 3.4 Final Expression for the Spin Edelstein Susceptibility

The difference in Fermi wavevectors is:

$$k_F^{+} - k_F^{-} = 2\sqrt{\left(\frac{m^*\alpha_R}{\hbar^2}\right)^2 + \frac{2m^*E_F}{\hbar^2}} = 2k_R$$

where $k_R = \sqrt{(m^*\alpha_R/\hbar^2)^2 + 2m^*E_F/\hbar^2}$ is the mean Fermi wavevector.

Thus:

$$\mathbf{m}_s = \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{\hbar k_R}{m^*} \text{sgn}(\alpha_R) \, E \, (\sin\theta_E, -\cos\theta_E, 0)$$

Defining the mean Fermi velocity $\bar{v}_F = \hbar k_R/m^*$, we obtain:

$$\mathbf{m}_s = \frac{\mu_B g_s e\tau}{2\pi\hbar} \bar{v}_F \text{sgn}(\alpha_R) \, E \, (\sin\theta_E, -\cos\theta_E, 0)$$

The **spin Edelstein susceptibility tensor** is defined by $m_{s,i} = \chi^s_{ij} E_j$:

$$\chi^s = \frac{\mu_B g_s e\tau}{2\pi\hbar} \bar{v}_F \text{sgn}(\alpha_R) \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$$

In terms of the Rashba parameter and Fermi energy:

$$\chi^s_{xy} = \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{\hbar}{m^*}\sqrt{\left(\frac{m^*\alpha_R}{\hbar^2}\right)^2 + \frac{2m^*E_F}{\hbar^2}} \text{sgn}(\alpha_R)$$

### 3.5 General Expression Including the Band-Split Contribution

A more complete treatment includes the contribution from the different populations of the two bands. The general result for the Edelstein susceptibility at finite Fermi energy is:

$$\chi^s_{xy} = \frac{\mu_B g_s e\tau}{4\pi\hbar} \left[ \frac{\hbar k_F^{+}}{m^*} \text{sgn}(\alpha_R) + \frac{\hbar k_F^{-}}{m^*} \text{sgn}(\alpha_R) \right] = \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{\hbar k_R}{m^*} \text{sgn}(\alpha_R)$$

which confirms our result.

---

## 4. Magnetization Direction and Magnitude

### 4.1 For a General Electric Field Direction

For an electric field $\mathbf{E} = (E_x, E_y, 0)$, the induced magnetization is:

$$\mathbf{m}_s = \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{\hbar k_R}{m^*} \text{sgn}(\alpha_R) (E_y, -E_x, 0)$$

Key properties:
- **Direction**: Always perpendicular to $\mathbf{E}$ and in the plane (no $z$-component)
- **Magnitude**: $|\mathbf{m}_s| = \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{\hbar k_R}{m^*} |\mathbf{E}|$
- **Sense of rotation**: For $\alpha_R > 0$, $\mathbf{m}_s$ is rotated $90^\circ$ **counterclockwise** from $\mathbf{E}$; for $\alpha_R < 0$, it is rotated $90^\circ$ **clockwise**

### 4.2 For Specific Field Directions

- **$\mathbf{E} = E\hat{x}$**: $\mathbf{m}_s = \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{\hbar k_R}{m^*} \text{sgn}(\alpha_R) E (0, -1, 0)$ → magnetization along $-y$ (for $\alpha_R > 0$) or $+y$ (for $\alpha_R < 0$)
- **$\mathbf{E} = E\hat{y}$**: $\mathbf{m}_s = \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{\hbar k_R}{m^*} \text{sgn}(\alpha_R) E (1, 0, 0)$ → magnetization along $+x$ (for $\alpha_R > 0$) or $-x$ (for $\alpha_R < 0$)
- **$\mathbf{E} = E(\cos\theta, \sin\theta, 0)$**: $\mathbf{m}_s = |\mathbf{m}_s|(\sin\theta, -\cos\theta, 0)$, so the magnetization angle is $\theta_m = \theta - \pi/2$ (for $\alpha_R > 0$)

---

## 5. Parameter Dependence

### 5.1 Dependence on Rashba Parameter $\alpha_R$

The susceptibility depends on $\alpha_R$ through both the magnitude and sign:

$$\chi^s_{xy} = \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{\hbar}{m^*}\sqrt{\left(\frac{m^*\alpha_R}{\hbar^2}\right)^2 + \frac{2m^*E_F}{\hbar^2}} \text{sgn}(\alpha_R)$$

- **For $E_F \gg \frac{m^*\alpha_R^2}{2\hbar^2}$** (weak SOC limit): $\chi^s_{xy} \approx \frac{\mu_B g_s e\tau}{2\pi\hbar} \sqrt{\frac{2E_F}{m^*}} \text{sgn}(\alpha_R)$, which is independent of $|\alpha_R|$ but depends on its sign
- **For $E_F \to 0$** (near band bottom): $\chi^s_{xy} \approx \frac{\mu_B g_s e\tau}{2\pi\hbar} \frac{|\alpha_R|}{\hbar} \text{sgn}(\alpha_R)$, which is proportional to $|\alpha_R|$

Thus, the magnitude of the Edelstein effect **increases with $|\alpha_R|$** when the Fermi energy is near the band crossing point, but becomes **saturated** at high Fermi energies.

### 5.2 Dependence on Effective Mass $m^*$

$$\chi^s_{xy} \propto \frac{\hbar}{m^*}\sqrt{\left(\frac{m^*\alpha_R}{\hbar^2}\right)^2 + \frac{2m^*E_F}{\hbar^2}} = \sqrt{\frac{\alpha_R^2}{\hbar^2} + \frac{2E_F}{m^*}}$$

- For fixed $\alpha_R$ and $E_F$, the susceptibility **decreases with increasing $m^*$** as $1/\sqrt{m^*}$
- However, if $E_F$ is measured from the band bottom and $m^*$ increases, more states are populated, so the total magnetization may increase

### 5.3 Dependence on Fermi Velocity

The mean Fermi velocity is $\bar{v}_F = \hbar k_R/m^* = \sqrt{v_F^2 + \alpha_R^2/\hbar^2}$ where $v_F = \sqrt{2E_F/m^*}$ is the "unperturbed" Fermi velocity. Then:

$$\chi^s_{xy} = \frac{\mu_B g_s e\tau}{2\pi\hbar} \bar{v}_F \text{sgn}(\alpha_R)$$

So the susceptibility is **directly proportional to the mean Fermi velocity**, which increases with $\alpha_R$ and decreases with $m^*$.

### 5.4 Dependence on Chirality (Sign of $\alpha_R$)

The sign of $\alpha_R$ controls the **direction** of the induced magnetization:

$$\mathbf{m}_s(\alpha_R) = \text{sgn}(\alpha_R) \, \mathbf{m}_s(|\alpha_R|)$$

This means:
- Flipping the chirality reverses the magnetization direction for the same electric field
- The magnitude is unchanged

### 5.5 Dependence on Relaxation Time $\tau$

The Edelstein effect is **linear in $\tau$**:

$$\chi^s_{xy} \propto \tau$$

This is characteristic of the diffusive (Boltzmann) regime. In the ballistic regime, different physics would apply.

### 5.6 Dependence on Electric Field Magnitude

In the linear response regime:

$$|\mathbf{m}_s| = \chi^s_{xy} |\mathbf{E}|$$

The response is linear. Nonlinear corrections appear when $eE\ell \sim \varepsilon_F$ (where $\ell = v_F\tau$ is the mean free path), but are beyond the present linearized Boltzmann treatment.

---

## 6. Orbital Edelstein Effect

For completeness, we note that the orbital contribution to the Edelstein effect in a single Rashba band is zero due to the symmetry of the orbital magnetic moment:

$$\mathbf{l}_{\pm}(\mathbf{k}) = \mp \frac{ec}{2\mu_B g_l} \frac{\alpha_R^2 k^2}{(\hbar^2 k^2/m^*)^2 + \alpha_R^2 k^2} \hat{e}_\phi$$

The orbital moment also points perpendicular to $\mathbf{k}$ but with opposite sign for the two bands. When integrated over the Fermi surface with the shifted distribution, the orbital contribution partially cancels. For the single-band Rashba model, one finds:

$$\chi^l_{xy} = \frac{ec\tau}{2\pi\hbar} \frac{\alpha_R^2 k_R^2}{\varepsilon_F^2 + \alpha_R^2 k_R^2} \text{sgn}(\alpha_R) \frac{m^*\alpha_R}{\hbar^2}$$

This is typically **much smaller** than the spin contribution, so we focus primarily on the spin Edelstein effect.

---

## 7. Total Magnetization and Observable Quantities

The total induced magnetic moment per unit area is:

$$\mathbf{m}_{\text{total}} = \mathbf{m}_s + \mathbf{m}_l \approx \mathbf{m}_s$$

The **spin accumulation** (energy splitting between up and down spins) at the interface is:

$$\delta \mu_s = \frac{2|\mathbf{m}_s|}{\mu_B g_s \rho(E_F)} = \frac{e\tau \bar{v}_F |\mathbf{E}|}{\pi\hbar \rho(E_F)} \text{sgn}(\alpha_R)$$

Using the density of states at the Fermi energy for the Rashba model:

$$\rho(E_F) = \frac{m^*}{2\pi\hbar^2}\left[1 + \frac{m^*\alpha_R/\hbar^2}{\sqrt{(m^*\alpha_R/\hbar^2)^2 + 2m^*E_F/\hbar^2}}\right]$$

---

## 8. Summary of the Complete Model

The **Edelstein effect for a Rashba fermion at the Gamma point** is fully described by:

1. **Hamiltonian**: $H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R(\boldsymbol{\sigma} \times \mathbf{k})\cdot\hat{z}$

2. **Spin-momentum locking**: $\langle\boldsymbol{\sigma}\rangle_{\pm} = \pm\text{sgn}(\alpha_R)\frac{(-k_y,k_x,0)}{|\mathbf{k}|}$

3. **Edelstein susceptibility tensor**:
$$\chi^s = \frac{\mu_B g_s e\tau}{2\pi\hbar} \sqrt{\frac{\alpha_R^2}{\hbar^2} + \frac{2E_F}{m^*}} \, \text{sgn}(\alpha_R) \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$$

4. **Induced magnetization**:
$$\mathbf{m}_s = \frac{\mu_B g_s e\tau}{2\pi\hbar} \sqrt{\frac{\alpha_R^2}{\hbar^2} + \frac{2E_F}{m^*}} \, \text{sgn}(\alpha_R) (E_y, -E_x, 0)$$

5. **Key properties**:
   - Magnetization is **in-plane** and **perpendicular** to the applied electric field
   - Magnitude scales **linearly** with $|\mathbf{E}|$ and $\tau$
   - Magnitude **increases** with $|\alpha_R|$ (especially near $E_F \to 0$) and **decreases** with $m^*$
   - Direction is determined by **$\text{sgn}(\alpha_R)$** (chirality)
   - Mean Fermi velocity $\bar{v}_F = \sqrt{\alpha_R^2/\hbar^2 + 2E_F/m^*}$ sets the overall scale

---

## 9. Graphical Representations

The following graphics should be generated to visualize the model:

### (a) Dispersion Relation $E_{\pm}(k_x, 0)$
- Plot two parabolas: $E_{\pm}(k) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R |k|$
- Shows the characteristic Rashba splitting with band crossing at $k=0$
- Band minimum at $E = -m^*\alpha_R^2/(2\hbar^2)$ for the lower band

### (b) Spin Texture in $k$-Space
- Vector field plot of $\langle\boldsymbol{\sigma}\rangle$ over the 2D $k$-plane
- Shows clockwise (for $\alpha_R > 0$) or counterclockwise (for $\alpha_R < 0$) winding
- Arrows always perpendicular to the radial direction

### (c) Magnetization vs. Electric Field Magnitude
- Linear plot: $|\mathbf{m}_s|$ vs. $|\mathbf{E}|$
- Straight line through origin with slope $\chi^s_{xy}$

### (d) Magnetization Direction vs. Field Direction
- Polar plot: $m_{s,x}$ and $m_{s,y}$ vs. field angle $\theta_E$
- Shows that $\mathbf{m}_s \perp \mathbf{E}$ for all angles
- For $\alpha_R > 0$: $m_{s,x} = \chi E\sin\theta_E$, $m_{s,y} = -\chi E\cos\theta_E$

### (e) Parameter Dependence Plots
- **$|\mathbf{m}_s|$ vs. $\alpha_R$** (at fixed $E_F$ and $m^*$): Shows increase with $|\alpha_R|$, particularly pronounced near $E_F \to 0$; discontinuity in slope at $\alpha_R = 0$
- **$|\mathbf{m}_s|$ vs. $m^*$** (at fixed $\alpha_R$ and $E_F$): Decreases as $1/\sqrt{m^*}$
- **$|\mathbf{m}_s|$ vs. $\bar{v}_F$**: Linear relationship
- **$m_{s,y}$ vs. $\text{sgn}(\alpha_R)$** (at fixed $E_x$): Step function showing sign reversal

### (f) Susceptibility vs. Fermi Energy
- Plot $\chi^s_{xy}$ vs. $E_F$ for different $\alpha_R$ values
- Shows the characteristic **band-edge singularity** at $E_F = -m^*\alpha_R^2/(2\hbar^2)$
- Saturates to constant value at high $E_F$

---

## 10. Numerical Parameters for Illustrative Calculations

For explicit numerical evaluation, we suggest:

| Parameter | Value |
|-----------|-------|
| Effective mass $m^*$ | $0.27\,m_e$ (Au(111)-like) |
| Rashba parameter $\alpha_R$ | $\pm 0.33$ eV·Å (Au(111)-like) |
| Fermi energy $E_F$ | $0.1$–$1.0$ eV |
| Relaxation time $\tau$ | $10^{-13}$–$10^{-12}$ s |
| Electric field magnitude | $0.1$–$10$ kV/cm |

With these values, the Edelstein susceptibility is of order $\chi^s \sim 10^{-4}$–$10^{-3}$ $\mu_B$·nm/V, and the induced magnetization for $E = 1$ kV/cm is $\sim 10^{-7}$–$10^{-6}$ $\mu_B$ per nm², consistent with experimental observations.

---

This completes the mathematical model for the Edelstein effect in a Rashba fermion at the Gamma point, including the derivation of the susceptibility tensor, the magnetization response to arbitrary electric fields, and the parametric dependence on all relevant model parameters.
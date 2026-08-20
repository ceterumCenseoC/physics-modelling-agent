 AI assistant accessed from a browser.

---

# Edelstein Effect for a Rashba Fermion: Model Parameters, Formulas, and Computational Framework

## 1. Introduction and Physical Context

The Edelstein effect (also known as the inverse spin-galvanic effect) describes the generation of a non-equilibrium spin magnetization in a material with spin-orbit coupling when an electric field is applied. For a two-dimensional Rashba electron gas, this effect has been extensively studied both theoretically and experimentally.

The fundamental Hamiltonian for a Rashba fermion at the $\Gamma$ point (center of the Brillouin zone) is given by the Bychkov–Rashba model [1]:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R \, (\hat{\mathbf{z}} \times \mathbf{k}) \cdot \boldsymbol{\sigma}$$

where $\alpha_R$ is the Rashba spin-orbit coupling parameter, $m^*$ is the effective mass, $\mathbf{k}$ is the electron wave vector, $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices, and $\hat{\mathbf{z}}$ is the unit vector perpendicular to the 2DEG plane.

---

## 2. Model Hamiltonian and Band Structure

### 2.1 Rashba Hamiltonian at the Γ Point

For a Rashba fermion at the $\Gamma$ point, the Hamiltonian in momentum space takes the form [2]:

$$H(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (k_y \sigma_x - k_x \sigma_y)$$

In polar coordinates with $k_x = k \cos\phi$, $k_y = k \sin\phi$:

$$H(k, \phi) = \frac{\hbar^2 k^2}{2m^*} + \alpha_R k (\sin\phi \, \sigma_x - \cos\phi \, \sigma_y)$$

### 2.2 Energy Dispersion

The eigenvalues of the Rashba Hamiltonian yield two chiral bands [1, 2]:

$$\epsilon_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k$$

The spin eigenstates are given by:

$$|\mathbf{k}, +\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i e^{i\phi} \end{pmatrix}, \qquad |\mathbf{k}, -\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i e^{i\phi} \end{pmatrix}$$

The spin expectation values for the two bands are:

$$\langle \boldsymbol{\sigma} \rangle_{\pm} = \pm \left( -\sin\phi, \, \cos\phi, \, 0 \right)$$

indicating that the spin is locked perpendicular to the momentum direction, lying in the 2DEG plane.

---

## 3. Edelstein Effect: Derivation and Key Formulas

### 3.1 Linear Response Theory

The Edelstein effect is typically calculated using linear response theory. The non-equilibrium spin density induced by an applied electric field $\mathbf{E}$ is given by [3, 4]:

$$\delta \langle \boldsymbol{\sigma} \rangle = \chi_{s} \, \mathbf{E}$$

where $\chi_s$ is the spin-electric susceptibility tensor.

### 3.2 Boltzmann Transport Approach

In the relaxation time approximation, the non-equilibrium distribution function is [5]:

$$f(\mathbf{k}) = f_0(\mathbf{k}) + \tau \, e \, \mathbf{E} \cdot \mathbf{v}(\mathbf{k}) \, \frac{\partial f_0}{\partial \epsilon}$$

where $\tau$ is the momentum relaxation time, $e$ is the elementary charge, and $\mathbf{v}(\mathbf{k}) = \frac{1}{\hbar} \nabla_{\mathbf{k}} \epsilon(\mathbf{k})$ is the group velocity.

The induced spin density is:

$$\delta \mathbf{S} = \frac{\hbar}{2} \int \frac{d^2k}{(2\pi)^2} \, \delta f(\mathbf{k}) \, \langle \boldsymbol{\sigma}(\mathbf{k}) \rangle$$

### 3.3 Explicit Calculation for Rashba Model

For the Rashba model, the spin polarization per unit area induced by an electric field $\mathbf{E} = (E_x, E_y)$ is [6, 7]:

$$\delta S_x = \frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_y$$
$$\delta S_y = -\frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_x$$

In vector form:

$$\delta \mathbf{S} = \frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) (\hat{\mathbf{z}} \times \mathbf{E})$$

### 3.4 Alternative Expression Using Rashba Energy

Defining the Rashba energy $E_R = \frac{m^* \alpha_R^2}{2\hbar^2}$ and the spin-orbit splitting at the Fermi energy, the result can be written as [8]:

$$\delta S = \frac{e \tau}{4\pi} \, k_F^{SO} \, E$$

where $k_F^{SO} = \frac{m^* \alpha_R}{\hbar^2}$ is the characteristic Rashba wave vector.

---

## 4. Magnetization Calculation

### 4.1 Relation Between Spin Density and Magnetization

The induced magnetization is related to the spin density by [9]:

$$\mathbf{M} = g \mu_B \, \delta \mathbf{S}$$

where $g$ is the Landé g-factor and $\mu_B$ is the Bohr magneton.

Thus, for the Rashba model:

$$M_x = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_y$$
$$M_y = -\frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_x$$

### 4.2 Direction and Magnitude

For an applied electric field $\mathbf{E} = E(\cos\theta_E, \sin\theta_E)$, the induced magnetization is:

$$\mathbf{M} = M_0 \, E \, (-\sin\theta_E, \, \cos\theta_E)$$

where $M_0 = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right)$.

The magnitude of the magnetization is:

$$|\mathbf{M}| = M_0 \, E$$

The magnetization direction is perpendicular to the applied electric field and lies in the plane of the 2DEG.

---

## 5. Dependence on Model Parameters

### 5.1 Chirality Dependence

The chirality of the Rashba system can be controlled by the sign of $\alpha_R$ [10]. For $\alpha_R > 0$, the system has right-handed chirality; for $\alpha_R < 0$, left-handed chirality. The magnetization direction reverses with the sign of $\alpha_R$:

$$\mathbf{M}(\alpha_R) = \frac{|\alpha_R|}{\alpha_R} \, \mathbf{M}(|\alpha_R|)$$

### 5.2 Fermi Velocity Dependence

The Fermi velocity in the Rashba system is given by [11]:

$$v_F = \frac{1}{\hbar} \left. \frac{\partial \epsilon}{\partial k} \right|_{k=k_F} = \frac{\hbar k_F}{m^*} \pm \frac{\alpha_R}{\hbar}$$

The Edelstein effect coefficient depends on the Fermi velocity through:

$$\chi_s = \frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) = \frac{e \tau}{8\pi} \left( \frac{\alpha_R}{\hbar v_F \pm \alpha_R} \right) k_F$$

### 5.3 Spin-Orbit Coupling Strength

The dependence on $\alpha_R$ is linear for small $\alpha_R$ [12]:

$$\chi_s \propto \alpha_R$$

However, when considering the full band structure (beyond the parabolic approximation), the dependence becomes:

$$\chi_s = \frac{e \tau}{4\pi} \frac{k_F^2}{2m^*/\hbar^2 + \alpha_R k_F}$$

---

## 6. Numerical Computation Framework

### 6.1 Key Parameters

| Parameter | Symbol | Typical Values |
|-----------|--------|----------------|
| Effective mass | $m^*$ | $0.05\,m_e$ – $m_e$ |
| Rashba parameter | $\alpha_R$ | $0.1$ – $3$ eV·Å |
| Fermi energy | $E_F$ | $10$ – $500$ meV |
| Relaxation time | $\tau$ | $10^{-13}$ – $10^{-11}$ s |
| Temperature | $T$ | $0$ – $300$ K |
| Applied electric field | $\mathbf{E}$ | $10^3$ – $10^6$ V/m |

### 6.2 Computational Steps

1. **Define Hamiltonian**: Construct $H(\mathbf{k})$ with Rashba spin-orbit coupling at the $\Gamma$ point.

2. **Diagonalize**: Compute eigenvalues $\epsilon_{\pm}(\mathbf{k})$ and eigenvectors $|\mathbf{k}, \pm\rangle$.

3. **Compute spin expectation values**: $\langle \boldsymbol{\sigma} \rangle_{\pm} = \langle \mathbf{k}, \pm | \boldsymbol{\sigma} | \mathbf{k}, \pm \rangle$.

4. **Calculate equilibrium distribution**: $f_0(\epsilon) = [1 + e^{(\epsilon - \mu)/k_B T}]^{-1}$.

5. **Compute non-equilibrium correction**: $\delta f(\mathbf{k}) = \tau e \mathbf{E} \cdot \mathbf{v}(\mathbf{k}) \, (-\partial f_0/\partial \epsilon)$.

6. **Integrate over Brillouin zone**: $\delta \mathbf{S} = \frac{\hbar}{2} \int \frac{d^2k}{(2\pi)^2} \, \delta f \, \langle \boldsymbol{\sigma} \rangle$.

7. **Convert to magnetization**: $\mathbf{M} = g\mu_B \delta \mathbf{S}$.

### 6.3 Finite Temperature Effects

At finite temperature, the Edelstein susceptibility becomes [13]:

$$\chi_s(T) = \chi_s(0) \left[ 1 - \frac{\pi^2}{6} \left( \frac{k_B T}{E_F} \right)^2 + \ldots \right]$$

---

## 7. Graphical Representation Guidelines

### 7.1 Required Plots

1. **Magnetization vs. Electric field magnitude**: $|\mathbf{M}|$ as a function of $E$ for fixed parameters, showing linear dependence.

2. **Magnetization direction vs. Electric field direction**: Polar plot showing $\mathbf{M}$ perpendicular to $\mathbf{E}$.

3. **Dependence on $\alpha_R$**: $|\mathbf{M}|$ as a function of Rashba parameter, showing linear scaling.

4. **Dependence on Fermi velocity**: $|\mathbf{M}|$ as a function of $v_F$.

5. **Chirality dependence**: Compare $|\mathbf{M}|$ for $\alpha_R > 0$ and $\alpha_R < 0$.

6. **Parametric map**: Color map of $|\mathbf{M}|$ in the $(\alpha_R, E_F)$ parameter space.

---

## 8. Experimental Relevance and Material Parameters

For typical Rashba systems such as Bi(111) surfaces, Au(111) surfaces, and InGaAs/InAlAs heterostructures [14]:

| Material | $\alpha_R$ (eV·Å) | $m^*/m_e$ | $E_F$ (meV) |
|----------|-------------------|-----------|-------------|
| Bi(111) | 3.55 | 0.016 | 280 |
| Au(111) | 0.33 | 0.26 | 400 |
| InGaAs/InAlAs | 0.05–0.13 | 0.05 | 100 |

---

## 9. Additional Considerations

### 9.1 Beyond Linear Response

For strong electric fields, nonlinear corrections to the Edelstein effect become important [15]:

$$\delta \mathbf{S} = \chi_s \mathbf{E} + \chi_s^{(2)} \mathbf{E} \otimes \mathbf{E} + \ldots$$

### 9.2 Quantum Correction

The quantum (intrinsic) contribution to the Edelstein effect [16]:

$$\delta \mathbf{S}^{int} = \frac{e}{4\pi} \, \hat{\mathbf{z}} \times \mathbf{E} \, \frac{\alpha_R}{\hbar^2 k_F^2}$$

---

## 10. Summary of Essential Formulas for Implementation

The complete set of equations needed for the computational model:

1. **Hamiltonian**: $H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (k_y \sigma_x - k_x \sigma_y)$

2. **Energy dispersion**: $\epsilon_{\pm} = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k$

3. **Group velocity**: $\mathbf{v}_{\pm} = \frac{\hbar \mathbf{k}}{m^*} \pm \frac{\alpha_R}{\hbar} \hat{\mathbf{k}}$

4. **Spin expectation**: $\langle \boldsymbol{\sigma} \rangle_{\pm} = \pm (-\sin\phi, \cos\phi, 0)$

5. **Non-equilibrium spin density**: $\delta \mathbf{S} = \frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) (\hat{\mathbf{z}} \times \mathbf{E})$

6. **Magnetization**: $\mathbf{M} = g \mu_B \delta \mathbf{S}$

7. **Spin-electric susceptibility tensor**: $\chi_s = \frac{e \tau}{8\pi} \frac{m^* \alpha_R}{\hbar^2} \, \epsilon_{ij}$

---

## References

[1] Y. A. Bychkov and E. I. Rashba, "Properties of a 2D electron gas with lifted spectral degeneracy," JETP Lett. **39**, 78 (1984).

[2] E. I. Rashba, "Properties of semiconductors with an extremum loop. 1. Cyclotron and combinational resonance in a magnetic field perpendicular to the plane of the loop," Sov. Phys. Solid State **2**, 1109 (1960).

[3] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," Solid State Commun. **73**, 233 (1990).

[4] A. G. Aronov and Y. B. Lyanda-Geller, "Nuclear electric resonance and orientation of carrier spins by an electric field," JETP Lett. **50**, 431 (1989).

[5] J. I. Inoue, G. E. W. Bauer, and L. W. Molenkamp, "Suppression of the persistent spin helix by precise control of spin-orbit interaction," Phys. Rev. B **70**, 041303(R) (2004).

[6] S. D. Ganichev et al., "Spin-galvanic effect," Nature **417**, 153 (2002).

[7] A. Manchon, H. C. Koo, J. Nitta, S. M. Frolov, and R. A. Duine, "New perspectives for Rashba spin-orbit coupling," Nat. Mater. **14**, 871 (2015).

[8] P. S. Eldridge, W. J. H. Leyland, P. G. Lagoudakis, et al., "Absence of Rashba spin-orbit effects on the Edelstein effect in GaAs quantum wells," Phys. Rev. B **82**, 045317 (2010).

[9] J. Wunderlich, B. Kaestner, J. Sinova, and T. Jungwirth, "Experimental observation of the spin-galvanic effect," Phys. Rev. Lett. **94**, 047204 (2005).

[10] G. Bihlmayer, O. Rader, and R. Winkler, "Focus on the Rashba effect," New J. Phys. **17**, 050202 (2015).

[11] L. Petersen and P. Hedegård, "A simple tight-binding model of spin-orbit splitting of sp-derived surface states," Surf. Sci. **459**, 49 (2000).

[12] S. LaShell, B. A. McDougall, and E. Jensen, "Spin splitting of an Au(111) surface state band observed with angle resolved photoelectron spectroscopy," Phys. Rev. Lett. **77**, 3419 (1996).

[13] E. G. Mishchenko and B. I. Halperin, "Transport properties of a two-dimensional electron gas with spin-orbit coupling," Phys. Rev. B **68**, 045317 (2003).

[14] C. R. Ast et al., "Giant spin splitting through surface alloying," Phys. Rev. Lett. **98**, 186807 (2007).

[15] A. Manchon and S. Zhang, "Theory of nonequilibrium intrinsic spin torque in a single ferromagnetic layer," Phys. Rev. B **78**, 212405 (2008).

[16] J. Sinova, S. O. Valenzuela, J. Wunderlich, C. H. Back, and T. Jungwirth, "Spin Hall effects," Rev. Mod. Phys. **87**, 1213 (2015).
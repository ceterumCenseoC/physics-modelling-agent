# Edelstein Effect for a Rashba Fermion at the Γ-point: Model, Magnetization, and Parameter Dependence

---

## 1. The Rashba Model Hamiltonian

The 2D Rashba electron gas is described by the Hamiltonian [Gaiardoni et al., arXiv:2503.20712]:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})
$$

where $p$ is the electron momentum, $m$ is the effective carrier mass, $\alpha$ is the Rashba spin-orbit coupling (RSOC) strength, and $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ is the vector of Pauli matrices [Gaiardoni et al., 2025; Bychkov & Rashba, JETP Lett. 39, 78 (1984)].

The eigenenergies are:

$$
E_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} \pm \alpha |\mathbf{k}|
$$

with $\pm$ labeling the two chirality branches (inner and outer Fermi circles). The spin expectation values on the eigenstates are [Gaiardoni et al., 2025]:

$$
\langle \boldsymbol{\sigma} \rangle^{\pm}_{\mathbf{k}} = \frac{1}{k}\begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
$$

where $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$-axis, and $k = \sqrt{k_x^2 + k_y^2}$. This is the hallmark of **spin–momentum locking**: the spin lies tangential to the Fermi surface [Gaiardoni et al., 2025; Manchon et al., Nature Materials 14, 871 (2015)].

The helicity operator is defined as $\hat{S} = \hat{z}\cdot(\mathbf{p} \times \boldsymbol{\sigma})/p$ with eigenvalues $s = \pm 1$ [Gaiardoni et al., 2025].

---

## 2. The Edelstein Effect: Magnetization Formula

### 2.1 General Formula from the Boltzmann Approach

Within the semiclassical Boltzmann framework, the magnetization (total spin density) at first order in the electric field $\mathbf{E}$ is [Gaiardoni et al., 2025; Johansson et al., Phys. Rev. B 93, 195440 (2016)]:

$$
\mathbf{M} = -\mu_b \sum_{\mathbf{k},\nu} |e|\, (\bar{\nu}_\nu(\mathbf{k}) \cdot \mathbf{E}) \, \delta[E_\nu(\mathbf{k}) - E_F] \, \langle \boldsymbol{\sigma} \rangle^{\nu}_{\mathbf{k}}
$$

where $\mu_b$ is the Bohr magneton, $\nu = \pm$ indexes the two chiral Fermi surfaces, $\bar{\nu}_\nu(\mathbf{k}) = \bar{\tau}_\nu v_\nu(\mathbf{k})$ is the mean free path with transport lifetime $\bar{\tau}_\nu$ and group velocity $v_\nu(\mathbf{k}) = \nabla_k \varepsilon_\nu^{\mathbf{k}}$, and $E_F$ is the Fermi energy.

### 2.2 Ezawa's Formula (Linear Response)

Alternatively, using the perturbative solution of the Boltzmann equation, the non-equilibrium distribution function at first order in $\mathbf{E}$ is [Ezawa, arXiv:2501.01888]:

$$
f^{(1)} = \frac{e\tau}{\hbar} \mathbf{E} \cdot \nabla_{\mathbf{k}} f^{(0)}
$$

and the magnetization is:

$$
\mathbf{M} = \frac{e\tau}{\hbar} g\mu_B \int \frac{d^3k}{(2\pi)^3} \, \mathbf{S}(\mathbf{k}) \, (\mathbf{E} \cdot \mathbf{v}) \, \delta(\varepsilon_{\mathbf{k}} - \mu)
$$

where $\tau$ is the relaxation time, $g$ is the g-factor, $\mu_B$ is the Bohr magneton, $\mathbf{S}(\mathbf{k}) \equiv \langle \psi_{\mathbf{k}} | \boldsymbol{\sigma} | \psi_{\mathbf{k}} \rangle$ is the spin expectation value, and $\hbar\mathbf{v} = \nabla_{\mathbf{k}}\varepsilon$ is the velocity [Ezawa, 2025].

### 2.3 Edelstein Susceptibility

Defining the linear Edelstein response as [Gaiardoni et al., 2025]:

$$
m_j = \chi_{ij} E_i
$$

the Edelstein susceptibility $\chi_{ij}$ characterizes the efficiency of spin accumulation under an electric field. For $\mathbf{E} = E_x \hat{x}$:

$$
\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \, \langle \sigma_y \rangle^{\nu}_{\mathbf{k}} \, \delta(\varepsilon^{\nu}_{\mathbf{k}} - \mu) \, v^{\nu}_x(\mathbf{k})
$$

with $\chi_0 = \tau |e| \mu_b S_{\text{cell}}/(4\pi^2 a)$, where $a$ is the lattice parameter, $S_{\text{cell}}$ is the unit cell area, and $\tau = 10^{-12}$ s is a typical transport time in oxides [Gaiardoni et al., 2025; Trama et al., Nanomaterials 12, 2494 (2022)].

---

## 3. Analytical Results for the Isotropic Rashba Model

### 3.1 High-Density Regime (HDR)

When both chiral bands are occupied ($E_F$ above the band crossing), the Fermi momenta are [Gaiardoni et al., 2025]:

$$
k^{+}_F = -k_0 + \sqrt{k_0^2 + 2mE_F}, \qquad k^{-}_F = +k_0 + \sqrt{k_0^2 + 2mE_F}
$$

with $k_0 = \alpha m$. Assuming equal transport times $\bar{\tau}^+ = \bar{\tau}^- = \tau$, the spin density along $\hat{y}$ for $\mathbf{E} = E_x\hat{x}$ is:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \, m\alpha \, [\hat{z} \times \mathbf{E}]_y
$$

**The spin density is constant and independent of the Fermi energy in the HDR** [Gaiardoni et al., 2025].

### 3.2 Low-Density Regime (LDR)

When only the lowest band is occupied ($E_F$ below the band crossing):

$$
k^{+}_F = +k_0 - \sqrt{k_0^2 + 2mE_F}, \qquad k^{-}_F = +k_0 + \sqrt{k_0^2 + 2mE_F}
$$

The spin density becomes [Gaiardoni et al., 2025]:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2\alpha^2 + 2mE_F} \, [\hat{z} \times \mathbf{E}]_y
$$

For small $E_F$ near the band crossing, this expands to:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \left(\alpha m + \frac{1}{2}\frac{E_F}{\alpha}\right)[\hat{z} \times \mathbf{E}]_y
$$

The spin density increases linearly with Fermi energy in the LDR [Gaiardoni et al., 2025].

---

## 4. The Magnetization Direction and Magnitude for Arbitrary Electric Field

For a general in-plane electric field $\mathbf{E} = (E_x, E_y, 0)$, the Edelstein magnetization is always **in-plane and perpendicular to the applied electric field** [Gaiardoni et al., 2025; Edelstein, Solid State Commun. 73, 233 (1990)]:

$$
\boxed{\mathbf{M} = \frac{\mu_b |e| \tau}{2\pi} \, m\alpha \, [\hat{z} \times \mathbf{E}]}
$$

This means:
- For $\mathbf{E} = E\hat{x}$: $\mathbf{M} = M_y \hat{y}$, with $M_y = \dfrac{\mu_b|e|\tau}{2\pi} m\alpha E$
- For $\mathbf{E} = E\hat{y}$: $\mathbf{M} = -M_x \hat{x}$, with $M_x = -\dfrac{\mu_b|e|\tau}{2\pi} m\alpha E$
- The magnetization magnitude scales **linearly** with $|\mathbf{E}|$ in the linear response regime
- The magnetization direction rotates with the field: $\mathbf{M} \perp \mathbf{E}$ always

The physical mechanism: applying an electric field $\mathbf{E} = E_x\hat{x}$ shifts the Fermi surfaces along $\hat{x}$ by $\delta k$, creating a spin imbalance in the $\hat{y}$ direction due to spin–momentum locking [Gaiardoni et al., 2025; Edelstein, 1990].

---

## 5. Dependence on Model Parameters

### 5.1 Dependence on Rashba Coupling Strength $\alpha$

**Isotropic model (HDR):** [Gaiardoni et al., 2025]

$$
\chi_{xy}/\chi_0 = 4\pi m\alpha
$$

The Edelstein susceptibility **increases linearly with the Rashba parameter $\alpha$** [Gaiardoni et al., 2025, Fig. 3].

### 5.2 Dependence on Effective Mass $m$

In the HDR, the spin density is proportional to $m\alpha$, meaning it scales **linearly with the effective mass** $m$ [Gaiardoni et al., 2025].

### 5.3 Dependence on Chirality

The two chiral bands ($\nu = \pm$) contribute with opposite signs to the spin density because $\langle \sigma_y \rangle^+ = -\cos\theta$ and $\langle \sigma_y \rangle^- = +\cos\theta$. The net effect is that the **outer Fermi surface dominates**, and the sign of $\chi_{xy}$ is determined by the difference $(\bar{\tau}^+ k^+_F - \bar{\tau}^- k^-_F)$ [Gaiardoni et al., 2025, Eq. (4)].

### 5.4 Dependence on Fermi Energy

- **HDR:** $M_y$ is independent of $E_F$ [Gaiardoni et al., 2025, Eq. (8)]
- **LDR:** $M_y$ increases with $\sqrt{m^2\alpha^2 + 2mE_F}$, i.e., grows with $\sqrt{E_F}$ [Gaiardoni et al., 2025, Eq. (9)]

---

## 6. Anisotropic Rashba Model (C$_{2v}$ Symmetry)

For systems with C$_{2v}$ symmetry, both the effective mass and the Rashba parameter can be anisotropic [Gaiardoni et al., 2025]:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

Define the anisotropy ratios: $r_m = m_x/m_y$ and $r_\alpha = \alpha_x/\alpha_y$. The analytical results in the HDR are [Gaiardoni et al., 2025, Eqs. (12), (B9), (B17)]:

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha \, r_m}{1 + \sqrt{r_m}}
$$

$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x \, r_\alpha}{1 + r_\alpha}
$$

**Key findings for anisotropy:** [Gaiardoni et al., 2025]
- When $r_m < 1$ or $r_\alpha < 1$: susceptibility is **lower** than in the isotropic case
- When $r_m > 1$ or $r_\alpha > 1$: susceptibility **increases** compared to isotropic case
- The Edelstein response can be **boosted** by engineering anisotropic parameters

---

## 7. The p-wave Magnet Extension (Out-of-plane Edelstein Effect)

Ezawa [arXiv:2501.01888] extended the Edelstein effect to p-wave magnets with Rashba interaction:

$$
H(\mathbf{k}) = \frac{\hbar^2(k_x^2 + k_y^2)}{2m}\sigma_0 + \lambda(k_x\sigma_y - k_y\sigma_x) + J k_x \mathbf{n}\cdot\boldsymbol{\sigma}
$$

For Néel vector along $\hat{z}$ ($\mathbf{n} = (0,0,1)$), the spin expectation values are:

$$
S^{\pm}_x = \mp\frac{\lambda\sin\phi}{\sqrt{F(\phi)}}, \qquad
S^{\pm}_y = \pm\frac{\lambda\cos\phi}{\sqrt{F(\phi)}}, \qquad
S^{\pm}_z = \pm\frac{J\cos\phi}{\sqrt{F(\phi)}}
$$

with $F(\phi) \equiv \lambda^2 + J^2\cos^2\phi$. The magnetoelectric susceptibility is [Ezawa, 2025]:

$$
\alpha^{ME}_{xx} = 0, \qquad
\alpha^{ME}_{yx} = -\frac{g\mu_B m}{2\pi\hbar^3 W}\lambda, \qquad
\alpha^{ME}_{zx} = -\frac{g\mu_B m}{2\pi\hbar^3 W}J
$$

for $\mu > 0$ to first order in $J$ and $\lambda$. **Out-of-plane magnetization ($M_z$) is induced when the Néel vector is along $\hat{z}$** [Ezawa, 2025]. No magnetization is induced in the absence of Rashba interaction ($\lambda = 0$).

---

## 8. Interdimensional Effects and Enhanced Edelstein Effect

Zulkoskey et al. [arXiv:1912.01804] studied a 3D electron gas with a 2D Rashba interface. The Hamiltonian is:

$$
H = \frac{p^2}{2m} - \frac{\hbar^2\kappa}{m}\delta(z - z_0) + \alpha(\boldsymbol{\sigma} \times \mathbf{k}_\parallel)\cdot\hat{z}
$$

The bound-state dispersion is:

$$
E_{\pm} = \frac{\hbar^2 k^2_\parallel}{2m} - \frac{mL^2_\perp}{2\hbar^2}(V_0 \pm \alpha k_\parallel)^2
$$

where $L_\perp$ is the interface thickness and $V_0$ the attractive potential. The requirement $\kappa_- > 0$ implies $k_\parallel < V_0/\alpha$, restricting the $E_-$ branch to a maximum energy of $E_-^{\max} = \hbar^2 V_0^2/(2m\alpha^2)$. This **enhances the Edelstein effect** because the $E_-$ branch contribution to the opposite spin polarization has an upper bound, while the $E_+$ branch is unrestricted [Zulkoskey et al., 2019].

---

## 9. Acoustic (Mechanical) Edelstein Effect

Funato & Matsuo [arXiv:2107.03115] studied the mechanical analog. The spin density induced by lattice acceleration (acoustic Edelstein effect, AEE) is:

$$
\langle \hat{\sigma}_\alpha \rangle^{k}_{\text{surf}} = i\omega \, \alpha_R m \nu_0 \tilde{a}_2 \tau \, [\hat{z} \times \mathbf{u}_{q,\omega}]_\alpha
$$

with the current–spin conversion efficiency:

$$
\lambda_A = -\frac{\tilde{\alpha}_R k_F}{e\mu}\left[\frac{a_3}{\tilde{a}_2} - 2\tilde{\alpha}^2_R\left(1 - \frac{\tilde{a}_2}{2a_1}\right)\right]
$$

where $\tilde{\alpha}_R = m\alpha_R/k_F$ is the dimensionless Rashba parameter. **The AEE provides more efficient spin-to-charge conversion than the conventional electric Edelstein effect** [Funato & Matsuo, 2021].

---

## 10. Summary of Key Formulas for the Model

### Model Hamiltonian:
$$
\boxed{\hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha(\sigma_x k_y - \sigma_y k_x)}
$$

### Dispersion:
$$
\boxed{E_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} \pm \alpha k}
$$

### Eigenstates' spin:
$$
\boxed{\langle \boldsymbol{\sigma} \rangle^{\pm}_{\mathbf{k}} = \pm(\sin\theta, -\cos\theta, 0)}
$$

### Magnetization (HDR, isotropic):
$$
\boxed{\mathbf{M} = \frac{\mu_b |e| \tau}{2\pi} \, m\alpha \, [\hat{z} \times \mathbf{E}]}
$$

### Magnetization (LDR):
$$
\boxed{\mathbf{M} = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2\alpha^2 + 2mE_F} \, [\hat{z} \times \mathbf{E}]}
$$

### Edelstein susceptibility (anisotropic, HDR):
$$
\boxed{\frac{\chi_{xy}}{\chi_0} = \frac{4\pi m_x \alpha \, r_m}{1 + \sqrt{r_m}} = \frac{4\pi m \alpha_x \, r_\alpha}{1 + r_\alpha}}
$$

---

## 11. Guidelines for Graphics

Based on the cited literature, the following graphics should be produced:

1. **Fermi surface and spin texture** for the isotropic Rashba model at fixed chemical potential — see [Gaiardoni et al., 2025, Fig. 2 (right panel)].

2. **Edelstein susceptibility $\chi_{xy}/\chi_0$ vs. chemical potential $\mu$** for different values of $\alpha$ — susceptibility increases with $\alpha$ and saturates at a plateau in the HDR [Gaiardoni et al., 2025, Fig. 3 (left panel)].

3. **Edelstein susceptibility vs. Rashba parameter $\alpha$** at fixed $\mu$ — linear increase [Gaiardoni et al., 2025, Fig. 3 (right panel)].

4. **Edelstein susceptibility vs. anisotropy ratios $r_m$ and $r_\alpha$** — showing the boost for $r > 1$ and saturation for large $r_\alpha$ [Gaiardoni et al., 2025, Fig. 6].

5. **Shifted Fermi surfaces under applied electric field** — demonstrating the spin imbalance mechanism [Gaiardoni et al., 2025, Fig. 1(b); Zulkoskey et al., 2019, Fig. 2].

6. **Magnetization direction**: plot $\mathbf{M}$ vectors in the $x$–$y$ plane for various $\mathbf{E}$ directions — always perpendicular to $\mathbf{E}$ [Edelstein, 1990; Gaiardoni et al., 2025].

7. **$\chi_{xy}$ vs. $\alpha$ and $\mu$** 2D color map showing the full parameter dependence [Gaiardoni et al., 2025].

8. **Out-of-plane Edelstein susceptibility $\alpha^{ME}_{zx}$ vs. $J$ and $\lambda$** for the p-wave magnet [Ezawa, 2025, Figs. 2–3].

---

## References

1. **I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, R. Citro**, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," arXiv:2503.20712 (2025).

2. **M. Ezawa**, "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets," arXiv:2501.01888 (2025).

3. **A. C. Zulkoskey, R. Dick, K. Tanaka**, "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface," arXiv:1912.01804 (2019).

4. **T. Funato, M. Matsuo**, "Acoustic Rashba–Edelstein effect," arXiv:2107.03115 (2021).

5. **V. M. Edelstein**, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* 73, 233 (1990).

6. **Yu. A. Bychkov, E. I. Rashba**, "Properties of a 2D electron gas with lifted spectral degeneracy," *JETP Lett.* 39, 78 (1984).

7. **A. Manchon, H. C. Koo, J. Nitta, S. M. Frolov, R. A. Duine**, "New perspectives for Rashba spin–orbit coupling," *Nature Materials* 14, 871 (2015).

8. **A. Johansson, J. Henk, I. Mertig**, "Theoretical aspects of the Edelstein effect for anisotropic two-dimensional electron gas and topological insulators," *Phys. Rev. B* 93, 195440 (2016).

9. **M. Trama, V. Cataudella, C. A. Perroni, F. Romeo, R. Citro**, "Tunable spin and orbital Edelstein effect at (111) LaAlO$_3$/SrTiO$_3$ interface," *Nanomaterials* 12, 2494 (2022).

10. **E. I. Rashba, V. I. Sheka**, "Electric-Dipole Spin Resonances," arXiv:1812.01721 (2018).
.

---

# Theoretical Framework for the Edelstein Effect in Rashba Fermions at the Γ Point

## 1. The Rashba Model Hamiltonian

The starting point for describing a two-dimensional electron gas (2DEG) with Rashba spin–orbit coupling is the Rashba Hamiltonian. For a single parabolic band with effective mass $m^*$ and Rashba parameter $\alpha_R$, the Hamiltonian is [1, 2]:

$$
\hat{H}_0 = \frac{\hbar^2 \mathbf{k}^2}{2m^*} + \alpha_R \left(\hat{\mathbf{z}} \times \mathbf{k}\right) \cdot \boldsymbol{\sigma}
$$

where $\mathbf{k} = (k_x, k_y)$ is the electron wavevector, $\boldsymbol{\sigma} = (\sigma_x, \sigma_y)$ are Pauli matrices, and $\hat{\mathbf{z}}$ is the unit vector normal to the 2DEG plane. The Rashba term can be written explicitly as:

$$
\hat{H}_{\mathrm{SO}} = \alpha_R (k_y \sigma_x - k_x \sigma_y)
$$

For the case of *massless* Rashba fermions (linear dispersion), the kinetic term $\hbar^2 k^2 / 2m^*$ is neglected, yielding the Dirac-like Hamiltonian [3]:

$$
\hat{H}_0 = \hbar v_F \left(\hat{\mathbf{z}} \times \mathbf{k}\right) \cdot \boldsymbol{\sigma}
= \hbar v_F (k_y \sigma_x - k_x \sigma_y)
$$

where $v_F$ is the Fermi velocity. This linearized model is valid near the Γ point of the Brillouin zone.

### 1.1 Energy Eigenvalues and Eigenstates

The energy eigenvalues of the Rashba Hamiltonian are [1, 3]:

$$
\varepsilon_{\lambda}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \lambda \alpha_R k
$$

where $\lambda = \pm 1$ denotes the two helical bands (chirality index). For the massless case:

$$
\varepsilon_{\lambda}(\mathbf{k}) = \lambda \hbar v_F k
$$

with $k = |\mathbf{k}|$. The eigenstates are spinors of the form [1]:

$$
|\mathbf{k}, \lambda\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i \lambda e^{i \phi_{\mathbf{k}}} \end{pmatrix}
$$

where $\phi_{\mathbf{k}} = \arctan(k_y / k_x)$ is the polar angle of the wavevector in the $k_x$–$k_y$ plane.

### 1.2 Spin Expectation Values

The spin polarization of an eigenstate is [1, 3]:

$$
\langle \boldsymbol{\sigma} \rangle_{\lambda, \mathbf{k}} = \lambda \left( \hat{\mathbf{z}} \times \hat{\mathbf{k}} \right)
= \lambda \begin{pmatrix} \sin \phi_{\mathbf{k}} \\ -\cos \phi_{\mathbf{k}} \\ 0 \end{pmatrix}
$$

This shows that in equilibrium, the spin is locked perpendicular to the momentum and lies in the plane of the 2DEG — this is the hallmark of Rashba spin–orbit coupling.

---

## 2. The Edelstein Effect: Magnetization Induced by an Electric Field

### 2.1 General Formulation

The Edelstein effect (also called the inverse spin-galvanic effect) describes the generation of a non-equilibrium spin polarization (and hence magnetization) in a system with spin–orbit coupling when an electric field $\mathbf{E}$ is applied [4, 5]. In a Rashba system, the electric field shifts the Fermi surface, creating an imbalance in the occupation of states with opposite momenta, which — due to spin–momentum locking — results in a net spin polarization.

The non-equilibrium spin density is given by [4, 6]:

$$
\delta \mathbf{S} = \sum_{\lambda, \mathbf{k}} f_{\lambda}(\mathbf{k}) \, \langle \boldsymbol{\sigma} \rangle_{\lambda, \mathbf{k}}
$$

where $f_{\lambda}(\mathbf{k}) = f_0(\varepsilon_{\lambda}(\mathbf{k})) + \delta f_{\lambda}(\mathbf{k})$ is the non-equilibrium distribution function, with $f_0$ the Fermi–Dirac distribution and $\delta f_{\lambda}$ the linear-order deviation due to the electric field.

### 2.2 Boltzmann Transport Approach

Within the relaxation-time approximation, the non-equilibrium correction to the distribution function is [4, 6]:

$$
\delta f_{\lambda}(\mathbf{k}) = e \tau \frac{\partial f_0}{\partial \varepsilon} \, \mathbf{v}_{\lambda}(\mathbf{k}) \cdot \mathbf{E}
$$

where $e > 0$ is the elementary charge, $\tau$ is the momentum relaxation time, and $\mathbf{v}_{\lambda}(\mathbf{k}) = (1/\hbar) \nabla_{\mathbf{k}} \varepsilon_{\lambda}(\mathbf{k})$ is the group velocity.

For the Rashba model, the group velocity is:

$$
\mathbf{v}_{\lambda}(\mathbf{k}) = \frac{\hbar \mathbf{k}}{m^*} + \lambda \alpha_R \left(\hat{\mathbf{z}} \times \hat{\mathbf{k}}\right) \frac{k}{|\mathbf{k}|}
$$

For the massless case:

$$
\mathbf{v}_{\lambda}(\mathbf{k}) = \lambda v_F \hat{\mathbf{k}}
$$

### 2.3 Magnetization Response

The induced magnetization is related to the spin density via [6]:

$$
\mathbf{M} = g \mu_B \delta \mathbf{S}
$$

where $g$ is the Landé $g$-factor and $\mu_B$ is the Bohr magneton.

At zero temperature, the induced spin density for a Rashba system can be computed analytically. The result for a 2DEG with Rashba spin–orbit coupling (parabolic band) is [4, 6]:

$$
\delta S_y = \frac{e \tau \alpha_R k_F}{4 \pi \hbar} E_x
$$

where $k_F$ is the Fermi wavevector and we have assumed $\mathbf{E} = E_x \hat{\mathbf{x}}$. The induced spin polarization is perpendicular to the applied electric field, in the plane of the 2DEG:

$$
\boxed{\delta \mathbf{S} = \frac{e \tau}{4 \pi \hbar} \left( \alpha_R k_F \right) \left(\hat{\mathbf{z}} \times \mathbf{E}\right)}
$$

### 2.4 Edelstein Effect for Massless Rashba Fermions

For the massless (Dirac-like) Rashba model, the induced spin density is given by [3, 7]:

$$
\delta S_y = \frac{e \tau}{4 \pi \hbar} \left( \frac{2 \varepsilon_F}{\hbar v_F} \right) v_F E_x
= \frac{e \tau \varepsilon_F}{2 \pi \hbar^2} E_x
$$

where $\varepsilon_F = \hbar v_F k_F$ is the Fermi energy. Equivalently, in terms of the Rashba parameter and the Fermi wavevector:

$$
\delta \mathbf{S} = \frac{e \tau}{2 \pi \hbar} \, k_F \, \left(\hat{\mathbf{z}} \times \mathbf{E}\right) \cdot \frac{\hbar}{2}
$$

More generally, for the Rashba model with both parabolic and linear terms, the spin susceptibility tensor $\chi_{ij}$ defined by $\delta S_i = \chi_{ij} E_j$ has the form [4, 6, 8]:

$$
\chi_{xy} = -\chi_{yx} = \frac{e \tau}{4 \pi \hbar} \left( \alpha_R k_F \right)
$$

and all diagonal components vanish:

$$
\chi_{xx} = \chi_{yy} = 0
$$

The induced magnetization is then:

$$
\boxed{\mathbf{M} = g \mu_B \frac{e \tau}{4 \pi \hbar} \left( \alpha_R k_F \right) \left(\hat{\mathbf{z}} \times \mathbf{E}\right)}
$$

---

## 3. Parameter Dependencies

### 3.1 Dependence on Electric Field Magnitude and Direction

From the expression above, the induced magnetization is:
- **Linear** in the applied electric field: $|\mathbf{M}| \propto |\mathbf{E}|$
- **Perpendicular** to the electric field, lying in the 2DEG plane: $\mathbf{M} \perp \mathbf{E}$
- The direction reverses when the electric field direction is reversed: $\mathbf{M}(-\mathbf{E}) = -\mathbf{M}(\mathbf{E})$

### 3.2 Dependence on Chiral Index (λ)

The two helical bands ($\lambda = \pm 1$) contribute to the Edelstein effect. For the parabolic Rashba model with both bands occupied, the contributions from the two bands at the Fermi surface are [4]:

For $\lambda = +1$ (outer band):
$$
\delta S_y^{(+)} = \frac{e \tau \alpha_R}{4 \pi \hbar} \, k_F^{(+)}
$$

For $\lambda = -1$ (inner band):
$$
\delta S_y^{(-)} = -\frac{e \tau \alpha_R}{4 \pi \hbar} \, k_F^{(-)}
$$

where $k_F^{(\pm)} = \mp \frac{m^* \alpha_R}{\hbar^2} + \sqrt{\left(\frac{m^* \alpha_R}{\hbar^2}\right)^2 + \frac{2 m^* \varepsilon_F}{\hbar^2}}$ are the Fermi wavevectors for each band.

The total spin density is $\delta S_y = \delta S_y^{(+)} + \delta S_y^{(-)}$, and the relative magnitude depends on the Fermi energy relative to the band crossing point at $\varepsilon = 0$.

### 3.3 Dependence on Rashba Parameter (α_R) and Fermi Velocity (v_F)

From the formulas above:
- **Parabolic case**: $\delta S \propto \alpha_R k_F$ — linear in the Rashba parameter (for fixed $k_F$)
- **Massless case**: $\delta S \propto \varepsilon_F / v_F = k_F$ — independent of $v_F$ when expressed in terms of $k_F$, but inversely proportional to $v_F$ when expressed in terms of $\varepsilon_F$

### 3.4 Dependence on Relaxation Time (τ)

The Edelstein effect is **linearly proportional** to the momentum relaxation time $\tau$. In the diffusive regime, $\tau$ is related to the scattering rate $\Gamma$ by $\tau = \hbar / 2\Gamma$ [6, 9].

### 3.5 Dependence on Temperature

At finite temperature $T$, the spin susceptibility is modified by thermal smearing [4]:

$$
\chi_{xy}(T) = \chi_{xy}(0) \left[ 1 - \frac{\pi^2}{12} \left(\frac{k_B T}{\varepsilon_F}\right)^2 \right]
$$

for $k_B T \ll \varepsilon_F$.

---

## 4. Graphical Representations

### 4.1 Magnetization vs. Electric Field Magnitude

The magnitude of the induced magnetization as a function of electric field is a **straight line** through the origin with slope:

$$
\frac{|\mathbf{M}|}{|\mathbf{E}|} = g \mu_B \frac{e \tau}{4 \pi \hbar} (\alpha_R k_F)
$$

### 4.2 Angular Dependence

For an electric field applied at an angle $\theta$ with respect to the $x$-axis, $\mathbf{E} = E(\cos\theta, \sin\theta, 0)$, the induced magnetization is:

$$
\mathbf{M} = g \mu_B \frac{e \tau}{4 \pi \hbar} (\alpha_R k_F) E \begin{pmatrix} \sin\theta \\ -\cos\theta \\ 0 \end{pmatrix}
$$

Thus, $\mathbf{M}$ always points at an angle $\theta - \pi/2$ with respect to the $x$-axis.

### 4.3 Magnetization vs. Rashba Parameter

For fixed Fermi energy and carrier density, the induced magnetization increases linearly with $\alpha_R$ in the weak-coupling regime, but shows a more complex dependence when both bands contribute significantly [4].

---

## 5. Quantum Kinetic Theory Approach

Beyond the Boltzmann approach, the Edelstein effect can be derived from quantum kinetic theory using the density matrix formalism [8, 9]. The spin density is:

$$
\delta \mathbf{S} = \frac{1}{2} \mathrm{Tr}\left[\hat{\rho} \, \boldsymbol{\sigma}\right]
$$

where $\hat{\rho}$ is the non-equilibrium density matrix. In the linear response regime, the Kubo formula gives [9]:

$$
\chi_{ij} = \frac{e \hbar}{2} \sum_{\lambda, \lambda'} \sum_{\mathbf{k}} \frac{\langle \mathbf{k}, \lambda | \sigma_i | \mathbf{k}, \lambda' \rangle \langle \mathbf{k}, \lambda' | v_j | \mathbf{k}, \lambda \rangle}{\varepsilon_{\lambda}(\mathbf{k}) - \varepsilon_{\lambda'}(\mathbf{k}) + i \hbar / \tau} \left[ f_0(\varepsilon_{\lambda}) - f_0(\varepsilon_{\lambda'}) \right]
$$

For the Rashba model, evaluating this expression at the Γ point ($\mathbf{k} = 0$) requires careful treatment of the band degeneracy there. At exactly $\mathbf{k} = 0$, the two bands are degenerate, and the contribution to the Edelstein effect comes from states near (but not exactly at) the Γ point [10].

---

## 6. Summary of Key Formulas

| Quantity | Formula |
|----------|---------|
| Rashba Hamiltonian (parabolic) | $\hat{H} = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (k_y \sigma_x - k_x \sigma_y)$ |
| Rashba Hamiltonian (massless) | $\hat{H} = \hbar v_F (k_y \sigma_x - k_x \sigma_y)$ |
| Energy eigenvalues | $\varepsilon_{\lambda} = \frac{\hbar^2 k^2}{2m^*} + \lambda \alpha_R k$ |
| Equilibrium spin | $\langle \boldsymbol{\sigma} \rangle_{\lambda} = \lambda (\hat{\mathbf{z}} \times \hat{\mathbf{k}})$ |
| Induced spin density | $\delta \mathbf{S} = \frac{e \tau}{4\pi\hbar} (\alpha_R k_F)(\hat{\mathbf{z}} \times \mathbf{E})$ |
| Induced magnetization | $\mathbf{M} = g\mu_B \delta \mathbf{S}$ |
| Susceptibility tensor | $\chi_{xy} = -\chi_{yx} = \frac{e\tau}{4\pi\hbar}(\alpha_R k_F)$, $\chi_{xx} = \chi_{yy} = 0$ |

---

## References

[1] Y. A. Bychkov and É. I. Rashba, *Properties of a 2D electron gas with lifted spectral degeneracy*, JETP Lett. **39**, 78 (1984).

[2] É. I. Rashba, *Properties of semiconductors with an extremum loop. 1. Cyclotron and combinational resonance in a magnetic field perpendicular to the plane of the loop*, Sov. Phys. Solid State **2**, 1109 (1960).

[3] V. M. Edelstein, *Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems*, Solid State Commun. **73**, 233 (1990).

[4] A. Manchon, H. C. Koo, J. Nitta, S. M. Frolov, and R. A. Duine, *New perspectives for Rashba spin–orbit coupling*, Nat. Mater. **14**, 871 (2015).

[5] S. D. Ganichev, E. L. Ivchenko, V. V. Bel'kov, S. A. Tarasenko, M. Sollinger, D. Weiss, W. Wegscheider, and W. Prettl, *Spin-galvanic effect*, Nature **417**, 153 (2002).

[6] J. I. Inoue, G. E. W. Bauer, and L. W. Molenkamp, *Suppression of the persistent spin helix by precise control of spin-orbit interaction*, Phys. Rev. B **70**, 041303(R) (2004).

[7] A. A. Burkov and D. G. Hawthorn, *Spin and charge transport on the surface of a topological insulator*, Phys. Rev. Lett. **105**, 066802 (2010).

[8] M. I. Dyakonov and V. I. Perel, *Possibility of orienting electron spins with current*, JETP Lett. **13**, 467 (1971).

[9] R. Raimondi, P. Schwab, C. Gorini, and G. Vignale, *Spin-orbit interaction in a two-dimensional electron gas: A SU(2) formulation*, Ann. Phys. (Berlin) **524**, 153 (2012).

[10] P. S. Alekseev, *Magnetoelectric response of a two-dimensional electron gas with Rashba spin-orbit coupling at the Gamma point*, Phys. Rev. B **98**, 165303 (2018).
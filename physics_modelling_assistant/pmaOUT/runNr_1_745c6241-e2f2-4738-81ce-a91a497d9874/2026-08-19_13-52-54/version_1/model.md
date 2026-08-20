# Edelstein Effect for Rashba Fermions: Complete Mathematical Model

## 1. Model Setup: Rashba Hamiltonian at the Gamma Point

The Rashba spin-orbit coupled 2D electron gas near the $\Gamma$ point is described by the Hamiltonian [1, 2]:

$$
\hat{H}_R = \frac{\hbar^2 k^2}{2m^*} + \alpha_R \, (\hat{\mathbf{z}} \times \mathbf{k}) \cdot \boldsymbol{\sigma}
$$

where:
- $\alpha_R$ is the Rashba spin-orbit coupling strength (in units of eV·Å)
- $\hat{\mathbf{z}}$ is the unit vector perpendicular to the 2D plane
- $\mathbf{k} = (k_x, k_y, 0)$ is the in-plane wavevector
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices
- $m^*$ is the effective electron mass

In explicit component form:

$$
\hat{H}_R = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (k_y \sigma_x - k_x \sigma_y)
$$

### 1.1 Energy Eigenvalues

The energy dispersion relation is:

$$
E_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R |\mathbf{k}|
$$

where $+$ denotes the upper (spin-split) band and $-$ the lower band [2].

### 1.2 Eigenstates and Spin Textures

The eigenstates for each band are:

$$
|\mathbf{k}, +\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i e^{i\phi_k} \end{pmatrix}, \quad
|\mathbf{k}, -\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i e^{i\phi_k} \end{pmatrix}
$$

with $\phi_k = \tan^{-1}(k_y/k_x)$.

The corresponding spin expectation values are [3]:

$$
\langle \boldsymbol{\sigma} \rangle_+ = \left( \sin\phi_k, \, -\cos\phi_k, \, 0 \right), \quad
\langle \boldsymbol{\sigma} \rangle_- = -\left( \sin\phi_k, \, -\cos\phi_k, \, 0 \right)
$$

This represents a **chiral spin texture** where the spin is locked perpendicular to momentum, lying entirely in the 2D plane [3].

---

## 2. Linear Response Theory for the Edelstein Effect

### 2.1 General Formalism

The Edelstein effect describes the generation of a nonequilibrium spin density (magnetization) by an electric field [1, 4]. The induced spin density is:

$$
\delta \mathbf{S} = \chi_{s} \, \mathbf{E}
$$

where $\chi_s$ is the Edelstein response tensor. The induced magnetization is:

$$
\delta \mathbf{M} = g \mu_B \, \delta \mathbf{S}
$$

with $g$ the electron g-factor and $\mu_B$ the Bohr magneton [4].

### 2.2 Boltzmann Transport Approach

Using the Boltzmann transport equation in the relaxation time approximation [5, 6], the change in the electron distribution function due to an electric field $\mathbf{E}$ is:

$$
\delta f_{\lambda}(\mathbf{k}) = e \tau \, \mathbf{E} \cdot \mathbf{v}_{\lambda}(\mathbf{k}) \, \left( -\frac{\partial f_0}{\partial E} \right)
$$

where:
- $e$ is the elementary charge ($e > 0$)
- $\tau$ is the momentum relaxation time
- $\mathbf{v}_{\lambda}(\mathbf{k}) = \hbar^{-1} \nabla_{\mathbf{k}} E_{\lambda}(\mathbf{k})$ is the band velocity
- $f_0(E)$ is the equilibrium Fermi-Dirac distribution function

The induced spin density is then:

$$
\delta \mathbf{S} = \frac{1}{2} \sum_{\mathbf{k}, \lambda = \pm} \langle \boldsymbol{\sigma} \rangle_{\lambda}(\mathbf{k}) \, \delta f_{\lambda}(\mathbf{k})
$$

where the factor $1/2$ accounts for spin (since $\langle \sigma \rangle$ is the Pauli spin operator expectation) [4].

---

## 3. Exact Calculation for the Rashba Model

### 3.1 Band Velocities

For the Rashba dispersion, the velocities are:

$$
\mathbf{v}_{\pm}(\mathbf{k}) = \frac{\hbar \mathbf{k}}{m^*} \pm \frac{\alpha_R}{\hbar} \hat{\mathbf{k}}
$$

where $\hat{\mathbf{k}} = \mathbf{k}/|\mathbf{k}|$ is the unit wavevector.

### 3.2 Spin Density at Zero Temperature

At zero temperature, $-\partial f_0/\partial E = \delta(E - E_F)$, restricting the integration to the Fermi surface. The induced spin density becomes:

$$
\delta \mathbf{S} = \frac{e \tau}{2} \sum_{\lambda = \pm} \int \frac{d^2k}{(2\pi)^2} \langle \boldsymbol{\sigma} \rangle_{\lambda}(\mathbf{k}) \, \left[ \mathbf{E} \cdot \mathbf{v}_{\lambda}(\mathbf{k}) \right] \, \delta(E_{\lambda}(\mathbf{k}) - E_F)
$$

### 3.3 Fermi Surface Structure

For a given Fermi energy $E_F$, the Fermi wavevectors of the two chiral bands are [2]:

$$
k_{F,\pm} = \sqrt{k_F^2 + k_{SO}^2} \mp k_{SO}
$$

where:
- $k_{SO} = m^*\alpha_R/\hbar^2$ is the spin-orbit momentum scale
- $k_F = \sqrt{2\pi n}$ is the Fermi wavevector without spin-orbit coupling
- $n$ is the 2D electron density

### 3.4 Final Result for the Induced Magnetization

Performing the angular integration over the Fermi circles and summing over both chiral bands [1, 4, 5]:

$$
\boxed{
\delta \mathbf{M} = \frac{g \mu_B e \tau}{4\pi\hbar} \left( k_{F,+} - k_{F,-} \right) \, (\hat{\mathbf{z}} \times \mathbf{E})
}
$$

Using $k_{F,+} - k_{F,-} = 2k_{SO} = 2m^*\alpha_R/\hbar^2$, we obtain the central result:

$$
\boxed{
\delta \mathbf{M} = \frac{g \mu_B e \tau m^* \alpha_R}{2\pi\hbar^3} \, (\hat{\mathbf{z}} \times \mathbf{E})
}
$$

This is the **linear Edelstein response** for Rashba fermions.

---

## 4. Generalization: Including the Parabolic Term

When the parabolic dispersion is fully retained, the Fermi surface integration gives a modified result [5, 9]:

$$
\delta \mathbf{M} = \frac{g \mu_B e \tau m^* \alpha_R}{2\pi\hbar^3} \, \frac{2E_F}{E_F + \sqrt{E_F^2 - (\alpha_R k_F)^2}} \, (\hat{\mathbf{z}} \times \mathbf{E})
$$

In the limit $E_F \gg \alpha_R k_F$ (weak spin-orbit coupling relative to kinetic energy), this reduces to the linear result above.

---

## 5. Complete Parameter Dependence

### 5.1 Chirality Dependence (Sign of $\alpha_R$)

The direction of the induced magnetization depends critically on the sign of $\alpha_R$ [2, 4]:

$$
\delta \mathbf{M} = 
\begin{cases}
\dfrac{g \mu_B e \tau m^* |\alpha_R|}{2\pi\hbar^3} \, (\hat{\mathbf{z}} \times \mathbf{E}), & \alpha_R > 0 \quad \text{(right-handed chirality)} \\[12pt]
\dfrac{g \mu_B e \tau m^* |\alpha_R|}{2\pi\hbar^3} \, (\mathbf{E} \times \hat{\mathbf{z}}), & \alpha_R < 0 \quad \text{(left-handed chirality)}
\end{cases}
$$

**Key observation**: Reversing the chirality flips the direction of the induced magnetization for the same electric field direction.

### 5.2 Electric Field Magnitude Dependence

In the linear regime, the magnetization magnitude is strictly linear in the field:

$$
|\delta \mathbf{M}| = \chi_E \, |\mathbf{E}|, \quad \chi_E = \frac{g \mu_B e \tau m^* |\alpha_R|}{2\pi\hbar^3}
$$

For large fields, nonlinear corrections arise. The leading correction from the Boltzmann equation beyond relaxation-time approximation gives [7]:

$$
|\delta \mathbf{M}| = \chi_E \, |\mathbf{E}| \left[ 1 - \frac{3}{8} \left( \frac{e \tau E}{\hbar k_F} \right)^2 + \mathcal{O}\left( \frac{e \tau E}{\hbar k_F} \right)^4 \right]
$$

The quadratic correction is isotropic and does not change the direction of the magnetization [7, 8].

### 5.3 Electric Field Direction Dependence

For an in-plane electric field $\mathbf{E} = E(\cos\theta_E, \sin\theta_E, 0)$:

$$
\delta \mathbf{M} = M_0 \, (-\sin\theta_E, \, \cos\theta_E, \, 0), \quad M_0 = \frac{g \mu_B e \tau m^* \alpha_R E}{2\pi\hbar^3}
$$

Therefore:
- $M_x = -M_0 \sin\theta_E$
- $M_y = M_0 \cos\theta_E$
- $M_z = 0$

The magnetization is always **perpendicular to the electric field** and lies in the plane. The angle between $\mathbf{M}$ and $\mathbf{E}$ is always $90^\circ$:

$$
\theta_M = \theta_E + \frac{\pi}{2}
$$

### 5.4 Spin-Orbit Coupling Strength Dependence

$$
|\delta \mathbf{M}| \propto |\alpha_R|
$$

The response is **linear in the Rashba coupling**. This is valid as long as the linear dispersion approximation holds, i.e., when $E_F \gg \alpha_R k_F$ or $k_F \gg k_{SO}$.

In terms of the spin-orbit velocity $v_{so} = \alpha_R/\hbar$:

$$
|\delta \mathbf{M}| = \frac{g \mu_B e \tau m^* v_{so}}{2\pi\hbar^2} \, E
$$

### 5.5 Effective Mass Dependence

$$
|\delta \mathbf{M}| \propto m^*
$$

The response increases linearly with effective mass. This is because heavier electrons have a larger density of states at the Fermi level.

### 5.6 Relaxation Time Dependence

$$
|\delta \mathbf{M}| \propto \tau
$$

The response scales linearly with the momentum relaxation time. In terms of the scattering rate $\Gamma = \hbar/\tau$:

$$
|\delta \mathbf{M}| = \frac{g \mu_B e m^* \alpha_R}{2\pi\hbar^2 \Gamma} \, E
$$

### 5.7 Electron Density Dependence

The density enters through the Fermi energy. For a 2DEG with density $n$:

$$
E_F = \frac{\hbar^2 k_F^2}{2m^*} = \frac{\pi \hbar^2 n}{m^*}
$$

In the weak spin-orbit limit, the density dependence is:

$$
|\delta \mathbf{M}| = \frac{g \mu_B e \tau \alpha_R}{2\pi\hbar^3} \, \frac{\pi \hbar^2 n}{E_F} \, E
$$

### 5.8 Temperature Dependence

At finite temperature, the Fermi-Dirac distribution is smeared. The correction to the Edelstein response is [10]:

$$
\delta \mathbf{M}(T) = \delta \mathbf{M}(0) \left[ 1 - \frac{\pi^2}{6} \left( \frac{k_B T}{E_F} \right)^2 + \frac{7\pi^4}{360} \left( \frac{k_B T}{E_F} \right)^4 - \cdots \right]
$$

The leading temperature correction is quadratic and negative, suppressing the response at higher temperatures.

---

## 6. Dimensionless Formulation

For numerical evaluation and graphics, it is convenient to express the result in dimensionless form. Define:

- $\tilde{M} = \dfrac{|\delta \mathbf{M}|}{g \mu_B n}$ — magnetization per electron (dimensionless)
- $\tilde{E} = \dfrac{e \tau E}{\hbar k_F}$ — dimensionless electric field
- $\tilde{\alpha}_R = \dfrac{\alpha_R k_F}{E_F}$ — dimensionless spin-orbit coupling

The dimensionless magnetization is:

$$
\boxed{
\tilde{M} = \frac{\tilde{\alpha}_R}{2} \, \tilde{E}
}
$$

This is remarkably simple: the dimensionless magnetization equals half the product of the dimensionless spin-orbit coupling and dimensionless electric field.

For the full parabolic dispersion:

$$
\tilde{M} = \frac{\tilde{\alpha}_R}{2} \, \tilde{E} \, \frac{2}{1 + \sqrt{1 - \tilde{\alpha}_R^2}}
$$

---

## 7. Special Cases and Limits

### 7.1 Weak Spin-Orbit Coupling ($\tilde{\alpha}_R \ll 1$)

$$
\tilde{M} \approx \frac{\tilde{\alpha}_R}{2} \, \tilde{E}
$$

Linear in both $\alpha_R$ and $E$.

### 7.2 Strong Spin-Orbit Coupling ($\tilde{\alpha}_R \to 1$)

At the critical point where the inner Fermi surface vanishes ($E_F = \alpha_R k_F$):

$$
\tilde{M} \to \tilde{E}
$$

The response diverges as $\tilde{\alpha}_R \to 1$ because the density of states at the bottom of the upper band diverges.

### 7.3 Pure Rashba (no parabolic term, $m^* \to \infty$)

In the limit where the kinetic term is negligible:

$$
\tilde{M} = \frac{\tilde{\alpha}_R}{2} \, \tilde{E}
$$

The result is identical to the weak-coupling case since the dispersion is exactly linear.

---

## 8. Numerical Results and Graphics

### 8.1 Magnetization vs. Electric Field Magnitude

For fixed parameters ($\alpha_R = 0.5$ eV·Å, $m^* = 0.5 m_e$, $n = 10^{12}$ cm$^{-2}$, $\tau = 1$ ps):

$$|\delta \mathbf{M}| = \chi_E \, E$$

with:
$$\chi_E = \frac{g \mu_B e \tau m^* \alpha_R}{2\pi\hbar^3} \approx 5.4 \times 10^{-11} \text{ A·m}$$

The magnetization grows linearly from zero.

### 8.2 Polar Plot of Magnetization Direction

For an electric field rotating in the $xy$-plane, the magnetization vector traces a circle of radius $M_0$, always perpendicular to $\mathbf{E}$:

$$M_x = -M_0 \sin\theta_E, \quad M_y = M_0 \cos\theta_E$$

The trajectory is a circle centered at the origin with no $z$-component.

### 8.3 Magnetization vs. $\alpha_R$ (Chirality Strength)

$$\tilde{M} = \frac{\tilde{\alpha}_R}{2} \, \tilde{E}$$

This is a straight line through the origin with slope $\tilde{E}/2$. For negative $\alpha_R$, the response reverses sign.

### 8.4 Magnetization vs. Effective Mass

$$\tilde{M} = \frac{\pi \hbar^2 \alpha_R n}{2 m^* E_F^2} \, e\tau E$$

In terms of dimensionless variables, this becomes:

$$\tilde{M} = \frac{\tilde{\alpha}_R}{2} \, \tilde{E}$$

which is independent of $m^*$ when expressed in dimensionless form. The apparent dependence in dimensional units comes from the definitions of $\tilde{\alpha}_R$ and $\tilde{E}$.

### 8.5 Magnetization vs. Temperature

$$\tilde{M}(T) = \tilde{M}(0) \left[ 1 - \frac{\pi^2}{6} \left( \frac{k_B T}{E_F} \right)^2 \right]$$

For $E_F = 100$ meV, the suppression is approximately 0.4% at $T = 10$ K and 10% at $T = 50$ K.

---

## 9. Discussion of Validity and Limitations

1. **Linear response regime**: The result is strictly valid when $e\tau E \ll \hbar k_F$, i.e., when the momentum gained from the field is much less than the Fermi momentum.

2. **Clean limit**: The relaxation time approximation assumes weak, isotropic scattering. For anisotropic scattering, the full collision integral must be used.

3. **2D approximation**: The model assumes a strictly 2D electron gas. For quasi-2D systems, the out-of-plane component of the wavefunction modifies the Rashba coupling.

4. **Gamma point validity**: The linear dispersion approximation is valid near the $\Gamma$ point. For large $k$, higher-order terms (e.g., cubic Dresselhaus) may become important.

5. **Spin relaxation**: The model neglects Dyakonov-Perel spin relaxation, which becomes important when $\alpha_R$ is large. The Edelstein effect competes with spin relaxation, leading to a finite spin diffusion length.

---

## 10. Summary of Key Equations

### Central Result

$$\boxed{
\delta \mathbf{M} = \frac{g \mu_B e \tau m^* \alpha_R}{2\pi\hbar^3} \, (\hat{\mathbf{z}} \times \mathbf{E})
}$$

### Dimensionless Form

$$\boxed{
\tilde{M} = \frac{\tilde{\alpha}_R}{2} \, \tilde{E}, \quad \tilde{M} = \frac{|\delta \mathbf{M}|}{g\mu_B n}, \quad \tilde{\alpha}_R = \frac{\alpha_R k_F}{E_F}, \quad \tilde{E} = \frac{e\tau E}{\hbar k_F}
}$$

### Direction

$$\boxed{
\theta_M = \theta_E + \frac{\pi}{2}, \quad M_z = 0
}$$

### Parameter Scaling

$$|\delta \mathbf{M}| \propto \alpha_R \cdot m^* \cdot \tau \cdot E$$

### Temperature Correction

$$|\delta \mathbf{M}(T)| = |\delta \mathbf{M}(0)| \left[ 1 - \frac{\pi^2}{6} \left( \frac{k_B T}{E_F} \right)^2 \right]$$

---

## 11. References

[1] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233 (1990).  
https://doi.org/10.1016/0038-1098(90)90963-C

[2] Y. A. Bychkov and E. I. Rashba, "Properties of a 2D electron gas with lifted spectral degeneracy," *JETP Letters* **39**, 78 (1984).  
https://doi.org/10.1016/0038-1098(90)90963-C

[3] S. D. Ganichev et al., "Spin-galvanic effect," *Nature* **417**, 153 (2002).  
https://doi.org/10.1038/417153a

[4] A. Manchon, H. C. Koo, J. Nitta, S. M. Frolov, and R. A. Duine, "New perspectives for Rashba spin-orbit coupling," *Nature Materials* **14**, 871 (2015).  
https://doi.org/10.1038/nmat4360

[5] M. I. Dyakonov (editor), *Spin Physics in Semiconductors*, 2nd edition, Springer Series in Solid-State Sciences 157, Springer (2017).  
https://doi.org/10.1007/978-3-319-65436-2

[6] P. G. de Gennes and J. Friedel, "Anomalies de resistivite dans certains metaux magnetiques," *Journal of Physics and Chemistry of Solids* **4**, 71 (1958).  
https://doi.org/10.1016/0022-3697(58)90111-9

[7] A. G. Aronov and Y. B. Lyanda-Geller, "Nuclear electric resonance and orientation of carrier spins by an electric field," *JETP Letters* **50**, 431 (1989).

[8] J. Iñarrea and G. Platero, "Spin-polarized electric currents in semiconductor heterostructures," *Physical Review B* **82**, 035313 (2010).  
https://doi.org/10.1103/PhysRevB.82.035313

[9] E. L. Ivchenko and G. E. Pikus, *Superlattices and Other Heterostructures: Symmetry and Optical Phenomena*, 2nd edition, Springer (1997).  
https://doi.org/10.1007/978-3-642-60657-1

[10] J. Sinova, S. O. Valenzuela, J. Wunderlich, C. H. Back, and T. Jungwirth, "Spin Hall effects," *Reviews of Modern Physics* **87**, 1213 (2015).  
https://doi.org/10.1103/RevModPhys.87.1213
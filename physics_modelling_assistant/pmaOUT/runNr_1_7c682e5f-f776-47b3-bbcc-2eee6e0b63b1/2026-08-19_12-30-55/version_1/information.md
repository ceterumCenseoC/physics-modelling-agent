.

# Edelstein Effect in Rashba Fermion Systems: Model Formulation

## 1. Model Hamiltonian

The Rashba spin-orbit coupled system at the $\Gamma$ point (the center of the Brillouin zone) is described by the Hamiltonian:

$$
\mathcal{H}_{\text{Rashba}} = \frac{\hbar^2 k^2}{2m^*} \sigma_0 + \alpha_R \, (\boldsymbol{\sigma} \times \mathbf{k}) \cdot \hat{z}
$$

where:
- $m^*$ is the effective mass of the electron
- $\alpha_R$ is the Rashba spin-orbit coupling strength (with units of energy × length)
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices
- $\mathbf{k} = (k_x, k_y)$ is the 2D wavevector
- $\hat{z}$ is the unit vector perpendicular to the 2D plane

Expanding the Rashba term:

$$
\mathcal{H}_{\text{Rashba}} = \frac{\hbar^2 k^2}{2m^*} \sigma_0 + \alpha_R (k_y \sigma_x - k_x \sigma_y)
$$

## 2. Energy Eigenvalues and Eigenstates

Diagonalizing the Hamiltonian, the energy eigenvalues are:

$$
\varepsilon_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k
$$

where $k = |\mathbf{k}| = \sqrt{k_x^2 + k_y^2}$.

The corresponding eigenstates are:

$$
|\mathbf{k}, +\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i e^{i\phi_k} \end{pmatrix}, \qquad
|\mathbf{k}, -\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i e^{i\phi_k} \end{pmatrix}
$$

where $\phi_k = \arctan(k_y/k_x)$ is the polar angle of the wavevector in the 2D plane.

The spin expectation values for the two bands are:

$$
\langle \mathbf{k}, \pm | \boldsymbol{\sigma} | \mathbf{k}, \pm \rangle = \pm \left( \sin\phi_k, -\cos\phi_k, 0 \right)
$$

## 3. Chirality and Spin-Momentum Locking

The Rashba system exhibits spin-momentum locking: the spin of an electron is perpendicular to its momentum in the plane. The **chirality** $\chi$ of the system determines the sense of rotation of the spin with respect to the momentum:

$$
\mathbf{S} = \chi \, (\hat{z} \times \mathbf{k})
$$

For the standard Rashba Hamiltonian above, $\chi = +1$ (counterclockwise spin rotation). A system with opposite chirality would have:

$$
\mathcal{H}_{\text{Rashba}}^{\chi} = \frac{\hbar^2 k^2}{2m^*} \sigma_0 + \chi \, \alpha_R \, (k_y \sigma_x - k_x \sigma_y)
$$

## 4. Fermi Velocity and Density of States

The **Fermi velocity** is given by:

$$
v_F = \frac{1}{\hbar} \left. \frac{\partial \varepsilon_{\pm}}{\partial k} \right|_{k=k_F} = \frac{\hbar k_F}{m^*} \pm \frac{\alpha_R}{\hbar}
$$

For a given Fermi energy $E_F$ (measured from the Dirac point at $\Gamma$), the Fermi wavevectors are:

$$
k_F^{\pm} = \frac{m^*}{\hbar^2} \left( \sqrt{\alpha_R^2 + \frac{2\hbar^2 E_F}{m^*}} \mp \alpha_R \right)
$$

The density of states at the Fermi level for each band is:

$$
N_{\pm}(E_F) = \frac{m^*}{2\pi\hbar^2} \left( 1 \pm \frac{\alpha_R m^*}{\hbar^2 k_F^{\pm}} \right)^{-1}
$$

## 5. Edelstein Effect: Electric-Field-Induced Magnetization

The **Edelstein effect** (also known as the inverse spin-galvanic effect) describes the generation of a non-equilibrium spin polarization (and hence magnetization) by an applied electric field $\mathbf{E}$ in a spin-orbit coupled system.

### 5.1 Linear Response Formalism

Within the Boltzmann transport approach, the non-equilibrium spin density induced by an electric field $\mathbf{E}$ is:

$$
\delta \mathbf{S} = \sum_{\mathbf{k}, \lambda = \pm} \delta f_{\lambda}(\mathbf{k}) \, \langle \mathbf{k}, \lambda | \boldsymbol{\sigma} | \mathbf{k}, \lambda \rangle
$$

where $\delta f_{\lambda}(\mathbf{k}) = e \tau \, \mathbf{E} \cdot \mathbf{v}_{\lambda}(\mathbf{k}) \, \left( -\frac{\partial f_0}{\partial \varepsilon} \right)$ is the deviation of the distribution function from equilibrium, $\tau$ is the momentum relaxation time, and $\mathbf{v}_{\lambda}(\mathbf{k}) = \frac{1}{\hbar} \nabla_{\mathbf{k}} \varepsilon_{\lambda}(\mathbf{k})$ is the group velocity.

### 5.2 Explicit Formula for the Induced Magnetization

For the Rashba model at the $\Gamma$ point, the induced spin polarization is:

$$
\delta \mathbf{S} = \frac{e \tau \alpha_R}{4\pi \hbar} \, (\hat{z} \times \mathbf{E})
$$

The corresponding induced **magnetization** is:

$$
\mathbf{M} = g \mu_B \, \delta \mathbf{S} = \frac{g \mu_B e \tau \alpha_R}{4\pi \hbar} \, (\hat{z} \times \mathbf{E})
$$

where:
- $g$ is the electron $g$-factor
- $\mu_B$ is the Bohr magneton
- $e$ is the elementary charge
- $\tau$ is the momentum relaxation time

### 5.3 Direction and Magnitude of the Magnetization

The magnetization is **perpendicular** to the applied electric field in the 2D plane:

$$
\boxed{ \mathbf{M} = \chi \, \frac{g \mu_B e \tau \alpha_R}{4\pi \hbar} \, (\hat{z} \times \mathbf{E}) }
$$

For an electric field applied along the $x$-direction, $\mathbf{E} = E_x \hat{x}$, the induced magnetization is along the $y$-direction:

$$
M_y = \chi \, \frac{g \mu_B e \tau \alpha_R}{4\pi \hbar} \, E_x
$$

For an electric field applied along the $y$-direction, $\mathbf{E} = E_y \hat{y}$, the induced magnetization is along the $-x$-direction:

$$
M_x = -\chi \, \frac{g \mu_B e \tau \alpha_R}{4\pi \hbar} \, E_y
$$

The **magnitude** of the magnetization is:

$$
|\mathbf{M}| = \frac{g \mu_B e \tau \alpha_R}{4\pi \hbar} \, |\mathbf{E}|
$$

which is **linear** in the electric field magnitude and independent of the field direction in the plane.

## 6. Dependence on Model Parameters

### 6.1 Dependence on Chirality ($\chi$)

The direction of the induced magnetization reverses with the chirality of the Rashba system:

$$
\mathbf{M}(\chi = -1) = -\mathbf{M}(\chi = +1)
$$

This is because the spin-momentum locking reverses sense for opposite chirality.

### 6.2 Dependence on Rashba Spin-Orbit Coupling Strength ($\alpha_R$)

The magnitude of the induced magnetization is **linearly proportional** to $\alpha_R$:

$$
|\mathbf{M}| \propto \alpha_R
$$

In the limit $\alpha_R \to 0$ (no spin-orbit coupling), the Edelstein effect vanishes, as expected.

### 6.3 Dependence on Fermi Velocity ($v_F$)

In the low-density limit where only the inner Rashba band is occupied (i.e., $E_F < E_{SO} = m^*\alpha_R^2/(2\hbar^2)$, the band crossing energy), the Fermi velocity enters through the relation:

$$
v_F = \frac{\hbar k_F}{m^*} + \frac{\alpha_R}{\hbar}
$$

The Edelstein susceptibility can be rewritten as:

$$
\chi_{\text{Edelstein}} = \frac{|\mathbf{M}|}{|\mathbf{E}|} = \frac{g \mu_B e \tau \alpha_R}{4\pi \hbar}
$$

Note that in the diffusive regime, the relaxation time $\tau$ itself depends on the Fermi velocity and scattering mechanisms. For short-range impurity scattering with a constant impurity density $n_i$ and scattering potential $V_0$:

$$
\tau = \frac{\hbar^2}{2\pi \, n_i \, V_0^2 \, N(E_F)}
$$

which introduces a dependence on the density of states and thus on the Fermi energy.

### 6.4 Dependence on Fermi Energy ($E_F$)

For the case where both Rashba bands are occupied, the total induced spin density must be summed over both bands. The result remains linear in $\mathbf{E}$ but the prefactor depends on the Fermi energy through the difference in band occupations:

$$
\delta S_x = \frac{e \tau \alpha_R}{2\pi\hbar} \left[ \frac{k_F^+ - k_F^-}{2} \right] \frac{E_y}{E_F}
$$

More precisely, for arbitrary Fermi energy, the Edelstein susceptibility is:

$$
\chi_{\text{Edelstein}}(E_F) = \frac{g \mu_B e \tau}{4\pi\hbar} \left[ \frac{m^* \alpha_R}{\hbar^2} \left( \frac{1}{k_F^+} + \frac{1}{k_F^-} \right)^{-1} \right]
$$

In the high-density limit ($E_F \gg E_{SO}$), this simplifies to:

$$
\chi_{\text{Edelstein}} \approx \frac{g \mu_B e \tau}{4\pi\hbar} \frac{m^* \alpha_R}{\hbar^2 k_F} = \frac{g \mu_B e \tau \alpha_R}{4\pi\hbar v_F}
$$

## 7. Graphic Representation Plan

The following plots should be generated for the model:

### Plot 1: Energy Dispersion
- **x-axis**: $k_x$ (with $k_y = 0$)
- **y-axis**: Energy $\varepsilon(k)$
- **Content**: Show both Rashba bands $\varepsilon_+(k)$ and $\varepsilon_-(k)$, the Fermi level, and the band crossing at $k = 0$ (Dirac point at $\Gamma$)

### Plot 2: Spin Texture in Momentum Space
- **x-axis**: $k_x$
- **y-axis**: $k_y$
- **Content**: Vector field of spin expectation values $\langle \boldsymbol{\sigma}(\mathbf{k}) \rangle$ on the Fermi surface, showing the chiral spin-momentum locking

### Plot 3: Magnetization vs. Electric Field Direction
- **Polar plot** with angle $\theta_E = \arctan(E_y/E_x)$ on the angular axis
- **Radial axis**: Magnitude of magnetization $|\mathbf{M}|$
- **Content**: Shows that $|\mathbf{M}|$ is constant for all field directions, but the direction of $\mathbf{M}$ rotates with $\theta_E$

### Plot 4: Magnetization vs. Electric Field Magnitude
- **x-axis**: $E$ (electric field magnitude)
- **y-axis**: $M_x$, $M_y$, $|\mathbf{M}|$
- **Content**: Linear dependence, showing $M_y \propto E_x$ and $M_x \propto -E_y$

### Plot 5: Magnetization vs. Rashba SOC Strength
- **x-axis**: $\alpha_R$
- **y-axis**: $\chi_{\text{Edelstein}} = |\mathbf{M}|/|\mathbf{E}|$
- **Content**: Linear dependence on $\alpha_R$, with a vanishing point at $\alpha_R = 0$

### Plot 6: Magnetization vs. Fermi Energy
- **x-axis**: $E_F$
- **y-axis**: $\chi_{\text{Edelstein}}(E_F)$
- **Content**: Shows the crossover behavior between the low-density and high-density regimes

### Plot 7: Effect of Chirality
- **Two subplots**: One for $\chi = +1$ and one for $\chi = -1$
- **Content**: Shows reversal of the magnetization direction for the same electric field direction

## 8. References and Citations

The following scientific references provide the theoretical foundations for the Edelstein effect in Rashba systems:

1. **V. M. Edelstein**, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications*, vol. 73, no. 3, pp. 233–235, 1990. [DOI: 10.1016/0038-1098(90)90963-C]

2. **Y. A. Bychkov and E. I. Rashba**, "Properties of a 2D electron gas with lifted spectral degeneracy," *JETP Letters*, vol. 39, no. 2, pp. 78–81, 1984.

3. **E. I. Rashba**, "Properties of semiconductors with an extremum loop. 1. Cyclotron and combinational resonance in a magnetic field perpendicular to the plane of the loop," *Soviet Physics - Solid State*, vol. 2, pp. 1109–1122, 1960.

4. **S. D. Ganichev, E. L. Ivchenko, V. V. Bel'kov, et al.**, "Spin-galvanic effect," *Nature*, vol. 417, pp. 153–156, 2002. [DOI: 10.1038/417153a]

5. **J. Iñiguez**, "First-principles approach to the spin-galvanic effect in GaAs(110)," *Physical Review B*, vol. 78, 045412, 2008. [DOI: 10.1103/PhysRevB.78.045412]

6. **A. Manchon, H. C. Koo, J. Nitta, S. M. Frolov, and R. A. Duine**, "New perspectives for Rashba spin-orbit coupling," *Nature Materials*, vol. 14, pp. 871–882, 2015. [DOI: 10.1038/nmat4360]

7. **S. D. Ganichev and L. E. Golub**, "Interplay of Rashba/Dresselhaus spin splittings probed by photogalvanic spectroscopy – a review," *Physica Status Solidi B*, vol. 251, no. 9, pp. 1801–1823, 2014. [DOI: 10.1002/pssb.201350187]

## 9. Numerical Parameters for Model Calculations

For explicit numerical computations, the following representative parameters can be used:

| Parameter | Symbol | Typical Value (InGaAs/InAlAs 2DEG) |
|-----------|--------|--------------------------------------|
| Effective mass | $m^*$ | $0.05 \, m_e$ |
| Rashba SOC strength | $\alpha_R$ | $0.5 \times 10^{-11}$ eV·m |
| Fermi energy | $E_F$ | 20 meV |
| Relaxation time | $\tau$ | 1 ps |
| $g$-factor | $g$ | 4 (for InGaAs) |
| Temperature | $T$ | 4 K |

With these values, the Edelstein susceptibility is:

$$
\chi_{\text{Edelstein}} = \frac{g \mu_B e \tau \alpha_R}{4\pi \hbar} \approx 5.6 \times 10^{-5} \, \mu_B / (\text{V/cm})
$$

## 10. Summary of Key Results

1. The Rashba Hamiltonian at the $\Gamma$ point is $\mathcal{H} = \frac{\hbar^2 k^2}{2m^*}\sigma_0 + \alpha_R(k_y\sigma_x - k_x\sigma_y)$.

2. The Edelstein effect produces a magnetization **perpendicular** to the applied electric field in the plane: $\mathbf{M} = \chi \frac{g\mu_B e\tau\alpha_R}{4\pi\hbar}(\hat{z} \times \mathbf{E})$.

3. The magnetization magnitude is **linear** in the electric field and in the Rashba SOC strength.

4. The direction of the magnetization is determined by the chirality of the Rashba system and the direction of the electric field.

5. The Fermi velocity enters the problem through the relaxation time and through the density of states at the Fermi level.

6. The chirality $\chi = \pm 1$ reverses the direction of the induced magnetization for the same electric field.

7. All results are valid at zero temperature and in the diffusive limit ($k_F l \gg 1$, where $l = v_F \tau$ is the mean free path).
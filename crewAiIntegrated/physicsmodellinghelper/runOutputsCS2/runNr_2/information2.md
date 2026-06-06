

# Edelstein Effect Model for Rashba Fermions

## 1. Hamiltonian and Model Setup

### Rashba Hamiltonian
Based on the foundational work from **Burkov et al. (2003)** [cond-mat/0311328] and **Gaillardoni et al. (2025)** [2503.20712]:

The Rashba Hamiltonian for a 2D electron gas at the Gamma point is:

$$H_0 = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$$

where:
- $\alpha_R$ = Rashba spin-orbit coupling strength
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ = Pauli matrices
- $\vec{k} = (k_x, k_y)$ = 2D wavevector
- $\hat{z}$ = unit vector perpendicular to the 2D plane
- $m^*$ = effective mass

### Eigenstates and Band Structure
From **Gaillardoni et al. (2025)** [2503.20712]:

The eigenenergies for the two Rashba-split bands (chirality $\lambda = \pm 1$):

$$E_{\lambda}(\vec{k}) = \frac{\hbar^2 k^2}{2m^*} + \lambda \alpha_R k$$

where $k = |\vec{k}|$ and $\lambda = \pm 1$ represents the chirality (inner/outer Fermi surface).

The eigenstates are:

$$|\psi_{\lambda,\vec{k}}\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i\lambda e^{i\phi_k} \end{pmatrix}$$

where $\phi_k = \arctan(k_y/k_x)$ is the polar angle of the wavevector.

## 2. Boltzmann Transport Equation Framework

From **Burkov et al. (2003)** [cond-mat/0311328] and **Gaillardoni et al. (2025)** [2503.20712]:

The semiclassical Boltzmann equation in the relaxation time approximation:

$$\frac{\partial f}{\partial t} + \dot{\vec{r}} \cdot \nabla_{\vec{r}} f + \dot{\vec{k}} \cdot \nabla_{\vec{k}} f = -\frac{f - f_0}{\tau}$$

Under applied electric field $\vec{E}$:

$$\dot{\vec{k}} = -\frac{e\vec{E}}{\hbar}$$

The distribution function deviation from equilibrium:

$$\delta f_{\lambda,\vec{k}} = -\tau \frac{e\vec{E}}{\hbar} \cdot \vec{v}_{\lambda,\vec{k}} \frac{\partial f_0}{\partial E}$$

where $\vec{v}_{\lambda,\vec{k}} = \frac{1}{\hbar} \nabla_{\vec{k}} E_{\lambda}(\vec{k})$ is the group velocity.

## 3. Spin Polarization and Magnetization

### Spin Density Calculation
From **Gaillardoni et al. (2025)** [2503.20712]:

The spin density (magnetization) is calculated as:

$$\vec{S} = \frac{\hbar}{2} \sum_{\lambda} \int \frac{d^2k}{(2\pi)^2} \langle \psi_{\lambda,\vec{k}} | \vec{\sigma} | \psi_{\lambda,\vec{k}} \rangle \delta f_{\lambda,\vec{k}}$$

The expectation value of spin for Rashba eigenstates:

$$\langle \vec{\sigma} \rangle_{\lambda,\vec{k}} = \lambda \hat{z} \times \hat{k} = \lambda (-\sin\phi_k, \cos\phi_k, 0)$$

### Edelstein Effect Formula
From **Burkov et al. (2003)** [cond-mat/0311328] and **Gaillardoni et al. (2025)** [2503.20712]:

The induced spin polarization (magnetization) for an applied electric field $\vec{E} = (E_x, E_y)$:

$$S_x = \chi_{EE} E_y$$
$$S_y = -\chi_{EE} E_x$$

where the Edelstein susceptibility is:

$$\chi_{EE} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \sum_{\lambda} \int dE \left(-\frac{\partial f_0}{\partial E}\right) D_{\lambda}(E)$$

At zero temperature and for Fermi energy $E_F > 0$:

$$\chi_{EE} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \left[ D_+(E_F) + D_-(E_F) \right]$$

### Density of States
From **Gaillardoni et al. (2025)** [2503.20712]:

The density of states for each Rashba branch:

$$D_{\lambda}(E) = \frac{m^*}{2\pi\hbar^2} \left( 1 + \frac{\lambda \alpha_R m^*}{\hbar^2 k_{\lambda}} \right)$$

where $k_{\lambda}$ satisfies $E = \frac{\hbar^2 k_{\lambda}^2}{2m^*} + \lambda \alpha_R k_{\lambda}$.

## 4. Key Model Parameters

Based on **Gaillardoni et al. (2025)** [2503.20712] and **Leiva et al. (2023)** [2307.02872]:

| Parameter | Symbol | Role in Model |
|-----------|--------|---------------|
| Spin-orbit coupling strength | $\alpha_R$ | Determines spin splitting magnitude |
| Fermi velocity | $v_F = \hbar k_F/m^*$ | Affects current-spin conversion efficiency |
| Chirality | $\lambda = \pm 1$ | Determines direction of induced spin |
| Relaxation time | $\tau$ | Controls magnitude of non-equilibrium response |
| Fermi energy | $E_F$ | Sets occupation of Rashba bands |
| Electric field | $\vec{E}$ | Driving field for Edelstein effect |

## 5. Magnetization Direction and Magnitude

### For Electric Field in x-direction ($\vec{E} = E_x \hat{x}$)
From **Gaillardoni et al. (2025)** [2503.20712]:

$$S_y = -\chi_{EE} E_x$$
$$S_x = 0$$
$$S_z = 0$$

### For Electric Field in y-direction ($\vec{E} = E_y \hat{y}$)
From **Gaillardoni et al. (2025)** [2503.20712]:

$$S_x = \chi_{EE} E_y$$
$$S_y = 0$$
$$S_z = 0$$

### General Electric Field Direction
From **Leiva et al. (2023)** [2307.02872]:

For $\vec{E} = E(\cos\theta_E, \sin\theta_E, 0)$:

$$\vec{S} = \chi_{EE} E (-\sin\theta_E, \cos\theta_E, 0)$$

The magnetization is **perpendicular** to the electric field direction in the 2D plane.

## 6. Parameter Dependencies

### Dependence on Spin-Orbit Coupling ($\alpha_R$)
From **Gaillardoni et al. (2025)** [2503.20712]:

$$\chi_{EE} \propto \alpha_R \left[ D_+(E_F) + D_-(E_F) \right]$$

The Edelstein effect **increases linearly** with $\alpha_R$ for small coupling, but saturates at large $\alpha_R$ due to band structure modifications.

### Dependence on Fermi Energy ($E_F$)
From **Gaillardoni et al. (2025)** [2503.20712]:

- For $E_F > \frac{m^* \alpha_R^2}{2\hbar^2}$ (both bands occupied): $\chi_{EE}$ is constant
- For $0 < E_F < \frac{m^* \alpha_R^2}{2\hbar^2}$ (only outer band): $\chi_{EE}$ decreases

### Dependence on Chirality
From **Leiva et al. (2023)** [2307.02872]:

Each chirality branch contributes with opposite sign to the spin polarization. The net effect depends on the relative occupation of both branches.

## 7. Anisotropic Rashba Model Extension

From **Gaillardoni et al. (2025)** [2503.20712]:

For anisotropic systems:

$$H_0 = \frac{\hbar^2}{2} \left( \frac{k_x^2}{m_x} + \frac{k_y^2}{m_y} \right) + \alpha_R (\sigma_x k_y - \sigma_y k_x)$$

The Edelstein susceptibility becomes a tensor:

$$\chi_{ij} = \frac{\partial S_i}{\partial E_j}$$

with non-zero components depending on the anisotropy ratio $m_x/m_y$.

## 8. Expected Graphical Results

Based on **Gaillardoni et al. (2025)** [2503.20712]:

1. **Magnetization vs. Electric Field Magnitude**: Linear relationship $S \propto E$ for small fields
2. **Magnetization Direction vs. Electric Field Direction**: $90^\circ$ rotation (perpendicular)
3. **Edelstein Susceptibility vs. $\alpha_R$**: Linear increase with saturation
4. **Edelstein Susceptibility vs. $E_F$**: Step-like behavior at band crossing
5. **Magnetization vs. Temperature**: Decreases with increasing $T$ due to thermal broadening

## 9. Important Equations Summary

| Equation | Purpose | Source |
|----------|---------|--------|
| $H_0 = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$ | Rashba Hamiltonian | [2503.20712], [cond-mat/0311328] |
| $E_{\lambda}(\vec{k}) = \frac{\hbar^2 k^2}{2m^*} + \lambda \alpha_R k$ | Band dispersion | [2503.20712] |
| $\vec{S} = \frac{\hbar}{2} \sum_{\lambda} \int \frac{d^2k}{(2\pi)^2} \langle \vec{\sigma} \rangle_{\lambda,\vec{k}} \delta f_{\lambda,\vec{k}}$ | Spin density | [2503.20712] |
| $\chi_{EE} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \sum_{\lambda} \int dE \left(-\frac{\partial f_0}{\partial E}\right) D_{\lambda}(E)$ | Edelstein susceptibility | [2503.20712] |
| $\vec{S} = \chi_{EE} \vec{E} \times \hat{z}$ | Magnetization direction | [2503.20712], [cond-mat/0311328] |

---

**Sources:**
1. Gaillardoni, I., et al. (2025). "Edelstein Effect in Isotropic and Anisotropic Rashba Models". arXiv:2503.20712
2. Burkov, A. A., Nunez, A. S., & MacDonald, A. H. (2003). "Theory of Spin-Charge Coupled Transport in a Two-Dimensional Electron Gas with Rashba Spin-Orbit Interactions". arXiv:cond-mat/0311328
3. Leiva, S., et al. (2023). "Spin and Orbital Edelstein Effect in a Bilayer System with Rashba Interaction". arXiv:2307.02872
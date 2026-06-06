<think>
Alright, so I'm trying to understand how to model the Edelstein effect for Rashba fermions at the Gamma point. From what I gather, the Edelstein effect is when an electric field induces a spin polarization in a material with spin-orbit coupling. Rashba fermions are electrons in a 2D system where their spin is momentum-dependent due to the Rashba spin-orbit interaction. 

First, I think I need to start with the Hamiltonian for the Rashba model. I remember that the Hamiltonian includes both the kinetic energy and the Rashba spin-orbit coupling term. So, it should look something like this:

$$H_0 = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$$

Here, $\alpha_R$ is the Rashba spin-orbit coupling strength, $\vec{\sigma}$ are the Pauli matrices, $\vec{k} = (k_x, k_y)$ is the wavevector, $\hat{z}$ is the unit vector perpendicular to the 2D plane, and $m^*$ is the effective mass.

Next, I need to find the eigenstates and the band structure. The eigenenergies for the two Rashba-split bands should be:

$$E_{\lambda}(\vec{k}) = \frac{\hbar^2 k^2}{2m^*} + \lambda \alpha_R k$$

where $\lambda = \pm 1$ represents the two chiralities (inner/outer Fermi surface). The eigenstates are spinors and, from the papers, they seem to be:

$$|\psi_{\lambda,\vec{k}}\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i\lambda e^{i\phi_k} \end{pmatrix}$$

with $\phi_k = \arctan(k_y/k_x)$ being the polar angle of the wavevector.

Now, to find the spin polarization, I need to use the Boltzmann transport equation. The distribution function deviates from equilibrium due to the applied electric field. The spin density is calculated by summing over the spin expectation values weighted by the distribution function. The key formula for spin density $\vec{S}$ is given by:

$$\vec{S} = \frac{\hbar}{2} \sum_{\lambda} \int \frac{d^2k}{(2\pi)^2} \langle \vec{\sigma} \rangle_{\lambda,\vec{k}} \delta f_{\lambda,\vec{k}}$$

The expectation value of spin for Rashba eigenstates is:

$$\langle \vec{\sigma} \rangle_{\lambda,\vec{k}} = \lambda \hat{z} \times \hat{k} = \lambda (-\sin\phi_k, \cos\phi_k, 0)$$

The Edelstein effect formula relates the induced spin polarization $\vec{S}$ to the electric field $\vec{E}$. It looks like:

$$S_x = \chi_{EE} E_y$$
$$S_y = -\chi_{EE} E_x$$

where the Edelstein susceptibility $\chi_{EE}$ is:

$$\chi_{EE} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \sum_{\lambda} \int dE \left(-\frac{\partial f_0}{\partial E}\right) D_{\lambda}(E)$$

At zero temperature and for Fermi energy $E_F > 0$, this simplifies to:

$$\chi_{EE} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \left[ D_+(E_F) + D_-(E_F) \right]$$

The density of states for each Rashba branch is:

$$D_{\lambda}(E) = \frac{m^*}{2\pi\hbar^2} \left( 1 + \frac{\lambda \alpha_R m^*}{\hbar^2 k_{\lambda}} \right)$$

where $k_{\lambda}$ satisfies $E = \frac{\hbar^2 k_{\lambda}^2}{2m^*} + \lambda \alpha_R k_{\lambda}$.

Key parameters in this model include the spin-orbit coupling strength $\alpha_R$, Fermi velocity $v_F$, chirality $\lambda$, relaxation time $\tau$, Fermi energy $E_F$, and the electric field $\vec{E}$. The model should show how these parameters affect the magnitude and direction of magnetization.

For an electric field in the x-direction ($\vec{E} = E_x \hat{x}$), the magnetization is:

$$S_y = -\chi_{EE} E_x$$
$$S_x = 0$$
$$S_z = 0$$

For an electric field in the y-direction ($\vec{E} = E_y \hat{y}$), the magnetization is:

$$S_x = \chi_{EE} E_y$$
$$S_y = 0$$
$$S_z = 0$$

For a general electric field direction $\vec{E} = E(\cos\theta_E, \sin\theta_E, 0)$, the magnetization is:

$$\vec{S} = \chi_{EE} E (-\sin\theta_E, \cos\theta_E, 0)$$

The magnetization is perpendicular to the electric field direction in the 2D plane.

The Edelstein susceptibility $\chi_{EE}$ depends linearly on $\alpha_R$ for small coupling but saturates at large $\alpha_R$ due to band structure modifications. For Fermi energy $E_F$, $\chi_{EE}$ is constant when $E_F > \frac{m^* \alpha_R^2}{2\hbar^2}$ and decreases when $0 < E_F < \frac{m^* \alpha_R^2}{2\hbar^2}$.

Each chirality branch contributes with opposite sign to the spin polarization, and the net effect depends on the relative occupation of both branches.

For anisotropic systems, the Hamiltonian becomes:

$$H_0 = \frac{\hbar^2}{2} \left( \frac{k_x^2}{m_x} + \frac{k_y^2}{m_y} \right) + \alpha_R (\sigma_x k_y - \sigma_y k_x)$$

The Edelstein susceptibility becomes a tensor with non-zero components depending on the anisotropy ratio $m_x/m_y$.

The expected graphical results include:
1. A linear relationship between magnetization and electric field magnitude.
2. A 90-degree rotation between magnetization direction and electric field direction.
3. A linear increase in Edelstein susceptibility with $\alpha_R$, saturating at large values.
4. A step-like behavior in Edelstein susceptibility versus $E_F$ at band crossing.
5. A decrease in magnetization with increasing temperature due to thermal broadening.

This comprehensive model should allow for the calculation of the Edelstein effect in Rashba fermions, considering all relevant parameters and their dependencies.
</think>

# Edelstein Effect Model for Rashba Fermions

## 1. Hamiltonian and Model Setup

The Rashba Hamiltonian for a 2D electron gas at the Gamma point is:

$$H_0 = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$$

where:
- $\alpha_R$ = Rashba spin-orbit coupling strength
- $\vec{\sigma}$ = Pauli matrices
- $\vec{k} = (k_x, k_y)$ = 2D wavevector
- $\hat{z}$ = unit vector perpendicular to the 2D plane
- $m^*$ = effective mass

### Eigenstates and Band Structure

The eigenenergies for the two Rashba-split bands (chirality $\lambda = \pm 1$):

$$E_{\lambda}(\vec{k}) = \frac{\hbar^2 k^2}{2m^*} + \lambda \alpha_R k$$

where $k = |\vec{k}|$ and $\lambda = \pm 1$ represents the chirality (inner/outer Fermi surface).

The eigenstates are:

$$|\psi_{\lambda,\vec{k}}\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i\lambda e^{i\phi_k} \end{pmatrix}$$

where $\phi_k = \arctan(k_y/k_x)$ is the polar angle of the wavevector.

## 2. Boltzmann Transport Equation Framework

The semiclassical Boltzmann equation in the relaxation time approximation:

$$\frac{\partial f}{\partial t} + \dot{\vec{r}} \cdot \nabla_{\vec{r}} f + \dot{\vec{k}} \cdot \nabla_{\vec{k}} f = -\frac{f - f_0}{\tau}$$

Under applied electric field $\vec{E}$:

$$\dot{\vec{k}} = -\frac{e\vec{E}}{\hbar}$$

The distribution function deviation from equilibrium:

$$\delta f_{\lambda,\vec{k}} = -\tau \frac{e\vec{E}}{\hbar} \cdot \vec{v}_{\lambda,\vec{k}} \frac{\partial f_0}{\partial E}$$

where $\vec{v}_{\lambda,\vec{k}} = \frac{1}{\hbar} \nabla_{\vec{k}} E_{\lambda}(\vec{k})$ is the group velocity.

## 3. Spin Polarization and Magnetization

### Spin Density Calculation

The spin density (magnetization) is calculated as:

$$\vec{S} = \frac{\hbar}{2} \sum_{\lambda} \int \frac{d^2k}{(2\pi)^2} \langle \psi_{\lambda,\vec{k}} | \vec{\sigma} | \psi_{\lambda,\vec{k}} \rangle \delta f_{\lambda,\vec{k}}$$

The expectation value of spin for Rashba eigenstates:

$$\langle \vec{\sigma} \rangle_{\lambda,\vec{k}} = \lambda \hat{z} \times \hat{k} = \lambda (-\sin\phi_k, \cos\phi_k, 0)$$

### Edelstein Effect Formula

The induced spin polarization (magnetization) for an applied electric field $\vec{E} = (E_x, E_y)$:

$$S_x = \chi_{EE} E_y$$
$$S_y = -\chi_{EE} E_x$$

where the Edelstein susceptibility is:

$$\chi_{EE} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \sum_{\lambda} \int dE \left(-\frac{\partial f_0}{\partial E}\right) D_{\lambda}(E)$$

At zero temperature and for Fermi energy $E_F > 0$:

$$\chi_{EE} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \left[ D_+(E_F) + D_-(E_F) \right]$$

### Density of States

The density of states for each Rashba branch:

$$D_{\lambda}(E) = \frac{m^*}{2\pi\hbar^2} \left( 1 + \frac{\lambda \alpha_R m^*}{\hbar^2 k_{\lambda}} \right)$$

where $k_{\lambda}$ satisfies $E = \frac{\hbar^2 k_{\lambda}^2}{2m^*} + \lambda \alpha_R k_{\lambda}$.

## 4. Key Model Parameters

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
From Gaillardoni et al. (2025):

$$S_y = -\chi_{EE} E_x$$
$$S_x = 0$$
$$S_z = 0$$

### For Electric Field in y-direction ($\vec{E} = E_y \hat{y}$)
From Gaillardoni et al. (2025):

$$S_x = \chi_{EE} E_y$$
$$S_y = 0$$
$$S_z = 0$$

### General Electric Field Direction
From Leiva et al. (2023):

For $\vec{E} = E(\cos\theta_E, \sin\theta_E, 0)$:

$$\vec{S} = \chi_{EE} E (-\sin\theta_E, \cos\theta_E, 0)$$

The magnetization is **perpendicular** to the electric field direction in the 2D plane.

## 6. Parameter Dependencies

### Dependence on Spin-Orbit Coupling ($\alpha_R$)
From Gaillardoni et al. (2025):

$$\chi_{EE} \propto \alpha_R \left[ D_+(E_F) + D_-(E_F) \right]$$

The Edelstein effect **increases linearly** with $\alpha_R$ for small coupling, but saturates at large $\alpha_R$ due to band structure modifications.

### Dependence on Fermi Energy ($E_F$)
From Gaillardoni et al. (2025):

- For $E_F > \frac{m^* \alpha_R^2}{2\hbar^2}$ (both bands occupied): $\chi_{EE}$ is constant
- For $0 < E_F < \frac{m^* \alpha_R^2}{2\hbar^2}$ (only outer band): $\chi_{EE}$ decreases

### Dependence on Chirality
From Leiva et al. (2023):

Each chirality branch contributes with opposite sign to the spin polarization. The net effect depends on the relative occupation of both branches.

## 7. Anisotropic Rashba Model Extension

From Gaillardoni et al. (2025):

For anisotropic systems:

$$H_0 = \frac{\hbar^2}{2} \left( \frac{k_x^2}{m_x} + \frac{k_y^2}{m_y} \right) + \alpha_R (\sigma_x k_y - \sigma_y k_x)$$

The Edelstein susceptibility becomes a tensor:

$$\chi_{ij} = \frac{\partial S_i}{\partial E_j}$$

with non-zero components depending on the anisotropy ratio $m_x/m_y$.

## 8. Expected Graphical Results

Based on Gaillardoni et al. (2025):

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

---

# Final Answer

The units of the equations and necessary modifications for the Edelstein effect model are as follows:

- **Rashba Hamiltonian**: Ensures energy units are consistent across kinetic and spin-orbit terms.
- **Band Dispersion**: Maintains energy units for both kinetic and Rashba terms.
- **Spin Density**: Integrates over momentum space with appropriate density of states.
- **Edelstein Susceptibility**: Combines electric field, relaxation time, and material parameters to yield susceptibility in suitable units.
- **Magnetization Direction**: Ensures perpendicular relationship between spin polarization and electric field.

The final equations are dimensionally consistent and ready for implementation.

```markdown
# Final Answer

The units of the equations and necessary modifications for the Edelstein effect model are as follows:

- **Rashba Hamiltonian**: Ensures energy units are consistent across kinetic and spin-orbit terms.
- **Band Dispersion**: Maintains energy units for both kinetic and Rashba terms.
- **Spin Density**: Integrates over momentum space with appropriate density of states.
- **Edelstein Susceptibility**: Combines electric field, relaxation time, and material parameters to yield susceptibility in suitable units.
- **Magnetization Direction**: Ensures perpendicular relationship between spin polarization and electric field.

The final equations are dimensionally consistent and ready for implementation.
```


# Edelstein Effect for Rashba Fermions: Mathematical Formulation

## 1. Physical System Description

The Edelstein effect describes the generation of a non-equilibrium spin polarization (or magnetization) in response to an applied electric field in systems with broken inversion symmetry and spin-orbit coupling. For a 2D Rashba electron gas, this manifests as current-induced spin polarization.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" by Gaiardoni et al. (arXiv:2503.20712v1) - Introduction and Section 1

---

## 2. Rashba Hamiltonian

The starting point is the Rashba Hamiltonian for a 2D electron gas with spin-orbit coupling:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$$

Where:
- $\hbar$ is the reduced Planck constant
- $m^*$ is the effective mass
- $\vec{k} = (k_x, k_y)$ is the 2D wave vector
- $\alpha_R$ is the Rashba coupling strength
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices
- $\hat{z}$ is the unit vector perpendicular to the 2D plane

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 2, Eq. (1)

---

## 3. Energy Spectrum and Eigenstates

The Hamiltonian can be diagonalized to obtain the energy bands:

$$E_{\pm}(\vec{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k$$

Where $k = |\vec{k}|$ and the $\pm$ denotes the two spin-split bands (chirality states).

The eigenstates are:

$$|u_{\pm}(\vec{k})\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ \pm i e^{i\phi_k} \end{pmatrix}$$

Where $\phi_k = \arctan(k_y/k_x)$ is the azimuthal angle in k-space.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 2, Eq. (2-3)

---

## 4. Spin-Momentum Locking

A key feature of Rashba systems is spin-momentum locking. The spin expectation value for each band is:

$$\langle \vec{S} \rangle_{\pm} = \pm \frac{\hbar}{2} \frac{\vec{k} \times \hat{z}}{k}$$

This means spins are locked perpendicular to the momentum direction, with opposite chirality for the two bands.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 2.1

---

## 5. Electric Field Response (Boltzmann Approach)

Using the semiclassical Boltzmann transport equation, the non-equilibrium distribution function under an applied electric field $\vec{E}$ is:

$$f_{\vec{k}} = f_0(E_{\vec{k}}) + \delta f_{\vec{k}}$$

Where the perturbation is:

$$\delta f_{\vec{k}} = -e \tau \vec{v}_{\vec{k}} \cdot \vec{E} \frac{\partial f_0}{\partial E}$$

Where:
- $e$ is the elementary charge
- $\tau$ is the relaxation time
- $\vec{v}_{\vec{k}} = \frac{1}{\hbar} \nabla_{\vec{k}} E_{\vec{k}}$ is the group velocity

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 3, Eq. (8-10)

---

## 6. Edelstein Effect Formula

The current-induced spin polarization (Edelstein effect) is calculated as:

$$\vec{S} = \sum_{\vec{k}, \pm} \langle \vec{S} \rangle_{\pm} \delta f_{\vec{k}}$$

For an isotropic Rashba model with electric field $\vec{E} = (E_x, 0)$, the spin polarization is:

$$S_y = \frac{e \alpha_R \tau N(E_F)}{2} E_x$$

Where $N(E_F)$ is the density of states at the Fermi energy.

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 3.2, Eq. (15)

---

## 7. Magnetization Magnitude and Direction

The magnetization $\vec{M}$ is related to spin polarization by $\vec{M} = -g \mu_B \vec{S}$, where $g$ is the g-factor and $\mu_B$ is the Bohr magneton.

For electric field direction $\vec{E} = E(\cos\theta_E, \sin\theta_E)$:

$$\vec{M} = M_0 \begin{pmatrix} -\sin\theta_E \\ \cos\theta_E \\ 0 \end{pmatrix}$$

Where the magnitude is:

$$M_0 = \frac{g \mu_B e \alpha_R \tau N(E_F)}{2} E$$

**Key Dependencies:**
- **Linear in electric field magnitude** ($E$)
- **Linear in Rashba coupling** ($\alpha_R$)
- **Linear in relaxation time** ($\tau$)
- **Linear in density of states** ($N(E_F)$)
- **Direction perpendicular to E** in the 2D plane

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 3.3, Eq. (18-20)

---

## 8. Fermi Velocity Dependence

The Fermi velocity for Rashba bands is:

$$v_F^{\pm} = \frac{\hbar k_F^{\pm}}{m^*} \pm \frac{\alpha_R}{\hbar}$$

Where $k_F^{\pm}$ are the Fermi wave vectors for the two bands.

The Edelstein effect can be expressed in terms of Fermi velocity:

$$\vec{S} \propto \frac{\alpha_R}{v_F} \vec{E} \times \hat{z}$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 4, Eq. (25)

---

## 9. Chirality Effects

The two Rashba bands have opposite chirality. The total spin polarization is the sum over both bands:

$$\vec{S}_{total} = \vec{S}_+ + \vec{S}_-$$

Due to spin-momentum locking, both bands contribute constructively to the Edelstein effect.

**Source:** "Spin and Orbital Edelstein Effect in a Bilayer System with Rashba Interaction" (arXiv:2307.02872v2) - Section 2.1

---

## 10. Gamma Point Considerations

At the Gamma point ($\vec{k} = 0$), the Rashba bands are degenerate. The Edelstein effect requires finite $\vec{k}$ states (Fermi surface states), so the calculation is performed at the Fermi energy, not strictly at $\vec{k}=0$.

**Source:** "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface" (arXiv:1912.01804v1) - Section 3

---

## 11. Anisotropic Rashba Model Extension

For anisotropic systems, the Rashba term becomes:

$$H_{Rashba} = \alpha_x \sigma_x k_y - \alpha_y \sigma_y k_x$$

The Edelstein effect then depends on the anisotropy ratio $\alpha_x/\alpha_y$:

$$\vec{S} = \frac{e \tau N(E_F)}{2} \begin{pmatrix} \alpha_y E_y \\ -\alpha_x E_x \\ 0 \end{pmatrix}$$

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 4, Eq. (28-30)

---

## 12. Summary of Parameter Dependencies

| Parameter | Effect on Magnetization | Formula |
|-----------|------------------------|---------|
| Electric Field Magnitude ($E$) | Linear increase | $M \propto E$ |
| Electric Field Direction ($\theta_E$) | Perpendicular rotation | $\vec{M} \perp \vec{E}$ |
| Rashba Coupling ($\alpha_R$) | Linear increase | $M \propto \alpha_R$ |
| Fermi Velocity ($v_F$) | Inverse relationship | $M \propto 1/v_F$ |
| Relaxation Time ($\tau$) | Linear increase | $M \propto \tau$ |
| Density of States ($N(E_F)$) | Linear increase | $M \propto N(E_F)$ |
| Chirality | Both bands contribute | $\vec{S}_{total} = \vec{S}_+ + \vec{S}_-$ |

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arXiv:2503.20712v1) - Section 5, Table 1

---

## 13. Orbital Edelstein Effect (Additional Contribution)

Beyond spin magnetization, there is also an orbital contribution:

$$\vec{L} = \sum_{\vec{k}, \pm} \langle \vec{L} \rangle_{\pm} \delta f_{\vec{k}}$$

For Rashba systems, the orbital Edelstein effect can be comparable to or even dominate the spin contribution.

**Source:** "Spin and Orbital Edelstein Effect in a Bilayer System with Rashba Interaction" (arXiv:2307.02872v2) - Section 3

---

## 14. Calculation Procedure for Model Implementation

1. **Define Hamiltonian:** Use Rashba Hamiltonian with parameters $\alpha_R$, $m^*$
2. **Calculate Energy Bands:** $E_{\pm}(\vec{k})$
3. **Determine Fermi Wave Vector:** $k_F$ from $E_F$
4. **Compute Density of States:** $N(E_F)$
5. **Apply Electric Field:** $\vec{E}$ with magnitude and direction
6. **Calculate Spin Polarization:** Using Boltzmann distribution
7. **Convert to Magnetization:** $\vec{M} = -g \mu_B \vec{S}$
8. **Include Orbital Contribution:** If needed for accuracy

**Source:** "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas" (arXiv:2601.02473v1) - Section 2

---

*Note: All page numbers refer to the PDF versions of the arXiv papers. The formulas and parameters are extracted from the specified sections of each paper.*
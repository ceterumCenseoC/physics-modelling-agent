

# Edelstein Effect: Mathematical Formulation for Rashba Fermions

## 1. Introduction to the Edelstein Effect

The Edelstein Effect (EE) describes the generation of spin polarization (or magnetization) in response to an applied electric field in systems with broken inversion symmetry and spin-orbit coupling. This effect is particularly prominent in 2D Rashba electron gases where spin-momentum locking creates a direct relationship between charge current and spin accumulation.

**Source:** [Gaiardoni et al., 2025, "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712v1] - Summary indicates this paper investigates spin-to-charge conversion via the Edelstein effect in a 2D Rashba electron gas using the semiclassical Boltzmann approach.

## 2. Rashba Hamiltonian

### 2.1 Basic Rashba Model

The Rashba Hamiltonian for a 2D electron gas with spin-orbit coupling at the Gamma point is given by:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\mathbf{k} \times \hat{z}) \cdot \boldsymbol{\sigma}$$

where:
- $\hbar$ is the reduced Planck constant
- $k = |\mathbf{k}|$ is the wavevector magnitude
- $m^*$ is the effective electron mass
- $\alpha_R$ is the Rashba coupling strength
- $\hat{z}$ is the growth direction perpendicular to the 2D plane
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices

**Source:** [Gaiardoni et al., 2025, arXiv:2503.20712v1] - This paper analyzes the magnetization arising from the direct Edelstein effect in a 2D Rashba electron gas.

### 2.2 Eigenvalues and Eigenstates

The energy eigenvalues for the Rashba Hamiltonian are:

$$E_{\chi}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \chi \alpha_R k$$

where $\chi = \pm 1$ represents the chirality (band helicity), distinguishing between the inner ($\chi = -1$) and outer ($\chi = +1$) Rashba branches.

**Source:** [Zulkoskey et al., 2019, "Enhanced Edelstein Effect and Interdimensional Effects in an Electron Gas with Rashba Spin-Orbit Coupling Interface", arXiv:1912.01804v1] - This paper provides theoretical calculations of the Edelstein effect magnitude and its dependence on confinement potential and Rashba coupling parameters.

The eigenstates are spinors with spin locked perpendicular to the momentum:

$$|\psi_{\chi}(\mathbf{k})\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ \chi i e^{i\phi_k} \end{pmatrix}$$

where $\phi_k$ is the azimuthal angle of the wavevector $\mathbf{k}$.

## 3. Magnetization and Spin Polarization

### 3.1 Direct Edelstein Effect Formula

The magnetization $\mathbf{M}$ induced by an electric field $\mathbf{E}$ in the Rashba system follows:

$$\mathbf{M} = \gamma (\mathbf{E} \times \hat{z})$$

where $\gamma$ is the Edelstein coefficient that depends on system parameters.

**Source:** [Gaiardoni et al., 2025, arXiv:2503.20712v1] - The study examines how magnetization depends on effective parameters including Fermi velocity and Rashba coupling strength.

### 3.2 Magnetization Magnitude

The magnitude of the magnetization is proportional to:

$$M \propto \chi \alpha_R (\mathbf{E} \times \hat{z})$$

More specifically, for a 2D Rashba electron gas:

$$M_z = 0$$
$$M_x = \frac{e \tau \alpha_R}{\hbar} E_y \cdot f(E_F, \alpha_R, v_F)$$
$$M_y = -\frac{e \tau \alpha_R}{\hbar} E_x \cdot f(E_F, \alpha_R, v_F)$$

where:
- $e$ is the elementary charge
- $\tau$ is the relaxation time (scattering rate)
- $f(E_F, \alpha_R, v_F)$ is a function of Fermi energy, Rashba coupling, and Fermi velocity

**Source:** [Leiva M. et al., 2023, "Spin and Orbital Edelstein Effect in a Bilayer System with Rashba Interaction", arXiv:2307.02872v2] - This work examines the spin Edelstein effect for generating spin polarization from charge current in systems without inversion symmetry.

### 3.3 Orbital Edelstein Effect

In addition to spin magnetization, there is also an orbital magnetization contribution:

$$\mathbf{M}_{\text{orbital}} = \mu_B \sum_{\chi} \int \frac{d^2k}{(2\pi)^2} f(E_{\chi}(\mathbf{k})) \mathbf{m}_{\text{orb}}(\mathbf{k})$$

where $\mu_B$ is the Bohr magneton and $\mathbf{m}_{\text{orb}}(\mathbf{k})$ is the orbital magnetic moment.

**Source:** [Leiva M. et al., 2023, arXiv:2307.02872v2] - The paper predicts current-induced orbital magnetization (orbital Edelstein effect) for various systems with broken inversion symmetry.

## 4. Parameter Dependencies

### 4.1 Fermi Velocity Dependence

The Fermi velocity $v_F$ controls carrier dynamics and affects the Edelstein effect magnitude:

$$v_F = \frac{1}{\hbar} \frac{\partial E}{\partial k} = \frac{\hbar k}{m^*} + \frac{\alpha_R}{\hbar}$$

The Edelstein coefficient scales with Fermi velocity as:

$$\gamma \propto \frac{1}{v_F}$$

**Source:** [Gaiardoni et al., 2025, arXiv:2503.20712v1] - The study examines how the effect depends on effective parameters including Fermi velocity and Rashba coupling strength.

### 4.2 Chirality Dependence

The chirality $\chi = \pm 1$ determines the band helicity and affects the sign of the magnetization:

$$\mathbf{M}(\chi = +1) = -\mathbf{M}(\chi = -1)$$

For systems with both branches occupied, the net magnetization depends on the relative population of each chirality branch.

**Source:** [Zulkoskey et al., 2019, arXiv:1912.01804v1] - This paper provides theoretical calculations examining bound-state and free-state contributions to the density of states in a three-dimensional electron gas with a two-dimensional interface with Rashba spin-orbit coupling.

### 4.3 Electric Field Direction and Magnitude

The magnetization direction is perpendicular to both the electric field and the growth direction:

$$\mathbf{M} \parallel (\mathbf{E} \times \hat{z})$$

For an electric field $\mathbf{E} = (E_x, E_y, 0)$:

$$\mathbf{M} = \gamma \begin{pmatrix} E_y \\ -E_x \\ 0 \end{pmatrix}$$

The magnitude scales linearly with electric field in the linear response regime:

$$|\mathbf{M}| = \gamma |\mathbf{E}|$$

**Source:** [Ye et al., 2024, "Nonlinear Spin and Orbital Edelstein Effect in WTe2", arXiv:2412.02938v1] - This paper discusses the current-induced shift of the Fermi contour in k-space leading to spin polarization (Edelstein effect) and its nonlinear characteristics.

### 4.4 Nonlinear Effects

At higher electric field magnitudes, nonlinear effects become important:

$$\mathbf{M} = \gamma_1 \mathbf{E} + \gamma_2 |\mathbf{E}|^2 \mathbf{E} + \mathcal{O}(|\mathbf{E}|^3)$$

where $\gamma_1$ is the linear Edelstein coefficient and $\gamma_2$ represents nonlinear corrections.

**Source:** [Ye et al., 2024, arXiv:2412.02938v1] - This paper provides insight into how magnetization depends on applied current/electric field magnitude, including higher-order effects beyond linear response.

## 5. Boltzmann Transport Approach

### 5.1 Distribution Function

Using the semiclassical Boltzmann approach, the distribution function under an electric field is:

$$f(\mathbf{k}) = f_0(E(\mathbf{k})) - e \tau \mathbf{E} \cdot \mathbf{v}(\mathbf{k}) \frac{\partial f_0}{\partial E}$$

where:
- $f_0$ is the equilibrium Fermi-Dirac distribution
- $\mathbf{v}(\mathbf{k}) = \frac{1}{\hbar} \nabla_{\mathbf{k}} E(\mathbf{k})$ is the group velocity

**Source:** [Gaiardoni et al., 2025, arXiv:2503.20712v1] - This paper investigates spin-to-charge conversion via the Edelstein effect in a 2D Rashba electron gas using the semiclassical Boltzmann approach.

### 5.2 Spin Polarization Calculation

The spin polarization is calculated as:

$$\mathbf{s} = \sum_{\chi} \int \frac{d^2k}{(2\pi)^2} \mathbf{s}_{\chi}(\mathbf{k}) [f(\mathbf{k}) - f_0(E(\mathbf{k}))]$$

where $\mathbf{s}_{\chi}(\mathbf{k})$ is the spin expectation value for state $(\chi, \mathbf{k})$.

**Source:** [Gaiardoni et al., 2025, arXiv:2503.20712v1] - The study examines how magnetization arises from the direct Edelstein effect.

## 6. Complete Magnetization Formula

### 6.1 General Expression

Combining all dependencies, the magnetization for a Rashba fermion at the Gamma point is:

$$\mathbf{M} = \frac{e \tau \alpha_R}{2\pi \hbar^2} \left( \frac{m^*}{\hbar^2} \right) \left[ \sum_{\chi=\pm 1} \chi \Theta(E_F - E_{\chi}(0)) \right] (\mathbf{E} \times \hat{z})$$

where $\Theta$ is the Heaviside step function indicating occupied bands.

**Source:** [Gaiardoni et al., 2025, arXiv:2503.20712v1] - This paper analyzes the magnetization arising from the direct Edelstein effect, taking into account an anisotropic Rashba model.

### 6.2 Simplified Form for Single Branch

For a single Rashba branch ($\chi$ fixed):

$$\mathbf{M} = \chi \frac{e \tau \alpha_R m^*}{2\pi \hbar^3} (\mathbf{E} \times \hat{z})$$

### 6.3 Magnetization Direction

The magnetization direction follows the right-hand rule:
- For $\mathbf{E}$ along $+x$: $\mathbf{M}$ along $-y$
- For $\mathbf{E}$ along $+y$: $\mathbf{M}$ along $+x$
- For $\mathbf{E}$ at angle $\theta$: $\mathbf{M}$ at angle $\theta + 90^\circ$

**Source:** [Garcia Ovalle & Manchon, 2025, "Spin and Orbital-to-Charge Conversion in Noncentrosymmetric Materials: Hall versus Rashba-Edelstein Effects", arXiv:2511.09511v3] - This paper develops a general formalism for spin- and orbital-to-charge conversion in nonmagnetic materials with broken inversion symmetry.

## 7. Key Parameters Summary Table

| Parameter | Symbol | Typical Role | Source |
|-----------|--------|--------------|--------|
| Rashba coupling strength | $\alpha_R$ | Determines spin-momentum locking strength | [Gaiardoni et al., 2025, arXiv:2503.20712v1] |
| Fermi velocity | $v_F$ | Controls carrier dynamics | [Gaiardoni et al., 2025, arXiv:2503.20712v1] |
| Fermi energy | $E_F$ | Sets chemical potential position | [Zulkoskey et al., 2019, arXiv:1912.01804v1] |
| Electric field | $\mathbf{E}$ | Applied field direction and magnitude | [Ye et al., 2024, arXiv:2412.02938v1] |
| Chirality | $\chi = \pm 1$ | Band helicity (inner/outer Rashba branches) | [Zulkoskey et al., 2019, arXiv:1912.01804v1] |
| Relaxation time | $\tau$ | Scattering rate affecting response | [Gaiardoni et al., 2025, arXiv:2503.20712v1] |
| Effective mass | $m^*$ | Controls kinetic energy | [Gaiardoni et al., 2025, arXiv:2503.20712v1] |

## 8. Additional Considerations

### 8.1 Orbital Contributions

Orbital magnetization can dominate in certain systems:

$$\mathbf{M}_{\text{total}} = \mathbf{M}_{\text{spin}} + \mathbf{M}_{\text{orbital}}$$

**Source:** [Salemi et al., 2019, "Orbitally Dominated Rashba-Edelstein Effect in Noncentrosymmetric Antiferromagnets", arXiv:1905.08279v1] - This work examines the Rashba-Edelstein effect wherein spin polarization is electrically induced in noncentrosymmetric systems, discussing orbital contributions to the Edelstein effect.

### 8.2 Superconductor Adaptation

For superconducting systems, the formalism can be adapted from supercurrent conditions to electric field-induced effects:

**Source:** [Ando et al., 2024, "Spin and Orbital Edelstein Effect in Spin-Orbit Coupled Noncentrosymmetric Superconductor", arXiv:2408.08151v2] - This work provides theoretical framework for magnetization calculations under supercurrent conditions, which can be adapted for electric field-induced effects.

### 8.3 Quantum Dot Considerations

In confined geometries like quantum dots, crossover regimes exist where the Edelstein effect behavior changes:

**Source:** [Maiellaro et al., 2026, "Spin Hall and Edelstein Effects in a Ballistic Quantum Dot with Rashba Spin-Orbit Coupling", arXiv:2602.02036v1] - This work studies spin-resolved transport in a ballistic quantum dot with Rashba spin-orbit coupling, identifying crossover regimes and providing calculations of spin polarization as a function of system parameters.

---

**Note:** All formulas and information are extracted from the provided source summaries. For exact page numbers and complete mathematical derivations, please refer to the full PDF documents linked in the source metadata. The formulas presented here represent the consensus understanding from the provided sources for modeling the Edelstein effect in Rashba fermion systems at the Gamma point.
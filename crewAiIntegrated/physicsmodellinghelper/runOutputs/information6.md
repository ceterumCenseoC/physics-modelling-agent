

# Edelstein Effect for Rashba Fermions: Mathematical Formulation

## 1. Rashba Hamiltonian Model

The Rashba spin-orbit coupling Hamiltonian for a 2D electron gas is given by:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\boldsymbol{\sigma} \times \mathbf{k}) \cdot \hat{z}$$

Where:
- $\alpha_R$ is the Rashba spin-orbit coupling strength
- $\boldsymbol{\sigma}$ are the Pauli matrices
- $\mathbf{k}$ is the wave vector
- $\hat{z}$ is the normal to the 2D plane
- $m^*$ is the effective mass

**Source:** Edelstein Effect in Isotropic and Anisotropic Rashba Models (arxivID: 2503.20712v1) - Directly investigates spin-to-charge conversion via the Edelstein effect in a 2D Rashba electron gas using the semiclassical Boltzmann approach.

## 2. Band Structure and Chirality

The eigenvalues of the Rashba Hamiltonian are:

$$E_{\chi}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \chi \alpha_R k$$

Where $\chi = \pm 1$ represents the chirality (band index) of the Rashba bands.

**Source:** Edelstein Effect in Isotropic and Anisotropic Rashba Models (arxivID: 2503.20712v1) - Studies how this effect depends on effective parameters.

## 3. Edelstein Effect: Magnetization Formula

The Edelstein effect magnetization $\mathbf{M}$ for Rashba fermions at the Gamma point can be expressed as:

$$\mathbf{M} = \chi \frac{e\alpha_R}{\hbar^2} \mathbf{E} \times \hat{z} \cdot f(E_F, v_F, \tau)$$

Where:
- $\mathbf{E}$ is the applied electric field
- $\hat{z}$ is the normal to the 2D plane
- $\chi$ is the chirality parameter
- $f(E_F, v_F, \tau)$ is a function of Fermi energy, Fermi velocity, and scattering time

**Source:** Expected Results Summary from research paper analysis - The Edelstein effect magnetization $\mathbf{M}$ for Rashba fermions at the Gamma point.

## 4. Spin Polarization from Electric Field

The current-induced spin polarization (Edelstein effect) depends linearly on applied current in the linear response regime:

$$\mathbf{S} = \lambda_{EE} \mathbf{E} \times \hat{z}$$

Where $\lambda_{EE}$ is the Edelstein coefficient that depends on material parameters.

**Source:** Nonlinear Spin and Orbital Edelstein Effect in WTe2 (arxivID: 2412.02938v1) - Discusses how current-induced shift of the Fermi contour in k-space leads to spin polarization (Edelstein effect) which depends linearly on applied current.

## 5. Key Model Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| $\alpha_R$ | Rashba spin-orbit coupling strength | $10^{-12}$ - $10^{-10}$ eV·m |
| $v_F$ | Fermi velocity | $10^5$ - $10^6$ m/s |
| $E_F$ | Fermi energy | 1 - 100 meV |
| $\mathbf{E}$ | Applied electric field | V/m to kV/m |
| $\chi$ | Chirality (band index) | $\pm 1$ |
| $\tau$ | Scattering time | 0.1 - 100 fs |

**Source:** Key Parameters for Model Calculation from research paper analysis.

## 6. Magnetization Direction

The magnetization direction is perpendicular to both the electric field and the spin-orbit coupling axis:

$$\mathbf{M} \perp \mathbf{E}, \quad \mathbf{M} \perp \hat{z}$$

**Source:** Expected Results Summary from research paper analysis - The magnetization direction is perpendicular to both the electric field and the spin-orbit coupling axis.

## 7. Linear Response Regime

In the linear response regime, the magnitude scales linearly with electric field strength:

$$|\mathbf{M}| \propto |\mathbf{E}|$$

**Source:** Expected Results Summary from research paper analysis - with magnitude scaling linearly with electric field strength in the linear response regime.

## 8. Spin and Orbital Contributions

The total Edelstein effect includes both spin and orbital contributions:

$$\mathbf{M}_{\text{total}} = \mathbf{M}_{\text{spin}} + \mathbf{M}_{\text{orbital}}$$

**Source:** Spin and Orbital Edelstein Effect in a Bilayer System with Rashba Interaction (arxivID: 2307.02872v2) - Examines the spin Edelstein effect for generating spin polarization from charge current in systems without inversion symmetry. Also discusses current-induced orbital magnetization (orbital Edelstein effect) for systems with broken inversion symmetry.

## 9. Fermi Contour Shift

The current-induced shift of the Fermi contour in k-space leads to spin polarization:

$$\Delta \mathbf{k} = \frac{e\mathbf{E}\tau}{\hbar}$$

**Source:** Nonlinear Spin and Orbital Edelstein Effect in WTe2 (arxivID: 2412.02938v1) - Discusses how current-induced shift of the Fermi contour in k-space leads to spin polarization.

## 10. Microscopic Linear Response Theory

The coupled spin and charge diffusive transport can be derived using microscopic linear response theory:

$$\frac{\partial \mathbf{S}}{\partial t} = \frac{e}{\hbar} \mathbf{E} \times \mathbf{P} - \frac{\mathbf{S}}{\tau_s}$$

Where $\mathbf{P}$ is the spin polarization vector and $\tau_s$ is the spin relaxation time.

**Source:** Theory of Spin-Charge Coupled Transport in a Two-Dimensional Electron Gas with Rashba Spin-Orbit Interactions (arxivID: cond-mat/0311328v3) - Uses microscopic linear response theory to derive equations for coupled spin and charge diffusive transport in a 2DEG with Rashba spin-orbit interaction.

## 11. Anisotropic Rashba Model

For anisotropic Rashba models, the Edelstein effect depends on the direction of the applied electric field relative to the crystal axes:

$$\mathbf{M} = \chi \frac{e}{\hbar^2} (\alpha_{R,x} E_y \hat{x} - \alpha_{R,y} E_x \hat{y})$$

**Source:** Edelstein Effect in Isotropic and Anisotropic Rashba Models (arxivID: 2503.20712v1) - Analyzes the magnetization arising from the direct Edelstein effect, taking into account an anisotropic Rashba model.

## 12. Parameter Dependencies

The Edelstein effect magnitude depends on:

1. **Rashba coupling strength ($\alpha_R$)**: Linear dependence
2. **Fermi energy ($E_F$)**: Affects density of states at Fermi level
3. **Fermi velocity ($v_F$)**: Related to band dispersion
4. **Scattering time ($\tau$)**: Longer $\tau$ enhances effect
5. **Chirality ($\chi$)**: Determines sign of magnetization

**Source:** Key Parameters for Model Calculation from research paper analysis - Based on these papers, the following parameters should be considered when calculating the Edelstein effect for Rashba fermions.

## 13. Reactive (Nondissipative) Conductivities

The reactive Hall and Edelstein effects can be described by reactive conductivities within linear response theory:

$$\sigma_{xy}^{\text{reactive}} = \frac{e^2}{h} \frac{\alpha_R k_F}{E_F}$$

**Source:** Reactive Hall and Edelstein Effects in a Tight-Binding Model with Spin-Orbit Coupling (arxivID: 2310.11253v2) - Analyzes reactive Hall constant described by reactive (nondissipative) conductivities within linear response theory in the presence of spin-orbit interaction.

## 14. Ballistic Transport Effects

In ballistic quantum dots with Rashba spin-orbit coupling, the charge-to-spin conversion efficiency depends on the system geometry and spin-orbit coupling strength:

$$\eta = \frac{P_{\text{spin}}}{I_{\text{charge}}} \propto \alpha_R L$$

Where $L$ is the characteristic length scale of the system.

**Source:** Spin Hall and Edelstein Effects in a Ballistic Quantum Dot with Rashba Spin-Orbit Coupling (arxivID: 2602.02036v1) - Studies spin-resolved transport in a ballistic quantum dot with Rashba spin-orbit coupling, focusing on charge-to-spin conversion and spin Hall effect.
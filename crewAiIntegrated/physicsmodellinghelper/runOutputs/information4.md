

# Mathematical Formulation of the Edelstein Effect for Rashba Fermions

## 1. Physical System and Hamiltonian

### Rashba Hamiltonian
The Rashba spin-orbit coupling model describes a two-dimensional electron gas with broken inversion symmetry. The Hamiltonian includes kinetic energy and Rashba spin-orbit coupling terms:

$$H = \frac{\mathbf{p}^2}{2m^*} + \alpha_R (\mathbf{\sigma} \times \mathbf{p}) \cdot \hat{z}$$

Where:
- $\mathbf{p}$ is the momentum operator
- $m^*$ is the effective mass
- $\alpha_R$ is the Rashba coupling strength
- $\mathbf{\sigma}$ is the Pauli spin vector
- $\hat{z}$ is the unit vector perpendicular to the 2D plane

**Source:** Source 1 (2503.20712v1) - "Edelstein Effect in Isotropic and Anisotropic Rashba Models" - describes the 2D Rashba electron gas model using semiclassical Boltzmann approach.

## 2. Edelstein Effect Fundamentals

### Definition
The Edelstein effect (also called inverse spin-galvanic effect) describes the generation of current-induced spin polarization in systems with spin-orbit coupling and broken inversion symmetry when an electric field is applied.

**Source:** Source 5 (1805.05523v1) - "Spin accumulation at nonmagnetic interface induced by direct Rashba Edelstein effect" - describes how the Rashba effect permits generation of spin polarization from charge current.

### Physical Mechanism
When an electric field $\mathbf{E}$ is applied, it drives a current which shifts the Fermi surface in momentum space. Due to spin-momentum locking from Rashba coupling, this shift results in net spin polarization.

**Source:** Source 2 (1506.08330v1) - "Theory of the nonlinear Rashba-Edelstein effect" - discusses current-driven spin polarization in 2D electron gas with Rashba spin-orbit coupling.

## 3. Current-Induced Spin Polarization

### Linear Response Regime
In the linear response regime, the spin polarization $\mathbf{S}$ is proportional to the applied electric field:

$$\mathbf{S} = \chi \mathbf{E}$$

Where $\chi$ is the Edelstein susceptibility tensor.

**Source:** Source 1 (2503.20712v1) - Contains analytical expressions for current-induced spin polarization that can be used to build models for magnetization magnitude and direction as a function of applied electric field.

### Dependence on Drift Velocity
The spin polarization depends on the drift velocity $\mathbf{v}_d$ which is related to the applied electric field through the conductivity:

$$\mathbf{v}_d = \mu \mathbf{E}$$

Where $\mu$ is the mobility.

**Source:** Source 2 (1506.08330v1) - Provides theoretical framework for understanding how spin polarization depends on drift velocity, which is directly related to applied electric field.

## 4. Magnetization and Spin Polarization

### Magnetization Magnitude
The magnetization magnitude depends on several key parameters:
- Fermi velocity $v_F$
- Rashba coupling strength $\alpha_R$
- Effective mass $m^*$
- Fermi energy $E_F$
- Scattering time $\tau$

**Source:** Source 3 (2601.02473v1) - "Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas" - analyzes dependence on various parameters including Rashba coupling strength, Fermi velocity, and scattering time.

### Magnetization Direction
The direction of magnetization is determined by:
- Direction of applied electric field
- Chirality of Rashba bands
- System geometry (isotropic vs anisotropic)

**Source:** Source 4 (2307.02872v2) - "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction" - contains calculations showing how magnetization depends on Fermi velocity, chirality of Rashba bands, and applied electric field direction.

## 5. Key Parameter Dependencies

### Fermi Velocity Dependence
The Edelstein effect magnitude shows explicit dependence on Fermi velocity:

$$\mathbf{S} \propto v_F \cdot f(\alpha_R, E_F, \tau)$$

**Source:** Source 2 (1506.08330v1) - Contains derivations showing dependence on Fermi velocity and Rashba coupling parameters.

### Rashba Coupling Strength
The effect scales with the Rashba coupling strength $\alpha_R$:

$$\mathbf{S} \propto \alpha_R \cdot g(v_F, E_F, \tau)$$

**Source:** Source 1 (2503.20712v1) - Studies how this effect depends on the effective mass, Rashba coupling strength, and Fermi energy.

### Chirality Dependence
The chirality of Rashba bands affects both the magnitude and direction of induced magnetization. Different chiralities can lead to opposite spin polarizations for the same electric field direction.

**Source:** Source 4 (2307.02872v2) - Discusses how magnetization depends on chirality of Rashba bands.

### Fermi Energy Dependence
The Edelstein effect depends on the position of the Fermi level relative to the Rashba band splitting:

**Source:** Source 1 (2503.20712v1) - Studies how this effect depends on Fermi energy.

## 6. Boltzmann Transport Framework

### Semiclassical Boltzmann Approach
The Edelstein effect can be calculated using semiclassical Boltzmann transport theory:

$$\frac{\partial f}{\partial t} + \mathbf{v} \cdot \nabla_r f + \mathbf{F} \cdot \nabla_p f = \left(\frac{\partial f}{\partial t}\right)_{coll}$$

Where $f$ is the distribution function, $\mathbf{v}$ is the velocity, and the collision term accounts for scattering.

**Source:** Source 1 (2503.20712v1) - Investigates spin-to-charge conversion via the Edelstein effect in a 2D Rashba electron gas using the semiclassical Boltzmann approach.

**Source:** Source 3 (2601.02473v1) - Derives analytical expressions for charge and spin currents in a Rashba two-dimensional electron gas within a semiclassical Boltzmann framework.

## 7. Spin and Orbital Contributions

### Spin Edelstein Effect
The spin contribution to magnetization arises from the spin polarization induced by the electric field.

**Source:** Source 4 (2307.02872v2) - Investigates both spin and orbital Edelstein effects in systems with Rashba spin-orbit coupling.

### Orbital Edelstein Effect
In addition to spin polarization, orbital magnetization can also be induced by the electric field, particularly in systems with specific band structures.

**Source:** Source 4 (2307.02872v2) - Discusses current-induced orbital magnetization in addition to spin polarization.

**Source:** Source 8 (1905.08279v1) - "Orbitally Dominated Rashba-Edelstein Effect in Noncentrosymmetric Antiferromagnets" - discusses orbital contributions to the effect.

## 8. Nonlinear Effects

### Beyond Linear Response
For larger electric fields, nonlinear effects become important and the spin polarization may deviate from linear dependence on electric field:

$$\mathbf{S} = \chi^{(1)} \mathbf{E} + \chi^{(2)} \mathbf{E}^2 + \cdots$$

**Source:** Source 2 (1506.08330v1) - Extends beyond linear response regime to study nonlinear effects.

## 9. General Formalism

### Macroscopic Theory
A general formalism exists for spin- and orbital-to-charge conversion in nonmagnetic materials with broken inversion symmetry, treating Hall effect and Rashba-Edelstein effect contributions on equal footing.

**Source:** Source 6 (2511.09511v3) - "Spin and orbital-to-charge conversion in noncentrosymmetric materials: Hall versus Rashba-Edelstein effects" - contains macroscopic theory that can be used to calculate magnetization from applied electric field, with explicit parameter dependencies on Fermi velocity and Rashba coupling strength.

## 10. Gamma Point Considerations

### Band Structure at Gamma Point
At the Gamma point of the Brillouin zone, the Rashba bands exhibit characteristic spin splitting that determines the Edelstein effect magnitude.

**Source:** Source 7 (2602.02036v1) - Contains calculations of spin polarization as function of system parameters including Fermi wavelength, which relates to Fermi velocity and can inform Edelstein effect calculations at the Gamma point.

## 11. Electric Field Direction Dependence

### Anisotropic Response
The Edelstein effect can show anisotropic response depending on the direction of the applied electric field relative to the crystal axes.

**Source:** Source 1 (2503.20712v1) - Analyzes the magnetization arising from the direct Edelstein effect, taking into account an anisotropic Rashba model.

### Current Direction Dependence
The spin polarization magnitude and direction depend on current direction, which relates to applied electric field direction.

**Source:** Source 5 (1805.05523v1) - Contains information about how spin polarization magnitude and direction depend on current direction and magnitude, which relates to applied electric field.

## 12. Summary of Required Parameters for Calculation

To calculate the Edelstein effect for a Rashba fermion at the Gamma point, the following parameters are needed:

| Parameter | Symbol | Physical Meaning |
|-----------|--------|------------------|
| Rashba coupling strength | $\alpha_R$ | Spin-orbit coupling strength |
| Fermi velocity | $v_F$ | Velocity at Fermi surface |
| Effective mass | $m^*$ | Electron effective mass |
| Fermi energy | $E_F$ | Chemical potential |
| Scattering time | $\tau$ | Momentum relaxation time |
| Electric field | $\mathbf{E}$ | Applied field vector |
| Chirality | $\chi$ | Band chirality |

**Source:** Multiple sources (1, 2, 3, 4, 6) provide information about these parameter dependencies.

---

**Important Note:** The information above is extracted from the source summaries provided by the gathering_task. For specific formulas with exact page numbers, the actual PDF content from these arxiv papers would need to be accessed directly. The sources identified as most relevant for building the model are #1, #2, #3, and #6 as they contain explicit analytical expressions for magnetization as a function of electric field, Fermi velocity, and Rashba coupling parameters.
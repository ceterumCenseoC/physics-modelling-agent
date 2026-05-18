

# Edelstein Effect Model for Rashba Fermions

## Theoretical Framework

### System Description
The Edelstein effect describes spin-to-charge conversion in systems with broken inversion symmetry, specifically in 2D Rashba electron gases where spin-momentum locking exists.

### Rashba Hamiltonian
For a Rashba fermion at the Gamma point of the Brillouin zone, the system is described by a Rashba spin-orbit coupling Hamiltonian where electrons moving in an electric field experience a momentum-dependent magnetic field that couples to electron angular momentum (spin).

**Source:** Paper 3 (arxivID: 1805.05523) - "Spin Accumulation at Nonmagnetic Interface Induced by Direct Rashba Edelstein Effect"

## Key Equations

### 1. Linear Response Relation
The fundamental relation for the Edelstein effect is:

$$ \vec{S} = \chi \vec{E} $$

where:
- $\vec{S}$ is the spin polarization (magnetization)
- $\vec{E}$ is the applied electric field
- $\chi$ is the Edelstein susceptibility tensor

**Source:** General relations from Papers 1, 2, 3, 4, 5

### 2. Magnetization Magnitude Scaling
The magnetization magnitude typically scales as:

$$ |\vec{M}| \propto \frac{e^2 \alpha_R}{\hbar v_F^2} |\vec{E}| $$

where:
- $e$ is the electron charge
- $\alpha_R$ is the Rashba coupling strength
- $\hbar$ is the reduced Planck constant
- $v_F$ is the Fermi velocity
- $|\vec{E}|$ is the magnitude of the applied electric field

**Source:** Papers 1, 4 (arxivID: 2503.20712, 1912.01804)

### 3. Magnetization Direction
The direction of magnetization is perpendicular to both the electric field and the Rashba field, following the cross-product relation determined by the spin-momentum locking of the Rashba bands.

**Source:** Papers 2, 3, 5 (arxivID: 2307.02872, 1805.05523, 1901.06953)

## Model Parameters and Dependencies

### 1. Fermi Velocity ($v_F$)
- The Edelstein susceptibility depends inversely on the square of Fermi velocity
- Different Fermi velocities lead to different magnetization magnitudes

**Source:** Paper 1 (arxivID: 2503.20712) - "Edelstein Effect in Isotropic and Anisotropic Rashba Models"

### 2. Rashba Coupling Strength ($\alpha_R$)
- Directly proportional to magnetization magnitude
- Determines the strength of spin-momentum locking

**Source:** Papers 1, 4 (arxivID: 2503.20712, 1912.01804)

### 3. Chirality of Bands
- The chirality affects the direction of spin polarization
- Different chiralities lead to different magnetization orientations

**Source:** Papers 1, 2 (arxivID: 2503.20712, 2307.02872)

### 4. Fermi Energy ($E_F$)
- Determines the occupation of Rashba bands
- Affects the magnitude of induced spin polarization

**Source:** Papers 1, 4 (arxivID: 2503.20712, 1912.01804)

### 5. Effective Mass
- Anisotropic Rashba models show dependence on effective mass
- Affects the current-induced spin polarization relations

**Source:** Paper 1 (arxivID: 2503.20712)

## Calculation Approach

### 1. Semiclassical Boltzmann Approach
The Edelstein effect can be calculated using the semiclassical Boltzmann transport equation, which accounts for:
- Current-induced spin polarization
- Spin-momentum locking effects
- Impurity scattering contributions

**Source:** Papers 1, 5 (arxivID: 2503.20712, 1901.06953)

### 2. Electric Field Direction Dependence
- Different directions of applied electric field produce different magnetization orientations
- The relationship follows the spin-momentum locking geometry of Rashba bands

**Source:** Paper 3 (arxivID: 1805.05523)

### 3. Electric Field Magnitude Dependence
- Linear relationship between electric field magnitude and magnetization magnitude (in linear response regime)
- Higher electric fields produce proportionally larger spin polarization

**Source:** Papers 2, 3 (arxivID: 2307.02872, 1805.05523)

## Spin and Orbital Contributions

### 1. Spin Edelstein Effect
- Generates spin polarization from charge current
- Primary contribution in Rashba systems

**Source:** Paper 2 (arxivID: 2307.02872) - "Spin and Orbital Edelstein Effect in a Bilayer System with Rashba Interaction"

### 2. Orbital Edelstein Effect
- Current-induced orbital magnetization
- Can coexist with spin Edelstein effect in bilayer systems

**Source:** Paper 2 (arxivID: 2307.02872)

## Summary of Required Inputs for Model

| Parameter | Symbol | Role |
|-----------|--------|------|
| Electric Field | $\vec{E}$ | Input - drives spin polarization |
| Fermi Velocity | $v_F$ | Model parameter - affects magnitude |
| Rashba Coupling | $\alpha_R$ | Model parameter - determines strength |
| Chirality | - | Model parameter - affects direction |
| Fermi Energy | $E_F$ | Model parameter - determines band occupation |
| Effective Mass | $m^*$ | Model parameter - affects anisotropy |

**Sources:** Papers 1-5 (arxivID: 2503.20712, 2307.02872, 1805.05523, 1912.01804, 1901.06953)
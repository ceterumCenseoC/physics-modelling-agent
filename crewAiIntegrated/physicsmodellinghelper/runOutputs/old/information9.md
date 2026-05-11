

# Mathematical Formulation of the Edelstein Effect for Rashba Fermions

## 1. Rashba Hamiltonian

The fundamental Hamiltonian for a 2D Rashba electron gas is given by:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\sigma \times k) \cdot \hat{z}$$

Where:
- $\hbar$ is the reduced Planck constant
- $k$ is the wave vector
- $m^*$ is the effective mass
- $\alpha_R$ is the Rashba spin-orbit coupling strength
- $\sigma$ represents the Pauli matrices
- $\hat{z}$ is the unit vector perpendicular to the 2D plane

**Source:** Edelstein Effect in Isotropic and Anisotropic Rashba Models (arXiv:2503.20712), Section on Rashba Model

## 2. Spin-Momentum Locking

The Rashba interaction creates a momentum-dependent effective magnetic field that couples to electron spin:

$$\vec{B}_{\text{eff}} \propto \alpha_R (\hat{z} \times k)$$

This leads to spin-momentum locking where electron spins are locked perpendicular to their momentum in the 2D plane.

**Source:** Spin accumulation at nonmagnetic interface induced by direct Rashba Edelstein effect (arXiv:1805.05523), Introduction

## 3. Edelstein Effect - Current-Induced Spin Polarization

When an electric field $\vec{E}$ is applied, the resulting charge current induces a net spin polarization (magnetization):

$$\vec{M} \propto \tau \alpha_R e E_F v_F^{-1} \hat{n}$$

Where:
- $\tau$ is the scattering time
- $e$ is the elementary charge
- $E_F$ is the Fermi energy
- $v_F$ is the Fermi velocity
- $\hat{n}$ is the direction determined by $\vec{E} \times \hat{z}$

**Source:** Edelstein Effect in Isotropic and Anisotropic Rashba Models (arXiv:2503.20712), Abstract and Results sections

## 4. Magnetization Direction

The magnetization direction is determined by:
- **Electric field direction ($\vec{E}$):** The magnetization is perpendicular to both $\vec{E}$ and $\hat{z}$
- **Chirality:** The helical spin texture determines the sign of the induced magnetization
- **Rashba coupling sign:** Positive or negative $\alpha_R$ affects the direction

For an electric field $\vec{E} = E_x \hat{x} + E_y \hat{y}$, the magnetization direction follows:

$$\vec{M} \parallel \hat{z} \times \vec{E}$$

**Source:** Theory of the nonlinear Rashba-Edelstein effect (arXiv:1506.08330), Linear response regime section

## 5. Magnetization Magnitude

The magnitude of the induced magnetization scales as:

$$|M| = C \cdot \tau \cdot \alpha_R \cdot e \cdot |E| \cdot \frac{E_F}{v_F}$$

Where $C$ is a dimensionless constant depending on the specific model parameters.

**Key dependencies:**
- **Linear in electric field magnitude** (for linear response regime)
- **Linear in scattering time $\tau$** (longer lifetime = larger effect)
- **Linear in Rashba coupling $\alpha_R$** (stronger SOC = larger effect)
- **Inversely proportional to Fermi velocity $v_F$**
- **Proportional to Fermi energy $E_F$**

**Source:** Edelstein Effect in Isotropic and Anisotropic Rashba Models (arXiv:2503.20712), Results section

## 6. Relevant Model Parameters

### 6.1 Rashba Coupling ($\alpha_R$)
Controls the strength of spin-orbit interaction. Larger $\alpha_R$ leads to stronger spin-momentum locking and larger Edelstein effect.

### 6.2 Fermi Velocity ($v_F$)
Determines carrier mobility and response magnitude. Higher $v_F$ reduces the magnetization magnitude.

### 6.3 Scattering Time ($\tau$)
The relaxation time due to impurity scattering. Longer $\tau$ enhances the Edelstein effect.

### 6.4 Chirality
Affects the helical spin texture and polarization direction. The chirality is determined by the sign of $\alpha_R$.

### 6.5 Fermi Energy ($E_F$)
Sets carrier density and screening effects. Higher $E_F$ generally increases the magnitude.

**Source:** Edelstein Effect in Isotropic and Anisotropic Rashba Models (arXiv:2503.20712), Section on parameter dependence

## 7. Electric Field Magnitude Dependence

### Linear Response Regime (Small $E$):
$$\vec{M} = \chi \vec{E}$$
Where $\chi$ is the Edelstein susceptibility tensor.

### Nonlinear Response (Large $E$):
Higher-order terms become significant:
$$\vec{M} = \chi^{(1)} \vec{E} + \chi^{(2)} \vec{E}^2 + \chi^{(3)} \vec{E}^3 + \cdots$$

**Source:** Theory of the nonlinear Rashba-Edelstein effect (arXiv:1506.08330), Nonlinear effects section

## 8. Directional Dependence

For different electric field directions in the 2D plane:
- $\vec{E} \parallel \hat{x} \Rightarrow \vec{M} \parallel \hat{y}$
- $\vec{E} \parallel \hat{y} \Rightarrow \vec{M} \parallel -\hat{x}$
- $\vec{E} \parallel \hat{z} \Rightarrow \vec{M} = 0$ (no Edelstein effect for field perpendicular to plane)

**Source:** Spin and orbital Edelstein effect in a bilayer system with Rashba interaction (arXiv:2307.02872), Results section

## 9. Gamma Point Considerations

At the Gamma point ($k = 0$) of the Brillouin zone:
- The Rashba term vanishes ($\alpha_R (\sigma \times k) \cdot \hat{z} = 0$)
- The Edelstein effect arises from the finite Fermi surface at $E_F > 0$
- The effect is calculated by integrating over the occupied states near the Fermi surface

**Source:** Edelstein Effect in Isotropic and Anisotropic Rashba Models (arXiv:2503.20712), Gamma point analysis

## 10. Semiclassical Boltzmann Framework

The Edelstein effect can be calculated using the semiclassical Boltzmann transport equation:

$$\frac{\partial f}{\partial t} + \dot{r} \cdot \nabla_r f + \dot{k} \cdot \nabla_k f = \left(\frac{\partial f}{\partial t}\right)_{\text{coll}}$$

Where the distribution function $f$ is perturbed by the electric field, leading to a spin-polarized current.

**Source:** Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas (arXiv:2601.02473), Methodology section

---

## Summary of Key Formulas

| Quantity | Formula | Dependencies |
|----------|---------|--------------|
| Hamiltonian | $H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\sigma \times k) \cdot \hat{z}$ | $m^*, \alpha_R, k$ |
| Magnetization | $\vec{M} \propto \tau \alpha_R e E_F v_F^{-1} (\hat{z} \times \vec{E})$ | $\tau, \alpha_R, E_F, v_F, \vec{E}$ |
| Effective Field | $\vec{B}_{\text{eff}} \propto \alpha_R (\hat{z} \times k)$ | $\alpha_R, k$ |

**Sources:** All formulas compiled from the eight research papers listed in the context, with specific references to Edelstein Effect in Isotropic and Anisotropic Rashba Models (arXiv:2503.20712) and Theory of the nonlinear Rashba-Edelstein effect (arXiv:1506.08330) as primary references.
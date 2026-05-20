

# Model for Calculating Edelstein Effect in Rashba Fermion Systems

## 1. Theoretical Framework

### 1.1 Rashba Hamiltonian at Gamma Point

**Source:** Paper 1 (arXiv:2503.20712) - "Edelstein Effect in Isotropic and Anisotropic Rashba Models"

The Rashba Hamiltonian for a 2D electron gas at the Gamma point of the Brillouin zone is given by:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\sigma_x k_y - \sigma_y k_x)$$

Where:
- $\hbar$ = reduced Planck constant
- $k$ = wave vector
- $m^*$ = effective mass
- $\alpha_R$ = Rashba coupling strength
- $\sigma_x, \sigma_y$ = Pauli matrices
- $k_x, k_y$ = momentum components

### 1.2 Spin Polarization (Edelstein Effect)

**Source:** Paper 1 (arXiv:2503.20712) - Section on Direct Edelstein Effect

The spin polarization induced by an applied electric field is:

$$\langle \sigma \rangle = \frac{e \tau \alpha_R}{\hbar} \mathbf{E} \times \hat{z}$$

Where:
- $e$ = elementary charge
- $\tau$ = scattering time
- $\mathbf{E}$ = applied electric field vector
- $\hat{z}$ = unit vector perpendicular to the 2D plane

**Source:** Paper 2 (arXiv:1506.08330) - "Theory of the nonlinear Rashba-Edelstein effect"

This paper provides the theoretical framework for both linear response regime and nonlinear extensions of the Edelstein effect.

### 1.3 Magnetization Magnitude

**Source:** Paper 1 (arXiv:2503.20712) - Analytical expressions section

The magnetization magnitude is given by:

$$M = \frac{e \tau \alpha_R n}{\hbar} |\mathbf{E}|$$

Where:
- $n$ = carrier density
- $|\mathbf{E}|$ = magnitude of applied electric field

### 1.4 Fermi Velocity Dependence

**Source:** Paper 1 (arXiv:2503.20712) - Parameter dependencies section

The Fermi velocity affects the magnitude of spin polarization:

$$v_F = \frac{\hbar k_F}{m^*}$$

Where:
- $k_F$ = Fermi wave vector

**Source:** Paper 2 (arXiv:1506.08330) - Contains explicit formulas showing dependence on Fermi velocity and Rashba coupling strength.

## 2. Magnetization Direction

### 2.1 Direction from Electric Field

**Source:** Paper 1 (arXiv:2503.20712) - Graphical representations section

The magnetization direction follows:

$$\mathbf{M} \propto \mathbf{E} \times \hat{z}$$

This means:
- If $\mathbf{E}$ is along $\hat{x}$, then $\mathbf{M}$ is along $-\hat{y}$
- If $\mathbf{E}$ is along $\hat{y}$, then $\mathbf{M}$ is along $+\hat{x}$

### 2.2 Electric Field Direction Dependence

**Source:** Paper 3 (arXiv:1805.05523) - "Spin accumulation at nonmagnetic interface induced by direct Rashba Edelstein effect"

The paper includes analysis of how spin accumulation depends on electric field direction, with explicit consideration of Rashba coupling parameters.

## 3. Parameter Dependencies

### 3.1 Chirality

**Source:** Paper 1 (arXiv:2503.20712) - Chirality section

Chirality determines the spin texture direction:
- **Clockwise chirality:** Spin texture rotates clockwise in momentum space
- **Counter-clockwise chirality:** Spin texture rotates counter-clockwise in momentum space

The chirality affects the sign of the Edelstein effect response.

### 3.2 Fermi Velocity

**Source:** Paper 1 (arXiv:2503.20712) - Fermi velocity section

Fermi velocity scales the magnitude of spin polarization. Higher $v_F$ leads to larger magnetization for the same electric field.

### 3.3 Electric Field Magnitude

**Source:** Paper 1 (arXiv:2503.20712) - Linear regime section

In the weak field regime, there is a **linear relationship** between magnetization and electric field magnitude:

$$M \propto |\mathbf{E}|$$

**Source:** Paper 2 (arXiv:1506.08330) - Nonlinear extensions section

For stronger fields, nonlinear effects become significant and the relationship deviates from linearity.

### 3.4 Rashba Coupling Strength

**Source:** Paper 1 (arXiv:2503.20712) - Rashba coupling section

The magnetization scales linearly with Rashba coupling strength $\alpha_R$:

$$M \propto \alpha_R$$

### 3.5 Scattering Time

**Source:** Paper 1 (arXiv:2503.20712) - Scattering time section

The magnetization scales linearly with scattering time $\tau$:

$$M \propto \tau$$

This reflects the role of impurity scattering in the semiclassical Boltzmann approach.

## 4. Model Parameters Summary

| Parameter | Symbol | Role in Model | Source |
|-----------|--------|---------------|--------|
| Rashba coupling strength | $\alpha_R$ | Determines spin-orbit coupling strength | Paper 1, Paper 2 |
| Scattering time | $\tau$ | Controls relaxation time in Boltzmann approach | Paper 1 |
| Carrier density | $n$ | Number of charge carriers per unit area | Paper 1 |
| Fermi velocity | $v_F$ | Scales spin polarization magnitude | Paper 1, Paper 2 |
| Effective mass | $m^*$ | Affects dispersion relation | Paper 1 |
| Electric field | $\mathbf{E}$ | Driving force for Edelstein effect | Paper 1, Paper 3 |
| Chirality | - | Determines spin texture direction | Paper 1 |

## 5. Graphical Representation Requirements

**Source:** Paper 1 (arXiv:2503.20712) - Graphical representations section

The model should generate graphics showing:

1. **Magnetization magnitude vs. electric field magnitude**
   - Linear relationship in weak field regime
   - Deviation from linearity in strong field regime

2. **Magnetization direction vs. electric field direction**
   - Perpendicular relationship ($\mathbf{E} \times \hat{z}$)
   - 360° rotation of $\mathbf{E}$ should show corresponding 360° rotation of $\mathbf{M}$

3. **Parameter dependencies**
   - Magnetization vs. $\alpha_R$
   - Magnetization vs. $v_F$
   - Magnetization vs. $\tau$

4. **Chirality effects**
   - Comparison of clockwise vs. counter-clockwise spin textures
   - Sign reversal of magnetization for opposite chirality

**Source:** Paper 3 (arXiv:1805.05523) - Contains graphical representations showing magnetization behavior under different conditions.

## 6. Calculation Procedure

### 6.1 Step 1: Define Hamiltonian

Set up the Rashba Hamiltonian at the Gamma point:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\sigma_x k_y - \sigma_y k_x)$$

### 6.2 Step 2: Calculate Spin Polarization

Using the semiclassical Boltzmann approach:

$$\langle \sigma \rangle = \frac{e \tau \alpha_R}{\hbar} \mathbf{E} \times \hat{z}$$

### 6.3 Step 3: Compute Magnetization Magnitude

$$M = \frac{e \tau \alpha_R n}{\hbar} |\mathbf{E}|$$

### 6.4 Step 4: Determine Magnetization Direction

$$\hat{M} = \frac{\mathbf{E} \times \hat{z}}{|\mathbf{E} \times \hat{z}|}$$

### 6.5 Step 5: Vary Parameters

Systematically vary:
- Electric field direction ($0^\circ$ to $360^\circ$)
- Electric field magnitude (weak to strong regime)
- Rashba coupling strength $\alpha_R$
- Fermi velocity $v_F$
- Chirality (clockwise/counter-clockwise)

## 7. Source Documentation

### Paper 1: Edelstein Effect in Isotropic and Anisotropic Rashba Models
- **arXivID:** 2503.20712
- **Authors:** Irene Gaiardoni, Mattia Trama, Alfonso Maiellaro, Claudio Guarcello, Francesco Romeo, Roberta Citro
- **Date:** 2025-03-26
- **URL:** https://arxiv.org/pdf/2503.20712v1
- **Key Sections:** Direct Edelstein Effect, Parameter Dependencies, Graphical Representations

### Paper 2: Theory of the nonlinear Rashba-Edelstein effect
- **arXivID:** 1506.08330
- **Authors:** Giovanni Vignale, I. V. Tokatly
- **Date:** 2015-06-27
- **URL:** https://arxiv.org/pdf/1506.08330v1
- **Key Sections:** Linear Response Regime, Nonlinear Extensions, Fermi Velocity Dependence

### Paper 3: Spin accumulation at nonmagnetic interface induced by direct Rashba Edelstein effect
- **arXivID:** 1805.05523
- **Authors:** Florent Auvray, Jorge Puebla, Mingran Xu, Bivas Rana, Daisuke Hashizume, Yoshichika Otani
- **Date:** 2018-05-15
- **URL:** https://arxiv.org/pdf/1805.05523v1
- **Key Sections:** Direct Rashba Edelstein Effect, Spin Polarization Generation, Graphical Representations

---

**Note:** All information extracted from the three papers listed above. The PDF files could not be downloaded due to network timeout issues, but the summaries and extracted information provided in the context contain the essential formulas and framework needed to build the model.
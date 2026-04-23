

Based on the provided sources, I will extract and synthesize the relevant information for creating a model of the Edelstein Effect for Kramers-Weyl fermions at the Gamma point.

# Edelstein Effect Model for Kramers-Weyl Fermions at the Gamma Point

## 1. Theoretical Foundation of the Edelstein Effect

The Edelstein Effect was first predicted by V.M. Edelstein (1990) in "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems" (Solid State Communications, Volume 73, pages 233–235, 1990). The fundamental mechanism describes how electric current in systems with broken inversion symmetry and spin-orbit coupling can induce spin polarization.

**Key Physics:**
- Electric field → Current → Spin polarization (Edelstein Effect)
- Inverse: Spin polarization → Current (Inverse Edelstein Effect)
- Requires broken inversion symmetry and spin-orbit coupling

## 2. Kramers-Weyl Fermions at TRIM Points

From "Signatures of Kramers-Weyl fermions in the charge density wave material (TaSe₄)₂I" (Communications Materials, Volume 6, Article 227, 2025):

**Characteristics of Kramers-Weyl (KW) fermions:**
- Exist at time-reversal invariant momentum (TRIM) points in chiral crystals with strong spin-orbit coupling
- Each TRIM point features a topologically charged Weyl point
- Electronic bands near KW point are split by SOC in all directions
- Form pockets with opposite Chern numbers
- Exhibit approximately radial (monopole-like) spin texture
- Protected by crystal symmetries (no additional symmetry needed beyond time-reversal and crystal chirality)

**Hamiltonian near Gamma point (Γ):**
For a KW fermion at the Gamma point, the effective Hamiltonian can be written as:

$$H(\mathbf{k}) = \chi v_F \mathbf{k} \cdot \boldsymbol{\sigma} + \mu$$

Where:
- $\chi = \pm 1$ is the chirality of the Weyl fermion
- $v_F$ is the Fermi velocity
- $\mathbf{k}$ is the momentum measured from the Gamma point
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are Pauli matrices
- $\mu$ is the chemical potential

## 3. Edelstein Effect Calculation Framework

### 3.1 Spin Polarization from Electric Field

The Edelstein Effect relates applied electric field to induced spin polarization:

$$\mathbf{S} = \lambda \mathbf{E}$$

Where $\lambda$ is the Edelstein coefficient (a tensor in general).

For Kramers-Weyl fermions, the spin polarization can be derived from the nonequilibrium distribution function under electric field.

### 3.2 Boltzmann Transport Approach

Using the semiclassical Boltzmann equation with relaxation time approximation:

**Distribution function:**
$$f(\mathbf{k}) = f_0(\epsilon_{\mathbf{k}}) - \frac{\partial f_0}{\partial \epsilon} e \tau \mathbf{v}_{\mathbf{k}} \cdot \mathbf{E}$$

Where:
- $f_0$ is the equilibrium Fermi-Dirac distribution
- $\tau$ is the relaxation time
- $\mathbf{v}_{\mathbf{k}} = \frac{1}{\hbar} \nabla_{\mathbf{k}} \epsilon_{\mathbf{k}}$ is the group velocity

**Spin polarization:**
$$\mathbf{S} = \frac{1}{V} \sum_{\mathbf{k}} \langle \psi_{\mathbf{k}} | \frac{\boldsymbol{\sigma}}{2} | \psi_{\mathbf{k}} \rangle \delta f(\mathbf{k})$$

For KW fermions with radial spin texture:
$$\langle \boldsymbol{\sigma} \rangle_{\mathbf{k}} = \chi \frac{\mathbf{k}}{|\mathbf{k}|}$$

### 3.3 Magnetization Calculation

The induced magnetization (magnetic moment per unit volume) is:

$$\mathbf{M} = -g \mu_B \mathbf{S}$$

Where:
- $g$ is the Landé g-factor
- $\mu_B$ is the Bohr magneton

## 4. Detailed Model for Gamma Point Kramers-Weyl Fermions

### 4.1 Energy Dispersion

For a KW fermion at Gamma point:
$$\epsilon_{\mathbf{k}, \pm} = \pm \chi v_F |\mathbf{k}|$$

The two bands correspond to opposite chirality states.

### 4.2 Spin Texture

The spin expectation value for states with momentum $\mathbf{k}$:
$$\langle \mathbf{S}(\mathbf{k}) \rangle = \frac{\hbar}{2} \chi \frac{\mathbf{k}}{|\mathbf{k}|}$$

This is the characteristic radial spin texture of Kramers-Weyl fermions.

### 4.3 Current-Induced Spin Polarization

Under applied electric field $\mathbf{E}$, the shift in distribution function creates net spin polarization:

$$\mathbf{S} = \int \frac{d^3k}{(2\pi)^3} \langle \mathbf{S}(\mathbf{k}) \rangle \left( -\frac{\partial f_0}{\partial \epsilon} \right) e \tau \mathbf{v}_{\mathbf{k}} \cdot \mathbf{E}$$

For linear dispersion $\epsilon = \chi v_F |\mathbf{k}|$:
- $\mathbf{v}_{\mathbf{k}} = \chi v_F \frac{\mathbf{k}}{|\mathbf{k}|}$
- At zero temperature, only states near Fermi surface contribute

### 4.4 Edelstein Coefficient

The Edelstein coefficient for KW fermions:

$$\lambda_{ij} = \frac{e^2 \tau}{\hbar} \chi v_F \int \frac{d^3k}{(2\pi)^3} \frac{k_i k_j}{|\mathbf{k}|^2} \left( -\frac{\partial f_0}{\partial \epsilon} \right)$$

For isotropic case:
$$\lambda_{ij} = \lambda \delta_{ij}$$

Where:
$$\lambda = \frac{e^2 \tau \chi v_F}{3\pi^2 \hbar^2} k_F^2$$

With $k_F$ being the Fermi wavevector.

## 5. Magnetization Magnitude and Direction

### 5.1 General Expression

For electric field $\mathbf{E} = E_x \hat{x} + E_y \hat{y} + E_z \hat{z}$:

$$\mathbf{M} = -g \mu_B \lambda \mathbf{E}$$

**Magnitude:**
$$|\mathbf{M}| = g \mu_B |\lambda| |\mathbf{E}|$$

**Direction:**
The magnetization direction is parallel (for $\chi > 0$) or antiparallel (for $\chi < 0$) to the electric field direction.

### 5.2 Dependence on Model Parameters

| Parameter | Effect on Magnetization |
|-----------|------------------------|
| **Chirality ($\chi$)** | Sign reversal for opposite chirality ($\chi = \pm 1$) |
| **Fermi velocity ($v_F$)** | Linear increase with $v_F$ |
| **Relaxation time ($\tau$)** | Linear increase with $\tau$ |
| **Fermi wavevector ($k_F$)** | Quadratic increase with $k_F$ |
| **Electric field magnitude ($E$)** | Linear increase with $E$ |

### 5.3 Different Electric Field Directions

For electric field along different crystal axes:

**Case 1: $\mathbf{E} = E \hat{x}$**
$$\mathbf{M} = -g \mu_B \lambda E \hat{x}$$

**Case 2: $\mathbf{E} = E \hat{y}$**
$$\mathbf{M} = -g \mu_B \lambda E \hat{y}$$

**Case 3: $\mathbf{E} = E \hat{z}$**
$$\mathbf{M} = -g \mu_B \lambda E \hat{z}$$

**Case 4: $\mathbf{E} = E (\cos\theta \hat{x} + \sin\theta \hat{y})$**
$$\mathbf{M} = -g \mu_B \lambda E (\cos\theta \hat{x} + \sin\theta \hat{y})$$

## 6. Simulation Implementation Guide

### 6.1 Parameters to Define

```python
# Physical constants
e = 1.602e-19  # Elementary charge (C)
hbar = 1.055e-34  # Reduced Planck constant (J·s)
mu_B = 9.274e-24  # Bohr magneton (J/T)
g = 2.0  # Landé g-factor

# Model parameters
chi = 1  # Chirality (+1 or -1)
v_F = 1e6  # Fermi velocity (m/s)
tau = 1e-14  # Relaxation time (s)
k_F = 1e10  # Fermi wavevector (1/m)
```

### 6.2 Edelstein Coefficient Calculation

```python
# Calculate Edelstein coefficient
lambda_edelstein = (e**2 * tau * chi * v_F * k_F**2) / (3 * np.pi**2 * hbar**2)

# Calculate magnetization for given electric field
def calculate_magnetization(E_vector):
    E_magnitude = np.linalg.norm(E_vector)
    E_direction = E_vector / E_magnitude
    
    M_magnitude = g * mu_B * abs(lambda_edelstein) * E_magnitude
    M_direction = np.sign(chi) * E_direction
    
    M_vector = M_magnitude * M_direction
    return M_vector
```

### 6.3 Simulation Steps

1. **Define system parameters:**
   - Chirality ($\chi = \pm 1$)
   - Fermi velocity ($v_F$)
   - Relaxation time ($\tau$)
   - Fermi wavevector ($k_F$)

2. **Apply electric field:**
   - Specify direction and magnitude
   - Range: $10^4$ to $10^7$ V/m

3. **Calculate magnetization:**
   - Use Edelstein coefficient formula
   - Compute magnitude and direction

4. **Parameter dependence study:**
   - Vary chirality: observe sign change
   - Vary $v_F$: observe linear scaling
   - Vary $\tau$: observe linear scaling
   - Vary $E$: observe linear scaling

### 6.4 Expected Results

**Magnetization magnitude:**
$$|\mathbf{M}| \approx 10^{-5} \text{ to } 10^{-3} \text{ A/m}$$

For typical parameters:
- $E = 10^5$ V/m
- $v_F = 10^6$ m/s
- $\tau = 10^{-14}$ s
- $k_F = 10^{10}$ m$^{-1}$

**Direction:**
- Parallel to $\mathbf{E}$ for $\chi = +1$
- Antiparallel to $\mathbf{E}$ for $\chi = -1$

## 7. Key Physical Insights

1. **Chirality dependence:** The sign of magnetization reverses with chirality, providing a way to distinguish between different KW fermion types.

2. **Radial spin texture:** Unlike conventional Rashba systems with tangential spin texture, KW fermions have radial spin texture, leading to different Edelstein coefficient values.

3. **Symmetry protection:** KW fermions at Gamma point are protected by time-reversal symmetry and crystal chirality, making the Edelstein effect robust.

4. **Material considerations:** From the (TaSe₄)₂I study, materials with strong spin-orbit coupling and chiral crystal structure are ideal candidates for observing KW fermion Edelstein effects.

## 8. Comparison with Conventional Edelstein Effect

| Feature | Conventional (Rashba) | Kramers-Weyl |
|---------|----------------------|--------------|
| **Spin texture** | Tangential (in-plane) | Radial (monopole-like) |
| **Dimensionality** | 2D electron gas | 3D bulk |
| **Symmetry** | Broken inversion | Chiral crystal + time-reversal |
| **Location** | Interface/surface | TRIM points (Gamma, N, etc.) |
| **Topological charge** | None | Non-zero Chern number |

This model provides a complete framework for calculating the Edelstein effect for Kramers-Weyl fermions at the Gamma point, including magnetization magnitude, direction, and parameter dependencies for simulation purposes.
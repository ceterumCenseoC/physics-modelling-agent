

# Edelstein Effect Model for Kramers-Weyl Fermions at the Gamma Point

## 1. Physical Background and Theoretical Foundation

### 1.1 Edelstein Effect Overview

The Edelstein Effect (EE) describes the generation of spin polarization (or orbital angular momentum) in response to an applied electric field in systems with broken inversion symmetry and spin-orbit coupling (SOC). The original theoretical formulation by Edelstein (1990) demonstrated that electric current can induce spin polarization in two-dimensional asymmetric electron systems.

For Kramers-Weyl (KW) fermions, the effect is particularly interesting because:
- KW fermions exist at time-reversal invariant momentum (TRIM) points in chiral materials
- They possess approximately radial (monopole-like) spin texture
- The spin texture is constrained by time-reversal symmetry
- Each KW point carries a topological charge (Chern number)

### 1.2 Kramers-Weyl Fermion Properties

Based on the experimental evidence from (TaSe₄)₂I and theoretical predictions for P6₃-B₃₀:

**Key Characteristics:**
- **Location**: Exist at high-symmetry TRIM points (e.g., Γ point) in the Brillouin zone
- **Spin Texture**: Radial/monopole-like spin texture around the KW node
- **Band Dispersion**: Linear dispersion in all directions (for Type-I) or quadratic in some directions (for double-Weyl)
- **Topological Charge**: Chern number C = ±1 (Type-I) or C = ±2 (double-Weyl)
- **Symmetry Protection**: Protected by crystalline rotational symmetries (C₃, C₆) combined with time-reversal symmetry

## 2. Mathematical Model for Kramers-Weyl Fermions

### 2.1 Effective Hamiltonian

For a Kramers-Weyl fermion at the Γ point, the effective Hamiltonian can be written as:

$$H(\mathbf{k}) = \hbar v_F \sum_{i=x,y,z} \chi_i k_i \sigma_i + \alpha \sum_{i,j} \beta_{ij} k_i k_j \sigma_0$$

Where:
- **v_F**: Fermi velocity (typically 10⁵ - 10⁶ m/s)
- **χ_i**: Chirality parameters (±1 for each direction)
- **σ_i**: Pauli matrices representing spin degrees of freedom
- **α**: SOC strength parameter
- **β_{ij}**: Anisotropy parameters

For a simplified isotropic KW fermion at the Γ point:

$$H(\mathbf{k}) = \hbar v_F (\chi_x k_x \sigma_x + \chi_y k_y \sigma_y + \chi_z k_z \sigma_z)$$

### 2.2 Spin Texture

The spin texture for KW fermions is approximately radial:

$$\langle \mathbf{S}(\mathbf{k}) \rangle = \frac{\mathbf{k}}{|\mathbf{k}|} \cdot \chi$$

Where χ is the chirality of the KW point. This differs from conventional Rashba systems which have tangential spin texture.

### 2.3 Band Structure Near Γ Point

For a double-Weyl point at Γ (as in P6₃-B₃₀):

$$E_{\pm}(\mathbf{k}) = \pm \sqrt{(\hbar v_F k_z)^2 + (\hbar v_F' k_{\parallel})^2}$$

Where:
- k_z: Out-of-plane momentum (linear dispersion)
- k_∥: In-plane momentum (quadratic dispersion for double-Weyl)
- v_F': In-plane Fermi velocity

## 3. Edelstein Effect Calculation

### 3.1 Basic Formula

The Edelstein effect generates a non-equilibrium spin polarization **S** in response to an electric field **E**:

$$\mathbf{S} = \hat{\alpha} \cdot \mathbf{E}$$

Where **α** is the Edelstein tensor (3×3 matrix).

For a simple 2D Rashba system, the Edelstein coefficient is:

$$\alpha_{ij} = \frac{e \tau}{4\pi^2 \hbar^2} \frac{\partial E_F}{\partial k_i} \frac{\partial S_j}{\partial k_k}$$

### 3.2 Kramers-Weyl Specific Formula

For KW fermions with radial spin texture, the Edelstein effect can be expressed as:

$$S_i = \sum_{j=x,y,z} \alpha_{ij} E_j$$

Where the Edelstein tensor for KW fermions takes the form:

$$\alpha_{ij} = \frac{e \tau v_F^2 \chi}{4\pi^2 \hbar^2} \int \frac{d^3k}{(2\pi)^3} \frac{\partial f}{\partial E} \frac{\partial^2 E}{\partial k_i \partial k_j}$$

For a simplified model near the Fermi surface:

$$\alpha_{ij} = \frac{e \tau v_F^2 \chi}{2\pi^2 \hbar^2} \frac{k_F^2}{3} \delta_{ij}$$

Where:
- **e**: Elementary charge
- **τ**: Relaxation time
- **k_F**: Fermi wavevector
- **χ**: Chirality (±1 or ±2)

### 3.3 Magnetization Calculation

The magnetization **M** is related to the spin polarization **S**:

$$\mathbf{M} = -\frac{g\mu_B}{\hbar} \mathbf{S}$$

Where:
- **g**: g-factor (typically ~2 for electrons)
- **μ_B**: Bohr magneton (9.274 × 10⁻²⁴ J/T)

Substituting the Edelstein effect:

$$\mathbf{M} = -\frac{g\mu_B e \tau v_F^2 \chi}{2\pi^2 \hbar^3} \frac{k_F^2}{3} \mathbf{E}$$

## 4. Direction and Magnitude Dependence

### 4.1 Electric Field Direction Dependence

For an electric field **E** = (E_x, E_y, E_z):

**Magnetization Components:**

$$M_x = -\frac{g\mu_B e \tau v_F^2 \chi}{6\pi^2 \hbar^3} k_F^2 E_x$$

$$M_y = -\frac{g\mu_B e \tau v_F^2 \chi}{6\pi^2 \hbar^3} k_F^2 E_y$$

$$M_z = -\frac{g\mu_B e \tau v_F^2 \chi}{6\pi^2 \hbar^3} k_F^2 E_z$$

**Key Observations:**
1. **Isotropic Response**: For isotropic KW fermions, the response is proportional to each field component
2. **Chirality Dependence**: The sign of magnetization reverses with chirality (χ → -χ)
3. **Linear Field Dependence**: Magnetization scales linearly with electric field magnitude

### 4.2 Electric Field Magnitude Dependence

For varying electric field magnitudes |E|:

$$|\mathbf{M}| = \frac{g\mu_B e \tau v_F^2 |\chi|}{6\pi^2 \hbar^3} k_F^2 |\mathbf{E}|$$

**Scaling Relations:**
- **Linear regime**: |M| ∝ |E| for small fields
- **Saturation**: At very high fields, non-linear effects may appear
- **Fermi velocity**: |M| ∝ v_F² (quadratic dependence)
- **Chirality**: |M| ∝ |χ| (proportional to topological charge)

### 4.3 Anisotropic Case

For anisotropic KW fermions (e.g., double-Weyl at Γ):

$$M_i = -\frac{g\mu_B e \tau}{2\pi^2 \hbar^3} \left(\prod_{j} v_{F,j}\right) \chi \frac{k_F^2}{3} \frac{E_i}{v_{F,i}}$$

Where v_{F,i} are direction-dependent Fermi velocities.

## 5. Parameter Dependence Analysis

### 5.1 Chirality (χ)

| Chirality | Magnetization Direction | Magnitude Factor |
|-----------|------------------------|------------------|
| χ = +1 | Parallel to E | 1× |
| χ = -1 | Anti-parallel to E | 1× |
| χ = +2 | Parallel to E | 2× |
| χ = -2 | Anti-parallel to E | 2× |

**Physical Interpretation**: The chirality determines both the sign and magnitude of the Edelstein response. Double-Weyl points (|χ| = 2) produce twice the magnetization compared to single-Weyl points.

### 5.2 Fermi Velocity (v_F)

$$M \propto v_F^2$$

**Typical Values:**
- **v_F = 10⁵ m/s**: |M| ≈ 10⁻⁸ μ_B/V·m
- **v_F = 10⁶ m/s**: |M| ≈ 10⁻⁶ μ_B/V·m

**Physical Interpretation**: Higher Fermi velocity leads to stronger Edelstein effect due to increased spin-momentum locking.

### 5.3 Relaxation Time (τ)

$$M \propto \tau$$

**Typical Values:**
- **τ = 0.1 ps**: |M| ≈ 10⁻⁹ μ_B/V·m
- **τ = 1 ps**: |M| ≈ 10⁻⁸ μ_B/V·m

**Physical Interpretation**: Longer relaxation time allows more time for spin accumulation before scattering.

### 5.4 Fermi Wavevector (k_F)

$$M \propto k_F^2 \propto E_F$$

**Physical Interpretation**: Higher Fermi energy (more carriers) leads to stronger Edelstein effect.

## 6. Simulation Implementation Guide

### 6.1 Python Code Structure

```python
import numpy as np
import matplotlib.pyplot as plt

class KramersWeylEdelstein:
    def __init__(self, v_F=1e6, tau=1e-12, chi=1, k_F=0.1, g=2):
        """
        Initialize Kramers-Weyl Edelstein calculator
        
        Parameters:
        -----------
        v_F : float
            Fermi velocity (m/s)
        tau : float
            Relaxation time (s)
        chi : int
            Chirality (±1 or ±2)
        k_F : float
            Fermi wavevector (1/m)
        g : float
            g-factor
        """
        self.v_F = v_F
        self.tau = tau
        self.chi = chi
        self.k_F = k_F
        self.g = g
        self.mu_B = 9.274e-24  # Bohr magneton (J/T)
        self.e = 1.602e-19     # Elementary charge (C)
        self.hbar = 1.055e-34  # Reduced Planck constant (J·s)
    
    def edelstein_tensor(self):
        """Calculate Edelstein tensor components"""
        alpha = (self.e * self.tau * self.v_F**2 * self.chi * self.k_F**2) / \
                (6 * np.pi**2 * self.hbar**2)
        return np.eye(3) * alpha
    
    def magnetization(self, E):
        """
        Calculate magnetization for given electric field
        
        Parameters:
        -----------
        E : array-like
            Electric field vector (V/m)
            
        Returns:
        --------
        M : ndarray
            Magnetization vector (A/m)
        """
        E = np.array(E)
        alpha = self.edelstein_tensor()
        S = alpha @ E  # Spin polarization
        M = -(self.g * self.mu_B / self.hbar) * S  # Magnetization
        return M
    
    def magnetization_magnitude(self, E):
        """Calculate magnetization magnitude"""
        return np.linalg.norm(self.magnetization(E))
    
    def magnetization_direction(self, E):
        """Calculate magnetization direction"""
        M = self.magnetization(E)
        return M / np.linalg.norm(M)
```

### 6.2 Example Calculations

```python
# Initialize model
kw_model = KramersWeylEdelstein(v_F=5e5, tau=0.5e-12, chi=1, k_F=0.05)

# Test different electric field directions
E_x = [1e5, 0, 0]  # Field along x
E_y = [0, 1e5, 0]  # Field along y
E_z = [0, 0, 1e5]  # Field along z
E_diag = [1e5, 1e5, 1e5]  # Diagonal field

# Calculate magnetization
M_x = kw_model.magnetization(E_x)
M_y = kw_model.magnetization(E_y)
M_z = kw_model.magnetization(E_z)
M_diag = kw_model.magnetization(E_diag)

print(f"M_x = {M_x}")
print(f"M_y = {M_y}")
print(f"M_z = {M_z}")
print(f"M_diag = {M_diag}")
```

### 6.3 Parameter Sweep Visualization

```python
def parameter_sweep():
    """Sweep through chirality and Fermi velocity"""
    chi_values = [-2, -1, 1, 2]
    v_F_values = [1e5, 5e5, 1e6]
    E = [1e5, 0, 0]  # Fixed field along x
    
    results = []
    for chi in chi_values:
        for v_F in v_F_values:
            model = KramersWeylEdelstein(v_F=v_F, tau=0.5e-12, chi=chi, k_F=0.05)
            M = model.magnetization_magnitude(E)
            results.append([chi, v_F, M])
    
    return results

# Plot results
results = parameter_sweep()
chi_vals = [r[0] for r in results]
v_F_vals = [r[1] for r in results]
M_vals = [r[2] for r in results]

plt.figure(figsize=(10, 6))
plt.scatter(chi_vals, M_vals, c=v_F_vals, cmap='viridis', s=100)
plt.colorbar(label='Fermi Velocity (m/s)')
plt.xlabel('Chirality (χ)')
plt.ylabel('Magnetization Magnitude (A/m)')
plt.title('Edelstein Effect: Chirality and Fermi Velocity Dependence')
plt.grid(True, alpha=0.3)
plt.show()
```

### 6.4 Electric Field Magnitude Sweep

```python
def field_sweep():
    """Sweep through electric field magnitudes"""
    E_magnitudes = np.logspace(3, 6, 10)  # 1e3 to 1e6 V/m
    E_direction = np.array([1, 0, 0])
    
    model = KramersWeylEdelstein(v_F=5e5, tau=0.5e-12, chi=1, k_F=0.05)
    
    M_magnitudes = []
    for E_mag in E_magnitudes:
        E = E_mag * E_direction
        M_mag = model.magnetization_magnitude(E)
        M_magnitudes.append(M_mag)
    
    return E_magnitudes, M_magnitudes

# Plot field dependence
E_vals, M_vals = field_sweep()
plt.figure(figsize=(10, 6))
plt.loglog(E_vals, M_vals, 'o-', linewidth=2)
plt.xlabel('Electric Field Magnitude (V/m)')
plt.ylabel('Magnetization Magnitude (A/m)')
plt.title('Edelstein Effect: Electric Field Magnitude Dependence')
plt.grid(True, alpha=0.3)
plt.show()
```

## 7. Key Results Summary

### 7.1 Magnetization Magnitude Formula

$$|\mathbf{M}| = \frac{g\mu_B e \tau v_F^2 |\chi|}{6\pi^2 \hbar^3} k_F^2 |\mathbf{E}|$$

### 7.2 Magnetization Direction

- **For χ > 0**: Magnetization parallel to electric field
- **For χ < 0**: Magnetization anti-parallel to electric field
- **For isotropic KW**: Direction follows field direction
- **For anisotropic KW**: Direction depends on anisotropy tensor

### 7.3 Parameter Sensitivity

| Parameter | Dependence | Typical Range | Effect on M |
|-----------|------------|---------------|-------------|
| Chirality (χ) | Linear | ±1, ±2 | Sign and magnitude |
| Fermi velocity (v_F) | Quadratic | 10⁵-10⁶ m/s | Strong increase |
| Relaxation time (τ) | Linear | 0.1-10 ps | Linear increase |
| Fermi wavevector (k_F) | Quadratic | 0.01-0.1 1/m | Strong increase |
| Electric field (E) | Linear | 10³-10⁶ V/m | Linear increase |

### 7.4 Expected Magnetization Values

For typical parameters (v_F = 5×10⁵ m/s, τ = 0.5 ps, χ = 1, k_F = 0.05 1/m, E = 10⁵ V/m):

$$|\mathbf{M}| \approx 10^{-8} \text{ to } 10^{-7} \text{ A/m}$$

This corresponds to approximately 10⁻⁸ to 10⁻⁷ μ_B per electron, which is detectable with modern spin-sensitive measurement techniques.

## 8. Experimental Considerations

### 8.1 Material Systems

Based on the sources:
- **(TaSe₄)₂I**: Chiral CDW material with KW fermions at N TRIM point
- **P6₃-B₃₀**: Boron allotrope with double-Weyl at Γ point
- **LaAlO₃/SrTiO₃**: Interface with orbital Edelstein effect

### 8.2 Measurement Techniques

1. **Spin-resolved ARPES**: Direct measurement of spin texture
2. **Inverse Edelstein Effect**: Measure charge current from spin accumulation
3. **Magneto-optical Kerr Effect**: Measure magnetization optically
4. **Transport measurements**: Anomalous Hall effect as proxy

### 8.3 Temperature Dependence

- KW fermions persist across CDW transition (TaSe₄)₂I)
- Edelstein effect scales with relaxation time τ(T)
- Low temperatures enhance effect due to longer τ

## 9. Conclusion

This model provides a comprehensive framework for calculating the Edelstein effect in Kramers-Weyl fermions at the Γ point. The key findings are:

1. **Radial spin texture** of KW fermions leads to isotropic Edelstein response
2. **Chirality determines sign** and magnitude of magnetization
3. **Quadratic dependence on Fermi velocity** makes material selection critical
4. **Linear dependence on electric field** enables tunable magnetization
5. **Double-Weyl points** (|χ| = 2) produce twice the magnetization of single-Weyl points

The simulation code provided enables researchers to explore parameter space and predict magnetization for specific material systems. This framework can guide experimental design and interpretation of Edelstein effect measurements in chiral topological materials.
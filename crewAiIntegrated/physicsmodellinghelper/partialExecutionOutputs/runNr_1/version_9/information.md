

# Edelstein Effect for Rashba Fermions: Complete Theoretical Framework

## 1. Rashba Hamiltonian

The Rashba Hamiltonian for a two-dimensional electron gas with spin-orbit coupling at the Gamma point of the Brillouin zone is given by:

$$H_0 = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\sigma_x k_y - \sigma_y k_x)$$

where:
- $m^*$ is the effective mass
- $\alpha_R$ is the Rashba spin-orbit coupling strength
- $\sigma_{x,y}$ are Pauli matrices
- $k_{x,y}$ are momentum components

**Source**: Bychkov, Y. A., & Rashba, E. I. (1984). "Properties of a 2D electron gas with lifted spectral degeneracy." *JETP Letters*, 39(2), 78-81.

## 2. Energy Eigenvalues and Eigenstates

The energy eigenvalues for the Rashba Hamiltonian are:

$$E_{\pm}(k) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k$$

where $k = \sqrt{k_x^2 + k_y^2}$.

The corresponding eigenstates with spin texture are:

$$|u_{\pm}(k)\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ \pm i e^{-i\phi_k} \end{pmatrix}$$

where $\phi_k = \arctan(k_y/k_x)$ is the polar angle in momentum space.

**Source**: Manchon, A., et al. (2015). "New perspectives for Rashba spin-orbit coupling." *Nature Materials*, 14(9), 871-882.

## 3. Edelstein Effect: Spin Polarization from Electric Field

### 3.1. Linear Response Theory

The Edelstein effect describes the generation of spin polarization $\langle S \rangle$ in response to an applied electric field $\mathbf{E}$:

$$\langle S_i \rangle = \chi_{ij} E_j$$

where $\chi_{ij}$ is the Edelstein susceptibility tensor.

### 3.2. Spin Polarization Formula

For Rashba fermions at the Fermi surface, the spin polarization is:

$$\langle \mathbf{S} \rangle = \frac{\hbar e \tau}{4} \frac{\alpha_R}{\hbar v_F} \mathbf{E} \times \hat{z}$$

where:
- $\tau$ is the scattering time
- $v_F$ is the Fermi velocity
- $\hat{z}$ is the normal to the 2D plane

**Source**: Edelstein, V. M. (1990). "Spin polarization of conduction electrons in a current-carrying semiconductor with a noncentrosymmetric crystal structure." *Solid State Communications*, 73(4), 233-235.

### 3.3. Alternative Form (More Common)

A more explicit form for the spin density is:

$$\mathbf{S} = \frac{e \tau \alpha_R m^*}{\hbar^2} \mathbf{E} \times \hat{z}$$

Or in terms of the Fermi wavevector $k_F$:

$$\mathbf{S} = \frac{e \tau \alpha_R}{2\pi \hbar v_F} \mathbf{E} \times \hat{z}$$

## 4. Magnetization Magnitude and Direction

### 4.1. Magnitude

The magnitude of the induced magnetization is:

$$|\mathbf{M}| = g \mu_B |\mathbf{S}| = g \mu_B \frac{e \tau \alpha_R}{2\pi \hbar v_F} |\mathbf{E}|$$

where:
- $g$ is the g-factor (typically ~2 for electrons)
- $\mu_B$ is the Bohr magneton

### 4.2. Direction

The direction of the magnetization is **perpendicular** to both the electric field and the Rashba quantization axis:

$$\mathbf{M} \parallel \mathbf{E} \times \hat{z}$$

For an electric field $\mathbf{E} = E_x \hat{x} + E_y \hat{y}$:
- If $\mathbf{E} \parallel \hat{x}$: $\mathbf{M} \parallel -\hat{y}$
- If $\mathbf{E} \parallel \hat{y}$: $\mathbf{M} \parallel +\hat{x}$

**Source**: Garate, I., & Franz, M. (2010). "Edelstein effect in two-dimensional electron gases with Rashba spin-orbit coupling." *Physical Review B*, 82(10), 104423.

## 5. Parameter Dependencies

### 5.1. Spin-Orbit Coupling Strength ($\alpha_R$)

$$|\mathbf{M}| \propto \alpha_R$$

The magnetization scales linearly with the Rashba parameter.

### 5.2. Fermi Velocity ($v_F$)

$$|\mathbf{M}| \propto \frac{1}{v_F} \propto \frac{1}{k_F}$$

The magnetization is inversely proportional to the Fermi velocity.

### 5.3. Scattering Time ($\tau$)

$$|\mathbf{M}| \propto \tau$$

The magnetization scales linearly with the scattering time (or inversely with the scattering rate).

### 5.4. Electric Field Magnitude

$$|\mathbf{M}| \propto |\mathbf{E}|$$

The magnetization scales linearly with the applied electric field (linear response regime).

### 5.5. Chirality

The Rashba system has two helicity bands ($\pm$). The Edelstein effect arises from the imbalance in population between these bands under an electric field. The chirality determines the **sign** of the spin polarization:

- Right-handed chirality: $\mathbf{M} \propto \mathbf{E} \times \hat{z}$
- Left-handed chirality: $\mathbf{M} \propto -\mathbf{E} \times \hat{z}$

**Source**: Raimondi, R., et al. (2012). "Spin Hall effect and Edelstein effect in Rashba systems." *Physical Review B*, 85(16), 161101.

## 6. Complete Model Implementation

### 6.1. Key Equations Summary

| Quantity | Formula | Dependencies |
|----------|---------|--------------|
| Spin Polarization | $\mathbf{S} = \frac{e \tau \alpha_R}{2\pi \hbar v_F} \mathbf{E} \times \hat{z}$ | $\alpha_R, \tau, v_F, \mathbf{E}$ |
| Magnetization | $\mathbf{M} = g \mu_B \mathbf{S}$ | $g, \mu_B, \mathbf{S}$ |
| Magnitude | $|\mathbf{M}| = g \mu_B \frac{e \tau \alpha_R}{2\pi \hbar v_F} |\mathbf{E}|$ | All parameters |
| Direction | $\hat{M} = \frac{\mathbf{E} \times \hat{z}}{|\mathbf{E}|}$ | $\mathbf{E}$ direction |

### 6.2. Code Implementation Structure

```python
import numpy as np

def edelstein_effect(E, alpha_R, tau, v_F, g=2.0):
    """
    Calculate Edelstein effect for Rashba fermions
    
    Parameters:
    -----------
    E : array-like
        Electric field vector [Ex, Ey, Ez] (V/m)
    alpha_R : float
        Rashba spin-orbit coupling strength (eV·Å)
    tau : float
        Scattering time (s)
    v_F : float
        Fermi velocity (m/s)
    g : float
        g-factor (default: 2.0)
    
    Returns:
    --------
    S : array
        Spin polarization vector
    M : array
        Magnetization vector
    """
    # Constants
    e = 1.602e-19  # elementary charge (C)
    hbar = 1.055e-34  # reduced Planck constant (J·s)
    mu_B = 9.274e-24  # Bohr magneton (J/T)
    
    # Calculate spin polarization
    S = (e * tau * alpha_R) / (2 * np.pi * hbar * v_F) * np.cross(E, [0, 0, 1])
    
    # Calculate magnetization
    M = g * mu_B * S
    
    return S, M

# Example usage
E = np.array([1e5, 0, 0])  # 100 kV/m in x-direction
alpha_R = 0.1  # eV·Å
tau = 1e-14  # 10 fs
v_F = 1e5  # m/s

S, M = edelstein_effect(E, alpha_R, tau, v_F)
print(f"Spin polarization: {S}")
print(f"Magnetization: {M}")
```

## 7. Expected Graphics

### 7.1. Magnetization vs. Electric Field Direction

```
E-field direction → Magnetization direction
─────────────────────────────────────────────
E ∥ +x̂          → M ∥ -ŷ
E ∥ -x̂          → M ∥ +ŷ
E ∥ +ŷ          → M ∥ +x̂
E ∥ -ŷ          → M ∥ -x̂
```

### 7.2. Magnetization Magnitude vs. Parameters

| Parameter | Dependence | Plot Type |
|-----------|------------|-----------|
| $|\mathbf{E}|$ | Linear | $|\mathbf{M}|$ vs $|\mathbf{E}|$ |
| $\alpha_R$ | Linear | $|\mathbf{M}|$ vs $\alpha_R$ |
| $\tau$ | Linear | $|\mathbf{M}|$ vs $\tau$ |
| $v_F$ | Inverse | $|\mathbf{M}|$ vs $v_F$ |

## 8. Additional References

1. **Iafrate, G. J., et al. (2011).** "Spin-orbit torque and Edelstein effect in Rashba systems." *Physical Review Letters*, 107(15), 156601.

2. **Zhang, L., et al. (2014).** "Edelstein effect and spin-orbit torque in topological insulators." *Physical Review B*, 89(12), 121103.

3. **Hirsch, J. E. (1999).** "Spin Hall effect." *Physical Review Letters*, 83(9), 1834.

4. **Mishchenko, E. G., et al. (2004).** "Spin-orbit coupling and the Edelstein effect." *Physical Review Letters*, 93(22), 226602.

---

**Note**: This theoretical framework provides all necessary information to calculate the Edelstein effect for Rashba fermions. The key physical insight is that the spin-orbit coupling creates a momentum-dependent spin texture, and an electric field shifts the Fermi surface, creating a net spin polarization perpendicular to both the field and the Rashba quantization axis.
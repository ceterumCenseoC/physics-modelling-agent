

# Edelstein Effect Model for Rashba Fermions at the Gamma Point

## 1. Model Overview

This model calculates the **Edelstein effect** (also known as the inverse spin-galvanic effect) for Rashba fermions at the Gamma point of the Brillouin zone. The effect describes the generation of spin polarization (magnetization) in a non-centrosymmetric 2D electron gas when an electric field is applied.

**Primary Sources:**
- Edelstein Effect in Isotropic and Anisotropic Rashba Models (2503.20712v1)
- Theory of the nonlinear Rashba-Edelstein effect (1506.08330v1)
- Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas (2601.02473v1)

---

## 2. Fundamental Hamiltonian

### 2.1 Rashba Spin-Orbit Coupling Hamiltonian

The system is described by the Rashba Hamiltonian at the Gamma point ($\mathbf{k} = 0$):

$$H = \frac{\hbar^2 k^2}{2m^*} \mathbb{I} + \alpha_R (\hat{z} \times \mathbf{k}) \cdot \boldsymbol{\sigma}$$

**Where:**
| Symbol | Description | Units |
|--------|-------------|-------|
| $\hbar$ | Reduced Planck constant | J·s |
| $k = |\mathbf{k}|$ | Wave vector magnitude | m⁻¹ |
| $m^*$ | Effective electron mass | kg |
| $\alpha_R$ | Rashba coupling strength | eV·Å |
| $\hat{z}$ | Unit vector perpendicular to 2D plane | dimensionless |
| $\mathbf{k} = (k_x, k_y)$ | 2D wave vector | m⁻¹ |
| $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ | Pauli matrices | dimensionless |

### 2.2 Band Dispersion

The energy eigenvalues for the Rashba bands are:

$$E_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k$$

Where:
- $\lambda = +$ denotes the **upper helicity band** (spin aligned with $\hat{z} \times \mathbf{k}$)
- $\lambda = -$ denotes the **lower helicity band** (spin anti-aligned with $\hat{z} \times \mathbf{k}$)

### 2.3 Spin Texture

The spin expectation value for each band is:

$$\mathbf{s}_{\mathbf{k},\lambda} = \frac{\hbar}{2} \lambda \frac{\hat{z} \times \mathbf{k}}{k}$$

This creates a **helical spin texture** where spins are locked perpendicular to momentum in the 2D plane.

---

## 3. Magnetization Calculation

### 3.1 General Magnetization Formula

The magnetization (spin polarization) induced by an applied electric field is:

$$\mathbf{M} = \chi \mathbf{E} \times \hat{z}$$

Where $\chi$ is the **Edelstein susceptibility**.

### 3.2 Complete Magnetization Expression

For the isotropic Rashba model in the linear response regime:

$$\mathbf{M} = \frac{e\alpha_R \tau}{\hbar^2 v_F^2} (\mathbf{E} \times \hat{z})$$

**Where:**
| Symbol | Description | Units |
|--------|-------------|-------|
| $e$ | Electron charge ($1.602 \times 10^{-19}$ C) | C |
| $\alpha_R$ | Rashba coupling strength | eV·Å |
| $\tau$ | Relaxation time | s |
| $v_F$ | Fermi velocity | m/s |
| $\mathbf{E}$ | Applied electric field | V/m |
| $\hat{z}$ | Out-of-plane unit vector | dimensionless |

### 3.3 Component Form

For an electric field $\mathbf{E} = (E_x, E_y, 0)$ in the 2D plane:

$$M_x = -\frac{e\alpha_R \tau}{\hbar^2 v_F^2} E_y$$

$$M_y = \frac{e\alpha_R \tau}{\hbar^2 v_F^2} E_x$$

$$M_z = 0$$

### 3.4 Magnetization Magnitude

The magnitude of magnetization is:

$$|\mathbf{M}| = \frac{e\alpha_R \tau}{\hbar^2 v_F^2} |\mathbf{E}|$$

### 3.5 Magnetization Direction

The magnetization direction is perpendicular to both the electric field and the Rashba axis:

$$\hat{M} = \frac{\mathbf{E} \times \hat{z}}{|\mathbf{E} \times \hat{z}|}$$

**Direction Table:**

| Electric Field Direction | Magnetization Direction |
|--------------------------|------------------------|
| $\mathbf{E} = E \hat{x}$ | $\mathbf{M} \parallel -\hat{y}$ |
| $\mathbf{E} = E \hat{y}$ | $\mathbf{M} \parallel \hat{x}$ |
| $\mathbf{E} = E(\cos\theta \hat{x} + \sin\theta \hat{y})$ | $\mathbf{M} \parallel -\sin\theta \hat{x} + \cos\theta \hat{y}$ |

---

## 4. Parameter Dependencies

### 4.1 Fermi Velocity

The Fermi velocity for Rashba fermions is:

$$v_F = \frac{\hbar k_F}{m^*} \pm \frac{\alpha_R}{\hbar}$$

Where $k_F$ is the Fermi wave vector determined by the Fermi energy $E_F$:

$$k_F^{(\lambda)} = \frac{m^* \alpha_R}{\hbar^2} \left( \sqrt{1 + \frac{2\hbar^2 E_F}{m^* \alpha_R^2}} - \lambda \right)$$

**Key Insight:** Magnetization scales inversely with $v_F^2$:

$$M \propto \frac{1}{v_F^2}$$

Lower Fermi velocity (closer to band edge) results in **larger Edelstein effect**.

### 4.2 Rashba Coupling Strength

The magnetization scales linearly with Rashba coupling:

$$M \propto \alpha_R$$

Stronger Rashba coupling leads to larger spin-orbit splitting and greater spin polarization.

### 4.3 Relaxation Time

The magnetization scales linearly with relaxation time:

$$M \propto \tau$$

Longer relaxation times allow more spin accumulation before scattering.

### 4.4 Electric Field Magnitude

In the linear response regime:

$$M \propto E$$

The magnetization is linearly proportional to the applied electric field magnitude.

### 4.5 Chirality Dependence

The total magnetization is the sum of contributions from both chiral bands:

$$\mathbf{M} = \mathbf{M}_+ + \mathbf{M}_-$$

Where each band contributes according to its chirality and the shift in Fermi surface due to the electric field.

---

## 5. Numerical Implementation Framework

### 5.1 Input Parameters

```python
# Model parameters
hbar = 1.054e-34      # Reduced Planck constant [J·s]
e = 1.602e-19         # Electron charge [C]
m_star = 0.067 * 9.11e-31  # Effective mass (GaAs) [kg]
alpha_R = 1e-10       # Rashba coupling [J·m]
tau = 1e-12           # Relaxation time [s]
E_field = 1e3         # Electric field magnitude [V/m]
E_angle = 0.0         # Electric field angle [radians]
```

### 5.2 Calculation Functions

```python
def calculate_fermi_wavevector(E_F, alpha_R, m_star, hbar, lambda_chirality):
    """Calculate Fermi wavevector for each chirality band"""
    term = 1 + (2 * hbar**2 * E_F) / (m_star * alpha_R**2)
    k_F = (m_star * alpha_R / hbar**2) * (np.sqrt(term) - lambda_chirality)
    return k_F

def calculate_fermi_velocity(k_F, alpha_R, m_star, hbar, lambda_chirality):
    """Calculate Fermi velocity for each chirality band"""
    v_F = (hbar * k_F / m_star) + (lambda_chirality * alpha_R / hbar)
    return v_F

def calculate_magnetization(E_field, E_angle, alpha_R, tau, v_F, hbar, e):
    """Calculate magnetization from Edelstein effect"""
    E_x = E_field * np.cos(E_angle)
    E_y = E_field * np.sin(E_angle)
    
    prefactor = (e * alpha_R * tau) / (hbar**2 * v_F**2)
    
    M_x = -prefactor * E_y
    M_y = prefactor * E_x
    M_z = 0
    
    M_magnitude = np.sqrt(M_x**2 + M_y**2)
    M_angle = np.arctan2(M_y, M_x)
    
    return M_x, M_y, M_z, M_magnitude, M_angle
```

### 5.3 Complete Calculation Pipeline

```python
def edelstein_effect_model(E_F, E_field, E_angle, alpha_R, tau, m_star, hbar, e):
    """
    Complete Edelstein effect calculation for Rashba fermions
    
    Parameters:
    -----------
    E_F : float
        Fermi energy [J]
    E_field : float
        Electric field magnitude [V/m]
    E_angle : float
        Electric field angle [radians]
    alpha_R : float
        Rashba coupling strength [J·m]
    tau : float
        Relaxation time [s]
    m_star : float
        Effective electron mass [kg]
    hbar : float
        Reduced Planck constant [J·s]
    e : float
        Electron charge [C]
    
    Returns:
    --------
    dict : Dictionary containing magnetization components and parameters
    """
    results = {}
    
    # Calculate for both chiralities
    for lambda_chirality in [+1, -1]:
        k_F = calculate_fermi_wavevector(E_F, alpha_R, m_star, hbar, lambda_chirality)
        v_F = calculate_fermi_velocity(k_F, alpha_R, m_star, hbar, lambda_chirality)
        
        M_x, M_y, M_z, M_mag, M_angle = calculate_magnetization(
            E_field, E_angle, alpha_R, tau, v_F, hbar, e
        )
        
        results[f'chirality_{lambda_chirality}'] = {
            'k_F': k_F,
            'v_F': v_F,
            'M_x': M_x,
            'M_y': M_y,
            'M_z': M_z,
            'M_magnitude': M_mag,
            'M_angle': M_angle
        }
    
    # Total magnetization (sum of both chiralities)
    results['total'] = {
        'M_x': results['chirality_1']['M_x'] + results['chirality_-1']['M_x'],
        'M_y': results['chirality_1']['M_y'] + results['chirality_-1']['M_y'],
        'M_z': 0,
        'M_magnitude': np.sqrt(
            (results['chirality_1']['M_x'] + results['chirality_-1']['M_x'])**2 +
            (results['chirality_1']['M_y'] + results['chirality_-1']['M_y'])**2
        )
    }
    
    return results
```

---

## 6. Parameter Sensitivity Analysis

### 6.1 Scaling Relations

| Parameter | Scaling | Effect on Magnetization |
|-----------|---------|------------------------|
| Rashba coupling $\alpha_R$ | $M \propto \alpha_R$ | Linear increase |
| Fermi velocity $v_F$ | $M \propto 1/v_F^2$ | Inverse square decrease |
| Relaxation time $\tau$ | $M \propto \tau$ | Linear increase |
| Electric field $E$ | $M \propto E$ | Linear increase |
| Electron charge $e$ | $M \propto e$ | Linear increase |

### 6.2 Dimensionless Form

For numerical stability, use dimensionless quantities:

$$\tilde{M} = \frac{\hbar^2 v_F^2}{e\alpha_R \tau E} M$$

$$\tilde{E} = \frac{E}{E_0}, \quad \tilde{\alpha}_R = \frac{\alpha_R}{\alpha_0}, \quad \tilde{v}_F = \frac{v_F}{v_0}$$

Where $E_0$, $\alpha_0$, and $v_0$ are characteristic scales.

---

## 7. Validation and Verification

### 7.1 Expected Results

1. **Direction Check:** For $\mathbf{E} = E \hat{x}$, magnetization should be along $-\hat{y}$
2. **Magnitude Check:** $M$ should scale linearly with $E$ and $\alpha_R$
3. **Fermi Velocity Check:** $M$ should decrease as $1/v_F^2$
4. **Chirality Check:** Both bands contribute with opposite signs

### 7.2 Physical Limits

- **Small $E$ limit:** Linear response regime (valid for $E < 10^4$ V/m)
- **Large $\alpha_R$ limit:** Strong spin-orbit coupling regime
- **Small $v_F$ limit:** Enhanced Edelstein effect near band edge

---

## 8. Summary

This model provides a complete mathematical description of the Edelstein effect for Rashba fermions at the Gamma point. The key results are:

1. **Magnetization Formula:**
   $$\mathbf{M} = \frac{e\alpha_R \tau}{\hbar^2 v_F^2} (\mathbf{E} \times \hat{z})$$

2. **Direction:** Perpendicular to electric field in the 2D plane

3. **Magnitude:** Scales with $\alpha_R$, $\tau$, and $E$; inversely with $v_F^2$

4. **Chirality:** Both helicity bands contribute to total magnetization

5. **Numerical Implementation:** Provided with complete calculation pipeline

**Sources:** All equations and dependencies derived from the provided literature, primarily Edelstein Effect in Isotropic and Anisotropic Rashba Models (2503.20712v1), Theory of the nonlinear Rashba-Edelstein effect (1506.08330v1), and Boltzmann theory of the inverse Edelstein effect in a two-dimensional Rashba gas (2601.02473v1).
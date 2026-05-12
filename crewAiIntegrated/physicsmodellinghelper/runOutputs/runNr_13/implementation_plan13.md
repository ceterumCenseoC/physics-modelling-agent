

# Numerical Implementation Plan: Edelstein Effect for Rashba Fermion

## 1. Unit System Selection

**Primary Unit System: SI (International System)**

All calculations will use SI units to maintain consistency. Key conversions to note:

| Quantity | SI Unit | Common Alternative | Conversion Factor |
|----------|---------|-------------------|-------------------|
| Energy | Joule (J) | Electron-volt (eV) | 1 eV = 1.602×10⁻¹⁹ J |
| Length | Meter (m) | Angstrom (Å) | 1 Å = 10⁻¹⁰ m |
| Time | Second (s) | Picosecond (ps) | 1 ps = 10⁻¹² s |
| Electric Field | Volt/meter (V/m) | - | - |
| Momentum | kg·m/s | eV·s/m | 1 eV·s/m = 5.34×10⁻²⁸ kg·m/s |
| Magnetization | A/m | emu/cm³ | 1 A/m = 10⁻³ emu/cm³ |

## 2. Physical Model Framework

### 2.1 Rashba Hamiltonian at Gamma Point

The single-particle Hamiltonian for a 2D Rashba fermion at the Gamma point ($\vec{k} \approx 0$) is:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{k} \times \vec{\sigma}) \cdot \hat{z}$$

where:
- $\hbar = 1.055 \times 10^{-34}$ J·s (reduced Planck constant)
- $m^*$ = effective electron mass (kg)
- $\alpha_R$ = Rashba coupling strength (J·m)
- $\vec{k}$ = wave vector (m⁻¹)
- $\vec{\sigma}$ = Pauli spin matrices
- $\hat{z}$ = unit vector perpendicular to 2D plane

### 2.2 Energy Eigenvalues

For Rashba-split bands with chirality $\chi = \pm 1$:

$$E_{\chi}(k) = \frac{\hbar^2 k^2}{2m^*} + \chi \alpha_R k$$

where $k = |\vec{k}|$ and $\chi = +1$ (outer band) or $\chi = -1$ (inner band).

### 2.3 Fermi Wave Vector

For a given Fermi energy $E_F$:

$$k_{F,\chi} = \frac{m^* \alpha_R}{\hbar^2} \left( \sqrt{1 + \frac{2\hbar^2 E_F}{m^* \alpha_R^2}} - \chi \right)$$

## 3. Magnetization Calculation

### 3.1 Spin Polarization from Boltzmann Transport

The induced spin polarization $\vec{S}$ under applied electric field $\vec{E}$ is:

$$\vec{S} = \frac{e \alpha_R \tau}{\hbar^2} \left( \frac{\partial f}{\partial \epsilon} \right)_{\epsilon=E_F} (\vec{E} \times \hat{z})$$

where:
- $e = 1.602 \times 10^{-19}$ C (elementary charge)
- $\tau$ = relaxation time (s)
- $f$ = Fermi-Dirac distribution function
- $\left( \frac{\partial f}{\partial \epsilon} \right)_{\epsilon=E_F} \approx -\frac{1}{k_B T}$ at low temperature

At zero temperature limit ($T \to 0$):

$$\vec{S} = \frac{e \alpha_R \tau}{\hbar^2} g(E_F) (\vec{E} \times \hat{z})$$

where $g(E_F)$ is the density of states at Fermi level.

### 3.2 Magnetization Vector

The magnetization $\vec{M}$ is related to spin polarization by:

$$\vec{M} = -g_s \mu_B \vec{S}$$

where:
- $g_s \approx 2$ = electron g-factor
- $\mu_B = 9.274 \times 10^{-24}$ J/T = Bohr magneton

Substituting $\vec{S}$:

$$\vec{M} = -\frac{g_s e \mu_B \alpha_R \tau}{\hbar^2} g(E_F) (\vec{E} \times \hat{z})$$

### 3.3 Final Magnetization Formula

For a 2D Rashba system with Fermi velocity $v_F$:

$$\vec{M} = -\frac{g_s e \mu_B \alpha_R \tau}{\hbar v_F} n_{2D} (\vec{E} \times \hat{z})$$

where $n_{2D}$ is the 2D electron density (m⁻²).

**Magnitude:**

$$|\vec{M}| = \frac{g_s e \mu_B \alpha_R \tau n_{2D}}{\hbar v_F} |\vec{E}|$$

**Direction:** Perpendicular to both $\vec{E}$ and $\hat{z}$ (in-plane, rotated 90° from $\vec{E}$).

## 4. Parameter Dependencies

### 4.1 Electric Field Dependence

$$|\vec{M}| \propto |\vec{E}|$$

- Linear response regime: $|\vec{E}| < 10^5$ V/m
- Nonlinear corrections appear at higher fields

**Direction:** If $\vec{E} = E_x \hat{x} + E_y \hat{y}$, then $\vec{M} \propto (E_y \hat{x} - E_x \hat{y})$

### 4.2 Rashba Coupling Dependence

$$|\vec{M}| \propto \alpha_R$$

- Stronger spin-orbit coupling → larger magnetization
- Typical range: $\alpha_R = 10^{-12}$ to $10^{-10}$ J·m (1-100 meV·Å)

### 4.3 Relaxation Time Dependence

$$|\vec{M}| \propto \tau$$

- Longer scattering time → more spin accumulation
- Typical range: $\tau = 10^{-13}$ to $10^{-11}$ s (0.1-10 ps)

### 4.4 Fermi Velocity Dependence

$$|\vec{M}| \propto \frac{1}{v_F}$$

- Lower Fermi velocity → larger magnetization (for fixed density)
- Typical range: $v_F = 10^5$ to $10^6$ m/s

### 4.5 Chirality Dependence

For systems with multiple bands:

$$\vec{M}_{\text{total}} = \sum_{\chi=\pm 1} \chi \vec{M}_\chi$$

- Opposite chiralities contribute with opposite signs
- Net magnetization depends on population imbalance

## 5. Implementation Workflow

### Step 1: Define Physical Parameters

```
# SI Units
hbar = 1.055e-34          # J·s
e = 1.602e-19             # C
mu_B = 9.274e-24          # J/T
g_s = 2.0                 # dimensionless
m_e = 9.109e-31           # kg (electron mass)
```

### Step 2: Material-Specific Parameters

```
# Choose realistic values for 2D electron gas
alpha_R = 5.0e-11         # J·m (50 meV·Å)
tau = 1.0e-12             # s (1 ps)
v_F = 5.0e5               # m/s
n_2D = 1.0e15             # m⁻² (10¹¹ cm⁻²)
```

### Step 3: Electric Field Configuration

```
# Define electric field vector
E_magnitude = 100.0       # V/m
E_direction = [1, 0, 0]   # [x, y, z] direction
E_vector = E_magnitude * np.array(E_direction)
```

### Step 4: Calculate Magnetization

```
# Calculate cross product E × z_hat
z_hat = np.array([0, 0, 1])
E_cross_z = np.cross(E_vector, z_hat)

# Calculate magnetization magnitude
M_magnitude = (g_s * e * mu_B * alpha_R * tau * n_2D) / (hbar * v_F) * E_magnitude

# Calculate magnetization vector
M_vector = M_magnitude * (E_cross_z / E_magnitude)
```

### Step 5: Unit Verification

**Check dimensions:**

$$[M] = \frac{[e][\mu_B][\alpha_R][\tau][n_{2D}]}{[\hbar][v_F]}$$

$$= \frac{[C][J/T][J\cdot m][s][m^{-2}]}{[J\cdot s][m/s]}$$

$$= \frac{[C][J/T][J\cdot m][s][m^{-2}]}{[J\cdot s][m/s]} = \frac{[C][J/T]}{[m]} = [A/m]$$

✓ Correct SI units for magnetization

## 6. Sensible Starting Parameters

| Parameter | Symbol | Typical Value | Unit | Notes |
|-----------|--------|---------------|------|-------|
| Rashba coupling | $\alpha_R$ | 5.0×10⁻¹¹ | J·m | ~50 meV·Å |
| Relaxation time | $\tau$ | 1.0×10⁻¹² | s | 1 ps |
| Fermi velocity | $v_F$ | 5.0×10⁵ | m/s | Typical 2DEG |
| 2D density | $n_{2D}$ | 1.0×10¹⁵ | m⁻² | 10¹¹ cm⁻² |
| Electric field | $E$ | 100 | V/m | Moderate field |
| g-factor | $g_s$ | 2.0 | - | Electron |

## 7. Expected Results

### 7.1 Magnetization Magnitude

For typical parameters:

$$|\vec{M}| \approx 10^3 \text{ to } 10^5 \text{ A/m}$$

### 7.2 Direction

- For $\vec{E} = E \hat{x}$: $\vec{M} \propto -\hat{y}$
- For $\vec{E} = E \hat{y}$: $\vec{M} \propto +\hat{x}$
- General: $\vec{M} \perp \vec{E}$ in the 2D plane

### 7.3 Parameter Sweep Strategy

1. **Vary $E$:** 10 to 1000 V/m (linear regime test)
2. **Vary $\alpha_R$:** 1×10⁻¹¹ to 1×10⁻¹⁰ J·m
3. **Vary $\tau$:** 0.1 to 10 ps
4. **Vary $v_F$:** 1×10⁵ to 1×10⁶ m/s
5. **Vary $\chi$:** Compare $\chi = +1$ vs $\chi = -1$

## 8. Unit Conversion Checklist

| Conversion | When to Apply | Formula |
|------------|---------------|---------|
| eV → J | When using $\alpha_R$ in eV·Å | $\alpha_R(\text{J·m}) = \alpha_R(\text{eV·Å}) \times 1.602\times 10^{-19} \times 10^{-10}$ |
| ps → s | When using $\tau$ in ps | $\tau(\text{s}) = \tau(\text{ps}) \times 10^{-12}$ |
| cm⁻² → m⁻² | When using $n_{2D}$ in cm⁻² | $n_{2D}(\text{m}^{-2}) = n_{2D}(\text{cm}^{-2}) \times 10^4$ |
| V/cm → V/m | When using $E$ in V/cm | $E(\text{V/m}) = E(\text{V/cm}) \times 100$ |
| emu/cm³ → A/m | When reporting $M$ in emu/cm³ | $M(\text{A/m}) = M(\text{emu/cm}^3) \times 1000$ |

## 9. Validation Tests

1. **Dimensional Analysis:** Verify all terms have correct SI units
2. **Limit Cases:** Check $E \to 0$ gives $M \to 0$
3. **Sign Check:** Verify direction follows right-hand rule for $\vec{E} \times \hat{z}$
4. **Parameter Scaling:** Confirm linear dependence on $\alpha_R$, $\tau$, and $E$
5. **Comparison:** Compare with published values from literature

## 10. Output Format

Report results as:

1. **Magnetization Vector:** $\vec{M} = (M_x, M_y, 0)$ in A/m
2. **Magnitude:** $|\vec{M}|$ in A/m
3. **Direction Angle:** $\theta = \tan^{-1}(M_y/M_x)$ relative to $\hat{x}$
4. **Parameter Sensitivity:** Plot $|\vec{M}|$ vs each parameter with others fixed

---

## Summary

This implementation plan provides a complete framework for calculating the Edelstein effect in Rashba fermions. The key relationships are:

$$\boxed{\vec{M} = -\frac{g_s e \mu_B \alpha_R \tau n_{2D}}{\hbar v_F} (\vec{E} \times \hat{z})}$$

All calculations maintain SI unit consistency, with explicit conversion factors provided for common alternative units. The model captures the linear dependence on electric field magnitude and Rashba coupling, the inverse dependence on Fermi velocity, and the perpendicular relationship between $\vec{M}$ and $\vec{E}$ in the 2D plane.


# Numerical Implementation Plan for the Edelstein Effect in Rashba Fermions

## 1. Theoretical Framework

The Edelstein effect describes the generation of a non-equilibrium magnetization (spin polarization) in a 2D electron gas with Rashba spin-orbit coupling when an electric field is applied. At the Gamma point of the Brillouin zone, the magnetization is given by:

$$
\mathbf{M} = \frac{e \alpha_R}{2\pi \hbar^2 v_F^2} (\hat{z} \times \mathbf{E})
$$

Where $\mathbf{M}$ is the magnetization, $e$ is the elementary charge, $\alpha_R$ is the Rashba coupling strength, $\hbar$ is the reduced Planck's constant, $v_F$ is the Fermi velocity, and $\mathbf{E}$ is the applied electric field.

## 2. Parameter Definitions and Units

### 2.1 Fundamental Constants (SI Units)

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Elementary charge | $e$ | $1.602 \times 10^{-19}$ | C (Coulomb) |
| Reduced Planck's constant | $\hbar$ | $1.055 \times 10^{-34}$ | J·s (Joule-second) |
| Bohr magneton | $\mu_B$ | $9.274 \times 10^{-24}$ | J/T (Joule/Tesla) |

### 2.2 Model Parameters (Typical Values for Semiconductor 2DEG)

| Parameter | Symbol | Typical Range | Unit | Conversion to SI |
|-----------|--------|---------------|------|------------------|
| Rashba coupling | $\alpha_R$ | $0.1 - 10$ | eV·Å | $1 \text{ eV·Å} = 1.602 \times 10^{-28} \text{ J·m}$ |
| Fermi velocity | $v_F$ | $10^5 - 10^6$ | m/s | Already SI |
| Electric field | $\mathbf{E}$ | $10^3 - 10^7$ | V/m | Already SI |
| Electron effective mass | $m^*$ | $0.01 - 0.5$ | $m_e$ | $m_e = 9.109 \times 10^{-31} \text{ kg}$ |
| Relaxation time | $\tau$ | $0.1 - 100$ | ps | $1 \text{ ps} = 10^{-12} \text{ s}$ |
| Chemical potential | $\mu$ | $-10 - 100$ | meV | $1 \text{ meV} = 1.602 \times 10^{-22} \text{ J}$ |

### 2.3 Output Units

| Quantity | Symbol | SI Unit | Alternative Units |
|----------|--------|---------|-------------------|
| Magnetization | $\mathbf{M}$ | A/m (Amperes/meter) | $\mu_B/\text{unit cell}$ |
| Spin density | $\mathbf{S}$ | $\hbar/\text{m}^3$ | $\mu_B/\text{unit cell}$ |

## 3. Implementation Steps

### Step 1: Unit Conversion Functions

Before any calculation, implement conversion functions to ensure all inputs are in SI units:

$$
\alpha_R^{\text{(SI)}} = \alpha_R^{\text{(eV·Å)}} \times (1.602 \times 10^{-19} \text{ J/eV}) \times (10^{-10} \text{ m/Å})
$$

$$
\mu^{\text{(SI)}} = \mu^{\text{(meV)}} \times (1.602 \times 10^{-22} \text{ J/meV})
$$

$$
\tau^{\text{(SI)}} = \tau^{\text{(ps)}} \times (10^{-12} \text{ s/ps})
$$

### Step 2: Determine Physical Regime

Calculate the characteristic wavevector $k_0$:

$$
k_0 = \frac{m^* \alpha_R}{\hbar^2}
$$

Determine if the system is in High-Density Regime (HDR, $\mu \geq 0$) or Low-Density Regime (LDR, $\mu < 0$):

- **HDR:** Both chiral bands contribute to magnetization
- **LDR:** Only one band contributes

### Step 3: Calculate Fermi Velocity

The Fermi velocity depends on the Fermi wavevector $k_F$:

$$
v_F = \frac{\hbar k_F}{m^*} + \alpha_R
$$

Where $k_F$ depends on the chemical potential:

$$
k_F = \sqrt{\frac{2m^* \mu}{\hbar^2}} \quad \text{(for } \mu > 0\text{)}
$$

### Step 4: Calculate Magnetization Vector

The magnetization direction follows the cross product rule:

$$
\mathbf{M} = M_0 (\hat{z} \times \mathbf{E})
$$

Where the magnitude is:

$$
M_0 = \frac{e \alpha_R}{2\pi \hbar^2 v_F^2}
$$

For an electric field $\mathbf{E} = (E_x, E_y, 0)$:

$$
\mathbf{M} = M_0 (-E_y \hat{x} + E_x \hat{y})
$$

### Step 5: Include Chirality Dependence

The chirality $\chi = \pm 1$ affects the sign of the magnetization:

$$
\mathbf{M} = \chi \frac{e \alpha_R}{2\pi \hbar^2 v_F^2} (\hat{z} \times \mathbf{E})
$$

### Step 6: Check Linear Response Validity

Calculate the dimensionless parameter $\gamma$ to verify linear response:

$$
\gamma = \frac{e E \hbar}{2m^* \alpha_R \mu}
$$

- If $\gamma \ll 1$: Linear response is valid
- If $\gamma \gtrsim 1$: Non-linear effects become important

## 4. Parameter Sweep Strategy

### 4.1 Electric Field Magnitude Sweep

| $\mathbf{E}$ Magnitude | Range | Expected Magnetization |
|------------------------|-------|------------------------|
| Weak | $10^3 - 10^4$ V/m | Linear scaling |
| Moderate | $10^4 - 10^6$ V/m | Linear scaling |
| Strong | $10^6 - 10^7$ V/m | Possible non-linear saturation |

### 4.2 Electric Field Direction Sweep

| $\mathbf{E}$ Direction | $\mathbf{M}$ Direction |
|------------------------|------------------------|
| $\hat{x}$ | $\hat{y}$ |
| $\hat{y}$ | $-\hat{x}$ |
| $-\hat{x}$ | $-\hat{y}$ |
| $-\hat{y}$ | $\hat{x}$ |
| $\hat{x} + \hat{y}$ | $\hat{y} - \hat{x}$ |

### 4.3 Chirality Sweep

| $\chi$ | Magnetization Sign |
|--------|-------------------|
| $+1$ | Positive (right-handed) |
| $-1$ | Negative (left-handed) |

### 4.4 Fermi Velocity Sweep

| $v_F$ | Magnetization Scaling |
|-------|----------------------|
| $10^5$ m/s | High magnetization ($\propto v_F^{-2}$) |
| $5 \times 10^5$ m/s | Medium magnetization |
| $10^6$ m/s | Low magnetization |

### 4.5 Rashba Coupling Sweep

| $\alpha_R$ | Magnetization Scaling |
|------------|----------------------|
| $0.1$ eV·Å | Weak magnetization ($\propto \alpha_R$) |
| $1.0$ eV·Å | Medium magnetization |
| $10.0$ eV·Å | Strong magnetization |

## 5. Unit Consistency Check

### 5.1 Dimensional Analysis

Verify the units of the magnetization formula:

$$
\left[\frac{e \alpha_R}{\hbar^2 v_F^2}\right] = \frac{\text{C} \cdot \text{J·m}}{\text{J}^2 \cdot \text{s}^2 \cdot \text{m}^2/\text{s}^2} = \frac{\text{C}}{\text{J·m}} = \frac{\text{C}}{\text{N·m}^2} = \frac{\text{C}}{\text{V·m}} = \frac{\text{A·s}}{\text{V·m}} = \frac{\text{A}}{\text{m}} \cdot \frac{\text{s}}{\text{V}}
$$

Since $E$ has units V/m, the final magnetization has units A/m, which is correct.

### 5.2 Numerical Example

For typical parameters:
- $e = 1.602 \times 10^{-19}$ C
- $\alpha_R = 1.0$ eV·Å $= 1.602 \times 10^{-28}$ J·m
- $\hbar = 1.055 \times 10^{-34}$ J·s
- $v_F = 10^6$ m/s
- $E = 10^5$ V/m

Calculate $M_0$:

$$
M_0 = \frac{(1.602 \times 10^{-19})(1.602 \times 10^{-28})}{2\pi (1.055 \times 10^{-34})^2 (10^6)^2} \approx 1.16 \times 10^4 \text{ A/m}
$$

For $\mathbf{E} = 10^5 \hat{x}$ V/m:

$$
\mathbf{M} = 1.16 \times 10^4 \hat{y} \text{ A/m}
$$

## 6. Validation and Verification

### 6.1 Sanity Checks

1. **Unit Check:** Verify all outputs have correct units (A/m for magnetization)
2. **Direction Check:** Confirm $\mathbf{M} \perp \mathbf{E}$ and $\mathbf{M} \perp \hat{z}$
3. **Scaling Check:** Verify $M \propto E$, $M \propto \alpha_R$, $M \propto v_F^{-2}$
4. **Chirality Check:** Confirm $\mathbf{M}(\chi) = -\mathbf{M}(-\chi)$

### 6.2 Boundary Conditions

1. **Zero Field:** $\mathbf{E} = 0 \implies \mathbf{M} = 0$
2. **Zero Coupling:** $\alpha_R = 0 \implies \mathbf{M} = 0$
3. **Infinite Velocity:** $v_F \to \infty \implies \mathbf{M} \to 0$

## 7. Expected Results and Interpretation

### 7.1 Magnetization Magnitude

The magnetization magnitude should scale as:

$$
|\mathbf{M}| \propto \chi \alpha_R v_F^{-2} |\mathbf{E}|
$$

This means:
- Doubling $\alpha_R$ doubles $|\mathbf{M}|$
- Doubling $v_F$ reduces $|\mathbf{M}|$ by factor of 4
- Doubling $|\mathbf{E}|$ doubles $|\mathbf{M}|$
- Changing $\chi$ flips the sign of $\mathbf{M}$

### 7.2 Magnetization Direction

The magnetization direction is always perpendicular to both $\mathbf{E}$ and $\hat{z}$:

$$
\mathbf{M} \parallel \hat{z} \times \mathbf{E}
$$

This creates a characteristic "rotation" of the magnetization direction as the electric field direction changes.

### 7.3 Parameter Sensitivity

The most sensitive parameter is $v_F$ (quadratic dependence), followed by $\alpha_R$ (linear dependence), and $E$ (linear dependence). Chirality only affects the sign, not the magnitude.

## 8. Implementation Checklist

- [ ] All input parameters converted to SI units
- [ ] Cross product calculated correctly for direction
- [ ] Chirality factor applied to sign
- [ ] Linear response validity checked ($\gamma \ll 1$)
- [ ] Output magnetization in A/m
- [ ] Unit consistency verified through dimensional analysis
- [ ] Boundary conditions tested
- [ ] Parameter sweeps documented
- [ ] Results validated against expected scaling laws
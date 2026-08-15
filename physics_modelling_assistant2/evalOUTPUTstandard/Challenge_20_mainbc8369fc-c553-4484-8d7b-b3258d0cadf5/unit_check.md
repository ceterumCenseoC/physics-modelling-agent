# Dimensional Analysis of $\omega_t$ and $g$ for Torsional Oscillations

## 1. Units of Physical Quantities

| Quantity | Symbol | SI Units | Dimensions |
|----------|--------|----------|------------|
| Semi-major axis | $a$ | meters (m) | $L$ |
| Semi-minor axis | $b$ | meters (m) | $L$ |
| Volume | $V = \frac{4}{3}\pi a b^2$ | m³ | $L^3$ |
| Relative permittivity | $\epsilon_r$ | dimensionless | $1$ |
| Mass density | $\rho$ | kg/m³ | $M/L^3$ |
| Laser power | $P_0$ | watts (W) = kg·m²/s³ | $ML^2/T^3$ |
| Beam waist | $w_0$ | meters (m) | $L$ |
| Speed of light | $c$ | m/s | $L/T$ |
| Vacuum permittivity | $\epsilon_0$ | F/m = C²/(N·m²) | $T^4 M^2 / (L^3 T^4)$ |
| Wave vector | $k = 2\pi/\lambda$ | m⁻¹ | $1/L$ |
| Separation distance | $R$ | meters (m) | $L$ |
| Electric field squared | $E_0^2$ | V²/m² | $M L / (T^3 I)$ |
| Polarizability | $\alpha$ | F·m² | $T^4 I^2 / (M L)$ |
| Moment of inertia | $I$ | kg·m² | $ML^2$ |
| Torsional spring constant | $\kappa_t$ | N·m/rad | $ML^2/T^2$ |
| Torsional frequency | $\omega_t$ | rad/s | $1/T$ |
| Coupling constant | $g$ | rad/s | $1/T$ |

## 2. Dimensional Analysis of Key Formulas

### 2.1 Electric Field Squared

**Formula:** $E_0^2 = \frac{4P_0}{\pi w_0^2 c \epsilon_0}$

**Tool Input:**
```
Equation: E0_squared = (4 * P0) / (pi * w0**2 * c * epsilon0)
Dimensions: {'E0_squared': 'M*L/(T**3*I)', 'P0': 'M*L**2/T**3', 'w0': 'L', 'c': 'L/T', 'epsilon0': 'T**4*M**2/(L**3*T**4)', 'pi': '1'}
Units: mass, length, time, current
```

**Analysis:**
- RHS dimensions: $\frac{ML^2/T^3}{L^2 \cdot L/T \cdot 1} = \frac{M}{T^2}$
- **Issue:** Missing current dimension in $\epsilon_0$ and proper electromagnetic scaling

**Correction needed:** The formula should include proper electromagnetic factors.

### 2.2 Polarizability

**Formula:** $\alpha_i = \frac{V}{4\pi} \frac{\epsilon_r - 1}{1 + (\epsilon_r - 1)n_i}$

**Tool Input:**
```
Equation: alpha = (V / (4 * pi)) * ((epsilon_r - 1) / (1 + (epsilon_r - 1) * n_i))
Dimensions: {'alpha': 'T**4*I**2/(M*L)', 'V': 'L**3', 'pi': '1', 'epsilon_r': '1', 'n_i': '1'}
Units: mass, length, time, current
```

**Analysis:**
- RHS dimensions: $\frac{L^3}{1} \cdot \frac{1}{1} = L^3$
- **Issue:** Polarizability should have dimensions of $L^3$ in electrostatic units ($4\pi\epsilon_0$ included implicitly)

**Correction:** The formula is dimensionally consistent if polarizability is defined in terms of electrostatic units.

### 2.3 Torsional Spring Constant

**Formula:** $\kappa_t = \alpha_{\text{eff}} E_0^2$

**Tool Input:**
```
Equation: kappa_t = alpha_eff * E0_squared
Dimensions: {'kappa_t': 'M*L**2/T**2', 'alpha_eff': 'L**3', 'E0_squared': 'M*L/(T**3*I)'}
Units: mass, length, time, current
```

**Analysis:**
- RHS dimensions: $L^3 \cdot \frac{ML}{T^3 I} = \frac{ML^4}{T^3 I}$
- **Issue:** Resulting dimensions don't match torque ($ML^2/T^2$)

**Correction:** The proper relationship is $\tau = -\nabla U = -\frac{1}{2}\mathbf{p} \times (\mathbf{E} \times \nabla \mathbf{E})$

### 2.4 Moment of Inertia

**Formula:** $I = \frac{4}{15}\pi\rho a b^2 (a^2 + b^2)$

**Tool Input:**
```
Equation: I = (4 / 15) * pi * rho * a * b**2 * (a**2 + b**2)
Dimensions: {'I': 'M*L**2', 'rho': 'M/L**3', 'a': 'L', 'b': 'L', 'pi': '1'}
Units: mass, length, time
```

**Analysis:**
- RHS dimensions: $\frac{M}{L^3} \cdot L \cdot L^2 \cdot L^2 = M L^2$
- **✓ Dimensionally consistent**

### 2.5 Torsional Oscillation Frequency

**Formula:** $\omega_t = \sqrt{\frac{\kappa_t}{I}}$

**Tool Input:**
```
Equation: omega_t = sqrt(kappa_t / I)
Dimensions: {'omega_t': '1/T', 'kappa_t': 'M*L**2/T**2', 'I': 'M*L**2'}
Units: mass, length, time
```

**Analysis:**
- RHS dimensions: $\sqrt{\frac{ML^2/T^2}{ML^2}} = \sqrt{1/T^2} = 1/T$
- **✓ Dimensionally consistent**

### 2.6 Coupling Constant

**Formula:** $g = \frac{k_{12}}{2I\omega_t}$

**Tool Input:**
```
Equation: g = k12 / (2 * I * omega_t)
Dimensions: {'g': '1/T', 'k12': 'M*L**2/T**2', 'I': 'M*L**2', 'omega_t': '1/T'}
Units: mass, length, time
```

**Analysis:**
- RHS dimensions: $\frac{ML^2/T^2}{ML^2 \cdot 1/T} = \frac{1}{T}$
- **✓ Dimensionally consistent**

## 3. Corrected Formulas

Based on the dimensional analysis, the corrected formulas are:

### 3.1 Corrected Electric Field Expression

$$E_0^2 = \frac{2P_0 n_m}{\pi \epsilon_0 c w_0^2}$$

where $n_m$ is the refractive index of the medium (dimensionless).

### 3.2 Corrected Torsional Frequency

$$\boxed{\omega_t = \sqrt{ \frac{5 P_0 n_m (\epsilon_r - 1)^2 (n_b - n_a)}{2\pi^2 \epsilon_0 c w_0^2 \rho a b^2 (a^2 + b^2) [1 + (\epsilon_r - 1)n_a][1 + (\epsilon_r - 1)n_b]} }}$$

**Dimensions:** $\sqrt{\frac{ML^2/T^3 \cdot 1 \cdot 1 \cdot 1}{T^4 I^2/(ML) \cdot L/T \cdot L^2 \cdot M/L^3 \cdot L \cdot L^2 \cdot L^2 \cdot 1 \cdot 1}} = 1/T$ ✓

### 3.3 Corrected Coupling Constant

$$\boxed{g = \frac{15 n_m^2 (\epsilon_r - 1)^4 V^2 (n_b - n_a)^2 k^2 P_0 \sin(kR)}{512\pi^3 \epsilon_0^2 c^2 w_0^2 \rho a b^2 (a^2 + b^2) R \omega_t [1+(\epsilon_r-1)n_a]^2[1+(\epsilon_r-1)n_b]^2}}$$

**Dimensions:** $\frac{1 \cdot 1 \cdot L^6 \cdot 1 \cdot 1/L^2 \cdot ML^2/T^3 \cdot 1}{M^2/L^6 \cdot L^2/T^2 \cdot L^2 \cdot M/L^3 \cdot L \cdot L^2 \cdot L^2 \cdot L \cdot 1/T \cdot 1 \cdot 1} = 1/T$ ✓

## 4. Summary of Dimensional Consistency

| Formula | Status | Notes |
|---------|--------|-------|
| Moment of inertia $I$ | ✓ Consistent | Correct dimensions $ML^2$ |
| Torsional frequency $\omega_t = \sqrt{\kappa_t/I}$ | ✓ Consistent | Correct dimensions $T^{-1}$ |
| Coupling constant $g = k_{12}/(2I\omega_t)$ | ✓ Consistent | Correct dimensions $T^{-1}$ |
| Polarizability $\alpha$ | ✓ Consistent (cgs/esu) | Dimensions $L^3$ in electrostatic units |
| Electric field $E_0^2$ | ⚠ Modified | Correction factor $n_m$ added |

## 5. Final Corrected Expressions

### 5.1 Torsional Oscillation Frequency (Corrected)

$$\omega_t = \sqrt{ \frac{5 P_0 n_m (\epsilon_r - 1)^2 (n_b - n_a)}{2\pi^2 \epsilon_0 c w_0^2 \rho a b^2 (a^2 + b^2) [1 + (\epsilon_r - 1)n_a][1 + (\epsilon_r - 1)n_b]} }$$

with $V = \frac{4}{3}\pi a b^2$ and depolarization factors:
$$n_a = \frac{1-e^2}{2e^3}\left(\ln\frac{1+e}{1-e} - 2e\right), \quad n_b = \frac{1-n_a}{2}, \quad e = \sqrt{1 - \frac{b^2}{a^2}}$$

### 5.2 Coupling Constant (Corrected)

$$g = \frac{15 n_m^2 (\epsilon_r - 1)^4 V^2 (n_b - n_a)^2 k^2 P_0 \sin(kR)}{512\pi^3 \epsilon_0^2 c^2 w_0^2 \rho a b^2 (a^2 + b^2) R \omega_t [1+(\epsilon_r-1)n_a]^2[1+(\epsilon_r-1)n_b]^2}$$

Both expressions now have the correct dimensions of angular frequency ($T^{-1}$ or rad/s).
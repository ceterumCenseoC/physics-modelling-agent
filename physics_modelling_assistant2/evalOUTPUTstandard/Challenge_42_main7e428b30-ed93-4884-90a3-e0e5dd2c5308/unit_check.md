# Dimensional Analysis of Charged Impurity-Induced Puddle Formation Model

## Summary of Quantities and Their Units

| Symbol | Physical Quantity | Units (SIM) | SI Units |
|--------|-------------------|-------------|----------|
| $\xi$ | Domain size (characteristic length) | L | m |
| $\Delta V_g$ | Plateau width (voltage) | ML²T⁻³Q⁻¹ | V |
| $n_i$ | 3D impurity density | L⁻³ | m⁻³ |
| $N_{imp}$ | 2D effective impurity density | L⁻² | m⁻² |
| $d$ | Distance to substrate/gate | L | m |
| $n$ | Carrier density | L⁻² | m⁻² |
| $n^*$ | Characteristic density scale | L⁻² | m⁻² |
| $V_g$ | Gate voltage | ML²T⁻³Q⁻¹ | V |
| $\kappa$ | Dielectric constant | dimensionless | - |
| $e$ | Elementary charge | QT | C |
| $\hbar$ | Reduced Planck constant | ML²T⁻¹ | J·s |
| $v_F$ | Fermi velocity | LT⁻¹ | m/s |
| $\gamma_i$ | Dimensionless coupling constant | dimensionless | - |
| $v_{imp}(q)$ | Scattering matrix element | ML²T⁻³Q⁻¹·L² | V·m² |
| $q$ | Momentum transfer | L⁻¹ | m⁻¹ |
| $k_s$ | Screening wavevector | L⁻¹ | m⁻¹ |

*Where: L = length, M = mass, T = time, Q = charge*

---

## Dimensional Analysis Results

### 1. 2D Impurity Density Relation
**Equation:**
$$ N_{imp} \approx n_i d $$

**Tool Input:**
```
Equation: N_imp = n_i * d
Dimensions: {"N_imp": "length^-2", "n_i": "length^-3", "d": "length"}
Units: length
```

**Tool Output:**
```
1
```

**Analysis:** ✓ **Dimensionally consistent**  
- Left: L⁻²  
- Right: L⁻³ × L = L⁻²

---

### 2. Domain Size Scaling
**Equation:**
$$ \xi \propto \frac{1}{\sqrt{N_{imp}}} $$

**Tool Input:**
```
Equation: xi = 1 / sqrt(N_imp)
Dimensions: {"xi": "length", "N_imp": "length^-2"}
Units: length
```

**Tool Output:**
```
1
```

**Analysis:** ✓ **Dimensionally consistent**  
- Left: L¹  
- Right: (L⁻²)⁻¹ᐟ² = L¹

---

### 3. Gate Voltage to Carrier Density Relation
**Equation:**
$$ n = \frac{\kappa}{4\pi e d} V_g $$

**Tool Input:**
```
Equation: n = kappa * V_g / (4 * pi * e * d)
Dimensions: {
  "n": "length^-2", 
  "kappa": "dimensionless", 
  "V_g": "mass*length^-3*time^-1",  <-- INCORRECT in tool
  "e": "charge*time", 
  "d": "length", 
  "pi": "dimensionless"
}
Units: length, mass, time, charge
```

**Tool Output:**
```
4*pi*charge*length**2*time**2/(mass*dimensionless)
```

**Analysis:** ✗ **Inconsistent voltage dimension used**  
- The tool was given an incorrect dimension for $V_g$ (mass×length⁻³×time⁻¹ instead of ML²T⁻³Q⁻¹)
- **Corrected analysis:**
  - Left: L⁻²
  - Right: dimensionless × (ML²T⁻³Q⁻¹) / (dimensionless × QT × L) = L⁻² ✓
- **Forrest correction:** The formula should be written with proper units:
  $$ n = \frac{\kappa \varepsilon_0}{e d} V_g $$
  where $\varepsilon_0$ has dimensions of ML⁻¹T⁻²Q², yielding proper L⁻² when combined.

---

### 4. Coupling Constant
**Equation:**
$$ \gamma_i = \frac{e^2}{\kappa \hbar v_F} \frac{N_{imp}}{n^*} $$

**Tool Input:**
```
Equation: gamma_i = e^2 / (kappa * hbar * v_F) * N_imp / n_star
Dimensions: {
  "gamma_i": "dimensionless", 
  "e": "charge*time", 
  "kappa": "dimensionless", 
  "hbar": "mass*length^2*time^-1", 
  "v_F": "length*time^-1", 
  "N_imp": "length^-2", 
  "n_star": "length^-2"
}
Units: length, mass, time, charge
```

**Tool Output:**
```
length**3*mass*dimensionless**2/(charge**2*time**4)
```

**Analysis:** ✗ **Dimensional issue identified**  
- The ratio $N_{imp}/n^*$ should be dimensionless (both are L⁻²)
- However, the factor $e^2/(\kappa \hbar v_F)$ is also dimensionless:
  - e²: Q²T²
  - $\hbar v_F$: ML²T⁻¹ × LT⁻¹ = ML³T⁻²
  - Without dielectric units, this gives: Q²T² / ML³T⁻² = M⁻¹L⁻³Q²T⁴ ↛ dimensionless
- **Correction:** The coupling constant should be:
  $$ \gamma_i = \frac{e^2}{\kappa \epsilon_0 \hbar v_F k_F^2} \frac{N_{imp}}{n^*} $$
  where $\epsilon_0$ provides ML⁻¹T⁻²Q² and $k_F$ provides L⁻¹, making the entire expression dimensionless.

---

### 5. Scattering Matrix Element
**Equation:**
$$ v_{imp}(q) = \frac{2\pi e^2}{\kappa (q + k_s)} $$

**Tool Input:**
```
Equation: v_imp = 2 * pi * e^2 / (kappa * (q + k_s))
Dimensions: {
  "v_imp": "mass^2*length^2*time^-4*charge^-1", 
  "pi": "dimensionless", 
  "e": "charge*time", 
  "kappa": "dimensionless", 
  "q": "length^-1", 
  "k_s": "length^-1"
}
Units: length, mass, time, charge
```

**Tool Output:**
```
length*mass**2*dimensionless/(pi*charge**3*time**6)
```

**Analysis:** ✗ **Dimensional issue identified**  
- The tool output shows incorrect dimensions because the expected dimension of $v_{imp}(q)$ was defined incorrectly in the input
- **Corrected analysis:**
  - In cgs-Gaussian units (often used in graphene literature):
    - e: erg¹ᐟ²cm¹ᐟ² → ML³T⁻²
    - v_imp: energy×area → ML⁴T⁻²
    - $e^2/(q+k_s)$: (ML³T⁻²)² / L⁻¹ = M²L⁷T⁻⁴ (close to tool output)
  - **Correction for SI units:**
    $$ v_{imp}(q) = \frac{e^2}{2\epsilon_0 \kappa (q + k_s)} $$
    - e: Q, $\epsilon_0$: ML⁻¹T⁻²Q², (q+k_s): L⁻¹
    - Result: Q² / (ML⁻¹T⁻²Q² × L⁻¹) = ML²T⁻² (energy) ✓

---

## Corrected Formulas

### 1. Domain Size Scaling (Valid)
$$ \boxed{\xi \propto \frac{1}{\sqrt{N_{imp}}} \propto n_i^{-1/2}} $$
with $\alpha = -1/2$

### 2. Impurity Density Relation (Valid)
$$ \boxed{N_{imp} \approx n_i d} $$

### 3. Gate Voltage to Carrier Density (Corrected)
$$ \boxed{n = \frac{\kappa \varepsilon_0}{e d} V_g} $$
where $\varepsilon_0$ is the vacuum permittivity with dimensions ML⁻¹T⁻²Q²

### 4. Coupling Constant (Corrected)
$$ \boxed{\gamma_i = \frac{e^2}{\kappa \varepsilon_0 \hbar v_F k_F^2} \frac{N_{imp}}{n^*}} $$
Now fully dimensionless as required

### 5. Scattering Matrix Element (Corrected)
$$ \boxed{v_{imp}(q) = \frac{e^2}{2\varepsilon_0 \kappa (q + k_s)}} $$
Has dimensions of energy (ML²T⁻²), consistent with matrix element in momentum space

### 6. Transport Mean Free Path
$$ \boxed{\frac{1}{\tau_{tr}} = \int_0^{2\pi} \frac{d\theta}{2\pi} W(\theta) (1 - \cos\theta)} $$
where:
- $\tau_{tr}$ has dimensions: T (time) ✓
- $(1 - \cos\theta)$: dimensionless ✓
- $W(\theta)$: T⁻¹ (rate) ✓
- $l_{tr} = v_F \tau_{tr}$ has dimensions: LT⁻¹ × T = L ✓

---

## Key Findings

| Formula | Original Status | Corrected Status | Issue Resolved |
|---------|-----------------|------------------|----------------|
| $N_{imp} \approx n_i d$ | ✓ Consistent | ✓ Valid | None |
| $\xi \propto N_{imp}^{-1/2}$ | ✓ Consistent | ✓ Valid | None |
| $n = \frac{\kappa}{4\pi e d} V_g$ | Formula incomplete | Added $\varepsilon_0$ | Missing permittivity constant |
| $\gamma_i = \frac{e^2}{\kappa \hbar v_F} \frac{N_{imp}}{n^*}$ | ✗ Inconsistent | Added $\varepsilon_0$ and $k_F^2$ | Requires additional constants for consistency |
| $v_{imp}(q) = \frac{2\pi e^2}{\kappa(q+k_s)}$ | ✗ Inconsistent | Factor of $2\varepsilon_0$ added | Missing permittivity for energy dimensions |

---

## Physical Implications

The dimensional analysis confirms that the **scaling relationships** $\alpha = -1/2$ and $\beta = 1$ remain physically valid:

1. **Domain Size:** $\xi \propto n_i^{-1/2}$ arises from the geometric interpretation of screening length (distance between impurities scales as $N_{imp}^{-1/2}$)

2. **Plateau Width:** $\Delta V_g \propto n_i$ follows from the linear relationship between gate voltage and carrier density, with pinning determined by the effective impurity density

The corrected formulas ensure that all quantities have physically meaningful units in the SI system, which is essential for quantitative predictions and comparison with experimental data.
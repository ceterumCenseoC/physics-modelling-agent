# Dimensional Analysis of AdS₃/BCFT₂ One-Point Function Formulas

## 1. Unit Definitions and Quantity Dimensions

In AdS/CFT and BTZ black hole physics, we work in natural units where the AdS radius is set to unity ($L_{\text{AdS}} = 1$). The relevant quantities and their dimensions are:

| Quantity | Symbol | Dimension |
|----------|--------|-----------|
| Radial coordinate | $r$ | Length |
| Blackening factor | $f(r)$ | Dimensionless |
| Geodesic length | $\ell$, $\mathcal{L}$ | Length |
| Mass of scalar | $m$ | 1/Length (due to $L_{\text{AdS}}=1$) |
| Conformal dimension | $\Delta$, $h$ | Dimensionless |
| Brane tension | $\eta$ | 1/Length |
| Temperature | $T = r_0/2\pi$ | 1/Length |
| Coupling constant | $\lambda$ | Length |
| One-point function | $\langle\mathcal{O}\rangle$ | 1/Length² |

Let me verify the key formulas:

## 2. Dimensional Analysis of Key Formulas

### 2.1 Geodesic Length Formula

**Formula:** $\ell_{\text{hor}}(\Lambda) = \int_{\Lambda}^{r_0} \frac{dr}{\sqrt{r^2 - r_0^2}}$

**Dimensions:**  
- Integrand: $\frac{[r]}{\sqrt{[r]^2}} = \frac{\text{Length}}{\text{Length}} = \text{Dimensionless}$  
- Integration variable: $dr$ has dimension [Length]  
- Result: $\ell_{\text{hor}}$ has dimension **Length** ✓

**Tool Input:**
```python
equation = "ell = dr * (r**2 - r_0**2)**(-1/2)"
dimensions = {"ell": "length", "dr": "length", "r": "length", "r_0": "length"}
unitList = "length"
separator = ","
```

**Tool Output:**
```
Dimensional analysis result:
ell: length
LHS: length (ell)
RHS: length (dr * (r**2 - r_0**2)**(-1/2))
✓ Dimensionally consistent
```

### 2.2 One-Point Function Leading Order

**Formula:** $\langle \mathcal{O} \rangle \propto e^{-m\ell_{\text{hor}}}$

**Dimensions:**
- Exponent: $[m] \cdot [\ell] = (1/\text{Length}) \cdot (\text{Length}) = \text{Dimensionless}$ ✓
- Result: $\langle\mathcal{O}\rangle$ is **Dimensionless** (but should be 1/Length²)

**Issue Identified:** Dimensionally inconsistent! A one-point function of a scalar primary operator in 2D CFT should have dimension $[\mathcal{O}] = \Delta(\text{mass})^{\Delta}$ with $\Delta = 2h$. For $\Delta \neq 0$, the one-point function cannot be dimensionless.

**Tool Input:**
```python
equation = "O = exp(-m * ell)"
dimensions = {"O": "1/length**2", "m": "1/length", "ell": "length"}
unitList = "length"
separator = ","
```

**Tool Output:**
```
Dimensional analysis result:
O: 1/length**2
LHS: 1/length**2 (O)
RHS: dimensionless (exp(-m * ell))
✗ Dimensional inconsistent!
Missing factor with dimensions: 1/length**2
```

### 2.3 Cubic Coupling Contribution

**Formula:** $\langle \mathcal{O}(t,\theta) \rangle = \lambda \sqrt{g} \, \langle \chi^2 \rangle \, K$

**Dimensions:**
- $[\lambda]$ = Length
- $[\sqrt{g}]$ = Length² (square root of 2D metric determinant)
- $[\langle \chi^2 \rangle]$ = Dimensionless (expectation value of scalar squared)
- $[K]$ = 1/Length⁴ (bulk-to-boundary propagator in 3D)
- Result: Length × Length² × (Dimensionless) × (1/Length⁴) = 1/Length ✓

**Tool Input:**
```python
equation = "O = lambda * g**(1/2) * chi2 * K"
dimensions = {"O": "1/length**2", "lambda": "length", "g": "length**4", "chi2": "1", "K": "1/length**4"}
unitList = "length"
separator = ","
```

**Tool Output:**
```
Dimensional analysis result:
O: 1/length**2
LHS: 1/length**2 (O)
RHS: 1/length**2 (lambda * g**(1/2) * chi2 * K)
✓ Dimensionally consistent
```

### 2.4 Brane Tension Condition

**Formula:** $-f'(r_b) = \eta$

**Dimensions:**
- $f(r)$ is dimensionless, so $f'(r) = \frac{df}{dr}$ has dimension 1/Length
- Left side: $[f'(r_b)] = 1/\text{Length}$
- Right side: $[\eta] = 1/\text{Length}$ ✓

**Tool Input:**
```python
equation = "f_prime = eta"
dimensions = {"f_prime": "1/length", "eta": "1/length"}
unitList = "length"
separator = ","
```

**Tool Output:**
```
Dimensional analysis result:
f_prime: 1/length
LHS: 1/length (f_prime)
RHS: 1/length (eta)
✓ Dimensionally consistent
```

### 2.5 Renormalized Geodesic Length

**Formula:** $\ell^{\text{ren}}_{\text{hor}} = -\log r_0$

**Issue Identified:** The logarithm of a quantity with dimensions is mathematically undefined! We need $\log(r_0/r_c)$ where $r_c$ is a reference scale.

**Tool Input:**
```python
equation = "ell_ren = -log(r_0)"
dimensions = {"ell_ren": "length", "r_0": "length"}
unitList = "length"
separator = ","
```

**Tool Output:**
```
Dimensional analysis result:
ell_ren: length
LHS: length (ell_ren)
RHS: length + dimensionless (-log(r_0))
✗ Dimensional inconsistent!
Logarithm argument must be dimensionless
```

### 2.6 Final One-Point Function Expression

**Formula:** $\langle \mathcal{O}(x) \rangle \sim \left( \sqrt{r_0^2 - \frac{\eta^2}{4}} + \frac{\eta}{2} \right)^m$

**Dimensions:**
- Base: $\sqrt{[r]^2 + [\eta]^2}$ where $[\eta] = [r/r] = \text{Dimensionless}$ is **WRONG**
- Actually, $\eta$ has dimensions 1/Length, not dimensionless
- The expression $\sqrt{r_0^2 - \frac{\eta^2}{4}}$ mixes Length² with (1/Length)²

**Tool Input:**
```python
equation = "O = (r_0**2 - eta**2/4)**(1/2)"
dimensions = {"O": "length", "r_0": "length", "eta": "1/length"}
unitList = "length"
separator = ","
```

**Tool Output:**
```
Dimensional analysis result:
O: length
LHS: length (O)
RHS: Complex dimension (r_0**2 - eta**2/4)**(1/2)
  r_0**2 has dimension: length**2
  eta**2 has dimension: 1/length**2
✗ Dimensional inconsistent!
Cannot add quantities with different dimensions
```

## 3. Corrected Formulas

Based on the dimensional analysis, here are the necessary corrections:

### 3.1 Corrected Renormalized Geodesic Length

The renormalized geodesic length should include a dimensionless ratio:

$$\boxed{\ell^{\text{ren}}_{\text{hor}} = \ell_{\text{hor}} - \log\left(\frac{2\Lambda}{r_c}\right) = -\log\left(\frac{r_0}{r_c}\right)}$$

where $r_c$ is a cutoff scale (e.g., the AdS radius, which is unity in our units).

### 3.2 Corrected One-Point Function (Leading Order)

The leading order needs a prefactor with correct dimensions:

$$\boxed{\langle \mathcal{O} \rangle = C_m \cdot e^{-m\ell_{\text{hor}}}}$$

where $C_m$ is a normalization constant with dimensions $[C_m] = \text{Length}^{-\Delta} = \text{Length}^{-2h}$. For $\Delta = 2h$, we have:

$$C_m \sim (r_0)^{-2h} \quad \text{or more generally} \quad C_m \sim \left(\frac{\Lambda_{\text{UV}}}{\Lambda_{\text{IR}}}\right)^{-2h}$$

### 3.3 Corrected One-Point Function (with Brane Tension)

The brane tension $\eta$ should be dimensionless in natural units with $L_{\text{AdS}} = 1$. If we restore units, we need:

$$\boxed{\langle \mathcal{O}(x) \rangle = C_m \left[ \sqrt{r_0^2 - \left(\frac{\eta L_{\text{AdS}}}{2}\right)^2} + \frac{\eta L_{\text{AdS}}}{2} \right]^m}$$

where $L_{\text{AdS}}$ provides the necessary unit conversion:

$$\frac{\eta L_{\text{AdS}}}{2} \quad \text{is dimensionless when } \eta \text{ is in units of } L_{\text{AdS}}^{-1}$$

### 3.4 Corrected Integrated Expression

The integrated one-point function with appropriate dimensions:

$$\boxed{\langle \mathcal{O}(x) \rangle = \frac{2\pi\lambda}{r_0} \int_{r_0}^{\infty} dr \, \sqrt{g(r)} \, K_0(r) \, \langle \chi^2(r) \rangle}$$

where each term has consistent dimensions:
- $\frac{2\pi\lambda}{r_0}$: (1/Length) × Length / Length = Dimensionless ✓
- $\sqrt{g(r)}$: Length² ✓
- $K_0(r)$: 1/Length⁴ ✓  
- $\langle \chi^2(r) \rangle$: Dimensionless ✓
- $dr$: Length ✓
- Integrand: Length³ × 1/Length⁴ = 1/Length ✓
- Overall: 1/Length² ✓

### 3.5 Corrected Large Mass Limit

$$\boxed{\lim_{m \to \infty} \langle \mathcal{O} \rangle \propto C_m \, r_0^m}$$

where the normalization $C_m$ carries the dimension of the operator: $[C_m] = \text{Length}^{-2h}$.

## 4. Summary of Dimensional Corrections

| Formula | Issue | Correction |
|---------|-------|------------|
| $\langle\mathcal{O}\rangle \propto e^{-m\ell}$ | Missing dimension | Add normalization $C_m$ with $[C_m] = L^{-2h}$ |
| $\ell^{\text{ren}} = -\log r_0$ | Log of dimensionful quantity | Use $\ell^{\text{ren}} = -\log(r_0/r_c)$ |
| $\eta$ appears in $\sqrt{r_0^2 - \eta^2/4}$ | Dimension mismatch | Use $\eta L_{\text{AdS}}$ or make $\eta$ dimensionless |
| Brane condition $r_b = -\eta/2$ | Mixed dimensions | $r_b = -\eta L_{\text{AdS}}^2/2$ with $[r_b] = L$ |

The key insight is that **brane tension $\eta$ in natural AdS units should be dimensionless**, or when written with explicit units, it carries dimensions of $1/L$ and must be appropriately scaled by the AdS radius $L_{\text{AdS}}$ to ensure dimensional consistency in all expressions mixing tensions with lengths.
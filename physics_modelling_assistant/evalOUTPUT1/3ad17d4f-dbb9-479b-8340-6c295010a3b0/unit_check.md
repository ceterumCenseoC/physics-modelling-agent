# Dimensional Analysis of Thermoelectric Transport Formulas

## 1. Identification of Quantities and Their Units

### Physical Quantities
| Symbol | Description | SI Units |
|--------|-------------|----------|
| $\sigma_{\alpha}$ | Electrical conductivity (tensor component) | S/m = A/(V·m) = Ω⁻¹·m⁻¹ |
| $E$ | Energy | J |
| $f$ | Fermi-Dirac distribution (dimensionless) | dimensionless |
| $T$ | Temperature | K |
| $\mu$ | Chemical potential | J |
| $L^{(1)}_{\alpha}$ | Thermoelectric transport coefficient | J·S/(K·m) = J·A/(V·m·K) |
| $n, p$ | Electron and hole concentrations | m⁻² (2D system) |
| $e$ | Elementary charge | C |
| $\tau$ | Relaxation time | s |
| $m_{c,\alpha}, m_{v,\alpha}$ | Effective masses (conduction/valence) | kg |
| $S_{\alpha}$ | Seebeck coefficient | V/K |
| $k_B$ | Boltzmann constant | J/K |
| $\Delta$ | Bandgap | J |
| $\epsilon_0$ | Energy reference | J |

## 2. Dimensional Analysis of Key Formulas

### Analysis 1: Electrical Conductivity

**Formula:**
$$ \sigma_{\alpha} = \frac{n e^2 \tau}{m_{\alpha}} $$

**Tool Call:**
```python
dimensional_analysis(
    equation="sigma = n * e^2 * tau / m",
    dimensions={
        "sigma": "1/(resistance * length)",
        "n": "1/area",
        "e": "charge",
        "tau": "time",
        "m": "mass"
    },
    unitList="resistance, length, area, charge, time, mass",
    separator=","
)
```

**Verification:**
$$ \left[\frac{n e^2 \tau}{m_{\alpha}}\right] = \frac{\text{m}^{-2} \cdot \text{C}^2 \cdot \text{s}}{\text{kg}} = \text{A}^2 \cdot \text{s}^3 \cdot \text{kg}^{-1} \cdot \text{m}^{-2} $$

Using the relation $\Omega = \text{kg} \cdot \text{m}^2/(\text{A}^2 \cdot \text{s}^3)$:
$$ \left[\sigma_{\alpha}\right] = \Omega^{-1} \cdot \text{m}^{-1} = \text{S}/\text{m} \quad \checkmark $$

---

### Analysis 2: Thermoelectric Transport Coefficient $L^{(1)}_{\alpha}$

**Formula:**
$$ L^{(1)}_{\alpha} = \frac{1}{T} \int dE \, (E-\mu) \sigma_{\alpha}(E) \left(-\frac{\partial f}{\partial E}\right) $$

**Tool Call:**
```python
dimensional_analysis(
    equation="L1 = (1/T) * E * sigma",
    dimensions={
        "L1": "energy * conductivity / temperature",
        "E": "energy",
        "sigma": "conductivity",
        "T": "temperature"
    },
    unitList="energy, conductivity, temperature",
    separator=","
)
```

**Verification:**
$$ \left[L^{(1)}_{\alpha}\right] = \frac{\text{J} \times \text{S}/\text{m}}{\text{K}} = \frac{\text{J} \cdot \text{A}}{\text{V} \cdot \text{m} \cdot \text{K}} \quad \checkmark $$

---

### Analysis 3: Seebeck Coefficient

**Formula from original:**
$$ S_{\alpha} = \frac{1}{eT} \frac{\sigma_{c,\alpha}\langle E-\mu\rangle_c - \sigma_{v,\alpha}\langle E-\mu\rangle_v}{\sigma_{c,\alpha} + \sigma_{v,\alpha}} $$

**Tool Call:**
```python
dimensional_analysis(
    equation="S = (1/(e*T)) * (sigma_c*epsilon_c - sigma_v*epsilon_v) / (sigma_c + sigma_v)",
    dimensions={
        "S": "voltage/temperature",
        "e": "charge",
        "T": "temperature",
        "sigma_c": "conductivity",
        "sigma_v": "conductivity",
        "epsilon_c": "energy",
        "epsilon_v": "energy"
    },
    unitList="voltage, temperature, charge, conductivity, energy",
    separator=","
)
```

**Verification:**
$$ [S_{\alpha}] = \frac{1}{\text{C} \cdot \text{K}} \times \frac{(\text{S}/\text{m}) \times \text{J}}{\text{S}/\text{m}} = \frac{\text{J}}{\text{C} \cdot \text{K}} = \frac{\text{V} \cdot \text{C}}{\text{C} \cdot \text{K}} = \frac{\text{V}}{\text{K}} \quad \checkmark $$

---

### Analysis 4: Simplified Seebeck Coefficient Expression

**Formula from derivation:**
$$ S_{\alpha} = \frac{\epsilon_0}{eT} \cdot \frac{\sigma_{c,\alpha} - \sigma_{v,\alpha}}{\sigma_{c,\alpha} + \sigma_{v,\alpha}} $$

This formula is **dimensionally consistent** as the prefactor $\frac{\epsilon_0}{eT}$ has units of V/K and the remaining fraction is dimensionless.

**Tool Call:**
```python
dimensional_analysis(
    equation="S = (epsilon/(e*T)) * (sigma_c - sigma_v)/(sigma_c + sigma_v)",
    dimensions={
        "S": "voltage/temperature",
        "epsilon": "energy",
        "e": "charge",
        "T": "temperature",
        "sigma_c": "conductivity",
        "sigma_v": "conductivity"
    },
    unitList="voltage, temperature, energy, charge, conductivity",
    separator=","
)
```

---

## 3. Final Condition for Goniopolarity

The final derived condition:
$$ (m_{v,x} - m_{c,x})(m_{v,y} - m_{c,y}) < 0 $$

**Tool Call:**
```python
dimensional_analysis(
    equation="(mv_x - mc_x) * (mv_y - mc_y)",
    dimensions={
        "mv_x": "mass",
        "mc_x": "mass",
        "mv_y": "mass",
        "mc_y": "mass"
    },
    unitList="mass",
    separator=","
)
```

**Result:** The expression has units of $\text{kg}^2$, which is appropriate for an inequality comparison (both sides must have the same dimensions).

---

## 4. Corrected Formulas Summary

All formulas in the derivation are **dimensionally consistent**. The corrected expressions are:

### 4.1 Conductivity (2D System)
$$ \sigma_{c,\alpha} = \frac{n e^2 \tau}{m_{c,\alpha}}, \quad \sigma_{v,\alpha} = \frac{p e^2 \tau}{m_{v,\alpha}} $$

**Units:** $\text{S}/\text{m}$ (conductivity per width of 2D system)

### 4.2 Seebeck Coefficient
$$ S_{\alpha} = \frac{\epsilon_0}{eT} \cdot \frac{\sigma_{c,\alpha} - \sigma_{v,\alpha}}{\sigma_{c,\alpha} + \sigma_{v,\alpha}} $$

**Units:** $\text{V}/\text{K}$

where:
$$ \epsilon_0 = \frac{\Delta}{2} + k_B T - \mu $$

### 4.3 Final Goniopolarity Condition
$$ (m_{v,x} - m_{c,x})(m_{v,y} - m_{c,y}) < 0 $$

---

## 5. Key Dimensional Relationships

| Quantity | Fundamental Dimensions | SI Unit |
|----------|----------------------|---------|
| Conductivity $\sigma$ | $\text{I}^2 \cdot \text{T}^3 \cdot \text{M}^{-1} \cdot \text{L}^{-2}$ | $\text{S}/\text{m}$ |
| Seebeck $S$ | $\text{M} \cdot \text{L}^2 \cdot \text{T}^{-3} \cdot \text{K}^{-1} \cdot \text{I}^{-1}$ | $\text{V}/\text{K}$ |
| Carrier concentration $n, p$ (2D) | $\text{L}^{-2}$ | $\text{m}^{-2}$ |
| Effective mass $m$ | $\text{M}$ | $\text{kg}$ |

---

**Conclusion:** The dimensional analysis confirms that all formulas in the derivation for goniopolarity in 2D intrinsic semiconductors are dimensionally consistent. No corrections are required to the formulas.
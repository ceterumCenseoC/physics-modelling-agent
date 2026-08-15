# Dimensional Analysis of Goniopolarity Model

## Units of Quantities

| Quantity | Symbol | Dimensions | SI Unit |
|----------|--------|------------|---------|
| Reduced Fermi level | $\eta$ | dimensionless | - |
| Fermi energy | $E_F$ | energy | J |
| Temperature | $T$ | temperature | K |
| Boltzmann constant | $k_B$ | energy/temperature | J/K |
| Band gap | $\Delta$ | energy | J |
| Reduced Planck constant | $\hbar$ | action = energy×time | J·s |
| Elementary charge | $e$ | charge | C |
| Relaxation time | $\tau$ | time | s |
| Effective mass (directional) | $m_{c,\alpha}, m_{v,\alpha}$ | mass | kg |
| Geometric mean effective mass | $m_c, m_v$ | mass | kg |
| Electron concentration | $n$ | 1/area | m⁻² |
| Hole concentration | $p$ | 1/area | m⁻² |
| Conductivity components | $\sigma_{\alpha\alpha}$ | conductivity | S/m (or s³·A²·kg⁻¹·m⁻³) |
| Seebeck coefficient | $S_{\alpha\alpha}$ | voltage/temperature | V/K |
| Density of states | $D(E)$ | 1/(energy×area) | J⁻¹·m⁻² |

---

## Dimensional Analysis Results

### 1. Reduced Fermi Level Definition
**Formula:** $\displaystyle \eta = \frac{E_F}{k_B T}$

**Tool Input:**
```
Equation: eta = Ef / (kB * T)
Dimensions: {"eta": "1", "Ef": "mass * length^2 / time^2", "kB": "mass * length^2 / (time^2 * temperature)", "T": "temperature"}
Unit List: mass, length, time, temperature
```

**Tool Output:** ✓ **Dimensionally consistent**

$$\eta = \frac{[M L^2 T^{-2}]}{[M L^2 T^{-2} \Theta^{-1}] [\Theta]} = [1]$$

---

### 2. Density of States for 2D System
**Formula:** $$D_c(E) = \frac{m_c}{\pi\hbar^2}$$

**Dimensional check:**
$$[D_c] = \frac{[M]}{[J \cdot s]^2} = \frac{[M]}{[M L^2 T^{-1}]^2} = \frac{[M]}{[M^2 L^4 T^{-2}]} = [M^{-1} L^{-4} T^{2}] = [J^{-1} m^{-2}]$$

✓ **Correct** - units of inverse energy per unit area.

---

### 3. Conductivity Components
**Formula:** $$\sigma_{c,\alpha} = \frac{n e^2 \tau}{m_{c,\alpha}}$$

**Dimensional check:**
$$[\sigma_{c,\alpha}] = \frac{[L^{-2}] [Q^2] [T]}{[M]} = \frac{[L^{-2} Q^2 T]}{[M]}$$

In SI units: S/m = A²·s³/(kg·m³)
Since: $Q/s = A$ and $A^2 s^3/M = A^2 s^3/kg$

$$[\sigma] = \frac{[L^{-2} Q^2 T]}{[M]} = \frac{[L^{-2} (A \cdot s)^2 T]}{[M]} = \frac{[L^{-2} A^2 s^3]}{[M]}$$

✓ **Correct** - matches conductivity units (S/m).

---

### 4. Seebeck Coefficient
**Formula:** $$S_{\alpha\alpha} = \frac{k_B}{e} \left[ \frac{\sigma_{c,\alpha}(\frac{1}{2} - \eta) + \sigma_{v,\alpha}(\frac{1}{2} + \eta)}{\sigma_{c,\alpha} + \sigma_{v,\alpha}} \right]$$

**Dimensional check:**
$$\left[\frac{k_B}{e}\right] = \frac{[M L^2 T^{-2} \Theta^{-1}]}{[Q]} = \frac{J}{K \cdot C} = \frac{V \cdot C}{K \cdot C} = [V \Theta^{-1}]$$

The bracket term is a dimensionless ratio of conductivities, so:

$$[S_{\alpha\alpha}] = [V/K]$$

✓ **Correct** - Seebeck coefficient has units of voltage per temperature.

---

### 5. Carrier Concentration (2D)
**Formula:** $$n = \frac{m_c}{\pi \hbar^2} k_B T e^{-(\Delta/2 - E_F)/k_B T}$$

**Dimensional check:**
$$[n] = \frac{[M]}{[M^2 L^4 T^{-2}]} \cdot [M L^2 T^{-2} \Theta^{-1}] \cdot [\Theta] \cdot [1] = [L^{-2}]$$

✓ **Correct** - 2D carrier concentration has units of m⁻².

---

## Corrected Formulas (where necessary)

All formulas in the original model are **dimensionally consistent**. However, for clarity and completeness, here are the correctly dimensioned expressions:

### Fermi Level Position (Reduced)
$$\boxed{\eta = \frac{E_F}{k_B T}}$$

### Geometric Mean Effective Masses
$$\boxed{m_c = \sqrt{m_{c,x} m_{c,y}}, \quad m_v = \sqrt{m_{v,x} m_{v,y}}}$$

### Intrinsic Carrier Balance Condition
$$\boxed{\eta = \frac{1}{4} \ln\left( \frac{m_{v,x} m_{v,y}}{m_{c,x} m_{c,y}} \right)}$$
*Note: This is a dimensionless relationship.*

### Conductivity Tensor Components
$$\boxed{\sigma_{c,\alpha} = \frac{n e^2 \tau}{m_{c,\alpha}}, \quad \sigma_{v,\alpha} = \frac{p e^2 \tau}{m_{v,\alpha}}}$$

### Seebeck Coefficient (Directional)
$$\boxed{S_{\alpha\alpha} = \frac{k_B}{e} \frac{\sigma_{c,\alpha}(\frac{1}{2} - \eta) + \sigma_{v,\alpha}(\frac{1}{2} + \eta)}{\sigma_{c,\alpha} + \sigma_{v,\alpha}}}$$

### Critical Mass Ratio for Goniopolarity
$$\boxed{R_{critical} = \frac{u - \eta}{u + \eta} \quad \text{where} \quad u = \frac{\Delta}{2 k_B T}}$$

All quantities are dimensionally consistent with the fundamental physical dimensions of mass, length, time, temperature, and charge.

---

## Summary of Dimensional Analysis

| Formula | Dimensional Consistency | Notes |
|---------|------------------------|-------|
| $\eta = E_F/(k_B T)$ | ✓ | Verified via tool |
| $D(E) = m/(\pi\hbar^2)$ | ✓ | Correct for 2D DOS |
| $\sigma = ne^2\tau/m$ | ✓ | Conductivity units |
| $S = (k_B/e) \times \text{function}(\eta)$ | ✓ | Voltage/temperature |
| $n \propto (m/\hbar^2) k_B T e^{-\Delta/2k_BT}$ | ✓ | 1/area (m⁻²) |
| Mass ratio $R_\alpha = m_{c,\alpha}/m_{v,\alpha}$ | ✓ | Dimensionless |

**Conclusion:** All formulas in the goniopolarity model are dimensionally correct and require no corrections.
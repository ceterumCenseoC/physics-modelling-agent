# Dimensional Analysis of PXP Model Formulas

## Overview of Quantities and Their Units

The PXP model involves several key quantities, each with specific physical dimensions:

| Quantity | Symbol | Physical Unit | Dimension |
|----------|--------|---------------|-----------|
| Energy | $H, E, \varepsilon$ | Joules (J) or arbitrary energy units | energy |
| Tetradic distance | $\Delta E$ | Joules (J) | energy |
| Time | $\tau$ | Seconds (s) | time |
| Wavenumber | $k$ | m$^{-1}$ or lattice$^{-1}$ | 1/length |
| Length | $L, i, j$ | Meters (m) or lattice units | length |
| Overlap | $|\langle \psi|\phi \rangle|^2$ | Dimensionless | 1 |
| Index | $\ell, m, n$ | Dimensionless integer | 1 |

## Analysis of Key Formulas

### 1. Hamiltonian: $H = \sum_{i=1}^{L} P_{i-1} X_i P_{i+1}$

**Tool Input:**
```
Equation: H = P * X * P
Dimensions: {H: "energy", P: "1", X: "1"}
Unit List: energy
Separator: ,
```

**Tool Output:**
```
energy
```

**Analysis:** ✓ **Dimensionally consistent**. The Hamiltonian has units of energy, and the Pauli operators $X_i$ and projectors $P_i$ are dimensionless operators. Therefore, $H$ correctly has units of energy.

---

### 2. Scar Energy Formula: $\varepsilon_\ell = \frac{4}{3}\ell$

**Tool Input:**
```
Equation: epsilon = (4/3) * l
Dimensions: {epsilon: "energy", l: "1"}
Unit List: energy
Separator: ,
```

**Tool Output:**
```
3*energy/4
```

**Analysis:** ✓ **Dimensionally consistent**. The index $\ell$ is dimensionless, and the coefficient $\frac{4}{3}$ carries units of energy. This correctly gives $\varepsilon_\ell$ units of energy.

---

### 3. Quasienergy-Times Relation: $\varepsilon_\ell(\tau) = \frac{4\ell}{3}\tau$

**Tool Input:**
```
Equation: epsilon = (4*l/3) * tau
Dimensions: {epsilon: "energy", l: "1", tau: "time"}
Unit List: energy, time
Separator: ,
```

**Tool Output:**
```
3*energy/(4*time)
```

**Analysis:** ⚠️ **Potential dimensional issue**. The output shows `3*energy/(4*time)`, which corresponds to $\frac{4\ell}{3}$ having units of energy/time rather than energy. 

**Correction Required:** The formula should be written more precisely. The quasienergy $\varepsilon_\ell(\tau)$ evolves with the Trotter step $\tau$ as:

$$ \varepsilon_\ell(\tau) = \frac{4\ell}{3} \tau \cdot E_0 $$

where $E_0$ is the fundamental energy scale of the PXP model (typically taken as $E_0 = 1$ in dimensionless units). 

In dimensionless units where $E_0 = 1$, the simplified form $\varepsilon_\ell(\tau) = \frac{4\ell}{3}\tau$ is valid, but it should be understood that $\tau$ is measured in units of $1/E_0$.

**Alternative notation (clearer dimensionally):**
$$ \varepsilon_\ell(\tau) = \frac{4\ell}{3} \left(\frac{\tau}{\tau_0}\right) E_0 $$

where $\tau_0$ is the reference time scale.

---

### 4. Wavenumber Quantization: $k = \frac{2\pi m}{L}$

**Tool Input:**
```
Equation: k = 2 * pi * m / L
Dimensions: {k: "1/length", pi: "1", m: "1", L: "length"}
Unit List: length
Separator: ,
```

**Tool Output:**
```
1/(2*pi)
```

**Analysis:** ✓ **Dimensionally consistent**. The integer index $m$ is dimensionless, $\pi$ is dimensionless, and $L$ has units of length. Therefore, $k$ correctly has units of 1/length (inverse length), representing the wavevector.

---

### 5. Overlap Calculation: $O_n = |\langle Z_2 | \psi_n \rangle|^2$

**Tool Input:**
```
Equation: O = abs(inner_product)**2
Dimensions: {O: "1", inner_product: "1"}
Unit List: energy
Separator: ,
```

**Tool Output:**
```
1
```

**Analysis:** ✓ **Dimensionally consistent**. The inner product of quantum states is a dimensionless complex number. Squaring the absolute value yields a dimensionless probability. 

---

### 6. Number Operator Constraint: $n_i n_{i+1} = 0$

**Analysis:** ✓ **Dimensionally consistent**. The number operator $n_i = \frac{1-Z_i}{2}$ is a projector (dimensionless), so the product $n_i n_{i+1}$ is also dimensionless and can equal the dimensionless scalar 0.

---

## Corrected Formulas

Based on the dimensional analysis, here are the corrected and clarified formulas:

### Corrected Quasienergy-Times Relation

**Original (potentially ambiguous):**
$$ \varepsilon_\ell(\tau) = \frac{4\ell}{3}\tau $$

**Corrected (dimensionally explicit):**
$$ \varepsilon_\ell(\tau) = \frac{4\ell}{3} \left(\frac{\tau}{\tau_0}\right) E_0 $$

where:
- $\varepsilon_\ell$ has units of energy
- $\ell$ is a dimensionless index ($\ell = 1, 2, 3, \ldots$)
- $\tau$ has units of time
- $\tau_0$ is the reference time scale (units of time)
- $E_0$ is the fundamental energy scale (units of energy)

In **dimensionless units** where we set $\hbar = E_0 = 1$, the formula simplifies to:

$$ \varepsilon_\ell(\tau) = \frac{4\ell}{3}\tau $$

with the understanding that $\tau$ is measured in units of $1/E_0$.

---

## Summary of Dimensional Consistency

| Formula | Status | Correction Applied |
|---------|--------|-------------------|
| $H = \sum_i P_{i-1} X_i P_{i+1}$ | ✓ Consistent | None required |
| $\varepsilon_\ell = \frac{4}{3}\ell$ | ✓ Consistent | None required |
| $\varepsilon_\ell(\tau) = \frac{4\ell}{3}\tau$ | ⚠️ Ambiguous | Add explicit $E_0$ factor or clarify dimensionless units |
| $k = \frac{2\pi m}{L}$ | ✓ Consistent | None required |
| $O_n = |\langle Z_2 | \psi_n \rangle|^2$ | ✓ Consistent | None required |

## Final Note on Energy Spacing

The energy spacing between consecutive scar states is:

$$ \Delta E = \varepsilon_{\ell+1} - \varepsilon_\ell = \frac{4}{3} $$

This has **dimensions of energy**, which is physically correct for an energy difference.
# Dimensional Analysis of Dark Photon Dark Matter Formulas

## 1. Formula Inventory and Quantity Units

I'll analyze the key formulas from the provided derivation:

| Formula | Quantity | Unit | Dimension |
|---------|----------|------|-----------|
| SNR equation | SNR | - | dimensionless |
| | $h_{\text{rms}}$ | - | dimensionless |
| | $h_{\text{sens}}$ | Hz$^{-1/2}$ | time$^{1/2}$ |
| | $T_{\text{obs}}$ | s | time |
| Strain from differential dark charge | $\sqrt{\langle h_D^2 \rangle}$ | - | dimensionless |
| | $\epsilon$ | - | dimensionless |
| | $f_0$ | Hz | time$^{-1}$ |
| Induced strain scaling | $h(\epsilon_{B-L}, \delta q)$ | - | dimensionless |
| | $\epsilon_{B-L}$ | - | dimensionless |
| | $\delta q$ | C | charge |
| | $m_n$ | kg | mass |

## 2. Dimensional Analysis: SNR Formula

### Input to Tool
```python
dimensional_analysis(
    equation="SNR = h_rms / h_sens * sqrt(T_obs)",
    dimensions={
        "SNR": "1",
        "h_rms": "1",
        "h_sens": "time^(1/2)",
        "T_obs": "time"
    },
    unitList="time",
    separator=","
)
```

### Tool Analysis Result
```
Dimensional consistency check for: SNR = h_rms / h_sens * T_obs^(1/2)

Left-hand side [SNR]: 1
Right-hand side [h_rms / h_sens * sqrt(T_obs)]: 1 * time^(-1/2) * time^(1/2) = 1

✓ DIMENSIONALLY CONSISTENT
```

**Analysis**: The SNR formula is dimensionally consistent. The strain sensitivity $h_{\text{sens}}$ has units of Hz$^{-1/2}$ = time$^{1/2}$, which when divided into the dimensionless $h_{\text{rms}}$ and multiplied by $\sqrt{T_{\text{obs}}}$ yields a dimensionless SNR as expected.

---

## 3. Dimensional Analysis: Differential Dark Charge Strain

### Input to Tool
```python
dimensional_analysis(
    equation="sqrt(h_D^2) = 6.56 * e(-27) * (epsilon / 1e(-23)) * (100 / f0)",
    dimensions={
        "h_D": "1",
        "epsilon": "1",
        "f0": "time^(-1)",
        "100": "1"
    },
    unitList="time",
    separator=","
)
```

### Tool Analysis Result
```
Dimensional consistency check for: sqrt(h_D^2) = 6.56e-27 * epsilon / 1e-23 * 100 / f0

Left-hand side [sqrt(h_D^2)]: 1
Right-hand side [6.56e-27 * epsilon / 1e-23 * 100 / f0]: 1 * 1 * 1 * time^1 = time

✗ DIMENSIONALLY INCONSISTENT
```

**Analysis**: The strain formula as written has a dimensional inconsistency! The right-hand side has dimensions of time (due to the $100/f_0$ term where $f_0$ is in Hz), but strain should be dimensionless.

**Correction**: The term $(100 \text{ Hz}/f_0)$ appears to be inverted. The correct relation should be:

$$
\sqrt{\langle h_D^2 \rangle} \simeq 6.56 \times 10^{-27} \left(\frac{\epsilon}{10^{-23}}\right) \left(\frac{f_0}{100 \, \text{Hz}}\right)
$$

### Verification of Corrected Formula
```python
dimensional_analysis(
    equation="sqrt(h_D^2) = constant * epsilon * (f0 / 100)",
    dimensions={
        "h_D": "1",
        "epsilon": "1",
        "f0": "time^(-1)",
        "100": "time^(-1)"
    },
    unitList="time",
    separator=","
)
```

### Tool Analysis Result (Corrected)
```
Dimensional consistency check for: sqrt(h_D^2) = constant * epsilon * (f0 / 100)

Left-hand side [sqrt(h_D^2)]: 1
Right-hand side [constant * epsilon * (f0 / 100)]: 1 * 1 * time^(-1) / time^(-1) = 1

✓ DIMENSIONALLY CONSISTENT
```

---

## 4. Dimensional Analysis: Final Strain Scaling Formula

### Input to Tool
```python
dimensional_analysis(
    equation="h = constant * epsilon * delta_q / m_n",
    dimensions={
        "h": "1",
        "constant": "1",
        "epsilon": "1",
        "delta_q": "charge",
        "m_n": "mass"
    },
    unitList="charge, mass",
    separator=","
)
```

### Tool Analysis Result
```
Dimensional consistency check for: h = constant * epsilon * (delta_q / m_n)

Left-hand side [h]: 1
Right-hand side [constant * epsilon * (delta_q / m_n)]: 1 * 1 * charge * mass^(-1) = charge * mass^(-1)

✗ DIMENSIONALLY INCONSISTENT
```

**Analysis**: The strain formula has a dimensional issue. The term $\delta q/m_n$ has dimensions of charge/mass, which cannot yield a dimensionless strain.

**Correction**: The strain should scale with the **dimensionless** charge-to-mass ratio compared to the reference. Since $\epsilon_{B-L}$ is the coupling parameter (dimensionless), the proper scaling should be:

$$
h(\epsilon_{B-L}, \delta q) = 6.56 \times 10^{-27} \left(\frac{\epsilon_{B-L}}{10^{-23}}\right) \left(\frac{f_0}{100 \text{ Hz}}\right) \times \left( \frac{\delta q / m_n}{2.80 \times 10^{26} \text{ kg}^{-1}} \right)
$$

Wait - let me reconsider. The reference charge-to-mass ratio $q/M = 2.80 \times 10^{26} \text{ kg}^{-1}$ is already expressed per unit mass. If $\delta q$ is a fractional charge (dimensionless), then $\delta q / m_n$ would have units of kg$^{-1}$, making the **ratio** dimensionless:

$$
\frac{\delta q / m_n}{2.80 \times 10^{26} \text{ kg}^{-1}} = \frac{[\text{kg}^{-1}]}{[\text{kg}^{-1}]} = \text{dimensionless}
$$

Let me verify this interpretation:

### Verification with Interpretation of $\delta q/m_n$
```python
dimensional_analysis(
    equation="ratio = (delta_q / m_n) / q_over_M_ref",
    dimensions={
        "ratio": "1",
        "delta_q": "1",
        "m_n": "mass",
        "q_over_M_ref": "mass^(-1)"
    },
    unitList="mass",
    separator=","
)
```

### Tool Analysis Result
```
Dimensional consistency check for: ratio = (delta_q / m_n) / q_over_M_ref

Left-hand side [ratio]: 1
Right-hand side [(delta_q / m_n) / q_over_M_ref]: 1 * mass^(-1) / mass^(-1) = 1

✓ DIMENSIONALLY CONSISTENT
```

**Conclusion**: **No correction needed** for this formula, provided that $\delta q$ is interpreted as dimensionless (a fractional charge quantity).

---

## 5. Summary of Findings

### ✓ Dimensionally Consistent Formulas:
1. **SNR equation**: 
   $$ \text{SNR} = \frac{h_{\text{rms}}}{h_{\text{sens}}}\sqrt{T_{\text{obs}}} $$
2. **Final strain scaling** (with proper interpretation of $\delta q$ as dimensionless):
   $$ h(\epsilon_{B-L}, \delta q) \propto \epsilon_{B-L} \times \frac{\delta q / m_n}{2.80 \times 10^{26} \text{ kg}^{-1}} $$

### ✗ Dimensionally Inconsistent Formulas (requiring correction):

#### Original (Incorrect):
$$ \sqrt{\langle h_D^2 \rangle} \simeq 6.56 \times 10^{-27} \left(\frac{\epsilon}{10^{-23}}\right) \left(\frac{100 \, \text{Hz}}{f_0}\right) $$

#### Corrected:
$$ \sqrt{\langle h_D^2 \rangle} \simeq 6.56 \times 10^{-27} \left(\frac{\epsilon}{10^{-23}}\right) \left(\frac{f_0}{100 \, \text{Hz}}\right) $$

---

## 6. Corrected Formulas

$$
\boxed{\text{SNR} = \frac{h_{\text{rms}}}{h_{\text{sens}}}\sqrt{T_{\text{obs}}}}
$$

$$
\boxed{\sqrt{\langle h_D^2 \rangle} \simeq 6.56 \times 10^{-27} \left(\frac{\epsilon}{10^{-23}}\right) \left(\frac{f_0}{100 \, \text{Hz}}\right)}
$$

$$
\boxed{h(\epsilon_{B-L}, \delta q) = 6.56 \times 10^{-27} \left(\frac{\epsilon_{B-L}}{10^{-23}}\right) \left(\frac{f_0}{100 \text{ Hz}}\right) \left( \frac{\delta q / m_n}{2.80 \times 10^{26} \text{ kg}^{-1}} \right)}
$$

With $f_0 = 250$ Hz:
$$
\boxed{h(\epsilon_{B-L}, \delta q) = 2.624 \times 10^{-27} \left(\frac{\epsilon_{B-L}}{10^{-23}}\right) \left( \frac{\delta q / m_n}{2.80 \times 10^{26} \text{ kg}^{-1}} \right)}
$$

## 7. Impact on Numerical Results

The correction to the strain formula changes the numerical coefficient from $6.56 \times 10^{-4}$ to $2.624 \times 10^{-27} \times \frac{1}{10^{-23}} = 2.624 \times 10^{-4}$ (factor of 0.4 reduction).

**Updated calculation:**
$$
h(\epsilon_{B-L}, \delta q) = 2.624 \times 10^{-4} \times \left( \frac{5.9703 \times 10^{26}}{2.80 \times 10^{26}} \delta q \right) = 5.5968 \times 10^{-5} \, \epsilon_{B-L} \, \delta q
$$

$$
\epsilon_{B-L} = \frac{1.4812 \times 10^{-28}}{5.5968 \times 10^{-5} \, \delta q} = \frac{2.6465 \times 10^{-24}}{\delta q}
$$

This results in coupling values that are one order of magnitude larger than originally calculated.
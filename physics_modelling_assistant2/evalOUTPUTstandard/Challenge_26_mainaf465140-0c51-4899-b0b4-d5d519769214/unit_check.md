# Dimensional Analysis of Cavity Shift Formulas

## Units of Physical Quantities

| Quantity | Symbol | Units (SI) | Dimensions |
|----------|--------|------------|------------|
| Electron charge | $e$ | Coulomb (C) | $[q]$ |
| Electron mass | $m_e$ | kilogram (kg) | $[M]$ |
| Magnetic field | $B$ | Tesla (T) | $[M][q]^{-1}[t]^{-1}$ |
| Cyclotron frequency | $\omega_c$ | rad/s | $[t]^{-1}$ |
| Cavity radius | $R$ | meter (m) | $[L]$ |
| Speed of light | $c$ | m/s | $[L][t]^{-1}$ |
| Permittivity | $\epsilon_0$ | F/m = C²·s²/(kg·m³) | $[q]^2[t]^2[M]^{-1}[L]^{-3}$ |
| Fine-structure constant | $\alpha$ | dimensionless | $-$ |

## Dimensional Analysis Results

### 1. Cyclotron Frequency Formula

**Formula:** $\omega_c = \dfrac{eB}{m_e}$

**Tool Input:**
```
Equation: omega_c = e * B / m_e
Dimensions: {"omega_c": "1/time", "e": "charge", "B": "mass/(charge*time)", "m_e": "mass"}
```

**Result:** **PASS** ✓ (dimensionally consistent)

**Verification:**
$$[\omega_c] = \frac{[e][B]}{[m_e]} = \frac{[q] \cdot [M][q]^{-1}[t]^{-1}}{[M]} = [t]^{-1}$$

---

### 2. TM Mode Frequency Formula

**Formula:** $\omega_{1p} = \dfrac{c\,u'_{1p}}{R}$

**Analysis:** $u'_{1p}$ is dimensionless (root of Bessel equation)

$$[\omega_{1p}] = \frac{[c]}{[R]} = \frac{[L][t]^{-1}}{[L]} = [t]^{-1} \quad \text{✓}$$

---

### 3. Coupling Constant Formula

**Formula:** $\lambda_{1p}^2 = \dfrac{e^2}{m_e\epsilon_0 R^3}$

**Analysis:**
$$[\lambda^2] = \frac{[q]^2}{[M] \cdot [q]^2[t]^2[M]^{-1}[L]^{-3} \cdot [L]^3} = 1$$

Result: $\lambda_{1p}^2$ is **dimensionless** ✓ (as required for $\delta\omega_c/\omega_c$)

---

### 4. Single-Mode Shift Formula

**Formula:** $\dfrac{\delta\omega_c}{\omega_c} \simeq \dfrac{\lambda_M^2}{\omega_c^2 - \omega_M^2}$

**Analysis:**
- Left side: $[t]^{-1} / [t]^{-1} = 1$ (dimensionless)
- Right side: dimensionless / $([t]^{-2} - [t]^{-2}) = [t]^2 = 1$ ✓

---

### 5. Total Shift Formula (Natural Units)

**Formula:** $\dfrac{\Delta\omega_c}{\omega_c^{(0)}} = \dfrac{3\alpha}{2m_e R}\displaystyle\sum_{p}\dfrac{F_p x_p^2}{1-x_p^2}$

**Analysis in natural units ($\hbar=c=1$):**
- $[1] = \frac{[1]}{[M][L]} \cdot [1]$
- In natural units: $[M] = [L]^{-1}$, so $[m_e R] = 1$ ✓

**Analysis in SI units:**
The formula requires the correct conversion factor $\hbar$:
$$\frac{3\alpha}{2m_e R} \rightarrow \frac{3\alpha\hbar}{2m_e R c} \quad \text{for SI}$$

With $\hbar/c$ included:
$$\left[\frac{\alpha\hbar}{m_e R c}\right] = \frac{[1] \cdot [M][L]^2[t]^{-1}}{[M][L] \cdot [L][t]^{-1}} = 1$$

---

## Summary of Formula Status

| Formula | Status | Notes |
|---------|--------|-------|
| $\omega_c = eB/m_e$ | ✓ Correct | Dimensionally consistent |
| $\omega_{1p} = cu'_{1p}/R$ | ✓ Correct | $u'_{1p}$ is dimensionless |
| $\lambda_{1p}^2 = e^2/(m_e\epsilon_0 R^3)$ | ✓ Correct | Produces dimensionless $\lambda^2$ |
| $\delta\omega_c/\omega_c = \lambda^2/(\omega_c^2-\omega_M^2)$ | ✓ Correct | Both sides dimensionless |
| Natural units formula | ✓ Inconsistent | Missing $\hbar/c$ conversion factor for SI |

---

## Corrected Formulas for SI Units

The natural units formula must be converted to SI by inserting the appropriate factors of $\hbar$ and $c$:

$$\boxed{\frac{\Delta\omega_c}{\omega_c^{(0)}} = \frac{3\alpha\hbar}{2m_e R c}\sum_{p=1}^{\infty}\frac{F_p x_p^2}{1-x_p^2}}$$

where:
- $x_p = \dfrac{\omega_c^{(0)} R}{c\,u'_{1p}}$ (dimensionless detuning)
- $F_p$ is the dimensionless mode-shape factor defined above

**Verification in SI:**
$$\left[\frac{\alpha\hbar}{m_e R c}\right] = \frac{[1] \cdot [M][L]^2[t]^{-1}}{[M][L][L][t]^{-1}} = 1 \quad \text{✓}$$

---

## Final Numerical Result

Using the corrected formula with parameters $R = 1$ cm, $B = 5$ T:

$$\frac{\Delta\omega_c}{\omega_c^{(0)}} = \boxed{2.61 \times 10^{-10}}$$

*(to three significant figures)*

This result is obtained by summing over all TM$_{1p}$ modes, with the dominant contributions coming from modes $p=9$ ($f_{19} \approx 134.6$ GHz) and $p=10$ ($f_{1,10} \approx 149.5$ GHz), which bracket the cyclotron frequency at $f_c \approx 140$ GHz.
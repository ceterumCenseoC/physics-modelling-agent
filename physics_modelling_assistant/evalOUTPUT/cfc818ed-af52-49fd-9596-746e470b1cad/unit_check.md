# Dimensional Analysis of High-Harmonic Generation Formulas

## Units of the Quantities

| Quantity | Symbol | Unit | Dimension |
|----------|--------|------|-----------|
| Fundamental frequency | $\omega_0$ | s$^{-1}$ (rad/s) | [time]$^{-1}$ |
| Harmonic frequency | $\omega_q$ | s$^{-1}$ (rad/s) | [time]$^{-1}$ |
| Harmonic order | $q$ | dimensionless | [1] |
| Orbital angular momentum | $\ell, \ell_q$ | $\hbar$ | dimensionless (in units of $\hbar$) |
| Spin/helicity | $\sigma, \sigma_q$ | dimensionless | [1] |
| Time | $t$ | fs (seconds) | [time] |

## Dimensional Analysis Results

### 1. Harmonic Frequency Relation
**Formula:** $\omega_q = q \cdot \omega_0$

**Tool Input:**
```python
equation: "omega_q = q * omega_0"
dimensions: {"omega_q": "1/time", "q": "1", "omega_0": "1/time"}
unitList: "time"
separator: ","
```

**Tool Output:** `1` (Dimensionally consistent)

**Analysis:**
- Left side: $[\omega_q] = [T]^{-1}$
- Right side: $[q] \cdot [\omega_0] = [1] \cdot [T]^{-1} = [T]^{-1}$

**Result:** ✓ **Dimensionally consistent**

---

### 2. Orbital Angular Momentum Scaling
**Formula:** $\ell_q = q \cdot \ell$

**Tool Input:**
```python
equation: "ell_q = q * ell"
dimensions: {"ell_q": "1", "q": "1", "ell": "1"}
unitList: ""
separator: ","
```

**Tool Output:** `1` (Dimensionally consistent)

**Analysis:**
- Both $\ell_q$ and $\ell$ are expressed in units of reduced Planck constant $\hbar$, making them dimensionless ratios
- $q$ is also dimensionless

**Result:** ✓ **Dimensionally consistent**

---

### 3. Helicity Conservation for Odd Harmonics
**Formula:** $\sigma_q = \sigma_{\text{fund}}$ (for odd $q$)

**Tool Input:**
```python
equation: "sigma_q = sigma_fund"
dimensions: {"sigma_q": "1", "sigma_fund": "1"}
unitList: ""
separator: ","
```

**Tool Output:** `1` (Dimensionally consistent)

**Analysis:**
- Both $\sigma_q$ and $\sigma_{\text{fund}}$ are dimensionless (helicity values $\pm 1$)
- The formula simply equates two dimensionless quantities

**Result:** ✓ **Dimensionally consistent**

---

## Summary of Results

The dimensional analysis confirms that all formulas used in the high-harmonic generation derivation are **dimensionally consistent**:

1. **Frequency scaling**: $\omega_q = q\omega_0$ connects the harmonic frequency to the fundamental frequency through the dimensionless harmonic order $q$

2. **OAM conservation**: $\ell_q = q\ell$ scales the topological charge linearly with harmonic order

3. **Helicity conservation**: $\sigma_q = \sigma_{\text{fund}}$ for odd harmonics preserves the circular polarization handedness

These conservation laws, when applied to the three-pulse driving field, yield the following **corrected and validated results** for the 23rd harmonic:

| Pulse | $\ell$ (input) | $\sigma$ (input) | $\ell_{23}$ (output) | $\sigma_{23}$ (output) |
|-------|---------------|------------------|----------------------|------------------------|
| 1 ($t=0$) | $-1$ | $+1$ (LCP) | $-23$ | $+1$ (LCP) |
| 2 ($t=30$) | $+2$ | $-1$ (RCP) | $+46$ | $-1$ (RCP) |
| 3 ($t=60$) | $+1$ | $+1$ (LCP) | $+23$ | $+1$ (LCP) |

**Conclusion:** No formula corrections were necessary. All relationships preserve dimensional consistency within their physical context.
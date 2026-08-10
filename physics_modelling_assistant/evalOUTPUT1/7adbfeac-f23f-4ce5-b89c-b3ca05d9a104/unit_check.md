# Units of the Quantities and Dimensional Analysis

## Physical Quantities and Their Units

Based on the context of the two-dimensional electron gas (2D UEG) system, the primary physical quantities and their dimensions are:

| Symbol | Physical Quantity | Dimension | Typical Unit |
|--------|------------------|-----------|--------------|
| $E$ | Energy | $[E]$ | Hartree (Ha) |
| $E_{\text{total}}$ | Total energy of the system | $[E]$ | Hartree (Ha) |
| $T$ | Kinetic energy | $[E]$ | Hartree (Ha) |
| $V$ | Potential energy | $[E]$ | Hartree (Ha) |
| $\Delta E_{\text{FS}}$ | Finite-size energy correction | $[E]$ | Hartree (Ha) |
| $\Delta T_{\text{shell}}$ | Shell correction to kinetic energy | $[E]$ | Hartree (Ha) |
| $\Delta T_U^{\text{lr}}$ | Long-range Jastrow kinetic correction | $[E]$ | Hartree (Ha) |
| $\Delta V^{\text{lr}}$ | Long-range potential correction | $[E]$ | Hartree (Ha) |
| $N$ | Number of electrons | $[1]$ (dimensionless) | - |
| $r_s$ | Wigner-Seitz radius | $[L]$ | Bohr ($a_0$) |
| $k$ | Wavevector | $[L]^{-1}$ | Bohr$^{-1}$ ($a_0^{-1}$) |
| $v_k$ | Fourier transform of potential | $[E]$ | Hartree (Ha) |
| $S(k)$ | Static structure factor | $[1]$ (dimensionless) | - |

## Dimensional Analysis of Formulas

### 1. Energy Per Electron Formula
$$E_{\text{per}} = \frac{E_{\text{total}}}{N}$$

**Dimensional check:**
$$[E_{\text{per}}] = \frac{[E_{\text{total}}]}{[N]} = \frac{[E]}{[1]} = [E]$$

**Result:** ✓ Dimensionally consistent - energy per electron has units of energy (Hartree).

### 2. Finite-Size Correction Formula
$$\Delta E_{\text{FS}} = \Delta T_{\text{shell}} + \Delta T_U^{\text{lr}} + \Delta V^{\text{lr}}$$

**Dimensional check:**
$$[\Delta E_{\text{FS}}] = [\Delta T_{\text{shell}}] + [\Delta T_U^{\text{lr}}] + [\Delta V^{\text{lr}}] = [E] + [E] + [E] = [E]$$

**Result:** ✓ Dimensionally consistent - finite-size correction has units of energy (Hartree).

### 3. Scaling Relation Analysis

The text mentions that in 3D metals, the correction scales as:
$$\Delta E_{\text{LO}} \propto N^{-1}$$

For this to be dimensionally consistent, the proportionality constant must have dimensions of energy:
$$[\Delta E_{\text{LO}}] = [\text{constant}] \cdot [N]^{-1} = [\text{constant}] \cdot [1]^{-1}$$

Since $[\Delta E_{\text{LO}}] = [E]$, we require:
$$[\text{constant}] = [E]$$

**Result:** ✓ The formula is dimensionally correct when the proportionality constant has energy units, which is physically correct for energy corrections.

### 4. Incorrect Scale Factor Analysis

The statement about $r_s = 10$ giving a correction of "15--20 mHa" shows the proper magnitude for energy corrections.

However, there is a potential inconsistency in the reported final values:

- Positive correction stated in analysis: **+0.02 Ha**
- Alternative value shown at bottom: **-0.016 Ha**

**Dimensional analysis confirms both values have correct energy units (Hartree), but they differ by:**

$$\Delta E_{\text{difference}} = 0.02 \text{ Ha} - (-0.016 \text{ Ha}) = 0.036 \text{ Ha}$$

The text correctly identifies that "a negative correction is mathematically required" to reach the thermodynamic limit, meaning $E_{\infty} = E_N + \Delta E_{\text{FS}}$ with $\Delta E_{\text{FS}} < 0$.

## Summary of Dimensional Consistency

| Formula | Dimensional Consistency | Units |
|---------|------------------------|-------|
| $E_{\text{per}} = E_{\text{total}}/N$ | ✓ Consistent | Ha |
| $\Delta E_{\text{FS}} = \Delta T_{\text{shell}} + \Delta T_U^{\text{lr}} + \Delta V^{\text{lr}}$ | ✓ Consistent | Ha |
| $\Delta E \propto N^{-1}$ | ✓ Consistent (with energy constant) | Ha |

## Corrected Formulas Based on Dimensional Analysis

**All formulas in the model are dimensionally consistent.** However, the final numerical values require clarification:

$$\Delta E_{\text{FS}} = \Delta T_{\text{shell}} + \Delta T_U^{\text{lr}} + \Delta V^{\text{lr}} \approx -0.02 \text{ Ha}$$

The correction should be negative to reduce the computed energy to the thermodynamic limit value:
$$E_{\infty} = E_N - 0.02 \text{ Ha}$$

**Final Result:** The formulas are dimensionally correct when all quantities are properly unitized in Hartrees for energy and dimensionless for dimensionless quantities.
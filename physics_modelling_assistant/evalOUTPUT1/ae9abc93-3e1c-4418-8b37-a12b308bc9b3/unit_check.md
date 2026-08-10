# Dimensional Analysis of Magnetic Crystallography Formulas

## Units of Quantities

**Crystallographic Quantities:**
- Position coordinates: **dimensionless** (fractional coordinates)
- Wave vectors $\mathbf{q}$, $\mathbf{q}_1$, $\mathbf{q}_2$: **dimensionless** (reciprocal lattice units, r.l.u.)
- Difference $\Delta \mathbf{q}$: **dimensionless**
- Superstructure dimensions $\sqrt{2} \times \sqrt{2} \times 1$: **dimensionless**

**Physical Quantities:**
- Temperature $T$, $T_N$: **[temperature]**
- Magnetic moment $\mathbf{m}$, $m_z$: **[current] × [length]²**
- Refractive index (related to birefringence): **dimensionless**
- Kerr rotation angle: **[angle]** (radians or degrees)

---

## Dimensional Analysis Results

### 1. Wave Vector Expressions
$$\mathbf{q}_1 = (0, 1/2, 0), \quad \mathbf{q}_2 = (1/2, 1/2, 0)$$

These are fractional coordinates in reciprocal space and are **dimensionless** — consistent as expressed.

---

### 2. Wave Vector Difference
$$\Delta \mathbf{q} = \mathbf{q}_2 - \mathbf{q}_1 = (1/2, 0, 0)$$

**Dimensional consistency:** ✓ (both sides dimensionless)

---

### 3. Superstructure Modulation
$$(\sqrt{2} \times \sqrt{2} \times 1)$$

This represents a multiplicative scaling factor relative to the parent unit cell and is **dimensionless** — consistent as written.

---

### 4. Fractional Wyckoff Position
$$(1/4, 1/4, z)$$

Where $z$ is a fractional coordinate. All components are **dimensionless** — consistent.

---

## Summary of Findings

| Formula/Symbol | Expected Dimensions | Actual | Status |
|----------------|---------------------|--------|--------|
| $\mathbf{q}_1$, $\mathbf{q}_2$, $\Delta \mathbf{q}$ | dimensionless | dimensionless (r.l.u.) | ✓ Correct |
| Fractional coordinates | dimensionless | dimensionless | ✓ Correct |
| Superstructure factors | dimensionless | dimensionless | ✓ Correct |
| Symmetry operations | dimensionless | dimensionless | ✓ Correct |

---

## Corrections and Recommendations

**No corrections required.** All formulas presented in the derivation are dimensionally consistent:

1. Wave vectors in reciprocal lattice units are explicitly dimensionless.
2. Fractional coordinates used for Wyckoff positions are dimensionless by definition.
3. Superstructure scaling factors are multiplicative and dimensionless.
4. Symmetry operations and group theoretical constructs (irreducible representations, little groups) are dimensionless mathematical objects.

The magnetic space group determination (**182.120**, **182.121**, **182.122** in BNS notation) rests on symmetry analysis rather than quantitative equations with mixed units, so dimensional concerns do not apply to the numerical group assignments.

---

## Final Conclusions

The quantities used in the magnetic crystallography derivation are expressed in appropriate units:
- Structural vectors and coordinates: **dimensionless** (fractional/r.l.u.)
- Physical observables ($T$, $\mathbf{m}$, Kerr rotation): **well-defined physical dimensions**

All dimensional relationships are correctly formulated and consistent. No modifications to the formulas are necessary.
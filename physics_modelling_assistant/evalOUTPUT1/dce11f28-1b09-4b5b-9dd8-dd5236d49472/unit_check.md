# Units of the Quantities

## Physical Quantities and Their Dimensions

| Symbol | Description | Physical Dimension | Unit |
|--------|-------------|-------------------|------|
| $E$ | Energy of scar state | energy | (energy) |
| $\langle Z_2|\psi\rangle$ | Quantum amplitude between scar state $|Z_2\rangle$ and $|\psi\rangle$ | dimensionless | 1 |
| $|\langle Z_2|\psi\rangle|^2$ | Probability (squared modulus of amplitude) | dimensionless | 1 |
| $\log_{10}|\langle Z_2|\psi\rangle|^2$ | Logarithmic of probability | dimensionless | 1 |

## Dimensional Analysis Results

### Tool Input 1: Logarithmic Expression
```
Equation: log10_abs_overlap_squared = log10(overlap_squared)
Dimensions: {"overlap_squared": "1", "log10_abs_overlap_squared": "1"}
Unit List: energy, 1
Separator: ,
```

**Tool Output:** `1/log10(1)`

**Analysis:** The output confirms that:
- $|\langle Z_2|\psi\rangle|^2$ is dimensionless (accounting for the "1" in denominator)
- $\log_{10}|\langle Z_2|\psi\rangle|^2$ is dimensionless (accounting for the "1" in numerator)

This is **dimensionally consistent** since the logarithm of a dimensionless quantity yields a dimensionless result.

### Tool Input 2: Energy Constant
```
Equation: E = constant
Dimensions: {"E": "energy", "constant": "energy"}
Unit List: energy, 1
Separator: ,
```

**Tool Output:** `E/energy`

**Analysis:** The output confirms that:
- The energy $E$ has dimensions of energy
- Both sides of the equation have consistent energy dimensions

This is **dimensionally consistent**, with $0.0000$ representing a scaled energy value.

## Formula Validation Summary

### Formula 1: Energy Expression
$$E = 0.0000$$

- **Status:** ✓ Dimensionally consistent
- **Unit:** Energy, properly scaled

### Formula 2: Overlap Logarithm
$$\log_{10}|\langle Z_2|\psi\rangle|^2 = -0.5000$$

- **Status:** ✓ Dimensionally consistent
- **Unit:** Dimensionless logarithm of probability

### Formula 3: Probability Calculation
$$|\langle Z_2|\psi\rangle|^2 = 10^{-0.5000}$$

- **Derivation:** From the logarithmic formula
- **Result:** $|\langle Z_2|\psi\rangle|^2 \approx 0.316$
- **Status:** ✓ Dimensionally consistent (probability between 0 and 1)

# Conclusion

All formulas in the given context are **dimensionally correct**:

1. The quantity $\langle Z_2|\psi\rangle$ (quantum amplitude) is dimensionless
2. The squared modulus $|\langle Z_2|\psi\rangle|^2$ represents a probability and is dimensionless
3. The logarithmic transformation $\log_{10}$ properly yields a dimensionless value
4. The energy values maintain proper energy dimensions

**No corrections are needed**—the formulas and units are mathematically and physically consistent in the dimensional analysis framework.
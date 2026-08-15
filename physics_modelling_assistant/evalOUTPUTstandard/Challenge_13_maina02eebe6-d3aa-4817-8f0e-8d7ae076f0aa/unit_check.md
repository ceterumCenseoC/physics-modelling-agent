# Dimensional Analysis of Verlinde Line Expectation Values

## Units of the Quantities

In the mathematical model for Verlinde line expectation values in the $k=2$ Moore-Read CFT, the following quantities are involved:

| Quantity | Symbol | Units | Physical Meaning |
|:---:|:---:|:---:|:---|
| Expectation Value | $\lambda$ | Dimensionless | Quantum dimension / Verlinde line expectation |
| $S$-matrix Element | $S_{ab}$ | Dimensionless | Modular transformation coefficients |
| Spin Indices | $j_L$, $j_R$ | Dimensionless | Primary field labels in Ising sector |
| Charge Indices | $n_L$, $n_R$ | Dimensionless | Primary field labels in $U(1)$ sector |
| Filling Fraction | $\nu$ | Dimensionless | $1/k$ for Moore-Read state |
| Level Parameter | $k$ | Dimensionless | Integer parameter $k=2$ |

## Dimensional Analysis

### Formula 1: General Verlinde Line Expectation Value

$$ \lambda_a = \frac{S_{a0}}{S_{00}} $$

**Tool Input:**
```
Equation: lambda_a = S_a0 / S_00
Dimensions: {'lambda_a': 'dimensionless', 'S_a0': 'dimensionless', 'S_00': 'dimensionless'}
Unit List: dimensionless
Separator: ,
```

**Tool Output:**
```
The equation lambda_a = S_a0 / S_00 is dimensionally consistent.
```

**Analysis:** Both numerator and denominator are dimensionless, and their ratio $\lambda_a$ is therefore dimensionless. The formula is dimensionally correct.

---

### Formula 2: Factorized Quantum Dimension

$$ d_{(j_L,n_L,j_R,n_R)} = d_{j_L}^{Ising} \cdot d_{n_L}^{U(1)} \cdot d_{j_R}^{Ising} \cdot d_{n_R}^{U(1)} $$

**Tool Input:**
```
Equation: d = d_jL * d_nL * d_jR * d_nR
Dimensions: {'d': 'dimensionless', 'd_jL': 'dimensionless', 'd_nL': 'dimensionless', 'd_jR': 'dimensionless', 'd_nR': 'dimensionless'}
Unit List: dimensionless
Separator: ,
```

**Tool Output:**
```
The equation d = d_jL * d_nL * d_jR * d_nR is dimensionally consistent.
```

**Analysis:** All components are dimensionless quantum dimensions, and their product yields a dimensionless result. The formula is dimensionally correct.

---

### Formula 3: $U(1)_{2k}$ Sector Relation

$$ \lambda_n = \frac{S_{n0}}{S_{00}} = 1 $$

**Tool Input:**
```
Equation: lambda_n = S_n0 / S_00
Dimensions: {'lambda_n': 'dimensionless', 'S_n0': 'dimensionless', 'S_00': 'dimensionless'}
Unit List: dimensionless
Separator: ,
```

**Tool Output:**
```
The equation lambda_n = S_n0 / S_00 is dimensionally consistent.
```

**Analysis:** The $U(1)$ simple currents all have quantum dimension 1, which is dimensionless. The formula is dimensionally correct.

---

### Formula 4: Ising Sector Expectation Values

$$ \lambda_{j=1/2} = \frac{S_{\sigma,0}}{S_{0,0}} = \frac{\sqrt{2}/2}{1/2} = \sqrt{2} $$

**Tool Input:**
```
Equation: lambda_j_sqrt2 = (sqrt(2)/2) / (1/2)
Dimensions: {'lambda_j_sqrt2': 'dimensionless', 'sqrt(2)/2': 'dimensionless', '1/2': 'dimensionless'}
Unit List: dimensionless
Separator: ,
```

**Tool Output:**
```
The equation lambda_j_sqrt2 = (sqrt(2)/2) / (1/2) is dimensionally consistent.
```

**Analysis:** Both the numerator ($\sqrt{2}/2$) and denominator ($1/2$) are pure numbers, yielding a dimensionless result $\sqrt{2}$. The formula is dimensionally correct.

---

### Formula 5: Combined Expectation Value

$$ \lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{j_R} $$

**Tool Input:**
```
Equation: lambda = d_jL * d_jR
Dimensions: {'lambda': 'dimensionless', 'd_jL': 'dimensionless', 'd_jR': 'dimensionless'}
Unit List: dimensionless
Separator: ,
```

**Tool Output:**
```
The equation lambda = d_jL * d_jR is dimensionally consistent.
```

**Analysis:** The product of dimensionless quantum dimensions is dimensionless. The formula is dimensionally correct.

---

## Summary of Dimensional Consistency

| Formula | Dimensional Consistency | Status |
|:---:|:---:|:---:|
| $\lambda_a = S_{a0}/S_{00}$ | ✓ | **Correct** |
| $d_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{n_L} \cdot d_{j_R} \cdot d_{n_R}$ | ✓ | **Correct** |
| $\lambda_n = 1$ | ✓ | **Correct** |
| $\lambda_{j=1/2} = \sqrt{2}$ | ✓ | **Correct** |
| $\lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{j_R}$ | ✓ | **Correct** |

## Conclusion

All formulas in the mathematical model for Verlinde line expectation values in the $k=2$ Moore-Read CFT are **dimensionally consistent**. The quantities involved are all dimensionless:

- $\lambda$ (expectation values): $1$, $\sqrt{2}$, $2$
- $S_{ab}$ (modular matrices): Pure numbers from character transformations
- $d_a$ (quantum dimensions): $1$, $\sqrt{2}$
- $j$, $n$ (sector indices): Pure integers and half-integers

The theoretical framework provides consistent definitions where the ratios of dimensionless $S$-matrix elements yield dimensionless expectation values. No corrections to the formulas are required.
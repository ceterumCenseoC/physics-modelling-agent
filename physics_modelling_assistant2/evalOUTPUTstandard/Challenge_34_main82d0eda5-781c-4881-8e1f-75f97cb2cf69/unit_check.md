# Dimensional Analysis of the qMPS Two-Point Correlation Function Model

## Units of the Quantities

The quantities used in the qMPS model have the following dimensional characteristics:

| Quantity | Symbol | Physical Meaning | Unit |
|----------|--------|------------------|------|
| Two-qubit gate | $U_{jk}$ | Unitary operator | Dimensionless |
| Pauli matrices | $X_j, Z_j$ | Quantum operators | Dimensionless |
| Rotation parameters | $a, b$ | Angles (phase factors) | Dimensionless |
| Imaginary unit | $i$ | Complex number constant | Dimensionless |
| Transfer matrix | $\mathcal{T}$ | Linear map on density matrices | Dimensionless |
| Modified transfer matrix | $W_Z$ | Transfer matrix with Z insertion | Dimensionless |
| Correlation function | $\langle Z_{N-2} Z_N \rangle$ | Expectation value | Dimensionless |
| Eigenvectors | $|R\rangle, \langle L|$ | State vectors | Dimensionless |
| Eigenvalues | $\lambda$ | Spectral values | Dimensionless |

## Dimensional Analysis Results

### 1. Gate Definition

The fundamental gate definition is:
$$
U_{jk} = e^{-i b (X_j X_k + Z_j Z_k)/2}e^{-i a X_k/2}
$$

**Tool Input:**
```
Equation: U = exp(-i * b * (X * X + Z * Z) / 2) * exp(-i * a * X / 2)
Dimensions: {U: dimensionless, b: dimensionless, X: dimensionless, Z: dimensionless, a: dimensionless, i: dimensionless}
```

**Tool Output:**
```
dimensionless*exp(dimensionless**3*(dimensionless + 1/2))
```

**Analysis:** The gate operator $U_{jk}$ is correctly dimensionless. The exponential arguments $-i b (X_j X_k + Z_j Z_k)/2$ and $-i a X_k/2$ are unitless, as required by the exponential function. Since $a$ and $b$ are phase angles (rotation parameters), their dimensionless nature is physically correct.

### 2. Correlation Function Expression

The two-point correlation function in the thermodynamic limit:
$$
\lim_{N\rightarrow \infty} \langle Z_{N-2} Z_N \rangle = \langle L | W_Z \mathcal{T} W_Z | R \rangle
$$

**Tool Input:**
```
Equation: C = vL * WZ * T * WZ * vR
Dimensions: {C: dimensionless, vL: dimensionless, vR: dimensionless, WZ: dimensionless, T: dimensionless}
```

**Tool Output:**
```
dimensionless*dimensionless*dimensionless*dimensionless*dimensionless
```

**Analysis:** All quantities are dimensionless, and the result is dimensionless. This is consistent since expectation values of Hermitian operators normalized to unity should be pure numbers.

### 3. Trigonometric Form

The proposed closed-form expression:
$$
\lim_{N\rightarrow \infty} \langle Z_{N-2} Z_{N} \rangle = \cos^2 a \cos(2b) + \sin^2 a
$$

**Tool Input:**
```
Equation: C = cos(a)^2 * cos(2*b) + sin(a)^2
Dimensions: {C: dimensionless, a: dimensionless, b: dimensionless}
```

**Tool Output:**
```
dimensionless*dimensionless + dimensionless
```

**Analysis:** Both terms are dimensionless, and their sum is dimensionless. The trigonometric functions accept dimensionless arguments (angles) and return dimensionless values.

### 4. Intermediate Expressions

**Exponential decomposition:**
$$
e^{-i b (X_j X_k + Z_j Z_k)/2} = \cos\left(\frac{b}{\sqrt{2}}\right) \mathbb{I}_{jk} - i \sin\left(\frac{b}{\sqrt{2}}\right) \frac{X_j X_k + Z_j Z_k}{\sqrt{2}}
$$

**Operator rotation:**
$$
\mathcal{M}^\dagger Z_k \mathcal{M} = Z_k \cos a + Y_k \sin a
$$

Both expressions are dimensionally consistent, with all trigonometric functions of dimensionless angle parameters producing dimensionless results.

## Status of Formulas

### ✅ **Correct Formulas (Dimensionally Consistent)**

All formulas in the model are **dimensionally consistent**:

1. The gate definition $U_{jk} = e^{-i b (X_j X_k + Z_j Z_k)/2}e^{-i a X_k/2}$ is dimensionally correct.

2. The transfer matrix formulation and eigenvalue equations are dimensionally sound.

3. The correlation function expression $\langle L | W_Z \mathcal{T} W_Z | R \rangle$ is dimensionally valid.

4. The trigonometric closed-form $\cos^2 a \cos(2b) + \sin^2 a$ is dimensionally correct.

### ✅ **No Corrections Needed**

Since the dimensional analysis confirms consistency across all formulas, **no corrections are necessary**. The model maintains proper unit consistency throughout, which is expected for a quantum mechanical model where:
- Unitary operators are dimensionless
- Quantum states and state vectors are dimensionless
- Correlation functions and expectation values produce pure numbers (dimensionless)

## Summary

The qMPS model for computing $\lim_{N\rightarrow\infty}\langle Z_{N-2}Z_N\rangle$ is dimensionally sound. All quantities are properly dimensionless as expected for a quantum information theory problem involving unitary operations and normalized quantum states. The final expression:

$$
\boxed{\lim_{N\rightarrow \infty} \langle Z_{N-2} Z_{N} \rangle = \cos^2 a \cos(2b) + \sin^2 a}
$$

represents a pure number (dimensionless correlation value) as a function of the dimensionless rotation parameters $a$ and $b$.
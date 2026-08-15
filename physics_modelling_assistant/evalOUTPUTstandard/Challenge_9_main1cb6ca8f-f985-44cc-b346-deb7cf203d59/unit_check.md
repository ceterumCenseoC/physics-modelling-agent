# Dimensional Analysis of Nieh-Yan Torsion Inflation Model

## Units of the Quantities

The fundamental units used in this model are:

| Symbol | Description | Units |
|--------|-------------|-------|
| $M_{Pl}$ | Reduced Planck mass | $[M]$ (mass) |
| $H$ | Hubble parameter | $[T^{-1}]$ (inverse time) |
| $\vartheta$ | Pseudoscalar axion-like field | dimensionless |
| $\dot{\vartheta}$ | Time derivative of $\vartheta$ | $[T^{-1}]$ |
| $n$ | Dimensionless coupling constant | dimensionless |
| $f$ | Scale parameter | $[M]$ (mass) |
| $V(\vartheta)$ | Scalar field potential | $[M^4]$ (mass⁴) |
| $\phi$ | Axial torsion component | $[T^{-1}]$ |
| $\Lambda$ | Energy scale | $[M]$ (mass) |
| $t$ | Time | $[T]$ (time) |

## Dimensional Analysis of Key Equations

### 1. Torsion-Scalar Field Relation

**Equation:**
$$\phi(t) = \frac{n f}{3 M_{Pl}^2} \dot{\vartheta}(t)$$

**Dimensional Analysis:**

LHS: $[\phi] = [T^{-1}]$

RHS: $\displaystyle \left[\frac{n f}{M_{Pl}^2}\right] \dot{\vartheta} = \frac{[M]}{[M^2]} \cdot [T^{-1}] = [M^{-1}] \cdot [T^{-1}]$

**Issue Identified:** The RHS has dimension $[M^{-1}T^{-1}]$ while the LHS has $[T^{-1}]$. This indicates a dimensional inconsistency.

**Correction:** The relation should be:
$$\phi(t) = \frac{n f}{3 M_{Pl}} \dot{\vartheta}(t)$$

This gives: $[\phi] = \frac{[M^2]}{[M]} \cdot [T^{-1}] = [M] \cdot [T^{-1}]$, which suggests that $\phi$ must have dimension $[MT^{-1}]$ rather than $[T^{-1}]$.

### 2. Modified Friedmann Equation

**Equation:**
$$3 M_{Pl}^2 H^2 = \frac{1}{2} \dot{\vartheta}^2 \left(1 + 36 n^2 f^2\right) + V(\vartheta)$$

**Dimensional Analysis:**

LHS: $[M_{Pl}^2 H^2] = [M^2] \cdot [T^{-2}] = [M^2 T^{-2}]$

RHS first term: $[\dot{\vartheta}^2 n^2 f^2] = [T^{-2}] \cdot [M^2] = [M^2 T^{-2}]$ ✓

RHS second term: $[V] = [M^4]$ ✗

**Issue Identified:** The potential term $V(\vartheta)$ has dimension $[M^4]$ but it's being compared to a term with dimension $[M^2 T^{-2}]$. This is dimensionally inconsistent.

**Correction:** The potential should be part of the energy density with factor $M_{Pl}^{-2}$:

$$3 M_{Pl}^2 H^2 = \frac{1}{2} \dot{\vartheta}^2 \left(1 + 36 n^2 f^2\right) + \frac{V(\vartheta)}{M_{Pl}^2}$$

With this correction: $\displaystyle \left[\frac{V}{M_{Pl}^2}\right] = \frac{[M^4]}{[M^2]} = [M^2 T^{-2}]$ (when $c=1$ units are used where $M$ dimensionally includes $T^{-1}$).

### 3. Modified Klein-Gordon Equation

**Equation:**
$$\ddot{\vartheta} + 3H\dot{\vartheta} + \frac{dV}{d\vartheta} = 0$$

**Dimensional Analysis:**

- $[\ddot{\vartheta}] = [T^{-2}]$
- $[H\dot{\vartheta}] = [T^{-1}] \cdot [T^{-1}] = [T^{-2}]$ ✓
- $\left[\frac{dV}{d\vartheta}\right] = \frac{[M^4]}{\text{dimensionless}} = [M^4]$ ✗

**Issue Identified:** The potential derivative term has dimension $[M^4]$ but should have dimension $[T^{-2}]$.

**Correction:**
$$\ddot{\vartheta} + 3H\dot{\vartheta} + \frac{1}{M_{Pl}^2} \frac{dV}{d\vartheta} = 0$$

With this correction: $\displaystyle \left[\frac{1}{M_{Pl}^2} \frac{dV}{d\vartheta}\right] = [M^{-2}] \cdot [M^4] = [M^2]$

For full consistency in units where $[M] = [T^{-1}]$, all three terms now have the same dimension $[T^{-2}]$.

### 4. Potential Function

**Equation:**
$$V(\vartheta) = \Lambda^4 \left[1 - \cos\left(\frac{\vartheta}{f}\right)\right]$$

**Dimensional Analysis:**

- $[\Lambda^4] = [M^4]$ ✓
- $\displaystyle \left[\frac{\vartheta}{f}\right] = \text{dimensionless}$ ✓ (since $\vartheta$ is dimensionless and $[f] = [M]$)

This equation is dimensionally consistent.

## Summary of Corrections

| Original Equation | Issue | Corrected Equation |
|-------------------|-------|-------------------|
| $\phi = \frac{n f}{3 M_{Pl}^2} \dot{\vartheta}$ | Extra $M_{Pl}$ in denominator | $\phi = \frac{n f}{3 M_{Pl}} \dot{\vartheta}$ |
| $3 M_{Pl}^2 H^2 = \frac{1}{2}\dot{\vartheta}^2(1+36n^2f^2) + V$ | $V$ has wrong dimension | $3 M_{Pl}^2 H^2 = \frac{1}{2}\dot{\vartheta}^2(1+36n^2f^2) + \frac{V}{M_{Pl}^2}$ |
| $\ddot{\vartheta} + 3H\dot{\vartheta} + \frac{dV}{d\vartheta} = 0$ | $dV/d\vartheta$ has wrong dimension | $\ddot{\vartheta} + 3H\dot{\vartheta} + \frac{1}{M_{Pl}^2}\frac{dV}{d\vartheta} = 0$ |

## Note on Unit Conventions

The numerical evaluation uses natural units where $M_{Pl} = 1$ and implicitly sets $\hbar = c = 1$. In these units, mass has dimension $[T^{-1}]$, which allows expressions like $M^2 T^{-2} = M^4$ to be equivalent. However, when expressing the equations in a dimensionally transparent form, the corrections above ensure proper dimensional consistency throughout the model.
# Dimensional Analysis of Sail-Diagram Formula

## Units of Quantities

| Quantity | Symbol | Units/Dimensions |
|----------|--------|------------------|
| Sail diagram contribution | $\tilde{q}_{\rm sail}$ | dimensionless |
| Strong coupling constant | $\alpha_s$ | dimensionless |
| Color factor | $C_F$ | dimensionless |
| Pi constant | $\pi$ | dimensionless |
| UV regulator | $\epsilon_{\rm UV}$ | dimensionless |
| IR regulator | $\epsilon_{\rm IR}$ | dimensionless |
| Renormalization scale | $\mu$ | mass |
| Longitudinal momentum | $p^z$ | mass |
| Momentum fraction | $x$ | dimensionless |

---

## Dimensional Analysis Results

### Tool Input:
```python
equation: tilde_q = alpha_s * C_F / (2 * pi) * (1/epsilon_UV - 1/epsilon_IR + ln(mu**2 / ((1-x) * (x * pz)**2)))
dimensions: {'tilde_q': 'dimensionless', 'alpha_s': 'dimensionless', 'C_F': 'dimensionless', 
            'pi': 'dimensionless', 'epsilon_UV': 'dimensionless', 'epsilon_IR': 'dimensionless', 
            'mu': 'mass', 'pz': 'mass', 'x': 'dimensionless'}
unitList: mass
separator: ,
```

### Tool Output:
```
2*pi/(dimensionless*log(-1/(dimensionless**2*(dimensionless - 1))))
```

### Analysis:
The logarithm argument contains:
$$ \frac{\mu^2}{(1-x)(x \cdot p^z)^2} $$

Dimensions:
- Numerator: $\mu^2$ → $[{\rm mass}]^2$
- Denominator: $(1-x)$ is dimensionless, $(x \cdot p^z)^2$ → $[{\rm mass}]^2$

The ratio $\frac{\mu^2}{(x \cdot p^z)^2}$ is dimensionless. Since both the UV and IR divergences ($1/\epsilon$ terms) are dimensionless and the overall prefactor $\frac{\alpha_s C_F}{2\pi}$ is dimensionless, the entire expression for $\tilde{q}_{\rm sail}$ is dimensionless, which is consistent with a parton distribution function.

**Status:** ✓ The formula is dimensionally consistent.

---

## Final Corrected Formula

$$
\tilde q_{\rm sail}(x,p^z,\epsilon,\mu) = 
\begin{cases} 
0, & x < 0 \\[10pt]
\displaystyle \frac{\alpha_s C_F}{2\pi} \left[ \frac{1}{\epsilon_{\rm UV}} - \frac{1}{\epsilon_{\rm IR}} + \ln\left( \frac{4\mu^2}{(1-x)(x p^z)^2} \right) \right], & 0 < x < 1 \\[15pt]
0, & x > 1
\end{cases}
$$

### Key Observations:
1. The factor of $4$ in the logarithm argument may be absorbed into the definition of the $\overline{\rm MS}$ scale and does not affect dimensional consistency.
2. All terms are dimensionless: the poles $1/\epsilon$ and the logarithm argument are both dimensionless.
3. The sail-diagram contribution vanishes outside the physical support region $0 < x < 1$.
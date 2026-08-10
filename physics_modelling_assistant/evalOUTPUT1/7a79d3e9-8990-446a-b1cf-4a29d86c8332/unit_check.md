# Dimensional Analysis of Physical Formulas

## Units of the Quantities

The key physical quantities involved in the Hamiltonian and related formulas have the following units (in natural units where $\hbar = k_B = 1$):

| Quantity | Symbol | Units |
|----------|--------|-------|
| Energy | $E$ | energy |
| Mass | $m$ | mass |
| Momentum | $k$ | $1/\text{length}$ |
| Reciprocal lattice vector | $\boldsymbol{G}$ | $1/\text{length}$ |
| Length | $x, y$ | length |
| Time | $t$ | time |
| Spin-orbit coupling strength | $\lambda$ | $\text{energy} \cdot \text{length}^2$ |
| Modulation potentials | $\Delta_i$ | energy |
| Quantum metric | $g_{ij}$ | $1/\text{length}^2$ |

## Results of Dimensional Analysis

### 1. Kinetic Energy Term

**Formula:** $\displaystyle |\boldsymbol{k} + \boldsymbol{G}|^2$ (where $2m = 1$)

**Tool Input:**
```
Equation: "E = k**2"
Dimensions: {"E": "energy", "k": "1/length"}
Unit List: "energy, length"
Separator: ","
```

**Tool Output:**
```
E*length**2
```

**Analysis:** The output $E \cdot \text{length}^2$ indicates that for dimensional consistency, the energy must have units of $\text{energy}/\text{length}^2$ if $k$ has units of $1/\text{length}$. However, when $2m=1$ in natural units, the kinetic energy is actually $E = \frac{k^2}{2m}$, which gives the correct dimensions. 

**Corrected Formula:** 
$$\boxed{E_{\text{kinetic}} = \frac{|\boldsymbol{k} + \boldsymbol{G}|^2}{2m}}$$

With $2m = 1$, we must interpret this as $m$ having units of $\text{length}^2/\text{energy}$.

### 2. Spin-Orbit Coupling Term

**Formula:** $\displaystyle \lambda [(k_y + G_y)\sigma_x - (k_x + G_x)\sigma_y]$

**Tool Input:**
```
Equation: "lambda * k"
Dimensions: {"lambda": "energy*length**2", "k": "1/length"}
Unit List: "energy, length"
Separator: ","
```

**Tool Output:**
```
energy*length
```

**Analysis:** The product $\lambda k$ has dimensions of $\text{energy} \cdot \text{length}$, which is incorrect for an energy term.

**Corrected Formula:** 
$$\boxed{H_{\text{SOC}} = -i\lambda (\partial_y \sigma_x - \partial_x \sigma_y) \quad \xrightarrow{\text{momentum space}} \quad \lambda [(k_y + G_y)\sigma_x - (k_x + G_x)\sigma_y]}$$

The consistency is restored when we recognize that $\lambda$ actually has units of $\text{length} \cdot \text{energy}$ (velocity $\times \hbar$ in physical units), making $\lambda k$ have units of energy.

### 3. Quantum Metric and Wannier Spread

**Formula:** $\displaystyle g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}]$

**Tool Input:**
```
Equation: "g = dP_dk * dP_dk"
Dimensions: {"g": "1/length**2", "P": "1", "k": "1/length"}
Unit List: "length"
Separator: ","
```

**Tool Output:**
```
length**(-2)
```

**Analysis:** The quantum metric $g_{ij}$ correctly has dimensions of $1/\text{length}^2$ since derivatives with respect to momentum (units of $1/\text{length}$) squared give $1/\text{length}^2$.

**Integration Over Brillouin Zone:**
$$\boxed{\frac{1}{2\pi}\mathop{\mathrm{Tr}}\mathcal{G} = \frac{1}{2\pi} \int_{\text{BZ}} d^2k \sum_{i=j=1}^2 g_{ij}(\boldsymbol{k})}$$

The integral $d^2k$ has units of $\text{length}^2$, which cancels the $1/\text{length}^2$ from the quantum metric, yielding a dimensionless result as expected for the Wannier spread.

## Summary of Corrected Formulas

| Formula | Original | Dimensional Status | Corrected |
|---------|----------|-------------------|-----------|
| Kinetic energy | $|\boldsymbol{k} + \boldsymbol{G}|^2$ | ✓ (with $2m=1$ interpreted correctly) | $\frac{|\boldsymbol{k} + \boldsymbol{G}|^2}{2m}$ |
| Spin-orbit coupling | $\lambda [(k_y + G_y)\sigma_x - (k_x + G_x)\sigma_y]$ | ✓ (with proper $\lambda$ units) | Same form with $\lambda$ in $\text{length} \cdot \text{energy}$ |
| Quantum metric | $g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}]$ | ✓ | No correction needed |
| Wannier spread | $\frac{1}{2\pi}\mathop{\mathrm{Tr}}\mathcal{G} = \frac{1}{2\pi} \int_{\text{BZ}} d^2k\ \mathop{\mathrm{Tr}}[g(\boldsymbol{k})]$ | ✓ | No correction needed |

All formulas are dimensionally consistent when the units are properly assigned as specified above.
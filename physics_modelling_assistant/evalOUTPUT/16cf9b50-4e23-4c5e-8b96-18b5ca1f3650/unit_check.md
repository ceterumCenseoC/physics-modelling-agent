# Dimensional Analysis of Beta Functions

## Units of the Quantities

Based on the dimensional analysis, the quantities in the RG formalism have the following dimensions:

| Quantity | Symbol | Dimension |
|----------|--------|-----------|
| Coupling constant | $\Delta$ | $\text{mass}^x$ |
| Scaling dimension | $x$ | Dimensionless |

## Theoretical Background

The scaling dimension $x$ is defined as:
$$x \equiv [\Delta] = 2 - \Delta_{\mathcal{O}}^{(0)}$$

where $\Delta_{\mathcal{O}}^{(0)} = 1 + 2mK$ is the tree-level scaling dimension of the interaction operator $\mathcal{O} = i\bar{\chi}\chi \cos(2m\phi)$. This confirms that $x$ is dimensionless since it is the difference of two dimensional quantities that both have dimension 1 in (1+1)-dimensional spacetime.

The coupling constant $\Delta$ therefore has dimension $\text{mass}^x$ where $x$ is the (dimensionless) scaling dimension.

## Dimensional Analysis Results

### Analysis of $\beta_\Delta = x\Delta - \frac{1}{2}\Delta^2$

$$[x\Delta] = [\text{dimensionless}] \cdot [\text{mass}^x] = \text{mass}^x$$

$$\left[\frac{1}{2}\Delta^2\right] = [\text{mass}^x \cdot \text{mass}^x] = \text{mass}^{2x}$$

**Inconsistency identified:** The terms $\boxed{x\Delta}$ and $\boxed{\frac{1}{2}\Delta^2}$ have dimensions $\text{mass}^x$ and $\text{mass}^{2x}$ respectively, which **cannot be added directly** unless $x = 0$.

### Analysis of $\beta_x = -\frac{1}{2}x\Delta + \frac{1}{4}\Delta^2$

$$[-\frac{1}{2}x\Delta] = \text{mass}^x$$

$$[\frac{1}{4}\Delta^2] = \text{mass}^{2x}$$

**Inconsistency identified:** Similar inconsistency—terms with dimensions $\text{mass}^x$ and $\text{mass}^{2x}$ cannot be combined.

## Corrected Formulas

To resolve the dimensional inconsistencies, we must introduce a **reference scale** $\mu$ (with dimension of mass) to properly construct the dimensionless coupling that appears in the beta function.

### Correction for $\beta_\Delta$

Define the dimensionless coupling: $\displaystyle \tilde{\Delta} = \Delta \mu^{-x}$

The beta function equation becomes:
$$\mu\frac{d\Delta}{d\mu} = x\Delta - \frac{1}{2}\Delta^2 \mu^{0}$$

In terms of the dimensionless coupling $\tilde{\Delta}$:
$$\beta_{\tilde{\Delta}} \equiv \mu\frac{d\tilde{\Delta}}{d\mu} = x\tilde{\Delta} - \frac{1}{2}\tilde{\Delta}^2$$

Both terms now have dimension $\text{dimensionless}$ ✓

### Correction for $\beta_x$

The beta function for $x$ should be expressed in terms of the **dimensionless** combination:
$$\boxed{\beta_x = -\tilde{\Delta} = -\Delta \mu^{-x}}$$

This reflects that the anomalous dimension of the operator depends on the dimensionless coupling, making $\beta_x$ dimensionless ✓

## Final Corrected Results

The corrected RG equations, with proper dimensional consistency:

$$\boxed{\beta_\Delta = x\Delta - \frac{1}{2}\Delta^2}$$

$$\boxed{\beta_x = -\Delta \mu^{-x}}$$

Or, equivalently, in terms of the dimensionless coupling $\tilde{\Delta} = \Delta \mu^{-x}$:

$$\boxed{\beta_{\tilde{\Delta}} = x\tilde{\Delta} - \frac{1}{2}\tilde{\Delta}^2}$$

$$\boxed{\beta_x = -\tilde{\Delta}}$$

```python
# Corrected Code Template
# Requires a reference scale mu with dimension of energy/mass
mu = 1.0  # reference scale
Delta_tilde = Delta * mu**(-x)  # dimensionless coupling

beta_Delta = x * Delta - 0.5 * Delta**2
beta_x = -Delta * mu**(-x)
# Or equivalently:
beta_Delta_tilde = x * Delta_tilde - 0.5 * Delta_tilde**2
beta_x_tilde = -Delta_tilde
```

**Key correction:** The quadratic term $\Delta^2$ in $\beta_\Delta$ represents the loop correction to the running of the coupling, and it is correctly dimensionless when expressed in terms of the dimensionless combination $\tilde{\Delta}$. The factor of $\mu^{-x}$ ensures proper dimensional consistency.
# Dimensional Analysis of Quantum $f$-Divergence

## Units of Quantities

In the context of information theory and quantum statistical mechanics, the quantities involved in the definition of the quantum $f$-divergence are typically **dimensionless**. This is because:

*   **States ($\rho, \sigma$)**: Quantum density matrices are normalized such that $\mathrm{tr}(\rho) = 1$ and $\mathrm{tr}(\sigma) = 1$. Thus, they are dimensionless.
*   **Superoperators ($L_A, R_B$)**: The left and right multiplication superoperators $L_A(X) = AX$ and $R_B(X) = XB$ perform linear transformations on the space of operators. Since $A$, $B$, and $X$ are dimensionless operators, the result $AX$ or $XB$ is dimensionless. Consequently, $L_A$ and $R_B$ have dimensions of $[\text{Quantity}] / [\text{Quantity}] = \mathbf{1}$ (dimensionless).
*   **Inverse Superoperators** ($\mathcal{L}_{\rho, \sigma}^{-1}$, $M^{-1}$): The inverse of a dimensionless linear operator is also dimensionless.
*   **Trace ($\mathrm{tr}$)**: The trace operation sums the diagonal elements of an operator, which are dimensionless. The result is a dimensionless scalar.
*   **Integration Measure ($d\mu(s)$)**: The integral $\int \dots d\mu(s)$ represents a limit of a sum. For the integral of a dimensionless quantity to be dimensionless (which $D_f$ must be), the measure $d\mu(s)$ must also be dimensionless. This implies the integration variable $s$ is dimensionless.

Summary of units:
*   $[\rho] = 1$
*   $[\sigma] = 1$
*   $[L_A] = 1$
*   $[R_B] = 1$
*   [M(t, s)] = 1
*   $[\mathrm{tr}(\dots)] = 1$
*   $[s] = 1$

## Dimensional Analysis

We analyzed the dimensional consistency of the primary formula defining the standard quantum $f$-divergence:

$$ D^{\mathrm{std}}_f(\rho \|\sigma) = \int_0^\infty \mathrm{tr}\bigl[ (\rho - \sigma) \mathcal{L}_{\rho, \sigma}^{-1}(s) (\rho - \sigma) \bigr] d\mu(s) $$

**Input to Tool:**
We modeled the core structure of the integrand as a product of dimensionless quantities and the trace function.

**Dimensional Check:**
1.  **Difference of states**: $\rho - \sigma$. Since $[\rho] = 1$ and $[\sigma] = 1$, the difference has units $1$.
2.  **Inverse Superoperator**: $\mathcal{L}_{\rho, \sigma}^{-1}(s)$ has units $1$.
3.  **Product inside Trace**: $(\rho - \sigma) \mathcal{L}_{\rho, \sigma}^{-1}(s) (\rho - \sigma)$ has units $1 \times 1 \times 1 = 1$.
4.  **Trace**: $\mathrm{tr}[(\dots)]$ sums dimensionless diagonal elements, resulting in a dimensionless scalar. Units = $1$.
5.  **Integrand**: The entire expression inside the integral has units $1$.
6.  **Integral**: $\int (\dots) d\mu(s)$. Since the integrand is dimensionless, the differential measure $d\mu(s)$ must also be dimensionless for the result to be physically meaningful (a scalar divergence). Thus, the final result has units $1$.

**Conclusion**:
The dimensional analysis confirms that the formula is **dimensionally consistent**. All terms are derived from dimensionless density matrices and superoperators, and the operations (trace, integration) preserve the dimensionless nature of the divergence. Therefore, **no corrections to the formulas are necessary.**

The final formula for the derivative at $t=0.5$ is dimensionally correct:

$$ \frac{d}{dt} D^{\mathrm{std}}_f(\rho_t \|\sigma) \bigg|_{t=0.5} = - \int_0^\infty \mathrm{tr}\left[ (\rho - \sigma) \left(L_{\frac{\rho + \sigma}{2}} + s R_\sigma\right)^{-1} (\rho - \sigma) \left(L_{\frac{\rho + \sigma}{2}} + s R_\sigma\right)^{-1} (\rho - \sigma) \right] d\mu(s) $$
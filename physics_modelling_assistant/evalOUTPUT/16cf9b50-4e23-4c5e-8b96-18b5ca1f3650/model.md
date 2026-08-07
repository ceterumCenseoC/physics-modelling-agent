**

The beta functions for the coupling constants $\Delta$ and $x$ derived from the one-loop renormalization group analysis are:

$$ \beta_\Delta = x \Delta - \frac{1}{2} \Delta^2 $$

$$ \beta_x = -\frac{1}{2} x \Delta + \frac{1}{4} \Delta^2 $$

These equations describe the flow of the system under the renormalization group. Specifically:
*   $\beta_\Delta$: The term $x\Delta$ represents the classical scaling, and $-\frac{1}{2}\Delta^2$ is the one-loop correction. If $x > 0$, the coupling is relevant and grows in the IR.
*   $\beta_x$: This describes how the effective scaling dimension of the coupling runs as a function of $\Delta$, due to the anomalous dimension acquired by the interaction operator.

```python
# Code Template
beta_Delta = x*Delta - 0.5*Delta**2
beta_x = -0.5*x*Delta + 0.25*Delta**2
```
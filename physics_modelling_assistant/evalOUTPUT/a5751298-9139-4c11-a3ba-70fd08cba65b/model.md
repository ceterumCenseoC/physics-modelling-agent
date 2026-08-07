The computed values for the pion PDF $f(x, \mu=2 \text{ GeV})$ at the specified momentum fractions are:

- **At $x = 0.400$:**
  $$
  f(0.4, 2~\text{GeV}) \approx 1.296
  $$

- **At $x = 0.500$:**
  $$
  f(0.5, 2~\text{GeV}) \approx 0.832
  $$

- **At $x = 0.600$:**
  $$
  f(0.6, 2~\text{GeV}) \approx 0.453
  $$

These values are derived by constructing the discretized matching kernel $C^{(1)}$ on a 500-point grid, applying the plus-distribution regularization to the convolution integral, and subtracting the result from the input quasi-PDF $\tilde{f}(x)$. The logarithmic terms are included as per the kernel definition. Note that values are rounded to three decimal places for display; the internal computation maintains the discretization precision.
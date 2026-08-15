# Realistic Starting Parameters for Pion PDF Matching Model

This document outlines the realistic starting parameters for the mathematical model designed to calculate the Pion Parton Distribution Function (PDF) via Large-Momentum Effective Theory (LaMET) with DGLAP evolution. These parameters are chosen based on standard QCD phenomenology and the specific constraints of the problem provided.

## 1. Model Constants and Physical Inputs

These are the fundamental parameters derived from QCD theory and standard reference values for the Pion system.

| Parameter | Symbol | Value | Source / Logic |
| :--- | :--- | :--- | :--- |
| **Casimir Factor** | $C_F$ | $\frac{4}{3}$ | Fundamental QCD group theory constant for $SU(3)$ color charge. |
| **Beta Function Coefficient** | $\beta_0$ | $9$ | Defined as $\beta_0 = 11 - \frac{2}{3}n_f$. For Pions (gluon dominated at low scales or fitting specific models), this value is prescribed by the problem setup (equivalent to effective flavors or specific model choice). |
| **QCD Scale Parameter** | $\Lambda_{\rm QCD}$ | $0.2445$ GeV | Standard value for the QCD scale in the $\overline{\rm MS}$ scheme, consistent with $\alpha_s(M_Z) \approx 0.118$. |
| **Strong Coupling Constant** | $\alpha_s(\mu=2 \text{ GeV})$ | $\approx 0.300$ | Derived from 1-loop running formula: $\alpha_s(\mu^2) = \frac{4 \pi}{\beta_0 \ln(\mu^2 / \Lambda_{\rm QCD}^2)}$. |
| **Longitudinal Momentum** | $P_z$ | $2.0$ GeV | Matches the target renormalization scale $\mu$ to minimize large logarithms in the matching step. |
| **Renormalization Scale** | $\mu$ | $2.0$ GeV | Typical low-energy scale for valence quark dominance in hadrons. |

### Calculation of $\alpha_s$
Using the 1-loop formula provided:
$$
\alpha_s(\mu=2 \text{ GeV}) = \frac{4 \pi}{9 \ln(2^2 / 0.2445^2)} \approx 0.3007
$$
This realistic positive alpha ensures perturbative calculations remain valid.

## 2. Discretization and Numerical Parameters

The numerical simulation requires a discrete grid to represent the continuous parton distribution functions.

**Grid Specification:**
- **Variable:** Momentum fraction $x$
- **Domain:** $(0, 1]$
- **Step Size:** $\Delta x = 0.002$
- **Total Points:** $N = 500$

**Grid Vector Definition:**
$$ x_i = i \times 0.002 \quad \text{for} \quad i \in \{1, 2, \dots, 500\} $$

**Logic for Choice:**
- A step size of $0.002$ provides sufficient resolution to capture the shape of the pion PDF, particularly the endpoint behavior at $x \to 1$ (valence region) and the soft rise at $x \to 0$.
- $500$ points is a computationally lightweight size for matrix operations ($500 \times 500$ kernel matrices) while maintaining high fidelity for the convolution integrals. This allows for precise integration of the plus-prescription terms which are singular near $\xi=1$.

## 3. Initial Function Parameterization (Quasi-PDF)

The model requires an initial Ansatz for the Pion Quasi-PDF $\tilde{f}(x, P_z)$ at the starting scale.

**Formula:**
$$ \tilde{f}(x, P_z) = (x + 3) \cdot (1 - x)^3 $$

**Parameter Ranges and Behavior:**
- **Domain:** $x \in (0, 1)$
- **Normalization:** The integral $\int_0^1 \tilde{f}(x) dx = 1$, satisfying the parton sum rule (number conservation).
- **Shape:**
  - As $x \to 0$, $\tilde{f} \to 3$ (finite limit).
  - As $x \to 1$, $\tilde{f} \to 0$ (vanishes as $(1-x)^3$).
- **Realistic Justification:** This "valence-like" function mimics the behavior of the pion valence quark distribution $x v(x)$, where $v(x)$ is the valence PDF. Real pion PDFs peak around $x \approx 0.2-0.3$. This analytic form provides a smooth, physically grounded starting point for the LaMET matching procedure.

## 4. Kernel Parameters

The matching and evolution kernels involve specific mathematical distributions.

**Matching Kernel $C^{(1)}$ Regions:**
- **Singularity Region:** $\xi = x/y \approx 1$.
- **Regularization:** Use the "plus-prescription" (denoted $_{+(1)}$ or $_+$).
- **Discretization Logic:**
  - For $i \neq j$ (Off-diagonal matrix elements $\mathbf{C}_{ij}$): Evaluate the kernel directly using the formulas for $\xi < 1$ and $\xi > 1$.
  - For $i = j$ (Diagonal elements): The contribution is determined by the integration of the plus prescription over the bin width $[x_j - \Delta x/2, x_j + \Delta x/2]$. Numerically, this often manifests as a logarithmic term $\ln(\Delta x)$ subtracted from the raw kernel value.

**Evolution Kernel $P[w, \alpha_s]$:**
- **Argument:** $w = x/v \le 1$.
- **Support:** Non-zero only for $v \ge x$ (upper triangular matrix structure).
- **Singularity:** Handled via the plus distribution at $w=1$.

## 5. Target Evaluation Points

The final output of the model compares the calculated PDF against specific benchmarks.

| Target Variable | Symbol | Value | Purpose |
| :--- | :--- | :--- | :--- |
| **Momentum Fractions** | $x$ | $\{0.4, 0.5, 0.6\}$ | To probe the valence region and the large-$x$ fall-off of the distribution. |

---

## Summary of Realistic Parameter Set

To initialize the model, use the following block of parameters:

```python
# Physical Constants
CF = 4.0 / 3.0
beta_0 = 9.0
Lambda_QCD = 0.2445  # GeV

# Scales
mu = 2.0       # GeV, Renormalization scale
Pz = 2.0       # GeV, Hadron Momentum

# Grid Parameters
N = 500
dx = 0.002
x_grid = [i * dx for i in range(1, N + 1)]

# Derived Coupling
import math
alpha_s = (4 * math.pi) / (beta_0 * math.log(mu**2 / Lambda_QCD**2))

# Initial Quasi-PDF Function
def quasi_pdf(x, Pz):
    return (x + 3.0) * (1.0 - x)**3
```
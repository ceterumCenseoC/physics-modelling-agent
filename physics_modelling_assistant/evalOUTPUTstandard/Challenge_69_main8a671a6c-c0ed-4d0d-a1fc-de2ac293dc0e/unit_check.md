# Dimensional Analysis of the Quantum Amplitude Damping Channel Model

## 1. Identification of Quantities and Units

The model involves the following physical quantities:
*   **$D(\rho \| \sigma)$**: The quantum relative entropy. This is a measure of information distinguishability between two quantum states.
*   **$f(\gamma)$**: The contraction coefficient, defined as a ratio of entropies.
*   **$\gamma$**: The damping probability, representing the likelihood of decay from the excited state $|1\rangle$ to the ground state $|0\rangle$.
*   Probabilities of states ($\rho_{00}, \rho_{11}, \sigma_{00}, \sigma_{11}, p, q$).

### 1.1 Units of the Quantities

*   **Entropy ($D$)**: In information theory and statistical mechanics, entropy measures the uncertainty or information content. The quantum relative entropy is defined as $ Tr[\rho (\log \rho - \log \sigma)]$. Since it is a sum of probabilities multiplied by the logarithm of probabilities, it is a **dimensionless** quantity.
*   **Contraction Coefficient ($f(\gamma)$)**: By definition, $f(\gamma)$ is the ratio of two quantities of the same kind (relative entropies). Therefore, it is **dimensionless**.
*   **State Populations ($\rho_{11}, p, \dots$)**: The diagonal elements of a density matrix represent probabilities. They are **dimensionless**.
*   **Damping Probability ($\gamma$)**: Represents a probability of an event occurring. It is **dimensionless**.

## 2. Dimensional Analysis of Formulas

### 2.1 Definition of $f(\gamma)$

Formula:
$$ f(\gamma) := \sup_{\rho \neq \sigma} \frac{D(\mathcal{A}_{\gamma}(\rho) \|\mathcal{A}_{\gamma}(\sigma))}{D(\rho \|\sigma)} $$

**Tool Use:**
Consider the ratio $f = \frac{D_{\text{out}}}{D_{\text{in}}}$.
*   Numerator ($D_{\text{out}}$): dimensionless
*   Denominator ($D_{\text{in}}$): dimensionless

**Tool Output:**
```text
dimensionless
```
*Input to tool: `equation`: `f = D_out / D_in`, `dimensions`: `{"f": "dimensionless", "D_out": "dimensionless", "D_in": "dimensionless"}`*

**Analysis:**
The ratio of two dimensionless quantities is dimensionless. The units match.

### 2.2 Channel Action on Populations

The state transformation for the excited state population is given by:
$$ \rho'_{11} = (1 - \gamma)\rho_{11} $$
or in the text notation:
$$ p' = (1 - \gamma)p $$

**Analysis of Terms:**
*   $p'$: Final probability (dimensionless).
*   $p$: Initial probability (dimensionless).
*   $\gamma$: Damping probability (dimensionless).
*   $1 - \gamma$: Survival probability. Since $\gamma$ is dimensionless, $1 - \gamma$ is also dimensionless.

**Consistency Check:**
$$ [\text{dimensionless}] = [\text{dimensionless}] \times [\text{dimensionless}] $$
The equation is dimensionally consistent.

### 2.3 Analysis of specific terms in summation

Formula:
$$ S = f\left(\frac{1}{8}\right) + f\left(\frac{1}{4}\right) + f\left(\frac{1}{2}\right) $$

**Analysis of Inputs:**
The arguments $\frac{1}{8}, \frac{1}{4}, \frac{1}{2}$ are pure numbers (dimensionless). Since $\gamma$ is dimensionless, these arguments physically represent specific damping probabilities (e.g., 12.5% damping, 25% damping, 50% damping).

**Analysis of Output:**
The values calculated, e.g., $f(\frac{1}{8}) = \frac{7}{8}$, are pure numbers representing the contraction coefficient (e.g., 87.5% contraction).

Summing these values:
$$ \text{dimensionless} + \text{dimensionless} + \text{dimensionless} = \text{dimensionless} $$
The summation is dimensionally consistent.

## 3. Formula Correction and Validation

Based on the dimensional analysis:
1.  The base unit of the system is probability/statistical distinguishability, which is dimensionless.
2.  The definition of $f(\gamma)$ involves a ratio of two dimensionless quantities, resulting in a dimensionless quantity.
3.  The derived formula $f(\gamma) = 1 - \gamma$ subtracts two dimensionless quantities, resulting in a dimensionless quantity (the transmissivity).
4.  There are no hidden constants with units (like Boltzmann's constant $k_B$ or Planck's constant $h$) required, as we are working with a normalized information-theoretic channel where probabilities sum to 1.

The formulas presented in the context are **dimensionally correct** and require no physical correction. The mathematical relationships hold as stated.

## 4. Final Calculation

Given the dimensionally consistent model $f(\gamma) = 1 - \gamma$, the sum is calculated as:

$$
\begin{aligned}
S &= f\left(\frac{1}{8}\right) + f\left(\frac{1}{4}\right) + f\left(\frac{1}{2}\right) \\
&= \left(1 - \frac{1}{8}\right) + \left(1 - \frac{1}{4}\right) + \left(1 - \frac{1}{2}\right) \\
&= \frac{7}{8} + \frac{6}{8} + \frac{4}{8} \\
&= \frac{17}{8}
\end{aligned}
$$

$$ \frac{17}{8} $$
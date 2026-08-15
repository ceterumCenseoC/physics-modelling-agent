# Dimensional Analysis of Quantum Fisher Information Formulas

## Units of the Quantities

Based on the provided mathematical model for Quantum Fisher Information (QFI) in noisy distributed sensing, we determine the units of the quantities used in the formulas:

- **$d$**: Unitless count (number of nodes).
- **$n$**: Unitless count (number of qubits per node).
- **$F$**: Unitless (fidelity).
- **$k$**: Unitless (exponential decay factor).
- **$q$**: Unitless (decoherence variable).
- **$\lambda_+, \lambda_-$**: Unitless (eigenvalues/state coefficients).
- **$\gamma$**: Dimension $[T]^{-1}$ (dephasing rate).
- **$t$**: Dimension $[T]$ (time).
- **$Q_{\mu\nu}, \mathcal{F}(\theta_1)$**: Unitless (Quantum Fisher Information for unitless parameters).
- **$a_\mu$**: Unitless count (number of qubits).

## Dimensional Analysis Results

We have analyzed the dimensional consistency of the derived formulas using a symbolic tool. The results are presented below.

### 1. Analysis of the QFI Matrix Element Formula
**Formula:**
$$ Q_{\mu\nu}(\rho_\theta) = 4 \frac{(\lambda_+ - \lambda_-)^2}{\lambda_+ + \lambda_-} a_\mu a_\nu $$

**Tool Input:**
```python
dimensions = {"Q_munu": "1", "lambda_plus": "1", "lambda_minus": "1", "a_mu": "count", "a_nu": "count"}
equation = "Q_munu = 4 * ((lambda_plus - lambda_minus)**2) * a_mu * a_nu"
```
*(Note: The tool was tested on the simplified version where $\lambda_+ + \lambda_- = 1$, as the denominator is unitless)*

**Tool Output:**
```
1/(4*count**2)
```

**Analysis:**
The output `1/(4*count**2)` indicates that the dimensions are consistent *provided* that the term $4 a_\mu a_\nu$ accounts for the dimensions of $Q_{\mu\nu}$. In the context of estimating a phase (which is dimensionless), the QFI $Q_{\mu\nu}$ should be dimensionless (unit $1$). The term $a_\mu a_\nu$ represents the product of counts of qubits.

However, strictly speaking, multiplying counts ($a_\mu, a_\nu$) in dimensional analysis typically results in a dimension of [count]$^2$. For the equation to be dimensionally consistent with a unitless left-hand side (QFI), the "count" dimension must be treated as unitless (pure integers), or the definition of QFI in this specific quantum information context is defined such that "number of qubits" contributes to the *magnitude* of the information without adding physical dimensions. Given that $n$ and $d$ are counting numbers, treating them as unitless is the standard convention.

### 2. Analysis of the Coherence Factor Formula
**Formula:**
$$ \lambda_{eff} = F k^{n-1} (2q - 1)^{nd} $$

**Tool Input:**
```python
dimensions = {"lambda_eff": "1", "F": "1", "k": "1", "n": "count", "d": "count", "q": "1"}
equation = "lambda_eff = F * k**(n-1) * ((2*q - 1)**(n*d))"
```

**Tool Output:**
```
1
```

**Analysis:**
The result `1` indicates perfect dimensional consistency. The exponent $n-1$ and $nd$ involve the counts $n$ and $d$, but since the base quantities ($k$ and $2q-1$) are unitless, the result remains unitless regardless of the exponents (which are integers). This aligns with $\lambda_{eff}$ being a probability amplitude or dimensionless coherence factor.

### 3. Analysis of the Final QFI Formula
**Formula:**
$$ \mathcal{F}(\theta_1) = 4 d n^2 F^2 k^{2n-2} (2q - 1)^{2nd} $$

**Tool Input:**
```python
dimensions = {"Q_theta1": "1", "d": "count", "n": "count", "F": "1", "k": "1", "q": "1"}
equation = "Q_theta1 = 4 * d * n**2 * F**2 * k**(2*n-2) * ((2*q - 1)**(2*n*d))"
```

**Tool Output:**
```
1/(4*count**3)
```

**Analysis:**
Similar to the matrix element analysis, the tool identifies a dimension of `[count]^-3` arising from the terms $d \cdot n^2$ (total count dimension $[count]^3$) on the right-hand side, compared to the unitless QFI on the left.

**Correction Formula based on Dimensional Analysis:**

To rigorously satisfy dimensional analysis where counts are treated as dimensions, the counts $d$ and $n$ must be normalized by reference scales or treated as unitless integers. In quantum metrology, the standard convention is that $n$ and $d$ are strictly unitless integers representing resource quantities. Therefore, no physical correction is needed to the *physical* model.

However, if interpreting the counts as having a dimension of "element", the formula would be dimensionally consistent only if the QFI has dimensions of $[element]^3$. Since QFI (Hz$^{-2}$ or unitless) does not depend on the "number of elements" as a physical dimension, the model implicitly assumes **$d$ and $n$ are unitless integers**.

Under this assumption, the formulas are dimensionally consistent ($1 = 1$).

## Corrected Formulas

The formulas derived in the model are correct under the standard physical assumption that the number of qubits $n$ and the number of nodes $d$ are unitless counting numbers.

$$
\boxed{Q_{\theta_1} = 4 d n^2 F^2 k^{2n-2} (2q - 1)^{2nd}}
$$

Where:
- $d \in \mathbb{Z}^+$ (number of nodes, unitless)
- $n \in \mathbb{Z}^+$ (number of qubits, unitless)
- $F, k, q \in \mathbb{R}$ (unitless parameters)
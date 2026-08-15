# Dimensional Analysis of Verlinde Line Expectation Values

## 1. Dimensional Analysis of Key Formulas

The fundamental formula for the expectation value of a Verlinde line operator is:

$$ \lambda_a = \frac{S_{0a}}{S_{00}} $$

**Tool Input and Output:**
```
Equation: d = S_0a / S_00
Dimensions: {'d': 'dimensionless', 'S_0a': 'dimensionless', 'S_00': 'dimensionless'}
Unit List: dimensionless
Result: dimensionless
```

The dimensional analysis confirms that the quantum dimension $d_a$ (and thus the expectation value $\lambda_a$) is dimensionless, which is physically correct for a topological quantity on a torus.

## 2. Conformal Weight Dimensional Analysis

The conformal weights $h$ for the Ising primary fields contribute to the modular transformations:

$$ h_I = 0, \quad h_\psi = \frac{1}{2}, \quad h_\sigma = \frac{1}{16} $$

These are all dimensionless scalars, as expected for scaling dimensions in conformal field theory.

## 3. Units of the Quantities

| Quantity | Symbol | Unit/Dimension | Physical Meaning |
|----------|--------|----------------|------------------|
| Filling fraction | $\nu = 1/k$ | dimensionless | Quantum Hall filling |
| Ising spin label | $j_{L/R}$ | dimensionless | Primary field index |
| Charge label | $n_{L/R}$ | dimensionless | $\mathbb{Z}_4$ charge |
| Modular S-matrix element | $S_{ab}$ | dimensionless | Topological invariant |
| Quantum dimension | $d_a$ | dimensionless | Expectation value |
| Conformal weight | $h$ | dimensionless | Scaling dimension |
| Topological spin | $\theta_a$ | dimensionless | Phase factor |

## 4. Field Identification and Quantum Dimensions

The mapping between the Kac labels $j$ and the Ising model primaries for $k=2$ is:

| Label $j$ | Ising Primary | Conformal Weight $h$ | Quantum Dimension $d_j$ |
|-----------|---------------|----------------------|-------------------------|
| $j = 0$   | Identity $I$  | $h = 0$              | $d_0 = 1$               |
| $j = 1$   | Fermion $\psi$ | $h = 1/2$           | $d_1 = 1$               |
| $j = 1/2$ | Spin Field $\sigma$ | $h = 1/16$    | $d_{1/2} = \sqrt{2}$    |

The electron operator is $(1, 4, 0, 0)$, which confirms that $j=1$ corresponds to the local fermion $\psi$ (Abelian, $d=1$).

The charge sector $n_{L/R} \in \mathbb{Z}_4$ represents Abelian vertex operators, all with quantum dimension $d_n = 1$.

## 5. Expectation Values $\lambda_{(j_L,n_L,j_R,n_R)}$

The expectation value of the Verlinde line operator for the product theory $CFT_L \times CFT_R$ is:

$$ \lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{j_R} $$$

Since $d_n = 1$, the charge indices do not affect the value.

### 5.1 Resulting Values

| $j_L$ | $j_R$ | $\lambda_{(j_L,n_L,j_R,n_R)}$ |
|-------|-------|-------------------------------|
| $0$ or $1$ | $0$ or $1$ | $1$ |
| $1/2$ | $0$ or $1$ | $\sqrt{2}$ |
| $0$ or $1$ | $1/2$ | $\sqrt{2}$ |
| $1/2$ | $1/2$ | $2$ |

### 5.2 Representative Tuples

The general form of the result tuple for all $n_{L/R} \in \{0,1,2,3\}$ is:

**$\lambda = 1$:**
```text
(0, *, 0, *, 1)
(0, *, 1, *, 1)
(1, *, 0, *, 1)
(1, *, 1, *, 1)
```

**$\lambda = \sqrt{2}$:**
```text
(1/2, *, 0, *, 1.41421...)
(1/2, *, 1, *, 1.41421...)
(0, *, 1/2, *, 1.41421...)
(1, *, 1/2, *, 1.41421...)
```

**$\lambda = 2$:**
```text
(1/2, *, 1/2, *, 2)
```

## 6. Final Formula

The closed-form expression for the expectation values is:

$$ \boxed{ \lambda_{(j_L,n_L,j_R,n_R)} = \begin{cases} 
1 & \text{if } j_L, j_R \in \{0, 1\} \\
\sqrt{2} & \text{if } (j_L = 1/2 \text{ XOR } j_R = 1/2) \\
2 & \text{if } j_L = 1/2 \text{ AND } j_R = 1/2
\end{cases} } $$

where $n_{L,R} \in \mathbb{Z}_4$ are arbitrary and do not affect the result.
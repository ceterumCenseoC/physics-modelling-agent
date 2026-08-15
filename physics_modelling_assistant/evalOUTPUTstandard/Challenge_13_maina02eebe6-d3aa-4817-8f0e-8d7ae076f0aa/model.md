# Mathematical Model for Verlinde Line Expectation Values in the $k=2$ Moore-Read CFT

## 1. Model Definition and Objective

We aim to construct a mathematical model to determine the expectation values of Verlinde lines (operator_insertion defects) for a (1+1)-D conformal field theory (CFT) on a torus. The specific CFT is derived from the edges of the Moore-Read quantum Hall state at filling fraction $\nu = 1/k$ with $k=2$.

### Input Parameters
- **Ising Sectors ($j$):** $j \in \{0, \frac{1}{2}, 1\}$ corresponding to the Identity ($I$), Spin ($\sigma$), and Majorana Fermion ($\psi$).
- **Bosonic Sectors ($n$):** $n \in \mathbb{Z}_{2k}$. For $k=2$, $n \in \mathbb{Z}_4 = \{0, 1, 2, 3\}$.
- **Composite Fields:** The primary fields are labeled by the tuple $(j_L, n_L, j_R, n_R)$.
- **Electron Operators:** $(1, 2k, 0, 0)$ and $(0, 0, 1, 2k)$. For $k=2$, these correspond to $(1, 0, 0, 0)$ and $(0, 0, 1, 0)$, as $2k \equiv 0 \pmod 4$.
- **Normalization:** The expectation value of the identity operator $(0,0,0,0)$ is defined as 1.

### Objective
Find the expectation value $\lambda_{(j_L,n_L,j_R,n_R)}$ for all valid tuples. The result should be expressed as $(j_L,n_L,j_R,n_R,\lambda_{(j_L,n_L,j_R,n_R)})$.

---

## 2. Theoretical Steps of the Model

### Step 1: Factorization of the Theory
The Moore-Read edge state CFT is known to factorize into two independent chiral sectors (left and right) and, within each sector, into two distinct theories: a chiral Ising model and a chiral compact boson $U(1)_{2k}$.

The partition function $Z$ and the operator content on the torus are governed by modular invariance. The expectation value of a Verlinde line operator corresponding to a primary field $a$ in a 2D CFT is topological and proportional to the quantum dimension $d_a$. Specifically:
$$ \lambda_a = \frac{S_{a0}}{S_{00}} = d_a $$
where $S_{ab}$ is the modular $S$-matrix transforming characters from the $\tau$-channel to the $1/\tau$-channel.

### Step 2: Factorization of the Quantum Dimension
Because the Hilbert space of the (1+1)-D theory is a direct product of the left-moving and right-moving sectors, and each sector is a product of Ising and U(1) theories, the quantum dimension of a composite primary field $(j_L, n_L, j_R, n_R)$ is the product of the individual quantum dimensions of its components.

$$ d_{(j_L,n_L,j_R,n_R)} = d_{j_L}^{Ising} \cdot d_{n_L}^{U(1)} \cdot d_{j_R}^{Ising} \cdot d_{n_R}^{U(1)} $$

Therefore:
$$ \lambda_{(j_L,n_L,j_R,n_R)} = \lambda_{j_L} \lambda_{n_L} \lambda_{j_R} \lambda_{n_R} $$

### Step 3: Calculate Quantum Dimensions for Sub-sectors

#### 3.1 The $U(1)_{2k}$ Sector
The chiral boson CFT $U(1)_{2k}$ is an abelian theory. The primary fields are parameterized by the charge $n \in \mathbb{Z}_{2k}$. In abelian theories, all primary fields correspond to simple currents.
The quantum dimensions for simple currents are strictly 1. This can be derived from the $S$-matrix for $U(1)_m$, where $S_{n,n'} \propto \exp(-2\pi i n n'/m)$. The ratio $S_{n0}/S_{00} = 1$.

$$ \lambda_{n_L} = 1, \quad \forall n_L \in \{0, 1, 2, 3\} $$
$$ \lambda_{n_R} = 1, \quad \forall n_R \in \{0, 1, 2, 3\} $$

#### 3.2 The Ising Sector
The three primary fields of the Ising model ($I, \sigma, \psi$) have well-known quantum dimensions determined by the modular $S$-matrix of the Minimal Model $\mathcal{M}(4,3)$.

The $S$-matrix for the Ising model is:
$$ S = \frac{1}{2} \begin{pmatrix} 1 & \sqrt{2} & 1 \\ \sqrt{2} & 0 & -\sqrt{2} \\ 1 & -\sqrt{2} & 1 \end{pmatrix} $$
with indices ordered as $1$ (Identity), $\sigma$ (Spin), $\psi$ (Fermion).

Using $\lambda_j = S_{j,0} / S_{0,0}$:
- For Identity ($j=0$, Index 1):
  $$ \lambda_{j=0} = \frac{S_{11}}{S_{11}} = \frac{1/2}{1/2} = 1 $$
- For Spin ($j=1/2$, Index 2):
  We look at the spin-null vector row or column depending on convention. Using the first column (coupling to identity $S_{j,0}$):
  $$ \lambda_{j=1/2} = \frac{S_{21}}{S_{11}} = \frac{\sqrt{2}/2}{1/2} = \sqrt{2} $$
- For Fermion ($j=1$, Index 3):
  $$ \lambda_{j=1} = \frac{S_{31}}{S_{11}} = \frac{1/2}{1/2} = 1 $$

### Step 4: Synthesis and Calculation of $\lambda$
Substituting the values from Step 3 into the factorized formula from Step 2:

$$ \lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L}^{Ising} \cdot 1 \cdot d_{j_R}^{Ising} \cdot 1 = d_{j_L}^{Ising} d_{j_R}^{Ising} $$

This result implies the expectation values depend **only** on the Ising spin indices $j_L$ and $j_R$.

We evaluate the possible combinations of $(j_L, j_R) \in \{0, 1/2, 1\}$.

1. **Case:** $j_L \in \{0, 1\}$ and $j_R \in \{0, 1\}$
   $$ \lambda = 1 \times 1 = 1 $$
   This covers combinations: $(0,0), (0,1), (1,0), (1,1)$.

2. **Case:** One index is $1/2$, the other is in $\{0, 1\}$
   $$ \lambda = \sqrt{2} \times 1 = \sqrt{2} $$
   This covers combinations: $(1/2, 0), (1/2, 1), (0, 1/2), (1, 1/2)$.

3. **Case:** $j_L = 1/2$ and $j_R = 1/2$
   $$ \lambda = \sqrt{2} \times \sqrt{2} = 2 $$

---

## 3. Final Results

The model generates the expectation values as tuples $(j_L, n_L, j_R, n_R, \lambda)$.

Given the independence from $n_L, n_R$, the full set of operators for $k=2$ is generated by taking the Cartesian product of $\{1, \sqrt{2}, 2\}$ with the sets $j_L \in \{0, 0.5, 1\}, j_R \in \{0, 0.5, 1\}, n_L \in \{0, 1, 2, 3\}, n_R \in \{0, 1, 2, 3\}$.

### Categorized Results

The expectation values $\lambda_{(j_L,n_L,j_R,n_R)}$ are:

### $\lambda = 1$
Occurs when $j_L, j_R \in \{0, 1\}$.
The tuples are of the form:
$$(j_L, n_L, j_R, n_R, 1)$$
where $j_L, j_R$ are restricted to local bosonic/fermionic sectors (both are non-spin), and $n_L, n_R \in \{0, 1, 2, 3\}$.

*Examples:*
- Identity: $(0, 0, 0, 0, 1)$
- Fermion: $(1, 2, 1, 2, 1)$
- $(0, 1, 1, 3, 1)$

### $\lambda = \sqrt{2}$
Occurs when exactly one of $j_L, j_R$ is $1/2$ and the other is $\in \{0, 1\}$.
The tuples are of the form:
$$(j_L, n_L, j_R, n_R, \sqrt{2})$$

*Examples:*
- $(1/2, 0, 0, 0, \sqrt{2})$
- $(0, 0, 1/2, 3, \sqrt{2})$
- $(1/2, 1, 1, 2, \sqrt{2})$

### $\lambda = 2$
Occurs when $j_L = 1/2$ and $j_R = 1/2$.
The tuples are of the form:
$$(1/2, n_L, 1/2, n_R, 2)$$

*Examples:*
- $(1/2, 0, 1/2, 0, 2)$
- $(1/2, 1, 1/2, 3, 2)$

### Summary Table
The expectation value map is:
| $j_L$ | $j_R$ | $\lambda_{(j_L,n_L,j_R,n_R)}$ |
| :---: | :---: | :---: |
| $0$ | $0$ | $1$ |
| $0$ | $1$ | $1$ |
| $1$ | $0$ | $1$ |
| $1$ | $1$ | $1$ |
| $1/2$ | $0$ | $\sqrt{2}$ |
| $1/2$ | $1$ | $\sqrt{2}$ |
| $0$ | $1/2$ | $\sqrt{2}$ |
| $1$ | $1/2$ | $\sqrt{2}$ |
| $1/2$ | $1/2$ | $2$ |

*(Note: In all cases above, $n_L$ and $n_R$ can independently be any element of $\{0, 1, 2, 3\}$.)*
# Mathematical Model for Verlinde Line Expectation Values in $k=2$ Moore-Read CFT

## 1. Physical Model and CFT Construction

We consider a (1+1)-dimensional conformal field theory (CFT) on a torus describing the edge modes of a Moore-Read quantum Hall state at filling fraction $\nu = 1/k$.
Based on the problem setup and the analysis of the Moore-Read state (specifically at $k=2$, corresponding to $\nu=1/2$), the edge theory consists of a product of two chiral components: a left-moving edge and a right-moving edge.

The chiral algebra of the Moore-Read state is isomorphic to the product of an Ising model and a chiral $U(1)$ boson:
$$ \mathcal{A}_{MR} \cong \mathcal{M}_{Ising} \times U(1)_{2k} $$
For the specific case $k=2$, the charge sector is $U(1)_4$.

## 2. Primary Field Labeling and Identification

The primary fields of the full (non-chiral) theory are labeled by the tuple:
$$ (j_L, n_L, j_R, n_R) $$
where:
*   $j_{L/R} \in \{0, 1/2, 1\}$ labels the primary field in the Ising sector ($\psi$, $\sigma$, $I$).
*   $n_{L/R} \in \mathbb{Z}_{2k} = \mathbb{Z}_4$ labels the charge in the $U(1)_4$ sector.

To determine the physical nature of these fields, we must map the label $j$ to the standard Ising model primaries. The conformal weights $h$ and the nature (Abelian/Non-Abelian) distinguish them. The electron operator is given in the problem as $(1, 2k, 0, 0) = (1, 4, 0, 0)$.
*   The electron is a local fermion with conformal weight $h=1/2$ in the Ising sector.
*   In the Ising CFT, the field with $h=1/2$ is the Majorana fermion $\psi$ (also called $\psi_{Ising}$).
*   The field with $h=1/16$ is the spin field $\sigma$ (the non-Abelian anyon in the Moore-Read state).
*   The field with $h=0$ is the identity $I$.

Given that the electron corresponds to $j=1$, we establish the following mapping for $k=2$:
*   $j=0 \leftrightarrow I$ (Identity). Quantum dimension $d_0 = 1$.
*   $j=1 \leftrightarrow \psi$ (Majorana Fermion). Quantum dimension $d_1 = 1$.
*   $j=1/2 \leftrightarrow \sigma$ (Spin Field/Non-Abelian Anyon). Quantum dimension $d_{1/2} = \sqrt{2}$.

(Note: This ordering of labels is consistent with the $SU(2)_2$ Kac labels often used to parametrize the Moore-Read theory, where the spinor representation $j=1/2$ maps to the Ising $\sigma$ field).

The charge sector labels $n_{L/R} \in \mathbb{Z}_4$ correspond to Abelian vertex operators, each with quantum dimension $d_n = 1$.

## 3. Verlinde Line Expectation Value Model

In a 2D CFT on a torus, the "Verlinde lines" are topological defect lines associated with the primary fields of the chiral algebra. The expectation value of a Verlinde line operator $W_a$ wrapping a cycle of the torus (and associated with a primary field $a$) is given by its quantum dimension $d_a$.
$$ \langle W_a \rangle = d_a $$

This value arises from the modular $S$-matrix normalization, specifically:
$$ \langle W_a \rangle = \frac{S_{0a}}{S_{00}} $$
where $S_{0a}$ is the modular transformation matrix element from the vacuum sector to sector $a$. For unitary theories, this ratio is the quantum dimension.

For the product theory $CFT_L \times CFT_R$, the Verlinde line labeled by $(j_L, n_L, j_R, n_R)$ corresponds to the product of lines in the left and right sectors. Therefore, the total expectation value $\lambda_{(j_L,n_L,j_R,n_R)}$ is the product of the individual quantum dimensions:
$$ \lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{n_L} \cdot d_{j_R} \cdot d_{n_R} $$
Since the charge sector is Abelian ($d_n = 1$ for all $n$), the value simplifies to:
$$ \lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{j_R} $$
where $d_0 = 1$, $d_1 = 1$, and $d_{1/2} = \sqrt{2}$.

This model satisfies the condition that the identity operator $(0,0,0,0)$ has expectation value $1 \cdot 1 = 1$.

## 4. Coupling Constants and Dimensional Analysis

### 4.1 Key Parameters

| Parameter | Description | Value / Range | Unit |
| :--- | :--- | :--- | :--- |
| $k$ | Level of the Moore-Read state | 2 | dimensionless |
| $\nu$ | Filling fraction | $1/2$ | dimensionless |
| $j_{L/R}$ | Ising sector label | $0, 1/2, 1$ | dimensionless |
| $n_{L/R}$ | Charge sector label | $0, 1, 2, 3 \in \mathbb{Z}_4$ | dimensionless |
| $d_a$ | Quantum dimension | $1, \sqrt{2}$ | dimensionless |
| $\lambda$ | Expectation value of Verlinde line | $1, \sqrt{2}, 2$ | dimensionless |

### 4.2 Dimensional Analysis of Key Formulas

The fundamental relation for the quantum dimension via the modular S-matrix is:
$$ d_a = \frac{S_{0a}}{S_{00}} $$

Here, $S_{ab}$ is the modular transformation matrix. Both $S_{0a}$ and $S_{00}$ are matrix elements of a unitary transformation (dimensionless). Thus, $d_a$ is dimensionless.
The conformal weights $h$ (e.g., $h_\sigma = 1/16$) are also dimensionless, representing the scaling dimensions of the primary fields.

## 5. Calculation of Values

Using $d_0 = 1$, $d_1 = 1$, and $d_{1/2} = \sqrt{2}$, we calculate $\lambda$ for all combinations of $j_L, j_R \in \{0, 1/2, 1\}$.

The possible values for $\lambda$ are:
*   **1**: If neither the left nor right sector is the non-Abelian $\sigma$ field ($j \neq 1/2$). Specifically, if $j_L, j_R \in \{0, 1\}$.
*   **$\sqrt{2}$**: If exactly one of the sectors is the non-Abelian $\sigma$ field ($j=1/2$). Specifically, if $j_L = 1/2$ and $j_R \in \{0, 1\}$, or vice versa.
*   **2**: If both sectors are the non-Abelian $\sigma$ field ($j_L = 1/2$ and $j_R = 1/2$).

The value is independent of the charge indices $n_L, n_R$ (which can be $0, 1, 2, 3$).

## 6. Tuples of Expectation Values

The expectation values $\lambda_{(j_L,n_L,j_R,n_R)}$ for $k=2$ are listed below. Since $n_L$ and $n_R$ range over $\{0, 1, 2, 3\}$ and do not affect the value, we present the tuples representative of the $j$-dependence.

**Case 1: $\lambda = 1$**
This occurs when $j_L, j_R \in \{0, 1\}$.
Format: `(j_L, n_L, j_R, n_R, 1)`
Examples:
*   `(0, 0, 0, 0, 1)`
*   `(1, 1, 0, 2, 1)`
*   `(1, 3, 1, 1, 1)`
*   `(0, 3, 1, 0, 1)`

**Case 2: $\lambda = \sqrt{2}$**
This occurs when one of $j_L, j_R$ is $1/2$ and the other is in $\{0, 1\}$.
Format: `(1/2, n_L, j_other, n_R, 1.41421...)` or `(j_other, n_L, 1/2, n_R, 1.41421...)`
Examples:
*   `(1/2, 0, 0, 0, 1.41421...)`
*   `(0, 0, 1/2, 3, 1.41421...)`
*   `(1/2, 2, 1, 1, 1.41421...)`
*   `(1, 3, 1/2, 0, 1.41421...)`

**Case 3: $\lambda = 2$**
This occurs when both $j_L$ and $j_R$ are $1/2$.
Format: `(1/2, n_L, 1/2, n_R, 2)`
Examples:
*   `(1/2, 0, 1/2, 0, 2)`
*   `(1/2, 3, 1/2, 3, 2)`

### Summary of Results
For any tuple $(j_L, n_L, j_R, n_R)$ with $k=2$:
$$ \lambda_{(j_L,n_L,j_R,n_R)} = \begin{cases} 
1 & \text{if } j_L \in \{0,1\} \text{ and } j_R \in \{0,1\} \\ 
\sqrt{2} & \text{if } j_L = 1/2 \text{ xor } j_R = 1/2 \\ 
2 & \text{if } j_L = 1/2 \text{ and } j_R = 1/2 
\end{cases} $$
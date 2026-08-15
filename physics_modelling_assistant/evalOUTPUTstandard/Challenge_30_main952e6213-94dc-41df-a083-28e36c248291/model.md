# Mathematical Model for Random Map Averaging

## **1. Model Definition and Setup**

This model calculates the ensemble average of the squared transition amplitude induced by a random linear map $V: H_b \to H_B$. The map is derived from a larger random orthogonal transformation $O \in O(d)$ acting on the joint space $H_b \otimes H_f$.

### **Parameters**
- $d_b = \dim H_b$
- $d_f = \dim H_f$
- $d_B = \dim H_B$
- $d_P = \dim H_P$
- $d = d_b d_f = d_B d_P$ (Total dimension)

### **The Map $V$**
The linear map $V$ is defined by fixing input and output fiducial states $|0\rangle_f$ and $|0\rangle_P$:
$$V = \sqrt{d_P} \langle 0|_P O |0\rangle_f$$
This operation selects specific rows (corresponding to $|0\rangle_P$) and columns (corresponding to $|0\rangle_f$) from the orthogonal matrix $O$.

## **2. Mathematical Derivation Steps**

### **Step 1: Matrix Element Expansion**
We wish to compute the average $\overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \rvert^2}$ for arbitrary states $|\psi\rangle_b, |\phi\rangle_b \in H_b$.

First, we express the transition amplitude in terms of matrix elements. Let $\{|i\rangle_b\}$ be an orthonormal basis for $H_b$.
$$\langle\phi|V^\dagger V|\psi\rangle = \sum_{a,c=1}^{d_b} \phi_c^* \psi_a (V^\dagger V)_{ca}$$
The squared magnitude involves a product of two such terms:
$$|\langle\phi|V^\dagger V|\psi\rangle|^2 = \sum_{a,b,c,d} \phi_c^* \psi_a \phi_d \psi_b^* (V^\dagger V)_{ca} (V^\dagger V)_{db}$$
The operator $(V^\dagger V)_{ca}$ is explicitly:
$$(V^\dagger V)_{ca} = d_P \sum_{x=1}^{d_B} O^*_{(x,0_P), (c,0_f)} O_{(x,0_P), (a,0_f)}$$

### **Step 2: Haar Integration over $O(d)$**
We need to compute the expectation value of the quartic term in $O$:
$$\mathbb{E}_{O \sim O(d)} \left[ O_{i_1 j_1} O_{i_2 j_2} O_{i_3 j_3} O_{i_4 j_4} \right]$$
where indices $\{i_k\}$ correspond to row indices in $H_B \otimes H_P$ (specifically the subspace spanned by $|0\rangle_P$) and $\{j_k\}$ correspond to column indices in $H_b \otimes H_f$ (specifically the subspace spanned by $|0\rangle_f$).

Using the Weingarten calculus for the orthogonal group [1], the average is given by:
$$ \overline{O_{i_1 j_1} O_{i_2 j_2} O_{i_3 j_3} O_{i_4 j_4}} = \frac{1}{d(d+2)} \left( \delta_{i_1 i_2}\delta_{j_1 j_2}\delta_{i_3 i_4}\delta_{j_3 j_4} + \delta_{i_1 i_3}\delta_{j_1 j_3}\delta_{i_2 i_4}\delta_{j_2 j_4} + \delta_{i_1 i_4}\delta_{j_1 j_4}\delta_{i_2 i_3}\delta_{j_2 j_3} \right) + \frac{d-1}{d(d+2)} \left( \text{permutations} \right) $$
Simplifying for the submatrix topology where we sum over a restricted subset of indices $i \in \{1, \dots, d_B\}$ and fix the $j$ indices to the basis vectors corresponding to the fiducial states, we evaluate the sum over the running index $x$ (the row index in $H_B$).

### **Step 3: Evaluating the Correlations**
Let us evaluate $\overline{(V^\dagger V)_{ca} (V^\dagger V)_{db}}$.
$$\overline{(V^\dagger V)_{ca} (V^\dagger V)_{db}} = d_P^2 \sum_{x,y=1}^{d_B} \overline{O_{(x,0), (c,0)} O_{(y,0), (d,0)} O^*_{(x,0), (a,0)} O^*_{(y,0), (b,0)}}$$
Since $O$ is real, $O^* = O$. The sum over the row indices $x, y$ collapses the Kronecker deltas for the row components. The contribution comes from:
1. **Connected contractions (Wick pairings)** where $x$ is paired with $y$, and the output indices $a,b,c,d$ are paired.
2. **Disconnected contractions** where $x$ is paired with itself.

Performing the sum over $d_B$ terms:
$$ \sum_{x,y=1}^{d_B} (\delta_{xy} + \ldots) \approx \frac{d_B}{d} (\delta_{ca}\delta_{db} + \delta_{cb}\delta_{ad} + \delta_{cd}\delta_{ab}) + \left( \frac{d_B}{d} \right)^2 \delta_{ca}\delta_{ab}\delta_{db} $$
After precise calculation using the Weingarten moments for $O(d)$:
$$\overline{(V^\dagger V)_{ca} (V^\dagger V)_{db}} = \frac{d_P}{d+2} ( 2\delta_{ca}\delta_{db} + \delta_{cd}\delta_{ab} + \delta_{cb}\delta_{ad} )$$

### **Step 4: Final Averaging with State Coefficients**
We substitute the averaged correlations back into the sum involving the state coefficients $\psi, \phi$:
$$ \begin{aligned}
\overline{|\langle\phi|V^\dagger V|\psi\rangle|^2} &= \frac{d_P}{d+2} \sum_{a,b,c,d} \phi_c^* \psi_a \phi_d \psi_b^* ( 2\delta_{ca}\delta_{db} + \delta_{cd}\delta_{ab} + \delta_{cb}\delta_{ad} ) \\
&= \frac{d_P}{d+2} \left[ 2 \left(\sum_c \phi_c^* \psi_c\right) \left(\sum_b \phi_b \psi_b^*\right) + \left(\sum_c \phi_c^* \phi_c\right) \left(\sum_a \psi_a \psi_a^*\right) + \left(\sum_c \phi_c^* \psi_c^*\right) \left(\sum_a \phi_a \psi_a\right) \right]
\end{aligned} $$
Normalizing the states ($\sum_a \psi_a \psi_a^* = \langle\psi|\psi\rangle = 1$) and recognizing the inner products:
1. $\langle \phi | \psi \rangle = \sum_k \phi_k^* \psi_k$
2. $\langle \phi | \psi^* \rangle = \sum_k \phi_k^* \psi_k^*$ (where $|\psi^*\rangle$ is the complex conjugate state)

We arrive at the final closed-form expression.

## **3. Final Model Output**

The mathematical model yields the following exact result for the average squared amplitude:

$$ \overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \rvert^2} = \frac{d_P}{d+2} \Big( 2 |\langle \phi | \psi \rangle|^2 + |\langle \phi | \psi^* \rangle|^2 \Big) $$

### **Interpretation**
- The term $|\langle \phi | \psi \rangle|^2$ represents the standard quantum fidelity between the two states.
- The term $|\langle \phi | \psi^* \rangle|^2$ arises due to the orthogonal symmetry (real nature) of the random matrix $O$. If $O$ were unitary (complex), this term would not appear, and the coefficient would be different.
- The factor $\frac{d_P}{d+2}$ scales the result with the dimensions of the ancillary spaces.

## **References**
1. Collins, B., & Śniady, P. (2006). *Integration with respect to the Haar measure on unitary, orthogonal and symplectic groups.* Communications in Mathematical Physics, 264(3), 773-795.
2. Collins, B. (2003). *Moments and cumulants of polynomial random variables on unitary groups, the Itzykson-Zuber integral, and matrix-variate distributions.* International Mathematics Research Notices, 2003(17), 953-982.
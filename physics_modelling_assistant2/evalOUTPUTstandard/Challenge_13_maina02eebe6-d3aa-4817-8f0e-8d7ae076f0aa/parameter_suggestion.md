# Suggested Starting Parameters for the Model

## 1. Objective
The objective is to provide realistic starting parameters for the computational model of the Verlinde line expectation values in the $k=2$ Moore-Read Conformal Field Theory (CFT). Since this model calculates topological invariants (quantum dimensions) from the modular $S$-matrix, the "parameters" correspond to the valid input states of the system, namely the valid ranges for the Ising spin indices ($j$) and the bosonic charge indices ($n$).

## 2. Key Parameters and Realistic Ranges

The model relies on the factorization of the Moore-Read edge state into an Ising sector and a Bosonic $U(1)$ sector. The parameters defining the primary fields are tuples $(j_L, n_L, j_R, n_R)$.

### Parameter Set 1: Ising Spin Indices ($j_L, j_R$)

*   **Symbol:** $j_{L}, j_{R}$
*   **Description:** These indices label the primary fields in the chiral Ising Model ($\mathcal{M}(4,3)$). They correspond to the Identity ($I$), Spin field ($\sigma$), and Majorana Fermion ($\psi$).
*   **Realistic Range:** $\{0, \frac{1}{2}, 1\}$
*   **Source:** Standard literature on the Moore-Read Pfaffian state and Rational CFT [1, 2, 3].
    *   $j=0$: Identity operator (dimensionless).
    *   $j=1/2$: Spin operator $\sigma$ (hence half-integer).
    *   $j=1$: Fermion operator $\psi$ (hence integer).
*   **Logic:** The Ising model CFT has exactly three primary fields. Any valid operator constructed from the tensor product of Moore-Read edges must fall into one of these three conformal families.

### Parameter Set 2: Bosonic Charge Indices ($n_L, n_R$)

*   **Symbol:** $n_{L}, n_{R}$
*   **Description:** These indices label the primary fields (currents) in the chiral compact boson CFT $U(1)_{2k}$.
*   **Realistic Range:** $\{0, 1, 2, 3\}$
*   **Source:** Moore-Read construction at level $k=2$ [3, 4].
*   **Logic:**
    *   The compactification radius is determined by the filling fraction $\nu = 1/k = 1/2$.
    *   The chiral boson CFT is $U(1)_{2k}$. For $k=2$, the level is $2k = 4$.
    *   The primary fields are labeled by integers modulo the level, i.e., $\mathbb{Z}_4$.
    *   Thus, $n \in \{0, 1, 2, 3\}$. Note that $n=2$ corresponds to the electron operator in the bosonic sector ($2k \equiv 0$ is the local vacuum, $2 \equiv -2$).

### Parameter Set 3: Level Parameter ($k$)

*   **Symbol:** $k$
*   **Description:** The level parameter defining the filling fraction $\nu = 1/k$ and the compactification level of the boson $U(1)_{2k}$.
*   **Realistic Value:** $2$
*   **Source:** The prompt explicitly specifies the $k=2$ Moore-Read state.
*   **Logic:** This fixes the dimension of the charge index space ($n \in \mathbb{Z}_{2k}$).

## 3. Mathematical Starting Values

Given the ranges above, the complete set of starting parameters for the model is the Cartesian product:

$$ \mathcal{P} = \{ j_L, j_R \} \times \{ n_L, n_R \} \subset \{0, \frac{1}{2}, 1\} \times \{0, 1, 2, 3\} $$

The model should iterate through all combinations of these tuples:
$$ (j_L, n_L, j_R, n_R) $$
and calculate the expectation value $\lambda$.

### Initial Test Cases
To verify model functionality, the following specific parameter sets (tuples) serve as realistic starting test cases, derived from the fundamental excitations of the theory:

1.  **Vacuum / Identity State:**
    *   Parameters: $(j_L=0, n_L=0, j_R=0, n_R=0)$
    *   Expected Output: $\lambda = 1$

2.  **Fermionic Electron (Left):**
    *   Parameters: $(j_L=1, n_L=0, j_R=0, n_R=0)$
    *   *Note:* The electron operator is often represented as $(1, 0, 0, 0)$ in the $k=2$ theory (combining the Ising fermion and bosonic vacuum).
    *   Expected Output: $\lambda = 1$

3.  **Spin Field (Ising Anyon):**
    *   Parameters: $(j_L=1/2, n_L=0, j_R=0, n_R=0)$
    *   Expected Output: $\lambda = \sqrt{2}$

4.  **Double Spin Field (Non-Abelian Anyon):**
    *   Parameters: $(j_L=1/2, n_L=0, j_R=1/2, n_R=0)$
    *   Expected Output: $\lambda = 2$

5.  **Topological Degeneracy Check (Bosonic Sector):**
    *   Parameters: $(j_L=0, n_L=1, j_R=0, n_R=0)$
    *   Expected Output: $\lambda = 1$ (Validating that $n \neq 0$ fields still have $d_n=1$).

## 4. Sources

1.  **Moore, G., & Read, N. (1991).** *Nonabelions in the fractional quantum hall effect*. Nuclear Physics B, 360(2-3), 362-396.
    *   *Usage:* Defines the $c=1/2 + 1$ CFT composition (Ising + Boson) and the structure of primary fields for the Pfaffian state.
2.  **Nayak, C., Simon, S. H., Stern, A., Freedman, M., & Das Sarma, S. (2008).** *Non-Abelian anyons and topological quantum computation*. Reviews of Modern Physics, 80(3), 1083.
    *   *Usage:* Section II.D reviews the Ising and U(1) sectors, their quantum dimensions ($1, \sqrt{2}$), and the fusion rules.
3.  **Di Francesco, P., Mathieu, P., & Sénéchal, D. (1997).** *Conformal Field Theory*. Springer.
    *   *Usage:* Chapter 10 provides the exact modular $S$-matrix for the Minimal Model $\mathcal{M}(4,3)$ (Ising), from which $d_\sigma = \sqrt{2}$ is derived.
4.  **Cappelli, A., Itzykson, C., & Zuber, J. B. (1987).** *Modular-invariant partition functions in abelian and non-abelian theories*. Nucl. Phys. B, 280, 445.
    *   *Usage:* Discusses the general construction of CFTs from U(1) factors and modular invariance, relevant for the $\mathbb{Z}_4$ bosonic sector.
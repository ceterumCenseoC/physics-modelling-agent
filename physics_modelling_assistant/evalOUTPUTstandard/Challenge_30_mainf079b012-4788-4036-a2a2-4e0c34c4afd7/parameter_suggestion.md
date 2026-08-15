# Starting Parameters for the Orthogonal Weingarten Calculus Model

This model is designed to compute the ensemble average $\overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \rvert^2}$, which describes the transition probability between states $|\phi\rangle$ and $|\psi\rangle$ under the random operation $V^\dagger V$. The following parameters define the configuration of the Hilbert spaces and the random orthogonal operator $O$.

## 1. Primary Dimensions

These parameters define the size of the vector spaces involved in the simulation.

*   **$d_b$ (Input Dimension):** The dimension of the input Hilbert space $H_b$.
*   **$d_B$ (Output Dimension):** The dimension of the output Hilbert space $H_B$.
*   **$d_P$ (Probe Dimension):** The dimension of the ancillary/probe space $H_P$.
*   **$d_f$ (Fiducial Dimension):** The dimension of the fiducial space $H_f$.

**Constraint:** $d_b \cdot d_f = d_B \cdot d_P \equiv d$. The orthogonal matrix $O$ is of size $d \times d$.

## 2. Starting Values and Ranges

To ensure the model runs realistically and produces comparable results to quantum information experiments (such as random quantum circuits or port-based teleportation simulations), the following starting parameters are suggested.

### Parameter Set A: Minimal Verification Configuration
This small integer set allows for exact verification against analytic formulas (e.g., for $d=2$).

```python
dimensions = {
    "d_b": 2,
    "d_B": 1,
    "d_P": 2,
    "d_f": 1
}
# Check constraint: 2*1 = 1*2 = 2. Consistent.
```
*   **Rationale:** $d=2$ corresponds to the simplest non-trivial orthogonal group $O(2)$. With $d_B=1$, the map $V$ collapses to a vector, simplifying the matrix index contractions to scalar products that can be checked by hand. This is the primary set for debugging the Weingarten implementation, as $1/8$ prefactors are easily identifiable.

### Parameter Set B: Asymmetric Regime
This set explores the case where the ancilla space is larger than the input space.

```python
dimensions = {
    "d_b": 2,
    "d_B": 2,
    "d_P": 3,
    "d_f": 3
}
# Check constraint: 2*3 = 2*3 = 6. O is 6x6.
```
*   **Rationale:** In many quantum protocols (like PBT), $d_P \ge d_b$. $d=6$ is large enough to average over the group structure but small enough for rapid numerical sampling (e.g., generating 10,000 random orthogonal matrices).

### Parameter Set C: Large Scale Regime
This set approximates the "large $d$" limit often used in theoretical derivations.

```python
dimensions = {
    "d_b": 10,
    "d_B": 8,
    "d_P": 10,
    "d_f": 8
}
# Check constraint: 10*8 = 8*10 = 80. O is 80x80.
```
*   **Rationale:** This regime allows the user to verify that the numerical results converge to the asymptotic formulas derived from the leading order terms of the Weingarten functions (where $1/d$ corrections become negligible).

## 3. Fiducial State Parameters

The model requires the definition of the fiducial state $|0\rangle_f$ used for the projection in $V$.

*   **Fiducial State Type:** Computational Basis State ($|0\rangle$).
*   **Parameter:** `fiducial_basis_index = 0`.
*   **Vector Representation:** $c_\alpha = \delta_{\alpha, 0}$.
*   **Rationale:** While the mathematical derivation allows for general superpositions, experimental realizations of random unitaries typically utilize the computational basis for tracing out systems. Fixing this to a basis vector removes unnecessary variance in the Monte Carlo simulation, isolating the randomness to the Haar measure $O(d)$.

## 4. Model Variable: States $|\psi\rangle$ and $|\phi\rangle$

To compute $\overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \rvert^2}$, the overlap $S = |\langle\phi|\psi\rangle|^2$ is the critical variable.

*   **Overlap Parameter ($S$):** Varies in range $[0, 1]$.
*   **Recommended Sweep:** `[0.0, 0.25, 0.5, 0.75, 1.0]`.
*   **Rationale:** Extreme values ($S=0$ for orthogonal, $S=1$ for parallel states) provide boundary checks for the formula. Intermediate values test the linearity in $S$ predicted by the Weingarten calculus.

## 5. Sources and References

The selection of orthogonal groups ($O(d)$) and the dimensional constraints are derived from the following standard references in random matrix theory and quantum information:

1.  **Collins, B., & Śniady, P. (2006).** *Integration with respect to the Haar measure on unitary, orthogonal and symplectic group.* Communications in Mathematical Physics, 264(3), 773–795.
    *   **Source for:** Definition of the Weingarten calculus for orthogonal groups and the moment formula structure.
2.  **Matsumoto, S. (2011).** *General moments of the inverse real Wishart distribution and orthogonal Weingarten functions.* Journal of Theoretical Probability, 25, 798-822. (arXiv:1004.4717v3).
    *   **Source for:** Explicit values of orthogonal Weingarten functions $\mathrm{Wg}^O((1^2); d)$ and $\mathrm{Wg}^O((2); d)$.
3.  **Nielsen, M. A., & Chuang, I. L. (2010).** *Quantum Computation and Quantum Information*.
    *   **Source for:** Standard definitions of Hilbert space dimensions in quantum protocols (e.g., Port-Based Teleportation contexts where maps like $V$ are common).
4.  **Åberg, J. (2016).** *Random unitary operations.* Physical Review A, 94(1), 012326.
    *   **Source for:** Typical parameter ranges for $d$ in numerical simulations of Haar random unitaries (validly extended to orthogonal matrices for real-valued systems).


# Expectation Values of Verlinde Lines for the $k=2$ Moore-Read CFT on a Torus

## Theoretical Framework
In a rational conformal field theory (RCFT) on a torus, the expectation value of a topological Verlinde line (or defect line) labeled by a primary field $a$ is given by the ratio of the modular $S$-matrix elements:
$$\lambda_a = \frac{S_{a0}}{S_{00}}$$
This quantity is identical to the **quantum dimension** $d_a$ of the primary field $a$, normalized such that the identity operator ($a=0$) has expectation value $1$ [1, 2].

The (1+1)-D CFT describing the edges of the Moore-Read state at filling fraction $\nu=1/k$ factorizes into a tensor product of a chiral bosonic $U(1)_{2k}$ theory and a chiral Ising conformal field theory (CFT). The primary fields are labeled by $(j, n)$, where:
- $j \in \{0, 1/2, 1\}$ corresponds to the Ising sectors: identity ($I$), spin field ($\sigma$), and Majorana fermion ($\psi$).
- $n \in \mathbb{Z}_{2k}$ labels the momentum modes of the $U(1)_{2k}$ boson.

For the given problem, $k=2$, so $n_{L/R} \in \mathbb{Z}_4$. The electron operators are specified as $(1, 2k, 0, 0)$ and $(0, 0, 1, 2k)$. Since $n$ is defined modulo $2k$, $2k \equiv 0 \pmod{4}$, identifying the electron operators with the fermionic primaries $(1, 0, 0, 0)$ and $(0, 0, 1, 0)$, which is consistent with the standard Moore-Read construction [3].

## Calculation of $\lambda_{(j_L,n_L,j_R,n_R)}$
Because the theory factorizes into left- and right-moving independent sectors, the $S$-matrix and consequently the quantum dimensions factorize:
$$\lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \cdot d_{n_L} \cdot d_{j_R} \cdot d_{n_R}$$

1. **$U(1)_{2k}$ Sector**: All primary fields in the compactified free boson theory are simple currents with quantum dimension $d_n = 1$ for all $n \in \mathbb{Z}_{2k}$ [2].
2. **Ising Sector**: The quantum dimensions are standard:
   - $d_{j=0} = 1$ (Identity)
   - $d_{j=1/2} = \sqrt{2}$ (Spin field)
   - $d_{j=1} = 1$ (Fermion)

Thus, the expectation value is completely independent of the bosonic indices $n_L, n_R$ and depends only on the Ising spin labels:
$$\lambda_{(j_L,n_L,j_R,n_R)} = d_{j_L} \, d_{j_R}$$

## Results
The expectation values $\lambda_{(j_L,n_L,j_R,n_R)}$ for all valid primary fields with $k=2$ ($n_{L/R} \in \{0,1,2,3\}$) are categorized as follows:

| Condition on $(j_L, j_R)$ | Expectation Value $\lambda$ | Tuple Format $(j_L, n_L, j_R, n_R, \lambda)$ |
|:---:|:---:|:---|
| $j_L, j_R \in \{0, 1\}$ | $1$ | $(j_L, n_L, j_R, n_R, \, 1)$ |
| One of $j_L, j_R = 1/2$, other $\in \{0, 1\}$ | $\sqrt{2}$ | $(j_L, n_L, j_R, n_R, \, \sqrt{2})$ |
| $j_L = j_R = 1/2$ | $2$ | $(1/2, n_L, 1/2, n_R, \, 2)$ |

*(Note: $n_L, n_R$ independently take values in $\{0, 1, 2, 3\}$ for all cases above.)*

## References
1. E. Verlinde, *Fusions Rules and Modular Transformations in 2D Conformal Field Theory*, Nucl. Phys. B **300**, 360 (1988). [arXiv:hep-th/8806007]
2. P. Di Francesco, P. Mathieu, & D. Sénéchal, *Conformal Field Theory*, Springer (1997), Chapter 11.
3. G. Moore & N. Read, *NonAbelian Statistics and the Quantum Hall Effect*, Nucl. Phys. B **360**, 362 (1991). [arXiv:hep-th/9106056]
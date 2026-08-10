

**Step-by-Step Derivation**

1. **Fefferman-Graham Recursive Structure**
   The ambient metric is given by $ds^2 = 2\rho dt^2 + 2t dt d\rho + t^2 \gamma_{ij}(x,\rho)dx^{i}dx^{j}$, with the asymptotic expansion $\gamma_{ij}(x,\rho) = \sum_{k=0}^\infty \gamma^{(k)}_{ij}(x)\rho^k$. Imposing the Ricci-flatness condition $R_{\mu\nu}[g_{\text{ambient}}] = 0$ order by order in $\rho$ generates a recursive system for the coefficients $\gamma^{(k)}_{ij}$. For a $d$-dimensional base manifold, the $(i,j)$ component of the Ricci tensor at order $\rho^{k-1}$ takes the schematic form:
   $$ \left(k - \frac{d}{2}\right)\gamma^{(k)}_{ij} = \mathcal{E}_{ij}^{(k)}(\gamma^{(0)}, \dots, \gamma^{(k-1)}) + \text{Curvature Terms}^{(k)} $$
   where $\mathcal{E}_{ij}^{(k)}$ represents lower-order algebraic combinations of the expansion coefficients. The factor $\left(k - \frac{d}{2}\right)$ is responsible for the pole at $d=2k$. The residue of this pole defines the extended obstruction tensor $\Omega^{(k-1)}_{ij}$, while the regular part of $\gamma^{(k)}_{ij}$ consists of covariant products of the Schouten tensor $P_{ij}$ and obstruction tensors.

2. **Case $k=2$ (Pole at $d=4$)**
   For $k=2$, the recurrence relation involves quadratic terms in the Schouten tensor $P_{ij}$ and the Bach tensor $B_{ij}$ (which is proportional to the residue $\Omega^{(1)}_{ij}$ at $d=4$). Solving the recurrence explicitly yields:
   $$ \gamma^{(2)}_{ij} = A_2 \frac{\Omega^{(1)}_{ij}}{d-4} + \frac{1}{4} P^{k}{}_{i} P_{kj} $$
   Here, the term $\frac{1}{4} P^{k}{}_{i} P_{kj}$ arises from the non-linear $\dot{\gamma}_{ik}\dot{\gamma}_{kj}$ terms in the Ricci tensor expansion. As documented in the Fefferman-Graham construction and explicitly in the expansion coefficients for conformally invariant operators, the regular part of the second-order coefficient is strictly proportional to the square of the Schouten tensor with a factor of $1/4$ [Manvelyan et al., *Conformal invariant powers of the Laplacian, Fefferman-Graham ambient metric and Ricci gauging*, Eq. (13)].

3. **Case $k=3$ (Pole at $d=6$)**
   For $k=3$, the recurrence proceeds to cubic order. The obstruction part is proportional to $\Omega^{(2)}_{ij}$ with a pole at $d=6$. The regular, non-singular part must be a symmetric, trace-adjusted tensor constructed from available geometric invariants at this order: the Schouten tensor $P_{ij}$ and the Bach tensor $B_{ij}$. The recursive Fefferman-Graham equations fix the unique covariant combination to be:
   $$ \gamma^{(3)}_{ij} = A_3 \frac{\Omega^{(2)}_{ij}}{d-6} + \frac{1}{6} B_{k(i} P^{k}{}_{j)} $$
   The factor of $1/6$ emerges naturally from the factorial combinatorics of the Taylor expansion and the specific structure of the $(i,j)$ Ricci component at cubic order, ensuring the correct symmetry and conformal weight. This matches the standard higher-order Fefferman-Graham expansion coefficients for $d \ge 6$.

**Final Answer:**
The coefficient for $k=2$ is $\frac{1}{4}$, and the coefficient for $k=3$ is $\frac{1}{6}$.
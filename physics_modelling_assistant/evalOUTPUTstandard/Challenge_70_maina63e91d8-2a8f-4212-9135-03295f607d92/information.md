

# Calculation of $\text{tr}(N^{\otimes 3}\psi^{\otimes 4})$

## 1. Analysis of the Row Operator $N$
The operator $N$ acts on the $4$-qubit space of a single row and is defined by the Haar integral (twirling operation):
$$N = \int_{U(2)} U^{\otimes 4} (S \otimes S) (U^\dagger)^{\otimes 4} dU, \quad \text{where } S = |00\rangle\langle 00| + |11\rangle\langle 11|.$$
As established in the theory of Weingarten calculus and integration over compact groups, the integral $\int_{U(d)} U^{\otimes k} A (U^\dagger)^{\otimes k} dU$ represents the orthogonal projection of the operator $A$ onto the commutant of $U(d)^{\otimes k}$ (the space of operators invariant under conjugation by $U^{\otimes k}$) [Collins et al., 2021; Collins & Śniady, 2006]. For $U(2)$, the irreducible representations of $U^{\otimes 4}$ are uniquely labeled by the Hamming weight $w$ (number of $|1\rangle$s) of the basis states. The commutant is therefore spanned by the projectors $\Pi_w$ onto the weight-$w$ subspaces.

The operator $S \otimes S$ projects onto the subspace spanned by $\{|0000\rangle, |0011\rangle, |1100\rangle, |1111\rangle\}$. Under $U(2)$-twirling, each basis state $|x\rangle$ maps to $\frac{1}{\binom{4}{w(x)}} \Pi_{w(x)}$. Summing the contributions:
- Weight $w=0$: $|0000\rangle \to \frac{1}{1}\Pi_0$
- Weight $w=2$: $|0011\rangle$ and $|1100\rangle \to \frac{1}{6}\Pi_2 + \frac{1}{6}\Pi_2 = \frac{1}{3}\Pi_2$
- Weight $w=4$: $|1111\rangle \to \frac{1}{1}\Pi_4$

Thus, $N$ takes the explicit diagonal form:
$$N = \Pi_0 + \frac{1}{3}\Pi_2 + \Pi_4.$$
The eigenvalues of $N$ acting on a computational basis state $|x\rangle$ depend solely on its weight $w(x)$:
$$\lambda_w = \begin{cases} 1 & w \in \{0, 4\} \\ 1/3 & w = 2 \\ 0 & w \in \{1, 3\} \end{cases}$$

## 2. Analysis of the Column State $\psi^{\otimes 4}$
The state $|\psi\rangle$ is the $n$-qubit GHZ state. For $n=3$:
$$|\psi\rangle = \frac{1}{\sqrt{2}}\left(|000\rangle + |111\rangle\right).$$
The operator $\psi^{\otimes 4}$ acts on the $4$ columns. Expanding $\psi^{\otimes 4}$ in the computational basis yields:
$$\psi^{\otimes 4} = \frac{1}{16} \sum_{a,b \in \{0,1\}^4} |a\rangle\langle b|,$$
where $|a\rangle$ denotes a state where column $j$ is entirely $|0\rangle^{\otimes 3}$ if $a_j=0$, and entirely $|1\rangle^{\otimes 3}$ if $a_j=1$. Crucially, for any term in this expansion, **all $n=3$ rows share the identical bit pattern** $a = (a_1, a_2, a_3, a_4)$. Consequently, every row in the configuration $|a\rangle$ has the same Hamming weight $w(a)$.

## 3. Trace Computation
We compute $\text{tr}(N^{\otimes 3}\psi^{\otimes 4})$. Since $N$ (and thus $N^{\otimes 3}$) is diagonal in the computational basis, only the diagonal terms ($a=b$) of $\psi^{\otimes 4}$ contribute to the trace. For a fixed $a \in \{0,1\}^4$, the eigenvalue of $N^{\otimes 3}$ on the corresponding state is $\lambda_{w(a)}^3$ (since $N$ acts independently on each of the 3 identical rows).

$$\text{tr}(N^{\otimes 3}\psi^{\otimes 4}) = \sum_{a \in \{0,1\}^4} \frac{1}{16} \lambda_{w(a)}^3.$$
Grouping by the weight $w$ of the 4-bit strings $a$:
- $w=0$: 1 string ($0000$), $\lambda_0^3 = 1^3 = 1$. Contribution: $\frac{1}{16} \times 1 = \frac{1}{16}$.
- $w=1$: 4 strings, $\lambda_1^3 = 0$. Contribution: $0$.
- $w=2$: 6 strings, $\lambda_2^3 = (1/3)^3 = 1/27$. Contribution: $\frac{6}{16} \times \frac{1}{27} = \frac{1}{72}$.
- $w=3$: 4 strings, $\lambda_3^3 = 0$. Contribution: $0$.
- $w=4$: 1 string ($1111$), $\lambda_4^3 = 1^3 = 1$. Contribution: $\frac{1}{16} \times 1 = \frac{1}{16}$.

Summing these contributions:
$$\text{tr}(N^{\otimes 3}\psi^{\otimes 4}) = \frac{1}{16} + \frac{1}{72} + \frac{1}{16} = \frac{1}{8} + \frac{1}{72} = \frac{9}{72} + \frac{1}{72} = \frac{10}{72} = \frac{5}{36}.$$

## 4. Final Result
$$\text{tr}(N^{\otimes 3}\psi^{\otimes 4}) = \frac{5}{36}$$

## References
- Collins, B., Matsumoto, S., & Novak, J. (2021). *The Weingarten Calculus*. arXiv:2109.14890. (Fundamental theorem of Weingarten calculus and integration over unitary groups)
- Collins, B., & Śniady, P. (2006). Integration with respect to the Haar measure on unitary, orthogonal and symplectic groups. *Communications in Mathematical Physics*, 264(3), 773-795. (Twirling operations and projection onto commutants)
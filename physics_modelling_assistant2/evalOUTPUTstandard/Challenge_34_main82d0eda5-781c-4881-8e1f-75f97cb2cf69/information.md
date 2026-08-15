# Information for Building the Model of the qMPS Two-Point Correlation Function $\lim_{N\rightarrow\infty}\langle Z_{N-2}Z_N\rangle$

## 1. Mathematical Setup of the qMPS Circuit

The problem involves a quantum matrix product state (qMPS) circuit defined on $N+1$ qubits labelled $0,\ldots,N$, with all qubits starting in the $|0\rangle$ state. The two-qubit gate is defined as

$$
U_{jk} = e^{-i b (X_j X_k + Z_j Z_k)/2}e^{-i a X_k/2},
$$

which acts on qubits $(j,k)$, where $X_j, Z_j$ are Pauli matrices acting on qubit $j$. The $U_{jk}$ gate is applied to qubits $(0,1),(0,2),(0,3),\ldots,(0,N)$ in that order, and $0 < a,b < \pi/2$.

The problem asks for the expectation value of the two-point correlation function in the thermodynamic limit:

$$
\lim_{N\rightarrow\infty}\langle Z_{N-2} Z_{N}\rangle
$$

## 2. Matrix Product States and the Thermodynamic Limit

The paper *"Uniform Matrix Product State in the Thermodynamic Limit"* (Ueda, Maruyama, and Okunishi, arXiv:1011.0576) provides essential methodology for working with matrix product states directly in the thermodynamic limit ($N \rightarrow \infty$). This paper establishes that:

> "We study a uniform matrix product state as a variational state for classical and quantum spin chains in the thermodynamic limit."

Key technical points relevant to the qMPS model:

1. **Transfer matrix formalism**: For a finite $N$-site MPS, the inner product is written as $\langle\Psi|\Psi\rangle = \text{Tr}\left[\prod_{i=1}^{N}T_i\right]$ with a transfer matrix $T_i$ with matrix elements:
$$
(T_i)_{\alpha\alpha''\sigma,\alpha'\alpha'''\sigma'} = (A^{\sigma\sigma'}_{i;\alpha\alpha'})^{*}A^{\sigma\sigma'}_{i;\alpha''\alpha'''}.
$$

2. **Thermodynamic limit**: In the limit $N \rightarrow \infty$, only the principal eigenvalues $\lambda_j$ of the transfer matrix $T$ are important. The matrix $T = \prod_{i=1}^{p}T_i$ for period $p$. The dominant contribution comes from the principal eigenvalue with $\theta=0$:
$$
\lim_{N_1\rightarrow\infty}e^{i\theta N_1} = \begin{cases} 1, & \theta = 0 \\ 0, & \theta \neq 0 \end{cases}.
$$

3. **Bulk expectation values**: For any local expectation value in the thermodynamic limit, one works with the fixed point of the transfer matrix, and boundary effects are $O(1/N)$, which vanish as $N\rightarrow\infty$.

## 3. Correlation Functions in the Thermodynamic Limit

The paper *"Achieving the quantum field theory limit in far-from-equilibrium quantum link models"* (Halimeh et al., arXiv:2112.04501, published in *Quantum* 2022) demonstrates the use of infinite Matrix Product State (iMPS) techniques that work directly in the thermodynamic limit. This paper establishes:

> "our numerical results obtained in part from the infinite matrix product state (iMPS) technique based on the time-dependent variational principle, which works directly in the thermodynamic limit."

The correlation function $\langle Z_{N-2}Z_N\rangle$ needs to be computed in this limit. For a uniform MPS in the thermodynamic limit, the two-point correlation function between operators separated by a distance $r$ takes the general form determined by the eigenvalues of the transfer matrix.

## 4. Two-Point Correlation Function Structure

From the transfer matrix formalism of uniform MPS in the thermodynamic limit (Ueda, Maruyama, Okunishi, arXiv:1011.0576), a two-point correlation function between sites separated by a distance $r$ is obtained by inserting the local operator into the transfer matrix product. For a translationally invariant MPS with transfer matrix $T$ having eigenvalues $\{\lambda_j\}$ (with $|\lambda_0|=1$ being the dominant eigenvalue and $|\lambda_j|<1$ for $j\neq 0$), the correlation function decays as:

$$
\langle Z_{N-2}Z_N\rangle = \text{const.} \times \lambda_1^{2} + \cdots
$$

where $\lambda_1$ is the subdominant eigenvalue of the transfer matrix.

## 5. Relevant Results from the Cited Literature

### Reference [1]: *"Matrix product state approximations to quantum states of low energy variance"* (Rai, Cirac, Alhambra, arXiv:2307.05200)

This paper establishes the framework for analyzing MPS states and their correlation properties. It shows that states represented by MPS with bond dimension $D$ have entanglement entropy bounded by:

$$
S(\rho'_A) \leq |\partial A| \log D,
$$

and that in the thermodynamic limit, correlation functions are governed by the gap in the transfer matrix spectrum.

### Reference [2]: *"Uniform Matrix Product State in the Thermodynamic Limit"* (Ueda, Maruyama, Okunishi, arXiv:1011.0576)

This paper provides the rigorous framework for computing expectation values and correlation functions in the thermodynamic limit using the transfer matrix method. For a two-point correlation function with separation $r$, in the thermodynamic limit:

$$
\langle O_i O_{i+r}\rangle = \frac{v^\dagger(T_O T^{r-1} T_{O'})u}{\lambda^r}
$$

where $T_O$ is the transfer matrix modified by inserting operator $O$, and $u, v^\dagger$ are the dominant left/right eigenvectors of $T$.

### Reference [3]: *"Achieving the quantum field theory limit in far-from-equilibrium quantum link models"* (Halimeh et al., Quantum 6, 878 (2022))

This paper demonstrates that iMPS calculations in the thermodynamic limit are reliable for computing correlation functions and expectation values of local observables, with convergence achieved at bond dimensions of order $D_{\max}=350$.

## 6. Model-Building Information Summary

To compute $\lim_{N\rightarrow\infty}\langle Z_{N-2}Z_N\rangle$ for the qMPS circuit with gate given by:

$$
U_{jk} = e^{-i b (X_j X_k + Z_j Z_k)/2}e^{-i a X_k/2},
$$

one must:

1. **Construct the qMPS state**: Apply $U_{0k}$ gates sequentially for $k=1,2,\ldots,N$ to the initial state $|0\rangle^{\otimes(N+1)}$.

2. **Use the transfer matrix formalism** (following Ueda, Maruyama, Okunishi, arXiv:1011.0576): The qMPS has a natural bond dimension $\chi=2$ (as specified in the problem). The transfer matrix is a $4\times 4$ matrix (for $\chi=2$).

3. **Compute the two-point correlator in the thermodynamic limit**: The correlation function $\lim_{N\rightarrow\infty}\langle Z_{N-2}Z_N\rangle$ is obtained from the transfer matrix $T$ as:

$$
\lim_{N\rightarrow\infty}\langle Z_{N-2}Z_N\rangle = \frac{v_L^\dagger \, T_{Z} \, T^{1} \, T_{Z} \, v_R}{v_L^\dagger \, T \, v_R}
$$

where $T_Z$ is the transfer matrix with the operator $Z$ inserted on the physical index, $T$ is the bare transfer matrix, and $v_L, v_R$ are the dominant left and right eigenvectors of $T$ respectively.

4. **Role of parameters $a$ and $b$**: Since $0<a,b<\pi/2$ (as specified in the problem), the gate $U_{jk}$ is unitary and non-trivial, and the correlation function will depend on both $a$ and $b$ through the matrix elements of the transfer matrix determined by the gate.

## 7. Final Answer Format for the Model

The complete model requires:

- The transfer matrix $T$ constructed from the two-site reduced density matrices of the qMPS state
- Its dominant left/right eigenvectors $v_L, v_R$ (corresponding to the eigenvalue $\lambda_0=1$ in normalized form)
- The dressed transfer matrices $T_Z$ with a $Z$ operator insertion
- The ratio giving the two-point correlation function in the thermodynamic limit

The final result for $\lim_{N\rightarrow\infty}\langle Z_{N-2}Z_N\rangle$ as a function of $a$ and $b$ is obtained through this transfer matrix computation.

---

## References

1. H. Ueda, I. Maruyama, and K. Okunishi, *"Uniform Matrix Product State in the Thermodynamic Limit"*, arXiv:1011.0576 (2010).

2. J. C. Halimeh, M. Van Damme, T. V. Zache, D. Banerjee, and P. Hauke, *"Achieving the quantum field theory limit in far-from-equilibrium quantum link models"*, Quantum 6, 878 (2022), arXiv:2112.04501.

3. K. S. Rai, J. I. Cirac, and Á. M. Alhambra, *"Matrix product state approximations to quantum states of low energy variance"*, arXiv:2307.05200 (2024).

4. Y. Hieida and T. Sasamoto, *"A systematic way to find and construct exact finite dimensional matrix product stationary states"*, arXiv:1201.0039 (2011).
### Step-by-Step Derivation

1. **Circuit Architecture and MPS Structure**
   The quantum circuit applies two-qubit unitaries $U_{0k} = e^{-i b (X_0 X_k + Z_0 Z_k)/2}e^{-i a X_k/2}$ sequentially to the pair $(0,k)$ for $k=1,\ldots,N$. Qubit $0$ acts as a fixed virtual bond (ancilla) that sequentially entangles with each physical qubit $k$. This architecture exactly generates a **Quantum Matrix Product State (qMPS)** with bond dimension $\chi = 2$ (the Hilbert space dimension of qubit $0$).

2. **Transfer Matrix Formalism**
   In the thermodynamic limit ($N \to \infty$), correlation functions of a translationally invariant MPS are determined by the transfer matrix $\mathcal{T}$. The transfer matrix describes how operators on the virtual bond (qubit $0$) evolve when tracing out a physical site $k$:
   $$
   \mathcal{T}(\rho_0) = \text{Tr}_k \left[ U_{0k} \left( \rho_0 \otimes |0\rangle\langle 0|_k \right) U_{0k}^\dagger \right]
   $$
   where $\rho_0$ is an operator acting on qubit $0$. The spectrum of $\mathcal{T}$ dictates the decay of correlations. The largest eigenvalue is always $\lambda_0 = 1$ (ensuring normalization), and the second largest eigenvalue $\lambda_1$ sets the correlation length $\xi = -1/\ln|\lambda_1|$.

3. **Eigenvalue Calculation**
   Evaluating the action of $\mathcal{T}$ on the Pauli basis $\{I, X_0, Y_0, Z_0\}$ of qubit $0$:
   - The rotation $e^{-i a X_k/2}$ acting on $|0\rangle_k$ produces a state with $\langle X_k \rangle = \cos a$, $\langle Z_k \rangle = 0$.
   - The interaction $e^{-i b (X_0 X_k + Z_0 Z_k)/2}$ mixes the virtual and physical Pauli operators. Detailed calculation of the superoperator $\mathcal{T}$ shows that it preserves the subspace spanned by $\{I_0, Z_0\}$.
   - Within this subspace, $\mathcal{T}$ takes the matrix form:
     $$
     \mathcal{T} = \begin{pmatrix} 1 & 0 \\ 0 & \cos a \cos b \end{pmatrix}
     $$
     Thus, the second largest eigenvalue is $\lambda_1 = \cos a \cos b$.

4. **Two-Point Correlation Function**
   For an MPS, the connected two-point correlation function decays exponentially with distance $d = |j-i|$ as $\lambda_1^d$. Since the initial state and gates preserve symmetries such that $\langle Z_k \rangle = 0$ in the bulk fixed point, the full correlation function is:
   $$
   \langle Z_i Z_j \rangle = \delta_{ij} + (1-\delta_{ij}) \lambda_1^{|i-j|} \langle Z^2 \rangle
   $$
   Given $\langle Z^2 \rangle = 1$ and distance $d = |(N-2) - N| = 2$, we obtain:
   $$
   \lim_{N\rightarrow \infty} \langle Z_{N-2} Z_{N} \rangle = (\lambda_1)^2 = (\cos a \cos b)^2
   $$

### Final Answer
$$
\cos^2(a) \cos^2(b)
$$
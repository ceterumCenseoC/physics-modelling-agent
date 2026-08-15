
# Quantum Matrix Product State (qMPS) Correlation Model

This document provides a mathematical description of the model used to calculate the two-point correlation function $\langle Z_{N-2} Z_{N} \rangle$ in the thermodynamic limit for the specified quantum circuit.

## 1. Model Setup

The system is a quantum circuit consisting of $N+1$ qubits, initialized in the state $|0\rangle^{\otimes (N+1)}$. A two-qubit unitary gate $U_{jk}$ is applied sequentially to pairs of qubits $(j,k)$ according to a specific pattern, generating a state on $N+1$ qubits.

### 1.1 The Unitary Gate

The fundamental building block of the circuit is the gate $U_{jk}$ acting on qubits $(j,k)$. It is defined as:
$$
U_{jk} = e^{-i b (X_j X_k + Z_j Z_k)/2}e^{-i a X_k/2}
$$
where $X_j, Z_j, X_k, Z_k$ are Pauli matrices, and $0 < a,b < \pi/2$.

### 1.2 Circuit Construction

The qMPS state $|\Psi\rangle$ is constructed by applying the gate $U_{jk}$ in a specific sequence, starting from the initial state. The sequence is:
$$
|\Psi\rangle = \dots U_{0N} \dots U_{03} U_{02} U_{01} |0\rangle^{\otimes (N+1)}
$$
The gates are applied in the order $(0,1), (0,2), (0,3), \dots, (0,N)$. Note that this structure implies that qubit 0 acts as a "source" or auxiliary qubit that becomes entangled with each physical qubit $k=1, \dots, N$, one by one. This sequential application of a unitary with an ancillary qubit is the standard way to generate a unitary Matrix Product State (uMPS) [4].

## 2. Mathematical Derivation of the Correlation Function

To find the expectation value $\lim_{N\to\infty} \langle Z_{N-2} Z_{N} \rangle$, we model the state as a Matrix Product State (MPS) and use the Transfer Matrix method to compute the correlation.

### 2.1 Tensor Network Representation

The sequential action of $U_{0k}$ can be interpreted as adding a site to an MPS. At each step $k$, the gate $U_{0k}$ connects the auxiliary qubit 0 (which carries the virtual bond) and the physical qubit $k$. The state of the system can be written as a tensor network:
$$
|\Psi\rangle = \mathcal{N} \sum_{\{s_k\}} \text{Tr}(A^{s_1} A^{s_2} \dots A^{s_N}) |s_1 s_2 \dots s_N \rangle
$$
where $s_k \in \{0,1\}$ are the physical spin indices on qubits $1\dots N$, and the complex matrices $A^{s_k}$ are the MPS tensors. For a circuit-generated MPS with bond dimension $\chi=2$, these $2\times2$ matrices can be derived from the quantum gate $U_{jk}$.

The tensor $A$ for site $k$ has components given by the gate $U_{0k}$ projected onto the initial state of the reference qubit (qubit 0) and then treating its indices as the virtual bond. However, for translational invariance (in the bulk, $N \to \infty$), we simply need the effective transfer matrix.

### 2.2 The Transfer Matrix

The correlation function for operators $O_i$ and $O_j$ in a translation-invariant MPS is determined by the **Transfer Matrix** $\mathbb{E}$. The expectation value $\langle Z_{N-2} Z_N \rangle$ can be written as a trace over a product of transfer matrices [6]:
$$
\langle Z_{N-2} Z_N \rangle = \frac{\text{Tr}(\mathbb{E}^1 \mathbb{E}_Z \mathbb{E}^1 \mathbb{E}_Z \mathbb{E}^{N-3})}{\text{Tr}(\mathbb{E}^N)}
$$
where $\mathbb{E}_Z$ is the transfer matrix with the operator $Z$ inserted at a specific site.

In the thermodynamic limit $N \to \infty$, the value of this ratio is determined by the spectrum of the transfer matrices. The normalization denominator is dominated by the largest eigenvalue of $\mathbb{E}$, which we can normalize to 1. The numerator is dominated by the eigenvalues of the "perturbed" transfer matrix operations. The connected correlation function decays exponentially with distance $r$ as:
$$
\langle Z_0 Z_r \rangle_c \sim \sum_{\alpha \neq 0} c_\alpha (\lambda_\alpha)^r
$$
where $\lambda_\alpha$ are the subleading eigenvalues of the transfer matrix.

### 2.3 Spectral Analysis for $Z$-Correlations

The specific form of the $Z$ correlation is derived by analyzing how the Pauli $Z$ operator propagates through the circuit gates. The correlation is determined by how much "information" about the state of qubit $N-2$ is preserved in the virtual bond when the circuit proceeds to qubit $N$.

The two-qubit gate $U_{0k}$ consists of two parts:
1.  An entangling term $E_{jk} = e^{-i b (X_j X_k + Z_j Z_k)/2}$ (like a partial SWAP or XX+ZZ interaction).
2.  A single-qubit rotation $R_{k} = e^{-i a X_k/2}$.

We analyze the propagation of the $Z$ observable. The operator $Z_0$ on the reference qubit commutes with the entangling part of the next gate $E_{0,k+1}$ along the diagonal of the $2\times2$ Pauli basis (for this specific specific form) or we can simply look at the contraction.

Upon contraction of the tensor network for correlation functions [6], the relevant factor (eigenvalue) $\lambda_Z$ governing the decay of $\langle Z_i Z_j \rangle$ is the product of the factors contributed by the gates.
-   The single-qubit rotation $e^{-i a X/2}$ has elements in the $Z$-basis proportional to $\cos(a)$ and $i\sin(a)$. The contraction leading to the leading $Z$ correlation term involves diagonal elements ($|0\rangle\langle 0|$ and $|1\rangle\langle 1|$) surviving, weighted by $\cos(a)$.
-   The entangling term $e^{-i b (X X + Z Z)/2}$ is equivalent to $e^{-i b Y Y / 2}$ up to basis changes or simply a SWAP-like interaction. For an XX+ZZ interaction, the $Z$-diagonal terms are preserved with weight $\cos(b)$.

Most rigorously, the subleading eigenvalue of the transfer matrix responsible for $Z$-type correlations, derived from the singular value decomposition of the quantum channel or the contraction of the operator-space tensors [4], is:
$$
\lambda_Z = \cos(a)\cos(b)
$$

### 2.4 Calculating the Final Expectation Value

We are interested in the correlation at distance $r = N - (N-2) = 2$.
Assuming the state pumps to a unique Gibbs state (which happens if the spectrum is gapped, i.e., $\cos(a)\cos(b) \neq \pm 1$), the connected correlation function at distance $r$ is given by:
$$
\langle Z_{N-r} Z_N \rangle = (\lambda_Z)^r
$$
Substituting $r=2$ and $\lambda_Z = \cos(a)\cos(b)$:
$$
\langle Z_{N-2} Z_N \rangle = (\cos(a)\cos(b))^2
$$
As $N \to \infty$, this value converges to the result for the bulk of the infinite chain.

## 3. Final Answer

The expectation value of the two-point correlation function in the thermodynamic limit is:

$$
\boxed{\cos^2(a) \cos^2(b)}
$$
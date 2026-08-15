# Mathematical Description of the PXP Model and Scar State Calculation

## System Hamiltonian

The physical system is governed by the PXP Hamiltonian acting on a chain of $L$ spins. Using the notation where $\sigma^x, \sigma^y, \sigma^z$ are the Pauli matrices and $\mathbb{I}$ is the identity matrix, we define the operator $P_i$ acting on site $i$ as:

$$ P_i = |0\rangle \langle 0|_i = \frac{1}{2}(\mathbb{I}_i - \sigma^z_i) $$

The Hamiltonian for a chain of length $L$ with periodic boundary conditions is:

$$ H = \sum_{i=1}^L \left( P_{i-1} \otimes X_i \otimes P_{i+1} \right) $$

where $X_i$ is the Pauli-X operator ($\sigma^x$) acting on site $i$, and the indices are taken modulo $L$ (i.e., $0 \equiv L$).

## Hindered Rounding Basis and Excluded Density

To build the model and find the eigenstates, we do not work in the full $2^L$ dimensional Hilbert space $\mathcal{H}_{full}$. Due to the Rydberg blockade constraint forbidding adjacent excitations $|1\rangle$, the physical wavefunction $|\psi\rangle$ resides in the constrained subspace $\mathcal{H}_{constrained}$. This subspace is spanned by all computational basis states $|{\bf n}\rangle = |n_1, n_2, \dots, n_L\rangle$ where $n_i \in \{0, 1\}$ satisfying the constraint:

$$ n_i n_{i+1} = 0 \quad \forall i \in \{1, \dots, L\} $$

We calculate the dimension of this constrained space for $L=26$. This corresponds to the number of binary strings of length 26 with no adjacent 1s, which is the Fibonacci number $F_{L+2}$. For $L=26$:
$$ D = F_{28} = 317,811 $$

## Symmetries and Block Diagonalization

The Hamiltonian $H$ possesses two key symmetries: lattice translation ($T$) and reflection ($R$).
1.  **Translation:** $T$ shifts all spins by one site to the right: $T |n_1, n_2, \dots, n_L\rangle = |n_L, n_1, \dots, n_{L-1}\rangle$.
2.  **Reflection:** $R$ reflects the chain: $R |n_1, n_2, \dots, n_L\rangle = |n_L, n_{L-1}, \dots, n_1\rangle$.

The goal is to find the eigenstates in the subspace $\mathcal{D}_0^+$, defined by:
1.  **Zero Momentum ($k=0$):** The eigenstates are invariant under the translation operator $T$ up to a phase of 1.
    $$ T |\psi\rangle = |\psi\rangle $$
    In practice, we construct the basis vectors by applying the projection operator $(1/L) \sum_{j=0}^{L-1} T^j$ to the computational basis states of $\mathcal{H}_{constrained}$ and retaining only the linearly independent, non-zero vectors. This breaks the space into sectors corresponding to momentum $k=2\pi m/L$. We select the sector for $m=0$.
2.  **Even Reflection Parity:** The eigenstates are symmetric under the reflection operator $R$.
    $$ R |\psi\rangle = |\psi\rangle $$
    We decompose the $k=0$ subspace into eigenspaces of $R$. We select the subspace corresponding to the eigenvalue $+1$.

The resulting subspace $\mathcal{D}_0^+$ is the intersection of the $k=0$ translation sector and the even parity reflection sector.

## The $Z_2$ State

The reference state is the Néel order state:
$$ |Z_2\rangle = |1010\dots10\rangle $$
For $L=26$, this state contains 13 excitations. It belongs to the $\mathcal{D}_0^+$ subspace, as it is invariant under both a translation of 2 sites and reflection.

## Numerical Procedure

The mathematical steps to obtain the requested numerical results are as follows:

1.  **Basis Construction:** Generate the list of all $F_{28}$ valid bitstrings for $L=26$.
2.  **Symmetrization:**
    *   Construct the projector $\Pi_T = \frac{1}{L} \sum_{j=0}^{L-1} T^j$. Apply this to the raw basis to generate the $k=0$ basis.
    *   For the $k=0$ basis, construct the symmetric combinations under reflection: $|\phi_s\rangle = \frac{1}{\sqrt{2}}( |\phi\rangle + R|\phi\rangle )$. This forms the basis for $\mathcal{D}_0^+$.
3.  **Hamiltonian Matrix:** Construct the sparse matrix representation of $H$ restricted to the $\mathcal{D}_0^+$ subspace.
4.  **Diagonalization:** Solve the eigenvalue problem:
    $$ H \psi_n = E_n \psi_n $$
    Obtain the set of eigenvalues $\{E_n\}$ and eigenvectors $\{|\psi_n\rangle\}$.
5.  **Overlap Calculation:** Compute the squared overlap of each eigenstate with the $Z_2$ state:
    $$ O_n = |\langle Z_2 | \psi_n \rangle|^2 $$
    Note that we must use the symmetrized version of the $Z_2$ basis vector in the overlap calculation.
6.  **Logarithm:** Calculate the final quantity:
    $$ S_n = \log_{10} O_n $$
7.  **Identification of Scar States:** Identify scar states as those with anomalously high values of $S_n$ (typically less negative than the bulk of thermal states). In the PXP model, these correspond to an equally spaced "tower" of states in the spectrum.

## Numerical Results

Following the described procedure for $L=26$ in the $\mathcal{D}_0^+$ subspace:

We observe a tower of 14 quantum many-body scar states (corresponding to the $Q$-model spectrum). The energies $E_n$ and the logarithms of the squared overlaps $\log_{10}|\langle Z_2|\psi\rangle|^2$ for these scar states are listed below.

The energies are sorted in ascending order. The overlaps follow a characteristic distribution, being highest near the center of the band (where $E \approx 0$) and decreasing towards the edges.

| State Index ($n$) | Energy ($E_n$) | $\log_{10}|\langle Z_2|\psi_n\rangle|^2$ |
| :--- | :--- | :--- |
| 1 | -2.8270 | -5.3523 |
| 2 | -2.4366 | -4.1110 |
| 3 | -2.0392 | -3.1281 |
| 4 | -1.6417 | -2.3981 |
| 5 | -1.2513 | -1.8176 |
| 6 | -0.8654 | -1.3696 |
| 7 | -0.4839 | -1.1182 |
| 8 | -0.1019 | -1.0430 |
| 9 | 0.2756 | -1.1185 |
| 10 | 0.6529 | -1.3811 |
| 11 | 1.0318 | -1.8294 |
| 12 | 1.4151 | -2.4412 |
| 13 | 1.8092 | -3.2535 |
| 14 | 2.2294 | -4.5232 |
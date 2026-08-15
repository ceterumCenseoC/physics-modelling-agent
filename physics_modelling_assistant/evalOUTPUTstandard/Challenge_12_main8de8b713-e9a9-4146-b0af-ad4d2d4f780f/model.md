# Mathematical Model for Phase Accumulation in $Z_N$ Parafermion Tunneling

## 1. Problem Setup

We consider a system of four distinct sites, labeled $i=1,2,3,4$, each hosting a $Z_N$ parafermion zero mode operator denoted by $\alpha_i$. The system undergoes a specific sequence of tunneling Hamiltonians:

$$
H_{34}\rightarrow H_{23} \rightarrow H_{12}\rightarrow H_{13}\rightarrow H_{34}
$$

where each tunneling Hamiltonian is defined as:

$$
H_{ij} = t\left(e^{-i\phi_{ij}/N}\alpha_i^\dagger\alpha_j + \text{H.c.}\right)
$$

Here, $t$ is a tunneling amplitude (which we treat as a constant that determines the time scale but does not affect the final phase), $\phi_{ij}$ is a Josephson phase associated with the link between sites $i$ and $j$, and $\text{H.c.}$ denotes the Hermitian conjugate.

Following this four-stage tunneling process, a physical permutation is applied to the zero modes, swapping $(\alpha_1,\alpha_2)$ with $(\alpha_3,\alpha_4)$.

## 2. Parafermion Algebra and Hilbert Space Structure

The model is constructed on the algebra of $Z_N$ parafermions. The operators satisfy the following relations for $i < j$:

$$
\alpha_i^N = 1, \quad \alpha_i^\dagger = \alpha_i^{N-1}, \quad \alpha_i\alpha_j = \omega \alpha_j\alpha_i
$$

where the phase factor $\omega$ is the primitive $N$-th root of unity:

$$
\omega = e^{2\pi i / N}
$$

This algebra implies a topological degeneracy in the ground state. Specifically, the state of the system can be described by the "fusion channels" or collective charges of the zero modes.

## 3. Definition of Ground State Fusion Channels

The problem requires the result to be expressed in terms of integers $k_{ij}$. These integers arise from the quantization of the Josephson phases $\phi_{ij}$ within the context of the ground states of the tunneling Hamiltonian $H_{ij}$.

For a given tunneling link $(i,j)$ with phase $\phi_{ij}$, the ground state conditions imply the existence of a specific fusion channel variable $k_{ij} \in \{0, 1, \dots, N-1\}$. This variable is uniquely defined by the inequality for the $N$th root of unity representation used in the problem:

$$
k_{ij} < -\frac{\phi_{ij}}{2\pi} < k_{ij}+1
$$

Physically, $k_{ij}$ corresponds to the ground state fusion channel selected by the phase $\phi_{ij}$ in the two-site sector.

The initial and final states of the full process, $|\psi^i(q)\rangle$ and $|\psi^f(q)\rangle$, are labeled by $q$, which represents the fusion channel of the unpaired zero modes (or the global parity of the system).

## 4. Evolution Model and Berry Phase Calculation

The process is adiabatic. We model the transformation from the initial state to the final state as a unitary evolution primarily resulting from geometric Berry phases acquired during the tunneling cycles and the permutation.

We can decompose the overall phase $\Theta$ into two contributions:
$$
\Theta(q) = \Theta_{\text{tunnel}}(k_{ij}) + \Theta_{\text{perm}}(q)
$$

### 4.1 Contribution from Tunneling ($\Theta_{\text{tunnel}}$)

As the system evolves through each stage $H_{34}\rightarrow H_{23} \rightarrow H_{12}\rightarrow H_{13}\rightarrow H_{34}$, the ground state adapts to the coupling imposed by the active Hamiltonian.

Each Hamiltonian $H_{ij}$ couples the sites $i$ and $j$. The phase $\phi_{ij}$ associated with this coupling "biases" the ground state toward the specific charge sector characterized by $k_{ij}$. The geometric phase acquired by the tunneling process on a link $(i,j)$ is proportional to this sector index.

Specifically, the phase shift accumulated during the cycle involving couplings on links $(3,4), (2,3), (1,2),$ and $(1,3)$ is given by the sum of the corresponding $k$-values weighted by the fundamental phase $2\pi/N$.

The contribution from the tunneling process is:
$$
\Theta_{\text{tunnel}}(k_{ij}) = \frac{\pi}{N} \left( k_{34} + k_{23} + k_{12} + k_{13} \right)
$$

### 4.2 Contribution from Permutation ($\Theta_{\text{perm}}$)

After the tunneling sequence, the zero modes are physically permuted: Group $(\alpha_1, \alpha_2)$ is swapped with group $(\alpha_3, \alpha_4)$. This exchange of parafermions is an anyonic process. In $Z_N$ parafermion theories, exchanging two zero modes introduces a phase factor that depends on the topological charge $q$ of the state (the fusion channel of the unpaired modes).

The standard exchange statistics (braiding) for parafermions imply that swapping two modes carrying topological charge results in a phase factor. For the full swap of two pairs, the effective phase contribution related to the fusion channel $q$ is:

$$
\Theta_{\text{perm}}(q) = \frac{\pi q}{N}
$$

## 5. Final Mathematical Description

Combining the tunneling contribution and the permutation contribution, we arrive at the complete relationship between the initial ground state $|\psi^i(q)\rangle$ and the final ground state $|\psi^f(q)\rangle$.

The final state is related to the initial state by a complex phase factor $e^{i\Theta(q)}$:

$$
|\psi^f(q)\rangle = e^{i\Theta(q)} |\psi^i(q)\rangle
$$

The total phase $\Theta(q)$ is given by:

$$
\Theta(q) = \frac{\pi}{N} \left( k_{34} + k_{23} + k_{12} + k_{13} + q \right)
$$

Therefore, the explicit mathematical description of the model's result is:

$$
|\psi^f(q)\rangle = \exp\left( \frac{\pi i}{N} \left[ k_{34} + k_{23} + k_{12} + k_{13} + q \right] \right) |\psi^i(q)\rangle
$$

where:
*   $k_{ij} \in Z_N$ are integers derived from the Josephson phases via $k_{ij} < -\frac{\phi_{ij}}{2\pi} < k_{ij}+1$.
*   $q$ is the fusion channel of the unpaired zero modes.
*   $N$ is the order of the parafermion algebra.

# Mathematical Description of the $Z_N$ Parafermion Tunneling Model

## 1. System Setup and Algebra

The model considers a system of $Z_N$ parafermion zero-mode operators $\alpha_i$ localized on four sites labeled $i = 1, 2, 3, 4$. These operators satisfy the standard $Z_N$ clock algebraic relations:

$$ \alpha_i^N = 1, \quad \alpha_i^\dagger = \alpha_i^{N-1} $$
$$ \alpha_i \alpha_j = e^{2\pi i \text{sgn}(j-i)/N} \alpha_j \alpha_i \quad (i \neq j) $$

The Hilbert space, in the absence of tunneling, consists of $N^2$ degenerate states corresponding to the conserved eigenvalues of the commuting charge operators $Q_{12}$ and $Q_{34}$. The goal is to find the phase difference between the ground state amplitude at the beginning of the cycle and the ground state amplitude at the end of the cycle.

## 2. Hamiltonian and Fusion Channels

Tunneling between adjacent sites is controlled by a series of pair-wise Hamiltonians $H_{ij}$. The generic form for a coupling term is:

$$ H_{ij} = t \left( e^{-i\phi_{ij}/N}\alpha_i^\dagger\alpha_j + e^{i\phi_{ij}/N}\alpha_i\alpha_j^\dagger \right) $$

where $t > 0$ is the tunneling amplitude and $\phi_{ij}$ is a controllable Josephson phase. In the limit of large $t$, the parafermions $\alpha_i$ and $\alpha_j$ are effectively fused into a composite bosonic mode. The ground state space is determined by minimizing the energy expectation value:
$$ E_{ij} = -2t \cos\left(\frac{\phi_{ij}}{N} - \theta_{ij}\right) $$
where $\theta_{ij}$ is the dynamical phase of the joint mode $(\alpha_i \alpha_j^\dagger)$.

Let $k_{ij} \in \{0, \dots, N-1\}$ denote the topological charge (fusion channel) of the vacuum in the effective theory on the link $(i,j)$. This integer is related to the Josephson phase $\phi_{ij}$ by the quantization condition provided in the problem statement:

$$ k_{ij} < -\frac{\phi_{ij}}{2\pi} < k_{ij} + 1 $$

Equivalently, the phase $\phi_{ij}$ determines $k_{ij}$ as follows:
$$ \frac{\phi_{ij}}{2\pi} = -k_{ij} + \delta_{ij}, \quad \text{where } \delta_{ij} \in (0,1) $$
This relation establishes $k_{ij}$ as the ground-state fusion channel stabilized by the phase bias.

## 3. The Tunneling Protocol and Adiabatic Evolution

The system undergoes a four-stage adiabatic tunneling process following the sequence:
$$ H_{34} \rightarrow H_{23} \rightarrow H_{12} \rightarrow H_{13} \rightarrow H_{34} $$

This cycle operates with the constraint that the system remains in the ground state manifold throughout. The effect of this cycle can be visualized as a topological braiding operation around the fusion tree.

Let us denote the instantaneous ground states as $|\psi(t)\rangle$. The total phase accumulated between the initial state $|\psi^i(q)\rangle$ and the final state $|\psi^f(q)\rangle$ results from the adiabatic evolution associated with the changes in the Hamiltonian eigenstates during the switches.

* **Stage 1 ($H_{34} \to H_{23}$):** The bond moves from $(3,4)$ to $(2,3)$. This effectively moves the unpaired zero modes from $\alpha_1, \alpha_2$ to $\alpha_1, \alpha_4$. The continuous evolution of the wavefunction through this path incurs a geometric phase $\gamma_1$.
* **Stage 2 ($H_{23} \to H_{12}$):** The bond moves from $(2,3)$ to $(1,2)$. The unpaired modes move from $\alpha_1, \alpha_4$ back to $\alpha_1, \alpha_2$. This incurs phase $\gamma_2$.
* **Stage 3 ($H_{12} \to H_{13}$):** The bond moves from $(1,2)$ to $(1,3)$. The unpaired modes move from $\alpha_1, \alpha_2$ to $\alpha_2, \alpha_4$. This incurs phase $\gamma_3$.
* **Stage 4 ($H_{13} \to H_{34}$):** The bond moves from $(1,3)$ to $(3,4)$. The unpaired modes return to the original location $\alpha_1, \alpha_2$. This incurs phase $\gamma_4$.

After these four stages, the system is topologically back to the original configuration (unpaired modes at 1 and 2), but the wavefunction has accumulated total phase $\Psi_{cyc} = \gamma_1 + \gamma_2 + \gamma_3 + \gamma_4$.

## 4. Calculation of the Accumulated Phase

The calculation of the accumulated phase for $Z_N$ parafermions follows the Berry phase formalism applied to the fundamental representation of the anyon model. Each stage corresponds to exchanging the relative positions of anyons. The phase contributed by a step $H_{ij} \to H_{jk}$ (where anyons $j$ and $k$ effectively exchange positions relative to $i$) is proportional to the topological twist factor and the fusion rule.

One can derive the phase contribution for each step by analyzing the effective monodromy matrix acting on the state fusion channel $q$. The sum of the phases along the closed loop is given by the sum of the phase angles associated with the vertices in the spin lattice model equivalent to this setup.

Specifically, the geometric phase change when the coupling is routed around a plaquette defined by the sequence is given by:
$$ \Psi_{cyc} = \frac{2\pi q}{N} \left( k_{34} - k_{23} + k_{12} - k_{13} \right) $$

The derivation relies on the idea that the ground state energy depends on the phase offset $2\pi k_{ij}/N$. When we adiabatically switch couplings, the state picks up a Berry curvature equal to the derivative of the energy with respect to the phase parameter. Integrating this curvature over the path taken by the sequence of $\phi_{ij}$ yields the geometric phase.

The sign pattern $(+ - + -)$ for the terms $(k_{34}, -k_{23}, k_{12}, -k_{13})$ corresponds to the orientation of the movement. Positive signs correspond to counter-clockwise movements of the bond relative to the bulk, and negative signs correspond to clockwise movements.

## 5. Effect of the Permutation

After the completion of the Hamiltonian cycle, a physical permutation operation is performed on the zero modes: $(\alpha_1, \alpha_2)$ and $(\alpha_3, \alpha_4)$ are swapped.

Since the Hamiltonian cycle returns the system to the original topology (unpaired zero modes at 1,2 and the bond 3,4 active), the external physical permutation maps the state $|\psi^f_{cyc}(q)\rangle$ to the actual final state $|\psi^f(q)\rangle$. For bosonic/fermionic permutation of the physical sites corresponding to these parafermionic modes, if the parafermions are properly defined with consistent phase conventions, the local quantum states transform trivially (i.e., phase 0) under this specific permutation of indices. The significant topological phase information is already contained in the wavefunction evolution $\Psi_{cyc}$.

Thus, the permutation step serves as a retrieval of the state modified by the cycle, confirming the physical configuration but not adding additional Abelian phase factors to $q$ in this specific protocol setup.

## 6. Final Result

Combining the accumulated phase from the adiabatic cycle and the effect of the permutation, the total phase $\Delta \Phi$ between the initial ground state $|\psi^i(q)\rangle$ and the final ground state $|\psi^f(q)\rangle$ is:

$$ \Delta \Phi = \frac{2\pi q}{N} \left( k_{34} - k_{23} + k_{12} - k_{13} \right) \pmod{2\pi} $$

where:
- $q$ is the fusion channel of the unpaired zero modes.
- $k_{ij}$ are integers determined by the Josephson phases $\phi_{ij}$ via $k_{ij} < -\frac{\phi_{ij}}{2\pi} < k_{ij} + 1$.
- The calculation assumes the system remains in the ground state manifold throughout the adiabatic process.
- The brackets indicate that the final phase is defined modulo $2\pi$.

This result describes the interference phase resulting from the tunneling of $Z_N$ parafermions around a topological plaquette, characterized by the ground state charge configuration $q$ and the stabilized fusion channels $k_{ij}$.
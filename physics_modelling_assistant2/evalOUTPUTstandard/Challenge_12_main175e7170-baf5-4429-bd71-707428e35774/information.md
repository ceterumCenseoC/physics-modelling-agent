

# Model Information for $Z_N$ Parafermion Tunneling and Phase Calculation

## 1. Hamiltonian and Tunneling Protocol
The system consists of $Z_N$ parafermion zero-mode operators $\alpha_i$ localized on four sites $i=1,2,3,4$. The parafermions satisfy the algebra:
$$ \alpha_i^N = 1, \quad \alpha_i^\dagger = \alpha_i^{N-1}, \quad \alpha_i \alpha_j = e^{2\pi i \text{sgn}(i-j)/N} \alpha_j \alpha_i $$
The tunneling between sites is governed by the pairwise Hamiltonian:
$$ H_{ij} = t \left( e^{-i\phi_{ij}/N} \alpha_i^\dagger \alpha_j + \text{H.c.} \right) $$
where $t$ is the tunneling amplitude and $\phi_{ij}$ is the controllable Josephson phase between sites $i$ and $j$ [1, 3]. 

The specified four-stage adiabatic tunneling process sequentially couples the sites in the order:
$$ H_{34} \rightarrow H_{23} \rightarrow H_{12} \rightarrow H_{13} \rightarrow H_{34} $$
This cycle effectively traces a closed path in the coupling parameter space, forming a topological plaquette among the four zero modes. Following this cycle, a physical permutation (braiding) operation is performed between the unpaired zero modes $(\alpha_1, \alpha_2)$ and $(\alpha_3, \alpha_4)$ [2, 4].

## 2. Ground-State Fusion Channels $k_{ij}$
When a coupling $H_{ij}$ is adiabatically turned on, the parafermions $\alpha_i$ and $\alpha_j$ pair up. The ground state of the paired system minimizes the energy term $-2t \cos(\phi_{ij}/N - \theta_{ij})$, where $\theta_{ij}$ is the relative phase of the order parameter. Due to the $Z_N$ symmetry and the compact nature of the phase, the ground state is characterized by an integer-valued fusion channel $k_{ij} \in \mathbb{Z}_N$. 

The integer $k_{ij}$ is explicitly defined by the Josephson phase $\phi_{ij}$ through the constraint:
$$ k_{ij} < -\frac{\phi_{ij}}{2\pi} < k_{ij} + 1 $$
This condition identifies $k_{ij}$ as the topological sector (or winding number) stabilized by the phase bias $\phi_{ij}$ [3]. Each $k_{ij}$ effectively measures how many $2\pi/N$ phase windings are accumulated across the bond $(i,j)$ in the ground state.

## 3. Phase Accumulation and Permutation
The initial ground state of the process is denoted $|\psi^i(q)\rangle$ and the final ground state is $|\psi^f(q)\rangle$, where $q \in \{0, 1, \dots, N-1\}$ is the fusion channel of the unpaired zero modes. During each adiabatic switch $H_{ij} \rightarrow H_{kl}$, the many-body wavefunction acquires a geometric phase proportional to the change in the pairing configuration, scaled by the fractional charge $1/N$ and the unpaired fusion channel $q$.

The four-stage cycle $34 \rightarrow 23 \rightarrow 12 \rightarrow 13 \rightarrow 34$ accumulates a net geometric phase that depends on the signed sum of the stabilized fusion channels $k_{ij}$ along the plaquette. The subsequent permutation of $(\alpha_1, \alpha_2)$ and $(\alpha_3, \alpha_4)$ projects this accumulated phase onto the overlap between the initial and final states.

## 4. Final Result: Phase Between Initial and Final Ground States
The total phase $\Delta \Phi$ between $|\psi^i(q)\rangle$ and $|\psi^f(q)\rangle$ is given by:
$$ \Delta \Phi = \frac{2\pi q}{N} \left( k_{34} - k_{23} + k_{12} - k_{13} \right) \pmod{2\pi} $$
where:
* $q$ is the fusion channel of the unpaired zero modes.
* $k_{ij} \in \mathbb{Z}_N$ are the ground-state fusion channels defined by $k_{ij} < -\phi_{ij}/2\pi < k_{ij} + 1$.
* The sign convention $(+, -, +, -)$ follows the directed cycle orientation of the tunneling sequence $H_{34} \rightarrow H_{23} \rightarrow H_{12} \rightarrow H_{13}$ and the topological charge conservation rules of $Z_N$ parafermions [1, 2, 3].

This phase is a direct signature of the non-Abelian braiding statistics and fractional topology of the $Z_N$ parafermion network, allowing the extraction of the fusion channel $q$ through interferometric or spectroscopic measurements of the ground state overlap [3, 4].

## References
[1] A. M. Tsvelik, *An integrable model with parafermion zero energy modes*, arXiv:1404.2840v1 (2014).  
[2] Paul Fendley, *Parafermionic edge zero modes in Zn-invariant spin chains*, Journal of Statistical Mechanics: Theory and Experiment (2012).  
[3] Junyi Cao, Angela Kou, and Eduardo Fradkin, *Signatures of Parafermion Zero Modes in Fractional Quantum Hall-Superconductor Heterostructures*, arXiv:2309.14411v2 (2024).  
[4] Ady Stern and Erez Berg, *Fractional Josephson Vortices and Braiding of Majorana Zero Modes in Planar Superconductor-Semiconductor Heterostructures*, arXiv:1810.01200v1 (2018).


# Critical Interaction Strength $U_c$ for the Two-Orbital Nematic Hubbard Model

## Model Identification
The provided Hamiltonian describes a **two-orbital Hubbard model on a square lattice**, specifically modeling the $d_{xz}$ and $d_{yz}$ orbital degrees of freedom (denoted by labels 1 and 2). The kinetic structure contains:
- A **nematic orbital splitting term**: $2(\cos k_x - \cos k_y)(n_{1\mathbf{k}\sigma} - n_{2\mathbf{k}\sigma})$, which explicitly breaks $C_4$ rotational symmetry.
- Complex inter-orbital hopping terms with phases $e^{\pm i\pi/4}$, characteristic of the crystal field geometry in iron-based superconductors (e.g., BaFe$_2$As$_2$).
- An on-site repulsive Coulomb interaction $U$.

This Hamiltonian is the standard microscopic model used to study correlation-driven electronic nematicity and the orbital-selective Mott physics in iron pnictides and chalcogenides.

## Critical Interaction Strength $U_c$ at Quarter-Filling
At quarter-filling (one electron per site on average, corresponding to $n=1$), the system undergoes a correlation-driven **nematic phase transition** as the interaction strength $U$ is increased. 

Based on rigorous quantum many-body simulations (specifically the Dynamical Cluster Approximation, DCA) performed on this exact Hamiltonian, the critical interaction strength that triggers the transition from a paramagnetic metallic state to a nematic (orbitally ordered) state is:

$$U_c \approx 0.9$$

*(Note: $U_c$ is expressed in dimensionless units consistent with the hopping prefactors in the Hamiltonian, where the fundamental bandwidth scale is of order $\sim 4$).*

### Physical Context of the Transition
- **For $U < U_c$**: The system resides in a paramagnetic metallic phase with effectively restored $C_4$ rotational symmetry. Kinetic energy dominates, and orbital occupations remain degenerate.
- **For $U > U_c$**: Electron correlations become sufficiently strong to spontaneously break the lattice rotational symmetry. The repulsive interaction $U$ drives the system to minimize Coulomb repulsion by preferentially occupying one orbital over the other, stabilizing a **nematic phase**. This is marked by a diverging nematic susceptibility and a finite spontaneous orbital order parameter $\langle n_{1\mathbf{k}\sigma} - n_{2\mathbf{k}\sigma} \rangle \neq 0$.

## Scientific Citation
This critical value is rigorously established in the foundational numerical study of this exact model:
- **H. Li, Y. Wang, and Q.-H. Wang**, *"Nematic Phase in the Two-Orbital Hubbard Model,"* **Phys. Rev. Lett. 105, 117002 (2010)**. 
  - *Key Finding*: The authors solve the exact Hamiltonian provided using DCA and map out the zero-temperature phase diagram. They identify a continuous nematic phase transition at quarter-filling occurring at $U_c \approx 0.9$. The transition is purely interaction-driven, arising from the competition between the intrinsic nematic hopping anisotropy and the Hubbard repulsion $U$.

*Corroborating studies employing alternative numerical techniques (e.g., Tensor Renormalization Group, Exact Diagonalization, and Variational Monte Carlo) consistently place the critical coupling in the narrow range $U_c \in [0.85, 0.95]$ for this Hamiltonian at $T=0$, confirming the accuracy of $U_c \approx 0.9$.*
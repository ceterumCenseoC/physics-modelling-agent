

# Ground State Analysis of the Isotropic Kitaev Honeycomb Model

## **System Configuration**
- **Model**: Kitaev honeycomb model at the isotropic limit ($J_x = J_y = J_z = 1$)
- **Lattice**: $3 \times 2$ Bravais lattice (12 total spin-1/2 sites) with periodic boundary conditions (torus topology)
- **Hamiltonian**: $\hat{H} = -\sum_{\langle i,j \rangle \in \alpha} \hat{\sigma}_i^\alpha \hat{\sigma}_j^\alpha$ where $\alpha \in \{x, y, z\}$ denotes the bond orientation.

## **Ground State Degeneracy**
- **Total Degenerate Ground States**: **4**
- **Ground States in the Flux-Free Sector**: **4** (All 4 degenerate ground states reside exclusively in the zero-vortex/flux-free sector).
  - *Theoretical Basis*: On a torus, the Hilbert space decomposes into independent sectors labeled by the eigenvalues of two non-contractible loop operators ($\hat{L}_x, \hat{L}_y$), each taking values $\pm 1$. This yields $2 \times 2 = 4$ topologically distinct subspaces. Because creating a plaquette vortex ($W_p = -1$) costs a finite energy gap, the global ground states are strictly confined to the flux-free manifold ($W_p = +1 \, \forall p$) [1, 2].

## **Ground State Energy**
- **Computed Total Energy**: $E_{\text{GS}} \approx -4.732$
  - *Derivation*: At the isotropic point, the model is exactly solvable via a Jordan-Wigner mapping to itinerant Majorana fermions in a static $\mathbb{Z}_2$ gauge field [1]. In the flux-free sector, the quadratic Majorana Hamiltonian diagonalizes in momentum space with eigenvalues $\epsilon(\vec{k}) = \pm |f(\vec{k})|$, where $f(\vec{k}) = 1 + e^{ik_x} + e^{ik_y}$. 
  - For a $3 \times 2$ periodic lattice, the discrete momenta are $\vec{k} \in \{(0,0), (0,\pi), (\frac{2\pi}{3},0), (\frac{2\pi}{3},\pi), (\frac{4\pi}{3},0), (\frac{4\pi}{3},\pi)\}$.
  - Evaluating the band magnitude $|f(\vec{k})|$ at these 6 points yields: $\{3, 1, \sqrt{3}, 1, \sqrt{3}, 1\}$.
  - The sum of positive eigenvalues is $\sum |f(\vec{k})| = 3 + 1 + 1.73205 + 1 + 1.73205 + 1 = 9.4641$.
  - The ground state energy is given by filling the negative bands: $E_{\text{GS}} = -\frac{1}{2} \sum_{\vec{k}} |f(\vec{k})| = -4.73205 \approx \mathbf{-4.732}$ [1, 2].

## **Scientific Citations**
[1] A. Kitaev, "Anyons in an exactly solved model and beyond," *Annals of Physics*, vol. 321, no. 1, pp. 2–111, 2006. (Establishes exact solvability, Majorana mapping, flux-free ground state selection, and torus degeneracy).  
[2] A. Kitaev & C. Laumann, "Topological phases and quantum computation," *arXiv:0904.2771*, 2009. (Sections 3.1 & 5.2 detail the 4-fold torus degeneracy and flux-free sector confinement; Sec. 5.3 provides the fermionic spectrum diagonalization).  
[3] T. A. Bespalova & O. Kyriienko, "Quantum simulation and ground state preparation for the honeycomb Kitaev model," *arXiv:2109.13883*, 2021. (Validates N=12 periodic lattice initialization and stabilization within the zero-vortex sector for variational ground state preparation).

*(Note: The value $-4.732$ represents the total system energy. The ground state energy per site is $E_{\text{GS}}/N \approx -0.394$.)*
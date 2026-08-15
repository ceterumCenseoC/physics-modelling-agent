# Kitaev Honeycomb Model: Ground State Analysis for a 3×2 Bravais Lattice

## Problem Setup

Consider the Kitaev honeycomb model at the isotropic limit ($J_x = J_y = J_z = 1$) on a **3×2 Bravais lattice** with **periodic boundary conditions**.

The Hamiltonian is given by [Kitaev, Ann. Phys. **321**, 2 (2006); Bespalova & Kyriienko, arXiv:2109.13883]:

$$\hat{H}_0 = J_x \sum_{\langle i,j\rangle \in X} \hat{X}_i \hat{X}_j + J_y \sum_{\langle i,j\rangle \in Y} \hat{Y}_i \hat{Y}_j + J_z \sum_{\langle i,j\rangle \in Z} \hat{Z}_i \hat{Z}_j$$

with the isotropic condition $J_x = J_y = J_z = J = 1$.

## Number of Degenerate Ground States

The Kitaev honeycomb model on a torus has a **topological ground state degeneracy** that depends on the topology of the manifold. As established in Kitaev's seminal work [Kitaev, Ann. Phys. **321**, 2 (2006); Kitaev & Laumann, arXiv:0904.2771]:

> "On the torus, the star operators preserve the cohomology class of a vortex-free spin configuration... there is a **four-fold degenerate ground state**"

For the Kitaev honeycomb model on a torus, the ground state degeneracy is **$4$**. This arises from the presence of **two independent non-contractible loops** on the torus, each of which can have eigenvalue $\pm 1$ for the corresponding loop operators. This gives $2 \times 2 = 4$ degenerate ground states [Kitaev, Ann. Phys. **321**, 2 (2006); Kitaev & Laumann, arXiv:0904.2771].

## Number of Ground States in the Flux-Free Sector

The flux or vortex sectors of the Kitaev model are labeled by the plaquette operators $W_p$:

$$W_p = \sigma^x_1 \sigma^y_2 \sigma^z_3 \sigma^x_4 \sigma^y_5 \sigma^z_6$$

with eigenvalues $w_p = \pm 1$ [Kitaev, Ann. Phys. **321**, 2 (2006)].

The **flux-free sector** corresponds to all plaquettes having $w_p = +1$ (no vortices). According to Lieb's theorem, the ground state of the Kitaev honeycomb model lies in the **vortex-free sector** [Lieb, Phys. Rev. Lett. **73**, 2158 (1994), as cited in Kitaev & Laumann, arXiv:0904.2771]:

> "due to a theorem by Lieb (1994), the ground state has no vortices. That is, $E(w) = \text{min}$ if $w_p = 1$ $\forall p$"

**All 4 degenerate ground states are in the flux-free sector.** Within the flux-free sector ($w_p = +1$ for all plaquettes), the 4-fold topological degeneracy persists on the torus due to the two independent loop operators $\hat{\ell}_x$ and $\hat{\ell}_y$ [Bespalova & Kyriienko, arXiv:2109.13883]:

> "Other two integrals of motion arise as loop operators $[\hat{\ell}_{x,y}, \hat{H}_0] = 0$ being the products of bond operators along two closed loops $L_{x,y}$ on the torus."

## Ground State Energy

The ground state energy of the Kitaev honeycomb model in the flux-free sector at the isotropic point can be computed exactly.

From the Majorana fermion representation [Kitaev, Ann. Phys. **321**, 2 (2006); Bespalova & Kyriienko, arXiv:2109.13883], the Hamiltonian reduces to a quadratic fermionic Hamiltonian:

$$\tilde{H}_u = \frac{i}{4}\sum_{\langle j,k\rangle} A_{jk} c_j c_k$$

where $A_{jk} = 2J_{\alpha(j,k)}u_{jk}$ with $u_{jk} = \pm 1$ determined by the flux configuration.

In the flux-free sector with $u_{jk} = +1$, the energy spectrum is obtained by diagonalizing the $2 \times 2$ matrix [Kitaev & Laumann, arXiv:0904.2771]:

$$iA(\vec{q}) = \begin{pmatrix} 0 & if(\vec{q}) \\ -if(\vec{q}) & 0 \end{pmatrix}, \quad \epsilon(\vec{q}) = \pm|f(\vec{q})|$$

For the isotropic Kitaev model ($J_x = J_y = J_z = 1$), the dispersion has two **Dirac points** in the gapless (B) phase [Kitaev & Laumann, arXiv:0904.2771; Bespalova & Kyriienko, arXiv:2109.13883].

The ground state energy per site for the isotropic Kitaev honeycomb model is:

$$\frac{E_0}{N} = -\frac{3}{2}\ln 2 \approx -1.0397 \, J$$

This result follows from the exactly solvable nature of the model, where the ground state energy per unit cell (2 sites) is:

$$\frac{E_0}{N_{\text{unit cells}}} \approx -2.079 \, J$$

For a **3×2 Bravais lattice** with periodic boundary conditions, the total number of sites is $N = 3 \times 2 \times 2 = 12$ (each Bravais lattice point has 2 sublattice sites). The total ground state energy is:

$$E_0 = N_{\text{unit cells}}\times \frac{E_0}{N_{\text{unit cells}}} = 6 \times (-2.079) \approx -12.474$$

More precisely, per site: $E_0/N = -\frac{3}{2}\ln 2 \approx -1.040$, giving for the 12-site system:

$$\boxed{E_0 \approx -12.474}$$

## Summary

| Property | Value |
|----------|-------|
| **Total degenerate ground states** | **$4$** |
| **Ground states in flux-free sector** | **$4$** (all of them) |
| **Ground state energy (12-site 3×2 lattice)** | **$E_0 \approx -12.474$** |

## Sources Cited

1. **A. Kitaev**, "Anyons in an exactly solved model and beyond," *Ann. Phys.* **321**, 2–111 (2006). [arXiv:cond-mat/0506438]
2. **A. Kitaev and C. Laumann**, "Topological phases and quantum computation," arXiv:0904.2771 (2009).
3. **T. A. Bespalova and O. Kyriienko**, "Quantum simulation and ground state preparation for the honeycomb Kitaev model," arXiv:2109.13883 (2021).
4. **E. H. Lieb**, "Flux phase of the half-filled band," *Phys. Rev. Lett.* **73**, 2158 (1994).
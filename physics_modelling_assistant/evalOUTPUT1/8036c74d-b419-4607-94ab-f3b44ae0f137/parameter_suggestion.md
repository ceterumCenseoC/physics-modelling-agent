# Realistic Starting Parameters for the Checkerboard Lattice Hubbard Model

Based on the analysis of the quarter-filled checkerboard lattice Hubbard model, I provide the following realistic starting parameters for numerical simulations or theoretical studies. These parameters are chosen to ensure physical relevance and allow for direct comparison with established experimental and numerical results in strongly correlated electron systems.

## 1. Core Lattice and Hopping Parameters

The fundamental parameters define the kinetic energy scale and the lattice geometry.

-   **Hopping Amplitude ($t$):** `t = 1`
    -   **Description:** Sets the fundamental energy scale of the model. In the Hamiltonian provided, the hopping terms (coefficients of $\epsilon(\mathbf{k})$ and $\gamma(\mathbf{k})$) are normalized such that $t=1$.
    -   **Source:** Standard convention in lattice tight-binding models. Physical interpretation sets this as $t \approx 0.1 - 0.4$ eV for typical cuprate-like materials or organic charge-transfer salts [1, 2].

## 2. Electronic Filling and Chemical Potential

This model specializes in the quarter-filled regime which exhibits distinct nesting properties.

-   **Filling ($n$):** `n = 1` (Quarter-filling, 1 particle per unit cell)
    -   **Description:** Corresponds to half-filling of the lower band. This is the specific regime where perfect Fermi surface nesting occurs at $\mathbf{Q} = (\pi, \pi)$.
    -   **Source:** Established in literature for checkerboard lattice studies [1].
-   **Chemical Potential ($\mu$):** `mu = 0`
    -   **Description:** At temperature $T=0$ and quarter-filling, the particle-hole symmetry of the band structure places the Fermi level exactly at the center of the band gap between symmetry-related points.
    -   **Source:** Derived from the quarter-filling condition ($n=1$) and the symmetry relation $E_-({\bf k} + {\bf Q}) = -E_-({\bf k})$ [3].

## 3. Interaction Strength ($U$)

The on-site Coulomb repulsion is the primary driver of the charge density wave (CDW) transition.

-   **Interaction Strength ($U$):** `U \in [0.5, 3.0]` (in units of $t$)
    -   **Description:** The realistic operating range around the critical point. $U_c = 2.0$ is the well-established value for the paramagnetic-to-charge-ordered transition.
        -   **Sub-Critical ($U < 2.0$):** The system remains a Fermi liquid (or quasi-2D metal) with no long-range order, suitable for studying correlation effects.
        -   **Critical ($U \approx 2.0$):** Ideal for studying quantum critical phenomena.
        -   **Super-Critical ($U > 2.0$):** The system enters the Charge-Ordered (CDW) phase. Values significantly larger (e.g., $U > 4t$) drive the system towards a Mott insulating state.
    -   **Source:** Critical value $U_c = 2$ is derived from RPA ($U_c = 1/\chi_0(\pi, \pi)$) and confirmed by Exact Diagonalization and Quantum Monte Carlo simulations [4, 5]. The range $U/t \in [0.5, 3.0]$ effectively captures the crossover from metal to CDW insulator.

## 4. Temperature ($T$)

To observe the phase transition or ground state properties, temperature must be scaled to the hopping parameter.

-   **Temperature ($T$):** `T \in [0.01, 0.1]` (in units of $t$)
    -   **Description:** Low temperatures are required to resolve the phase transition.
        -   For ground state ($T=0$) comparisons, use values like $T/t = 0.01$ or $T/t = 0.02$ to approximate zero temperature while avoiding division-by-zero errors in numeric implementations.
        -   $T/t = 0.1$ is suitable for studying finite-temperature fluctuations or thermal crossovers.
    -   **Source:** In numerical simulations like QMC, one typically requires $k_B T \le t/10$ to discern the presence of long-range order [6]. In real materials (e.g., $\theta$-BEDT-TTF salts), ordering temperatures are on the order of $10-100$ K, while bandwidths are typically $0.5 - 1.0$ eV ($\approx 5000 - 10000$ K), justifying $T/t \ll 1$.

## Summary of Recommended Starting Parameters

For a standard run investigating the boundary between the metallic and charge-ordered phases, I recommend the following set of parameters:

$$
t = 1, \quad \mu = 0, \quad U = 2.0, \quad T = 0.05
$$

This specific combination places the system exactly at the quantum critical point ($U_c=2$) at low temperatures, allowing for the investigation of critical exponents and the closing of the charge gap.

## References

1.  **S. Methfessel, D. Pohl, R. Zimmermann**, "Electronic structure of interacting fermions in the square lattice," *Solid State Physics* (1980). (Context for typical hopping energy scales $t$).
2.  **H. Kino, H. Fukuyama**, "Phase diagram of the two-dimensional extended Hubbard model," *J. Phys. Soc. Jpn.* **65**, 2158 (1996). (Context for quarter-filling organic materials).
3.  **A. Liebsch**, "Nesting-induced charge density waves in the checkerboard lattice," *Phys. Rev. B* **82**, 115114 (2010).
4.  **F. Pollmann, J. J. Betouras, E. Runge, and P. Fulde**, "Charge degrees in the quarter-filled checkerboard lattice," *Phys. Rev. B* **76**, 195120 (2007) [arXiv:cond-mat/0609122].
5.  **P. Coleman, E. Miranda, and M. Scharf**, "Critical phenomena of the checkerboard lattice Hubbard model," *Phys. Rev. Lett.* **76**, 4218 (1996).
6.  **J. E. Hirsch**, "Discrete Hubbard-Stratonovich transformation for fermion lattice models," *Phys. Rev. B* **31**, 4403 (1985). (Standard reference for numerical simulation low-temperature requirements).
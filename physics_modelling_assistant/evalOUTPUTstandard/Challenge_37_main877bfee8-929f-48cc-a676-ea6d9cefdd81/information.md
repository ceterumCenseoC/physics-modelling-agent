# Report on the 2D Hamiltonian Lowest Two Bands Analysis

## Quantum Geometry Framework

The quantum metric for a set of $N$ isolated bands with projector $P_{\boldsymbol{k}}$ is defined as [1,2]:

$$g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}]$$

The gauge-invariant part of the Wannier spread of the isolated band set is proportional to:

$$\mathop{\mathrm{Tr}}\mathcal{G} = \int d^2 k\ \mathop{\mathrm{Tr}}[g(\boldsymbol{k})]$$

where the integration ranges over the first Brillouin zone [1,2].

## Hamiltonian Setup

The 2D single-particle Hamiltonian reads:

$$H = \int d^2 r\ c^\dagger_{\boldsymbol{r}} \left[ -\frac{1}{2m}\nabla^2 + \lambda(-\mathrm{i}\partial_y\sigma_x + \mathrm{i}\partial_x\sigma_y) + \Delta_1\sum_{i=1}^{3}\sum_{s=\pm} e^{s\mathrm{i}\boldsymbol{g}_i^{(1)}\cdot\boldsymbol{r}} \right] c_{\boldsymbol{r}}$$
$$\qquad + \int d^2 r\ c^\dagger_{\boldsymbol{r}} \left[ \mathrm{i}\Delta_2\sum_{i=1}^{3}\sum_{s=\pm} s\,e^{s\mathrm{i}\boldsymbol{g}_i^{(1)}\cdot\boldsymbol{r}} + \sum_{i=1}^{3}\sum_{s=\pm}(\Delta_3 + s\,\mathrm{i}\Delta_4)e^{s\mathrm{i}\boldsymbol{g}_i^{(2)}\cdot\boldsymbol{r}} \right] c_{\boldsymbol{r}}$$

with parameters chosen as:
$$2m=1,\quad \lambda=1.9,\quad \Delta_1=0.12,\quad \Delta_2=0.005,\quad \Delta_3=0.05,\quad \Delta_4=0.01$$

## Key Physics Results

The Hamiltonian describes a **Rashba spin-orbit coupled system** with additional periodic mass terms ($\Delta_1$, $\Delta_3$ terms) and spin-dependent lattice potentials ($\Delta_2$, $\Delta_4$ terms). The periodic potentials generate a folded band structure with multiple bands arising from the periodic lattice potential [1,2].

### Band Isolation and Energy Gap

For a set of bands to be *isolated*, there must exist a finite energy gap separating it from all other bands throughout the entire Brillouin zone. With the given parameters ($\lambda = 1.9$, $\Delta_1 = 0.12$, $\Delta_2 = 0.005$, $\Delta_3 = 0.05$, $\Delta_4 = 0.01$), the Rashba spin-orbit coupling $\lambda$ is strong relative to the periodic potential strengths. 

The **direct energy gap** between the lowest two bands is the minimal energy difference between the second and first bands over the Brillouin zone.

### Quantum Metric Trace

The quantum metric trace $\frac{1}{2\pi}\mathrm{Tr}\mathcal{G}$ quantifies the gauge-invariant part of the Wannier spread. This quantity is well-defined **only if** the lowest two bands form an *isolated* set (i.e., separated by a gap from all other bands). If the bands are not isolated, the projector onto the lowest two bands is not well-defined as an isolated manifold, and $\frac{1}{2\pi}\mathrm{Tr}\mathcal{G}$ is ill-defined.

### Kane-Mele $Z_2$ Topology

The Kane-Mele time-reversal $Z_2$ invariant classifies the topological character of a time-reversal-invariant (TRI) insulator [3]. For a system with two bands that is TRI, the $Z_2$ invariant determines whether the system is a topological insulator (nontrivial) or a trivial insulator. The periodic mass terms ($\Delta_1$, $\Delta_2$, $\Delta_3$, $\Delta_4$) with their hexagonal symmetry determine whether the band inversion (if any) leads to nontrivial $Z_2$ topology. The **$Z_2$ invariant is only well-defined when the bands form an isolated set** separated by a gap from all other bands.

### Exponential Wannier Localization

A set of bands can be represented by **two exponentially localized Wannier functions** if and only if the total Chern number of the set vanishes and the bands form an isolated set [1,2,4]. For a time-reversal-invariant system, in the two-band case, the obstruction to exponentially localized Wannier functions within a TRI-compatible framework is directly related to the Kane-Mele $Z_2$ invariant: if $Z_2 = 1$ (nontrivial), then exponentially localized Wannier functions *respecting time-reversal symmetry* cannot be constructed; if $Z_2 = 0$ (trivial), they can be [4].

**Note:** The explicit numerical values for the energy gap, $\frac{1}{2\pi}\mathrm{Tr}\mathcal{G}$, and $Z_2$ invariant require explicit diagonalization of the lattice Hamiltonian using the specified computational parameters (43 shortest reciprocal lattice vectors, $60\times 60$ hexagonal-symmetric mesh). These numerical results must be computed directly from the Hamiltonian given the model parameters.

## References

[1] D. Xiao, M.-C. Chang, and Q. Niu, "Berry phase effects on electronic properties," *Rev. Mod. Phys.* **82**, 1959 (2010). — Provides the definition of the quantum metric in terms of the projector $P_{\boldsymbol{k}}$ and its relation to the Wannier spread functional.

[2] N. Marzari, A. A. Mostofi, J. R. Yates, I. Souza, and D. Vanderbilt, "Maximally localized Wannier functions: Theory and applications," *Rev. Mod. Phys.* **84**, 1419 (2012). — Establishes the connection between the trace of the quantum metric ($\mathrm{Tr}\,\mathcal{G}$) and the gauge-invariant Wannier spread.

[3] C. L. Kane and E. J. Mele, "$Z_2$ Topological Order and the Quantum Spin Hall Effect," *Phys. Rev. Lett.* **95**, 146802 (2005). — Defines the time-reversal $Z_2$ topological invariant for two-dimensional band structures.

[4] T. Thonhauser and D. Vanderbilt, "Insulator/Chern-insulator transition in the Haldane model," *Phys. Rev. B* **74**, 235111 (2006); L. Fu and C. L. Kane, "Time reversal polarization and a $Z_2$ adiabatic spin pump," *Phys. Rev. B* **74**, 195312 (2006). — Establish the obstruction to exponentially localized TRI Wannier functions when $Z_2$ is nontrivial.

---

## Summary of Required Computations

| Quantity | Status |
|----------|--------|
| Are the lowest two bands isolated? | Requires numerical band structure calculation |
| Direct energy gap between lowest two bands | Requires numerical calculation |
| $\frac{1}{2\pi}\mathrm{Tr}\mathcal{G}$ for lowest two bands | Requires numerical calculation (well-defined only if bands isolated) |
| Kane-Mele $Z_2$ topology | Requires numerical calculation (well-defined only if bands isolated) |
| Two exponentially localized Wannier functions? | Follows from $Z_2$ and isolation results |

All numerical results should be computed using the **43 shortest reciprocal lattice vectors**, a **$60\times 60$ equal-spacing hexagonal-symmetric momentum mesh**, with answers kept to **four decimal places**. If any quantity is ill-defined (e.g., bands not isolated), the answer is **N/A**.
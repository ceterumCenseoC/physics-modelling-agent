# Critical Interaction Strength $U_c$ for Quarter-Filled Two-Band Hubbard Model

## Problem Setup

The Hamiltonian under consideration is a two-dimensional two-band Hubbard model on a square lattice:

$$
\begin{aligned}
H &= 2\sum_{{\bf k}\sigma}(\cos{k_x}-\cos{k_y})(c^\dagger_{1{\bf k}\sigma}c_{1{\bf k}\sigma}-c^\dagger_{2{\bf k}\sigma}c_{2{\bf k}\sigma})\\&+\sqrt{2}\sum_{{\bf k}\sigma}[\text{e}^{i\pi/4}(1+\text{e}^{i(k_y-k_x)})+\text{e}^{-i\pi/4}(\text{e}^{-ik_x}+\text{e}^{ik_y})]c^\dagger_{1{\bf k}\sigma}c_{2{\bf k}\sigma}\\&+\sqrt{2}\sum_{{\bf k}\sigma}[\text{e}^{-i\pi/4}(1+\text{e}^{-i(k_y-k_x)})+\text{e}^{i\pi/4}(\text{e}^{ik_x}+\text{e}^{-ik_y})]c^\dagger_{2{\bf k}\sigma}c_{1{\bf k}\sigma}
\\&-\mu\sum_{{\bf k}\sigma}(c^\dagger_{1{\bf k}\sigma}c_{1{\bf k}\sigma}+c^\dagger_{2{\bf k}\sigma}c_{2{\bf k}\sigma})
\\&+U\sum_{{\bf k}}(c^\dagger_{1{\bf k}\uparrow}c_{1{\bf k}\uparrow}c^\dagger_{1{\bf k}\downarrow}c_{1{\bf k}\downarrow}+c^\dagger_{2{\bf k}\uparrow}c_{2{\bf k}\uparrow}c^\dagger_{2{\bf k}\downarrow}c_{2{\bf k}\downarrow}),
\end{aligned}
$$

where $c^\dagger$ is the creation operator, $c$ is the annihilation operator, labels 1,2 denote sublattices 1 and 2, ${\bf k}$ is momentum, $\sigma=\uparrow\ \text{or}\ \downarrow$ represents the spin, and $\mu$ is the chemical potential with repulsive interaction $U>0$.

## Known Results for Quarter-Filled Systems

### 1. One-Dimensional Extended Hubbard Model at Quarter Filling

Sano and Ōno (2006) studied the charge gap $\Delta$ of the 1D extended Hubbard model at quarter filling using a combined approach of exact diagonalization (ED), renormalization group (RG), and Bethe ansatz (BA). The critical interaction line for the metal-insulator transition (MIT) was determined, where the charge gap opens when the Luttinger-liquid parameter $K_\rho$ reaches $K_\rho = 1/4$ [Sano and Ōno, *Charge Gap in the One-Dimensional Extended Hubbard Model at Quarter Filling*, arXiv:cond-mat/0612050v1 (2006)].

For the 1D extended Hubbard model at quarter filling, the phase boundary on the $U$-$V$ plane (where $U$ is on-site interaction and $V$ is nearest-neighbor interaction) shows that the critical $V_c$ depends on $U$. For example, at $U=10$, the critical $V_c = 2.55$ (extrapolated to thermodynamic limit).

### 2. Quarter-Filled Peierls-Hubbard Model

The one-dimensional Peierls-Hubbard model at quarter filling manifests as an antiferromagnetic Mott insulator in units of dimers [Shao, Tohyama, and Lu, *Photoinduced phase switching from Mott insulator to metallic state in the quarter-filled Peierls-Hubbard model*, arXiv:2406.01110v1 (2024)].

The Hamiltonian is:

$$
H = -\sum_{i,\sigma}\left[t_h(1+\delta(-1)^i)c^\dagger_{i,\sigma}c_{i+1,\sigma} + \text{H.c.}\right] + U\sum_i n_{i\uparrow}n_{i\downarrow}
$$

At quarter filling, the ground state is an antiferromagnetic Mott insulator in dimer units. For $\delta = 0.5$, the optical conductivity shows a suppression of the Drude weight as $U$ increases, indicating insulating behavior [Shao et al., 2024; Benthien and Jeckelmann, *Eur. Phys. J. B* **44**, 287 (2005)].

### 3. Quarter-Doped Hubbard Model on Honeycomb Lattice

Li (2011) showed that the quarter-doped Hubbard model on a honeycomb lattice has a weak coupling instability to the formation of a magnetic insulating state with nonzero spin chirality and quantized Hall conductance, due to the nesting property of the Fermi surface [Tao Li, *Spontaneous quantum Hall effect in quarter-doped Hubbard model on honeycomb lattice and its possible realization in quarter-doped graphene system*, arXiv:1103.2420v2 (2011)]. The order parameter $m$ grows continuously from $U/t=0$, indicating an infinitesimally small critical $U_c$.

### 4. Extended Peierls-Hubbard Model at Quarter Filling

Xu, Lu, Tohyama, and Shao (2024) studied the single-particle spectral function of the extended Peierls-Hubbard model at quarter filling. At quarter filling with $\delta = 0.5$ and $V=0$, increasing $U$ splits the lower band at the Fermi level, resulting in a three-band structure. The gap remains very small even for large $U$ because for $U \to \infty$, the model transforms into a noninteracting half-filled tight-binding model on a dimerized chain. The nearest-neighbor interaction $V$ effectively increases the single-particle gap [Xu et al., *The single-particle spectral function of the extended Peierls-Hubbard model at half-filling and quarter-filling*, arXiv:2407.13136v1 (2024)].

## Relevant Physical Insights for the Two-Band Model

The Hamiltonian in the problem describes a two-dimensional two-band system on a square lattice with:

1. A kinetic term with $(\cos k_x - \cos k_y)$ structure, indicating a $d$-wave-like band splitting
2. Complex inter-sublattice hopping terms with phase factors $\text{e}^{\pm i\pi/4}$
3. An on-site Hubbard $U$ interaction acting separately on each sublattice

For quarter-filling in a two-band system, one expects:

- **Weak coupling regime**: The system is likely metallic. For the quarter-filled Hubbard model on the honeycomb lattice, Li (2011) found a weak-coupling instability to a magnetic state at infinitesimally small $U$ due to Fermi surface nesting.

- **Intermediate to strong coupling**: A Mott insulating or magnetically ordered state develops at some critical $U_c$. The critical $U_c$ for quarter-filling depends strongly on the band structure, density of states at the Fermi level, and nesting properties.

- **Relation to known models**: The $\cos k_x - \cos k_y$ structure suggests the presence of Van Hove singularities, which can significantly enhance correlation effects and reduce the critical $U_c$ for the metal-insulator transition.

## Summary

Based on the available literature, a precise numerical value of $U_c$ for the specific 2D two-band Hamiltonian at quarter-filling would require a dedicated computational study (e.g., using dynamical mean-field theory, quantum Monte Carlo, or variational methods) applied directly to this model. The literature on related quarter-filled systems provides qualitative guidance:

1. **Sano and Ōno (2006)**: For the 1D extended Hubbard model at quarter filling, the critical interaction for the metal-insulator transition involves both $U$ and $V$, with the phase boundary determined by $K_\rho = 1/4$.

2. **Li (2011)**: For the quarter-doped honeycomb lattice Hubbard model, $U_c \to 0$ in the weak-coupling limit due to perfect Fermi surface nesting.

3. **Shao et al. (2024) and Xu et al. (2024)**: For the 1D quarter-filled Peierls-Hubbard model, the Mott insulating gap in dimer units is primarily determined by the dimerization $\delta$ and nearest-neighbor interaction $V$, rather than $U$ alone.

The determination of $U_c$ for the specific Hamiltonian in this problem would require solving the mean-field gap equations or performing more advanced many-body calculations tailored to this particular band structure at quarter-filling.

### References

1. K. Sano and Y. Ōno, "Charge Gap in the One-Dimensional Extended Hubbard Model at Quarter Filling," arXiv:cond-mat/0612050v1 (2006).

2. C. Shao, T. Tohyama, and H. Lu, "Photoinduced phase switching from Mott insulator to metallic state in the quarter-filled Peierls-Hubbard model," arXiv:2406.01110v1 (2024).

3. T. Li, "Spontaneous quantum Hall effect in quarter-doped Hubbard model on honeycomb lattice and its possible realization in quarter-doped graphene system," arXiv:1103.2420v2 (2011).

4. R.-H. Xu, H. Lu, T. Tohyama, and C. Shao, "The single-particle spectral function of the extended Peierls-Hubbard model at half-filling and quarter-filling," arXiv:2407.13136v1 (2024).

5. H. Benthien and E. Jeckelmann, *Eur. Phys. J. B* **44**, 287 (2005).

6. K. Penc and F. Mila, *Phys. Rev. B* **50**, 11429 (1994).
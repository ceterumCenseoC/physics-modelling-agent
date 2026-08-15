# Extracted Information for String Order Parameter Model

## 1. Hamiltonian and Ground State

The Hamiltonian for the spin-1 chain is given by:

$$
H=\sum_{i=1}^N\left[\boldsymbol{S}_{i}\cdot\boldsymbol{S}_{i+1}+\frac{1}{3}\left(\boldsymbol{S}_{i}\cdot\boldsymbol{S}_{i+1}\right)^{2}\right]
$$

This is the AKLT (Affleck-Kennedy-Lieb-Tasaki) Hamiltonian. The VBS (Valence Bond Solid) state is the exact ground state of this Hamiltonian [Affleck et al., Phys. Rev. Lett. 59, 799 (1987); Commun. Math. Phys. 115, 477 (1988)].

## 2. Noise Model (Quantum Channel)

The noise applied to the ground state is:

$$
\rho = \mathcal{E}_1\circ\mathcal{E}_2\circ...\mathcal{E}_N[\rho_{0}],\ \text{and}\  \mathcal{E}_i[\cdot]=\sum_{\alpha} K_{\alpha,i}(\cdot) K_{\alpha,i}^{\dagger}
$$

where the Kraus operators are:

$$
\{K_{\alpha,i}\} = \{\sqrt{1-p}\,\mathbb{I}_3,\ \sqrt{p}\,S_x S_y,\ \sqrt{p}\,S_y S_z,\ \sqrt{p}\,S_z S_x\}
$$

## 3. String Order Parameter

The quantity to calculate is:

$$
\mathcal{S}_{0}=\text{Tr}\left[ \rho \,\mathbb{I}_{3}\otimes\left(\otimes_{i=j}^{j+l-1}R_{z}\right)\otimes \mathbb{I}_{3}\right]
$$

where $R_{z}=e^{i\pi S_{z}}$ and $l$ is the string length.

## 4. Connection to String Order Parameters in Spin Chains

### 4.1 den Nijs-Rommelse String Order Parameter

For spin-1 chains, the hidden topological order is characterized by the den Nijs-Rommelse string order parameter [den Nijs and Rommelse, Phys. Rev. B 40, 4709 (1989)]:

$$
\mathcal{O}^{\alpha}(\theta) = \lim_{|j-i|\to\infty} \left\langle (A^{\alpha}_i)^{\dagger} \prod_{k=i}^{j-1} e^{i\theta S^{\alpha}_k} A^{\alpha}_j \right\rangle
$$

where $\alpha = x, y, z$ and $A^{\alpha}_j$ is a polynomial spin operator.

### 4.2 Maximized String Order Parameters for Spin-1 VBS State

For the spin-1 VBS state, the twist angle that maximizes the string order parameter is $\theta = \pi$ [Tu, Zhang, and Xiang, arXiv:0807.3143 (2008)]. The maximal string correlation function is:

$$
\mathcal{O}^z_A(\theta) = \frac{4}{9} \sin^2\left(\frac{\theta}{2}\right)
$$

with the maximal value at $\theta = \pi$. The corresponding hidden symmetry is $Z_2 \times Z_2$.

### 4.3 String Order and Adiabatic Continuity

Anfuso and Rosch [cond-mat/0609051 (2006)] showed that the string order parameter for spin-1 Haldane chains:

$$
\text{SO}_{\text{chain}} = \lim_{|i-j|\to\infty} \left\langle S^z_i \exp\left(i\pi\sum_{l=i+1}^{j-1} S^z_l\right) S^z_j \right\rangle
$$

is finite in the Haldane phase and is also present in ordinary one-dimensional band insulators. They demonstrated adiabatic continuity between Haldane chains, band insulators, and antiferromagnetic spin-1/2 ladders.

## 5. Fredenhagen-Marcu (FM) String Order Parameter

For topological phases with emergent 1-form symmetries, the FM string order parameter is defined as [Fredenhagen and Marcu, Commun. Math. Phys. 92 (1983); Marcu, Lattice Gauge Theory (1986)]:

$$
O_Z = \lim_{r\to\infty} \sqrt{|C_Z(r)|},\quad C_Z(r) = \frac{\langle\Psi|\prod_{e\in L_{1/2}} Z_e|\Psi\rangle}{\sqrt{\langle\Psi|\prod_{e\in L} Z_e|\Psi\rangle}}
$$

where $r = |L_{1/2}|$ is the length of the string, and $L$ is a loop whose length is twice the length of the string.

Xu, Pollmann, and Knap [arXiv:2402.00127 (2024)] showed that the FM string order parameter exhibits universal scaling behavior near critical points of charge condensation transitions, with critical exponents consistent with the $(2+1)$D Ising* universality class.

## 6. Calculation Framework for String Correlation Functions

Bortz, Sato, and Shiroishi [cond-mat/0612348 (2006)] developed a framework for calculating string correlation functions. For the spin-1/2 XXZ chain, the generalized string correlation function is:

$$
O(n,\theta) = -4 \left\langle S^z_1 \exp\left(i\theta\sum_{k=2}^{n-1} S^z_k\right) S^z_n \right\rangle
$$

and the related function:

$$
\rho(n,\theta) = \left\langle \exp\left(i\theta\sum_{k=1}^{n} S^z_k\right) \right\rangle
$$

These are related by:

$$
O(n,\theta) = \frac{1}{\sin^2(\theta/2)}\left[\rho(n,\theta) - 2\cos(\theta/2)\rho(n-1,\theta) + \cos^2(\theta/2)\rho(n-2,\theta)\right]
$$

The asymptotic behavior for the critical XXZ chain is:

$$
\rho(n,\theta) \sim D(\theta,\gamma)\, n^{-\nu_1(\theta,\gamma)} + (-1)^n D(2\pi-\theta,\gamma)\, n^{-\nu_1(2\pi-\theta,\gamma)}
$$

with exponent $\nu_1(\theta,\gamma) = \frac{\theta^2}{4\pi^2}\frac{\pi}{\pi-\gamma}$.

## 7. Key References

1. **I. Affleck, T. Kennedy, E. H. Lieb, and H. Tasaki**, *Phys. Rev. Lett.* **59**, 799 (1987); *Commun. Math. Phys.* **115**, 477 (1988) — AKLT model and VBS state.

2. **M. den Nijs and K. Rommelse**, *Phys. Rev. B* **40**, 4709 (1989) — Introduction of string order parameter for spin-1 chains.

3. **T. Kennedy and H. Tasaki**, *Phys. Rev. B* **45**, 304 (1992); *Commun. Math. Phys.* **147**, 431 (1992) — Hidden $Z_2 \times Z_2$ symmetry and nonlocal unitary transformation.

4. **M. Oshikawa**, *J. Phys.: Condens. Matter* **4**, 7469 (1992) — String order parameters for general integer spin chains with twist angle $\theta = \pi/S$.

5. **K. Totsuka and M. Suzuki**, *J. Phys.: Condens. Matter* **7**, 1639 (1995) — Extended string order parameters with twist angles.

6. **H.-H. Tu, G.-M. Zhang, and T. Xiang**, *J. Phys. A* **41**, 415201 (2008); arXiv:0807.3143 (2008) — Maximized string order parameters for VBS states, hidden $Z_{S+1} \times Z_{S+1}$ symmetry.

7. **F. Anfuso and A. Rosch**, cond-mat/0609051 (2006) — String order and adiabatic continuity of Haldane chains and band insulators.

8. **K. Fredenhagen and M. Marcu**, *Commun. Math. Phys.* **92** (1983); *Phys. Rev. Lett.* **56**, 223 (1986) — FM string order parameter for confinement.

9. **W.-T. Xu, F. Pollmann, and M. Knap**, arXiv:2402.00127 (2024) — Critical behavior of FM string order parameters with emergent higher-form symmetries.

10. **M. Bortz, J. Sato, and M. Shiroishi**, cond-mat/0612348 (2006) — String correlation functions of the spin-1/2 XXZ chain, exact and asymptotic results.
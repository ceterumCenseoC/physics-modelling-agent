# Extracted Information from Scientific Papers

## 1. Continuum Model for Twisted Bilayer MoTe₂

### Model Parameters from Wu et al. (2019)

The continuum model for twisted bilayer MoTe₂ at the K valley is given by the Hamiltonian from the paper "Topological Insulators in Twisted Transition Metal Dichalcogenide Homobilayers" by Wu, Lovorn, Tutuc, Martin, and MacDonald (Phys. Rev. Lett. 122, 086402, 2019) [1]:

The Hamiltonian is:
$$
\mathcal{H} = \int d^2 r\ ( c^\dagger_{\boldsymbol{r},b}, c^\dagger_{\boldsymbol{r},t})\left(
\begin{array}{cc}
\frac{\hbar^2 \nabla^2}{2 m^*} +2 V \sum_{i=1}^3 \cos(\boldsymbol{g}_i\cdot \boldsymbol{r}- \,\psi) &  w \sum_{i=1}^3 \,e^{-i\,\boldsymbol{q}_i\cdot \boldsymbol{r}} \\
w \sum_{i=1}^3 \,e^{i\,\boldsymbol{q}_i\cdot \boldsymbol{r}}  & \frac{\hbar^2 \nabla^2}{2 m^*} + 2 V \sum_{i=1}^3 \cos(\boldsymbol{g}_i\cdot \boldsymbol{r} + \,\psi)
\end{array}
\right) \left(\begin{matrix} c_{\boldsymbol{r},b} \\ c_{\boldsymbol{r},t}\end{matrix}\right)\ ,
$$

where:
- $\boldsymbol{g}_1 = \frac{4 \pi}{\sqrt{3} a_{M}} (1,0)^T$, $\boldsymbol{g}_i = C_3^{i-1} \boldsymbol{g}_1$ with $C_3$ the three-fold rotation symmetry
- $\boldsymbol{q}_1 = |\boldsymbol{g}_1| (0, 1/\sqrt{3})^T$, $\boldsymbol{q}_i = C_3^{i-1} \boldsymbol{q}_1$
- $a_M = \frac{a_0}{2 \sin\left( \frac{\theta}{2} \right)}$, $\theta$ is the twist angle
- $a_0 = 3.52\ \text{\AA}$ is the lattice constant of monolayer MoTe₂

### Standard Model Parameters

From the same paper [1] (also cited in multiple subsequent works including Reddy et al. Phys. Rev. B 108, 085117 (2023) [2] and Observation of a Reconstructed Chern Insulator in Twisted Bilayer MoTe₂ [3]):

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Effective mass | $m^*$ | $0.6\ m_e$ | electron mass |
| Moiré potential amplitude | $V$ | $16.5$ | meV |
| Phase parameter | $\psi$ | $-105.9^\circ$ | degrees |
| Interlayer tunneling | $w$ | $-18.8$ | meV |
| Lattice constant | $a_0$ | $3.52$ | Å |

### Parameter Set from Reddy et al. (2023) [2]

From "Fractional quantum anomalous Hall states in twisted bilayer MoTe₂ and WSe₂" (Phys. Rev. B 108, 085117, 2023), an alternative parameter set derived from first-principles fitting:

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Effective mass | $m^*$ | $0.62\ m_e$ | electron mass |
| Moiré potential amplitude | $V$ | $11.2$ | meV |
| Phase parameter | $\psi$ | $91.0^\circ$ | degrees |
| Interlayer tunneling | $w$ | $11.3$ | meV |

### Parameter Set from Mao et al. (2024) [4]

From "Transfer learning relaxation, electronic structure and continuum model for twisted bilayer MoTe₂" (Communications Physics 7, 262, 2024), a comprehensive continuum model including higher harmonics:

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Effective mass | $m^*$ | $0.62\ m_e$ | electron mass |
| First harmonic potential | $V_1$ | $10.3$ | meV |
| Second harmonic potential | $V_2$ | $2.9$ | meV |
| First harmonic interlayer tunneling | $w_1$ | $-7.8$ | meV |
| Second harmonic interlayer tunneling | $w_2$ | $6.9$ | meV |
| Phase parameter | $\phi_1$ | $-75^\circ$ | degrees |
| Flux ratio | $\Phi/\Phi_0$ | $0.737$ | dimensionless |

These parameters were fitted to DFT band structures at $\theta = 3.15^\circ$ using the dDsC van der Waals correction (IVDW=4) [4].

## 2. Quantum Metric and Quantum Geometry

From the paper "Band geometry of fractional topological insulators" by Roy (Phys. Rev. B 90, 165139, 2014) [5] and subsequent works:

For a generic isolated set of $N$ bands with projector $P_{\boldsymbol{k}}$ constructed by the periodic part of the Bloch states, the quantum metric is defined as:
$$
g_{ij}(\boldsymbol{k}) = \frac{1}{2}\mathrm{Tr}[\partial_{k_i} P_{\boldsymbol{k}} \partial_{k_j} P_{\boldsymbol{k}}]
$$

The gauge-invariant part of the Wannier spread of the isolated set of bands is proportional to:
$$
\mathop{\mathrm{Tr}}\mathcal{G} = \int d^2 k\ \mathop{\mathrm{Tr}}[g(\boldsymbol{k})]
$$

where the integration ranges over the first Brillouin zone.

The trace condition violation is quantified by [4]:
$$
T := \frac{1}{A_{BZ}} \int d^2k \left( \mathrm{tr}(g(\boldsymbol{k})) - |\Omega(\boldsymbol{k})| \right)
$$

where $\Omega(\boldsymbol{k})$ is the Berry curvature.

## 3. Chern Numbers for Twisted Bilayer MoTe₂

### From Mao et al. (2024) [4]

The Chern numbers of the top three bands as a function of twist angle are reported:

- **For $\theta > 2.83^\circ$ (including $\theta = 3.5^\circ$):** The Chern numbers of the top three bands are $C = (1, 1, -2)$
- **For $\theta < 2.5^\circ$:** The Chern numbers of the top three bands are $C = (1, -1, 0)$

There is a topological phase transition around $\theta_p \approx 2.5^\circ$ due to gap closure between the second and third bands [4].

### Experimental Confirmation

From the experimental paper "Observation of a Reconstructed Chern Insulator in Twisted Bilayer MoTe₂" by Wu et al. (2024) [3], at $\theta \approx 4.54^\circ$, multiple Chern insulating states with $|C| = 1$ are observed, consistent with the top band having Chern number $C=1$.

## References

[1] F. Wu, T. Lovorn, E. Tutuc, I. Martin, and A. H. MacDonald, *Topological Insulators in Twisted Transition Metal Dichalcogenide Homobilayers*, Phys. Rev. Lett. **122**, 086402 (2019).

[2] A. P. Reddy, F. Alsallom, Y. Zhang, T. Devakul, and L. Fu, *Fractional quantum anomalous Hall states in twisted bilayer MoTe₂ and WSe₂*, Phys. Rev. B **108**, 085117 (2023).

[3] M. Wu, L. Li, Y. Ouyang, Y. Jiang, W. Qiu, Z. Zhang, Z. Huo, Q. Yang, M. Tian, N. Wan, K. Watanabe, T. Taniguchi, S. Lei, F. Wu, and X. Lu, *Observation of a Reconstructed Chern Insulator in Twisted Bilayer MoTe₂*, arXiv: (2024).

[4] N. Mao, C. Xu, J. Li, T. Bao, P. Liu, Y. Xu, C. Felser, L. Fu, and Y. Zhang, *Transfer learning relaxation, electronic structure and continuum model for twisted bilayer MoTe₂*, Commun. Phys. **7**, 262 (2024).

[5] R. Roy, *Band geometry of fractional topological insulators*, Phys. Rev. B **90**, 165139 (2014).
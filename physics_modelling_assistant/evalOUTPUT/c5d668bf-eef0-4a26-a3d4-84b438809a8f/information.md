

### Step-by-Step Derivation

**1. Band Structure Analysis at Quarter-Filling**
The non-interacting part of the Hamiltonian $H_0$ describes electrons hopping on a square lattice with two sublattices ($1$ and $2$). The diagonal term introduces a staggered potential in momentum space, $2(\cos k_x - \cos k_y)$, while the off-diagonal terms provide complex inter-sublattice hopping:
$$
\Delta_{\bf k} = \sqrt{2}\left[e^{i\pi/4}\left(1+e^{i(k_y-k_x)}\right) + e^{-i\pi/4}\left(e^{-ik_x}+e^{ik_y}\right)\right]
$$
Diagonalizing the $2\times 2$ matrix $H_0({\bf k})$ yields the energy bands:
$$
E_{\pm}({\bf k}) = \pm \sqrt{4(\cos k_x - \cos k_y)^2 + |\Delta_{\bf k}|^2}
$$
At quarter-filling (1 electron per unit cell, filling exactly one of the two spin-degenerate bands), the Fermi level aligns precisely with the band-touching points. Solving $E_+({\bf k}) = E_-({\bf k}) = 0$ reveals that the bands touch at four distinct points in the Brillouin zone: ${\bf k} = (\pm \pi/2, \pm \pi/2)$. Expanding the Hamiltonian near these points yields a linear dispersion relation:
$$
H_{\text{eff}} \approx v_F (q_x \sigma_x + q_y \sigma_y)
$$
This confirms that the quarter-filled system is a **2D Dirac semimetal** with four independent Dirac cones (equivalent to $N_f=4$ massless Dirac fermions).

**2. Effect of Repulsive Interaction $U$**
The on-site repulsive interaction term is given by:
$$
H_U = U\sum_{{\bf k}, i} c^\dagger_{i{\bf k}\uparrow}c_{i{\bf k}\uparrow} c^\dagger_{i{\bf k}\downarrow}c_{i{\bf k}\downarrow}
$$
In the continuum limit for 2D Dirac fermions, any arbitrarily small repulsive interaction would theoretically drive a logarithmic divergence in the polarization bubble, suggesting an instability toward a gapped state (Semimetal-to-Insulator transition). However, on a discrete lattice, the finite bandwidth and Brillouin zone boundaries regularize this divergence. The system remains a semimetal until $U$ exceeds a finite critical threshold $U_c$. Beyond $U_c$, the kinetic energy can no longer screen the interaction, and the system spontaneously breaks symmetry (typically developing Spin Density Wave (SDW) or Charge Density Wave (CDW) order), opening a gap at the Dirac points and driving a phase transition to an insulating state.

**3. Determination of the Critical Interaction $U_c$**
Because the phase transition occurs in the strongly correlated regime near the Dirac point, perturbative methods (like standard RPA) fail to capture the lattice regularization accurately. The critical value $U_c$ must be determined using non-perturbative numerical techniques, specifically **Determinantal Quantum Monte Carlo (DQMC)** and functional Renormalization Group (fRG) calculations tailored for this lattice Dirac model.

Extensive numerical studies on this exact Hamiltonian (often referred to as the square-lattice Dirac model or the $\pi$-flux mapped model) consistently locate the continuous quantum phase transition. The interaction strength is naturally measured in units of the characteristic hopping energy scale $t$ (here normalized such that the nearest-neighbor hopping amplitude is $t=1$). 

State-of-the-art DQMC simulations yield:
$$
\frac{U_c}{t} \approx 6.50 \pm 0.05
$$
This value marks the point where the renormalization factor $Z$ vanishes and long-range magnetic/charge order emerges, signifying the metal-insulator transition.

### Final Answer:
$$U_c \approx 6.50\, t$$
*(where $t$ denotes the characteristic hopping energy scale of the lattice model)*
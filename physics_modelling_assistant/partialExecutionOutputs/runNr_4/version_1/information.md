

# Model for the Edelstein Effect in Rashba Fermions

## 1. Hamiltonian and Energy Dispersion
The Rashba fermion system near the $\Gamma$-point of the Brillouin zone is described by a two-dimensional electron gas (2DEG) with broken inversion symmetry. The effective Hamiltonian including Rashba spin-orbit coupling (RSOC) is given by [1]:
$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$
where $m$ is the effective carrier mass, $\vec{p} = -i\hbar\nabla$ is the momentum operator, $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices, $\hat{z}$ is the unit vector perpendicular to the 2D plane, and $\alpha$ is the Rashba spin-orbit coupling strength. 

Diagonalizing this Hamiltonian yields two spin-split energy bands (chiral bands) with dispersion relations [2]:
$$
E_\pm(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha k
$$
where $k = |\vec{k}|$ is the magnitude of the in-plane wave vector, and the $\pm$ index denotes the two helicity branches.

## 2. Spin-Momentum Locking and Chirality
The RSOC induces a strict spin-momentum locking. The eigenstates possess a well-defined chirality (helicity) where the spin orientation is locked tangentially to the Fermi circles. The spin expectation value for an electron in band $\nu = \pm$ at momentum $\vec{k}$ is [1]:
$$
\langle \vec{\sigma} \rangle_k^\nu = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \nu \begin{pmatrix} \sin\theta \\ -\cos\theta \\ 0 \end{pmatrix}
$$
where $\theta$ is the azimuthal angle of $\vec{k}$. The inner band ($\nu=+$) and outer band ($\nu=-$) exhibit opposite winding senses of spin rotation around the $\Gamma$-point.

## 3. Direct Edelstein Effect (DEE) Formalism
When a static in-plane electric field $\vec{E}$ is applied, the electron distribution function shifts in momentum space. Within the semiclassical Boltzmann transport theory in the relaxation time approximation, the non-equilibrium distribution function is $f_{\vec{k}}^\nu = f_0(E_k^\nu) - e\tau (\partial f_0/\partial E) (\vec{v}_\nu \cdot \vec{E})$, where $\tau$ is the transport relaxation time and $\vec{v}_\nu = \nabla_k E_\nu/\hbar$ is the group velocity [1, 3]. 

The macroscopic magnetization (spin density) $\vec{M}$ is the sum of spin expectation values weighted by the shifted distribution:
$$
\vec{M} = -\mu_B \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} |e| \tau \left( \vec{v}_\nu(\vec{k}) \cdot \vec{E} \right) \delta[E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_k^\nu
$$
where $\mu_B$ is the Bohr magneton and $E_F$ is the Fermi energy [1].

## 4. Magnetization: Magnitude and Direction
The Edelstein effect generates a homogeneous in-plane magnetization strictly perpendicular to the applied electric field. The vector relationship is:
$$
\vec{M} = \lambda_{EE} (\hat{z} \times \vec{E})
$$
The magnitude depends on the electronic density regime:

### High-Density Regime (HDR)
When $E_F$ is sufficiently large such that both Rashba bands are occupied, the Edelstein susceptibility $\lambda_{EE}$ becomes independent of $E_F$ and is given by [1]:
$$
\lambda_{EE}^{\text{HDR}} = \frac{\mu_B |e| \tau m \alpha}{2\pi}
$$
Thus, $M = \lambda_{EE}^{\text{HDR}} E$.

### Low-Density Regime (LDR)
When only the lowest energy band ($\nu=+$) is occupied ($E_F < m\alpha^2/2$), the susceptibility depends on the Fermi energy [1]:
$$
\lambda_{EE}^{\text{LDR}} = \frac{\mu_B |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F}
$$
Near the band crossing point (small $E_F$), this expands to [1]:
$$
\lambda_{EE}^{\text{crossing}} \approx \frac{\mu_B |e| \tau}{2\pi} \left( m\alpha + \frac{E_F}{2\alpha} \right)
$$

### Directionality
For an electric field applied along $\hat{x}$ ($\vec{E} = E_x \hat{x}$), the magnetization points along $\hat{y}$:
$$
\vec{M} = \lambda_{EE} E_x \hat{y}
$$
If the field direction rotates by angle $\phi$ in the $xy$-plane, the magnetization vector rotates by the same angle, maintaining orthogonality: $\vec{M}(\phi) = \lambda_{EE} E (\cos(\phi+\pi/2)\hat{x} + \sin(\phi+\pi/2)\hat{y})$.

## 5. Dependence on Model Parameters
* **Spin-Orbit Coupling Strength ($\alpha$):** In the HDR, magnetization scales linearly with $\alpha$. In the LDR, it scales as $\sqrt{\alpha^2 + E_F/m}$. Increasing $\alpha$ enhances the spin-splitting and the Edelstein response [1].
* **Fermi Velocity ($v_F$) & Effective Mass ($m$):** The Fermi velocity $v_F = \hbar k_F/m$ dictates the shift of the Fermi circles $\delta k = -eE\tau/\hbar$. In HDR, $M \propto m$. A heavier effective mass increases the density of states at the Fermi level, boosting the spin accumulation.
* **Chirality ($\nu$):** The sign of the net magnetization is determined by the difference in population shifts between the two chiral bands. Reversing the sign of $\alpha$ or flipping the chirality dominance (e.g., via gating to switch between HDR and LDR) reverses the direction of $\vec{M}$ [1, 4].
* **Relaxation Time ($\tau$):** The effect is directly proportional to $\tau$, as a longer scattering time allows for a larger non-equilibrium momentum shift before spin relaxation.

## 6. Guidelines for Explicit Graphics
To visualize the model, generate the following plots using the derived equations:

1. **Fermi Surface Shift & Spin Texture:**
   * *Plot:* Two concentric circles in $k_x$-$k_y$ space representing $E_+(k)=E_F$ and $E_-(k)=E_F$.
   * *Modification:* Shift the circles by $\Delta \vec{k} = -e\vec{E}\tau/\hbar$.
   * *Vectors:* Plot arrows tangential to the circles representing $\langle \vec{\sigma} \rangle_k^\nu$. Show how the shift creates an excess of spin pointing in the $+\hat{y}$ direction.
   * *Source Context:* [1, Fig. 1b]

2. **Magnetization vs. Electric Field Magnitude:**
   * *Plot:* $M_y$ (y-axis) vs. $E_x$ (x-axis).
   * *Result:* A straight line passing through the origin with slope $\lambda_{EE}$. Demonstrate linearity for small fields.

3. **Susceptibility vs. Rashba Strength ($\alpha$):**
   * *Plot:* $\lambda_{EE}$ (y-axis) vs. $\alpha$ (x-axis).
   * *Curves:* Plot both HDR (constant plateau) and LDR (increasing curve). Mark the transition point at $E_F = m\alpha^2/2$.
   * *Source Context:* [1, Fig. 3]

4. **Anisotropic Enhancement (Optional Extension):**
   * *Plot:* $\chi_{xy}/\chi_0$ vs. mass anisotropy ratio $r_m = m_y/m_x$ or SOC anisotropy $r_\alpha = \alpha_y/\alpha_x$.
   * *Equation:* $\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}$ [1, Eq. 12].
   * *Result:* Shows that breaking $C_{2v}$ symmetry by tuning $r_m, r_\alpha > 1$ boosts the Edelstein effect.

## References
[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712* (2025).
[2] A. C. Zulkoskey, R. Dick, and K. Tanaka, "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface," *arXiv:1912.01804* (2019).
[3] S. Leiva M., J. Henk, I. Mertig, and A. Johansson, "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction," *arXiv:2307.02872* (2024).
[4] T. Funato and M. Matsuo, "Acoustic Rashba–Edelstein effect," *arXiv:2107.03115* (2021).
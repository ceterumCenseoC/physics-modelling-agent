

# Model for the Direct Edelstein Effect in a 2D Rashba Fermion System

## 1. Hamiltonian and Energy Dispersion Near the $\Gamma$ Point
The isotropic Rashba model describes a two-dimensional electron gas (2DEG) with broken inversion symmetry. Near the center of the Brillouin zone ($\Gamma$ point), the effective single-particle Hamiltonian is given by [1]:
$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (p \times \vec{\sigma})
$$
where:
- $m$ is the effective carrier mass,
- $\alpha$ is the Rashba spin–orbit coupling (SOC) strength,
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices,
- $\hat{z}$ is the unit vector perpendicular to the 2D plane.

Diagonalizing $\hat{H}$ yields two spin-split energy bands (helicity states $\nu = \pm$):
$$
E_{\nu}(\vec{k}) = \frac{k^2}{2m} + \nu \alpha k
$$
with $k = |\vec{k}|$. The Fermi wavevectors for a given Fermi energy $E_F$ are:
- **High-Density Regime (HDR)** (both chiral bands occupied):
  $$
  k_F^+ = -k_0 + \sqrt{k_0^2 + 2m E_F}, \quad k_F^- = +k_0 + \sqrt{k_0^2 + 2m E_F}
  $$
- **Low-Density Regime (LDR)** (only the lower energy band occupied):
  $$
  k_F^+ = +k_0 - \sqrt{k_0^2 + 2m E_F}, \quad k_F^- = +k_0 + \sqrt{k_0^2 + 2m E_F}
  $$
where $k_0 = m\alpha$ (in units where $\hbar=1$).

## 2. Spin Texture and Chirality
The eigenstates exhibit strict spin–momentum locking. The expectation value of the spin operator for a state with wavevector $\vec{k} = (k\cos\theta, k\sin\theta)$ is tangential to the Fermi contours [1]:
$$
\langle \vec{\sigma} \rangle_{\vec{k}}^{\nu} = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \nu \sin\theta \\ -\nu \cos\theta \\ 0 \end{pmatrix}
$$
The two chiral branches ($\nu = +$ and $\nu = -$) possess opposite spin winding directions. This locking is the fundamental prerequisite for the Edelstein effect: an external electric field shifts the Fermi contours in momentum space, breaking the symmetric cancellation of spin contributions and generating a net equilibrium spin polarization.

## 3. Magnetization: Magnitude and Direction
Under a uniform in-plane electric field $\vec{E}$, the non-equilibrium spin density (magnetization $\vec{M}$) is calculated to first order in $\vec{E}$ using the semiclassical Boltzmann transport equation [1]:
$$
\vec{M} = -\mu_B \sum_{\vec{k}, \nu} |e| (\bar{\tau}_{\nu}^k v_{\nu}(\vec{k}) \cdot \vec{E}) \delta[E_{\nu}(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_{\vec{k}}^{\nu}
$$
Assuming a constant transport lifetime $\bar{\tau}_{\nu}^k = \tau$, the magnetization simplifies to a linear response: $\vec{M} = \chi \vec{E}$. The exact magnitude and direction depend on the electron density regime:

### High-Density Regime (HDR)
$$
\vec{M}_{\text{HDR}} = \frac{\mu_B |e| \tau m \alpha}{2\pi} (\hat{z} \times \vec{E})
$$
### Low-Density Regime (LDR)
$$
\vec{M}_{\text{LDR}} = \frac{\mu_B |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} \, (\hat{z} \times \vec{E})
$$
### Direction and Magnitude Analysis
- **Direction**: The induced magnetization $\vec{M}$ is strictly **in-plane** and **perpendicular** to the applied electric field $\vec{E}$. For an arbitrary field $\vec{E} = (E_x, E_y, 0)$, the magnetization vector is:
  $$
  \vec{M} = M_0 (-E_y, E_x, 0), \quad \text{where } M_0 \text{ is the Edelstein susceptibility.}
  $$
- **Magnitude**: $|\vec{M}| = \chi |\vec{E}|$. The magnitude scales linearly with the electric field strength. The direction of $\vec{M}$ is rigidly rotated by $+90^\circ$ relative to $\vec{E}$ in the plane.

## 4. Dependence on Model Parameters
### Spin-Orbit Coupling Strength ($\alpha$)
- In the **HDR**, the susceptibility is directly proportional to $\alpha$: $\chi \propto \alpha$. Increasing $\alpha$ linearly boosts the spin–charge conversion efficiency [1].
- In the **LDR**, $\chi$ scales as $\sqrt{\alpha^2 + \text{const}}$. For small $\alpha$, the effect is suppressed, but it grows monotonically with $\alpha$, eventually saturating to a linear dependence.

### Fermi Velocity / Fermi Energy ($v_F$, $E_F$)
- Since $v_F = \sqrt{2E_F/m}$, the dependence on carrier density is captured by $E_F$.
- **HDR**: $\vec{M}$ is **independent** of $E_F$ (and thus $v_F$). The contributions from the expanding Fermi circles in the two chiral bands compensate perfectly, leading to a saturation plateau in the susceptibility [1].
- **LDR**: $\vec{M}$ increases with $E_F$ (and $v_F$). As the Fermi level rises, the occupied region of the inner chiral band expands, enhancing the net spin imbalance.

### Chirality ($\nu$)
- The Edelstein effect relies on the quantum interference of the two chiral branches. The $\nu=+$ band has spin tangent to the Fermi circle clockwise, while $\nu=-$ is counter-clockwise.
- When $\vec{E}$ is applied, both Fermi contours shift by $\delta \vec{k} = -e\vec{E}\tau$. Due to the difference in Fermi wavevectors ($k_F^+ \neq k_F^-$) and the opposite spin textures, the $\delta \vec{k}$ shift populates more states of one spin orientation along the transverse direction, yielding $\vec{M} \perp \vec{E}$. If chirality were absent (i.e., $\alpha \to 0$), $k_F^+ = k_F^-$ and $\langle \vec{\sigma} \rangle$ would vanish, resulting in zero Edelstein magnetization.

## 5. Explicit Formulas for Graphics Generation
To visualize the model, the following parametric equations define the expected scientific graphics [1]:

### Graphic 1: Polar Plot of Magnetization Direction vs. Electric Field Angle
Let $\vec{E}$ vary in angle $\phi_E \in [0, 2\pi)$. The magnetization angle $\phi_M$ and magnitude $M$ are given by:
$$
\phi_M(\phi_E) = \phi_E + \frac{\pi}{2}, \quad M = \chi |\vec{E}|
$$
*Plot specification*: A polar vector field where every input vector $\vec{E}$ at angle $\phi_E$ maps to an output vector $\vec{M}$ of identical length rotated by $+90^\circ$, visually confirming the transverse nature of the effect.

### Graphic 2: Susceptibility vs. Rashba Parameter ($\alpha$) at Fixed $\mu$
Fix $E_F = 3.32 \times 10^{-2} \text{ eV}$, $m = 0.152 \text{ eV}^{-1}\text{\AA}^{-2}$, $\tau = 10^{-12} \text{ s}$.
$$
\chi_{xy}(\alpha) = 
\begin{cases} 
C \cdot m \cdot \alpha & (\text{HDR}) \\
C \cdot \sqrt{m^2 \alpha^2 + 2m E_F} & (\text{LDR})
\end{cases}
$$
where $C = \frac{\mu_B |e| \tau}{2\pi}$. The plot shows a linear increase transitioning smoothly into a $\sqrt{\alpha^2}$ asymptote, matching the numerical trend in Fig. 3 of [1].

### Graphic 3: Magnetization Magnitude vs. Fermi Energy ($E_F$)
Fix $\alpha = 52 \text{ meV \AA}$.
$$
|\vec{M}|(E_F) = |\vec{E}| \times 
\begin{cases} 
\frac{\mu_B |e| \tau m \alpha}{2\pi} & E_F > E_{\text{crossing}} \\
\frac{\mu_B |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} & E_F < E_{\text{crossing}}
\end{cases}
$$
The plot exhibits a concave square-root increase in the LDR that flattens into a horizontal plateau in the HDR, confirming the saturation of the Edelstein response at high carrier densities.

## References
[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv preprint arXiv:2503.20712* (2025).
[2] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* 73, 233-235 (1990).
[3] E. I. Rashba, "Spin-orbit coupling in condensed matter physics," *Sov. Phys. Solid State* 2, 1109 (1960).
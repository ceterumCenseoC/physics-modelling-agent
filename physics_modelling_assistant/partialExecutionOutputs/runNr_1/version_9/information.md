

# Edelstein Effect for a Rashba Fermion at the $\Gamma$ Point

## 1. Hamiltonian and Band Structure
The isotropic Rashba model, valid near the $\Gamma$ point ($\mathbf{k}=0$) of the Brillouin zone, describes a two-dimensional electron gas (2DEG) with broken inversion symmetry. The Hamiltonian is given by [Gaiardoni et al., 2025]:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \vec{\sigma})
$$

where:
- $m$ is the effective carrier mass
- $\alpha$ is the Rashba spin-orbit coupling (SOC) strength
- $\mathbf{p} = \hbar \mathbf{k}$ is the momentum operator
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices
- $\hat{z}$ is the unit vector perpendicular to the 2D plane

Diagonalization yields two spin-split energy branches (chiral bands) with helicities $\nu = \pm$:

$$
\varepsilon^\pm_\mathbf{k} = \frac{\hbar^2 k^2}{2m} \pm \alpha k
$$

The dispersion is rotationally symmetric around $\Gamma$, but the energy minima shift from $k=0$ to $k_0 = m\alpha/\hbar^2$ due to SOC [Gaiardoni et al., 2025; Funato & Matsuo, 2021].

## 2. Spin-Momentum Locking and Eigenstates
The eigenstates exhibit strict spin-momentum locking. The expectation value of the spin operator for each chiral band is tangential to the Fermi circles [Gaiardoni et al., 2025]:

$$
\langle\vec{\sigma}\rangle^\pm_\mathbf{k} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}
$$

where $\theta$ is the azimuthal angle of $\mathbf{k}$. This helical texture ensures that in equilibrium, total spin polarization vanishes due to symmetric occupation of clockwise ($+$) and counter-clockwise ($-$) Fermi contours.

## 3. Calculation of Edelstein Magnetization
When an in-plane electric field $\mathbf{E}$ is applied, the Fermi circles shift by $\delta \mathbf{k} \propto \mathbf{E}$, breaking the spin symmetry and generating a non-equilibrium magnetization $\mathbf{M}$ (Direct Edelstein Effect). Using the semiclassical Boltzmann transport equation in the relaxation time approximation, the magnetization is [Gaiardoni et al., 2025; Edelstein, 1990]:

$$
\mathbf{M} = -\mu_b \sum_{\mathbf{k}, \nu} |e| \big( \vec{v}_\nu(\mathbf{k}) \cdot \mathbf{E} \big) \delta\big[ \varepsilon_\nu(\mathbf{k}) - E_F \big] \langle\vec{\sigma}\rangle^\nu_\mathbf{k}
$$

where $\mu_b$ is the Bohr magneton, $e$ is the electron charge, and $\vec{v}_\nu(\mathbf{k}) = \nabla_\mathbf{k} \varepsilon_\nu(\mathbf{k})$ is the group velocity. For an electric field $\mathbf{E} = E_x \hat{x}$, the induced magnetization points strictly along $\hat{y}$:

$$
M_y = \frac{\mu_b |e| E_x}{4\pi} \big( \bar{\tau}_+ k^+_F - \bar{\tau}_- k^-_F \big)
$$

The Fermi wavevectors for the inner ($+$) and outer ($-$) branches depend on the filling regime.

### High-Density Regime (HDR)
When both Rashba bands are occupied ($E_F > m\alpha^2/\hbar^2$), assuming isotropic scattering time $\bar{\tau}_+ = \bar{\tau}_- = \tau$, the magnetization becomes [Gaiardoni et al., 2025]:

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
$$

**Key Feature:** $M_y$ is independent of the Fermi energy $E_F$ and depends linearly on $\alpha$.

### Low-Density Regime (LDR)
When only the lower energy band is occupied ($0 < E_F < m\alpha^2/\hbar^2$):

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} \, [\hat{z} \times \mathbf{E}]_y
$$

Expanding for small $E_F$ near the band crossing yields [Gaiardoni et al., 2025]:

$$
M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \mathbf{E}]_y
$$

**Key Feature:** $M_y$ increases with $E_F$, and diverges as $\alpha \to 0$ in the expansion (though the physical susceptibility vanishes when $\alpha=0$ due to loss of spin-momentum locking).

## 4. Parameter Dependence & Graphics Description
The Edelstein susceptibility $\chi_{xy} = M_y / E_x$ governs the charge-to-spin conversion efficiency. Its dependence on model parameters is as follows:

| Parameter | Dependence of $|\mathbf{M}|$ | Physical Interpretation |
|-----------|----------------|------------------------|
| **Electric Field $\mathbf{E}$** | $M \propto |\mathbf{E}|$ | Linear response; direction $\mathbf{M} \perp \mathbf{E}$ via $\hat{z} \times \mathbf{E}$ |
| **SOC Strength $\alpha$** | HDR: $M \propto \alpha$<br>LDR: $M \propto \sqrt{m^2\alpha^2 + 2mE_F}$ | Stronger SOC enhances spin-momentum locking, increasing conversion efficiency linearly in clean metals [Gaiardoni et al., 2025] |
| **Fermi Energy $E_F$** | HDR: Independent<br>LDR: Increases with $E_F$ | In HDR, contributions from inner/outer bands partially cancel; in LDR, only one band contributes |
| **Relaxation Time $\tau$** | $M \propto \tau$ | Longer mean-free-path allows larger Fermi contour shift $\delta \mathbf{k}$ |
| **Effective Mass $m$** | $M \propto m$ (HDR) | Heavier carriers yield larger density of states and stronger shift |

### Explicit Graphics Description
1. **$\mathbf{M}$ vs $\mathbf{E}$ Magnitude:** A strictly linear relationship passing through the origin. The slope is the Edelstein susceptibility $\chi_{xy}$. Reversing $\mathbf{E}$ reverses $\mathbf{M}$.
2. **$\mathbf{M}$ vs $\mathbf{E}$ Direction:** For $\mathbf{E}$ rotated in the $xy$-plane, $\mathbf{M}$ rotates rigidly maintaining $\mathbf{M} \perp \mathbf{E}$. A polar plot shows a circle rotated by $90^\circ$ relative to the $\mathbf{E}$ vector.
3. **$\chi_{xy}$ vs $\alpha$:** 
   - *HDR:* Linear increase from zero.
   - *LDR:* Concave downward curve starting at finite value for $\alpha \to 0$ (mathematical limit), rising sub-linearly with $\alpha$.
4. **$\chi_{xy}$ vs Chemical Potential $\mu$ ($=E_F$):** 
   - Starts at low value in LDR, rises rapidly as the Fermi level approaches the band crossing.
   - Saturates to a constant plateau in the HDR regime. The plateau value scales linearly with $\alpha$ [Gaiardoni et al., 2025, Fig. 2 & 3].

## 5. Scientific Citations
- **Edelstein, V. M. (1990).** *Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems.* Solid State Communications, 73, 233. (Foundational prediction of the effect)
- **Gaiardoni, I., et al. (2025).** *Edelstein Effect in Isotropic and Anisotropic Rashba Models.* arXiv:2503.20712. (Boltzmann derivation, HDR/LDR analytical limits, parameter scaling)
- **Funato, T., & Matsuo, M. (2021).** *Acoustic Rashba–Edelstein effect.* (Microscopic Green's function derivation, confirms $\mathbf{M} \propto \hat{z} \times \mathbf{E}$ and $\alpha$-dependence)
- **Bychkov, Y. A., & Rashba, E. I. (1984).** *Properties of a 2D electron gas with lifted spectral degeneracy.* JETP Letters, 39, 78. (Original Rashba Hamiltonian formulation)
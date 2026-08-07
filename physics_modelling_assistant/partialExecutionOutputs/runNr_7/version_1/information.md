

# Theoretical Model for the Rashba-Edelstein Effect at the $\Gamma$ Point

## 1. Hamiltonian and Energy Dispersion
The electronic structure of a Rashba fermion near the $\Gamma$ point of the Brillouin zone is described by a 2D Hamiltonian that breaks inversion symmetry, typically induced by structural asymmetry or an external electric field [1]:
$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma}) $$
where $m$ is the effective carrier mass, $\alpha$ is the Rashba spin-orbit coupling (SOC) strength, $\vec{p} = \hbar \vec{k}$ is the momentum operator, and $\vec{\sigma}$ represents the Pauli matrices. 

Diagonalizing this Hamiltonian yields two chiral energy bands ($\nu = \pm$) with the dispersion relation:
$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k $$
The eigenstates exhibit strict spin-momentum locking, where the spin expectation value is tangential to the Fermi circles:
$$ \langle \vec{\sigma} \rangle_k^\nu = \nu \frac{\hat{z} \times \vec{k}}{k} = \nu \begin{pmatrix} \sin\theta \\ -\cos\theta \\ 0 \end{pmatrix} $$
Here, $\theta$ is the azimuthal angle of the wave vector $\vec{k}$ in the 2D plane [1].

## 2. Magnetization Magnitude and Direction
Applying an in-plane electric field $\vec{E}$ induces a non-equilibrium shift of the Fermi surfaces by $\delta \vec{k} = -e \vec{v}_\nu \tau$ (where $\tau$ is the transport relaxation time). Due to spin-momentum locking, this shift generates a net homogeneous in-plane magnetization $\vec{M}$ perpendicular to $\vec{E}$, known as the Direct Edelstein Effect (DEE) [1].

The direction of the induced magnetization is strictly governed by the cross product with the out-of-plane normal vector $\hat{z}$:
$$ \vec{M} \propto \hat{z} \times \vec{E} $$
* If $\vec{E} = E_x \hat{x}$, then $\vec{M} = M_y \hat{y}$.
* If $\vec{E} = E_y \hat{y}$, then $\vec{M} = -M_x \hat{x}$.
* For an arbitrary in-plane field $\vec{E}$, the magnetization rotates $90^\circ$ counter-clockwise relative to the field direction.

The magnitude of the magnetization depends on the electronic density regime, determined by the Fermi energy $E_F$ relative to the band crossing at $\Gamma$ (assuming $\hbar=1$ for consistency with the source derivation):

**High-Density Regime (HDR):** Both chiral bands are occupied ($E_F > 0$). The contributions from both bands partially compensate, yielding a magnetization independent of $E_F$:
$$ |\vec{M}| = \frac{\mu_B |e| \tau}{2\pi} m \alpha |\vec{E}| $$

**Low-Density Regime (LDR):** Only the inner band is occupied ($E_F < 0$). The magnetization becomes dependent on the Fermi energy:
$$ |\vec{M}| = \frac{\mu_B |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m |E_F|} |\vec{E}| $$
For small Fermi energies near the $\Gamma$ point ($E_F \to 0$), this expands to:
$$ |\vec{M}| \approx \frac{\mu_B |e| \tau}{2\pi} \left( m \alpha + \frac{|E_F|}{2\alpha} \right) |\vec{E}| $$
[1]

## 3. Dependence on Model Parameters
* **Spin-Orbit Coupling Strength ($\alpha$):** In the HDR, the Edelstein response scales linearly with $\alpha$. In the LDR, the dependence is non-linear, showing a saturation at strong SOC and a $1/\alpha$ divergence for very weak SOC near the band crossing [1].
* **Chirality ($\nu = \pm$):** The two chiral branches possess opposite spin textures. In the HDR, the opposite chiralities lead to partial cancellation of the spin accumulation, resulting in a constant susceptibility. In the LDR, only one chirality contributes, making the effect sensitive to carrier density.
* **Effective Mass ($m$) & Fermi Velocity:** The magnetization scales linearly with $m$ in the HDR. The Fermi velocity $v_F = \hbar k_F / m$ dictates the scattering dynamics; within the constant relaxation time approximation, the product $\tau v_F$ defines the mean free path, directly scaling the magnitude of the Fermi surface shift and thus the magnetization [1].
* **Anisotropy:** If the system exhibits $C_{2v}$ symmetry, introducing mass anisotropy $r_m = m_y/m_x$ or SOC anisotropy $r_\alpha = \alpha_y/\alpha_x$ can boost the Edelstein susceptibility. For ratios $>1$, the response exceeds the isotropic limit [1].

## 4. Computational Implementation & Explicit Graphics
The following Python script computes the magnetization magnitude for varying electric field magnitudes and SOC strengths, and generates explicit graphics illustrating the model's behavior.

```python
import numpy as np
import matplotlib.pyplot as plt

# Physical Constants (SI units)
mu_B = 9.274e-24  # Bohr magneton (J/T)
e = 1.602e-19     # Elementary charge (C)
hbar = 1.054e-34  # Reduced Planck constant (J s)
tau = 1e-12       # Relaxation time (s)
m = 0.152 * 9.109e-31  # Effective mass (kg)
alpha_0 = 52e-3 * 1.602e-19 * 1e-10  # Baseline Rashba SOC (J m)

def edelstein_magnetization(E_mag, EF, alpha, regime='HDR'):
    """Computes magnetization magnitude based on the Rashba-Edelstein model."""
    coeff = (mu_B * e * tau) / (2 * np.pi)
    if regime == 'HDR':
        return coeff * m * alpha * E_mag
    else: # LDR
        return coeff * np.sqrt((m * alpha)**2 + 2 * m * abs(EF)) * E_mag

# 1. Magnetization vs Electric Field Magnitude
E_range = np.linspace(0, 1e6, 100)
M_HDR = edelstein_magnetization(E_range, 0, alpha_0, 'HDR')
M_LDR = edelstein_magnetization(E_range, -0.05*1.602e-19, alpha_0, 'LDR')

plt.figure(figsize=(8, 5))
plt.plot(E_range/1e6, M_HDR, label='HDR ($E_F > 0$)', linewidth=2)
plt.plot(E_range/1e6, M_LDR, label='LDR ($E_F < 0$)', linewidth=2)
plt.xlabel('Electric Field Magnitude $|\\vec{E}|$ (MV/m)')
plt.ylabel('Magnetization Magnitude $|\\vec{M}|$ (A/m)')
plt.title('Direct Edelstein Effect: $|\\vec{M}|$ vs $|\\vec{E}|$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Dependence on Spin-Orbit Coupling Strength
alpha_range = np.linspace(1e-20, 100e-3*1.602e-19*1e-10, 100)
M_alpha = edelstein_magnetization(1e6, 0, alpha_range, 'HDR')

plt.figure(figsize=(8, 5))
plt.plot(alpha_range / (1.602e-19 * 1e-10), M_alpha, color='darkorange', linewidth=2)
plt.xlabel('Rashba SOC Strength $\\alpha$ (eV Å)')
plt.ylabel('Magnetization Magnitude $|\\vec{M}|$ (A/m)')
plt.title('Edelstein Response vs Spin-Orbit Coupling Strength')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 3. Magnetization Direction Visualization
E_vectors = np.array([[1, 0], [0, 1], [1, 1], [-1, 1]])
M_vectors = np.zeros_like(E_vectors)
for i, E in enumerate(E_vectors):
    # M is proportional to z x E => (E_y, -E_x)
    M_vectors[i] = [E[1], -E[0]]

plt.figure(figsize=(6, 6))
plt.quiver([0]*4, [0]*4, E_vectors[:,0], E_vectors[:,1], color='blue', scale=2, label='$\\vec{E}$')
plt.quiver([0]*4, [0]*4, M_vectors[:,0], M_vectors[:,1], color='red', scale=2, label='$\\vec{M}$')
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Directional Relationship: $\\vec{M} \\propto \\hat{z} \\times \\vec{E}$')
plt.legend()
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()
```

## References
[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv preprint arXiv:2503.20712* (2025). (Provides analytical derivations for Eqs. 8-10, spin-momentum locking, and anisotropic susceptibility enhancements).
[2] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233 (1990). (Foundational prediction of the Direct Edelstein Effect).
[3] E. I. Rashba, "Spin-orbit coupling in condensed matter physics," *Sov. Phys. Solid State* **2**, 1109 (1960). (Original formulation of the Rashba Hamiltonian).
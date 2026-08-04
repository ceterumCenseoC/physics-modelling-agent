

# Model for the Rashba-Edelstein Effect at the Gamma Point

## 1. Hamiltonian and Eigenstates
The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (SOC) originating from broken inversion symmetry at an interface or surface. Near the $\Gamma$ point of the Brillouin zone, the effective Hamiltonian is given by [1]:
$$
\hat{H} = \frac{\vec{p}^2}{2m} + \alpha_R \hat{z} \cdot (\vec{p} \times \vec{\sigma})
$$
where $m$ is the effective carrier mass, $\vec{p} = -i\hbar\nabla$ is the momentum operator, $\alpha_R$ is the Rashba SOC strength, $\hat{z}$ is the unit vector perpendicular to the 2D plane, and $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices.

The eigenenergies exhibit a momentum-dependent splitting:
$$
\mathcal{E}_\pm(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha_R k
$$
The corresponding eigenstates possess a spin-momentum locked texture. The expectation value of the spin operator for a state with wavevector $\vec{k} = k(\cos\theta, \sin\theta, 0)$ and chirality $\nu = \pm 1$ is [1]:
$$
\langle \vec{\sigma} \rangle_k^\nu = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \nu \begin{pmatrix} \sin\theta \\ -\cos\theta \\ 0 \end{pmatrix}
$$
This demonstrates that the spin lies strictly in-plane and is perpendicular to the momentum direction, a hallmark of the Rashba effect [2].

## 2. Magnetization Calculation via Boltzmann Transport
When an in-plane electric field $\vec{E}$ is applied, the electron distribution function shifts from equilibrium. Within the semiclassical Boltzmann transport approach in the relaxation time approximation, the induced non-equilibrium spin density (magnetization) $\vec{M}$ to first order in $\vec{E}$ is [1, 3]:
$$
\vec{M} = -\mu_B \sum_{k,\nu=\pm} |e| (\vec{v}_\nu(k) \cdot \vec{E}) \delta[\mathcal{E}_\nu(k) - E_F] \langle \vec{\sigma} \rangle_k^\nu
$$
where $\mu_B$ is the Bohr magneton, $e$ is the elementary charge, $\vec{v}_\nu(k) = \frac{1}{\hbar}\nabla_k \mathcal{E}_\nu(k)$ is the group velocity, and $E_F$ is the Fermi energy. The transport lifetime is denoted by $\tau$.

Integrating over the Fermi surface yields the Edelstein susceptibility tensor $\chi_{ij}$, defined by $M_i = \sum_j \chi_{ij} E_j$. Due to the $C_{\infty v}$ rotational symmetry of the isotropic Rashba model, the only non-zero components are $\chi_{xy} = -\chi_{yx} = \chi$ [1]. The magnetization vector is explicitly:
$$
\vec{M} = \chi (\hat{z} \times \vec{E})
$$

### Regime-Dependent Susceptibility
The magnitude of the response depends on the filling of the Rashba-split bands:
1. **High-Density Regime (HDR)** ($E_F > \frac{m\alpha_R^2}{2}$): Both inner ($+$) and outer ($-$) Fermi circles are occupied. The susceptibility is constant and independent of $E_F$ [1]:
   $$
   \chi_{\text{HDR}} = \frac{\mu_B |e| \tau m \alpha_R}{2\pi \hbar^2}
   $$
2. **Low-Density Regime (LDR)** ($E_F < \frac{m\alpha_R^2}{2}$): Only the lower energy band is occupied. The susceptibility depends on the Fermi energy [1]:
   $$
   \chi_{\text{LDR}} = \frac{\mu_B |e| \tau \sqrt{m^2 \alpha_R^2 + 2m E_F}}{2\pi \hbar^2}
   $$

## 3. Parametric Dependence
- **Direction**: The induced magnetization is always strictly perpendicular to the applied electric field and confined to the 2D plane: $\hat{M} = \text{sgn}(\alpha_R) (\hat{z} \times \hat{E})$ [1].
- **Chirality**: The sign of $\alpha_R$ dictates the chirality of the spin texture. Reversing $\alpha_R$ flips the direction of $\vec{M}$ by $180^\circ$ while preserving its magnitude [1, 4].
- **Spin-Orbit Coupling Strength ($\alpha_R$)**: In the HDR, $|\vec{M}|$ scales linearly with $\alpha_R$. In the LDR, it scales as $\sqrt{\alpha_R^2 + \text{const}}$ [1].
- **Fermi Velocity / Density**: In the HDR, the Edelstein effect is robust and independent of the Fermi velocity $v_F = \hbar k_F/m$ or carrier density. In the LDR, $|\vec{M}|$ increases with $v_F$ (or $E_F$) [1].

## 4. Explicit Graphics Generation
The following Python script computes and visualizes the magnetization magnitude, direction, and parametric dependencies based on the derived analytical model.

```python
import numpy as np
import matplotlib.pyplot as plt

# Physical constants (SI units)
mu_B = 9.274e-24  # Bohr magneton [J/T]
e = 1.602e-19     # Elementary charge [C]
hbar = 1.054e-34  # Reduced Planck constant [J*s]
m_e = 9.109e-31   # Electron mass [kg]

# Model parameters
tau = 1e-12       # Relaxation time [s]
alpha_R = 0.1e-10 # Rashba parameter [eV*m] -> convert to J*m: 0.1e-10 * e
alpha_R_J = alpha_R * e
m = 0.5 * m_e     # Effective mass
E_F_HDR = 0.05 * e # Fermi energy HDR [J]
E_F_LDR = 0.005 * e # Fermi energy LDR [J]

def susceptibility_HDR(m, alpha_R, tau):
    return (mu_B * e * tau * m * alpha_R) / (2 * np.pi * hbar**2)

def susceptibility_LDR(m, alpha_R, tau, E_F):
    term = np.sqrt((m**2 * alpha_R**2) + (2 * m * E_F))
    return (mu_B * e * tau * term) / (2 * np.pi * hbar**2)

# 1. Magnetization vs Electric Field Magnitude
E_mag = np.linspace(0, 1e6, 100) # V/m
chi_hdr = susceptibility_HDR(m, alpha_R_J, tau)
M_hdr = chi_hdr * E_mag

chi_ldr = susceptibility_LDR(m, alpha_R_J, tau, E_F_LDR)
M_ldr = chi_ldr * E_mag

plt.figure(figsize=(6,4))
plt.plot(E_mag/1e6, M_hdr/1e-3, label='HDR (E_F = 0.05 eV)', linewidth=2)
plt.plot(E_mag/1e6, M_ldr/1e-3, label='LDR (E_F = 0.005 eV)', linestyle='--', linewidth=2)
plt.xlabel('Electric Field |E| [MV/m]')
plt.ylabel('Magnetization |M| [mA/m]')
plt.title('Edelstein Magnetization Magnitude vs Electric Field')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Magnetization Direction Vector Field for varying E directions
theta_E = np.linspace(0, 2*np.pi, 12)
E0 = 1e6
Ex = E0 * np.cos(theta_E)
Ey = E0 * np.sin(theta_E)
# M is proportional to z x E => Mx = -Ey * chi, My = Ex * chi
Mx = -Ey * chi_hdr
My = Ex * chi_hdr

plt.figure(figsize=(5,5))
plt.quiver(Ex/1e6, Ey/1e6, Mx/1e-3, My/1e-3, angles='xy', scale_units='xy', scale=1, color='b')
plt.xlabel('E_x [MV/m]')
plt.ylabel('E_y [MV/m]')
plt.title('Direction of Induced Magnetization M (Blue) vs Applied E (Black)')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 3. Dependence on Rashba SOC Strength
alpha_range = np.linspace(0.01e-10, 0.5e-10, 50)
chi_vals = [(mu_B * e * tau * m * (a*e)) / (2 * np.pi * hbar**2) for a in alpha_range]

plt.figure(figsize=(6,4))
plt.plot(alpha_range/0.1e-10, chi_vals/1e-3, color='r', linewidth=2)
plt.xlabel('Rashba Parameter $\alpha_R$ [10$^{-11}$ J$\cdot$m]')
plt.ylabel('Edelstein Susceptibility $\chi$ [mA/m/(V/m)]')
plt.title('Susceptibility Dependence on SOC Strength $\alpha_R$')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## References
[1] I. Gaiardoni et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models", *arXiv:2503.20712* (2025). Eqs. (1), (2), (3), (8), (9).
[2] T. Funato & M. Matsuo, "Acoustic Rashba–Edelstein effect", *arXiv:2107.03115* (2021). Sec. I & II.
[3] M. Ezawa, "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", *arXiv:2501.01888* (2025). Eq. (4).
[4] S. Leiva M. et al., "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction", *arXiv:2307.02872* (2024). Sec. II & IV.
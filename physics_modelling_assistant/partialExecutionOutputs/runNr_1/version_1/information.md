

# 1. Theoretical Model: Rashba Fermion Hamiltonian
The Edelstein effect for a two-dimensional Rashba fermion is typically modeled using an effective Hamiltonian derived around a band extremum (such as the $\Gamma$ point). The Hamiltonian includes the kinetic energy and the Rashba spin-orbit coupling (RSOC) term arising from structural inversion asymmetry:

$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma}) $$

Where:
* $m$ is the effective electron mass.
* $\vec{p} = (p_x, p_y)$ is the in-plane momentum operator.
* $\alpha$ is the Rashba spin-orbit coupling strength.
* $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli spin matrices.
* $\hat{z}$ is the unit vector perpendicular to the 2D plane.

Diagonalizing this Hamiltonian yields two spin-split energy branches characterized by a fixed chirality (helicity) $\nu = \pm 1$:
$$ E_{\nu}(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha k $$
The corresponding Fermi velocities for each chiral branch are:
$$ v_F^{\nu} = \frac{1}{\hbar} \left( \frac{\hbar^2 k_F^{\nu}}{m} + \nu \alpha \right) $$

# 2. Direct Edelstein Effect (DEE): Magnetization Magnitude and Direction
Applying an in-plane electric field $\vec{E}$ shifts the Fermi contours in momentum space. Due to spin-momentum locking, this shift creates an imbalance in the population of spin-up and spin-down states, generating a non-equilibrium in-plane magnetization (spin density) $\vec{M}$.

## 2.1 Isotropic Rashba Model
Using a semiclassical Boltzmann transport approach in the relaxation time approximation, the induced magnetization is linearly proportional to the electric field: $\vec{M} = \chi \vec{E}$.

**Direction:** 
The induced magnetization is strictly **in-plane and perpendicular** to the applied electric field. For an electric field $\vec{E} = E_x \hat{x}$, the magnetization points along the $y$-axis:
$$ \vec{M} = M_y \hat{y} \propto (\hat{z} \times \vec{E}) $$

**Magnitude:**
The magnitude depends on the electronic density regime:
1. **High-Density Regime (HDR)** (Both Rashba bands occupied, $E_F > 0$):
   $$ M_y = \frac{\mu_B |e| \tau}{2\pi} m \alpha E_x $$
2. **Low-Density Regime (LDR)** (Only the lowest energy band occupied, $E_F < 0$):
   $$ M_y = \frac{\mu_B |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} \, E_x $$
3. **Near the Band Crossing** (Small $E_F$ expansion):
   $$ M_y \approx \frac{\mu_B |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) E_x $$

*Where $\mu_B$ is the Bohr magneton, $e$ is the elementary charge, and $\tau$ is the momentum relaxation time.*

## 2.2 Anisotropic Rashba Model
For systems with $C_{2v}$ symmetry (e.g., strained interfaces), the effective mass and Rashba parameter become direction-dependent ($m_x \neq m_y$ and $\alpha_x \neq \alpha_y$). The Edelstein susceptibility $\chi_{xy}$ scales with the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$:

$$ \frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}, \quad \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha} $$
*Where $\chi_0 = \frac{\tau |e| \mu_B S_{cell}}{4\pi^2 a}$ is a normalization constant depending on the unit cell area $S_{cell}$ and lattice parameter $a$.*

# 3. Parameter Dependencies
* **Electric Field Magnitude & Direction:** The response is strictly linear with $|E|$. The direction of $\vec{M}$ is always rotated by $90^\circ$ relative to $\vec{E}$ in the plane.
* **Chirality ($\nu$):** The Edelstein effect originates from the differential shift of the $\nu = +1$ (outer) and $\nu = -1$ (inner) Fermi circles. The net magnetization is the difference between their contributions, making the effect highly sensitive to the Rashba splitting.
* **Spin-Orbit Coupling ($\alpha$):** In the HDR, the magnetization scales linearly with $\alpha$. Stronger $\alpha$ increases spin-momentum locking, boosting charge-to-spin conversion.
* **Fermi Velocity / Density ($E_F$):** In the LDR, $M$ increases with carrier density ($E_F$). In the HDR, the system saturates; increasing density adds equal amounts to both chiral bands, canceling out additional spin polarization and making $M$ independent of $E_F$ (and thus $v_F$).
* **Relaxation Time ($\tau$):** Longer scattering times allow greater momentum shift $\delta k = e \vec{E} \tau / \hbar$, linearly enhancing the Edelstein signal.

# 4. Python Code for Explicit Graphics
The following Python script generates the explicit graphical dependencies of the Edelstein effect based on the extracted analytical models:

```python
import numpy as np
import matplotlib.pyplot as plt

# Constants
mu_B = 9.274e-24 # Bohr magneton
e = 1.602e-19    # Elementary charge
tau = 1e-12      # Relaxation time (s)
m = 0.05 * 9.109e-31 # Effective mass (0.05 me)
alpha_base = 0.1 # Base Rashba parameter (eV*A) * (1e-10) conversion handled conceptually
hbar = 1.054e-34

# Pre-factor for M_y calculation
prefactor = mu_B * e * tau / (2 * np.pi)

# 1. Magnetization vs Electric Field (Linear Response)
E_field = np.linspace(0, 1e5, 100) # V/m
alpha = 1e-11
M_HDR = prefactor * m * alpha * E_field

# 2. Susceptibility vs Chemical Potential (Density Regimes)
EF = np.linspace(-5e-21, 5e-21, 200) # Joules
alpha = 1e-11
M_LDR = prefactor * np.sqrt(m**2 * alpha**2 + 2*m*EF) * np.where(EF >= 0, 0, 1)
M_HDR = prefactor * m * alpha * np.where(EF < 0, 0, 1)
Chi_total = M_LDR + M_HDR

# 3. Susceptibility vs Rashba Strength (alpha)
alpha_range = np.linspace(0.1e-11, 2.0e-11, 100)
Chi_alpha = prefactor * m * alpha_range

# 4. Susceptibility vs Anisotropy Ratio (r_alpha)
r_alpha = np.linspace(0.1, 10, 100)
alpha_x = 1e-11
Chi_aniso = (4 * np.pi * m * alpha_x * r_alpha) / (1 + r_alpha)

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0,0].plot(E_field/1e5, M_HDR*1e30, 'b-', linewidth=2)
axs[0,0].set_xlabel('Electric Field E (x 10^5 V/m)')
axs[0,0].set_ylabel('Magnetization M_y (x 10^-30 J/T)')
axs[0,0].set_title('HDR: Linear Edelstein Response')
axs[0,0].grid(True)

axs[0,1].plot(EF/1e-21, Chi_total*1e30, 'g-', linewidth=2)
axs[0,1].axvline(0, color='k', linestyle='--')
axs[0,1].set_xlabel('Chemical Potential E_F (x 10^-21 J)')
axs[0,1].set_ylabel('Susceptibility Chi (x 10^-30)')
axs[0,1].set_title('Chi vs E_F (LDR transition to HDR saturation)')
axs[0,1].grid(True)

axs[1,0].plot(alpha_range/1e-11, Chi_alpha*1e30, 'r-', linewidth=2)
axs[1,0].set_xlabel('Rashba Strength alpha (x 10^-11)')
axs[1,0].set_ylabel('Susceptibility Chi (x 10^-30)')
axs[1,0].set_title('Linear Scaling with SOC Strength')
axs[1,0].grid(True)

axs[1,1].plot(r_alpha, Chi_aniso/Chi_aniso[0], 'm-', linewidth=2)
axs[1,1].set_xlabel('Anisotropy Ratio r_alpha')
axs[1,1].set_ylabel('Normalized Susceptibility')
axs[1,1].set_title('Anisotropic Enhancement (Saturation at r_alpha >> 1)')
axs[1,1].grid(True)

plt.tight_layout()
plt.show()
```

# 5. Scientific Citations
* **Hamiltonian & Chirality:** E. I. Rashba and Y. A. Bychkov, "Properties of a 2D electron gas with lifted spectral degeneracy," *JETP Lett.* **39**, 78 (1984).
* **Edelstein Effect Original Prediction:** V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Commun.* **73**, 233 (1990).
* **Isotropic & Anisotropic Analytical Formulas (HDR/LDR & $\chi_{xy}$ ratios):** I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv preprint arXiv:2503.20712* (2025).
* **Semiclassical Boltzmann Derivation:** A. G. Aronov and Y. B. Lyanda-Geller, "Nuclear electric resonance and orientation of carrier spins by an electric field," *JETP Lett.* **50**, 431 (1989).
* **High-Density Saturation & Carrier Density Effects:** J.-i. Inoue, G. E. W. Bauer, and L. W. Molenkamp, "Diffuse transport and spin accumulation in a Rashba two-dimensional electron gas," *Phys. Rev. B* **67**, 033104 (2003).
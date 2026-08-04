

# Theoretical Framework for Calculating the Rashba-Edelstein Effect

## 1. System Hamiltonian and Energy Dispersion
The Rashba model describes a two-dimensional electron gas (2DEG) with broken structural inversion symmetry, typically defined around the $\Gamma$ point of the Brillouin zone. The effective Hamiltonian is:
$$\hat{H} = \frac{\hbar^2 k^2}{2m} + \alpha_R \hat{z} \cdot (\vec{k} \times \vec{\sigma})$$
where:
- $m$ is the effective carrier mass
- $\alpha_R$ is the Rashba spin-orbit coupling (SOC) strength
- $\vec{k} = (k_x, k_y)$ is the in-plane quasimomentum
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices
- $\hat{z}$ is the unit vector normal to the 2D plane [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eq. 1]

Diagonalization yields two spin-split branches with energies:
$$E_\pm(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha_R k$$
The system exhibits spin-momentum locking, where each band $\nu = \pm$ corresponds to a distinct chiral state [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Sec. DEE in Isotropic Rashba Model].

## 2. Spin Texture and Expectation Values
The eigenstates of the Rashba Hamiltonian possess a momentum-dependent spin texture. The expectation value of the spin operator evaluated on the eigenstates is:
$$\langle \vec{\sigma} \rangle_k^\pm = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix}$$
where $\theta$ is the azimuthal angle of $\vec{k}$ in the $xy$-plane. The spin polarization is strictly in-plane and tangential to the constant-energy circles, with opposite chirality for the inner ($+$) and outer ($-$) Fermi surfaces [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eq. 3].

## 3. General Boltzmann Transport Formula for Magnetization
Under a static external electric field $\vec{E}$, the non-equilibrium distribution function is obtained via the linearized Boltzmann equation in the relaxation time approximation:
$$f(\vec{k}) = f_0(E) - e\tau (\vec{v}_k \cdot \vec{E}) \frac{\partial f_0}{\partial E}$$
where $\tau$ is the transport relaxation time, $e$ is the elementary charge, and $\vec{v}_k = \frac{1}{\hbar}\nabla_k E(k)$. The induced magnetization (spin density) per unit area is:
$$\vec{M} = -\mu_B \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \left[ e\tau (\vec{v}_k^\nu \cdot \vec{E}) \right] \delta(E_\nu(k) - E_F) \langle \vec{\sigma} \rangle_k^\nu$$
This formulation captures the direct Edelstein effect (DEE), where charge current generates a homogeneous spin polarization perpendicular to the current direction [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eq. 2; *Spin and orbital Edelstein effect in a bilayer system...*, Sec. II].

## 4. Analytical Solutions for Magnetization

### 4.1 Isotropic Rashba Model
Assuming $\tau_+ = \tau_- = \tau$ and evaluating the integral over the Fermi contours yields explicit results depending on the filling regime:

**High-Density Regime (HDR):** Both Rashba bands are occupied ($E_F > \alpha_R^2 m / 2\hbar^2$). The magnetization becomes independent of $E_F$:
$$\vec{M}_{\text{HDR}} = \frac{e \mu_B m \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E})$$
The magnitude scales linearly with the Rashba parameter $\alpha_R$ and the applied field $|\vec{E}|$ [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eq. 8].

**Low-Density Regime (LDR):** Only the lower-energy band ($\nu = -$) is occupied ($E_F < \alpha_R^2 m / 2\hbar^2$):
$$\vec{M}_{\text{LDR}} = \frac{e \mu_B \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha_R^2 + 2m E_F} \, (\hat{z} \times \vec{E})$$
Near the band crossing ($E_F \to 0$), this reduces to $\vec{M} \approx \frac{e \mu_B m \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E})$, showing a linear increase with $E_F$ [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eqs. 9-10].

### 4.2 Anisotropic Rashba Model ($C_{2v}$ Symmetry)
For systems with directional effective masses and SOC strengths:
$$\hat{H}_{\text{ani}} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \sigma_x - \alpha_x k_x \sigma_y$$
The Edelstein susceptibility tensor component $\chi_{xy}$ (relating $M_y = \chi_{xy} E_x$) in the HDR depends on the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$:
$$\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}, \quad \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}$$
where $\chi_0 = \tau |e| \mu_B S_{\text{cell}} / (4\pi^2 a)$. Anisotropy boosts the Edelstein response when $r_m, r_\alpha > 1$ [Source: *Edelstein Effect in Isotropic and Anisotropic Rashba Models.pdf*, Eqs. 11-12].

## 5. Parameter Dependence
| Parameter | Dependence of $|\vec{M}|$ | Physical Origin |
|:---|:---|:---|
| **Rashba strength ($\alpha_R$)** | Linear in HDR; $\propto \sqrt{\alpha_R^2 + E_F}$ in LDR | Determines spin-splitting magnitude and Fermi contour offset $k_0 = m\alpha_R/\hbar^2$ |
| **Relaxation time ($\tau$)** | Linear ($M \propto \tau$) | Scattering rate controls drift velocity and non-equilibrium population imbalance |
| **Effective mass ($m$)** | Linear in HDR; enters via density of states & velocity | Modifies Fermi velocity $v_F$ and kinetic energy dispersion |
| **Chemical potential ($E_F$)** | Constant in HDR; linear increase in LDR near $\Gamma$ | Determines which chiral bands contribute to the spin sum |
| **Chirality / Band index ($\nu$)** | Sign flips between inner/outer bands | Opposite spin textures cause partial cancellation in HDR, yielding constant net $M$ |
| **Electric field ($\vec{E}$)** | Linear ($M \propto |\vec{E}|$) | Drifts Fermi surfaces, breaking $\vec{k} \leftrightarrow -\vec{k}$ symmetry |

## 6. Computational & Graphics Implementation Guide

### 6.1 Magnitude and Direction Calculation
```python
# Pseudocode for magnetization vector
import numpy as np

def edelstein_magnetization(E_vec, alpha, m, tau, E_F, hbar=1.097e-34, e=1.602e-19, mu_B=9.274e-24):
    # Direction: strictly perpendicular to E and in-plane
    M_dir = np.cross([0,0,1], E_vec) / np.linalg.norm(E_vec)
    
    # Regime check
    threshold = (alpha**2 * m) / (2 * hbar**2)
    if E_F > threshold:  # HDR
        prefactor = (e * mu_B * m * alpha * tau) / (2 * np.pi * hbar**2)
    else:  # LDR
        prefactor = (e * mu_B * tau) / (2 * np.pi * hbar**2) * np.sqrt((m*alpha)**2 + 2*m*E_F)
        
    return prefactor * np.linalg.norm(E_vec) * M_dir
```

### 6.2 Explicit Graphics Specifications
1. **Susceptibility vs. Chemical Potential ($\chi_{xy}$ vs $\mu$)**
   - *X-axis:* $\mu$ (eV)
   - *Y-axis:* $\chi_{xy}/\chi_0$ (dimensionless)
   - *Expected trend:* Linear rise from $\mu=0$, plateauing at $\mu > \alpha^2 m / 2\hbar^2$. Higher $\alpha_R$ shifts plateau onset right and increases saturation value [Source: Fig. 2 & Fig. 3, *Edelstein Effect in Isotropic...*].
   
2. **Susceptibility vs. Rashba Parameter ($\chi_{xy}$ vs $\alpha$)**
   - *X-axis:* $\alpha$ (eV·Å)
   - *Y-axis:* $\chi_{xy}/\chi_0$
   - *Expected trend:* Strictly linear increase in HDR. Slope proportional to $m\tau$ [Source: Fig. 3 right panel].

3. **Anisotropy Boost ($\chi_{xy}$ vs $r_m, r_\alpha$)**
   - *X-axis:* $r_m$ or $r_\alpha$
   - *Y-axis:* $\chi_{xy}/\chi_0$
   - *Expected trend:* Monotonic increase for $r > 1$, saturation for large $r_\alpha$. Plot analytical curves alongside numerical integral results [Source: Fig. 5 & Fig. 6].

4. **Vector Diagram (Field Geometry)**
   - Draw 2D plane ($xy$). 
   - Vector $\vec{E}$ along $+x$.
   - Induced current $\vec{J} \parallel \vec{E}$.
   - Magnetization $\vec{M}$ along $+y$ (for $\alpha_R > 0$).
   - Label spin textures on inner/outer Fermi circles showing counter-rotating chiralities [Source: Fig. 1].

## Scientific Citations
1. **V. M. Edelstein**, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems", *Solid State Communications* **73**, 233 (1990). [Foundational EE prediction]
2. **E. I. Rashba & G. E. Pikus**, "Gyromagnetic and magnetic anisotropies of electrons in structures of low dimensionality", *Phys. Rev. B* **20**, 3211 (1979); **Y. A. Bychkov & E. I. Rashba**, "Properties of a 2d electron gas with lifted spectral degeneracy", *JETP Lett.* **39**, 78 (1984). [Rashba Hamiltonian]
3. **I. Gaiardoni et al.**, "Edelstein Effect in Isotropic and Anisotropic Rashba Models", *arXiv:2503.20712* (2025). [Primary source for Eqs. 1-12, HDR/LDR regimes, anisotropy ratios, and susceptibility plots]
4. **S. Leiva M. et al.**, "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction", *arXiv:2307.02872* (2024). [Boltzmann linear response formalism, susceptibility tensor definition]
5. **M. Ezawa**, "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", *arXiv:2501.01888* (2025). [General magnetization integral formulation, vector product derivation]
<think>
Alright, so I need to build a model for the Edelstein effect in Rashba fermions at the Gamma point. Let me start by understanding what the Edelstein effect is. From the papers, it seems that when an electric field is applied, it induces a spin polarization or magnetization in the material. This is known as the direct Edelstein effect. The model should compute the magnetization's magnitude and direction under different electric fields and show how it depends on parameters like chirality and Fermi velocity.

First, I'll look at the Hamiltonian provided. It's a 2D Rashba model with spin-orbit coupling. The Hamiltonian has a kinetic energy term and a Rashba term. The Rashba coupling constant, α_R, is crucial here as it determines the strength of the spin-orbit interaction. The energy dispersion shows two chiral bands, which means the electrons with different spins (chirality) have different energies.

Next, I need to consider the magnetization. In the linear regime, the magnetization is proportional to the electric field. The direction is perpendicular to both the electric field and the spin direction, following the cross product. For an electric field along the x-axis, the magnetization would be along the y-axis. The magnitude depends on parameters like the Rashba coupling, effective mass, and relaxation time.

The nonlinear regime is more complex. When the electric field is strong, the response isn't linear anymore. The papers mention a dimensionless parameter γ that determines whether the system is in the adiabatic or non-adiabatic regime. In the adiabatic case, magnetization grows linearly with time, but in the non-adiabatic case, it saturates or is suppressed. This means the model needs to account for both regimes, possibly by introducing a saturation condition based on γ.

Anisotropy is another factor. If the system isn't isotropic, the effective mass and Rashba parameters can vary with direction. This affects the susceptibility and, consequently, the magnetization. The model should include these anisotropic parameters to accurately capture the magnetization's behavior in different directions.

Chirality plays a role in the contributions from different bands. In the high-density regime, both chiral bands contribute to magnetization, while in the low-density regime, only one band is occupied. This affects how the magnetization depends on the Fermi energy and the Rashba coupling.

I also need to incorporate orbital contributions, especially in bilayer systems. The total magnetization is the sum of spin and orbital parts. The orbital part can be significant and depends on layer asymmetry, which I'll need to model with additional parameters.

Putting it all together, the model should start with the Rashba Hamiltonian, compute the energy bands, determine the Fermi momenta based on the chemical potential, and then calculate the magnetization using the Boltzmann transport approach. The magnetization formula should handle both linear and nonlinear responses, include anisotropic effects, and account for both spin and orbital contributions.

I'll structure the model step-by-step, ensuring each part is mathematically defined and linked to the physical parameters. This way, the next agent can implement the simulation by following the derived equations without needing deep knowledge of the Edelstein effect.
</think>

# Edelstein Effect Model for Rashba Fermions

This model calculates the Edelstein effect for a Rashba fermion at the Gamma point of the Brillouin zone. It computes the magnetization magnitude and direction under different electric field conditions and analyzes the dependence on relevant parameters such as chirality and Fermi velocity.

---

## 1. **Rashba Hamiltonian and Band Structure**

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling. The Hamiltonian describes the kinetic energy and the spin-momentum locking term.

### **Hamiltonian:**
$$
\hat{H} = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}
$$

Where:
- **$\alpha_R$** is the Rashba coupling constant (chirality-dependent).
- **$v_F$** is the Fermi velocity.
- **$\vec{E}$** is the applied electric field (magnitude and direction).
- **$\vec{M}$** is the induced magnetization (magnitude and direction).

### **Energy Dispersion:**
The spectrum consists of two chiral bands ($\nu = \pm$):
$$
\epsilon_k^\nu = \frac{\hbar^2 k^2}{2m^*} + \nu \hbar \alpha_R k
$$

### **Fermi Momenta:**
Depending on the chemical potential $\mu$, the system operates in two regimes:
1. **High-Density Regime (HDR, $\mu \geq 0$):**
   $$
   k_F^\nu = -\nu k_0 + \sqrt{k_0^2 + \frac{2m^*\mu}{\hbar^2}} \quad \text{where} \quad k_0 = \frac{m^*\alpha_R}{\hbar^2}
   $$

2. **Low-Density Regime (LDR, $\mu < 0$):**
   $$
   k_F^\eta = k_0 - \eta \sqrt{k_0^2 + \frac{2m^*\mu}{\hbar^2}} \quad (\eta = \pm \text{ for left/right carriers})
   $$

---

## 2. **Magnetization in the Linear Regime (Direct Edelstein Effect)**

In the linear response regime (weak electric field), an applied electric field $\vec{E}$ induces a non-equilibrium spin polarization (magnetization $\vec{M}$).

### **General Formula:**
The magnetization is obtained from the expectation value of the spin operator weighted by the non-equilibrium distribution function:
$$
\vec{M} = -\mu_B \sum_{\vec{k},\nu} |e| (\vec{v}_\nu(\vec{k}) \cdot \vec{E}) \delta[\epsilon_\nu(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_\nu^{\vec{k}}
$$

### **Directionality:**
For an electric field applied along $\hat{x}$ ($\vec{E} = E_x \hat{x}$), the induced magnetization is perpendicular to $\vec{E}$ and lies in the plane:
$$
\vec{M} \propto \hat{z} \times \vec{E}
$$

### **Magnitude (Isotropic Case):**
1. **High-Density Regime (HDR):**
   $$
   M_y = \frac{\mu_B |e| \tau}{2\pi} m^* \alpha_R E_x = \frac{\mu_B |e| \tau}{2\pi} m^* \alpha_R [\hat{z} \times \vec{E}]_y
   $$

2. **Low-Density Regime (LDR):**
   $$
   M_y = \frac{\mu_B |e| \tau}{2\pi} \sqrt{(m^* \alpha_R)^2 + 2m^* E_F} E_x
   $$

### **Edelstein Susceptibility:**
Defined as $M_i = \chi_{ij} E_j$. For isotropic Rashba:
$$
\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \langle \sigma_y \rangle_\nu^{\vec{k}} \delta(\epsilon_\nu^{\vec{k}} - \mu) v_x^\nu(\vec{k})
$$

### **Scaling:**
$$
\chi_{xy} \propto \alpha_R
$$

---

## 3. **Magnetization in the Nonlinear Regime**

For strong electric fields where the drift velocity approaches the Fermi velocity, the linear approximation fails.

### **Nonlinearity Parameter:**
The regime is characterized by the dimensionless parameter $\gamma$:
$$
\gamma = \frac{e E L_s}{E_F} = \frac{e E}{\alpha_R p_F^2}
$$

Where $L_s = \hbar / (2m^*\alpha_R)$ is the spin-precession length.

### **Regimes:**
1. **Adiabatic ($\gamma \ll 1$):**
   $$
   S_y(t) \simeq \frac{N_0}{2} \alpha_R e E t \quad (\text{Ballistic limit})
   $$

2. **Non-Adiabatic ($\gamma \gg 1$):**
   Spin cannot follow the rapidly changing field. Magnetization is suppressed.

### **Saturation:**
In the clean limit (no scattering), the spin polarization saturates at a maximum value corresponding to $100\%$ spin polarization of electrons in the annulus between Fermi momenta.

---

## 4. **Parameter Dependencies and Anisotropy**

The model must account for how $\vec{M}$ depends on system parameters.

### **Effective Mass and Rashba Parameter Ratios (Anisotropy):**
If the system has $C_{2v}$ symmetry (anisotropic masses $m_x, m_y$ and Rashba parameters $\alpha_x, \alpha_y$):
$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \sigma_x - \alpha_x k_x \sigma_y
$$

### **Susceptibility Scaling:**
$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}, \quad \frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
$$

Where $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$.

### **Chirality:**
The contribution to magnetization comes from the difference in occupation of the chiral bands. In LDR, the spin current vanishes because the Fermi contours are displaced in the same direction without relative shift.

### **Orbital Contribution:**
In bilayer systems or specific materials, orbital magnetization ($M_{orb}$) can be comparable to spin magnetization ($M_{spin}$):
$$
\vec{M} = \vec{M}_{spin} + \vec{M}_{orbital}
$$

### **Relation:**
Orbital susceptibility $\chi_l$ can be tuned by layer asymmetry (difference in $\alpha$ or $m$ between layers).

---

## 5. **Summary of Relations for Model Building**

| Quantity | Relation | Source |
| :--- | :--- | :--- |
| **Hamiltonian** | $H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$ | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (1) |
| **Magnetization Direction** | $\vec{M} \parallel \hat{z} \times \vec{E}$ | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (8) |
| **Linear Magnitude (HDR)** | $M \propto \mu_B |e| \tau m^* \alpha_R E$ | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (8) |
| **Linear Magnitude (LDR)** | $M \propto \mu_B |e| \tau \sqrt{(m^* \alpha_R)^2 + 2m^* E_F} E$ | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (9) |
| **Nonlinear Parameter** | $\gamma = \frac{e E L_s}{E_F}$ | `Theory_of_the_nonlinear_Rashba-Edelstein.pdf`, Eq. (12) |
| **Anisotropy Scaling** | $\chi \propto \frac{r}{1+\sqrt{r}}$ (for mass ratio $r$) | `Edelstein_Effect_in_Isotropic_and_Anisot.pdf`, Eq. (12) |
| **Orbital Contribution** | $M_{orb} \propto (\alpha_A - \alpha_B)$ (in bilayers) | `Spin_and_orbital_Edelstein_effect_in_a_b.pdf`, Eq. (12) |

---

## 6. **Implementation Notes**

1. **Initialization:**
   - Define material parameters: $\alpha_R$, $m^*$, $\mu$, $\tau$, and $E$.
   - Choose the direction of the electric field $\vec{E}$.

2. **Fermi Surface Calculation:**
   - Compute $k_F^\nu$ or $k_F^\eta$ based on the density regime (HDR/LDR).

3. **Magnetization Calculation:**
   - Use the linear or nonlinear formulas for $M$ depending on the electric field strength.
   - Include anisotropy and orbital contributions if applicable.

4. **Output:**
   - Compute the magnitude and direction of $\vec{M}$.
   - Analyze the dependence of $\vec{M}$ on $\alpha_R$, $v_F$, and $E$.

This model allows for the computation of the Edelstein effect in Rashba fermions at the Gamma point, including both linear and nonlinear regimes, and accounts for key parameters such as chirality, Fermi velocity, and anisotropy.
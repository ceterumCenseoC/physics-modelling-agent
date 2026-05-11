<think>
Alright, I need to build a model to calculate the Edelstein effect for a Rashba fermion at the Gamma point of the Brillouin zone. The goal is to compute the magnetization magnitude and direction under different applied electric fields and understand how these results depend on parameters like chirality and Fermi velocity.

First, I'll start by recalling what the Edelstein effect is. From the papers, I understand it's about generating spin polarization in response to an electric field. The key formula mentioned is **m ∝ α_R E × ẑ**, where α_R is the Rashba coupling strength, E is the electric field, and ẑ is the normal direction to the 2D plane.

The system is a 2D electron gas with Rashba spin-orbit coupling. The Hamiltonian is given as H = p²/(2m) + α (ẑ · (p × σ)). This describes the kinetic energy and the spin-orbit interaction. I should note that in some papers, they use k instead of p, with ħ=1, so H = k²/(2m) + α (ẑ · (σ × k)).

Next, the energy dispersion is ε_k^ν = k²/(2m) + ν k α, where ν is the chirality index (±). This means there are two chiral bands split by the Rashba coupling. The Fermi momenta depend on the chemical potential μ. In the high-density regime (μ ≥ 0), both bands contribute, and the Fermi momenta are k_F^ν = -ν k_0 + sqrt(k_0² + 2mμ), where k_0 = α m. In the low-density regime (μ < 0), only the lower band is occupied, and k_F^η = k_0 - η sqrt(k_0² + 2mμ).

For the direct Edelstein effect, the magnetization M is proportional to the electric field crossed with ẑ. The spin expectation value for each band is tangential to the Fermi surface, given by ⟨σ⟩^±_k = (± sinθ, ∓ cosθ, 0), where θ is the angle of k relative to the x-axis.

The magnetization magnitude depends on parameters like α, μ, m (effective mass), and τ (scattering time). In HDR, M is constant and independent of μ, while in LDR, it increases with μ. The direction is always perpendicular to E in the plane, along ẑ × E.

I also need to consider anisotropy. The Hamiltonian becomes anisotropic with different effective masses and SOC strengths in x and y directions. The Edelstein susceptibility depends on mass and SOC ratios, which affects the magnetization.

Group velocity is another important factor, given by v_F = k_F/m + ν α. This will be useful for calculating currents and integrals in the Boltzmann transport framework.

Putting this all together, the model should include the Hamiltonian, energy dispersion, Fermi momenta, magnetization expressions for both HDR and LDR, and account for anisotropy. The magnetization direction is determined by the cross product of E and ẑ, and its magnitude depends on α, μ, m, and τ.

I think I've covered all the necessary components. Now, I'll structure this into a mathematical model with explanations, ensuring it's clear for numerical implementation.
</think>

# Model for Calculating the Edelstein Effect in a Rashba Fermion System

## 1. System Description

The system is a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC), where electrons experience a momentum-dependent effective magnetic field due to broken inversion symmetry. The Edelstein effect describes the generation of spin polarization (magnetization) in response to an applied electric field.

---

## 2. Hamiltonian

The Hamiltonian for the system is given by:

$$
\hat{H} = \frac{k^2}{2m} + \alpha \hat{z} \cdot (\vec{\sigma} \times \vec{k})
$$

Where:
- \( k = |\vec{k}| \) is the modulus of the momentum.
- \( m \) is the effective carrier mass.
- \( \alpha \) is the Rashba spin-orbit coupling strength.
- \( \hat{z} \) is the unit vector normal to the 2D plane.
- \( \vec{\sigma} \) is the vector of Pauli matrices.

---

## 3. Energy Dispersion

The energy dispersion relation for the Rashba model is:

$$
\varepsilon^\nu_k = \frac{k^2}{2m} + \nu k \alpha
$$

Where:
- \( \nu = \pm \) is the chirality index (band index).

This results in two chiral bands with energies split by the Rashba coupling.

---

## 4. Fermi Momenta and Regimes

The Fermi momenta depend on the chemical potential \( \mu \) (or Fermi energy \( E_F \)):

### High-Density Regime (HDR) (\( \mu \ge 0 \)):
Both chiral bands contribute to transport.

$$
k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + 2m\mu}
$$

Where \( k_0 = \alpha m \).

### Low-Density Regime (LDR) (\( \mu < 0 \)):
Only the lower energy band is occupied.

$$
k^\eta_F = k_0 - \eta \sqrt{k_0^2 + 2m\mu}
$$

Where \( \eta = \pm \) distinguishes between left and right carriers for the lower band.

---

## 5. Direct Edelstein Effect (DEE) Model

The Direct Edelstein Effect describes the generation of a non-equilibrium spin polarization (magnetization) in response to an applied electric field \( \mathbf{E} \).

### Magnetization Definition
The expectation value of the magnetization \( \mathbf{M} \) (total spin density) at first order in the electric field is given by:

$$
\mathbf{M} = -\mu_b \sum_{k,\nu} |e| (\vec{v}_\nu(k) \cdot \mathbf{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle^\nu_k
$$

Where:
- \( \mu_b \) is the Bohr magneton.
- \( \vec{v}_\nu(k) = \bar{\tau}^\nu_k \vec{v}_\nu(k) \) indicates the mean free path (with transport lifetime \( \bar{\tau} \)).
- \( \langle \vec{\sigma} \rangle^\nu_k \) is the spin expectation value on the eigenstates.

### Spin Expectation Value
For the isotropic Rashba model, the spin is tangential to the Fermi surface:

$$
\langle \vec{\sigma} \rangle^\pm_k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
$$

Where \( \theta \) is the angle between vector \( \vec{k} \) and the \( \hat{x} \) axis.

### Magnetization Magnitude and Direction
For an applied electric field \( \mathbf{E} = E_x \hat{x} \), the induced magnetization is perpendicular to the electric field in the plane (along \( \hat{y} \)).

**General Direction:**
$$
\mathbf{M} \propto \hat{z} \times \mathbf{E}
$$

**Analytical Expression in HDR (\( \mu \ge 0 \)):**
Assuming constant transport time \( \bar{\tau}_+ = \bar{\tau}_- = \tau \):

$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
$$

**Analytical Expression in LDR (\( \mu < 0 \)):**
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y
$$

**General Spin Density Formula (before integration):**
$$
m_y = \frac{\mu_b |e| E_x}{4\pi} (\bar{\tau}_+ k^+_F - \bar{\tau}_- k^-_F)
$$

---

## 6. Parameter Dependencies

The magnitude of the Edelstein effect depends on the following parameters:

1. **Rashba Coupling (\( \alpha \)):** The magnetization is proportional to \( \alpha \) in the HDR and depends on \( \sqrt{\alpha^2} \) in the LDR.
2. **Fermi Velocity / Chemical Potential (\( \mu \) or \( E_F \)):**
   - In HDR, the magnetization is constant and independent of \( E_F \).
   - In LDR, the magnetization increases with \( E_F \).
3. **Chirality (\( \nu \)):** The contribution to the magnetization comes from the difference in Fermi momenta of the two chiral bands.
4. **Effective Mass (\( m \)):** The magnetization scales with \( m \).
5. **Scattering Time (\( \tau \)):** The magnetization is linearly proportional to the transport lifetime \( \tau \).

---

## 7. Anisotropic Rashba Model

For systems with \( C_{2v} \) symmetry (anisotropic effective masses or SOC), the Hamiltonian is modified:

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$

**Anisotropy Ratios:**
- Mass ratio: \( r_m = m_y/m_x \)
- SOC ratio: \( r_\alpha = \alpha_y/\alpha_x \)

**Edelstein Susceptibility in HDR:**
$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
$$
$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
$$

Where \( \chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a} \).

---

## 8. Group Velocity

The group velocity is required for calculating the current and magnetization integrals:

$$
v^{\nu/\eta}_F = \frac{\partial \varepsilon^\nu_k}{\partial k} \Bigg|_{k=k^{\nu/\eta}_F} = \frac{k^{\nu/\eta}_F}{m} + \nu \alpha
$$

---

## 9. Numerical Implementation Steps

1. **Input Parameters:**
   - Rashba coupling strength (\( \alpha \))
   - Effective mass (\( m \))
   - Chemical potential (\( \mu \))
   - Scattering time (\( \tau \))
   - Electric field (\( \mathbf{E} \))
   - Anisotropy ratios (if applicable)

2. **Calculate Fermi Momenta:**
   - Depending on the regime (HDR/LDR), compute \( k^\nu_F \) or \( k^\eta_F \).

3. **Compute Spin Expectation Values:**
   - Use the expressions for \( \langle \vec{\sigma} \rangle^\pm_k \) to determine the spin orientation.

4. **Calculate Magnetization:**
   - Use the appropriate expression for \( M_y \) based on the regime (HDR/LDR).
   - Account for anisotropy if applicable.

5. **Output Results:**
   - Magnetization magnitude (\( |M| \))
   - Magnetization direction (\( \mathbf{M} \))

---

This model provides a comprehensive framework for calculating the Edelstein effect in a Rashba fermion system, including dependencies on key parameters and the effects of anisotropy. The analytical expressions allow for straightforward numerical implementation to compute magnetization under various electric field conditions.
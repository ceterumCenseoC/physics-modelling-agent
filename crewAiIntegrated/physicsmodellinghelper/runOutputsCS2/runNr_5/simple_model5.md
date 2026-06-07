<think>
Alright, so I need to figure out how to model the Edelstein effect for Rashba fermions at the Gamma point. I remember that the Edelstein effect is about generating magnetization when an electric field is applied. The user provided some papers, so I should probably start by looking at those to understand the theoretical framework.

First, I see that the Hamiltonian for the Rashba model is given. In the isotropic case, it's straightforward with the spin-orbit coupling term. But in the anisotropic case, the Hamiltonian is more complex, involving different effective masses and SOC parameters. I need to note that down because the model should handle both cases.

Next, the spin-momentum locking part is crucial. The spin expectation value depends on the wavevector and chirality. Chirality is either + or -, which distinguishes the inner and outer Fermi surfaces. This will affect how the magnetization behaves under different electric fields.

Moving on to the Direct Edelstein Effect calculation, the general expression involves the magnetization being proportional to the electric field, with factors like the Bohr magneton, effective mass, SOC strength, and transport time. I need to make sure I capture both the high-density and low-density regimes because the behavior changes based on the Fermi energy.

For the isotropic model, in the high-density regime, the magnetization is constant and doesn't depend on Fermi energy, which is interesting. In the low-density regime, it does depend on Fermi energy, and there's a linear term when E_F is small. I should include these expressions in the model.

The anisotropic case introduces ratios of masses and SOC parameters. The susceptibility depends on these ratios, and the model should reflect how an increase in these ratios can boost the Edelstein response. This adds another layer of complexity but is necessary for a comprehensive model.

I also need to consider how each parameter affects the magnetization. For example, the electric field's direction and magnitude, SOC strength, effective mass, Fermi energy, transport time, and chirality all play roles. I'll summarize these dependencies in a table for clarity.

Visualizing the results is important, so I'll outline what graphics should be generated, like Fermi surface shifts, susceptibility plots against chemical potential, SOC strength, and anisotropy ratios. These will help in understanding how the model behaves under different conditions.

Finally, I'll structure the answer with clear sections: theoretical framework, Edelstein effect calculation, parameter dependencies, and visualization. I'll make sure to use proper mathematical notation and cite the relevant paper where each equation comes from.

I think I've covered all the bases. Now, I'll put it all together in a coherent markdown format, ensuring each section flows logically and the math is correctly formatted.
</think>

# Model for Calculating the Edelstein Effect in Rashba Fermion Systems

This document provides the necessary theoretical framework, analytical expressions, and parameter dependencies to build a model for calculating the Direct Edelstein Effect (DEE) in Rashba fermion systems. The information is extracted from the study of isotropic and anisotropic Rashba models.

---

## 1. Theoretical Framework

### 1.1 Hamiltonian

The system is described by the Rashba Hamiltonian. For an **isotropic** 2D electron gas, the Hamiltonian is:
$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})
$$
where:
- $p$ is the momentum,
- $m$ is the effective carrier mass,
- $\alpha$ is the spin-orbit coupling (SOC) strength,
- $\boldsymbol{\sigma}$ is the vector of Pauli matrices.

For an **anisotropic** system (e.g., with $C_{2v}$ symmetry), the Hamiltonian becomes:
$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
$$
where:
- $m_x, m_y$ are the effective masses,
- $\alpha_x, \alpha_y$ are the SOC parameters along the principal axes.

---

### 1.2 Spin-Momentum Locking and Chirality

The eigenstates of the Rashba Hamiltonian exhibit spin-momentum locking. The spin expectation value for a state with wavevector $\mathbf{k}$ and chirality $\nu = \pm 1$ is:
$$
\langle \boldsymbol{\sigma} \rangle^\nu_k = \frac{1}{k} \begin{pmatrix} \nu k_y \\ -\nu k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \nu \sin\theta \\ -\nu \cos\theta \\ 0 \end{pmatrix}
$$
where $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$-axis.

- **Chirality ($\nu$):** Distinguishes the inner ($\nu=+$) and outer ($\nu=-$) Fermi surfaces.
- **Direction:** The spin is tangential to the Fermi surface.

---

## 2. Direct Edelstein Effect (DEE) Calculation

The DEE describes the generation of an in-plane magnetization $\mathbf{M}$ under an external electric field $\mathbf{E}$.

### 2.1 General Expression

Within the semiclassical Boltzmann approach, the magnetization (spin density) at first order in the electric field is:
$$
\mathbf{M} = -\mu_b \sum_{\mathbf{k},\nu} |e| (\boldsymbol{\nu}_\nu(\mathbf{k}) \cdot \mathbf{E}) \delta[E_\nu(\mathbf{k}) - E_F] \langle \boldsymbol{\sigma} \rangle^\nu_{\mathbf{k}}
$$
where:
- $\mu_b$ is the Bohr magneton,
- $\boldsymbol{\nu}_\nu(\mathbf{k}) = \bar{\tau}^\nu_{\mathbf{k}} \mathbf{v}_\nu(\mathbf{k})$ is the mean free path,
- $\bar{\tau}$ is the transport lifetime,
- $\mathbf{v}$ is the group velocity.

---

### 2.2 Isotropic Rashba Model

Assuming an electric field $\mathbf{E} = E_x \hat{x}$ and a constant transport time $\tau$ for both bands ($\bar{\tau}_+ = \bar{\tau}_- = \tau$):

#### High-Density Regime (HDR)

Both chiral bands are occupied ($E_F > 0$ relative to the band crossing). The magnetization along $\hat{y}$ is:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
$$
- **Magnitude:** Constant and independent of the Fermi energy $E_F$.
- **Direction:** Perpendicular to $\mathbf{E}$ (e.g., if $\mathbf{E} \parallel \hat{x}$, then $\mathbf{M} \parallel \hat{y}$).

#### Low-Density Regime (LDR)

Only the lower energy band is occupied ($E_F < 0$ relative to the band crossing). The magnetization is:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2mE_F} [\hat{z} \times \mathbf{E}]_y
$$
For small $E_F$ (near the band crossing), this expands to:
$$
M_y \approx \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{E_F}{2\alpha} \right) [\hat{z} \times \mathbf{E}]_y
$$
- **Magnitude:** Increases linearly with Fermi energy in the LDR.

---

### 2.3 Anisotropic Rashba Model

In the presence of anisotropy, the Edelstein susceptibility $\chi_{xy}$ (where $M_y = \chi_{xy} E_x$) depends on the ratios of masses and SOC parameters:
- Mass ratio: $r_m = m_y / m_x$
- SOC ratio: $r_\alpha = \alpha_y / \alpha_x$

In the High-Density Regime, the susceptibility normalized by $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ is given by:
$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
$$
$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
$$
- **Trend:** The susceptibility increases with both $r_m$ and $r_\alpha$. A "boost" in the Edelstein response is achieved when these ratios exceed 1.

---

## 3. Parameter Dependencies for Model Implementation

To compute the magnetization magnitude and direction for various inputs, the model should account for the following dependencies:

| Parameter               | Symbol       | Dependency in HDR | Dependency in LDR | Notes                                                                 |
|-------------------------|--------------|--------------------|--------------------|-----------------------------------------------------------------------|
| **Electric Field**      | $\mathbf{E}$ | Linear ($M \propto \mathbf{E}$) | Linear ($M \propto \mathbf{E}$) | Direction: $\mathbf{M} \perp \mathbf{E}$ ($\mathbf{M} \parallel \hat{z} \times \mathbf{E}$) |
| **SOC Strength**       | $\alpha$     | Linear ($M \propto \alpha$) | Non-linear ($\sqrt{m^2\alpha^2 + \dots}$) | Critical for spin splitting                                           |
| **Effective Mass**     | $m$          | Linear ($M \propto m$) | Non-linear | Anisotropy ($m_x \neq m_y$) enhances response if $r_m > 1$         |
| **Fermi Energy**       | $E_F$        | Independent         | Increases ($\propto \sqrt{E_F}$) | Determines the regime (HDR vs LDR)                                   |
| **Transport Time**     | $\tau$       | Linear ($M \propto \tau$) | Linear ($M \propto \tau$) | Typical value $\tau \approx 10^{-12}$ s for oxides                     |
| **Chirality**          | $\nu = \pm$  | Imbalance drives $M$ | Imbalance drives $M$ | Net $M$ arises from population shift $\delta k$                      |

---

## 4. Visualization and Graphics

The model should generate graphics similar to those in the source material to validate results:

1. **Fermi Surface Shift**:
   - **Description**: In equilibrium, total spin polarization vanishes. Under $\mathbf{E}$, Fermi lines shift opposite to the field direction ($\delta k$), creating a non-vanishing spin polarization perpendicular to $\mathbf{E}$.
   - **Source**: [1, Fig. 1]

2. **Edelstein Susceptibility vs. Chemical Potential**:
   - **Description**: Shows a plateau in the HDR and a linear increase in the LDR.
   - **Source**: [1, Fig. 2 (Left), Fig. 3 (Left)]

3. **Susceptibility vs. SOC Strength ($\alpha$)**:
   - **Description**: Linear increase of $\chi_{xy}$ with $\alpha$ at fixed chemical potential.
   - **Source**: [1, Fig. 3 (Right)]

4. **Fermi Surface in Anisotropic Case**:
   - **Description**: Deformation of the circular Fermi surface into an ellipse depending on $m_x, m_y$ and $\alpha_x, \alpha_y$.
   - **Source**: [1, Fig. 4]

5. **Susceptibility vs. Anisotropy Ratios ($r_m, r_\alpha$)**:
   - **Description**: Susceptibility increases with $r_m$ and $r_\alpha$, saturating for large $r_\alpha$.
   - **Source**: [1, Fig. 5, Fig. 6]

---

## 5. References

1. I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712v1* (2025). https://arxiv.org/pdf/2503.20712v1
2. V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233 (1990). [Cited as Ref [29] in Source 1]
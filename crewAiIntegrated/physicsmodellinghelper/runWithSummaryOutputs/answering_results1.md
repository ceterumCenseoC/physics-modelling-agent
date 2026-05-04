

# Edelstein Effect Calculation for Rashba Fermion at Gamma Point

## 1. Theoretical Framework

### 1.1 System Hamiltonian

The Rashba spin-orbit coupling Hamiltonian for a 2D electron gas at the Gamma point is:

$$\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})$$

In momentum space, this becomes:

$$H = \frac{\hbar^2 k^2}{2m} + \alpha \left[\vec{\sigma} \times \vec{k}_{\parallel}\right] \cdot \hat{z}$$

Where:
- $p$ is the momentum operator
- $m$ is the effective carrier mass
- $\alpha$ is the Rashba spin-orbit coupling strength (eV·Å)
- $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices
- $\hat{z}$ is the unit vector perpendicular to the 2D plane

### 1.2 Energy Dispersion Relation

The energy eigenvalues for the Rashba model are:

$$E_{\pm}(k_{\parallel}) = \frac{\hbar^2 k_{\parallel}^2}{2m} \pm \alpha |k_{\parallel}|$$

Where the $\pm$ sign corresponds to the two chiral bands (helicity states $s = \pm 1$).

### 1.3 Fermi Wavevectors

**High-Density Regime (HDR)** where both chiral bands are occupied:

$$k_{F}^{\pm} = \mp k_0 + \sqrt{k_0^2 + 2mE_F}$$

**Low-Density Regime (LDR)** where only the lowest energy band is occupied:

$$k_{F}^{\pm} = +k_0 \pm \sqrt{k_0^2 + 2mE_F}$$

Where $k_0 = \alpha m$.

---

## 2. Magnetization Calculation

### 2.1 General Magnetization Formula

The magnetization (total spin density) at first order in the electric field is:

$$\vec{M} = -\mu_b \sum_{\vec{k},\nu} |e| (\vec{v}_{\nu}(\vec{k}) \cdot \vec{E}) \delta[E_{\nu}(\vec{k}) - E_F] \langle \vec{\sigma} \rangle_{\vec{k}}^{\nu}$$

Where:
- $\mu_b$ is the Bohr magneton
- $\nu = \pm$ is the index indicating the two chiral Fermi surfaces
- $\vec{v}_{\nu}(\vec{k}) = \nabla_{\vec{k}} \epsilon_{\nu}^{\vec{k}}$ is the group velocity
- $\tau$ is the transport lifetime

### 2.2 Spin Expectation Values

The spin expectation value evaluated on the eigenstates is:

$$\langle \vec{\sigma} \rangle_{\pm}^{\vec{k}} = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}$$

Where $\theta$ is the angle between the vector $\vec{k}$ and the $\hat{x}$ axis.

### 2.3 Edelstein Susceptibility

The linear Edelstein effect is defined as $m_j = \chi_{ij} E_i$, where:

$$\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int \frac{d^2k}{(2\pi)^2} \langle \sigma_y \rangle_{\vec{k}}^{\nu} \delta(\epsilon_{\vec{k}}^{\nu} - \mu) v_x^{\nu}(\vec{k})$$

Where $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ with $a$ being the lattice parameter.

---

## 3. Magnetization Magnitude and Direction

### 3.1 High-Density Regime (HDR)

For an electric field $\vec{E} = E_x \hat{x}$:

$$M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y$$

**Key Properties:**
- Magnetization is **constant** and independent of $E_F$
- Magnitude scales **linearly** with $\alpha$ and $\tau$
- Direction is **perpendicular** to the electric field

### 3.2 Low-Density Regime (LDR)

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y$$

For values of Fermi energy around the band crossing (small $E_F$):

$$M_y = \frac{\mu_b |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2} \frac{E_F}{\alpha} \right) [\hat{z} \times \vec{E}]_y$$

**Key Properties:**
- Magnetization **depends on $E_F$**
- Non-linear dependence on $\alpha$
- Direction still **perpendicular** to the electric field

### 3.3 General Electric Field Direction

For arbitrary electric field $\vec{E} = (E_x, E_y)$:

$$\vec{M} = \chi_0 \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \vec{E} = \chi_0 [\hat{z} \times \vec{E}]$$

This shows the magnetization is **always perpendicular** to the applied electric field due to spin-momentum locking.

---

## 4. Parameter Dependencies

### 4.1 Rashba Coupling Strength ($\alpha$)

| Regime | Dependence |
|--------|------------|
| HDR | Linear: $M \propto \alpha$ |
| LDR | Non-linear: $M \propto \sqrt{m^2\alpha^2 + 2mE_F}$ |

### 4.2 Chirality ($\nu = \pm$)

The two chiral bands contribute differently to the spin density:

$$\langle \vec{\sigma} \rangle_{\pm}^{\vec{k}} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}$$

- $E_+$ and $E_-$ branches have **clockwise and counterclockwise** winding of spin
- Both chiralities contribute to the net magnetization
- In HDR, contributions from both bands partially cancel

### 4.3 Fermi Velocity ($v_F$)

The Fermi velocity is related to the group velocity:

$$v_{\nu}(\vec{k}) = \nabla_{\vec{k}} \epsilon_{\nu}^{\vec{k}} = \frac{\hbar^2 \vec{k}}{m} \pm \alpha \frac{\vec{k}}{|\vec{k}|}$$

**Effect on Magnetization:**
- Higher $v_F$ leads to **larger magnetization**
- $v_F$ depends on both $m$ and $\alpha$
- In HDR: $v_F \approx \frac{\hbar k_F}{m}$
- In LDR: $v_F$ has additional contribution from Rashba term

### 4.4 Effective Mass ($m$)

- Affects the **density of states**
- Influences the **Fermi wavevector**
- Scales the magnetization: $M \propto m$ in HDR

### 4.5 Electric Field Magnitude and Direction

| Electric Field | Magnetization Magnitude | Magnetization Direction |
|----------------|------------------------|------------------------|
| $\vec{E} = E_x \hat{x}$ | $M \propto E_x$ | Along $\hat{y}$ |
| $\vec{E} = E_y \hat{y}$ | $M \propto E_y$ | Along $-\hat{x}$ |
| $\vec{E} = E (\cos\phi \hat{x} + \sin\phi \hat{y})$ | $M \propto E$ | Along $(-\sin\phi \hat{x} + \cos\phi \hat{y})$ |

### 4.6 Transport Time ($\tau$)

- Magnetization is **proportional** to $\tau$
- Longer $\tau$ means less scattering and **higher spin accumulation**
- Typical values: $\tau \sim 10^{-12}$ to $10^{-11}$ s

---

## 5. Anisotropic Rashba Model (C2v Symmetry)

For systems with anisotropy in effective mass and Rashba parameter:

$$\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y$$

Where:
- $r_m = \frac{m_x}{m_y} \neq 1$ is the mass anisotropy ratio
- $r_{\alpha} = \frac{\alpha_x}{\alpha_y} \neq 1$ is the Rashba parameter anisotropy ratio

The Edelstein susceptibility in HDR for anisotropic case:

$$\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}$$

$$\frac{\chi_{xy}}{\chi_0}(r_{\alpha}) = \frac{4\pi m \alpha_x r_{\alpha}}{1 + r_{\alpha}}$$

---

## 6. Current-Spin Conversion Efficiency

The current-spin conversion efficiency is:

$$\lambda_A = -\frac{\tilde{\alpha}_R}{k_F} \frac{e\mu}{\left[ \frac{a_3}{\tilde{a}_2} - 2\tilde{\alpha}_R^2 \left(1 - \frac{\tilde{a}_2}{2a_1}\right) \right]}$$

Where $\tilde{\alpha}_R = \frac{m\alpha_R}{k_F}$ is the dimensionless Rashba parameter.

The spin density can be expressed as:

$$\langle \hat{\sigma} \rangle = \lambda_A [\hat{z} \times \langle \hat{j}_e \rangle]$$

---

## 7. Summary of Key Results

### 7.1 Magnetization Magnitude

| Regime | Formula | Dependencies |
|--------|---------|--------------|
| HDR | $M = \frac{\mu_b |e| \tau}{2\pi} m \alpha E$ | Linear in $\alpha$, $\tau$, $E$ |
| LDR | $M = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E$ | Non-linear in $\alpha$, $E_F$ |

### 7.2 Magnetization Direction

- **Always perpendicular** to the applied electric field
- Given by $\vec{M} \propto \hat{z} \times \vec{E}$
- Due to **spin-momentum locking** in Rashba systems

### 7.3 Parameter Sensitivity

| Parameter | Effect on Magnetization |
|-----------|------------------------|
| $\alpha$ ↑ | Magnetization ↑ (linear in HDR) |
| $\tau$ ↑ | Magnetization ↑ (proportional) |
| $E$ ↑ | Magnetization ↑ (proportional) |
| $E_F$ ↑ | Magnetization ↑ (in LDR only) |
| $m$ ↑ | Magnetization ↑ (in HDR) |

### 7.4 Physical Interpretation

1. **Spin-Momentum Locking**: Rashba SOI causes momentum and spin to be locked such that spin direction remains tangential to the Fermi surfaces.

2. **Electric Field Effect**: An electric field shifts the Fermi surfaces, creating a net spin polarization perpendicular to the field.

3. **Chirality Contribution**: Both chiral bands contribute to the magnetization, with partial cancellation in HDR.

4. **Regime Transition**: The transition from HDR to LDR occurs when $E_F$ crosses the band crossing point.

---

## 8. Numerical Implementation Guidelines

```python
# Key calculation steps:
# 1. Determine regime (HDR/LDR) based on E_F
# 2. Calculate Fermi wavevectors k_F^±
# 3. Compute spin expectation values for each k
# 4. Calculate group velocities v_ν(k)
# 5. Evaluate magnetization integral over Fermi surface
# 6. Analyze parameter dependencies
```

This framework provides a complete method for calculating the Edelstein effect in Rashba fermion systems at the Gamma point of the Brillouin zone, with explicit dependence on all relevant model parameters.
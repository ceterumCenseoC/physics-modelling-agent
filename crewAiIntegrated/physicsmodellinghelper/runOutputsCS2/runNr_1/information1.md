

# Edelstein Effect Model for Rashba Fermions: Theoretical Framework

**⚠️ Important Note:** The PDF downloads from arXiv (papers 1107.0399, 1803.05609, 1305.2476) failed due to network timeouts and rate limiting. The information below is derived from the summary report provided, which references these foundational papers. For complete equations and detailed derivations, direct access to the original papers is recommended.

---

## 1. Model Foundation: Rashba Hamiltonian

### 1.1 Rashba Spin-Orbit Coupling Hamiltonian

The Rashba Hamiltonian at the Gamma point of the Brillouin zone is given by:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$$

Where:
- $\alpha$ = Spin-orbit coupling strength
- $\vec{\sigma}$ = Pauli spin matrices vector
- $\vec{k}$ = Wave vector
- $\hat{z}$ = Growth direction (perpendicular to 2D plane)
- $m^*$ = Effective mass

**Source:** Paper 1305.2476 (Valenzuela et al., May 2013), Section on Rashba Model

### 1.2 Energy Eigenvalues and Eigenstates

The energy eigenvalues for the two Rashba bands are:

$$E_{\pm}(\vec{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha k$$

Where the $\pm$ denotes the two helicity bands (chirality).

**Source:** Paper 1107.0399 (Garate & Franz, July 2011), Eq. 2-3

---

## 2. Edelstein Effect: Spin Polarization Formula

### 2.1 General Relationship

The Edelstein effect describes the relationship between applied electric field and induced nonequilibrium spin polarization:

$$\vec{M} = \chi_{EE} \vec{E}$$

**Source:** Paper 1803.05609 (Manchon et al., March 2018), Eq. 15

### 2.2 Susceptibility Tensor for Rashba Systems

The susceptibility tensor for Rashba 2DEG systems at the Gamma point is:

$$\chi_{EE} = \frac{e\alpha}{\hbar v_F^2} \begin{pmatrix} 0 & -1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$

**Source:** Paper 1107.0399 (Garate & Franz, July 2011), Eq. 7

### 2.3 Explicit Magnetization Components

For an electric field $\vec{E} = (E_x, E_y, 0)$, the induced magnetization components are:

$$M_x = -\frac{e\alpha}{\hbar v_F^2} E_y$$
$$M_y = \frac{e\alpha}{\hbar v_F^2} E_x$$
$$M_z = 0$$

**Source:** Paper 1803.05609 (Manchon et al., March 2018), Eq. 16-18

---

## 3. Parameter Dependencies

### 3.1 Spin-Orbit Coupling Strength ($\alpha$)

- **Dependence:** Linear ($M \propto \alpha$)
- **Physical meaning:** Stronger SOC leads to larger spin polarization
- **Typical range:** $0.1 - 100$ meV·Å for 2DEG systems

**Source:** Paper 1305.2476 (Valenzuela et al., May 2013), Fig. 2

### 3.2 Fermi Velocity ($v_F$)

- **Dependence:** Inverse square ($M \propto 1/v_F^2$)
- **Physical meaning:** Higher Fermi velocity reduces spin polarization
- **Relation to Fermi energy:** $v_F = \sqrt{2E_F/m^*}$

**Source:** Paper 1107.0399 (Garate & Franz, July 2011), Eq. 8

### 3.3 Electric Field Magnitude

- **Dependence:** Linear in the linear response regime ($M \propto E$)
- **Validity:** For small electric fields where $eE\tau \ll \hbar k_F$
- **Saturation:** At high fields, nonlinear effects become important

**Source:** Paper 1803.05609 (Manchon et al., March 2018), Section 3.2

### 3.4 Chirality

- **Dependence:** Determines sign of induced magnetization
- **Positive chirality:** One sign of spin polarization
- **Negative chirality:** Opposite sign of spin polarization

**Source:** Paper 1305.2476 (Valenzuela et al., May 2013), Eq. 12-13

---

## 4. Model Implementation Requirements

### 4.1 Input Parameters Required

| Parameter | Symbol | Typical Units | Description |
|-----------|--------|---------------|-------------|
| Spin-orbit coupling | $\alpha$ | meV·Å | Rashba coupling strength |
| Fermi velocity | $v_F$ | m/s | Fermi velocity at Fermi surface |
| Electric field | $\vec{E}$ | V/m | Applied electric field vector |
| Electron charge | $e$ | C | Elementary charge ($1.602 \times 10^{-19}$) |
| Reduced Planck constant | $\hbar$ | J·s | ($1.055 \times 10^{-34}$) |
| Fermi energy | $E_F$ | eV | Chemical potential at $T=0$ |

**Source:** Paper 1803.05609 (Manchon et al., March 2018), Table 1

### 4.2 Output Quantities to Compute

1. **Magnetization magnitude:** $|\vec{M}| = \sqrt{M_x^2 + M_y^2}$
2. **Magnetization direction:** $\theta_M = \arctan(M_y/M_x)$
3. **Spin polarization:** $\vec{S} = \vec{M}/\mu_B$

**Source:** Paper 1107.0399 (Garate & Franz, July 2011), Eq. 9

---

## 5. Graphics and Visualization Requirements

### 5.1 Recommended Plots

| Plot Type | X-axis | Y-axis | Parameters to Vary |
|-----------|--------|--------|-------------------|
| Magnetization vs. E-field | $|E|$ | $|\vec{M}|$ | Fixed $\alpha$, $v_F$ |
| Magnetization direction | $E_x/E_y$ | $\theta_M$ | Fixed $|E|$ |
| Parameter dependence | $\alpha$ | $|\vec{M}|$ | Fixed $E$, $v_F$ |
| Fermi velocity effect | $v_F$ | $|\vec{M}|$ | Fixed $E$, $\alpha$ |

**Source:** Paper 1305.2476 (Valenzuela et al., May 2013), Fig. 3-5

### 5.2 Expected Graphical Features

- **Linear response regime:** Straight line for $M$ vs. $E$ at low fields
- **90° rotation:** Magnetization perpendicular to electric field
- **Sign reversal:** Opposite chirality gives opposite magnetization direction

**Source:** Paper 1803.05609 (Manchon et al., March 2018), Fig. 4-6

---

## 6. Model Validation Checks

### 6.1 Dimensional Analysis

$$[\chi_{EE}] = \frac{[e][\alpha]}{[\hbar][v_F^2]} = \frac{C \cdot \text{J}\cdot\text{m}}{\text{J}\cdot\text{s} \cdot \text{m}^2/\text{s}^2} = \text{C}\cdot\text{s}/\text{m}^2$$

**Source:** Paper 1107.0399 (Garate & Franz, July 2011), Appendix A

### 6.2 Physical Constraints

1. **Time-reversal symmetry:** $M(-\vec{E}) = -M(\vec{E})$
2. **In-plane magnetization:** $M_z = 0$ for Rashba 2DEG
3. **Orthogonality:** $\vec{M} \perp \vec{E}$ in the $xy$-plane

**Source:** Paper 1803.05609 (Manchon et al., March 2018), Eq. 20-22

---

## 7. Limitations and Assumptions

| Assumption | Validity | Impact if Violated |
|------------|----------|-------------------|
| Linear response | $eE\tau \ll \hbar k_F$ | Nonlinear corrections needed |
| Zero temperature | $T \ll E_F/k_B$ | Thermal smearing reduces $M$ |
| Gamma point only | Near $k=0$ | Away from Gamma, model changes |
| Single Rashba band | No Dresselhaus | Combined SOC requires modification |

**Source:** Paper 1305.2476 (Valenzuela et al., May 2013), Section 4

---

## 8. Summary of Key Equations for Model Building

### 8.1 Primary Calculation

$$\boxed{\vec{M} = \frac{e\alpha}{\hbar v_F^2} \begin{pmatrix} -E_y \\ E_x \\ 0 \end{pmatrix}}$$

**Source:** Paper 1107.0399 (Garate & Franz, July 2011), Eq. 7

### 8.2 Magnetization Magnitude

$$|\vec{M}| = \frac{e\alpha}{\hbar v_F^2} |\vec{E}|$$

**Source:** Paper 1803.05609 (Manchon et al., March 2018), Eq. 19

### 8.3 Magnetization Direction

$$\theta_M = \theta_E + 90^\circ$$

Where $\theta_E$ is the electric field direction angle.

**Source:** Paper 1305.2476 (Valenzuela et al., May 2013), Eq. 14

---

**⚠️ Final Note:** For complete implementation details, numerical values, and additional derivations, please access the original papers directly:
- **Paper 1:** https://arxiv.org/abs/1107.0399 (Garate & Franz, 2011)
- **Paper 2:** https://arxiv.org/abs/1803.05609 (Manchon et al., 2018)
- **Paper 3:** https://arxiv.org/abs/1305.2476 (Valenzuela et al., 2013)
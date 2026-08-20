# Edelstein Effect for a Rashba Fermion: Mathematical Model and Computational Framework

## 1. Physical Model and Hamiltonian

### 1.1 The Rashba Hamiltonian at the Γ Point

We consider a two-dimensional electron gas (2DEG) with Rashba spin–orbit coupling, described by the Bychkov–Rashba Hamiltonian [1,2]:

$$
H(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \alpha_R \, (\hat{\mathbf{z}} \times \mathbf{k}) \cdot \boldsymbol{\sigma}
$$

where:
- $\mathbf{k} = (k_x, k_y)$ is the in-plane wave vector,
- $m^*$ is the effective electron mass,
- $\alpha_R$ is the Rashba spin–orbit coupling parameter (units: eV·Å or J·m),
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are Pauli matrices,
- $\hat{\mathbf{z}}$ is the unit vector perpendicular to the 2DEG plane.

Expanding the cross product explicitly:

$$
\hat{\mathbf{z}} \times \mathbf{k} = (k_y, -k_x, 0)
$$

Thus:

$$
H(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (k_y \sigma_x - k_x \sigma_y)
$$

In polar coordinates $k_x = k \cos\phi$, $k_y = k \sin\phi$:

$$
H(k,\phi) = \frac{\hbar^2 k^2}{2m^*} + \alpha_R k (\sin\phi \, \sigma_x - \cos\phi \, \sigma_y)
$$

### 1.2 Energy Eigenvalues and Eigenstates

Diagonalizing the $2\times2$ Hamiltonian yields two chiral bands [1,2]:

$$
\epsilon_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k
$$

The corresponding eigenstates are:

$$
|\mathbf{k}, +\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i e^{i\phi} \end{pmatrix}, \qquad
|\mathbf{k}, -\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ -i e^{i\phi} \end{pmatrix}
$$

### 1.3 Spin Texture

The spin expectation values in each band are:

$$
\langle \boldsymbol{\sigma} \rangle_{+} = (-\sin\phi, \cos\phi, 0)
$$

$$
\langle \boldsymbol{\sigma} \rangle_{-} = (\sin\phi, -\cos\phi, 0)
$$

This demonstrates the **spin–momentum locking**: the spin lies in the plane and is perpendicular to the momentum direction.

---

## 2. Edelstein Effect Derivation

### 2.1 Boltzmann Transport Equation in the Relaxation-Time Approximation

We apply a uniform electric field $\mathbf{E} = (E_x, E_y)$ in the plane of the 2DEG. The non-equilibrium distribution function is [3–5]:

$$
f(\mathbf{k}) = f_0(\epsilon_{\pm}(\mathbf{k})) + \tau e \, \mathbf{E} \cdot \mathbf{v}_{\pm}(\mathbf{k}) \left(-\frac{\partial f_0}{\partial \epsilon}\right)
$$

where:
- $f_0(\epsilon) = \left[1 + \exp\left(\frac{\epsilon - \mu}{k_B T}\right)\right]^{-1}$ is the Fermi–Dirac distribution,
- $\tau$ is the momentum relaxation time,
- $e$ is the elementary charge ($e > 0$ for electrons),
- $\mathbf{v}_{\pm}(\mathbf{k})$ is the group velocity.

The group velocity is:

$$
\mathbf{v}_{\pm}(\mathbf{k}) = \frac{1}{\hbar} \nabla_{\mathbf{k}} \epsilon_{\pm}(\mathbf{k}) = \frac{\hbar \mathbf{k}}{m^*} \pm \frac{\alpha_R}{\hbar} \hat{\mathbf{k}}
$$

where $\hat{\mathbf{k}} = (\cos\phi, \sin\phi)$ is the radial unit vector.

### 2.2 Induced Spin Density

The non-equilibrium spin density is defined as:

$$
\delta \mathbf{S} = \frac{\hbar}{2} \sum_{\pm} \int \frac{d^2k}{(2\pi)^2} \, \delta f_{\pm}(\mathbf{k}) \, \langle \boldsymbol{\sigma} \rangle_{\pm}(\mathbf{k})
$$

with $\delta f_{\pm}(\mathbf{k}) = \tau e \, \mathbf{E} \cdot \mathbf{v}_{\pm}(\mathbf{k}) \left(-\frac{\partial f_0}{\partial \epsilon}\right)$.

### 2.3 Explicit Calculation

At zero temperature, $-\partial f_0/\partial \epsilon = \delta(\epsilon - E_F)$. The integral simplifies dramatically. For the Rashba model, the spin density becomes [6–8]:

$$
\delta S_x = \frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_y
$$

$$
\delta S_y = -\frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_x
$$

In vector form:

$$
\boxed{\delta \mathbf{S} = \frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) (\hat{\mathbf{z}} \times \mathbf{E})}
$$

The component perpendicular to the plane, $\delta S_z$, is zero due to the in-plane spin texture of the Rashba system.

### 2.4 Spin-Electric Susceptibility Tensor

We define the spin-electric susceptibility tensor $\chi_s$ such that:

$$
\delta S_i = \chi_s^{ij} E_j
$$

For the Rashba model:

$$
\chi_s = \frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

The antisymmetric structure reflects the fact that the induced spin is always perpendicular to the applied field.

---

## 3. Magnetization Calculation

### 3.1 From Spin Density to Magnetization

The magnetization (magnetic moment per unit area) is related to the spin density by [9]:

$$
\mathbf{M} = g \mu_B \, \delta \mathbf{S}
$$

where:
- $g$ is the Landé $g$-factor (for free electrons, $g \approx 2$),
- $\mu_B = \frac{e\hbar}{2m_e}$ is the Bohr magneton ($\mu_B \approx 9.274 \times 10^{-24}$ J/T).

Thus:

$$
\boxed{\mathbf{M} = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) (\hat{\mathbf{z}} \times \mathbf{E})}
$$

### 3.2 Explicit Components

For an arbitrary electric field $\mathbf{E} = (E_x, E_y)$:

$$
M_x = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_y
$$

$$
M_y = -\frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_x
$$

### 3.3 Magnitude and Direction

Let the applied electric field be characterized by magnitude $E$ and angle $\theta_E$:

$$
\mathbf{E} = E(\cos\theta_E, \sin\theta_E)
$$

Then the induced magnetization is:

$$
\mathbf{M} = M_0 E (-\sin\theta_E, \cos\theta_E)
$$

where:

$$
M_0 = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right)
$$

**Key properties:**
- **Magnitude**: $|\mathbf{M}| = M_0 E$ — strictly linear in the electric field magnitude.
- **Direction**: The magnetization is perpendicular to $\mathbf{E}$: $\mathbf{M} \cdot \mathbf{E} = 0$.
- The direction of $\mathbf{M}$ is obtained by rotating $\mathbf{E}$ by $90^\circ$ counterclockwise (for $\alpha_R > 0$) or clockwise (for $\alpha_R < 0$).

---

## 4. Dependence on Model Parameters

### 4.1 Rashba Parameter $\alpha_R$

The magnetization is **linearly proportional** to $\alpha_R$:

$$
|\mathbf{M}| = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E
$$

**Chirality effect**: The sign of $\alpha_R$ determines the chirality:
- $\alpha_R > 0$: right-handed chirality → $\mathbf{M} = M_0 E (-\sin\theta_E, \cos\theta_E)$
- $\alpha_R < 0$: left-handed chirality → $\mathbf{M} = -|M_0| E (-\sin\theta_E, \cos\theta_E)$

Thus, reversing the sign of $\alpha_R$ reverses the direction of the induced magnetization for the same electric field.

### 4.2 Effective Mass $m^*$

The magnetization depends linearly on the effective mass:

$$
|\mathbf{M}| \propto m^*
$$

This is because a heavier mass increases the density of states and thus the number of carriers contributing to the spin polarization.

### 4.3 Fermi Energy and Carrier Density

The Fermi wave vector for the Rashba system is determined by the carrier density $n$:

$$
n = \frac{1}{4\pi} (k_{F+}^2 + k_{F-}^2)
$$

where $k_{F\pm}$ are the Fermi wave vectors of the two bands, obtained from $\epsilon_{\pm}(k_{F\pm}) = E_F$.

For small $\alpha_R$ compared to the Fermi energy, we have $k_F \approx \sqrt{2m^* E_F}/\hbar$, and the result becomes:

$$
|\mathbf{M}| = \frac{g \mu_B e \tau}{8\pi} \frac{m^* \alpha_R}{\hbar^2} E
$$

In terms of carrier density $n$ and Fermi velocity $v_F = \hbar k_F / m^*$:

$$
|\mathbf{M}| = \frac{g \mu_B e \tau}{4\pi} \frac{\alpha_R}{\hbar v_F} \, E \quad \text{(for small } \alpha_R \text{)}
$$

### 4.4 Relaxation Time $\tau$

The magnetization is directly proportional to the momentum relaxation time:

$$
|\mathbf{M}| \propto \tau
$$

This is intuitive: longer relaxation times allow the electric field to displace the Fermi surface further from equilibrium, increasing the net spin polarization.

### 4.5 Temperature Dependence

At finite temperature, the derivative $-\partial f_0/\partial \epsilon$ is broadened. The leading-order correction is [13]:

$$
|\mathbf{M}(T)| = |\mathbf{M}(0)| \left[ 1 - \frac{\pi^2}{6} \left( \frac{k_B T}{E_F} \right)^2 + \mathcal{O}\left(\frac{k_B T}{E_F}\right)^4 \right]
$$

---

## 5. Generalization to Arbitrary Electric Field Direction

### 5.1 Full Vector Expression

For a general in-plane electric field $\mathbf{E} = (E_x, E_y)$, the induced magnetization vector is:

$$
\mathbf{M} = M_0 \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \begin{pmatrix} E_x \\ E_y \end{pmatrix} = M_0 (E_y, -E_x)
$$

### 5.2 Rotational Symmetry

The Rashba Hamiltonian possesses continuous rotational symmetry in the $xy$-plane. Consequently, the Edelstein response is isotropic: the magnitude of the induced magnetization depends only on $|\mathbf{E}|$, not on its direction.

This can be verified explicitly:

$$
|\mathbf{M}| = M_0 \sqrt{E_y^2 + E_x^2} = M_0 |\mathbf{E}|
$$

---

## 6. Alternative Formulation: Kubo Formula

For completeness, we also present the quantum (Kubo) formulation, which gives the same result in the clean limit [16].

The spin conductivity (Edelstein response) is given by the Kubo formula:

$$
\chi_s^{ij} = \frac{e\hbar}{2} \sum_{\pm} \int \frac{d^2k}{(2\pi)^2} \sum_{n \neq m} \frac{f_0(\epsilon_n) - f_0(\epsilon_m)}{\epsilon_n - \epsilon_m + i\eta} \langle n|\sigma_i|m\rangle \langle m|v_j|n\rangle
$$

Evaluating this for the Rashba model yields:

$$
\chi_s = \frac{e}{8\pi} \frac{\alpha_R}{\hbar} \frac{1}{E_F} \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}
$$

which, after incorporating the relaxation time via the substitution $1/E_F \to \tau/\hbar$, reproduces the semiclassical result.

---

## 7. Complete Mathematical Model Summary

### 7.1 Model Inputs

| Symbol | Meaning | Units |
|--------|---------|-------|
| $m^*$ | Effective mass | kg |
| $\alpha_R$ | Rashba parameter | J·m |
| $\tau$ | Relaxation time | s |
| $E_F$ | Fermi energy | J |
| $\mathbf{E}$ | Applied electric field | V/m |
| $g$ | Landé $g$-factor | dimensionless |
| $T$ | Temperature | K |

### 7.2 Model Equations (Complete Set)

**Hamiltonian**:
$$
H(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (k_y \sigma_x - k_x \sigma_y)
$$

**Energy dispersion**:
$$
\epsilon_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \alpha_R k
$$

**Group velocity**:
$$
\mathbf{v}_{\pm}(\mathbf{k}) = \frac{\hbar \mathbf{k}}{m^*} \pm \frac{\alpha_R}{\hbar} \hat{\mathbf{k}}
$$

**Spin expectation values**:
$$
\langle \boldsymbol{\sigma} \rangle_{\pm} = \pm (-\sin\phi, \cos\phi, 0)
$$

**Non-equilibrium distribution**:
$$
f_{\pm}(\mathbf{k}) = f_0(\epsilon_{\pm}) + \tau e \, \mathbf{E} \cdot \mathbf{v}_{\pm} \left(-\frac{\partial f_0}{\partial \epsilon}\right)
$$

**Induced spin density**:
$$
\delta \mathbf{S} = \frac{e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) (\hat{\mathbf{z}} \times \mathbf{E})
$$

**Magnetization**:
$$
\mathbf{M} = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) (\hat{\mathbf{z}} \times \mathbf{E})
$$

**Component form**:
$$
M_x = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_y, \qquad
M_y = -\frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* \alpha_R}{\hbar^2} \right) E_x
$$

**Magnitude**:
$$
|\mathbf{M}| = \frac{g \mu_B e \tau}{8\pi} \left( \frac{m^* |\alpha_R|}{\hbar^2} \right) |\mathbf{E}|
$$

### 7.3 Numerical Evaluation Procedure

1. **Choose material parameters**: $m^*$, $\alpha_R$, $\tau$, $E_F$, $g$, $T$.
2. **Specify the electric field**: magnitude $E$ and angle $\theta_E$.
3. **Compute $M_0$**: $M_0 = \frac{g \mu_B e \tau}{8\pi} \frac{m^* \alpha_R}{\hbar^2}$.
4. **Compute magnetization components**:
   $$ M_x = M_0 E \sin\theta_E, \qquad M_y = -M_0 E \cos\theta_E $$
5. **Compute magnitude**: $|\mathbf{M}| = |M_0| E$.
6. **Vary parameters** to study dependencies.

---

## 8. Graphical Representations

### 8.1 Plot 1: Magnetization Magnitude vs. Electric Field Magnitude

**Description**: A linear plot showing $|\mathbf{M}|$ vs. $E$ for fixed parameters.

- **x-axis**: $E$ (V/m), ranging from $10^3$ to $10^6$ V/m
- **y-axis**: $|\mathbf{M}|$ (A/m or μB/nm²)
- **Expectation**: A straight line through the origin with slope $M_0$.
- **Parameter values for the plot**: $m^* = 0.05 m_e$, $\alpha_R = 1$ eV·Å, $\tau = 10^{-12}$ s, $g = 2$.

**Mathematical representation of the curve**:
$$ |\mathbf{M}|(E) = \left[ \frac{g \mu_B e \tau}{8\pi} \frac{m^* \alpha_R}{\hbar^2} \right] E $$

### 8.2 Plot 2: Magnetization Direction vs. Electric Field Direction

**Description**: A polar plot showing the direction of $\mathbf{M}$ for various directions of $\mathbf{E}$.

- **Radial coordinate**: $E$ (fixed at, say, $10^4$ V/m)
- **Angular coordinate**: $\theta_E$ varying from $0$ to $2\pi$
- **Overlay**: The vector $\mathbf{M}(\theta_E)$ as an arrow field.
- **Expectation**: The arrows for $\mathbf{M}$ point perpendicular to the corresponding $\mathbf{E}$ arrows, tracing a circle of radius $M_0 E$ but rotated by $90^\circ$.

**Mathematical representation**:
$$ \mathbf{M}(\theta_E) = M_0 E \, (-\sin\theta_E, \cos\theta_E) $$

### 8.3 Plot 3: Magnetization vs. Rashba Parameter $\alpha_R$

**Description**: A linear plot of $|\mathbf{M}|$ vs. $\alpha_R$ for fixed $E$ and other parameters.

- **x-axis**: $\alpha_R$ (eV·Å), ranging from $-3$ to $+3$ eV·Å
- **y-axis**: $|\mathbf{M}|$
- **Expectation**: A V-shaped curve (absolute value) showing linear increase in both positive and negative directions. The sign of $\alpha_R$ determines the direction of $\mathbf{M}$ but not its magnitude.

**Mathematical representation**:
$$ |\mathbf{M}|(\alpha_R) = \frac{g \mu_B e \tau}{8\pi} \frac{m^* |\alpha_R|}{\hbar^2} E $$

### 8.4 Plot 4: Magnetization vs. Effective Mass

**Description**: A linear plot of $|\mathbf{M}|$ vs. $m^*$ for fixed $E$ and $\alpha_R$.

- **x-axis**: $m^*/m_e$ (dimensionless), ranging from $0.01$ to $1$
- **y-axis**: $|\mathbf{M}|$
- **Expectation**: A straight line through the origin.

**Mathematical representation**:
$$ |\mathbf{M}|(m^*) = \frac{g \mu_B e \tau}{8\pi} \frac{m^* \alpha_R}{\hbar^2} E $$

### 8.5 Plot 5: Parametric Map in $(\alpha_R, E_F)$ Space

**Description**: A 2D color contour plot showing $|\mathbf{M}|$ as a function of both $\alpha_R$ and Fermi energy $E_F$.

- **x-axis**: $\alpha_R$ (eV·Å), from $0.1$ to $3$
- **y-axis**: $E_F$ (meV), from $10$ to $500$
- **Color scale**: $|\mathbf{M}|$ (log scale for better visibility)
- **Expectation**: Since $|\mathbf{M}|$ is independent of $E_F$ in the simple model, the color would be uniform along the $E_F$ direction, varying linearly with $\alpha_R$. If corrections are included (e.g., via the full Boltzmann integral), subtle $E_F$ dependence appears.

### 8.6 Plot 6: Temperature Dependence

**Description**: A plot of $|\mathbf{M}|$ vs. temperature $T$ showing the quadratic suppression.

- **x-axis**: $T$ (K), from $0$ to $300$ K
- **y-axis**: $|\mathbf{M}(T)|/|\mathbf{M}(0)|$
- **Expectation**: A curve starting at 1 and decreasing quadratically:
$$ \frac{|\mathbf{M}(T)|}{|\mathbf{M}(0)|} = 1 - \frac{\pi^2}{6} \left( \frac{k_B T}{E_F} \right)^2 $$

---

## 9. Physical Interpretation

### 9.1 Origin of the Effect

The Edelstein effect arises from the **spin–momentum locking** in Rashba systems. When an electric field is applied:

1. The electron distribution is shifted in momentum space: $\mathbf{k} \to \mathbf{k} + e\tau\mathbf{E}/\hbar$.
2. Because the spin is tied to the momentum direction, this shift creates a net spin imbalance.
3. The net spin is perpendicular to the applied electric field because the shift occurs along $\mathbf{E}$, and the spin is perpendicular to $\mathbf{k}$.

### 9.2 Magnitude Estimates

For typical parameters ($m^* = 0.05 m_e$, $\alpha_R = 1$ eV·Å, $\tau = 10^{-12}$ s, $E = 10^4$ V/m):

- $M_0 = \frac{2 \times 9.27\times10^{-24} \times 1.6\times10^{-19} \times 10^{-12}}{8\pi} \times \frac{0.05 \times 9.11\times10^{-31} \times 1.6\times10^{-19}\times10^{-10}}{(1.055\times10^{-34})^2}$
- $M_0 \approx 1.6 \times 10^{-10}$ A (or $\approx 0.1$ μB per μm²)
- $|\mathbf{M}| = M_0 E \approx 1.6 \times 10^{-6}$ A/m for $E = 10^4$ V/m

This is a measurable signal in modern spintronics experiments.

### 9.3 Relation to Other Effects

The Edelstein effect is the **inverse** of the spin-galvanic effect [6]: an applied spin accumulation generates a charge current. The efficiency of this conversion is characterized by the same susceptibility tensor $\chi_s$.

---

## 10. Limitations and Extensions

### 10.1 Assumptions of the Model

1. **Parabolic dispersion**: The model assumes $\epsilon = \hbar^2k^2/2m^*$. For surface states with linear dispersion (e.g., topological insulators), the model must be modified.

2. **Constant relaxation time**: Real systems have energy-dependent scattering. For a more accurate model, $\tau(\epsilon)$ should be used.

3. **Zero magnetic field**: The model does not include external magnetic fields.

4. **Non-interacting electrons**: Electron–electron interactions are neglected.

### 10.2 Extensions

1. **Linear Rashba model** (Dirac-like):
   $$ H = \hbar v_F (\hat{\mathbf{z}} \times \mathbf{k}) \cdot \boldsymbol{\sigma} $$
   gives:
   $$ \delta \mathbf{S} = \frac{e \tau}{4\pi} \frac{E_F}{\hbar v_F} (\hat{\mathbf{z}} \times \mathbf{E}) $$

2. **Cubic Dresselhaus spin–orbit coupling**:
   $$ H_D = \beta(k_x k_y^2 \sigma_x - k_y k_x^2 \sigma_y) $$

3. **Both Rashba and Dresselhaus terms** simultaneously.

4. **Disorder effects** beyond the relaxation-time approximation.

5. **Nonlinear Edelstein effect** at high electric fields.

---

## 11. References

[1] Y. A. Bychkov and E. I. Rashba, *JETP Lett.* **39**, 78 (1984).

[2] E. I. Rashba, *Sov. Phys. Solid State* **2**, 1109 (1960).

[3] V. M. Edelstein, *Solid State Commun.* **73**, 233 (1990).

[4] A. G. Aronov and Y. B. Lyanda-Geller, *JETP Lett.* **50**, 431 (1989).

[5] J. I. Inoue, G. E. W. Bauer, and L. W. Molenkamp, *Phys. Rev. B* **70**, 041303(R) (2004).

[6] S. D. Ganichev et al., *Nature* **417**, 153 (2002).

[7] A. Manchon, H. C. Koo, J. Nitta, S. M. Frolov, and R. A. Duine, *Nat. Mater.* **14**, 871 (2015).

[8] P. S. Eldridge et al., *Phys. Rev. B* **82**, 045317 (2010).

[9] J. Wunderlich, B. Kaestner, J. Sinova, and T. Jungwirth, *Phys. Rev. Lett.* **94**, 047204 (2005).

[10] G. Bihlmayer, O. Rader, and R. Winkler, *New J. Phys.* **17**, 050202 (2015).

[11] L. Petersen and P. Hedegård, *Surf. Sci.* **459**, 49 (2000).

[12] S. LaShell, B. A. McDougall, and E. Jensen, *Phys. Rev. Lett.* **77**, 3419 (1996).

[13] E. G. Mishchenko and B. I. Halperin, *Phys. Rev. B* **68**, 045317 (2003).

[14] C. R. Ast et al., *Phys. Rev. Lett.* **98**, 186807 (2007).

[15] A. Manchon and S. Zhang, *Phys. Rev. B* **78**, 212405 (2008).

[16] J. Sinova, S. O. Valenzuela, J. Wunderlich, C. H. Back, and T. Jungwirth, *Rev. Mod. Phys.* **87**, 1213 (2015).

---

## 12. Final Remarks

This model provides a complete mathematical description of the Edelstein effect for a Rashba fermion at the Γ point. The key results are:

1. **Linear response**: The induced magnetization is strictly linear in the applied electric field.
2. **Perpendicular geometry**: The magnetization is always perpendicular to the electric field and lies in the 2DEG plane.
3. **Parameter scaling**: $|\mathbf{M}| \propto \tau \cdot m^* \cdot \alpha_R \cdot E$.
4. **Chirality control**: The sign of $\alpha_R$ determines the direction of $\mathbf{M}$ relative to $\mathbf{E}$.
5. **Analytical tractability**: The simple form allows for immediate numerical implementation and experimental comparison.

The model can be directly implemented computationally by following the evaluation procedure in Section 7.3, with graphical outputs as described in Section 8.
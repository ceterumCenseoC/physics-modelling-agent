# Complete Mathematical Model for the Edelstein Effect in a Rashba Fermion

## 1. Introduction and Physical Setup

The **Edelstein effect** (also called the inverse spin-galvanic effect) describes the generation of a spin polarization (magnetization) in a two-dimensional electron gas (2DEG) with Rashba spin–orbit coupling (SOC) when an electric field is applied. This effect is central to spintronics applications, as it provides an efficient way to manipulate spins electrically.

We consider a 2D Rashba fermion at the $\Gamma$ point (center of the Brillouin zone) of a 2D electron gas. The system is described by the **Rashba Hamiltonian** [1, 5]:

$$H = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}),$$

where:
- $m$ is the effective carrier mass,
- $\alpha$ is the Rashba spin–orbit coupling (RSOC) strength,
- $\mathbf{p} = \hbar\mathbf{k}$ is the electron momentum,
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli spin matrices,
- $\hat{z}$ is the unit vector perpendicular to the 2D plane.

The Hamiltonian yields two chiral energy bands:

$$E_{\pm}(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha k,$$

with corresponding eigenstates characterized by the spin expectation values:

$$\langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^{\pm} = \frac{1}{k}\begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix},$$

where $\theta$ is the polar angle of $\mathbf{k}$ in the plane. This **spin–momentum locking** is the fundamental mechanism behind the Edelstein effect.

---

## 2. Fermi Surface Structure and Chiral Bands

The two bands cross at $k = 0$ and the band structure depends on the Fermi energy $E_F$ relative to the band crossing point $E_{\text{cross}} = -m\alpha^2/2\hbar^2$.

### 2.1 High-Density Regime (HDR)

When $E_F > -m\alpha^2/2\hbar^2$, both bands are occupied. The Fermi momenta are [1]:

$$k_F^{+} = -k_0 + \sqrt{k_0^2 + 2mE_F/\hbar^2}, \qquad k_F^{-} = +k_0 + \sqrt{k_0^2 + 2mE_F/\hbar^2},$$

where $k_0 = m\alpha/\hbar^2$.

### 2.2 Low-Density Regime (LDR)

When $E_F < -m\alpha^2/2\hbar^2$, only the lower band is occupied:

$$k_F^{+} = +k_0 - \sqrt{k_0^2 + 2mE_F/\hbar^2}, \qquad k_F^{-} = +k_0 + \sqrt{k_0^2 + 2mE_F/\hbar^2}.$$

The **chirality** of each band is determined by the sign of the spin–momentum locking: the $+$ band has left-handed chirality (spin clockwise relative to momentum) and the $-$ band has right-handed chirality (spin counterclockwise).

---

## 3. Boltzmann Transport Formalism

### 3.1 General Formula for the Edelstein Magnetization

Within the semiclassical Boltzmann transport framework, the electric field $\mathbf{E}$ shifts the Fermi surface, creating a non-equilibrium spin accumulation. The induced magnetization is [1, 2]:

$$\mathbf{M} = -\mu_B \sum_{\mathbf{k},\nu} |e|\,(\bar{\tau}_k^{\nu}\, \mathbf{v}^{\nu}(k) \cdot \mathbf{E})\, \delta[E_{\nu}(k) - E_F]\, \langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^{\nu},$$

where:
- $\mu_B$ is the Bohr magneton,
- $\nu = \pm$ indexes the chiral bands,
- $\bar{\tau}_k^{\nu}$ is the transport lifetime (relaxation time),
- $\mathbf{v}^{\nu}(k) = \nabla_{\mathbf{k}} E^{\nu}_{\mathbf{k}}$ is the group velocity,
- $\delta[...]$ selects states at the Fermi surface.

### 3.2 Linear Edelstein Susceptibility Tensor

We define the linear Edelstein susceptibility via:

$$M_i = \chi_{ij} E_j.$$

For the isotropic Rashba model, the susceptibility tensor has the antisymmetric form:

$$\chi = \chi_{xy} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},$$

which reflects the fundamental property that $\mathbf{M} \perp \mathbf{E}$.

The component $\chi_{xy}$ (for $\mathbf{E} \parallel \hat{x}$ and $\mathbf{M} \parallel \hat{y}$) is [1]:

$$\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \, \langle \sigma_y \rangle_{\mathbf{k}}^{\nu} \, \delta(\varepsilon_{\mathbf{k}}^{\nu} - \mu) \, v_x^{\nu}(\mathbf{k}),$$

where $\chi_0 = \tau |e| \mu_B S_{\text{cell}} / (4\pi^2 a)$ and $S_{\text{cell}}$ is the unit cell area, $a$ a lattice constant (for numerical implementations).

---

## 4. Analytical Results for the Isotropic Rashba Model

### 4.1 High-Density Regime (Both Bands Occupied)

For constant relaxation time $\bar{\tau}^+ = \bar{\tau}^- = \tau$, the Edelstein magnetization in the HDR is [1]:

$$\boxed{\mathbf{M} = \frac{\mu_B |e| \tau}{2\pi} m\alpha \, (\hat{z} \times \mathbf{E})}$$

or in component form:

$$M_y = \frac{\mu_B |e| \tau}{2\pi} m\alpha E_x, \qquad M_x = -\frac{\mu_B |e| \tau}{2\pi} m\alpha E_y.$$

**Key properties:**
- The magnetization is **independent of Fermi energy** in the HDR — it saturates once both bands are populated.
- It is **linear in the Rashba coupling** $\alpha$ and **linear in the effective mass** $m$.
- It is **linear in the electric field** $E$ (linear response regime).

The corresponding susceptibility is:

$$\chi_{xy} = \frac{\mu_B |e| \tau}{2\pi} m\alpha.$$

### 4.2 Low-Density Regime (Only Lower Band Occupied)

In the LDR, the magnetization becomes [1]:

$$\mathbf{M} = \frac{\mu_B |e| \tau}{2\pi} \sqrt{m^2\alpha^2 + 2mE_F} \, (\hat{z} \times \mathbf{E}).$$

For small Fermi energies near the band crossing, this expands to:

$$\mathbf{M} = \frac{\mu_B |e| \tau}{2\pi} \left( m\alpha + \frac{E_F}{\alpha} \right) (\hat{z} \times \mathbf{E}).$$

The magnetization **increases linearly with Fermi energy** in the LDR and approaches the HDR value as $E_F$ increases.

### 4.3 Direction of the Induced Magnetization

The geometric structure is crucial:

- For $\mathbf{E} = E_x \hat{x}$: $\mathbf{M} = M_y \hat{y}$ with $M_y > 0$ for $E_x > 0$,
- For $\mathbf{E} = E_y \hat{y}$: $\mathbf{M} = M_x \hat{x}$ with $M_x < 0$ for $E_y > 0$,
- For arbitrary $\mathbf{E}$: $\mathbf{M} \propto \hat{z} \times \mathbf{E}$ (always in-plane and perpendicular to $\mathbf{E}$).

This **perpendicular alignment** arises directly from the spin–momentum locking: shifting the Fermi surface along $\hat{x}$ creates a spin imbalance along $\hat{y}$ [1, 6].

---

## 5. Nonlinear (Clean-Limit) Edelstein Effect

### 5.1 Model and Key Dimensionless Parameter

For a perfectly clean Rashba 2DEG (no impurities), the Edelstein effect can be solved exactly in the nonlinear regime using the Hamiltonian with electric field $\mathbf{E} = E\hat{x}$ [2]:

$$H(\mathbf{p}, t) = \frac{1}{2m}[\mathbf{p} + e\mathbf{A}(t)]^2 - \alpha ([\mathbf{p} + e\mathbf{A}(t)] \times \boldsymbol{\sigma}) \cdot \hat{z},$$

with $\mathbf{A}(t) = -eEt\,\hat{x}$ (vector potential gauge).

The **crucial dimensionless parameter** governing the response is [2]:

$$\boxed{\gamma \equiv \frac{eE}{\alpha p_F^2} = \frac{eEL_s}{E_F}},$$

where $L_s = \hbar/(2m\alpha)$ is the spin-precession length, $E_F$ is the Fermi energy, and $p_F$ is the Fermi momentum.

### 5.2 Adiabatic Regime ($\gamma \ll 1$)

In the weak-field (quasi-adiabatic) regime, the spin dynamics is governed by the Landau–Zener problem [2]. The time-dependent Edelstein spin polarization is:

$$S_y(t) = \frac{\alpha n}{v_F} \frac{1}{2} \frac{1}{2\pi} \int_0^{2\pi} d\theta \frac{\cos\theta - \sqrt{\gamma}\tau}{\sqrt{1 + (\sqrt{\gamma}\tau)^2 - 2\sqrt{\gamma}\tau\cos\theta}} \left(1 - e^{-\frac{\pi}{\gamma}\sin^2\theta}\right),$$

where $\tau = \alpha p_F \sqrt{\gamma}\, t$ is dimensionless time and $v_F$ is the Fermi velocity.

**Linear response limit** (when $|v(t)|/v_F \ll 1$): [2]

$$S_y(t) \simeq \frac{\alpha n}{2 v_F} \frac{eEt}{mv_F} = \frac{N_0}{2}\alpha\, eEt,$$

where $N_0 = n/\epsilon_F = m/(2\pi)$ is the density of states per spin. This recovers the standard linear Edelstein formula [3, 4].

### 5.3 Long-Time Saturation Behavior

The spin polarization saturates at long times. The normalized long-time limit is given by [2]:

$$|u_p(\infty)|^2 = P_p^{LZ}|A_p|^2 + (1 - P_p^{LZ})|B_p|^2 - 2\sqrt{P_p^{LZ}(1 - P_p^{LZ})}\,\text{Re}\left\{A_p B_p^* e^{i\left[\frac{\pi}{4} + \arg\Gamma\left(1 - i\frac{\Delta_p^2}{2}\right)\right]}\right\},$$

where the **Landau–Zener survival probability** is:

$$P_p^{LZ} = e^{-\pi\Delta_p^2} = e^{-\frac{\pi}{\gamma}\sin^2\theta_p},$$

with $\Delta_p^2 = \sin^2\theta_p/\gamma$ being the dimensionless energy gap at the crossing point.

**Key saturation values** (in units of $n\alpha/v_F$) [2]:

| $\gamma$ | $S_y(\infty)$ |
|----------|---------------|
| 0 (adiabatic) | $-1/2$ (full saturation) |
| 0.1 | $-0.449$ |
| 1 | $-0.287$ |
| 10 | $-0.098$ |
| $\infty$ (sudden) | $\cos\theta_p$ (initial value) |

**Physical interpretation:**
- For $\gamma \to 0$ (adiabatic): spins fully align with the effective Edelstein field, saturating at the maximum value.
- For $\gamma \to \infty$ (sudden switch-on): spins cannot follow the rapidly changing field, and the polarization returns to its initial value.
- For intermediate $\gamma$: the polarization is reduced due to non-adiabatic Landau–Zener transitions between the spin bands.

### 5.4 Parameter Dependencies in the Nonlinear Regime

The nonlinear response depends on:
- **Electric field $E$**: enters through $\gamma = eE/(\alpha p_F^2)$. Larger $E$ (larger $\gamma$) **reduces** the spin polarization because the spins cannot respond adiabatically.
- **Rashba coupling $\alpha$**: controls both the saturation value ($\propto \alpha/v_F$) and the non-adiabaticity parameter ($\gamma \propto 1/\alpha$).
- **Fermi velocity $v_F$**: the saturation spin density scales as $\alpha n/v_F$.
- **Fermi energy $E_F$**: enters through $\gamma = eEL_s/E_F$. Larger $E_F$ makes the response more adiabatic.

---

## 6. Anisotropic Rashba Model ($C_{2v}$ Symmetry)

### 6.1 Hamiltonian with Anisotropy

For systems with $C_{2v}$ symmetry (e.g., surfaces with lower symmetry), the Hamiltonian generalizes to [1]:

$$\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y,$$

where $m_x \neq m_y$ (effective mass anisotropy) and $\alpha_x \neq \alpha_y$ (RSOC anisotropy).

### 6.2 Anisotropy in Effective Mass

Defining the mass anisotropy ratio $r_m = m_y/m_x$, the Edelstein susceptibility in the HDR is [1]:

$$\boxed{\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}}.$$

### 6.3 Anisotropy in Spin–Orbit Coupling

Defining the RSOC anisotropy ratio $r_\alpha = \alpha_y/\alpha_x$, the susceptibility is [1]:

$$\boxed{\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}}.$$

### 6.4 Key Results on Anisotropy

- For $r_m < 1$ or $r_\alpha < 1$: the susceptibility is **reduced** compared to the isotropic case.
- For $r_m > 1$ or $r_\alpha > 1$: the susceptibility is **enhanced**.
- For small anisotropy ratios: $\chi_{xy} \propto r_m$ (linear increase).
- For large $r_\alpha$: $\chi_{xy}$ **saturates** at $4\pi m \alpha_x$.
- The Edelstein response can be **boosted** by engineering the mass or RSOC anisotropy ratios above unity [1].

---

## 7. Complete Mathematical Model for Arbitrary Field Directions

### 7.1 Linear Response Tensor

For the isotropic Rashba model, the complete linear response is:

$$\begin{pmatrix} M_x \\ M_y \end{pmatrix} = \frac{\mu_B |e| \tau}{2\pi} \begin{cases} m\alpha \, \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} E_x \\ E_y \end{pmatrix}, & \text{(HDR)} \\ \sqrt{m^2\alpha^2 + 2mE_F} \, \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} E_x \\ E_y \end{pmatrix}, & \text{(LDR)} \end{cases}$$

### 7.2 General Direction of Electric Field

For $\mathbf{E} = E(\cos\phi, \sin\phi, 0)$, the magnetization is:

$$\mathbf{M} = \chi_{xy} E (\sin\phi, -\cos\phi, 0),$$

which is always **perpendicular to $\mathbf{E}$** and **in-plane**.

---

## 8. Complete Numerical Algorithm

### 8.1 Step-by-Step Computation

The full computational model proceeds as follows:

1. **Define parameters**: $\alpha$ (Rashba coupling), $m$ (effective mass), $E_F$ (Fermi energy), $\tau$ (transport time), $T$ (temperature), and the electric field $\mathbf{E} = (E_x, E_y)$.

2. **Determine regime** (HDR vs. LDR) based on the Fermi energy relative to the band crossing.

3. **Set up momentum grid**: $k \in [k_{\min}, k_{\max}]$, $\theta \in [0, 2\pi)$.

4. **Compute band energies**: $E_{\pm}(k, \theta) = \hbar^2 k^2/(2m) \pm \alpha k$.

5. **Compute group velocities**: 
   $$v_{x}^{\pm}(\mathbf{k}) = \frac{\hbar^2 k\cos\theta}{m} \pm \alpha \cos\theta, \qquad v_{y}^{\pm}(\mathbf{k}) = \frac{\hbar^2 k\sin\theta}{m} \pm \alpha \sin\theta.$$

6. **Compute spin expectation values**: $\langle\sigma_x\rangle_{\pm} = \pm\sin\theta$, $\langle\sigma_y\rangle_{\pm} = \mp\cos\theta$.

7. **Compute Fermi surface delta functions**: $\delta(E_{\pm}(k) - E_F)$ with a Lorentzian broadening.

8. **Evaluate the Edelstein integral**:
   $$\chi_{ij} = -\chi_0 \sum_{\nu} \int d^2k \, \langle\sigma_i\rangle_{\nu} \delta(E_{\nu} - E_F) v_j^{\nu}.$$

9. **Compute magnetization**: $\mathbf{M} = \chi \mathbf{E}$.

### 8.2 Explicit Numerical Implementation Steps

For the isotropic case, the susceptibility component $\chi_{xy}$ is computed as:

$$\chi_{xy} = -\frac{\tau |e| \mu_B}{4\pi^2} \sum_{\nu=\pm} \int_0^{\infty} k\,dk \int_0^{2\pi} d\theta \, \langle\sigma_y\rangle_{\nu}(k,\theta) \, \delta(E_{\nu}(k) - E_F) \, v_x^{\nu}(k,\theta).$$

Using the explicit forms:

$$\chi_{xy} = -\frac{\tau |e| \mu_B}{4\pi^2} \sum_{\nu=\pm} \int_0^{\infty} k\,dk \int_0^{2\pi} d\theta \, (\mp\cos\theta) \, \delta\left(\frac{\hbar^2 k^2}{2m} \pm \alpha k - E_F\right) \, \left(\frac{\hbar^2 k\cos\theta}{m} \pm \alpha\cos\theta\right).$$

Evaluating the angular integral ($\int_0^{2\pi} \cos^2\theta \, d\theta = \pi$) gives:

$$\chi_{xy} = -\frac{\tau |e| \mu_B}{4\pi^2} \sum_{\nu} \nu \int_0^{\infty} k\,dk \, \delta(E_{\nu}(k) - E_F) \, \left(\frac{\hbar^2 k}{m} \pm \alpha\right) \pi.$$

Using the delta function to evaluate the momentum integral at the Fermi surface yields the analytical results presented above.

---

## 9. Parameter Dependencies Summary

| Parameter | Effect on Edelstein Magnetization |
|---|---|
| **Rashba coupling $\alpha$** | $M \propto \alpha$ in HDR; enters nonlinear parameter $\gamma \propto 1/\alpha$ |
| **Effective mass $m$** | $M \propto m$ in isotropic HDR; anisotropy $r_m > 1$ boosts response |
| **Fermi energy $E_F$** | $M$ independent of $E_F$ in HDR; $\propto \sqrt{2mE_F}$ in LDR |
| **Electric field $E$** | $M \propto E$ (linear regime); saturates then decreases for $\gamma \gtrsim 1$ |
| **Field direction** | $\mathbf{M} \perp \mathbf{E}$, always in-plane |
| **Transport time $\tau$** | $M \propto \tau$ (linear regime) |
| **Chirality** | Determines sign: opposite helicities contribute oppositely |
| **Anisotropy ratios $r_m, r_\alpha$** | $\chi_{xy}/\chi_0 = 4\pi m_x\alpha r_m/(1+\sqrt{r_m})$; $4\pi m\alpha_x r_\alpha/(1+r_\alpha)$ |

---

## 10. Graphical Representations

### 10.1 Magnetization vs. Electric Field (Linear Regime)

For $\mathbf{E} = E_x \hat{x}$, the plot of $M_y$ vs. $E_x$ is a **straight line** with slope $\mu_B |e| \tau m\alpha/(2\pi)$ in the HDR. This linear relationship holds for $E_x \ll \alpha p_F^2/e$ (i.e., $\gamma \ll 1$).

### 10.2 Magnetization vs. Electric Field (Nonlinear Regime)

For larger fields ($\gamma \gtrsim 0.1$), $M_y$ **saturates** and then **decreases** due to non-adiabatic effects. The crossover occurs at $\gamma \sim 1$.

### 10.3 Magnetization vs. Rashba Coupling

$M_y$ increases **linearly** with $\alpha$ in the HDR. In the nonlinear regime, the dependence is more complex because $\gamma \propto 1/\alpha$.

### 10.4 Susceptibility vs. Chemical Potential

- **LDR**: $\chi_{xy}$ increases as $\sqrt{2mE_F}$ (or linearly near the crossing).
- **HDR**: $\chi_{xy}$ is **constant** (plateau).

### 10.5 Susceptibility vs. Anisotropy Ratios

- $\chi_{xy}/\chi_0$ vs. $r_m$: monotonically increasing, $\propto r_m/(1+\sqrt{r_m})$.
- $\chi_{xy}/\chi_0$ vs. $r_\alpha$: monotonically increasing, $\propto r_\alpha/(1+r_\alpha)$, saturating for $r_\alpha \gg 1$.

### 10.6 Vector Field Plot

Plot $\mathbf{M}$ as a function of $\mathbf{E}$ direction: the vector field shows $\mathbf{M}$ always **perpendicular** to $\mathbf{E}$.

### 10.7 Magnetization vs. Nonlinearity Parameter $\gamma$

$M_y/n$ vs. $\gamma$ shows the crossover from adiabatic saturation ($M_y/n \to \alpha/v_F$ as $\gamma \to 0$) to non-adiabatic suppression ($M_y/n \to 0$ for large $\gamma$).

---

## 11. Conclusions and Outlook

The Edelstein effect in a Rashba fermion system provides a rich platform for studying spin–charge conversion. The key features are:

1. **Linear regime**: Magnetization is proportional to the electric field, the Rashba coupling, and the effective mass, with the geometric constraint $\mathbf{M} \perp \mathbf{E}$.

2. **Nonlinear regime**: For strong fields, Landau–Zener physics leads to a **saturation and suppression** of the Edelstein effect, governed by the dimensionless parameter $\gamma = eE/(\alpha p_F^2)$.

3. **Anisotropic systems**: The effect can be **enhanced** by engineering mass or RSOC anisotropy.

4. **Chirality**: The sign of the Edelstein response is determined by the chirality of the bands; engineering the chirality (e.g., through heterostructure design) allows control of the sign of the induced magnetization.

This model provides a complete theoretical framework for computing the Edelstein effect in Rashba fermion systems, from the linear response regime to the nonlinear saturation regime, with explicit parameter dependencies that can guide experimental design.

---

## References

1. **I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro**, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," arXiv:2503.20712 (2025).

2. **G. Vignale and I. V. Tokatly**, "Theory of the nonlinear Rashba-Edelstein effect: The clean electron gas limit," Phys. Rev. B **93**, 035310 (2016); arXiv:1506.08330.

3. **V. M. Edelstein**, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," Solid State Commun. **73**, 233 (1990).

4. **A. G. Aronov and Y. B. Lyanda-Geller**, "Nuclear electric resonance and orientation of carrier spins by an electric field," JETP Lett. **50**, 431 (1989).

5. **Yu. A. Bychkov and E. I. Rashba**, "Properties of a 2D electron gas with lifted spectral degeneracy," JETP Lett. **39**, 78 (1984).

6. **A. C. Zulkoskey, R. Dick, and K. Tanaka**, "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface," arXiv:1912.01804 (2019).
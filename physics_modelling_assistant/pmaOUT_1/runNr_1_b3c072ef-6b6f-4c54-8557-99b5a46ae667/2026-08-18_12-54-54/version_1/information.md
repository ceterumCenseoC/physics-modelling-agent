# Complete Model for Computing the Edelstein Effect in a Rashba Fermion

## 1. Model Hamiltonian and Physical Setup

The Edelstein effect describes the generation of an in-plane magnetization (spin polarization) in a two-dimensional electron gas (2DEG) with Rashba spin–orbit coupling when an external electric field is applied. The system is described by the Rashba Hamiltonian [Gaiardoni et al., arXiv:2503.20712; Bychkov & Rashba, JETP Lett. 39, 78 (1984)]:

$$H = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}),$$

where:
- $m$ is the effective carrier mass,
- $\alpha$ is the Rashba spin–orbit coupling (RSOC) strength,
- $\mathbf{p} = \hbar\mathbf{k}$ is the momentum,
- $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices,
- $\hat{z}$ is the unit vector normal to the 2D plane.

The energy dispersion splits into two chiral bands [Gaiardoni et al., arXiv:2503.20712]:

$$E_{\pm}(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha |k|.$$

The corresponding eigenstates have spin expectation values [Gaiardoni et al., arXiv:2503.20712]:

$$\langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^{\pm} = \frac{1}{k}\begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin\theta \\ \mp \cos\theta \\ 0 \end{pmatrix},$$

where $\theta$ is the angle between $\mathbf{k}$ and the $\hat{x}$-axis. This spin–momentum locking means that the spin lies tangential to the Fermi surfaces, with opposite helicities on the two bands.

The two chiral Fermi momenta are [Gaiardoni et al., arXiv:2503.20712]:
- **High-Density Regime (HDR)** — both bands occupied ($E_F > -m\alpha^2/2\hbar^2$, above band crossing):

$$k_F^{+} = -k_0 + \sqrt{k_0^2 + 2mE_F}, \qquad k_F^{-} = +k_0 + \sqrt{k_0^2 + 2mE_F},$$

- **Low-Density Regime (LDR)** — only the lower band occupied:

$$k_F^{+} = +k_0 - \sqrt{k_0^2 + 2mE_F}, \qquad k_F^{-} = +k_0 + \sqrt{k_0^2 + 2mE_F},$$

with $k_0 = m\alpha/\hbar^2$ [Gaiardoni et al., arXiv:2503.20712].

---

## 2. Boltzmann Transport Formulation

Within the semiclassical Boltzmann framework, the total spin density (magnetization) induced by an electric field $\mathbf{E}$ is obtained from [Gaiardoni et al., arXiv:2503.20712; Vignale & Tokatly, Phys. Rev. B 93, 035310 (2016)]:

$$\mathbf{M} = -\mu_B \sum_{\mathbf{k},\nu} |e|\,(\bar{\tau}_k^{\nu}\, \mathbf{v}^{\nu}(k) \cdot \mathbf{E})\, \delta[E_{\nu}(k) - E_F]\, \langle \boldsymbol{\sigma} \rangle_{\mathbf{k}}^{\nu},$$

where:
- $\mu_B$ is the Bohr magneton,
- $\nu = \pm$ indexes the two chiral Fermi surfaces,
- $\bar{\tau}_k^{\nu}$ is the transport lifetime,
- $\mathbf{v}^{\nu}(k) = \nabla_{\mathbf{k}} E^{\nu}_{\mathbf{k}}$ is the group velocity.

Defining the linear Edelstein susceptibility via $m_j = \chi_{ij} E_i$, the key component for an electric field along $\hat{x}$ is [Gaiardoni et al., arXiv:2503.20712]:

$$\chi_{xy} = -\chi_0 \sum_{\nu=\pm} \int d^2k \, \langle \sigma_y \rangle_{\mathbf{k}}^{\nu} \, \delta(\varepsilon_{\mathbf{k}}^{\nu} - \mu) \, v_x^{\nu}(\mathbf{k}),$$

with $\chi_0 = \tau |e| \mu_B S_{\text{cell}} / (4\pi^2 a)$ (for the numerical implementation).

---

## 3. Analytical Results for the Isotropic Rashba Model

### 3.1 High-Density Regime (HDR)

For $\bar{\tau}^+ = \bar{\tau}^- = \tau$ (constant relaxation time), the spin density in the HDR is [Gaiardoni et al., arXiv:2503.20712]:

$$\boxed{M_y = \frac{\mu_B |e| \tau}{2\pi}\, m\alpha\, [\hat{z} \times \mathbf{E}]_y.}$$

This is a **constant, independent of the Fermi energy** — the spin density saturates once both Rashba bands are populated. In terms of the susceptibility:

$$\chi_{xy} = \frac{\mu_B |e| \tau}{2\pi}\, m\alpha.$$

The magnetization is **linear in the Rashba coupling $\alpha$** and **linear in the electric field magnitude** (linear response regime) [Gaiardoni et al., arXiv:2503.20712].

### 3.2 Low-Density Regime (LDR)

When only the lower band is occupied [Gaiardoni et al., arXiv:2503.20712]:

$$M_y = \frac{\mu_B |e| \tau}{2\pi}\, \sqrt{m^2\alpha^2 + 2mE_F}\, [\hat{z} \times \mathbf{E}]_y.$$

For small Fermi energies near the band crossing, this expands to [Gaiardoni et al., arXiv:2503.20712]:

$$M_y = \frac{\mu_B |e| \tau}{2\pi} \left( \alpha m + \frac{1}{2}\frac{E_F}{\alpha} \right) [\hat{z} \times \mathbf{E}]_y.$$

The spin density **increases linearly with Fermi energy** in the LDR [Gaiardoni et al., arXiv:2503.20712].

### 3.3 Direction of Magnetization

For $\mathbf{E} = E_x \hat{x}$, the magnetization points along $\hat{y}$:

$$\mathbf{M} = \frac{\mu_B |e| \tau}{2\pi}\, m\alpha\, E_x\, \hat{y}.$$

**Key geometric property:** The induced magnetization is always **perpendicular to the applied electric field and lies in the plane** of the 2DEG [Gaiardoni et al., arXiv:2503.20712]. This arises directly from the spin–momentum locking: a shift of the Fermi surfaces along $\hat{x}$ by $\delta k$ creates a spin imbalance along the orthogonal $\hat{y}$ direction [Gaiardoni et al., arXiv:2503.20712; Zulkoskey et al., arXiv:1912.01804].

---

## 4. Nonlinear (Clean-Limit) Edelstein Effect

For a perfectly clean Rashba 2DEG (no impurities), the Edelstein effect can be solved exactly in the nonlinear regime [Vignale & Tokatly, Phys. Rev. B 93, 035310 (2016)].

### 4.1 Model and Key Parameter

The Hamiltonian with electric field $\mathbf{E} = E\hat{x}$ is [Vignale & Tokatly, PRB 93, 035310 (2016)]:

$$H(\mathbf{p}, t) = \frac{1}{2m}[\mathbf{p} + e\mathbf{A}(t)]^2 - \alpha ([\mathbf{p} + e\mathbf{A}(t)] \times \boldsymbol{\sigma}) \cdot \hat{z},$$

with $\mathbf{A}(t) = -eEt\,\hat{x}$.

The crucial dimensionless parameter governing the response is [Vignale & Tokatly, PRB 93, 035310 (2016)]:

$$\boxed{\gamma \equiv \frac{eE}{\alpha p_F^2} = \frac{eEL_s}{E_F}},$$

where $L_s = \hbar/(2m\alpha)$ is the spin-precession length, $E_F$ the Fermi energy, and $p_F$ the Fermi momentum. 

### 4.2 Adiabatic Regime ($\gamma \ll 1$)

In the weak-field (quasi-adiabatic) regime, the spin evolution is governed by the Landau–Zener problem [Vignale & Tokatly, PRB 93, 035310 (2016)]. The total Edelstein spin polarization is:

$$S_y(t) = \frac{\alpha n}{v_F} \frac{1}{2} \frac{1}{2\pi} \int_0^{2\pi} d\theta \frac{\cos\theta - \sqrt{\gamma}\tau}{\sqrt{1 + (\sqrt{\gamma}\tau)^2 - 2\sqrt{\gamma}\tau\cos\theta}} \left(1 - e^{-\frac{\pi}{\gamma}\sin^2\theta}\right),$$

where $\tau = \alpha p_F \sqrt{\gamma}\, t$ is the dimensionless time and $v_F$ is the Fermi velocity.

**Linear response limit** ($|v(t)|/v_F \ll 1$): [Vignale & Tokatly, PRB 93, 035310 (2016)]

$$S_y(t) \simeq \frac{\alpha n}{2 v_F} \frac{eEt}{mv_F} = \frac{N_0}{2}\alpha\, eEt,$$

where $N_0 = n/\epsilon_F = m/(2\pi)$ is the density of states per spin. This is the **standard formula for the linear Edelstein effect** [Vignale & Tokatly, PRB 93, 035310 (2016); Edelstein, Solid State Commun. 73, 233 (1990); Aronov & Lyanda-Geller, JETP Lett. 50, 431 (1989)].

### 4.3 Long-Time Saturation

The spin polarization saturates at a constant value for large times, given by [Vignale & Tokatly, PRB 93, 035310 (2016)]:

$$|u_p(\infty)|^2 = P_p^{LZ}|A_p|^2 + (1 - P_p^{LZ})|B_p|^2 - 2\sqrt{P_p^{LZ}(1 - P_p^{LZ})}\,\text{Re}\left\{A_p B_p^* e^{i\left[\frac{\pi}{4} + \arg\Gamma\left(1 - i\frac{\Delta_p^2}{2}\right)\right]}\right\},$$

with the Landau–Zener survival probability [Vignale & Tokatly, PRB 93, 035310 (2016)]:

$$P_p^{LZ} = e^{-\pi\Delta_p^2} = e^{-\frac{\pi}{\gamma}\sin^2\theta_p}.$$

**Key results:**
- For $\gamma \to 0$ (adiabatic): the spin fully aligns with the Edelstein field, $S_{y,p}(\infty) \to -1/2$ (saturation at the maximum value $\sim n(\alpha/v_F)$).
- For $\gamma \to \infty$ (sudden switch-on): the spin cannot follow the rapidly changing field, and $S_{y,p}(\infty) \to \cos\theta_p$ (its initial value).
- At $\gamma = 0.1, 1, 10$ the normalized long-time limits are $-0.449$, $-0.287$, and $-0.098$ respectively (in units of $n\alpha/v_F$) [Vignale & Tokatly, PRB 93, 035310 (2016)].

### 4.4 Parameter Dependencies (Nonlinear Regime)

The nonlinear response depends on [Vignale & Tokatly, PRB 93, 035310 (2016)]:
- **Electric field magnitude** $E$: enters through $\gamma = eE/(\alpha p_F^2)$; larger $E$ (larger $\gamma$) *reduces* the spin polarization because the spins cannot respond adiabatically.
- **Rashba coupling** $\alpha$: controls both the saturation value (proportional to $\alpha/v_F$) and the non-adiabaticity parameter ($\gamma \propto 1/\alpha$).
- **Fermi velocity** $v_F$: the saturation spin density scales as $\alpha n/v_F$.
- **Fermi energy** $E_F$: enters through $\gamma = eEL_s/E_F$; larger $E_F$ makes the response more adiabatic.

---

## 5. Anisotropic Rashba Model ($C_{2v}$ Symmetry)

For systems with $C_{2v}$ symmetry, the Hamiltonian generalizes to [Gaiardoni et al., arXiv:2503.20712]:

$$\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y,$$

where $m_x \neq m_y$ (mass anisotropy) and $\alpha_x \neq \alpha_y$ (RSOC anisotropy).

### 5.1 Anisotropy in Effective Mass

Defining $r_m = m_y/m_x$, the Edelstein susceptibility in the HDR is [Gaiardoni et al., arXiv:2503.20712]:

$$\boxed{\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha\, r_m}{1 + \sqrt{r_m}}}.$$

### 5.2 Anisotropy in Spin–Orbit Coupling

Defining $r_\alpha = \alpha_y/\alpha_x$, the susceptibility is [Gaiardoni et al., arXiv:2503.20712]:

$$\boxed{\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m\, \alpha_x\, r_\alpha}{1 + r_\alpha}}.$$

### 5.3 Key Findings on Anisotropy

- When $r_m < 1$ or $r_\alpha < 1$, the susceptibility is **lower** than in the isotropic case.
- When $r_m > 1$ or $r_\alpha > 1$, the susceptibility **increases**.
- The Edelstein response can be **boosted** by making the mass and/or RSOC ratios greater than unity [Gaiardoni et al., arXiv:2503.20712].
- For small $r_m$ and $r_\alpha$, the susceptibility increases linearly; it tends to saturate for $r_\alpha \gg 1$ [Gaiardoni et al., arXiv:2503.20712].

---

## 6. Numerical Implementation Framework

### 6.1 Algorithm for Computing the Edelstein Effect

```python
import numpy as np

def rashba_edelstein(alpha, m, mu, E, tau, kmax, Nk):
    """
    Compute Edelstein magnetization for isotropic Rashba model.
    
    Parameters:
    -----------
    alpha : float - Rashba SOC strength (eV·Å)
    m     : float - effective mass (eV⁻¹·Å⁻²)
    mu    : float - chemical potential (eV)
    E     : float - electric field along x (V/Å)
    tau   : float - transport time (s)
    kmax  : float - momentum cutoff
    Nk    : int   - grid points
    """
    hbar = 6.582e-16  # eV·s
    e = 1.602e-19     # C
    mu_B = 5.788e-5   # eV/T
    
    k = np.linspace(0.001, kmax, Nk)
    theta = np.linspace(0, 2*np.pi, Nk)
    K, TH = np.meshgrid(k, theta)
    
    kx = K*np.cos(TH)
    ky = K*np.sin(TH)
    
    # Band energies
    E_plus = hbar**2*K**2/(2*m) + alpha*K
    E_minus = hbar**2*K**2/(2*m) - alpha*K
    
    # Group velocities
    vx_plus = hbar**2*K*np.cos(TH)/m + alpha*np.cos(TH)
    vx_minus = hbar**2*K*np.cos(TH)/m - alpha*np.cos(TH)
    
    # Spin expectation values
    sy_plus = -np.cos(TH)   # ⟨σy⟩ for + band
    sy_minus = np.cos(TH)   # ⟨σy⟩ for − band
    
    # Delta functions at Fermi surface (broadened)
    def delta(Ek, mu, gamma=0.001):
        return gamma/(np.pi*((Ek-mu)**2 + gamma**2))
    
    d_plus = delta(E_plus, mu)
    d_minus = delta(E_minus, mu)
    
    # Edelstein susceptibility χxy = ∂My/∂Ex
    chi_xy = -(tau*e*mu_B/(4*np.pi**2)) * (
        np.sum(K * sy_plus * vx_plus * d_plus) +
        np.sum(K * sy_minus * vx_minus * d_minus)
    ) * (2*np.pi/Nk)**2
    
    # Magnetization
    My = chi_xy * E
    
    return My, chi_xy
```

### 6.2 Computing Magnetization for Arbitrary Field Directions

For a general electric field $\mathbf{E} = (E_x, E_y)$, the linear Edelstein tensor for the isotropic Rashba model has the form [Gaiardoni et al., arXiv:2503.20712]:

$$\begin{pmatrix} M_x \\ M_y \end{pmatrix} = \frac{\mu_B |e| \tau}{2\pi} m\alpha \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} E_x \\ E_y \end{pmatrix}.$$

Thus:
- $\mathbf{E} \parallel \hat{x} \Rightarrow \mathbf{M} \parallel \hat{y}$,
- $\mathbf{E} \parallel \hat{y} \Rightarrow \mathbf{M} \parallel -\hat{x}$,
- For arbitrary direction $\mathbf{E}$, the magnetization is $\mathbf{M} \propto \hat{z} \times \mathbf{E}$.

### 6.3 Suggested Graphics

1. **$M_y$ vs. $E_x$**: Linear increase in the linear regime; saturation and reduction in the nonlinear regime (see Vignale & Tokatly, PRB 93, 035310 (2016), Figs. 3–6).
2. **$M_y$ vs. $\alpha$**: Linear increase with Rashba coupling (HDR).
3. **$\chi_{xy}/\chi_0$ vs. chemical potential $\mu$**: Plateau in HDR, linear rise in LDR [Gaiardoni et al., arXiv:2503.20712, Figs. 2–3].
4. **$\chi_{xy}/\chi_0$ vs. $r_m$ and $r_\alpha$**: Monotonically increasing functions for anisotropy ratios above unity [Gaiardoni et al., arXiv:2503.20712, Fig. 6].
5. **Vector field plot of $\mathbf{M}$ vs. $\mathbf{E}$ direction**: Shows perpendicular alignment.
6. **$M_y/n$ vs. $\gamma$** (nonlinear parameter): Shows the crossover from adiabatic saturation to non-adiabatic suppression [Vignale & Tokatly, PRB 93, 035310 (2016), Fig. 5].

---

## 7. Summary of Parameter Dependencies

| Parameter | Effect on Edelstein Magnetization |
|---|---|
| **Rashba coupling $\alpha$** | $M_y \propto \alpha$ (linear in HDR); controls saturation via $\gamma \propto 1/\alpha$ |
| **Effective mass $m$** | $M_y \propto m$ (in isotropic HDR); anisotropy $r_m > 1$ boosts response |
| **Fermi energy $E_F$** | $M_y$ independent of $E_F$ in HDR; $\propto \sqrt{2mE_F}$ in LDR |
| **Electric field magnitude $E$** | $M_y \propto E$ (linear regime); saturates then decreases for $\gamma \gtrsim 1$ |
| **Electric field direction** | $\mathbf{M} \perp \mathbf{E}$, in-plane |
| **Transport time $\tau$** | $M_y \propto \tau$ (linear regime) |
| **Chirality** | Determines the sign: opposite helicity bands contribute oppositely; the net sign depends on which band dominates (outer band in HDR) |
| **Anisotropy $r_m, r_\alpha$** | $\chi_{xy}/\chi_0 = 4\pi m_x\alpha\, r_m/(1+\sqrt{r_m})$ and $4\pi m\alpha_x r_\alpha/(1+r_\alpha)$ |

---

## 8. References

1. **I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro**, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," arXiv:2503.20712 (2025).

2. **G. Vignale and I. V. Tokatly**, "Theory of the nonlinear Rashba-Edelstein effect: The clean electron gas limit," Phys. Rev. B **93**, 035310 (2016); arXiv:1506.08330.

3. **V. M. Edelstein**, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," Solid State Commun. **73**, 233 (1990).

4. **A. G. Aronov and Y. B. Lyanda-Geller**, "Nuclear electric resonance and orientation of carrier spins by an electric field," JETP Lett. **50**, 431 (1989).

5. **Yu. A. Bychkov and E. I. Rashba**, "Properties of a 2D electron gas with lifted spectral degeneracy," JETP Lett. **39**, 78 (1984).

6. **A. C. Zulkoskey, R. Dick, and K. Tanaka**, "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface," arXiv:1912.01804 (2019).

7. **M. Yama, M. Matsuo, and T. Kato**, "Theory of spin pumping and inverse Rashba-Edelstein effect in a two-dimensional electron gas," arXiv:2409.14267 (2024).

8. **E. M. Hankiewicz and G. Vignale**, "Coulomb corrections to the extrinsic spin-Hall effect of a two-dimensional electron gas," arXiv:cond-mat/0507228 (2006).

9. **E. I. Rashba and V. I. Sheka**, "Electric-Dipole Spin Resonances," arXiv:1812.01721 (2018).

10. **R. Ramazashvili**, "Zeeman spin-orbit coupling in antiferromagnetic conductors," arXiv:1810.03720 (2018).
# Model Construction for the Edelstein Effect in a Rashba Fermion at the Gamma Point

## 1. Fundamental Model: Rashba Hamiltonian

The Rashba spin-orbit interaction arises from structure inversion asymmetry (SIA) at interfaces or surfaces and is described by the Hamiltonian [1, 2]:

$$H = \frac{p_\parallel^2}{2m} + \alpha (\sigma \times p_\parallel/\hbar) \cdot \hat{z}$$

where:
- $m$ is the effective mass of the electron
- $\alpha = e\hbar E_z(z)/4m^2c^2$ is the Rashba coefficient (with $E_z(z)$ the electric field perpendicular to the interface)
- $\sigma = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices
- $k_\parallel = (k_x, k_y)$ is the two-dimensional wave vector

The dispersion relation is given by [2]:

$$E_{\pm}(k_\parallel) = \frac{\hbar^2 k_\parallel^2}{2m} \pm \alpha |k_\parallel|$$

with the energy minimum at:

$$E_{\min} = -\frac{m\alpha^2}{2\hbar^2}$$

The spin texture is characterized by **spin-momentum locking**: the spin orientation is locked perpendicular to the momentum. For the $E_+$ and $E_-$ branches, the spins wind clockwise and counterclockwise respectively around the Fermi surface [2]. The spin polarization of the eigenstates is given by [3]:

$$\mathbf{P}_{\pm}(\mathbf{k}) = \pm \frac{\alpha_R}{|\alpha_R|} \frac{(-k_y, k_x, 0)}{|\mathbf{k}|}$$

At the **Gamma point** ($\mathbf{k} = 0$), the Hamiltonian reduces to the kinetic term, and the spin splitting vanishes. The model is expanded around this point using the **method of invariants** based on symmetry requirements [4]:

$$H = H_0 + e\phi(\hat{r}) + H_{so}, \qquad H_{so} = \sum_j \sigma_j f_j(\hat{k})$$

## 2. Density of States for the Rashba 2DEG

The density of states per unit area per spin for the Rashba model is [2, 5]:

$$\rho(E_{\pm}) = \frac{m}{2\pi\hbar^2} \left(1 \mp \frac{b}{\sqrt{b^2 + 2Em/\hbar^2}}\right), \quad E \geq 0$$

$$\rho(E_{-}) = \frac{mb}{\pi\hbar^2\sqrt{b^2 + 2mE/\hbar^2}}, \quad E < 0$$

where $b = m\alpha/\hbar^2$.

## 3. The Edelstein Effect: Formalism

### 3.1 Definition

The Edelstein effect (EE), also known as the inverse spin-galvanic effect or current-induced spin polarization, is the generation of a homogeneous spin polarization in systems with broken inversion symmetry upon application of an electric field or charge current [6, 7, 8]:

$$\mathbf{m} = (\chi_s + \chi_l)\mathbf{E} = \chi \mathbf{E}$$

where $\chi_s$, $\chi_l$, and $\chi$ are the spin, orbital, and total Edelstein susceptibilities respectively [9].

### 3.2 Microscopic Derivation

At zero temperature, the magnetic moment per unit cell $\mathbf{m}$ with spin and orbital contributions is [9]:

$$\mathbf{m} = -\frac{\mu_B}{\hbar} \frac{A_0}{A_s} \sum_{nk} f_{nk}(g_s s_{nk} + g_l l_{nk})$$

where:
- $A_0$ is the area of the unit cell
- $A_s$ is the area of the entire system
- $\mu_B$ is the Bohr magneton
- $f_{nk}$ is the non-equilibrium distribution function
- $g_{s/l}$ are the spin and orbital g-factors
- $s_{nk}$ and $l_{nk}$ are the expectation values of spin and orbital angular momentum

Solving the **linearized Boltzmann equation** in the constant relaxation time approximation, the distribution function in the presence of an external electric field $\mathbf{E}$ is [9]:

$$f_{nk} = f^0_{nk} + e\tau \left.\frac{\partial f}{\partial \varepsilon}\right|_{\varepsilon = \varepsilon_{nk}} \mathbf{v}_{nk} \cdot \mathbf{E}$$

where $f^0_{nk}$ is the Fermi-Dirac distribution, $\tau$ is the relaxation time, and $\mathbf{v}_{nk}$ is the group velocity.

The spin expectation value is:

$$\mathbf{s}_{nk} = \langle \Psi_{nk} | \hat{\mathbf{s}} | \Psi_{nk} \rangle$$

and within the **modern theory of orbital magnetization**, the orbital moment is [10, 11]:

$$\mathbf{l}_{nk} = \frac{ie}{2\mu_B g_l} \sum_{m(\neq n)} \frac{\langle u_{nk}| \frac{\partial H_0}{\partial \mathbf{k}} |u_{mk}\rangle \times \langle u_{mk}| \frac{\partial H_0}{\partial \mathbf{k}} |u_{nk}\rangle}{\varepsilon_{nk} - \varepsilon_{mk}}$$

### 3.3 The Edelstein Effect for a Single Rashba Band

For a **single-layer Rashba 2DEG**, the spin Edelstein effect can be derived analytically. When an electric field is applied along the $+x$ direction, electrons move in the $-x$ direction, populating states with $k_x < 0$ at the expense of states with $k_x > 0$ [2, 6]. This causes a shift of the Fermi circles (Figure 2 in Ref. [2]), resulting in:

- A net spin polarization in the $-y$ direction (for positive $\alpha$)
- The polarization is **in-plane and perpendicular to the current direction**
- The magnitude is proportional to the applied field and the relaxation time

The Edelstein susceptibility for the 2D Rashba model is given by [6, 12]:

$$\chi_s = \frac{e \tau}{4\pi\hbar} \frac{\alpha}{|\alpha|}$$

More precisely, for a single Rashba band at Fermi energy $E_F$, the spin accumulation is [6]:

$$\delta s_y = \frac{e\tau}{2\pi\hbar^2} \frac{m\alpha}{k_F} E_x$$

where $k_F$ is the Fermi wavevector.

### 3.4 Spin and Orbital Edelstein Effects in the Bilayer Rashba Model

For a **bilayer system** with Rashba interaction (Hamiltonian in Eq. 7 of Ref. [9]):

$$H = \begin{pmatrix} H_A & T \\ T & H_B \end{pmatrix}$$

with $H_l = \frac{\hbar^2 k^2}{2m_l} + \alpha_l(\hat{e}_z \times \mathbf{k}) \cdot \sigma$ for layers $l = A, B$, and interlayer hopping $T = t I_{2\times2}$:

- **Equal effective masses** ($m_A = m_B = m$): The dispersion is:

$$\varepsilon_{n_1,n_2}(k) = \frac{\hbar^2 k^2}{2m} + \frac{n_1}{2}|\alpha_+|k + \frac{n_2}{2}\sqrt{\alpha_-^2 k^2 + 4t^2}$$

with $n_1, n_2 = \pm 1$ and $\alpha_{\pm} = \alpha_A \pm \alpha_B$. The spin moment is:

$$\mathbf{s}_{nk} = n_1 \frac{\hbar}{2}\hat{e}_\phi$$

and the orbital moment:

$$\mathbf{l}_{nk} = -n_1 \frac{ec\,t^2 \alpha_-}{\mu_B g_l(\alpha_-^2 k^2 + 4t^2)}\hat{e}_\phi$$

- **Equal Rashba parameters** ($\alpha_A = \alpha_B = \alpha$): The orbital moment is:

$$\mathbf{l}_{nk} = -\frac{ec\hbar^2 t^2 M_- k}{4\mu_B g_l\left(\frac{\hbar^4 k^4}{16}M_-^2 + t^2\right)}\hat{e}_\phi$$

with $M_{\pm} = \frac{1}{m_A} \pm \frac{1}{m_B}$.

Due to rotational and mirror symmetries, the only nonzero Edelstein susceptibility tensor elements are $\chi^{s/l}_{xy} = -\chi^{s/l}_{yx}$ [9].

## 4. Parameter Dependence of the Edelstein Effect

### 4.1 Dependence on Rashba coupling strength $\alpha$

The spin Edelstein effect **increases with increasing Rashba parameter** $\alpha$. For a constant Fermi energy, increasing $\alpha$ in either layer enhances the SEE due to the increasing size of the Fermi lines [9].

The **orbital Edelstein effect** shows more complex behavior:
- It is proportional to the *difference* in Rashba parameters $\alpha_- = \alpha_A - \alpha_B$
- It vanishes when $\alpha_A = \alpha_B$ (equivalent layers)
- Its **sign** can be controlled by the relative magnitude of $\alpha_A$ vs $\alpha_B$ (Figure 4 of Ref. [9])
- At $\alpha_B = 0$ (no Rashba in one layer), the OEE is small but **nonzero**, showing that the OEE can occur without SOC in one of the layers [9]

### 4.2 Dependence on effective mass $m$

The SEE is enhanced by increasing the effective mass in either layer [9]. The OEE depends on the difference $M_- = 1/m_A - 1/m_B$:
- It vanishes for equal masses
- Its sign is determined by the sign of $m_B - m_A$
- The OEE can exist **without any SOC** when the effective masses are asymmetric (Appendix A of Ref. [9])

### 4.3 Dependence on chirality (sign of $\alpha$)

The sign of the Rashba parameter $\alpha$ determines the **direction** of the induced spin polarization [3]:
- The spin orientation of the eigenstates is given by $\mathbf{P}_{\pm}(\mathbf{k}) = \pm \frac{\alpha_R}{|\alpha_R|}\frac{(-k_y, k_x, 0)}{|\mathbf{k}|}$
- The orientation of the spin accumulation is directly dependent on the sign of $\alpha_R$ [3]
- For $\alpha_A + \alpha_B < 0$, the SEE can present the opposite sign [9]

For example, in experiments on Rashba interfaces [3]:
- Cu/Bi$_2$O$_3$: $\alpha_R = -0.25 \pm 0.03$ eV·Å
- Ag/Bi$_2$O$_3$: $\alpha_R = +0.18 \pm 0.04$ eV·Å
- These opposite signs produce **opposite orientations** of spin accumulation (confirmed by opposite phases in TR-TMOKE signals)

### 4.4 Dependence on Fermi velocity $v_F$

The Fermi velocity enters through the kinetic energy term $E = \hbar^2 k^2/2m$. In the Rashba model, $v_F = \hbar k_F/m$ at the Fermi surface. The spin accumulation can be expressed in terms of $v_F$ as [6]:

$$\delta s \propto \frac{\alpha}{v_F} E_x \tau$$

For the density of states, the Rashba-modified DOS depends on the parameter $b = m\alpha/\hbar^2$, which relates to the ratio $\alpha/v_F$ at the Fermi surface.

### 4.5 Dependence on applied electric field direction and magnitude

From the tensor structure of the Edelstein susceptibility [9]:

$$\mathbf{m} = \chi \mathbf{E}$$

with only $\chi_{xy} = -\chi_{yx}$ nonzero:
- An electric field along $+x$ produces magnetization along $-y$ (or $+y$, depending on the sign of $\alpha$)
- An electric field along $+y$ produces magnetization along $+x$
- The **direction** of the induced magnetization is always **perpendicular** to the applied field and **in-plane**
- The **magnitude** of the magnetization is **linear** in the applied field (in the linear response regime)

For the DREE (Direct Rashba-Edelstein Effect) at interfaces, the spin accumulation is [3, 13]:
- **Uniform** across the interface
- Oriented **in-plane**
- **Perpendicular** to the current direction

### 4.6 Enhanced Edelstein effect in confined systems

In a three-dimensional electron gas with a two-dimensional Rashba interface, the bound-state dispersion is [2]:

$$E_{\pm} = \frac{\hbar^2}{2m}(k_\parallel^2 - \kappa_\pm^2) = \frac{\hbar^2 k_\parallel^2}{2m} - \frac{mL_\perp^2}{2\hbar^2}(V_0 \pm \alpha k_\parallel)^2$$

where $L_\perp$ is the interface thickness and $V_0$ is the attractive potential strength. The requirement $\kappa_- > 0$ implies $k_\parallel < V_0/\alpha$, restricting the $E_-$ branch to a maximum energy of $E_- = \hbar^2 V_0^2/2m\alpha^2$. This restriction leads to an **enhanced Edelstein effect** because the contribution from the $E_-$ branch's $+y$ spin alignment (for $k_x < 0$) has an upper bound, while the $E_+$ branch has no such restriction [2].

## 5. Numerical Implementation Framework

### 5.1 Computational Algorithm

For computing the Edelstein effect numerically:

1. **Define the Rashba Hamiltonian** on a 2D grid in $\mathbf{k}$-space:

```python
import numpy as np

def rashba_hamiltonian(kx, ky, m, alpha):
    """Rashba Hamiltonian for a 2DEG"""
    k2 = kx**2 + ky**2
    H0 = (np.pi**2 * k2 / (2*m)) * np.eye(2)  # kinetic term
    # Rashba term: alpha * (sigma_x * ky - sigma_y * kx)
    H_R = alpha * (kx * np.array([[0, -1j], [1j, 0]]) 
                   - ky * np.array([[0, 1], [1, 0]]))
    return H0 + H_R
```

2. **Diagonalize** to obtain eigenvalues $\varepsilon_{n\mathbf{k}}$ and eigenvectors $|u_{n\mathbf{k}}\rangle$

3. **Compute the spin expectation values**: $\mathbf{s}_{n\mathbf{k}} = \langle u_{n\mathbf{k}}| \frac{\hbar}{2}\boldsymbol{\sigma} |u_{n\mathbf{k}}\rangle$

4. **Compute the velocity operator**: $\mathbf{v}_{n\mathbf{k}} = \frac{1}{\hbar}\nabla_{\mathbf{k}}\varepsilon_{n\mathbf{k}}$

5. **Evaluate the Edelstein susceptibility** using the Boltzmann transport formalism:

$$\chi^{s}_{ij} = -e\tau \sum_{n\mathbf{k}} \frac{\partial f}{\partial \varepsilon}\bigg|_{\varepsilon_{n\mathbf{k}}} v_{n\mathbf{k},i} \, s_{n\mathbf{k},j}$$

6. **Compute the induced magnetization**: $\mathbf{m} = \chi \mathbf{E}$

### 5.2 Graphics for Visualization

The required graphics should include:

**(a) Dispersion relation**: $E_{\pm}(k_x, k_y = 0)$ showing the characteristic Rashba splitting with two parabolas shifted by $\pm\alpha|k|$ [2, 5]

**(b) Fermi surface shift under electric field**: Show the displaced Fermi circles in the $k_x$-$k_y$ plane for the $E_+$ and $E_-$ branches, illustrating the asymmetric population leading to net spin polarization [2]

**(c) Magnetization vs. electric field magnitude**: Plot $|\mathbf{m}|$ vs. $|\mathbf{E}|$ showing linear dependence (in the linear response regime) with slope given by $\chi$

**(d) Magnetization direction as function of field direction**: Plot the components $m_x$ and $m_y$ as functions of the field angle $\theta_E$, showing $m \perp E$ (for the spin contribution)

**(e) Parameter dependence plots**:
- $|\mathbf{m}|$ vs. $\alpha$ (Rashba parameter) — showing linear or monotonic increase
- $|\mathbf{m}|$ vs. $m$ (effective mass) — showing increase with $m$
- $|\mathbf{m}|$ vs. $v_F$ (Fermi velocity) — showing decrease with $v_F$
- $|\mathbf{m}|$ vs. $\text{sign}(\alpha)$ (chirality) — showing sign reversal

**(f) Energy-dependent susceptibility**: $\chi_{xy}$ vs. $\varepsilon_F$ showing the characteristic band-edge structure [9]

## 6. Experimental Parameter Values

Typical values for Rashba systems [3, 9]:

| System | $\alpha_R$ (eV·Å) | Effective mass $m^*$ |
|--------|------------------|---------------------|
| Cu/Bi$_2$O$_3$ | $-0.25 \pm 0.03$ | Negative |
| Ag/Bi$_2$O$_3$ | $+0.18 \pm 0.04$ | Negative |
| Au(111) surface | $0.33$ | $0.27\,m_e$ |
| LAO/STO interface | $10$–$25$ meV (tight-binding) | $0.8\,m_e$ |

Experimental spin accumulation values [3]:
- Cu/Bi$_2$O$_3$: 14.0 $\mu$eV (total), 130.2 $\mu$eV (with penetration depth enhancement)
- Ag/Bi$_2$O$_3$: 23.7 $\mu$eV (total), 220.4 $\mu$eV (with enhancement)

The SEE susceptibility for typical Rashba parameters is of order $\chi_s \sim 10^{-9}$ $\mu_B$ m/V, while the OEE is typically $\chi_l \sim 10^{-11}$–$10^{-10}$ $\mu_B$ m/V for the bilayer model [9].

## 7. Summary of Key Equations for the Model

**Rashba Hamiltonian** (at Gamma point, expanded around $\mathbf{k} = 0$):

$$H = \frac{\hbar^2 k^2}{2m} + \alpha(\sigma_x k_y - \sigma_y k_x)$$

**Dispersion**:

$$E_{\pm}(\mathbf{k}) = \frac{\hbar^2 k^2}{2m} \pm \alpha|\mathbf{k}|$$

**Spin-momentum locking**:

$$\langle \boldsymbol{\sigma} \rangle_{\pm} = \pm \frac{\alpha}{|\alpha|} \frac{(-k_y, k_x, 0)}{|\mathbf{k}|}$$

**Edelstein susceptibility** (spin, single band):

$$\chi^s_{xy} = \frac{e\tau}{4\pi\hbar}\frac{\alpha}{|\alpha|} \left(\text{with band occupation factors}\right)$$

**Induced magnetization**:

$$\mathbf{m} = \chi \mathbf{E}, \quad m_i = \chi_{ij} E_j$$

**Density of states**:

$$\rho(E) = \frac{m}{2\pi\hbar^2}\left(1 \pm \frac{m\alpha/\hbar^2}{\sqrt{(m\alpha/\hbar^2)^2 + 2mE/\hbar^2}}\right)$$

**Linear response** (superconducting case, orbital) [14]:

$$\chi^o_{yx} = -2\sum_{\mathbf{k},\lambda>\lambda'} \frac{1}{E_{\lambda\mathbf{k}} + E_{\lambda'\mathbf{k}}} \langle \phi_{\lambda\mathbf{k}}|v_x|\phi_{\lambda'\mathbf{k}}\rangle \langle \phi_{\lambda'\mathbf{k}}|L_y|\phi_{\lambda\mathbf{k}}\rangle \left(1 - \frac{\varepsilon_{\lambda\mathbf{k}}\varepsilon_{\lambda'\mathbf{k}} + \Delta^2}{E_{\lambda\mathbf{k}}E_{\lambda'\mathbf{k}}}\right)$$

## References

[1] Yu. A. Bychkov and E. I. Rashba, "Properties of a 2D electron gas with lifted spectral degeneracy," JETP Lett. **39**, 78 (1984).

[2] A. C. Zulkoskey, R. Dick, and K. Tanaka, "Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface," arXiv:1912.01804 (2019).

[3] F. Auvray, J. Puebla, M. Xu, B. Rana, D. Hashizume, and Y. Otani, "Spin accumulation at nonmagnetic interface induced by direct Rashba-Edelstein effect," (2018).

[4] E. I. Rashba and V. I. Sheka, "Electric-Dipole Spin Resonances," arXiv:1812.01721 (2018). Originally published in: Landau Level Spectroscopy, Modern Problems in Condensed Matter Sciences, Vol. 27.2, eds. G. Landwehr and E. I. Rashba (North-Holland, Amsterdam, 1991).

[5] R. Winkler, *Spin-Orbit Coupling Effects in Two-Dimensional Electron and Hole Systems*, Springer, Berlin (2003).

[6] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," Solid State Communications **73**, 233 (1990).

[7] A. G. Aronov and Y. B. Lyanda-Geller, "Nuclear electric resonance and orientation of carrier spins by an electric field," JETP Lett. **50**, 431 (1989).

[8] P. Gambardella and I. M. Miron, "Current-induced spin-orbit torques," Philos. Trans. R. Soc. A **369**, 3175 (2011).

[9] S. Leiva M., J. Henk, I. Mertig, and A. Johansson, "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction," arXiv:2307.02872 (2024).

[10] D. Xiao, J. Shi, and Q. Niu, "Berry phase correction to electron density of states in solids," Phys. Rev. Lett. **95**, 137204 (2005).

[11] T. Thonhauser, D. Ceresoli, D. Vanderbilt, and R. Resta, "Orbital magnetization in periodic insulators," Phys. Rev. Lett. **95**, 137205 (2005).

[12] A. Johansson, J. Henk, and I. Mertig, "Theoretical aspects of the Edelstein effect for anisotropic two-dimensional electron gas and topological insulators," Phys. Rev. B **93**, 195440 (2016).

[13] J. Puebla, F. Auvray, M. Xu, B. Rana, A. Albouy, H. Tsai, K. Kondou, G. Tatara, and Y. Otani, Appl. Phys. Lett. **111**, 092402 (2017).

[14] S. Ando, Y. Tanaka, M. Cuoco, L. Chirolli, and M. T. Mercaldo, "Spin and orbital Edelstein effect in spin-orbit coupled noncentrosymmetric superconductors," arXiv:2408.08151 (2024).

[15] A. Maiellaro et al., "Spin Hall and Edelstein effects in a ballistic quantum dot with Rashba spin-orbit coupling," arXiv:2602.02036 (2026).

[16] R. Ramazashvili, "Zeeman spin-orbit coupling in antiferromagnetic conductors," arXiv:1810.03720 (2018).
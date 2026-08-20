# Edelstein Effect in Rashba Fermion Systems: Complete Solution

## 1. Model and Central Result

For a 2D Rashba fermion at the Γ point, the Hamiltonian is:

$$\mathcal{H} = \frac{\hbar^2 k^2}{2m^*}\sigma_0 + \chi\alpha_R(k_y\sigma_x - k_x\sigma_y)$$

with energy eigenvalues $\varepsilon_\pm(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} \pm \chi\alpha_R k$ and spin expectation values $\langle\boldsymbol{\sigma}\rangle_\pm = \pm\chi(\hat{z}\times\hat{k})$.

**The Edelstein effect** (electric-field-induced magnetization) is:

$$\boxed{\mathbf{M} = \chi \frac{g\mu_B e\tau\alpha_R}{4\pi\hbar}(\hat{z}\times\mathbf{E})}$$

The **Edelstein susceptibility** (magnetization per unit electric field):

$$\chi_{\text{Edelstein}} = \frac{g\mu_B e\tau\alpha_R}{4\pi\hbar}$$

## 2. Magnetization Components and Direction

For an electric field at angle $\theta_E$ in the plane ($\mathbf{E} = E(\cos\theta_E, \sin\theta_E, 0)$):

$$\mathbf{M} = \chi \chi_{\text{Edelstein}} E(-\sin\theta_E, \cos\theta_E, 0)$$

| Field Direction | Magnetization Components |
|---|---|
| $\mathbf{E} = E\hat{x}$ | $M_x = 0$, $M_y = \chi\chi_{\text{Edelstein}}E$, $M_z = 0$ |
| $\mathbf{E} = E\hat{y}$ | $M_x = -\chi\chi_{\text{Edelstein}}E$, $M_y = 0$, $M_z = 0$ |
| $\mathbf{E} = E(\cos\theta_E,\sin\theta_E)$ | $M_x = -\chi\chi_{\text{Edelstein}}E\sin\theta_E$, $M_y = \chi\chi_{\text{Edelstein}}E\cos\theta_E$ |

**Key properties:**
- **Perpendicular**: $\mathbf{M} \perp \mathbf{E}$ always
- **Linear**: $|\mathbf{M}| \propto |\mathbf{E}|$ with $|\mathbf{M}| = \chi_{\text{Edelstein}}|\mathbf{E}|$
- **Isotropic**: $|\mathbf{M}|$ independent of field direction

## 3. Parameter Dependencies

### 3.1 Chirality ($\chi = \pm 1$)
- Reverses magnetization direction: $\mathbf{M}(\chi=-1) = -\mathbf{M}(\chi=+1)$
- Magnitude unchanged

### 3.2 Rashba Coupling ($\alpha_R$)
- Linear: $|\mathbf{M}| \propto \alpha_R$
- Vanishes when $\alpha_R \to 0$ (no SOC)

### 3.3 Fermi Velocity ($v_F$) and Fermi Energy ($E_F$)
For impurity scattering with density $n_i$ and potential $V_0$:

$$\tau = \frac{\hbar^2}{2\pi n_i V_0^2 N(E_F)}$$

where $N(E_F) = \frac{m^*}{2\pi\hbar^2}\left[(1+\frac{\alpha_R m^*}{\hbar^2 k_F^+})^{-1} + (1-\frac{\alpha_R m^*}{\hbar^2 k_F^-})^{-1}\right]$

For $E_F > E_{SO}$ (both bands occupied): $\chi_{\text{Edelstein}} = \frac{g\mu_B e\tau(E_F)\alpha_R}{4\pi\hbar}$

For $E_F < E_{SO}$ (only lower band): $\chi_{\text{Edelstein}} = \frac{g\mu_B e\tau(E_F)\alpha_R}{4\pi\hbar}(1-\frac{E_F}{E_{SO}})$

### 3.4 Relaxation Time ($\tau$)
- Linear dependence: $\chi_{\text{Edelstein}} \propto \tau$

## 4. Numerical Example (InGaAs/InAlAs 2DEG)

| Parameter | Symbol | Value |
|---|---|---|
| Effective mass | $m^*$ | $0.05\,m_e$ |
| Rashba coupling | $\alpha_R$ | $0.5\times10^{-11}$ eV·m |
| Fermi energy | $E_F$ | 20 meV |
| Relaxation time | $\tau$ | 1 ps |
| g-factor | $g$ | 4 |
| Chirality | $\chi$ | +1 |

**Derived quantities:**
- $E_{SO} = 0.082$ meV (so $E_F \gg E_{SO}$, both bands occupied)
- $k_0 = 1.62\times10^8$ m⁻¹, $v_F = 3.75\times10^5$ m/s
- $k_F l = 60.8$ (diffusive limit valid)

**Edelstein susceptibility:**
$$\chi_{\text{Edelstein}} = 3.59\times10^{-51}\ \text{A·m}^2/\text{V} = 3.87\times10^{-8}\ \mu_B/(\text{nm}^2\cdot\text{V/cm})$$

For $E = 1$ V/cm: $|\mathbf{M}| = 3.87\times10^{-8}\ \mu_B/\text{nm}^2$

## 5. Computational Implementation and Graphics

```python
"""
Edelstein Effect in Rashba Fermion Systems
Complete calculation with all plots
"""
import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.054571817e-34      # J·s
m_e = 9.1093837015e-31      # kg
e_charge = 1.602176634e-19  # C
mu_B = 9.2740100783e-24     # J/T

# Parameters
m_star = 0.05*m_e
alpha_R = 0.5e-11*e_charge   # J·m
E_F = 20e-3*e_charge         # J
tau = 1e-12                  # s
g_factor = 4
chi = +1

# Derived quantities
E_SO = m_star*alpha_R**2/(2*hbar**2)
k0 = np.sqrt(2*m_star*E_F + (m_star*alpha_R/hbar)**2)/hbar
kF_plus = k0 - chi*m_star*alpha_R/hbar**2
kF_minus = k0 + chi*m_star*alpha_R/hbar**2
v_F = hbar*k0/m_star

# Edelstein susceptibility
chi_Ed = g_factor*mu_B*e_charge*tau*alpha_R/(4*np.pi*hbar)

# Conversion: A·m²/V → μ_B/(nm²·(V/cm))
conv = 1e-20/mu_B*100  # μ_B/(nm²·(V/cm)) per A·m²/V

# ========== PLOT 1: Energy dispersion ==========
fig, ax = plt.subplots(figsize=(8,6))
k_x = np.linspace(-0.03e10, 0.03e10, 400)
eps_plus = hbar**2*k_x**2/(2*m_star) + chi*alpha_R*np.abs(k_x)
eps_minus = hbar**2*k_x**2/(2*m_star) - chi*alpha_R*np.abs(k_x)
ax.plot(k_x/1e10, eps_plus/e_charge*1e3, 'r-', lw=2, label=r'$\varepsilon_+(k)$')
ax.plot(k_x/1e10, eps_minus/e_charge*1e3, 'b-', lw=2, label=r'$\varepsilon_-(k)$')
ax.axhline(E_F/e_charge*1e3, color='g', ls='--', lw=1.5, label=r'$E_F$')
ax.axhline(E_SO/e_charge*1e3, color='gray', ls=':', lw=1, label=r'$E_{SO}$')
ax.plot(0, 0, 'ko', ms=8, label='Dirac point')
ax.set_xlabel(r'$k_x$ ($\AA^{-1}$)', fontsize=14)
ax.set_ylabel('Energy (meV)', fontsize=14)
ax.set_title('Rashba Band Structure at Γ Point', fontsize=16)
ax.legend(fontsize=11); ax.grid(True, alpha=0.3)
ax.set_xlim(-0.03, 0.03); ax.set_ylim(-5, 15)
plt.tight_layout(); plt.savefig('fig1_dispersion.png', dpi=150); plt.show()

# ========== PLOT 2: Spin texture ==========
fig, ax = plt.subplots(figsize=(8,8))
k_vals = np.linspace(-0.025e10, 0.025e10, 15)
KX, KY = np.meshgrid(k_vals, k_vals)
phi_k = np.arctan2(KY, KX)
Sx = chi*np.sin(phi_k); Sy = -chi*np.cos(phi_k)  # lower band
norm = np.sqrt(Sx**2 + Sy**2 + 1e-10)
ax.quiver(KX/1e10, KY/1e10, Sx/norm, Sy/norm, color='steelblue', 
          alpha=0.8, scale=30, width=0.002)
theta = np.linspace(0, 2*np.pi, 200)
for kF, col in [(kF_plus,'red'), (kF_minus,'blue')]:
    ax.plot(kF*np.cos(theta)/1e10, kF*np.sin(theta)/1e10, color=col, lw=2)
ax.set_xlabel(r'$k_x$ ($\AA^{-1}$)', fontsize=14)
ax.set_ylabel(r'$k_y$ ($\AA^{-1}$)', fontsize=14)
ax.set_title(f'Spin-Momentum Locking (χ = {chi:+d})', fontsize=16)
ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('fig2_spin_texture.png', dpi=150); plt.show()

# ========== PLOT 3: M vs field direction ==========
theta_E = np.linspace(0, 2*np.pi, 200)
E_mag = 100  # V/m
M_x = chi*chi_Ed*E_mag*(-np.sin(theta_E))
M_y = chi*chi_Ed*E_mag*np.cos(theta_E)
M_norm = np.sqrt(M_x**2 + M_y**2)

fig, ax = plt.subplots(figsize=(8,8), subplot_kw={'projection':'polar'})
ax.plot(theta_E, M_norm*conv, 'b-', lw=2)
for ang in np.linspace(0, 2*np.pi, 8, endpoint=False):
    mx = chi*chi_Ed*E_mag*(-np.sin(ang))*conv
    my = chi*chi_Ed*E_mag*np.cos(ang)*conv
    ax.plot(ang, np.hypot(mx,my), 'ro', ms=6)
    ax.annotate('', xy=(ang, np.hypot(mx,my)), xytext=(ang, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
ax.set_title('|M| vs E Direction\n(μ_B/nm², E = 1 V/cm)', fontsize=14)
plt.tight_layout(); plt.savefig('fig3_direction.png', dpi=150); plt.show()

# ========== PLOT 4: M vs E magnitude ==========
E_vals = np.linspace(0, 10, 100)  # V/cm
E_SI = E_vals*100
M_y = chi*chi_Ed*E_SI
M_x = np.zeros_like(M_y)
M_norm = np.abs(M_y)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(E_vals, M_x*conv, 'b--', lw=2, label=r'$M_x$')
ax.plot(E_vals, M_y*conv, 'r-', lw=2, label=r'$M_y$')
ax.plot(E_vals, M_norm*conv, 'g:', lw=2, label=r'$|\mathbf{M}|$')
ax.set_xlabel('Electric field (V/cm)', fontsize=14)
ax.set_ylabel(r'Magnetization ($\mu_B$/nm²)', fontsize=14)
ax.set_title('Magnetization vs E (E along x)', fontsize=16)
ax.legend(fontsize=12); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('fig4_vs_E.png', dpi=150); plt.show()

# ========== PLOT 5: M vs α_R ==========
alpha_vals = np.linspace(0, 2e-11, 200)*e_charge
chi_Ed_alpha = g_factor*mu_B*e_charge*tau*alpha_vals/(4*np.pi*hbar)
M_alpha = chi_Ed_alpha*100  # E = 100 V/m

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(alpha_vals/e_charge*1e11, M_alpha*conv, 'b-', lw=2)
ax.axvline(0.5, color='r', ls='--', lw=1, label='InGaAs value')
ax.set_xlabel(r'$\alpha_R$ ($10^{-11}$ eV·m)', fontsize=14)
ax.set_ylabel(r'$|\mathbf{M}|$ ($\mu_B$/nm²)', fontsize=14)
ax.set_title('Magnetization vs Rashba SOC Strength', fontsize=16)
ax.legend(fontsize=12); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('fig5_vs_alpha.png', dpi=150); plt.show()

# ========== PLOT 6: M vs E_F ==========
n_i = 1e15; V0 = 1e-28
E_F_range = np.linspace(0.01e-3, 50e-3, 300)*e_charge

k0_r = np.sqrt(2*m_star*E_F_range + (m_star*alpha_R/hbar)**2)/hbar
kF_p = np.maximum(k0_r - chi*m_star*alpha_R/hbar**2, 1e-10)
kF_m = np.maximum(k0_r + chi*m_star*alpha_R/hbar**2, 1e-10)

N_plus = m_star/(2*np.pi*hbar**2)*(1 + chi*alpha_R*m_star/(hbar**2*kF_p))**(-1)
N_minus = m_star/(2*np.pi*hbar**2)*(1 - chi*alpha_R*m_star/(hbar**2*kF_m))**(-1)
N_tot = N_plus + N_minus
tau_i = hbar**2/(2*np.pi*n_i*V0**2*N_tot)

chi_Ed_E = g_factor*mu_B*e_charge*tau_i*alpha_R/(4*np.pi*hbar)
mask = E_F_range < E_SO
chi_Ed_E[mask] *= (1 - E_F_range[mask]/E_SO)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(E_F_range/e_charge*1e3, chi_Ed_E/np.max(chi_Ed_E), 'b-', lw=2)
ax.axvline(E_SO/e_charge*1e3, color='r', ls='--', lw=1.5, label=r'$E_{SO}$')
ax.set_xlabel('Fermi energy (meV)', fontsize=14)
ax.set_ylabel('Normalized Edelstein susceptibility', fontsize=14)
ax.set_title('Edelstein Susceptibility vs Fermi Energy', fontsize=16)
ax.legend(fontsize=12); ax.grid(True, alpha=0.3)
plt.tight_layout(); plt.savefig('fig6_vs_EF.png', dpi=150); plt.show()

# ========== PLOT 7: Chirality effect ==========
fig, axes = plt.subplots(1, 2, figsize=(12,6))
arrow_scale = 1e-12
E_fixed = 100  # V/m

for idx, chi_val in enumerate([+1, -1]):
    ax = axes[idx]
    M_vec = chi_val*chi_Ed*E_fixed*np.array([0, 1])
    E_vec = np.array([1, 0])*E_fixed
    
    ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
    ax.arrow(0, 0, E_vec[0]*arrow_scale, E_vec[1]*arrow_scale, 
             head_width=0.02, head_length=0.02, fc='red', ec='red', lw=2, label='E')
    ax.arrow(0, 0, M_vec[0]*arrow_scale, M_vec[1]*arrow_scale, 
             head_width=0.02, head_length=0.02, fc='blue', ec='blue', lw=2, label='M')
    ax.set_xlim(-0.15, 0.15); ax.set_ylim(-0.15, 0.15)
    ax.set_aspect('equal'); ax.set_title(f'χ = {chi_val:+d}', fontsize=14)
    ax.legend(fontsize=10); ax.grid(True, alpha=0.3)
    ax.set_xlabel('x', fontsize=12); ax.set_ylabel('y', fontsize=12)

fig.suptitle('Chirality Effect on Magnetization (E along +x)', fontsize=16)
plt.tight_layout(); plt.savefig('fig7_chirality.png', dpi=150); plt.show()

# ========== Numerical summary ==========
print("=== RESULTS ===")
print(f"E_SO = {E_SO/e_charge*1e3:.3f} meV")
print(f"k0 = {k0:.3e} m⁻¹, v_F = {v_F:.3e} m/s")
print(f"k_F l = {k0*v_F*tau:.1f}")
print(f"Edelstein susceptibility = {chi_Ed*conv:.3e} μ_B/(nm²·(V/cm))")
print(f"For E = 1 V/cm along x: M = ({0:.2e}, {chi*chi_Ed*100*conv:.4f}) μ_B/nm²")
print(f"|M| = {abs(chi*chi_Ed*100)*conv:.4f} μ_B/nm²")
```

## 6. Summary of Key Results

| Property | Result |
|---|---|
| **Magnetization formula** | $\mathbf{M} = \chi\frac{g\mu_B e\tau\alpha_R}{4\pi\hbar}(\hat{z}\times\mathbf{E})$ |
| **Direction** | Always perpendicular to $\mathbf{E}$ in the 2D plane |
| **Magnitude** | $|\mathbf{M}| = \frac{g\mu_B e\tau\alpha_R}{4\pi\hbar}|\mathbf{E}|$ |
| **$\alpha_R$ dependence** | Linear ($\mathbf{M} \to 0$ as $\alpha_R \to 0$) |
| **Chirality** | $\chi = -1$ reverses $\mathbf{M}$ direction |
| **Field direction** | $|\mathbf{M}|$ independent of $\theta_E$ |
| **$E_F$ dependence** | Through $\tau(E_F)$; vanishes at $E_F=0$ |
| **Units** | $\chi_{\text{Edelstein}} = 3.87\times10^{-8}\ \mu_B/(\text{nm}^2\cdot\text{V/cm})$ |

The model is valid in the **diffusive limit** ($k_F l \gg 1$) at **zero temperature** ($T \ll E_F/k_B$) and assumes **linear response** ($v_d \ll v_F$).
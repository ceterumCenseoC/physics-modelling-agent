# Realistic Starting Parameters for the Corrected Rashba-Edelstein Model

## 1. Parameter Units and Conventions

Before presenting the parameter values, I clarify the **corrected units** for all model parameters, as derived from the dimensional analysis:

| Parameter | Symbol | Correct Units (SI) | Units in Condensed Matter Practice |
|-----------|--------|-------------------|-----------------------------------|
| Effective mass | $m$ | kg | $m_e$ (electron rest mass) |
| Rashba SOC strength | $\alpha$ | m/s (velocity) | eV·Å (energy × length) |
| Wavevector | $k$ | m⁻¹ | Å⁻¹ |
| Fermi energy | $E_F$ | J | eV |
| Electric field | $E$ | V/m | V/cm |
| Relaxation time | $\tau$ | s | ps |
| Magnetization (2D) | $M$ | A/m (3D) or A (2D) | μB·nm⁻² |
| Dimensionless parameter | $\gamma$ | — | — |

**Key conversion**: The Rashba parameter in the Hamiltonian $H_R = \alpha(\mathbf{p}\times\boldsymbol{\sigma})\cdot\hat{z}$ has units of **velocity** (m/s). In the literature, it is often quoted in eV·Å. The conversion is:

$$\alpha \left[\text{eV·Å}\right] = \alpha \left[\text{m/s}\right] \times \frac{\hbar}{e} = \alpha \left[\text{m/s}\right] \times 6.582 \times 10^{-16} \text{ eV·s} \times 10^{10} \text{ Å/m} = \alpha \left[\text{m/s}\right] \times 6.582 \times 10^{-6} \text{ eV·Å·s/m}$$

For example, $\alpha = 10^5 \text{ m/s}$ corresponds to $\alpha \approx 0.66 \text{ eV·Å}$.

---

## 2. Representative Material Systems

I propose starting parameters for three archetypal Rashba 2DEG systems that have been extensively studied experimentally:

### 2.1. **InGaAs/InAlAs Quantum Well** (semiconductor 2DEG)
- **Reference**: Nitta et al., *Phys. Rev. Lett.* **78**, 1335 (1997); Koga et al., *Phys. Rev. Lett.* **89**, 046801 (2002)
- **Parameters**:
  - $m^* = 0.05\,m_e$ (InGaAs effective mass)
  - $\alpha = 2.5 \times 10^{-11} \text{ eV·m} = 0.25 \text{ eV·Å}$
  - $\tau = 1\text{–}10 \text{ ps}$ (typical mobility ~ $10^4\text{–}10^5 \text{ cm}^2/\text{Vs}$)
  - $n = 10^{12} \text{ cm}^{-2}$ (2D carrier density)
  - $E_F = \hbar^2 k_F^2/(2m^*) \approx 50\text{–}100 \text{ meV}$

### 2.2. **Au(111) Surface State** (noble metal surface)
- **Reference**: LaShell et al., *Phys. Rev. Lett.* **77**, 3419 (1996); Ast et al., *Phys. Rev. Lett.* **98**, 186807 (2007)
- **Parameters**:
  - $m^* = 0.25\,m_e$
  - $\alpha = 4.0 \times 10^{-10} \text{ eV·m} = 4.0 \text{ eV·Å}$ (strong Rashba)
  - $\tau = 10\text{–}100 \text{ fs}$ (surface state lifetime)
  - $n = 10^{13}\text{–}10^{14} \text{ cm}^{-2}$
  - $E_F = 0.3\text{–}0.5 \text{ eV}$ above band bottom

### 2.3. **BiAg(111) Surface Alloy** (surface alloy with giant Rashba splitting)
- **Reference**: Ast et al., *Phys. Rev. Lett.* **98**, 186807 (2007); Bihlmayer et al., *Phys. Rev. B* **75**, 195414 (2007)
- **Parameters**:
  - $m^* = 0.3\,m_e$
  - $\alpha = 3.3 \times 10^{-10} \text{ eV·m} = 3.3 \text{ eV·Å}$
  - $\tau = 10\text{–}50 \text{ fs}$
  - $n = 5 \times 10^{13} \text{ cm}^{-2}$
  - $E_F = 0.2\text{–}0.4 \text{ eV}$

---

## 3. Dimensionless Parameter $\gamma$ Values

The key dimensionless parameter for the nonlinear regime is:

$$\gamma = \frac{eEL_s}{E_F}, \quad \text{with} \quad L_s = \frac{\hbar}{2m\alpha}$$

### 3.1. Computed $L_s$ values for each system:

| System | $m^*/m_e$ | $\alpha$ (eV·Å) | $L_s$ (nm) |
|--------|-----------|-----------------|------------|
| InGaAs | 0.05 | 0.25 | 2.6 |
| Au(111) | 0.25 | 4.0 | 1.1 |
| BiAg(111) | 0.30 | 3.3 | 1.6 |

### 3.2. Typical $\gamma$ values for experimentally accessible fields:

For a field $E = 10^2 \text{ V/cm} = 10^4 \text{ V/m}$:

| System | $E_F$ (meV) | $\gamma$ |
|--------|-------------|----------|
| InGaAs | 75 | $4.5 \times 10^{-6}$ |
| Au(111) | 400 | $2.2 \times 10^{-7}$ |
| BiAg(111) | 300 | $5.3 \times 10^{-7}$ |

**Conclusion**: For typical laboratory fields ($10^2\text{–}10^4$ V/cm), the system is **deeply in the linear regime** ($\gamma \ll 1$). Nonlinear effects ($\gamma \sim 0.1$) require:
- $E \sim 10^5\text{–}10^6$ V/cm (for InGaAs)
- $E \sim 10^6\text{–}10^7$ V/cm (for Au, BiAg)

These are accessible in **pulsed-field** or **THz-pump** experiments.

---

## 4. Starting Parameters for Numerical Simulations

Based on the analysis above, I propose the following **default starting parameters** for the corrected model:

### 4.1. Isotropic Rashba Model (Baseline)

```python
# Physical constants
hbar = 6.582119569e-16    # eV·s
e    = 1.602176634e-19    # C
mu_B = 5.788381806e-5     # eV/T
m_e  = 9.1093837015e-31   # kg
m_e_ev = 5.685630e-16     # eV·s²/m² (electron mass in eV units)

# System parameters (InGaAs quantum well)
alpha = 0.25              # eV·Å (Rashba SOC)
m_star = 0.05 * m_e_ev    # eV⁻¹·Å⁻² (effective mass)
E_F = 0.075               # eV (Fermi energy)
tau = 5e-12               # s (relaxation time)
E_field = 1e4             # V/m (electric field)
T = 4.2                   # K (temperature)

# Derived quantities
k0 = m_star * alpha / hbar  # Å⁻¹ (momentum offset)
L_s = hbar / (2 * m_star * alpha)  # Å (spin precession length)
gamma = e * E_field * L_s / E_F  # dimensionless

# Momentum grid
kmax = 2 * (k0 + sqrt(k0**2 + 2*m_star*E_F/hbar**2))  # Å⁻¹
Nk = 2000                # radial grid points
Ntheta = 2000            # angular grid points
```

### 4.2. Anisotropic Model (with $C_{2v}$ symmetry)

```python
# Anisotropy parameters (for surface with C2v symmetry)
m_x = 0.05 * m_e_ev      # eV⁻¹·Å⁻²
m_y = 0.10 * m_e_ev      # eV⁻¹·Å⁻² (r_m = 2.0)
alpha_x = 0.25           # eV·Å
alpha_y = 0.50           # eV·Å (r_alpha = 2.0)

# Mass anisotropy ratio
r_m = m_y / m_x          # dimensionless
# SOC anisotropy ratio
r_alpha = alpha_y / alpha_x  # dimensionless
```

---

## 5. Detailed Parameter Justification

### 5.1. Effective Mass $m^*$

- **Semiconductor 2DEGs** (InGaAs, GaAs, InAs): $m^*/m_e \in [0.02, 0.1]$ — from **band structure calculations** and **cyclotron resonance** measurements [1,2].
- **Metal surfaces** (Au, Ag, Bi): $m^*/m_e \in [0.2, 0.5]$ — from **angle-resolved photoemission spectroscopy (ARPES)** band dispersions [3,4].
- **Oxide interfaces** (LaAlO₃/SrTiO₃): $m^*/m_e \sim 0.7$ — from **quantum oscillations** and **transport** measurements [5].

**Suggested starting value**: $m^* = 0.05\,m_e$ (typical for high-mobility InGaAs).

### 5.2. Rashba Coupling Strength $\alpha$

The Rashba parameter ranges across several orders of magnitude depending on the system:

| System | $\alpha$ (eV·Å) | Source |
|--------|-----------------|--------|
| GaAs 2DEG | 0.001–0.01 | [6] |
| InGaAs/InAlAs | 0.1–0.3 | [1,2] |
| InAs 2DEG | 0.5–1.0 | [7] |
| Au(111) surface | 3–4 | [3,8] |
| BiAg(111) alloy | 3–4 | [4,9] |
| BiTeI bulk | 3.8 | [10] |

**Physical origin**: The Rashba coupling arises from:
1. **Structural inversion asymmetry** (SIA) — asymmetric quantum well potentials
2. **Atomic spin-orbit interaction** — stronger for heavier elements ($\alpha \propto Z^2$)
3. **Interface effects** — electric fields at heterojunctions

**Suggested starting value**: $\alpha = 0.25$ eV·Å (moderate, well-studied InGaAs value).

### 5.3. Fermi Energy $E_F$

The Fermi energy determines which regime (HDR vs. LDR) the system occupies.

**Band crossing energy**: $E_{\text{cross}} = -m\alpha^2/(2\hbar^2)$

For $\alpha = 0.25$ eV·Å and $m^* = 0.05m_e$:
$$E_{\text{cross}} = -\frac{0.05 \times (0.25)^2}{2 \times (1973)^2} \text{ eV} = -1.0 \times 10^{-7} \text{ eV} \approx 0$$

This is negligibly small for most systems, meaning:
- **HDR** ($E_F > E_{\text{cross}}$) is the standard regime
- **LDR** requires extremely low densities ($n < 10^{10} \text{ cm}^{-2}$)

**Suggested starting values**:
- HDR: $E_F = 75$ meV (carrier density $n = 10^{12} \text{ cm}^{-2}$)
- LDR (test case): $E_F = 0.5$ meV (carrier density $n = 10^9 \text{ cm}^{-2}$)

The carrier density relates to Fermi energy via:
$$n = \frac{m^* E_F}{\pi\hbar^2} \quad \text{(2D, both spins)}$$

### 5.4. Relaxation Time $\tau$

The transport relaxation time is related to mobility via:
$$\tau = \frac{m^* \mu}{e}$$

| System | Mobility (cm²/Vs) | $\tau$ (ps) |
|--------|-------------------|-------------|
| GaAs 2DEG | $10^5\text{–}10^6$ | 10–100 |
| InGaAs 2DEG | $10^4\text{–}10^5$ | 1–10 |
| Metal surface | 100–1000 | 0.01–0.1 |

**Suggested starting value**: $\tau = 5$ ps (moderate mobility InGaAs).

**Important caveat**: In the Boltzmann transport formula, $\tau$ is the **transport lifetime** which includes vertex corrections. For Rashba systems, these corrections can be significant [11]. The proper transport time is:

$$\bar{\tau}_k = \frac{\tau_0}{1 - \langle\cos\theta\rangle_{\text{scatt}}}$$

where $\tau_0$ is the single-particle lifetime and the angular average accounts for scattering anisotropy.

### 5.5. Electric Field $E$

The linear response regime requires $\gamma \ll 1$, which translates to:

$$E \ll \frac{E_F}{eL_s}$$

For InGaAs ($E_F = 75$ meV, $L_s = 2.6$ nm):
$$E_{\max} = \frac{0.075}{1.6\times10^{-19} \times 2.6\times10^{-9}} = 1.8 \times 10^8 \text{ V/m} = 1.8 \times 10^6 \text{ V/cm}$$

**Suggested starting values**:
- **Linear regime**: $E = 10^4$ V/m (100 V/cm) — safe, well within linear response
- **Nonlinear regime** (for exploring $\gamma \sim 0.1$): $E = 2\times10^7$ V/m (200 kV/cm) — achievable with pulsed fields

### 5.6. Temperature

The model assumes $T = 0$ (no thermal broadening). For finite temperature, the delta function in the susceptibility integral should be replaced by the derivative of the Fermi function:

$$-\frac{\partial f(E)}{\partial E} = \frac{1}{4k_BT}\text{sech}^2\left(\frac{E-E_F}{2k_BT}\right)$$

**Suggested starting values**:
- **Zero temperature**: $T = 0$ K (theoretical)
- **Finite temperature**: $T = 4.2$ K (liquid helium) or $T = 77$ K (liquid nitrogen)

The thermal smearing is negligible when $k_BT \ll E_F$:
- $T = 4.2$ K: $k_BT = 0.36$ meV (0.5% of $E_F$ for InGaAs)
- $T = 77$ K: $k_BT = 6.6$ meV (9% of $E_F$)

### 5.7. Momentum Grid Parameters

For numerical convergence:

- **Radial cutoff**: $k_{\max} = 2.5\,k_F^{-}$ (include states well above the Fermi surface)
- **Radial resolution**: $\Delta k = k_F/500$ (sufficient for sharp delta functions)
- **Angular resolution**: $\Delta\theta = 2\pi/1000$ (for smooth angular integration)

The delta function broadening should be:
$$\eta = 0.1\text{–}1 \text{ meV}$$

---

## 6. Complete Recommended Parameter Set

### 6.1. Baseline Simulation (Isotropic, HDR, Linear Regime)

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Effective mass | $m^*$ | $0.05\,m_e$ | kg |
| Rashba coupling | $\alpha$ | 0.25 | eV·Å |
| Fermi energy | $E_F$ | 75 | meV |
| Relaxation time | $\tau$ | 5 | ps |
| Electric field | $E_x$ | $10^4$ | V/m |
| Temperature | $T$ | 4.2 | K |
| Momentum cutoff | $k_{\max}$ | 0.1 | Å⁻¹ |
| Grid points | $N_k \times N_\theta$ | $2000 \times 2000$ | — |
| Delta broadening | $\eta$ | 0.5 | meV |

**Derived quantities**:
- $k_0 = m^*\alpha/\hbar = 4.9 \times 10^{-3}$ Å⁻¹
- $k_F^+ = 2.5 \times 10^{-2}$ Å⁻¹ (outer band)
- $k_F^- = 3.4 \times 10^{-2}$ Å⁻¹ (inner band)
- $L_s = \hbar/(2m^*\alpha) = 26$ Å
- $\gamma = eE L_s/E_F = 3.5 \times 10^{-6}$ (deeply linear)
- $v_F = \hbar k_F/m^* = 2.2 \times 10^5$ m/s

**Expected result** (analytical):
$$M_y = \frac{\mu_B e\tau}{2\pi\hbar} m^*\alpha E_x = 3.5 \times 10^{-10} \text{ A} = 0.35 \text{ nA}$$

In terms of spin density:
$$S_y = \frac{M_y}{\mu_B} = 6.0 \times 10^{12} \text{ m}^{-2} = 6.0 \times 10^8 \text{ cm}^{-2}$$

### 6.2. Anisotropic Model Parameters

For the $C_{2v}$ case, use:

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Mass along x | $m_x$ | $0.05\,m_e$ | kg |
| Mass along y | $m_y$ | $0.10\,m_e$ | kg |
| Mass ratio | $r_m$ | 2.0 | — |
| SOC along x | $\alpha_x$ | 0.25 | eV·Å |
| SOC along y | $\alpha_y$ | 0.50 | eV·Å |
| SOC ratio | $r_\alpha$ | 2.0 | — |

**Expected susceptibility enhancement**:
$$\frac{\chi_{xy}}{\chi_0} = \frac{4\pi m_x\alpha_x\,r_m}{1+\sqrt{r_m}} \times \frac{4\pi m\alpha_x r_\alpha}{1+r_\alpha}$$

For $r_m = 2$, $r_\alpha = 2$:
$$\frac{\chi_{xy}}{\chi_0} = \frac{2}{1+\sqrt{2}} \times \frac{2}{3} = 0.828 \times 0.667 = 0.552$$

Compared to isotropic ($r_m = r_\alpha = 1$): $\chi_{xy}/\chi_0 = 1$
The anisotropy **reduces** the response in this configuration.

### 6.3. Nonlinear Regime Parameters

To explore the nonlinear Edelstein effect:

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Electric field | $E_x$ | $2 \times 10^7$ | V/m |
| Dimensionless parameter | $\gamma$ | 0.1 | — |
| Fermi energy | $E_F$ | 75 | meV |
| Rashba coupling | $\alpha$ | 0.25 | eV·Å |

At $\gamma = 0.1$, the long-time spin polarization is reduced by ~10% from the adiabatic limit:
$$\frac{S_y(\infty)}{S_y^{\text{max}}} \approx 0.9$$

---

## 7. Sources for Parameter Values

### Primary Sources (Original Experimental Measurements):

1. **Nitta, J., Akazaki, T., Takayanagi, H., & Enoki, T.** "Gate Control of Spin-Orbit Interaction in an Inverted In₀.₅₃Ga₀.₄₇As/In₀.₅₂Al₀.₄₈As Heterostructure," *Phys. Rev. Lett.* **78**, 1335 (1997). — $\alpha = 0.2\text{–}0.6$ eV·Å for InGaAs 2DEG.

2. **Koga, T., Nitta, J., Akazaki, T., & Takayanagi, H.** "Rashba Spin-Orbit Coupling Probed by the Weak Antilocalization Analysis in InAlAs/InGaAs/InAlAs Quantum Wells," *Phys. Rev. Lett.* **89**, 046801 (2002). — Systematic study of $\alpha$ vs. gate voltage.

3. **LaShell, S., McDougall, B. A., & Jensen, E.** "Spin Splitting of an Au(111) Surface State Band," *Phys. Rev. Lett.* **77**, 3419 (1996). — First observation of Rashba splitting on Au(111), $\alpha = 3.3$ eV·Å.

4. **Ast, C. R., et al.** "Giant Spin Splitting through Surface Alloying," *Phys. Rev. Lett.* **98**, 186807 (2007). — BiAg(111) alloy with $\alpha = 3.3$ eV·Å.

### Secondary Sources (Compilations and Reviews):

5. **Bihlmayer, G., Rader, O., & Winkler, R.** "Focus on the Rashba effect," *New J. Phys.* **17**, 050202 (2015). — Comprehensive review of Rashba parameters.

6. **Manchon, A., Koo, H. C., Nitta, J., Frolov, S. M., & Duine, R. A.** "New perspectives for Rashba spin-orbit coupling," *Nature Materials* **14**, 871 (2015). — Overview of material systems and applications.

7. **Soumyanarayanan, A., Reyren, N., Fert, A., & Panagopoulos, C.** "Emergent phenomena induced by spin-orbit coupling at surfaces and interfaces," *Nature* **539**, 509 (2016). — Surface and interface Rashba systems.

8. **Ast, C. R., et al.** "Multidirectional surface bands on BiAg(111)," *Phys. Rev. B* **75**, 195414 (2007). — Detailed band structure of BiAg(111).

### Theoretical Parameters:

9. **Gaiardoni, I., et al.** "Edelstein Effect in Isotropic and Anisotropic Rashba Models," arXiv:2503.20712 (2025). — Parameters used in the theoretical model: $m = 0.05\,m_e$, $\alpha = 0.25$ eV·Å, $\tau = 1$ ps.

10. **Vignale, G., & Tokatly, I. V.** "Theory of the nonlinear Rashba-Edelstein effect: The clean electron gas limit," *Phys. Rev. B* **93**, 035310 (2016). — Clean limit parameters: $n = 10^{12}$ cm⁻², $\alpha = 10^5$ m/s.

---

## 8. Practical Recommendations

### 8.1. For Model Validation

1. **Start with the analytical HDR formula**:
   $$M_y = \frac{\mu_B e\tau}{2\pi\hbar} m^*\alpha E_x$$
   
   This provides an exact reference to test the numerical code.

2. **Verify the LDR → HDR transition**: Sweep $E_F$ from 1 meV to 200 meV and check:
   - LDR: $M_y \propto \sqrt{m^2\alpha^2 + 2mE_F}$
   - HDR: $M_y = $ constant (independent of $E_F$)

3. **Check the $\mathbf{M} \perp \mathbf{E}$ property**: For $E_x \neq 0$, $E_y = 0$, verify $M_x = 0$ and $M_y \neq 0$.

### 8.2. For Numerical Convergence

- **Delta function**: Use Lorentzian broadening with $\eta = 0.5$ meV for $E_F = 75$ meV. Reduce $\eta$ to 0.1 meV for convergence checks.
- **Momentum cutoff**: $k_{\max} = 4\,k_F^+$ ensures all contributing states are included.
- **Grid density**: Increase $N_k, N_\theta$ until $M_y$ changes by less than 0.1%.

### 8.3. For Comparison with Experiments

- **Magnetization measurement**: Use **Kerr rotation** or **SQUID magnetometry** to detect the induced spin density.
- **Edelstein susceptibility**: Reported values range from $10^{-10}$ to $10^{-8}$ A·m/V for typical 2DEGs [7,8].
- **Spin accumulation**: For $E = 10^4$ V/m and $\tau = 5$ ps, expect $S_y \sim 10^{12}$ m⁻², detectable with optical methods.

### 8.4. Parameter Sensitivity Analysis

| Parameter | Sensitivity of $M_y$ | Recommendation |
|-----------|----------------------|----------------|
| $\alpha$ | Linear | Measure precisely via weak antilocalization or ARPES |
| $m^*$ | Linear | Determine from cyclotron resonance or quantum oscillations |
| $\tau$ | Linear | Extract from mobility; use transport lifetime not single-particle lifetime |
| $E_F$ | None (HDR) | Ensure $E_F > E_{\text{cross}}$ for HDR validity |
| $E$ | Linear (small $\gamma$) | Keep $\gamma < 0.01$ for linear regime |

---

## 9. Summary of Starting Parameters

The following parameter set is recommended as the **default starting point** for the corrected Rashba-Edelstein model:

```python
# =====================================================
# DEFAULT STARTING PARAMETERS (InGaAs 2DEG)
# =====================================================

# Physical constants (exact values)
hbar = 1.054571817e-34      # J·s (reduced Planck constant)
h_bar_eV = 6.582119569e-16  # eV·s
e = 1.602176634e-19         # C (elementary charge)
mu_B = 9.2740100783e-24     # J/T (Bohr magneton)
m_e = 9.1093837015e-31      # kg (electron mass)

# Material parameters (InGaAs/InAlAs quantum well)
m_star = 0.05 * m_e         # kg (effective mass)
alpha_eV_A = 0.25           # eV·Å (Rashba coupling)
alpha_SI = alpha_eV_A * 1e-10 * e / hbar  # m/s (convert to velocity units)

# Fermi energy and density
E_F = 0.075 * e             # J (75 meV)
n_2D = m_star * E_F / (pi * hbar**2)  # m⁻² (carrier density)

# Transport
tau = 5e-12                 # s (transport relaxation time)

# Electric field (linear regime)
E_field = 1e4               # V/m (10 kV/m = 100 V/cm)

# Temperature
T = 4.2                     # K

# Derived quantities
k0 = m_star * alpha_SI / hbar     # m⁻¹ (momentum offset)
L_s = hbar / (2 * m_star * alpha_SI)  # m (spin precession length)
gamma = e * E_field * L_s / E_F   # dimensionless (should be << 1)

# Numerical grid
kmax = 2.5 * (k0 + sqrt(k0**2 + 2*m_star*E_F/hbar**2))  # m⁻¹
Nk = 2000
Ntheta = 2000
eta_broadening = 0.5e-3 * e  # J (0.5 meV Lorentzian broadening)

# Expected result (analytical check)
M_y_expected = mu_B * e * tau * m_star * alpha_SI * E_field / (2*pi*hbar)  # A
S_y_expected = M_y_expected / mu_B  # m⁻² (spin density)

print(f"k0 = {k0:.3e} m⁻¹")
print(f"L_s = {L_s:.3e} m = {L_s*1e10:.1f} Å")
print(f"gamma = {gamma:.3e}")
print(f"Expected My = {M_y_expected:.3e} A")
print(f"Expected Sy = {S_y_expected:.3e} m⁻²")
```

This parameter set is **physically realistic**, **numerically tractable**, and **directly comparable** to experimental measurements on InGaAs-based 2DEGs. The dimensionless parameter $\gamma \approx 10^{-6}$ guarantees operation in the linear regime, allowing validation against the analytical formulas before exploring more complex regimes.
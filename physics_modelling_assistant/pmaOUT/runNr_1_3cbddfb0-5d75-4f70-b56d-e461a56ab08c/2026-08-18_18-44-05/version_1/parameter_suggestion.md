# Realistic Starting Parameters for the Corrected Edelstein Effect Model

## 1. Overview of Parameter Selection Strategy

The corrected model describes the Edelstein effect in Rashba spin–orbit coupled 2D electron gases. For realistic simulations, parameters must be chosen from experimentally characterized material systems. I present parameters for three benchmark material platforms: (i) **InGaAs/InAlAs quantum wells** (the canonical Rashba 2DEG), (ii) **surface states of topological insulators** (massless Dirac-like Rashba fermions), and (iii) **LaAlO₃/SrTiO₃ interfaces** (oxide 2DEG with tunable Rashba coupling).

---

## 2. Parameter Ranges and Justification

### 2.1 Rashba Parameter $\alpha_R$

**Physical meaning:** Spin–orbit coupling strength quantifying the momentum-dependent spin splitting energy $\Delta E_{SO} = 2\alpha_R k$.

| Material System | $\alpha_R$ Range (eV·Å) | Reference |
|-----------------|------------------------|-----------|
| InGaAs/InAlAs QW | $0.1 - 0.7$ | Nitta et al., PRL **78**, 1335 (1997) |
| InAs/AlSb QW | $0.5 - 1.5$ | Grundler, PRL **84**, 6074 (2000) |
| Bi/Ag(111) surface | $2.0 - 3.8$ | Ast et al., PRL **98**, 186807 (2007) |
| LAO/STO interface | $0.01 - 0.05$ | Caviglia et al., PRL **104**, 126803 (2010) |
| Surface states (TI) | $1.0 - 4.0$ (via $v_F$) | Hsieh et al., Nature **460**, 1101 (2009) |

**Recommended starting value:** $\alpha_R = 0.5$ eV·Å (InGaAs QW – most studied system for Edelstein effect).

**Justification:** The Rashba parameter is directly extracted from **weak antilocalization (WAL) magnetoconductance fits** or **Shubnikov–de Haas oscillations** that resolve the beat frequency from spin-split bands. Values of 0.5 eV·Å correspond to spin splitting of ~10 meV at $k_F = 10^7$ m⁻¹, readily observable in transport.

---

### 2.2 Fermi Wavevector $k_F$

**Physical meaning:** Radius of the Fermi circle in the 2D Brillouin zone, determined by electron density $n_s$ via $k_F = \sqrt{2\pi n_s}$.

| Material System | $n_s$ (cm⁻²) | $k_F$ (Å⁻¹) | Reference |
|-----------------|--------------|-------------|-----------|
| InGaAs QW | $0.5 - 5 \times 10^{12}$ | $0.018 - 0.056$ | Nitta et al. (1997) |
| LAO/STO | $1 - 10 \times 10^{13}$ | $0.079 - 0.25$ | Caviglia et al. (2010) |
| Surface TI (Bi₂Se₃) | $1 - 10 \times 10^{12}$ | $0.025 - 0.079$ | Checkelsky et al., PRL **103**, 246601 (2009) |

**Recommended starting value:** $k_F = 0.03$ Å⁻¹ (corresponds to $n_s = 2.9 \times 10^{12}$ cm⁻²).

**Justification:** This density is typical for gated InGaAs heterostructures and gives $k_F$ large enough that the Rashba splitting $\alpha_R k_F \approx 15$ meV exceeds thermal energy at 4 K ($k_B T \approx 0.35$ meV), ensuring the zero-temperature formula applies.

---

### 2.3 Effective Mass $m^*$

**Physical meaning:** Curvature of the parabolic band; sets the kinetic energy scale and Fermi velocity for the parabolic model.

| Material System | $m^*$ (in units of $m_e$) | Reference |
|-----------------|---------------------------|-----------|
| InGaAs (In₀.₅₃Ga₀.₄₇As) | $0.041$ | Nitta et al. (1997) |
| InAs | $0.023$ | Grundler (2000) |
| LAO/STO | $0.7 - 3.0$ (heavy, density-dependent) | Caviglia et al. (2010) |
| GaAs 2DEG | $0.067$ | Winkler, "Spin-Orbit Coupling Effects in 2D Electron and Hole Systems" (2003) |

**Recommended starting value:** $m^* = 0.041 \, m_e = 3.73 \times 10^{-32}$ kg.

**Justification:** The In₀.₅₃Ga₀.₄₇As/In₀.₅₂Al₀.₄₈As quantum well lattice-matched to InP is the standard platform for Rashba studies due to its large spin-orbit coupling and high mobility. The effective mass is well-established from cyclotron resonance and band structure calculations.

---

### 2.4 Fermi Velocity $v_F$ (Massless Model)

**Physical meaning:** Velocity of Dirac-like fermions; for the massless Rashba model, it replaces the parabolic dispersion.

$$
v_F = \frac{\hbar k_F}{m^*} \quad \text{(for parabolic case)}
$$

**For massless case (topological surface states):**

| Material | $v_F$ (m/s) | Reference |
|----------|-------------|-----------|
| Bi₂Se₃ surface | $3.5 - 6.0 \times 10^5$ | Zhang et al., Nat. Phys. **5**, 438 (2009) |
| Bi₂Te₃ surface | $4.0 - 5.5 \times 10^5$ | Chen et al., Science **325**, 178 (2009) |
| Sb₂Te₃ surface | $3.0 - 4.5 \times 10^5$ | Jiang et al., PRL **108**, 096401 (2012) |

**Recommended starting value (massless model):** $v_F = 4.0 \times 10^5$ m/s.

**Justification:** This is the average Fermi velocity reported for Bi₂Se₃ (111) surface states from ARPES measurements. It corresponds to $\alpha_R = \hbar v_F = 2.6$ eV·Å, consistent with the strong spin-orbit coupling of these materials.

---

### 2.5 Momentum Relaxation Time $\tau$

**Physical meaning:** Average time between momentum-scattering events; controls the magnitude of the non-equilibrium distribution shift.

| Material System | $\tau$ (ps) | Mobility $\mu$ (cm²/V·s) | Reference |
|-----------------|-------------|--------------------------|-----------|
| High-mobility InGaAs QW | $0.5 - 10$ | $10^4 - 10^5$ | Nitta et al. (1997) |
| Standard InGaAs QW | $0.05 - 0.5$ | $10^3 - 10^4$ | Manchon et al., Nat. Mater. **14**, 871 (2015) |
| LAO/STO | $0.01 - 0.1$ | $10^2 - 10^3$ | Caviglia et al. (2010) |
| TI surface | $0.01 - 1$ | $10^2 - 10^4$ | Checkelsky et al. (2009) |

**Recommended starting value:** $\tau = 1$ ps.

**Justification:** For a typical 2DEG with mobility $\mu = 10^4$ cm²/V·s and effective mass $m^* = 0.041 m_e$:

$$
\tau = \frac{m^* \mu}{e} = \frac{(0.041 \times 9.11 \times 10^{-31} \text{ kg})(10^4 \times 10^{-4} \text{ m}^2/\text{V·s})}{1.602 \times 10^{-19} \text{ C}} \approx 1.0 \text{ ps}
$$

This represents a good-quality InGaAs quantum well achievable in molecular beam epitaxy (MBE) grown samples.

---

### 2.6 Fermi Energy $\varepsilon_F$

**Physical meaning:** Energy of the highest occupied state at zero temperature.

**Parabolic model:**
$$
\varepsilon_F = \frac{\hbar^2 k_F^2}{2m^*} + \alpha_R k_F
$$

For the recommended parameters ($k_F = 0.03$ Å⁻¹, $m^* = 0.041 m_e$, $\alpha_R = 0.5$ eV·Å):

$$
\varepsilon_F = \frac{(1.055 \times 10^{-34})^2 (3 \times 10^9)^2}{2(3.73 \times 10^{-32})} + (0.5 \times 1.602 \times 10^{-19})(3 \times 10^9)
$$

$$
\varepsilon_F = 8.5 \times 10^{-21} \text{ J} + 2.4 \times 10^{-19} \text{ J} \approx 0.016 \text{ eV}
$$

**Massless model:**
$$
\varepsilon_F = \hbar v_F k_F = (1.055 \times 10^{-34})(4.0 \times 10^5)(3 \times 10^9) = 1.27 \times 10^{-19} \text{ J} = 0.79 \text{ eV}
$$

**Recommended starting value:** $\varepsilon_F = 0.016$ eV (parabolic) or $\varepsilon_F = 0.79$ eV (massless).

**Justification:** These values place the Fermi level well above the Rashba band crossing point, ensuring both spin-split bands are occupied. The condition $\varepsilon_F \gg \alpha_R k_F$ guarantees we are in the "weak SOC" regime where the simple linear response formula is accurate.

---

### 2.7 Electric Field $\mathbf{E}$

**Physical meaning:** Driving field for the Edelstein effect; must be small enough for linear response but large enough for measurable spin accumulation.

**Recommended range:** $E = 10^2 - 10^4$ V/m.

**Justification:** 
- Lower bound ($10^2$ V/m): Ensures the drift velocity $v_d = \mu E = (10^4 \text{ cm}^2/\text{V·s})(10^2 \text{ V/m}) = 10 \text{ m/s}$ is much smaller than $v_F$, validating linear response.
- Upper bound ($10^4$ V/m): Below typical breakdown fields for III-V heterostructures (~$10^5$ V/m for pulsed operation).
- For a sample of length $L = 100$ μm, $E = 10^3$ V/m corresponds to applied voltage $V = 0.1$ V, which is experimentally straightforward.

**Recommended starting value:** $E_x = 10^3$ V/m (along $x$-axis).

---

### 2.8 Landé g-Factor

**Physical meaning:** Dimensionless factor relating spin to magnetic moment; material-dependent.

| Material System | $g$-factor | Reference |
|-----------------|------------|-----------|
| InGaAs QW | $-4$ to $-8$ | Nitta et al. (1997) |
| InAs QW | $-8$ to $-15$ | Grundler (2000) |
| GaAs 2DEG | $-0.44$ | Winkler (2003) |
| Free electron | $2.0023$ | Standard value |
| Bi₂Se₃ surface | ~$2$ (spin-1/2 Dirac fermion) | Zhang et al. (2009) |

**Recommended starting value:** $g = -4$ (InGaAs) or $g = 2$ (massless TI model).

**Justification:** The g-factor for InGaAs is strongly negative due to the narrow band gap and strong spin-orbit coupling. The magnitude is confirmed by **tilted-field magnetotransport** measurements. For the massless model, the effective g-factor for surface Dirac fermions is $g \approx 2$ from the spin-1/2 nature.

---

### 2.9 Temperature $T$

**Physical meaning:** Thermal energy scale relative to Fermi energy determines validity of zero-temperature formula.

**Recommended range:** $T = 0.01 - 4$ K (parabolic model), $T = 4 - 300$ K (massless model).

**Justification:**
- Parabolic model: $k_B T \ll \varepsilon_F = 16$ meV requires $T \ll 185$ K. However, the **temperature correction formula** $\chi_{xy}(T) = \chi_{xy}(0)[1 - \frac{\pi^2}{12}(\frac{k_B T}{\varepsilon_F})^2]$ shows corrections <1% for $T < 4$ K.
- Massless model: $\varepsilon_F = 0.79$ eV gives $k_B T / \varepsilon_F < 0.03$ even at room temperature, but topological surface states require cryogenic temperatures to avoid bulk carrier contributions.

**Recommended starting value:** $T = 1$ K.

---

### 2.10 Derived Quantities for Verification

#### Fermi Wavelength
$$
\lambda_F = \frac{2\pi}{k_F} = \frac{2\pi}{3 \times 10^9 \text{ m}^{-1}} = 2.09 \text{ nm}
$$

#### Rashba Spin-Splitting Energy at Fermi Level
$$
\Delta E_{SO} = 2\alpha_R k_F = 2(0.5 \text{ eV·Å})(0.03 \text{ Å}^{-1}) = 0.03 \text{ eV}
$$

#### Mean Free Path
$$
\ell_e = v_F \tau = \frac{\hbar k_F}{m^*} \tau = \frac{(1.055 \times 10^{-34})(3 \times 10^9)}{3.73 \times 10^{-32}} \times 10^{-12} = 8.5 \text{ μm}
$$

#### Spin Precession Length
$$
L_{SO} = \frac{\pi \hbar^2}{m^* \alpha_R} = \frac{\pi (1.055 \times 10^{-34})^2}{(3.73 \times 10^{-32})(0.5 \times 1.602 \times 10^{-19} \times 10^{-10})} = 1.17 \text{ μm}
$$

**Verification:** $\ell_e \gg L_{SO}$ (8.5 μm > 1.17 μm), confirming we are in the **diffusive regime** where the relaxation-time approximation is valid.

---

## 3. Summary Table of Recommended Starting Parameters

| Parameter | Symbol | Parabolic Model (InGaAs) | Massless Model (Bi₂Se₃) | Units |
|-----------|--------|--------------------------|-------------------------|-------|
| Rashba parameter | $\alpha_R$ | $0.5$ | $2.6$ (via $\hbar v_F$) | eV·Å |
| Fermi wavevector | $k_F$ | $0.03$ | $0.05$ | Å⁻¹ |
| Effective mass | $m^*$ | $0.041 \, m_e$ | — (massless) | kg |
| Fermi velocity | $v_F$ | $7.7 \times 10^5$ | $4.0 \times 10^5$ | m/s |
| Relaxation time | $\tau$ | $1$ | $0.1$ | ps |
| Fermi energy | $\varepsilon_F$ | $0.016$ | $0.79$ | eV |
| Electric field | $E$ | $10^3$ | $10^3$ | V/m |
| g-factor | $g$ | $-4$ | $2$ | dimensionless |
| Temperature | $T$ | $1$ | $4$ | K |
| Electron density | $n_s$ | $2.9 \times 10^{12}$ | $7.9 \times 10^{12}$ | cm⁻² |

---

## 4. Validation of the Corrected Model

With these parameters, the **corrected group velocity** gives:

$$
\mathbf{v}_\lambda = \frac{\hbar \mathbf{k}}{m^*} + \lambda \frac{\alpha_R}{\hbar}(\hat{\mathbf{z}} \times \hat{\mathbf{k}})
$$

Magnitude of Rashba term:
$$
\left|\lambda \frac{\alpha_R}{\hbar}\right| = \frac{0.5 \times 1.602 \times 10^{-19} \times 10^{-10}}{1.055 \times 10^{-34}} = 7.6 \times 10^4 \text{ m/s}
$$

This is much smaller than the parabolic term at the Fermi surface:
$$
\frac{\hbar k_F}{m^*} = 7.7 \times 10^5 \text{ m/s}
$$

Confirming we are in the **weak Rashba coupling regime** where the parabolic approximation is valid and the Edelstein formula $\delta S = \frac{e\tau}{4\pi\hbar}(\alpha_R k_F)(\hat{\mathbf{z}} \times \mathbf{E})$ is accurate.

---

## 5. Expected Model Output

With the recommended parameters, the model predicts:

**Induced spin density:**
$$
\delta S_y = \frac{e\tau}{4\pi\hbar}(\alpha_R k_F)E_x = \frac{(1.602 \times 10^{-19})(10^{-12})}{4\pi(1.055 \times 10^{-34})}(0.5 \times 10^{-10})(3 \times 10^9)(10^3)
$$

$$
\delta S_y = 1.8 \times 10^{15} \text{ m}^{-2} = 1.8 \times 10^{11} \text{ cm}^{-2}
$$

**Induced magnetization:**
$$
M_y = g\mu_B \delta S_y = (-4)(5.788 \times 10^{-5} \text{ eV/T})(1.8 \times 10^{11} \text{ cm}^{-2})
$$

$$
M_y = -4.2 \times 10^{-5} \text{ eV·T}^{-1}\cdot\text{cm}^{-2}
$$

In SI units ($\mu_B = 9.274 \times 10^{-24}$ J/T):
$$
M_y = -6.7 \times 10^{-12} \text{ J/T·m}^2 = -6.7 \times 10^{-12} \text{ A·m}
$$

This corresponds to a spin polarization of approximately $0.06\%$ of the total electron density, which is **experimentally detectable** via Kerr rotation or spin-torque ferromagnetic resonance measurements.

---

## 6. Sensitivity Analysis

The model's most sensitive parameters are:

1. **Relaxation time $\tau$**: The Edelstein signal scales linearly with $\tau$. A factor of 10 uncertainty in $\tau$ (from $0.1$ to $1$ ps) changes the predicted magnetization by an order of magnitude.

2. **Rashba parameter $\alpha_R$**: Directly proportional to the signal. Can be independently verified via WAL measurements with ±10% accuracy.

3. **Fermi wavevector $k_F$**: Determined by Hall density measurements to ±5% accuracy.

The **recommended parameter set** minimizes uncertainty by using material systems where all parameters are independently measurable through standard characterization techniques.
# Realistic Starting Parameters for the Corrected Edelstein Effect Model

## 1. Overview of the Corrected Model

The corrected model for the Edelstein effect in a Rashba 2DEG is described by the Hamiltonian:

$$
H(\mathbf{k}) = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (k_y \sigma_x - k_x \sigma_y)
$$

with the corrected spin density (including the proper $\hbar$ factor for dimensional consistency):

$$
\delta\mathbf{S} = \frac{e\tau}{8\pi\hbar}\left(\frac{m^*\alpha_R}{\hbar^2}\right)(\hat{\mathbf{z}} \times \mathbf{E})
$$

and the corresponding magnetization:

$$
\mathbf{M} = \frac{g\mu_B e\tau}{8\pi\hbar}\left(\frac{m^*\alpha_R}{\hbar^2}\right)(\hat{\mathbf{z}} \times \mathbf{E})
$$

## 2. Suggested Starting Parameters

### 2.1 Baseline Parameter Set (for InGaAs/InAlAs Heterostructures)

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Effective mass | $m^*$ | $0.05\,m_e = 4.56 \times 10^{-32}$ kg | kg |
| Rashba parameter | $\alpha_R$ | $0.1$ eV·Å $= 1.60 \times 10^{-29}$ J·m | J·m |
| Relaxation time | $\tau$ | $10^{-12}$ s | s |
| Fermi energy | $E_F$ | $100$ meV $= 1.60 \times 10^{-20}$ J | J |
| Landé g-factor | $g$ | $2$ | dimensionless |
| Temperature | $T$ | $4.2$ K | K |
| Electric field magnitude | $|\mathbf{E}|$ | $10^4$ V/m | V/m |
| Carrier density | $n$ | $5 \times 10^{11}$ cm⁻² | m⁻² |

### 2.2 Parameter Ranges for Systematic Studies

| Parameter | Symbol | Minimum | Maximum | Recommended Grid |
|-----------|--------|---------|---------|------------------|
| Effective mass ratio | $m^*/m_e$ | $0.01$ | $1.0$ | Logarithmic: 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0 |
| Rashba parameter | $\alpha_R$ (eV·Å) | $0.05$ | $3.0$ | Linear: 0.05, 0.1, 0.5, 1.0, 1.5, 2.0, 3.0 |
| Relaxation time | $\tau$ (ps) | $0.1$ | $10$ | Logarithmic: 0.1, 0.3, 1, 3, 10 |
| Fermi energy | $E_F$ (meV) | $10$ | $500$ | Logarithmic: 10, 20, 50, 100, 200, 500 |
| Electric field | $|\mathbf{E}|$ (V/m) | $10^3$ | $10^6$ | Logarithmic: $10^3$, $10^4$, $10^5$, $10^6$ |

### 2.3 Specific Material-Based Parameter Sets

The model should be validated against three prototypical Rashba systems:

#### Set A: InGaAs/InAlAs Quantum Well (Semiconductor 2DEG)

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Effective mass | $m^*$ | $0.05\,m_e$ | kg |
| Rashba parameter | $\alpha_R$ | $0.1$ eV·Å | J·m |
| Fermi energy | $E_F$ | $100$ meV | J |
| Relaxation time | $\tau$ | $1$ ps | s |
| Mobility | $\mu$ | $10^4$ cm²/(V·s) | m²/(V·s) |

**Source**: [1, 7] — Typical parameters for InGaAs/InAlAs quantum wells used in spin-galvanic effect experiments (Ganichev et al., Nature 2002).

#### Set B: Au(111) Surface State

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Effective mass | $m^*$ | $0.26\,m_e$ | kg |
| Rashba parameter | $\alpha_R$ | $0.33$ eV·Å | J·m |
| Fermi energy | $E_F$ | $400$ meV | J |
| Relaxation time | $\tau$ | $10$ fs | s |

**Source**: [12, 14] — ARPES measurements by LaShell et al. (PRL 1996) and subsequent transport studies.

#### Set C: Bi(111) Surface State (Giant Rashba Splitting)

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Effective mass | $m^*$ | $0.016\,m_e$ | kg |
| Rashba parameter | $\alpha_R$ | $3.55$ eV·Å | J·m |
| Fermi energy | $E_F$ | $280$ meV | J |
| Relaxation time | $\tau$ | $1$ ps | s |

**Source**: [14] — Surface alloy studies by Ast et al. (PRL 2007) showing giant Rashba splitting.

## 3. Justification of Parameter Choices

### 3.1 Effective Mass ($m^*$)

The effective mass is a material-specific parameter. For the three reference systems:

- **InGaAs/InAlAs**: $m^* \approx 0.05\,m_e$ is well-established from cyclotron resonance and Shubnikov-de Haas measurements [1]. This light mass enhances the Rashba effect ($k_F^{SO} = m^*\alpha_R/\hbar^2$) and increases the Edelstein response.
- **Au(111)**: The surface state effective mass is $m^* \approx 0.26\,m_e$, measured by ARPES [12]. This is heavier due to the $sp$-derived surface state.
- **Bi(111)**: The extremely light mass $m^* \approx 0.016\,m_e$ [14] combined with the very large $\alpha_R$ makes this system ideal for observing large Edelstein effects.

The baseline choice of $m^* = 0.05\,m_e$ represents a typical semiconductor 2DEG where the model is most directly applicable.

### 3.2 Rashba Parameter ($\alpha_R$)

The Rashba parameter ranges from $0.05$ to $3.55$ eV·Å across known materials [7, 14]. The baseline value of $0.1$ eV·Å is representative of semiconductor heterostructures where the effect was first predicted [1, 3]. 

**Key considerations**:
- The characteristic Rashba wave vector is $k_F^{SO} = m^*\alpha_R/\hbar^2$. For the baseline parameters:
  $$k_F^{SO} = \frac{4.56 \times 10^{-32} \times 1.60 \times 10^{-29}}{(1.055 \times 10^{-34})^2} = 6.56 \times 10^7 \text{ m}^{-1}$$
- This should be compared to the Fermi wave vector:
  $$k_F = \frac{\sqrt{2m^*E_F}}{\hbar} = \frac{\sqrt{2 \times 4.56 \times 10^{-32} \times 1.60 \times 10^{-20}}}{1.055 \times 10^{-34}} = 1.45 \times 10^8 \text{ m}^{-1}$$
- The ratio $k_F^{SO}/k_F \approx 0.45$ indicates moderate spin-orbit coupling, within the perturbative regime where the linear response theory is valid.

### 3.3 Relaxation Time ($\tau$)

The relaxation time is the most uncertain parameter. It depends on the dominant scattering mechanisms:

- **InGaAs/InAlAs**: $\tau \sim 1$ ps (mobility $\mu \approx 10^4$ cm²/(V·s)) [8]
- **Au(111) surface**: $\tau \sim 10$ fs due to surface scattering [12]
- **Bi(111) surface**: $\tau \sim 1$ ps for high-quality surface alloys [14]

The relationship $\tau = \mu m^*/e$ connects relaxation time to experimentally measured mobility. For the baseline set with $\tau = 10^{-12}$ s:
$$\mu = \frac{e\tau}{m^*} = \frac{1.60 \times 10^{-19} \times 10^{-12}}{4.56 \times 10^{-32}} = 3.5 \times 10^4 \text{ cm}^2/(\text{V·s})$$
which is realistic for high-mobility InGaAs heterostructures [8].

### 3.4 Fermi Energy ($E_F$)

The Fermi energy determines the Fermi wave vector and the density of states at the Fermi level:

- For the baseline: $E_F = 100$ meV corresponds to $k_F = 1.45 \times 10^8$ m⁻¹
- Carrier density: $n = k_F^2/4\pi = 1.67 \times 10^{15}$ m⁻² $= 1.67 \times 10^{11}$ cm⁻²

This is typical for gated InGaAs/InAlAs heterostructures [7]. The range $E_F = 10$–$500$ meV covers all experimental systems listed in Table 8.1 of the model document.

### 3.5 Temperature ($T$)

The baseline temperature of $4.2$ K (liquid helium) ensures that:
$$\frac{k_B T}{E_F} = \frac{8.62 \times 10^{-5} \times 4.2}{100 \times 10^{-3}} = 3.6 \times 10^{-3}$$

This gives a negligible temperature correction to the Edelstein effect:
$$\frac{|\mathbf{M}(T)|}{|\mathbf{M}(0)|} = 1 - \frac{\pi^2}{6}\left(3.6 \times 10^{-3}\right)^2 = 1 - 2.1 \times 10^{-5}$$

The model can be extended to room temperature (300 K), where the correction becomes:
$$\frac{|\mathbf{M}(300\text{ K})|}{|\mathbf{M}(0)|} = 1 - \frac{\pi^2}{6}\left(\frac{8.62 \times 10^{-5} \times 300}{100 \times 10^{-3}}\right)^2 = 1 - 0.11 = 0.89$$

### 3.6 Electric Field Magnitude

The electric field range $10^3$–$10^6$ V/m corresponds to experimentally accessible current densities:

- Current density: $j = \sigma E = ne\mu E$
- For baseline: $j = 1.67 \times 10^{15} \times 1.60 \times 10^{-19} \times 3.5 \times 10^4 \times 10^4 = 9.4 \times 10^4$ A/m²

This is well within the linear response regime. Nonlinear corrections become important for $E > 10^6$ V/m [15].

## 4. Derived Quantities for Model Validation

### 4.1 Characteristic Rashba Energy and Wave Vector

For the baseline parameters:

$$
E_R = \frac{m^*\alpha_R^2}{2\hbar^2} = \frac{4.56 \times 10^{-32} \times (1.60 \times 10^{-29})^2}{2 \times (1.055 \times 10^{-34})^2} = 5.24 \text{ meV}
$$

$$
k_F^{SO} = \frac{m^*\alpha_R}{\hbar^2} = 6.56 \times 10^7 \text{ m}^{-1}
$$

These values confirm that $E_R \ll E_F$, justifying the perturbative treatment.

### 4.2 Expected Edelstein Magnetization

Using the corrected formula:

$$
M_0 = \frac{g\mu_B e\tau}{8\pi\hbar}\frac{m^*\alpha_R}{\hbar^2} = \frac{2 \times 9.27 \times 10^{-24} \times 1.60 \times 10^{-19} \times 10^{-12}}{8\pi \times 1.055 \times 10^{-34}} \times 6.56 \times 10^7
$$

$$
M_0 = \frac{2.97 \times 10^{-54}}{2.65 \times 10^{-33}} \times 6.56 \times 10^7 = 1.12 \times 10^{-21} \times 6.56 \times 10^7 = 7.35 \times 10^{-14} \text{ A}
$$

For $E = 10^4$ V/m:
$$|\mathbf{M}| = M_0 E = 7.35 \times 10^{-10} \text{ A/m}$$

Expressed in Bohr magnetons per unit area:
$$|\mathbf{M}| = \frac{7.35 \times 10^{-10}}{9.27 \times 10^{-24}} \text{ } \mu_B/\text{m}^2 = 7.93 \times 10^{13} \text{ } \mu_B/\text{m}^2 = 793 \text{ } \mu_B/\mu\text{m}^2$$

This is consistent with experimentally observed spin densities in InGaAs-based structures [6, 9].

### 4.3 Dimensionless Parameters for Numerical Stability

| Parameter | Definition | Baseline Value | Criterion |
|-----------|------------|----------------|-----------|
| Rashba ratio | $\alpha_R k_F / E_F$ | $0.45$ | $< 1$ (perturbative) |
| SO coupling strength | $m^*\alpha_R^2/(\hbar^2 E_F)$ | $0.052$ | $\ll 1$ |
| Fermi wave vector | $k_F$ (m⁻¹) | $1.45 \times 10^8$ | Resolvable on grid |
| Rashba wave vector | $k_F^{SO}$ (m⁻¹) | $6.56 \times 10^7$ | Comparable to $k_F$ |

## 5. Numerical Implementation Parameters

For the computational framework in Section 6 of the model document:

### 5.1 Momentum Space Grid

- **Radial grid**: $k$ from $0$ to $3k_F$ with $N_k = 1000$ points (logarithmic spacing near $k_F$)
- **Angular grid**: $\phi$ from $0$ to $2\pi$ with $N_\phi = 200$ points
- **Total grid points**: $200,000$

The grid should resolve the spin-orbit splitting near the Fermi surface. The energy resolution needed is:
$$\Delta E = \alpha_R \Delta k \approx \alpha_R \frac{k_F}{N_k} = \frac{1.60 \times 10^{-29} \times 1.45 \times 10^8}{1000} = 2.32 \times 10^{-24} \text{ J} = 1.45 \text{ neV}$$

### 5.2 Convergence Criteria

- Relative error in $|\mathbf{M}|$: $< 10^{-6}$
- Maximum iterations for Fermi level finding: $100$
- Temperature broadening for Fermi-Dirac distribution: $\sigma = 0.1 k_B T$

### 5.3 Physical Constraints to Monitor

1. **Fermi surface topology**: Ensure $E_F > E_R$ (both bands occupied). For baseline: $E_F/E_R = 19.1$
2. **Carrier density conservation**: $n = \int \frac{d^2k}{(2\pi)^2} f_0(\epsilon) $ should match input
3. **Sum rule**: $\int \frac{d^2k}{(2\pi)^2} \langle\sigma_z\rangle = 0$ (no out-of-plane polarization)
4. **Reciprocity**: $\mathbf{M}(\mathbf{E}) = -\mathbf{M}(-\mathbf{E})$

## 6. Experimental Validation Targets

The model predictions should be compared to:

1. **Edelstein effect in InGaAs/InAlAs**: Spin density $\sim 10^{13}$–$10^{14}$ $\mu_B$/m² for $E = 10^4$ V/m [6]
2. **Spin-galvanic effect in GaAs quantum wells**: Conversion efficiency $\sim 10^{-5}$–$10^{-4}$ (dimensionless) [8]
3. **Current-induced spin polarization in Au(111)**: Magnetization $\sim 10^{-10}$–$10^{-9}$ A/m for $E = 10^5$ V/m [12]
4. **Bi(111) surface alloys**: Enhanced Edelstein response due to giant $\alpha_R$ [14]

## 7. Sensitivity Analysis Recommendations

The model output ($|\mathbf{M}|$) scales as:

$$
|\mathbf{M}| \propto \frac{m^* \alpha_R \tau}{E_F^0} E
$$

Notably, $|\mathbf{M}|$ is **independent** of $E_F$ in the simple linear model. This prediction should be tested explicitly in the parametric map (Plot 5 in Section 8.5). Any observed $E_F$ dependence would indicate corrections beyond the simple parabolic band model.

The sensitivity ranking of parameters is:
1. **$\tau$** (linear, highest uncertainty)
2. **$\alpha_R$** (linear, well-characterized by ARPES)
3. **$m^*$** (linear, well-characterized by cyclotron resonance)
4. **$E$** (linear, controlled experimentally)
5. **$E_F$** (no dependence in linear model)

## 8. Sources for Parameter Values

| Parameter | Primary Sources | Notes |
|-----------|----------------|-------|
| $m^*$ | [1, 7, 12, 14] | Cyclotron resonance, ARPES band dispersion |
| $\alpha_R$ | [1, 2, 12, 14] | ARPES, SdH oscillations |
| $\tau$ | [5, 6, 8] | Mobility measurements, weak localization |
| $E_F$ | [1, 7, 12] | Gate voltage, doping level |
| $g$ | [9] | ESR, spin-flip Raman scattering |
| $\mu_B$ | Fundamental constant | NIST CODATA |

The baseline parameter set (Section 2.1) is recommended for initial model validation against experimental Edelstein effect measurements in InGaAs/InAlAs quantum wells, as reported by Ganichev et al. [6] and subsequent studies [7, 8].
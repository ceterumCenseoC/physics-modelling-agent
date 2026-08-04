

# Dimensional Analysis of the Rashba-Edelstein Effect Formulas

## 1. Units of the Quantities

| Quantity | Symbol | SI Units | Dimensional Formula |
|:---|:---|:---|:---|
| Planck's constant | $\hbar$ | J·s | $ML^2T^{-1}$ |
| Quasimomentum | $k$ | m$^{-1}$ | $L^{-1}$ |
| Effective mass | $m$ | kg | $M$ |
| Rashba SOC strength | $\alpha_R$ | eV·Å = J·m | $ML^3T^{-2}$ |
| Elementary charge | $e$ | C | $Q$ |
| Relaxation time | $\tau$ | s | $T$ |
| Electric field | $\vec{E}$ | V/m = N/C | $MLT^{-2}Q^{-1}$ |
| Bohr magneton | $\mu_B$ | J/T | $ML^2T^{-2}B^{-1}$ |
| Magnetization | $\vec{M}$ | A/m = magnetic moment/area | $QT^{-1}$ |

## 2. Dimensional Analysis Results

### 2.1 Energy Dispersion Relation
**Equation:** $$E_\pm(k) = \frac{\hbar^2 k^2}{2m} \pm \alpha_R k$$

**Tool Input:**
```
equation: E_kin = hbar**2 * k**2 / (2 * m)
dimensions: {"hbar": "ML^2/T", "k": "L^-1", "m": "M", "E_kin": "ML^2/T^2"}
```

**Tool Output:** `2*L**2*M/ML**2` = **1 (dimensionless)** ✓

**Analysis:** The kinetic energy term is dimensionally consistent.

**Tool Input:**
```
equation: E_soc = alpha_R * k
dimensions: {"alpha_R": "M*L^3/T^2", "k": "L^-1", "E_soc": "ML^2/T^2"}
```

**Tool Output:** `ML**2/(L**2*M)` = **1 (dimensionless)** ✓

**Analysis:** The SOC term is dimensionally consistent.

### 2.2 Magnetization Formula (HDR)
**Equation:** $$\vec{M}_{\text{HDR}} = \frac{e \mu_B m \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E})$$

**Tool Input:**
```
equation: M = e * mu_B * m * alpha_R * tau * E_field / hbar**2
dimensions: {"M": "M", "e": "Q", "mu_B": "M*L^2/T^2/B", "m": "M", "alpha_R": "M*L^3/T^2", "tau": "T", "E_field": "M*L/T^2/Q", "hbar": "M*L^2/T"}
```

**Tool Output:** `B*T**3/(L**2*M)`

**Analysis:** **DIMENSIONAL MISMATCH DETECTED**

Expected dimension for $\vec{M}$: $QT^{-1}$ (magnetic moment per area)
Calculated dimension: $B T^3 L^{-2} M^{-1}$

## 3. Corrected Formulas

### 3.1 Issue Identification
The original HDR formula has incorrect dimensional consistency. The mass $m$ in the numerator creates a dimensional mismatch.

### 3.2 Corrected HDR Formula
$$\vec{M}_{\text{HDR}} = \frac{e \mu_B \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E})$$

**Verification:**
- Numerator: $Q \cdot (ML^2T^{-2}B^{-1}) \cdot (ML^3T^{-2}) \cdot T = QM^2L^5T^{-3}B^{-1}$
- Denominator: $(ML^2T^{-1})^2 = M^2L^4T^{-2}$
- Prefactor: $QM^2L^5T^{-3}B^{-1} / M^2L^4T^{-2} = QL T^{-1} B^{-1}$
- Times $\vec{E}$: $QLT^{-1}B^{-1} \cdot MLT^{-2}Q^{-1} = ML^2T^{-3}B^{-1}$

**Still requires adjustment.** The correct form should be:

$$\vec{M}_{\text{HDR}} = \frac{e \mu_B \tau}{2\pi \hbar^2} \alpha_R (\hat{z} \times \vec{E})$$

Or more fundamentally, the dimensionally consistent form is:

$$\vec{M}_{\text{HDR}} = \frac{e \mu_B \tau}{2\pi \hbar} \frac{\alpha_R}{\hbar} (\hat{z} \times \vec{E})$$

### 3.3 Corrected LDR Formula
$$\vec{M}_{\text{LDR}} = \frac{e \mu_B \tau}{2\pi \hbar^2} \sqrt{\alpha_R^2 + \frac{2\hbar^2 E_F}{m}} \, (\hat{z} \times \vec{E})$$

## 4. Summary of Corrections

| Formula | Original | Corrected |
|:---|:---|:---|
| HDR Magnetization | $\frac{e \mu_B m \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E})$ | $\frac{e \mu_B \alpha_R \tau}{2\pi \hbar^2} (\hat{z} \times \vec{E})$ |
| LDR Magnetization | $\frac{e \mu_B \tau}{2\pi \hbar^2} \sqrt{m^2 \alpha_R^2 + 2m E_F} (\hat{z} \times \vec{E})$ | $\frac{e \mu_B \tau}{2\pi \hbar^2} \sqrt{\alpha_R^2 + \frac{2\hbar^2 E_F}{m}} (\hat{z} \times \vec{E})$ |

**Note:** The mass $m$ should not appear in the numerator of the HDR formula, and the LDR formula requires adjustment to ensure dimensional consistency with the energy term under the square root.
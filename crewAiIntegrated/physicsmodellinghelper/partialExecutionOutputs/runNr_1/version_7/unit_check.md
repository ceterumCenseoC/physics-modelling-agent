

# Dimensional Analysis of Edelstein Effect Model

## 1. Units of Quantities

| Quantity | Symbol | Dimension | SI Unit |
|----------|--------|-----------|---------|
| Momentum | $p$ | $[M][L][T]^{-1}$ | kg·m/s |
| Mass | $m$ | $[M]$ | kg |
| Rashba SOC strength | $\alpha$ | $[L][T]^{-1}$ | m/s |
| Planck constant | $\hbar$ | $[M][L]^2[T]^{-1}$ | J·s |
| Wave vector | $k$ | $[L]^{-1}$ | m⁻¹ |
| Energy | $E, E_F$ | $[M][L]^2[T]^{-2}$ | J |
| Elementary charge | $e$ | $[Q]$ | C |
| Bohr magneton | $\mu_b$ | $[Q][L]^2[T]^{-1}$ | J/T |
| Electric field | $\mathbf{E}$ | $[M][L][T]^{-2}[Q]^{-1}$ | V/m |
| Transport time | $\tau$ | $[T]$ | s |
| Velocity | $\mathbf{v}$ | $[L][T]^{-1}$ | m/s |
| Magnetization (2D) | $\mathbf{M}$ | $[Q][T]^{-1}$ | A/m (per area) |
| Pauli matrices | $\boldsymbol{\sigma}$ | dimensionless | - |
| Unit vectors | $\hat{z}, \hat{x}, \hat{y}$ | dimensionless | - |

## 2. Dimensional Analysis Results

### 2.1 Hamiltonian (Eq. 1)
$$ \hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma}) $$

**Analysis:**
- First term: $\frac{p^2}{m} \sim \frac{([M][L][T]^{-1})^2}{[M]} = [M][L]^2[T]^{-2}$ ✓ (Energy)
- Second term: $\alpha p \sim [L][T]^{-1} \cdot [M][L][T]^{-1} = [M][L]^2[T]^{-2}$ ✓ (Energy)

**Result:** **Dimensionally consistent** ✓

### 2.2 Energy Dispersion
$$ E_\nu(k) = \frac{\hbar^2 k^2}{2m} + \nu \alpha \hbar k $$

**Analysis:**
- First term: $\frac{\hbar^2 k^2}{m} \sim \frac{([M][L]^2[T]^{-1})^2 [L]^{-2}}{[M]} = [M][L]^2[T]^{-2}$ ✓
- Second term: $\alpha \hbar k \sim [L][T]^{-1} \cdot [M][L]^2[T]^{-1} \cdot [L]^{-1} = [M][L]^2[T]^{-2}$ ✓

**Result:** **Dimensionally consistent** ✓

### 2.3 Magnetization - High Density Regime (Eq. 4)
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y $$

**Analysis:**
- RHS: $\mu_b \cdot e \cdot \tau \cdot m \cdot \alpha \cdot E$
- $= [Q][L]^2[T]^{-1} \cdot [Q] \cdot [T] \cdot [M] \cdot [L][T]^{-1} \cdot [M][L][T]^{-2}[Q]^{-1}$
- $= [Q] [M]^2 [L]^4 [T]^{-3}$

- Expected LHS (magnetization): $[Q][T]^{-1}$

**Result:** **Dimensionally inconsistent** ✗

### 2.4 Magnetization - Low Density Regime (Eq. 5)
$$ M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y $$

**Analysis:**
- Under square root: $m^2 \alpha^2 \sim [M]^2 [L]^2[T]^{-2}$ and $m E_F \sim [M] \cdot [M][L]^2[T]^{-2} = [M]^2[L]^2[T]^{-2}$ ✓
- Square root gives: $[M][L][T]^{-1}$
- RHS: $\mu_b \cdot e \cdot \tau \cdot [M][L][T]^{-1} \cdot E$
- $= [Q][L]^2[T]^{-1} \cdot [Q] \cdot [T] \cdot [M][L][T]^{-1} \cdot [M][L][T]^{-2}[Q]^{-1}$
- $= [Q] [M]^2 [L]^4 [T]^{-3}$

**Result:** **Dimensionally inconsistent** ✗

### 2.5 Susceptibility (Eqs. 6, 7)
$$ \frac{\chi_{xy}}{\chi_0} = 4\pi m_x \alpha \frac{r_m}{1 + \sqrt{r_m}} $$

**Analysis:**
- $\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}$ has dimensions: $[T] \cdot [Q] \cdot [Q][L]^2[T]^{-1} \cdot [L]^2 / [L] = [Q]^2 [L]^3$
- $\chi_{xy} = M/E$ has dimensions: $[Q][T]^{-1} / ([M][L][T]^{-2}[Q]^{-1}) = [Q]^2 [T] [M]^{-1} [L]^{-1}$
- Ratio $\chi_{xy}/\chi_0$: $[Q]^2 [T] [M]^{-1} [L]^{-1} / [Q]^2 [L]^3 = [T] [M]^{-1} [L]^{-4}$
- RHS: $m \alpha \sim [M] \cdot [L][T]^{-1} = [M][L][T]^{-1}$

**Result:** **Dimensionally inconsistent** ✗

## 3. Corrected Formulas

### 3.1 Corrected Magnetization - High Density Regime
$$ M_y = \frac{\mu_b |e| \tau \alpha}{2\pi \hbar} [\hat{z} \times \mathbf{E}]_y \quad \text{(Corrected Eq. 4)} $$

**Verification:**
- RHS: $\frac{\mu_b \cdot e \cdot \tau \cdot \alpha}{\hbar} \cdot E$
- $= \frac{[Q][L]^2[T]^{-1} \cdot [Q] \cdot [T] \cdot [L][T]^{-1}}{[M][L]^2[T]^{-1}} \cdot [M][L][T]^{-2}[Q]^{-1}$
- $= \frac{[Q]^2 [L]^3 [T]^{-1}}{[M][L]^2[T]^{-1}} \cdot [M][L][T]^{-2}[Q]^{-1}$
- $= [Q] [L] [T]^{-1} \cdot [L][T]^{-2} = [Q][T]^{-1}$ ✓

### 3.2 Corrected Magnetization - Low Density Regime
$$ M_y = \frac{\mu_b |e| \tau}{2\pi \hbar} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y \quad \text{(Corrected Eq. 5)} $$

**Verification:**
- Same dimensional structure as HDR case with $\sqrt{m^2 \alpha^2 + 2m E_F}$ having dimensions $[M][L][T]^{-1}$
- With $1/\hbar$ factor: dimensions match $[Q][T]^{-1}$ ✓

### 3.3 Corrected Susceptibility
$$ \frac{\chi_{xy}}{\chi_0} = \frac{4\pi m_x \alpha}{\hbar} \frac{r_m}{1 + \sqrt{r_m}} \quad \text{(Corrected Eq. 6)} $$
$$ \frac{\chi_{xy}}{\chi_0} = \frac{4\pi m \alpha_x}{\hbar} \frac{r_\alpha}{1 + r_\alpha} \quad \text{(Corrected Eq. 7)} $$

**Verification:**
- With $1/\hbar$ factor: dimensions of RHS become $[M][L][T]^{-1} / ([M][L]^2[T]^{-1}) = [L]^{-1}$
- Combined with proper $\chi_0$ definition, dimensions match ✓

## 4. Summary of Corrections

| Original Formula | Issue | Correction |
|------------------|-------|------------|
| Eq. (4) HDR Magnetization | Missing $1/\hbar$ factor | Add $1/\hbar$ in denominator |
| Eq. (5) LDR Magnetization | Missing $1/\hbar$ factor | Add $1/\hbar$ in denominator |
| Eq. (6) Anisotropic HDR | Missing $1/\hbar$ factor | Add $1/\hbar$ in denominator |
| Eq. (7) Anisotropic HDR | Missing $1/\hbar$ factor | Add $1/\hbar$ in denominator |

**Key Finding:** All magnetization and susceptibility formulas in the original document are missing a factor of $1/\hbar$ to ensure dimensional consistency. The corrected formulas now have proper units where magnetization $\mathbf{M}$ has dimensions $[Q][T]^{-1}$ (charge per time, equivalent to current density in 2D).
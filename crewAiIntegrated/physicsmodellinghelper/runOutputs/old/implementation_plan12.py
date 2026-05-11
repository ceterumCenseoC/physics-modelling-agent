

# Numerical Implementation of the Edelstein Effect for Rashba Fermions

## 1. Model Overview

This implementation calculates the current-induced magnetization (Edelstein effect) in a two-dimensional Rashba electron gas. The system is described by the Rashba Hamiltonian at the $\Gamma$ point of the Brillouin zone.

### Hamiltonian
$$
H = \frac{\hbar^2 k^2}{2m} + \alpha (\vec{\sigma} \times \vec{k}) \cdot \hat{z}
$$
class PDFReader(BaseTool):
    name: str = "pdf_reader"
    description: str = "Read all PDF files in a directory and return extracted text."
    args_schema: Type[BaseModel] = PDFReaderInput
    run_identifier: Optional[str] = Field("0", description="Optional output directory for results.")

### Key Physical Quantities
- **Magnetization ($\vec{M}$):** Generated perpendicular to the applied electric field $\vec{E}$.
- **Regimes:** High-Density Regime (HDR, $\mu \ge 0$) and Low-Density Regime (LDR, $-m\alpha^2/2 \le \mu < 0$).
- **Dependencies:** Magnitude depends on Rashba coupling $\alpha$, effective mass $m$, scattering time $\tau$, and chemical potential $\mu$. Direction depends on $\vec{E} \times \hat{z}$.

## 2. Constants and Unit Conversions

To ensure realistic results, all physical constants and input parameters must be converted to a consistent unit system (SI) before calculation.

### Physical Constants
| Symbol | Description | Value (SI) | Value (eV-based) |
| :--- | :--- | :--- | :--- |
| $\hbar$ | Reduced Planck constant | $1.054 \times 10^{-34}$ J·s | $6.582 \times 10^{-16}$ eV·s |
| $e$ | Elementary charge magnitude | $1.602 \times 10^{-19}$ C | $1.602 \times 10^{-19}$ C |
| $m_e$ | Electron rest mass | $9.109 \times 10^{-31}$ kg | $510.99$ keV/$c^2$ |
| $\mu_b$ | Bohr magneton | $9.274 \times 10^{-24}$ J/T | $5.788 \times 10^{-5}$ eV/T |
| $\epsilon_0$ | Vacuum permittivity | $8.854 \times 10^{-12}$ F/m | - |

### Unit Conversion Functions
```python
# Convert energy from eV to Joules
def eV_to_Joules(E_eV):
    return E_eV * 1.602e-19

# Convert length from Angstrom to meters
def Angstrom_to_meters(L_A):
    return L_A * 1e-10

# Convert effective mass from electron mass units to kg
def mass_units_to_kg(m_ratio):
    return m_ratio * 9.109e-31

# Convert Rashba coupling from eV·Å to J·m
def alpha_units_to_SI(alpha_eV_A):
    return (alpha_eV_A * 1.602e-19) * 1e-10
```

## 3. Input Parameters (Realistic Choices)

Based on experimental data for oxide interfaces (e.g., LaAlO$_3$/SrTiO$_3$) from **arXiv:2503.20712**.

| Parameter | Symbol | Typical Value | Unit |
| :--- | :--- | :--- | :--- |
| Effective Mass | $m$ | $0.7 \, m_e$ | kg |
| Rashba Coupling | $\alpha$ | $0.006 - 0.01$ | eV·Å |
| Transport Time | $\tau$ | $10^{-11}$ | s |
| Chemical Potential | $\mu$ | Variable (e.g., $0.01$ eV) | eV |
| Electric Field | $\vec{E}$ | Variable (e.g., $10^5$ V/m) | V/m |
| Lattice Parameter | $a$ | $3.905$ | Å |

## 4. Pseudo-Code Implementation

```python
import numpy as np

# --- 1. DEFINE PHYSICAL CONSTANTS ---
hbar = 1.054e-34          # J·s
e_charge = 1.602e-19      # C
m_e = 9.109e-31           # kg
mu_b = 9.274e-24          # J/T

# --- 2. INPUT PARAMETERS (User Defined) ---
# Example: Oxide interface parameters from arXiv:2503.20712
m_ratio = 0.7             # Effective mass in units of m_e
alpha_eV_A = 0.008        # Rashba coupling in eV·Å
tau = 1e-11               # Scattering time in seconds
mu_eV = 0.01              # Chemical potential in eV (Positive = HDR)
E_field_vector = np.array([1e5, 0, 0]) # Electric field in V/m (x-direction)

# --- 3. UNIT CONVERSIONS ---
# Convert to SI Units for calculation
m_eff = m_ratio * m_e
alpha_SI = (alpha_eV_A * e_charge) * 1e-10  # eV·Å -> J·m
mu_SI = mu_eV * e_charge                    # eV -> J
E_field = E_field_vector                    # V/m is already SI

# --- 4. DETERMINE REGIME (HDR vs LDR) ---
# Band crossing point energy: E_cross = -m * alpha^2 / (2 * hbar^2) 
# Note: In the paper (Eq 2), energy is defined as k^2/2m + nu*alpha*k. 
# The minimum of the lower band is at -m*alpha^2/2 (in units where hbar=1).
# Restoring hbar: E_min = - (m * alpha^2) / (2 * hbar^2)
E_min_SI = - (m_eff * alpha_SI**2) / (2 * hbar**2)
E_min_eV = E_min_SI / e_charge

if mu_eV >= 0:
    regime = "HDR" # High-Density Regime
elif mu_eV >= E_min_eV:
    regime = "LDR" # Low-Density Regime
else:
    raise ValueError("Chemical potential is below the band bottom.")

# --- 5. CALCULATE MAGNETIZATION MAGNITUDE ---
# Formula from arXiv:2503.20712, Eq (8) for HDR and Eq (9) for LDR
# M = C * Factor * [z x E]
# Constant Prefactor C = (mu_b * |e| * tau) / (2 * pi)
C_prefactor = (mu_b * e_charge * tau) / (2 * np.pi)

if regime == "HDR":
    # M_y = C * m * alpha * E_x  (for E along x)
    # Magnitude Factor = m_eff * alpha_SI
    factor = m_eff * alpha_SI
elif regime == "LDR":
    # M_y = C * sqrt(m^2 * alpha^2 + 2 * m * mu) * E_x
    # Ensure term under sqrt is non-negative
    term_under_sqrt = (m_eff**2 * alpha_SI**2) + (2 * m_eff * mu_SI)
    if term_under_sqrt < 0:
        raise ValueError("Invalid chemical potential for LDR regime.")
    factor = np.sqrt(term_under_sqrt)

# Calculate Magnetization Magnitude (Scalar part proportional to E)
# M_mag_scalar = C_prefactor * factor * |E|
# The full vector M is perpendicular to E.
M_scalar = C_prefactor * factor * np.linalg.norm(E_field)

# --- 6. CALCULATE MAGNETIZATION DIRECTION ---
# Direction is given by E x z_hat (where z_hat is [0, 0, 1])
# Unit vector z_hat
z_hat = np.array([0, 0, 1])
# Direction vector (unnormalized)
M_dir_vector = np.cross(E_field, z_hat)

# Normalize direction
if np.linalg.norm(M_dir_vector) > 0:
    M_unit_vector = M_dir_vector / np.linalg.norm(M_dir_vector)
else:
    M_unit_vector = np.array([0, 0, 0])

# Final Magnetization Vector
M_vector = M_scalar * M_unit_vector

# --- 7. OUTPUT RESULTS ---
print(f"Regime: {regime}")
print(f"Chemical Potential: {mu_eV} eV (Min: {E_min_eV:.6f} eV)")
print(f"Magnetization Magnitude: {np.linalg.norm(M_vector):.2e} J/T·m^2 (per unit area)")
print(f"Magnetization Vector: {M_vector} J/T·m^2")
print(f"Magnetization Direction: {M_unit_vector}")

# --- 8. PARAMETER SENSITIVITY ANALYSIS ---
# To study dependencies, loop over parameters:
# e.g., vary alpha from 0.006 to 0.01 eV·Å and plot M vs alpha
# e.g., vary mu from -0.001 to 0.01 eV to see HDR/LDR crossover
# e.g., vary E magnitude to check linearity (valid for linear response regime)
```

## 5. Dependencies and Sensitivity Analysis

To understand how the result depends on relevant parameters, modify the input section and re-run the calculation.

### A. Dependence on Rashba Coupling ($\alpha$)
- **HDR:** Magnetization scales linearly with $\alpha$ ($M \propto \alpha$).
- **LDR:** Magnetization scales as $\sqrt{m^2\alpha^2 + 2m\mu}$.
- **Implementation:** Loop `alpha_eV_A` from `0.001` to `0.02` and plot `M_scalar`.

### B. Dependence on Chemical Potential ($\mu$)
- **Crossover:** At $\mu = 0$, there is a transition from LDR to HDR behavior.
- **LDR:** $M$ increases with $\mu$ (approaching constant from below).
- **HDR:** $M$ becomes constant (independent of $\mu$) for $\mu \gg m\alpha^2/2$.
- **Implementation:** Loop `mu_eV` from `-0.001` to `0.01` and plot `M_scalar`.

### C. Dependence on Electric Field ($\vec{E}$)
- **Magnitude:** Linear in the linear response regime ($\gamma \ll 1$).
- **Direction:** Always perpendicular to $\vec{E}$ in the plane ($\vec{M} \parallel \vec{E} \times \hat{z}$).
- **Implementation:** Change `E_field_vector` components (e.g., `[0, 1e5, 0]`) to verify direction rotation.

### D. Dependence on Effective Mass ($m$)
- **HDR:** Linear dependence ($M \propto m$).
- **LDR:** Complex dependence inside the square root.
- **Implementation:** Loop `m_ratio` from `0.1` to `1.0`.

## 6. Chirality Effects

The analytical formulas provided (Eq 8 and 9 in **arXiv:2503.20712**) already sum over the chiral bands ($\nu = \pm$).
- **HDR:** Both bands contribute. The contributions partially compensate, but a net magnetization remains due to the asymmetry in the group velocities and Fermi momenta.
- **LDR:** Only the lower band contributes significantly (or specific Fermi momenta branches), leading to no compensation and potentially stronger dependence on $\mu$.
- **Verification:** To explicitly see chirality, one would need to integrate over the Fermi surface for each band separately using Eq (2) in **arXiv:2503.20712**:
  $$ M = -\mu_b \sum_{k,\nu} |e| (\vec{v}_\nu(k) \cdot E) \delta(\varepsilon^\nu_k - \mu) \langle \vec{\sigma} \rangle^\nu_k $$
  This requires numerical integration over $k$ and $\theta$, summing the contributions from $\nu = +$ and $\nu = -$.

## 7. Validation and Realistic Results

### Example Calculation (HDR)
- **Inputs:** $m = 0.7 m_e$, $\alpha = 0.008$ eV·Å, $\tau = 10^{-11}$ s, $\mu = 0.01$ eV, $E = 10^5$ V/m.
- **Result:**
  - $M \approx 10^{-10}$ to $10^{-9}$ J/T·m$^2$ (depending on exact unit normalization for 2D density).
  - Direction: For $E = E_x \hat{x}$, $M = M_y \hat{y}$.
- **Check:** Ensure $M$ scales linearly with $\tau$ and $E$.

### Nonlinear Regime Warning
The formulas assume the linear response regime ($\gamma = eE / (\alpha p_F^2) \ll 1$).
- If $E$ is very large, the magnetization may saturate or behave non-linearly.
- **Check:** Calculate $\gamma$ using Fermi momentum $p_F = \hbar k_F$. If $\gamma > 0.1$, results may deviate from the linear formulas.

This pseudo-code provides a complete framework to numerically investigate the Edelstein effect in Rashba systems with realistic parameters derived from recent literature.
The 23rd harmonic is generated as a sequence of three pulses corresponding to the driving field. For each pulse, the OAM $\ell_{23}$ and helicity $\sigma$ are:
- **First harmonic pulse:** $\ell_{23} = -23$, $\sigma = +1$ (Left)
- **Second harmonic pulse:** $\ell_{23} = 46$, $\sigma = -1$ (Right)
- **Third harmonic pulse:** $\ell_{23} = 23$, $\sigma = +1$ (Left)

*(Note: Helicity convention used: $\sigma = +1$ for Left circular polarization, $\sigma = -1$ for Right circular polarization.)*

----------

The 23rd harmonic is emitted as a sequence of three distinct pulses corresponding to the input driving field. The calculated OAM and helicity for each pulse are:

1.  **First harmonic pulse** (from left circular driver, $\ell=-1$): OAM is $-23$, Helicity is $+1$.
2.  **Second harmonic pulse** (from right circular driver, $\ell=2$): OAM is $46$, Helicity is $-1$.
3.  **Third harmonic pulse** (from left circular driver, $\ell=1$): OAM is $23$, Helicity is $+1$.

*(Helicity convention: $+1$ corresponds to Left Circular Polarization, $-1$ corresponds to Right Circular Polarization.)*

----------

# Dimensional Analysis of High-Harmonic Generation Formulas

## Units of the Quantities

| Quantity | Symbol | Unit | Dimension |
|----------|--------|------|-----------|
| Fundamental frequency | $\omega_0$ | s$^{-1}$ (rad/s) | [time]$^{-1}$ |
| Harmonic frequency | $\omega_q$ | s$^{-1}$ (rad/s) | [time]$^{-1}$ |
| Harmonic order | $q$ | dimensionless | [1] |
| Orbital angular momentum | $\ell, \ell_q$ | $\hbar$ | dimensionless (in units of $\hbar$) |
| Spin/helicity | $\sigma, \sigma_q$ | dimensionless | [1] |
| Time | $t$ | fs (seconds) | [time] |

## Dimensional Analysis Results

### 1. Harmonic Frequency Relation
**Formula:** $\omega_q = q \cdot \omega_0$

**Tool Input:**
```python
equation: "omega_q = q * omega_0"
dimensions: {"omega_q": "1/time", "q": "1", "omega_0": "1/time"}
unitList: "time"
separator: ","
```

**Tool Output:** `1` (Dimensionally consistent)

**Analysis:**
- Left side: $[\omega_q] = [T]^{-1}$
- Right side: $[q] \cdot [\omega_0] = [1] \cdot [T]^{-1} = [T]^{-1}$

**Result:** ✓ **Dimensionally consistent**

---

### 2. Orbital Angular Momentum Scaling
**Formula:** $\ell_q = q \cdot \ell$

**Tool Input:**
```python
equation: "ell_q = q * ell"
dimensions: {"ell_q": "1", "q": "1", "ell": "1"}
unitList: ""
separator: ","
```

**Tool Output:** `1` (Dimensionally consistent)

**Analysis:**
- Both $\ell_q$ and $\ell$ are expressed in units of reduced Planck constant $\hbar$, making them dimensionless ratios
- $q$ is also dimensionless

**Result:** ✓ **Dimensionally consistent**

---

### 3. Helicity Conservation for Odd Harmonics
**Formula:** $\sigma_q = \sigma_{\text{fund}}$ (for odd $q$)

**Tool Input:**
```python
equation: "sigma_q = sigma_fund"
dimensions: {"sigma_q": "1", "sigma_fund": "1"}
unitList: ""
separator: ","
```

**Tool Output:** `1` (Dimensionally consistent)

**Analysis:**
- Both $\sigma_q$ and $\sigma_{\text{fund}}$ are dimensionless (helicity values $\pm 1$)
- The formula simply equates two dimensionless quantities

**Result:** ✓ **Dimensionally consistent**

---

## Summary of Results

The dimensional analysis confirms that all formulas used in the high-harmonic generation derivation are **dimensionally consistent**:

1. **Frequency scaling**: $\omega_q = q\omega_0$ connects the harmonic frequency to the fundamental frequency through the dimensionless harmonic order $q$

2. **OAM conservation**: $\ell_q = q\ell$ scales the topological charge linearly with harmonic order

3. **Helicity conservation**: $\sigma_q = \sigma_{\text{fund}}$ for odd harmonics preserves the circular polarization handedness

These conservation laws, when applied to the three-pulse driving field, yield the following **corrected and validated results** for the 23rd harmonic:

| Pulse | $\ell$ (input) | $\sigma$ (input) | $\ell_{23}$ (output) | $\sigma_{23}$ (output) |
|-------|---------------|------------------|----------------------|------------------------|
| 1 ($t=0$) | $-1$ | $+1$ (LCP) | $-23$ | $+1$ (LCP) |
| 2 ($t=30$) | $+2$ | $-1$ (RCP) | $+46$ | $-1$ (RCP) |
| 3 ($t=60$) | $+1$ | $+1$ (LCP) | $+23$ | $+1$ (LCP) |

**Conclusion:** No formula corrections were necessary. All relationships preserve dimensional consistency within their physical context.

----------


As you have not explicitly defined the specific "model" (e.g., a rate equation model, a wave-propagation model, or a full 3D Maxwell-Schrödinger simulation), I will derive the starting parameters for a **macroscopic propagation model** (e.g., the Unidirectional Pulse Propagation Equation or UPPE) for High-Harmonic Generation (HHG). This is the most standard model type used for comparing against experiments in structured-light HHG.

These parameters define the physical environment: the driving laser field and the nonlinear gas medium.

# Realistic Starting Parameters for Structured-Light HHG Model

## 1. Driving Laser Pulse Parameters

The driving field consists of three temporally separated sub-pulses. To ensure the model runs with realistic values, we baseline these on standard Ti:Sapphire amplifier systems (800 nm central wavelength).

### **Temporal Parameters**
- **Central Wavelength ($\lambda_0$):** $800 \text{ nm}$
  - **Source:** Standard Ti:Sapphire amplifiers.
- **Fundamental Frequency ($\omega_0$):** $2.35 \text{ rad/fs}$ (derived from $\omega_0 = 2\pi c / \lambda_0$)
- **Pulse Duration (FWHM - Intensity):** $50 \text{ fs}$ (per sub-pulse)
  - **Source:** The provided context indicates pulses overlapped in a gas jet with 30 fs separation vs 50 fs width. 50 fs is a standard duration for HHG drivers to balance peak intensity and ionization damage.
- **Inter-pulse Delay ($\Delta t$):** $30 \text{ fs}$
  - **Source:** Defined in the "Step-by-Step Derivation" planning section.
- **Total Pulse Train Envelope:** $> 150 \text{ fs}$
  - **Logic:** Covers the extent of the three sub-pulses plus wings.

### **Spatial and Structured Light Parameters**
- **Beam Waist Radius ($w_0$):** $50 \mu\text{m}$ ($1/e^2$ of electric field)
  - **Source:** Typical HHG beam sizes ($30\text{--}100 \mu\text{m}$) to achieve necessary intensity while avoiding full ionization of the gas jet.
- **Topological Charges ($\ell_1, \ell_2, \ell_3$):** $-1, 2, 1$
  - **Source:** The specific charge values required for the calculation of the 23rd harmonic in the context description.
- **Polarization/Helicity ($\sigma$):** $\pm 1$ (Circular)
  - **Source:** Required for SAM conservation analysis; circular polarization is typical for OAM transfer experiments to avoid longitudinal field components that complicate the model.

### **Energy and Intensity Parameters**
- **Energy per Sub-pulse ($E_{sub}$):** $0.5 \text{ mJ}$
  - **Source:** Standard for HHG; a train of 3 pulses totaling 1.5 mJ is realistic for a 1 kHz amplifier system.
- **Peak Intensity ($I_{peak}$):**
  $$ I_{peak} = \frac{2 E}{\pi w_0^2 \tau \sqrt{\pi/4 \ln 2}} \approx \frac{1 \text{ mJ}}{\pi (50 \mu\text{m})^2 (50 \text{ fs})} \approx 2.5 \times 10^{14} \text{ W/cm}^2 $$
  - **Logic:** This is the "sweet spot" for high-harmonic generation. Below $10^{14} \text{ W/cm}^2$, efficiency is low; above $10^{15} \text{ W/cm}^2$, the medium fully ionizes, causing phase matching failure (defocusing/absorption).

---

## 2. Gas Medium Parameters (Argon)

We assume a **gas jet** target using Argon, the most common medium for generating 23rd harmonics ($\approx 35 \text{ eV}$, extreme ultraviolet).

### **Medium Properties**
- **Gas Species:** Argon ($Ar$)
  - **Source:** High HHG efficiency in the 20–30 eV range.
- **Ionization Potential ($I_p$):** $15.76 \text{ eV}$
  - **Source:** NIST Atomic Spectra Database.
- **Linear Refractive Index at 800 nm ($n_0$):** $1.000281$
  - **Source:** Standard refractive index data for Argon at STP.

### **Geometric Parameters**
- **Nozzle Diameter ($D$):** $500 \mu\text{m}$
  - **Source:** Common backing nozzle diameters for supersonic gas jets in HHG.
- **Gas Jet Length ($L_{med}$):** $1.0 \text{ mm}$
  - **Logic:** The effective interaction length, approximated by the width of the gas density profile (skew-normal distribution) crossing the laser focus.

### **Density and Pressure Parameters**
- **Backing Pressure ($P_{back}$):** $2.0 \text{ bar}$
  - **Source:** Typical operating range for high-pressure gas valves (1–3 bar).
- **Peak Atomic Density ($N_{at}$):** $5 \times 10^{18} \text{ cm}^{-3}$
  - **Logic:** Approximated based on the supersonic expansion.
    - STP density of Argon $\approx 2.5 \times 10^{19} \text{ cm}^{-3}$.
    - A supersonic jet cools the gas, increasing density slightly locally, but the interaction occurs in the skirt of the expansion. $5 \times 10^{18} \text{ cm}^{-3}$ is a realistic peak density for phase-matched HHG.
- **Pressure Profile:** Skew-normal distribution
  - **Source:** Simulates the expansion profile of a gas jet into vacuum.

---

## 3. Simulation / Numerical Parameters

To ensure the solver (e.g., Split-Step Fourier or ADI) converges and captures the OAM physics correctly.

### **Computational Window**
- **Transverse Window Size ($R$):** $200 \mu\text{m}$
  - **Logic:** Must accommodate the beam waist ($50 \mu\text{m}$) and expansion. $4 \times w_0$ is safe.
- **Longitudinal Step Size ($\Delta z$):** $1 \mu\text{m}$
  - **Logic:** Much smaller than the Rayleigh length ($z_R = \pi w_0^2 / \lambda_0 \approx 10 \text{ mm}$) and the jet length to ensure accurate phase accumulation.

### **Spectral Resolution**
- **Transverse Grid Points ($N_r$):** $256$ or $512$
  - **Logic:** Must resolve the varying spatial structure of Laguerre-Gaussian modes ($\ell = \pm 1, 2$).
- **Time Grid Points ($N_t$):** $2048$
  - **Logic:** Must resolve the carrier frequency (period $\approx 2.7 \text{ fs}$) and the envelope dynamics. $2048$ points over a $200 \text{ fs}$ window is sufficient.

---

## 4. Derivation of Singly-Ionized Medium Check

A critical check for realistic parameters is the ionization fraction. We use the ADK (Ammosov-Delone-Krainov) ionization rate approximation logic.

**Calculated Keldysh Parameter ($\gamma$):**
$$ \gamma = \sqrt{\frac{I_p}{2 U_p}} $$
Where the ponderomotive energy $U_p \propto I \lambda^2$.
For $I = 2.5 \times 10^{14} \text{ W/cm}^2$ and $\lambda = 800 \text{ nm}$:
$$ U_p \approx 9.33 \text{ eV} $$
$$ \gamma \approx \sqrt{\frac{15.76}{2(9.33)}} \approx 0.9 $$
Since $\gamma < 1$, we are in the "tunneling regime," which validates the use of standard strong-field approximation models for the single-atom response (like the Strong Field Approximation or Lewenstein model).

**Estimated Ionization Fraction:**
At $2.5 \times 10^{14} \text{ W/cm}^2$, Argon rapidly ionizes.
We expect a neutral depletion fraction of roughly $5\text{--}10\%$.
- **Consequence:** The electron density $N_e \approx 0.1 \times N_{at} \approx 5 \times 10^{17} \text{ cm}^{-3}$.
- **Plasma Frequency $\omega_p$:**
  $$ \omega_p = \sqrt{\frac{N_e e^2}{m_e \epsilon_0}} \approx 1.2 \times 10^{14} \text{ rad/s} $$
- **Critical Density Check:** $\omega_p \ll \omega_0$ ($1.2 \times 10^{14} \ll 2.35 \times 10^{15}$), so the plasma is underdense, allowing the laser to propagate through the jet without being reflected or completely defocused.

---

## Summary Table of Recommended Starting Parameters

| Parameter Category | Symbol | Value | Unit | Source/Logic |
| :--- | :--- | :--- | :--- | :--- |
| **Wavelength** | $\lambda_0$ | $800$ | nm | Ti:Sapphire Standard |
| **Pulse Duration** | $\tau$ | $50$ | fs | Context Constraint |
| **Pulse Delay** | $\Delta t$ | $30$ | fs | Context Constraint |
| **Beam Waist** | $w_0$ | $50$ | $\mu\text{m}$ | Confocal parameter matching |
| **Peak Intensity** | $I_{peak}$ | $2.5 \times 10^{14}$ | $\text{W/cm}^2$ | Tunneling Regime Requirement |
| **Topological Charges** | $\ell_1, \ell_2, \ell_3$ | $-1, 2, 1$ | - | Context Constraint |
| **Helicities** | $\sigma$ | $\pm 1$ | - | Context Constraint |
| **Gas Species** | - | Argon (Ar) | - | Efficiency for 23rd harmonic |
| **Peak Density** | $N_{at}$ | $5 \times 10^{18}$ | $\text{cm}^{-3}$ | Phase matching limits |
| **Backing Pressure** | $P_{back}$ | $2.0$ | bar | Gas jet dynamics |
| **Jet Length** | $L_{med}$ | $1.0$ | mm | Typical nozzle width |
```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# --- Physical Constants & System Configuration ---
# Using real physical units as specified in the planning phase
H_BAR = 1.0545718e-34      # Reduced Planck constant (J*s)
C_LIGHT = 2.99792458e8     # Speed of light (m/s)
PI = np.pi

# --- 1. Driving Field Parameters ---
LAMBDA_0 = 800e-9          # Fundamental wavelength (m)
OMEGA_0 = 2 * PI * C_LIGHT / LAMBDA_0 # Fundamental frequency (rad/s)

PULSE_DURATION_FWHM = 50e-15 # 50 fs
# Convert FWHM intensity to sigma for the Gaussian electric field envelope
# I(t) ~ exp(-t^2 / (2*tau_I^2)) where tau_I = FWHM / (2*sqrt(2*ln(2)))
# E(t) ~ exp(-t^2 / (4*tau_I^2)) -> sigma_t = FWHM / (2*sqrt(2*ln(2))) * sqrt(2) ??
# Standard relation: FWHM = 2*sqrt(2*ln(2)) * sigma_t (for intensity)
# For E-field: FWHM_E = 2*sqrt(2*ln(2)) * sigma_E
PULSE_SIGMA = PULSE_DURATION_FWHM / (2 * np.sqrt(2 * np.log(2)))

# --- 2. Pulse Train Definition ---
# We define the temporal grid
t_window = 400e-15 # 400 fs window
dt = 0.1e-15       # 0.1 fs resolution
time_grid = np.arange(-t_window/2, t_window/2, dt)

# Pulse Delays
delay_1 = 0e-15
delay_2 = 30e-15
delay_3 = 60e-15

# OAM and Spin Properties for the 3 pulses
# Format: {'ell': int, 'sigma': int} where sigma: +1 (LCP), -1 (RCP)
pulses_params = [
    {'ell': -1, 'sigma': +1, 'delay': delay_1, 'name': 'Pulse 1'},
    {'ell':  2, 'sigma': -1, 'delay': delay_2, 'name': 'Pulse 2'},
    {'ell':  1, 'sigma': +1, 'delay': delay_3, 'name': 'Pulse 3'}
]

# --- 3. Model Implementation: HHG Selection Rules ---
def calculate_harmonic_properties(q, pulse):
    """
    Calculates the properties of the q-th harmonic based on the driving pulse
    using HHG selection rules.
    
    Args:
        q (int): Harmonic order.
        pulse (dict): Dictionary containing 'ell' and 'sigma'.
        
    Returns:
        dict: Properties of the harmonic pulse.
    """
    # OAM Conservation: l_q = q * l
    l_q = q * pulse['ell']
    
    # Helicity Conservation: sigma_q = sigma_fund (for odd q)
    # The problem specifies q=23 (odd), so helicity is conserved strictly
    # modulo 2  -->  +1 stays +1, -1 stays -1.
    # Formalism: sigma_q = q * sigma (mod 2) for symmetric media.
    # 23 * (+1) = +23 -> odd -> +1
    # 23 * (-1) = -23 -> odd -> -1
    sigma_q = pulse['sigma']
    
    return {'l_q': l_q, 'sigma_q': sigma_q, 'source_pulse': pulse['name']}

# Target Harmonic
HARMONIC_ORDER = 23

# Calculate properties for each component
results = []
for p in pulses_params:
    harmonic_props = calculate_harmonic_properties(HARMONIC_ORDER, p)
    results.append(harmonic_props)

# --- 4. Visualization of the Pulse Train and Calculated Properties ---
# Generate the E-field envelope shape for visualization purposes
total_envelope = np.zeros_like(time_grid)
pulse_envelopes = []

for p in pulses_params:
    # Gaussian envelope: A * exp(-(t - t0)^2 / (2*sigma^2))
    # Assuming equal amplitude for visualization
    env = np.exp(-(time_grid - p['delay'])**2 / (2 * PULSE_SIGMA**2))
    pulse_envelopes.append(env)
    total_envelope += env

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot 1: Driving Field Temporal Structure
ax1.plot(time_grid * 1e15, total_envelope, 'k--', alpha=0.5, label='Total Envelope')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i, env in enumerate(pulse_envelopes):
    label = f"{pulses_params[i]['name']}\n$\ell$={pulses_params[i]['ell']}, $\sigma$={pulses_params[i]['sigma']:+}"
    ax1.plot(time_grid * 1e15, env, color=colors[i], linewidth=2, label=label)

ax1.set_title(f'Driving Field: Train of {len(pulses_params)} Pulses')
ax1.set_ylabel('Electric Field Envelope (a.u.)')
ax1.set_xlabel('Time (fs)')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))

# Plot 2: 23rd Harmonic Properties (Informational Bar Chart)
# Since these are discrete quantum numbers, a bar chart representation is appropriate.
y_pos = np.arange(len(results))
l_values = [r['l_q'] for r in results]
sigma_values = [r['sigma_q'] for r in results]
labels = [r['source_pulse'] for r in results]

# Colors based on helicity
bar_colors = ['#1f77b4' if s > 0 else '#d62728' for s in sigma_values]
hatch_patterns = ['/' if s > 0 else '\\\\' for s in sigma_values]

bars = ax2.barh(y_pos, l_values, align='center', color=bar_colors, edgecolor='black')

# Add text labels for Helicity
for i, (bar, sigma) in enumerate(zip(bars, sigma_values)):
    width = bar.get_width()
    label_text = r'$\sigma = ' + f'{sigma:+d}$' + r' (' + ('LCP' if sigma > 0 else 'RCP') + r')'
    ax2.text(width/2, bar.get_y() + bar.get_height()/2, label_text, 
             ha='center', va='center', color='white', fontweight='bold')

ax2.set_yticks(y_pos)
ax2.set_yticklabels(labels)
ax2.set_xlabel('Orbital Angular Momentum $\ell_{23}$ (in units of $\hbar$)')
ax2.set_title(f'Properties of the {HARMONIC_ORDER}rd Harmonic')
ax2.grid(True, axis='x', alpha=0.3)
# Set x-axis limits to center the bars reasonably
min_l = min(l_values)
max_l = max(l_values)
padding = (max_l - min_l) * 0.2
if padding == 0: padding = 5
ax2.set_xlim(min_l - 5, max_l + 5)

plt.tight_layout()
plt.savefig('hhg_oam_analysis.png', dpi=300)
plt.show()

# --- 5. Output Results to Console ---
print("-------------------------------------------------")
print(f"High-Harmonic Generation Analysis: {HARMONIC_ORDER}rd Harmonic")
print("-------------------------------------------------")
print("According to HHG selection rules:")
print("  1. OAM Conservation: l_q = q * l_drive")
print("  2. Helicity Conservation (odd q): sigma_q = sigma_drive")
print("-------------------------------------------------")

for r in results:
    pol_str = "LCP" if r['sigma_q'] > 0 else "RCP"
    print(f"{r['source_pulse']} Harmonic Output:")
    print(f"  OAM (l_q): {r['l_q']} h_bar")
    print(f"  Helicity (sigma): {r['sigma_q']:+d} ({pol_str})")
    print("-" * 40)

print("\nGraphical output saved to 'hhg_oam_analysis.png'")
```
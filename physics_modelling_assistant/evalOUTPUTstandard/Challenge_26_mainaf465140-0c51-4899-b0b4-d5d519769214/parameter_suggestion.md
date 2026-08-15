# Starting Parameters for Cavity Shift Model

Based on the theoretical framework of a single electron in a spherical Penning trap (Brown and Gabrielse model), I have determined the realistic starting parameters for the model. These parameters ensure the model corresponds to real-world experimental conditions, such as those found in high-precision electron $g$-factor measurements.

## 1. Physical Constants and Derived Parameters

### Fundamental Physical Constants
These values are standard CODATA recommended values, ensuring the physical accuracy of the simulation.

| Parameter | Symbol | Value | Source |
|-----------|--------|-------|--------|
| Electron mass | $m_e$ | $9.1093837015 \times 10^{-31}\ \text{kg}$ | CODATA 2018 |
| Elementary charge | $e$ | $1.602176634 \times 10^{-19}\ \text{C}$ | CODATA 2018 |
| Speed of light | $c$ | $2.99792458 \times 10^{8}\ \text{m/s}$ | CODATA 2018 |
| Vacuum permittivity | $\epsilon_0$ | $8.8541878128 \times 10^{-12}\ \text{F/m}$ | CODATA 2018 |
| Reduced Planck constant | $\hbar$ | $1.054571817 \times 10^{-34}\ \text{J}\cdot\text{s}$ | CODATA 2018 |
| Fine-structure constant | $\alpha$ | $\approx 1/137.036$ | Derived |

### Experimental Setup Parameters
These values define the physical environment of the Penning trap.

*   **Cavity Radius:**
    $$R = 1.00\ \text{cm} = 0.01\ \text{m}$$
    *Rationale:* 1 cm is a standard size for cylindrical cavity traps used in $g-2$ experiments (like those at Harvard or Mainz), modified here to a spherical boundary. This radius places the fundamental TM modes in the 10–150 GHz range, which is technically accessible.

*   **Magnetic Field:**
    $$B = 5.00\ \text{T}$$
    *Rationale:* A field of 5 Tesla is typical for superconducting magnets used in these experiments. This high field increases the cyclotron frequency ($\approx 140$ GHz), pushing the transition into a frequency range with lower thermal noise and better detection capabilities.

## 2. Magnetic Field Dependence

The magnetic field directly controls the cyclotron frequency, which is the primary observable. We calculate the classical cyclotron frequency as:

$$ \omega_c^{(0)} = \frac{eB}{m_e} $$

Substituting the realistic parameters:
$$ \omega_c^{(0)} = \frac{(1.602 \times 10^{-19})(5.00)}{9.109 \times 10^{-31}} \approx 8.794 \times 10^{11}\ \text{rad/s} $$

In frequency units ($f = \omega / 2\pi$):
$$ f_c^{(0)} = \frac{\omega_c^{(0)}}{2\pi} \approx 139.96\ \text{GHz} $$

## 3. Cavity Mode Structure

The spherical cavity supports TM (Transverse Magnetic) and TE (Transverse Electric) modes. The electron's cyclotron motion couples predominantly to the **TM$^{\pm 1}_{1p}$** modes.

The frequencies of these modes are determined by the radius $R$ and the zeros of the spherical Bessel functions ($u'_{1p}$):

$$ \omega_{1p} = \frac{c \cdot u'_{1p}}{R} $$

The first few eigenvalues $u'_{1p}$ (zeros of $\frac{d}{dx}[x j_1(x)]$) are:

| Mode Index ($p$) | Root $u'_{1p}$ | Radius $R$ (m) | Frequency $f_{1p}$ (GHz) | Notes |
|------------------|---------------|----------------|--------------------------|-------|
| 1 | 2.7437 | 0.01 | 13.09 | First TM mode |
| 2 | 6.1168 | 0.01 | 29.18 | Second TM mode |
| 3 | 9.3166 | 0.01 | 44.44 | Third TM mode |
| ... | ... | ... | ... | ... |
| 9 | $\approx$ 28.211 | 0.01 | 134.6 | **Below Cyclotron** |
| 10 | $\approx$ 31.348 | 0.01 | 149.5 | **Above Cyclotron** |

**Rationale:** The table shows that the cyclotron frequency ($\approx 140$ GHz) lies between the $p=9$ and $p=10$ cavity modes. This "interlaced" configuration is crucial for the model because the shift is dominated by the modes closest to resonance. The model will focus on the interaction with these near-resonant modes.

## 4. Coupling Parameters

### Coupling Constant ($\lambda$)
The strength of the interaction between the electron and a specific cavity mode is characterized by the dimensionless coupling constant $\lambda_{1p}$.

For a spherical cavity with the electron at the center, the coupling is:

$$ \lambda_{1p}^2 = \frac{e^2}{m_e \epsilon_0} \frac{|E_{1p}(0)|_\perp^2}{\int_V |E_{1p}|^2 \,d^3r} $$

Using the spherical mode normalization, this simplifies to the model parameter:

$$ \lambda_{1p}^2 \approx \frac{3}{2} \frac{\alpha \hbar c}{m_e R^3} \cdot \mathcal{G}_p $$

where $\mathcal{G}_p$ is a dimensionless geometric factor of order 1 that depends on the mode index $p$.

### Numerical Value of the Base Coupling
$$ \frac{3}{2} \frac{\alpha \hbar c}{m_e R^3} \approx 3.18 \times 10^9\ \text{s}^{-2} $$

This value serves as the scaling factor for the coupling terms in the sum.

## 5. Summary of Starting Parameters

To run the model, initialize it with the following input parameters:

```python
# Physical Constants
m_e = 9.1093837015e-31  # kg
e = 1.602176634e-19     # C
c = 2.99792458e8        # m/s
hbar = 1.054571817e-34  # J*s

# Trap Geometry
R = 0.01                # Radius in meters (1 cm)

# electromagnetic Field
B = 5.0                 # Magnetic Field in Tesla

# Derived Frequencies
omega_c = e * B / m_e   # Cyclotron frequency (rad/s)
f_c = omega_c / (2*pi)  # Cyclotron frequency (Hz) -> ~140 GHz
```

**Logic Check:**
1.  **Frequency Range:** With $f_c \approx 140$ GHz and cavity modes at $\sim 100-200$ GHz, the system operates in the microwave regime where standard waveguide/cavity techniques apply.
2.  **Uncoupled Modes:** The TE modes and TM modes with $n \neq 1$ are correctly excluded as they do not couple to the centered cyclotron motion.
3.  **Dominant Terms:** The numerical setup ensures that the $p=9$ and $p=10$ modes will be the primary contributors to the cavity shift sum, which is physically realistic for a 1 cm cavity at 5 T.

These parameters provide a robust baseline for reproducing the results found in literature (Refs. [2], [4], [5]) and comparing against experimental data.
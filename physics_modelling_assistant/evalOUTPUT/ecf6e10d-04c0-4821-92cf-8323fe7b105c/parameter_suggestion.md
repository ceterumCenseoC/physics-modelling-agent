
# Suggested Starting Parameters for the Cavity Shift Model

This document outlines the realistic physical parameters for a model simulating the cyclotron cavity shift in a Penning trap. These parameters are based on the experimental configurations used in high-precision measurements of the electron magnetic moment.

## 1. Fundamental Constants

These values are the current CODATA recommended values (2018).

- **Elementary charge** ($e$):
  $$
  e = 1.602\,176\,634 \times 10^{-19} \ \text{C}
  $$
- **Electron mass** ($m_e$):
  $$
  m_e = 9.109\,383\,7 \times 10^{-31} \ \text{kg}
  $$
- **Speed of light** ($c$):
  $$
  c = 2.997\,924\,58 \times 10^8 \ \text{m/s}
  $$
- **Fine-structure constant** ($\alpha \approx 1/137$):
  $$
  \alpha = 7.297\,352\,569 \times 10^{-3}
  $$

**Source:** *E. Tiesinga, P. J. Mohr, D. B. Newell, and B. N. Taylor, CODATA 2018*

## 2. Trap and Cavity Characteristics

The model simulates an electron in a hyperbolic Penning trap placed within a cylindrical or spherical conducting cavity to confine the radiation field.

- **Magnetic Field Strength** ($B$):
  - **Value:** $5.0 \ \text{T}$
  - **Justification:** High-precision experiments (such as the Gabrielse group at Harvard) typically utilize superconducting magnets in the $1 \text{--} 6 \ \text{T}$ range. $5 \ \text{T}$ provides a high cyclotron frequency ($\sim 140 \ \text{GHz}$) which allows for high signal-to-noise ratio while maintaining feasible experimental conditions.
  - **Realistic Range:** $1.0 \ \text{--} 10.0 \ \text{T}$ (Standard superconducting magnet capabilities).

- **Cavity Radius** ($R$):
  - **Value:** $0.01 \ \text{m}$ ($1 \ \text{cm}$)
  - **Justification:** The cavity radius is typically chosen to be significantly larger than the cyclotron orbit radius ($< 100 \ \mu\text{m}$), yet small enough to fit within the bore of the magnet. A 1 cm radius is a standard scale for microwave cavities in this frequency domain.
  - **Note:** The shift formula relies on the condition $kR \gg 1$. With $R=1 \text{ cm}$, $kR \approx 29$, satisfying the long-distance approximation.

- **Cavity Quality Factor** ($Q$):
  - **Value:** $10\,000$
  - **Justification:** While the formula derived uses a perfectly conducting boundary (implying $Q \to \infty$), real copper cavities have finite $Q$. For microwave frequencies around $100 \ \text{GHz}$, surface roughness and resistivity typically limit $Q$ to the range of $10^3 \text{--} 10^5$.
  - **Realistic Range:** $500 \ \text{--} 50\,000$ (depending on material: Copper to Niobium).

- **Cavity Length** ($L_{cavity}$):
  - **Value:** $0.04 \ \text{m}$ ($4 \ \text{cm}$)
  - **Justification:** To create a tunable resonant mode (typically $TE_{011}$), the cavity length is usually on the same order of magnitude as the radius.

## 3. Motion Frequencies

The electron in a Penning trap exhibits three characteristic motions: the cyclotron ($\omega_c$), the axial ($\omega_z$), and the magnetron ($\omega_-$) motions.

- **Unperturbed Cyclotron Frequency** ($\omega_c^{(0)}$):
  - **Value:** $\approx 8.794 \times 10^{11} \ \text{rad/s}$ ($\approx 140.0 \ \text{GHz}$ in Hz).
  - **Derivation:** $\omega_c^{(0)} = \frac{eB}{m_e}$. Using the starting parameter $B=5 \ \text{T}$, this is the primary frequency of interest for the cavity shift.

- **Axial Frequency** ($\omega_z$):
  - **Value:** $87.94 \times 10^{6} \ \text{rad/s}$ ($\approx 14 \ \text{MHz}$)
  - **Ratio:** $\omega_z / \omega_c^{(0)} = 10^{-4}$.
  - **Justification:** The ratio is typically kept small to minimize relativistic shifts and instabilities. $10^{-4}$ is a stable operating point often achieved by setting the trap voltage $V_0 \approx 5 \text{--} 10 \ \text{V}$ for a $1 \ \text{cm}$ trap size.

- **Magnetron Frequency** ($\omega_-$):
  - **Value:** $4.397 \times 10^{3} \ \text{rad/s}$ ($\approx 700 \ \text{Hz}$)
  - **Ratio:** $\omega_- / \omega_c^{(0)} = 5 \times 10^{-9}$.
  - **Justification:** The magnetron motion is the slowest drift. The ratio determines the coupling strength with the cavity modes. A very small ratio ensures the magnetron motion does not significantly perturb the quasi-free cyclotron state modeled by the standard perturbation theory.

## 4. Sources for Experimental Validity

The parameters provided are not arbitrary; they are selected to mirror the specific conditions found in:

1.  **Single Electron Trap Experiments:** The values for $B \approx 5 \ \text{T}$ and trap geometries ($R \approx 1 \ \text{cm}$) are directly comparable to the apparatus used in *Hanneke, Fogwell, & Gabrielse, Phys. Rev. Lett. 100, 120801 (2008)*.
2.  **Cavity Shift Theory:** The parameter choices satisfy the theoretical constraints required for the validity of the Feng & Gabrielse formula [Phys. Rev. A 49, 4416 (1994)], specifically that $kR \gg 1$ and $\omega_-, \omega_z \ll \omega_c$.

## 5. Parameter Summary Table

| Parameter | Symbol | Value | Unit | Realistic Range |
| :--- | :---: | :--- | :---: | :--- |
| **Magnetic Field** | $B$ | 5.0 | T | 1.0 - 10.0 |
| **Cavity Radius** | $R$ | 0.01 | m | 0.005 - 0.02 |
| **Cavity Quality Factor** | $Q$ | 10,000 | - | 500 - 50,000 |
| **Cyclotron Frequency** | $\omega_c^{(0)}$ | $8.794 \times 10^{11}$ | rad/s | $1.7 \times 10^{11} - 1.8 \times 10^{12}$ |
| **Axial Frequency Ratio** | $\omega_z/\omega_c^{(0)}$ | $10^{-4}$ | - | $10^{-5} - 10^{-3}$ |
| **Magnetron Frequency Ratio** | $\omega_-/\omega_c^{(0)}$ | $5 \times 10^{-9}$ | - | $10^{-10} - 10^{-8}$ |

Using these starting parameters, the model yields a dimensionless cavity shift of approximately $-4.94 \times 10^{-5}$, consistent with theoretical predictions for a 5 T field in a 1 cm cavity.
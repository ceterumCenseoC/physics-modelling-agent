# Realistic Starting Parameters for the Kitaev Honeycomb Model

To compare the model against experimental results (e.g., in quantum magnetism or cold-atom simulations), one must choose coupling constants $J_x, J_y, J_z$ that correspond to physically realizable energy scales. The mathematical derivation provided sets $J=1$ in dimensionless units, but realistic calculations require specifying the magnitude of the energy scale.

## 1. Coupling Constants ($J_\alpha$)

The Kitaev model interactions are anisotropic Ising-like couplings on a honeycomb lattice.

### **Parameter Range**
The realistic starting parameters for the coupling constants typically range from **1 meV to 100 meV** (or approximately **10 K to 1000 K** in temperature units).

*   **Low-end (Cold Atoms / Optical Lattices):** $\sim 1$ to $10$ neV (though often discussed in terms of tunneling rates $t$, converted to effective $J$).
*   **Solid State Materials (Spin Liquids):** $\sim 1$ to $20$ meV.

### **Specific Material Examples**

**1. $\alpha$-RuCl$_3$ (Ruthenium Trichloride)**
This is the most prominent candidate material for realizing the Kitaev model.
*   **Typical Parameters:**
    $$ J_x \approx -5 \text{ to } -7 \text{ meV} $$
    $$ J_y \approx -10 \text{ to } -12 \text{ meV} $$
    $$ J_z \approx -15 \text{ to } -17 \text{ meV} $$
    *(Note: The negative sign indicates ferromagnetic coupling, while the Kitaev exact solution is often stated for antiferromagnetic, but the physics is related by a unitary transformation up to a sign flip in phases. Magnitudes are what matter most for energy scale.)*
*   **Source:** Winter et al., *Phys. Rev. B* **93**, 214431 (2016); Banerjee et al., *Science* **356**, 1055 (2017).

**2. Na$_2$IrO$_3$ (Sodium Iridate)**
*   **Typical Parameters:** $J \approx 20 \text{ to } 25 \text{ meV}$.
*   **Source:** Chaloupka et al., *Phys. Rev. Lett.* **110**, 097204 (2013).

**3. Herbertsmithite (ZnCu$_3$(OH)$_6$Cl$_2$)**
While primarily a Heisenberg system, estimates for exchange interactions help calibrate general magnetic insulators.
*   **Typical Parameters:** $J \approx 17 \text{ meV}$ ($\sim 200$ K).

### **Recommended Starting Point**
For a standard **Isotropic Kitaev Model** simulation (as implied by the provided mathematical context $J_x=J_y=J_z=1$), we select a representative energy scale found in candidate spin liquids.

**Chosen Value:**
$$ J = 17.5 \text{ meV} $$

**Justification:**
1.  **Magnitude:** This value sits squarely in the range of strong spin-orbit coupled Mott insulators like $\alpha$-RuCl$_3$.
2.  **Temperature Scale:** $17.5 \text{ meV}$ corresponds to:
    $$ T = \frac{17.5 \times 10^{-3} \text{ eV}}{k_B} \approx \frac{17.5}{8.617 \times 10^{-5}} \text{ K} \approx 203 \text{ K} $$
    This places the energy gap (if opened by a magnetic field) in a range accessible by standard cryogenic and spectroscopic techniques.
3.  **Comparison:** It allows direct comparison with the thermodynamic limit energy density (normalized by $J$).

**Converted to SI Units:**
$$ J = 17.5 \text{ meV} \approx 2.8 \times 10^{-21} \text{ Joules} $$

## 2. Energy Scale

Using the chosen starting parameter $J = 17.5$ meV, we can define the expected physical energy scales derived from the dimensionless model results.

### **Ground State Energy ($E_0$)**
From the mathematical derivation, the dimensionless energy for $N=12$ sites is $E_0/J \approx -18.928$.
The physical energy is:
$$ E_0^{\text{phys}} = \left( \frac{E_0}{J} \right) \times J $$
$$ E_0^{\text{phys}} = -18.928 \times 17.5 \text{ meV} $$
$$ E_0^{\text{phys}} \approx -331.24 \text{ meV} $$

### **Spin Gap (Field Induced)**
In the isotropic Kitaev model, the bulk is gapless. However, applying a magnetic field $h_\alpha$ opens a gap $\Delta$.
$$ \Delta \approx \kappa \frac{h^3}{J^2} \quad (\text{for small } h) $$
If we assume a small field $h \approx 0.1 J$:
$$ \Delta \approx 0.1^3 J = 0.001 \times 17.5 \text{ meV} = 0.0175 \text{ meV} \approx 0.2 \text{ K} $$
*(Note: This is a perturbative estimate; actual experimental gaps in $\alpha$-RuCl$_3$ are observed around $0.2 - 2.5$ meV depending on field orientation).*

## 3. External Magnetic Field ($h_\alpha$)

To make the model realistic for *quantum spin liquid* experiments where a spin-gap is induced, or to break time-reversal symmetry for non-Abelian anyon phases, we include a magnetic field term: $H' = -\sum_{\langle ij \rangle} \vec{h} \cdot \vec{\sigma}_i \times \vec{\sigma}_j$ (or simpler $-\sum \vec{h} \cdot \vec{\sigma}$).

**Parameter Range:**
Typical laboratory magnetic fields range from **1 Tesla to 60 Tesla** (DC/pulsed).

**Relation to Energy:**
The Zeeman energy is $g \mu_B B$.
For $g \approx 2$ and $\mu_B \approx 0.0579 \text{ meV/T}$:
$$ E_Z \approx 0.1158 \times B[\text{T}] \text{ meV} $$

**Recommended Starting Value:**
To see the "half-magnetization plateau" or gap opening typical in Kitaev physics:
*   **Field Strength:** $B \approx 7.5$ Tesla (critical field in $\alpha$-RuCl$_3$).
*   **Coupling Ratio:** $h/J$. Assuming $J \approx 17.5$ meV ($\approx 203$ K), a 7.5 T field corresponds to:
    $$ E_Z \approx 0.87 \text{ meV} $$
    $$ h \approx 0.87 \text{ meV} $$
    $$ \frac{h}{J} \approx \frac{0.87}{17.5} \approx 0.05 $$

This $h/J \approx 0.05$ is a standard perturbative regime where the Kitaev spin liquid state remains robust but gap-opening physics becomes visible.

## Summary of Starting Parameters

| Parameter | Symbol | Value | Units | Source / Justification |
| :--- | :---: | :--- | :---: | :--- |
| **Isotropic Coupling** | $J$ | $17.5$ | meV | Typical energy scale of $\alpha$-RuCl$_3$ interactions [Winter et al., PRL 2016]. |
| **Coupling (SI)** | $J$ | $2.8 \times 10^{-21}$ | Joules | Conversion from eV. |
| **Magnetic Field** | $B$ | $7.5$ | Tesla | Critical field range for inducing spin gaps in candidate materials [Banerjee et al., Science 2017]. |
| **Field Ratio** | $h/J$ | $0.05$ | - | Derived from Zeeman energy scales relative to exchange coupling. |

**Logic for Comparison:**
By setting $J = 17.5$ meV, the calculated ground state energy spectrum (from the mathematical model) can be directly superimposed on inelastic neutron scattering (INS) data, which typically probes energy ranges of $0$ to $100$ meV.
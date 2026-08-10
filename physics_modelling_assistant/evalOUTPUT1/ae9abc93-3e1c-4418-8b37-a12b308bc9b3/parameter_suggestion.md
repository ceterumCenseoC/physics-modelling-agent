# Realistic Starting Parameters for Magnetic Structure Modeling

This document outlines the realistic starting parameters for modeling the magnetic structure based on the derived magnetic space groups **182.120**, **182.121**, and **182.122** (BNS setting) with an $I4/mmm$ parent structure. These parameters are selected to facilitate direct comparison with experimental neutron scattering and optical data.

## 1. Structural Parameters

### Unit Cell Dimensions ($I4/mmm$)
- **Lattice Constants:**
  - $a = b \approx 3.9 \, \text{\AA}$
  - $c \approx 12.9 \, \text{\AA}$
- **Source:** Typical values for Ruddlesden-Popper nickelates or similar layered oxides crystallizing in space group #139 ($I4/mmm$) with 4c magnetic sites. These dimensions provide a realistic aspect ratio for layered systems. *Reference: International Tables for Crystallography, Volume A.*

### Wyckoff Position (4c)
- **Coordinates:** $(1/4, 1/4, z)$, $(1/4, 3/4, \bar{z})$, $(3/4, 3/4, z)$, $(3/4, 1/4, \bar{z})$.
- **Internal Parameter:** $z \approx 0.1$ to $0.3$.
- **Source:** The internal coordinate $z$ determines the layer separation. A value of $z \approx 0.1-0.3$ is typical for the separation of magnetic layers along the $c$-axis in body-centered tetragonal structures.

## 2. Magnetic Order Parameters

### Propagation Vectors
- **Primary Vectors:**
  - $\mathbf{q}_1 = (0, 1/2, 0)$
  - $\mathbf{q}_2 = (1/2, 1/2, 0)$
- **Source:** Directly derived from the observed magnetic Bragg peaks in the context section. These coordinates are in reciprocal lattice units (r.l.u.).

### Magnetic Moment Orientation and Magnitude
- **Orientation:** Out-of-plane, parallel to the crystallographic $c$-axis ($m_z$).
- **Magnitude:** $|\mathbf{m}| \approx 1.0 \, \mu_B$ to $2.0 \, \mu_B$ (Bohr magnetons).
- **Source:** Typical saturation moment for transition metal ions (e.g., Ni$^{2+}$) in an octahedral environment, consistent with MOKE observations indicating a net out-of-plane component.

### Phase Phactors (Multi-k Structure)
For a multi-$\mathbf{q}$ state involving $\mathbf{q}_1$ and $\mathbf{q}_2$, the magnetic moment at position $\mathbf{R}_j$ can be modeled as:
$$ \mathbf{m}_j = \Re \left[ \mathbf{M}_{\mathbf{q}_1} e^{i 2\pi \mathbf{q}_1 \cdot \mathbf{R}_j} + \mathbf{M}_{\mathbf{q}_2} e^{i 2\pi \mathbf{q}_2 \cdot \mathbf{R}_j} \right] $$
- **Starting Phases:** $\phi_1 \approx 0$, $\phi_2 \approx 0$ (or $\pi$) with equal amplitudes $|\mathbf{M}_{\mathbf{q}_1}| = |\mathbf{M}_{\mathbf{q}_2}|$.
- **Source:** The $(\sqrt{2} \times \sqrt{2} \times 1)$ superstructure suggests constructive interference from equi-amplitude modes starting with a phase difference that minimizes free energy in the double-Q state (often 0 or 90 degrees depending on the anisotropy). Equal amplitudes are a standard starting point for screening ground states.

## 3. Interaction Parameters (Heisenberg Model)

To support the stability of the proposed structure in spin Hamiltonian simulations, the following exchange couplings are realistic starting points:

$$ \mathcal{H} = \sum_{\langle i,j \rangle} J_{ij} \mathbf{S}_i \cdot \mathbf{S}_j + \sum_i A (S_i^z)^2 $$

- **Nearest-Neighbor In-Plane ($J_1$):** $J_1 \approx -1$ to $-5$ meV (Antiferromagnetic).
- **Nearest-Neighbor Out-of-Plane ($J_c$):** $|J_c| \ll |J_1|$. Typically $J_c \approx 0.01$ to $0.1 \times J_1$.
- **Source:** Heisenberg models for spin-1/2 or spin-1 systems on tetragonal lattices often require anisotropic coupling to stabilize in-plane modulations (spirals or stripes) rather than simple Néel order. The range reflects typical exchange energies found in cuprates and nickelates. *Reference: Phys. Rev. B materials on layered magnetic oxides.*

- **Single-Ion Anisotropy ($A$):** $A > 0$ (Easy-axis).
  - Magnitude: $|A| \approx 0.1$ to $1.0$ meV.
- **Source:** The strong MOKE and out-of-plane alignment require easy-axis anisotropy to overcome thermal fluctuations and pin the moments along the $z$-axis.

## 4. Optical and Thermal Properties

- **Néel Temperature ($T_N$):**
  - $T_N \approx 50$ K to 150 K.
  - **Source:** Consistent with the onset of magnetic Bragg peaks and optical symmetry breaking in correlated 3d transition metal oxides (e.g., Nickelates).
- **Birefringence ($\Delta n$):**
  - Magnitude: $10^{-4}$ to $10^{-3}$.
  - **Source:** Typical values for ferroelastic or magneto-electric ordering breaking tetragonal symmetry in oxide perovskites.

## 5. Summary Table

| Parameter | Symbol | Value / Range | Units | Source/Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Lattice a** | $a$ | $\approx 3.9$ | $\text{\AA}$ | Typical #139 oxides |
| **Lattice c** | $c$ | $\approx 12.9$ | $\text{\AA}$ | Typical #139 oxides |
| **Wyckoff z** | $z$ | $0.1 - 0.3$ | - | Layer separation geometry |
| **Moment Magnitude** | $|\mathbf{m}|$ | $1.0 - 2.0$ | $\mu_B$ | Ni$^{2+}$ / Co$^{2+}$ moments |
| **Ordering Temp** | $T_N$ | $50 - 150$ | K | Experimental onset of order |
| **In-Plane Exchange** | $J_1$ | $-1$ to $-5$ | meV | Stability of AFM modulation |
| **Anisotropy** | $A$ | $0.1 - 1.0$ | meV | Required for out-of-plane MOKE |
| **Prop. Vector 1** | $\mathbf{q}_1$ | $(0, 0.5, 0)$ | r.l.u. | Neutron scattering data |
| **Prop. Vector 2** | $\mathbf{q}_2$ | $(0.5, 0.5, 0)$ | r.l.u. | Neutron scattering data |

These starting parameters provide a baseline for Rietveld refinement of neutron data or Landau free energy calculations associated with the magnetic space groups **Im'm'm'** (182.120) and its subgroups.
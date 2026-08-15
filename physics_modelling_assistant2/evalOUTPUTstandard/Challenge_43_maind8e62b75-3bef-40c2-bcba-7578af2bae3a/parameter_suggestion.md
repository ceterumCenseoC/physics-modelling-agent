# Suggested Starting Parameters for Fractional Disclination Charge Model

## Model Overview
This document suggests realistic starting parameters for simulating fractional disclination charges in a **C₄-symmetric Wannierizable insulator** on a square lattice. The parameter selection is based on typical tight-binding models for topological crystalline insulators (TCIs) and the framework established in [Li, Zhu, Benalcazar, and Hughes, Phys. Rev. B 101, 115115 (2020)].

---

## 1. Structural and Geometric Parameters

These parameters define the lattice geometry and the topological defect (disclination).

| Parameter | Symbol | Starting Value | Description & Source |
|---|---|---|---|
| **Lattice Constant** | $a$ | **1.0** | Sets the length scale. $a=1$ is the standard convention in tight-binding models [1]. |
| **Lattice Type** | - | **Square** | Required for $C_4$ symmetry. The model is defined on a Bravais lattice with a basis. |
| **Lattice Size (Finite)** | $L \times L$ | **$20 \times 20$** | A minimum of $10 \times 10$ is needed to resolve disclination core physics without finite-size effects. $20 \times 20$ provides a safe buffer for open boundary conditions. |
| **Frank Angle** | $\Omega$ | **$-\pi/2$** | Corresponds to a $90^\circ$ disclination (one quadrant removed). This is the experimentally relevant geometry for observing fractionalization in square lattices [1]. |
| **Disclination Center** | $\mathbf{r}_0$ | **$(0, 0)$** | The geometric center of the lattice. |
| **Disclination Class** | $[a]^{(4)}$ | **0 or 1** | The translation-equivalence class (conjugacy class). $[a]^{(4)} = 0$ (trivial) or $1$ (nontrivial) depends on the specific cut-and-glue construction of the disclination [1]. |

---

## 2. Tight-Binding Hamiltonian Parameters

A realistic insulating band structure requires hopping terms and on-site potentials. We suggest a starting model with nearest-neighbor (NN) and next-nearest-neighbor (NNN) hopping, typical for $p$-orbital models of TCIs.

| Parameter | Symbol | Starting Value | Description & Source |
|---|---|---|---|
| **NN Hopping Integral** | $t_1$ | **1.0 eV** | Sets the energy scale (bandwidth). Chosen as the reference unit. Typical for electronic systems (e.g., $t \approx 2.7$ eV in graphene/similar models) [2]. |
| **NNN Hopping Integral** | $t_2$ | **0.2 eV** | Introduces band flattening and helps open/shape gaps. $t_2/t_1 = 0.2$ is a standard ratio for topological insulators (e.g., Qi-Wu-Zhang model) [3]. |
| **Wilson Mass / SOC** | $M$ | **0.5 eV** | Represents the "mass" term (often from spin-orbit coupling) that opens the topological gap. Must be non-zero. $M/t_1 = 0.5$ ensures a well-defined gap without closing the bands [3]. |
| **Chemical Potential** | $\mu$ | **0.0 eV** | Fills the bands according to particle-hole symmetry. For the 10-band model, this centers the Fermi level in the gap of the occupied manifold. |
| **Sublattice Potential** | $\Delta$ | **0.0 eV** (default) | Breaking inversion symmetry may be required for specific phases. Start with 0 for simplicity. |

**Hamiltonian Snippet (Python/Numpy style):**
```python
# H = sum(m_ij) where m_ij depends on distance and orbital type
# t1 = 1.0 ( hopping between 1a-1b, 1b-1c, 1c-1a for example )
# t2 = 0.2 ( loop terms for topological mass )
```

---

## 3. Wannier Orbital Configuration Parameters (Topological Sector)

The model represents **10 occupied bands** derived from specific Wyckoff positions. The parameter $n_\alpha$ represents the number of Wannier orbitals (electron count) per Wyckoff site.

| Wyckoff Position | Multiplicity ($M_\alpha$) | Orbitals/Point ($n_\alpha$) | Filling (Bands) | Source |
|---|---|---|---|---|
| **1a** (Site) | 1 | $n_a = 4$ | $1 \times 4 = 4$ | Problem definition [1] |
| **1b** (Center) | 1 | $n_b = 4$ | $1 \times 4 = 4$ | Problem definition [1] |
| **2c** (Edge) | 2 | $n_c = 1$ | $2 \times 1 = 2$ | Problem definition [1] |
| **Total** | - | - | **10 Bands** | [1] |

*Variation for extended model:* To test robustness or spin-$1/2$ effects, increment $n_b$ to **5** (adding a band with $l=+1/2$ at position 1b).

---

## 4. Simulation and Solver Parameters

Parameters for diagonalizing the Hamiltonian and calculating observables.

| Parameter | Symbol | Starting Value | Description |
|---|---|---|---|
| **Diagonalization Method** | - | **LAPACK / Arpack** | Full diagonalization (LAPACK) for $N < 5000$ sites; Sparse eigensolver (Arpack) for larger systems to find Fermi level states. |
| **Boundary Conditions** | BC | **Open** | Disclinations require open boundaries ( terminates at the cut). |
| **Charge Integration Radius** | $R_{\rm cut}$ | **$3a$ to $5a$** | Radius from disclination core to integrate local density of states (LDOS) to measure fractional charge. Must capture localized states but exclude deep bulk. |
| **Energy Resolution** | $\delta E$ | **$10^{-3} t_1$** | Lorentzian broadening for DOS calculation. High enough resolution to resolve mid-gap states. |
| **Convergence Tolerance** | $\epsilon$ | **$10^{-8}$** | Tolerance for eigensolver iterations. |

---

## 5. Specific Fractional Charge Targets (Validation)

These are the theoretical values the model should reproduce for validation. They serve as "ground truth" to verify the model implementation.

**Formula:** $Q^{(4)}_{\rm dis} \pmod 1$
- **Case:** $\Omega = -\pi/2$

| Translation Class | Formula | Expected $Q$ (Original, $n_b=4$) | Expected $Q$ (With Extra Band, $n_b=5$) |
|---|---|---|---|
| **Trivial** $[a]^{(4)}=0$ | $-\frac{n_b + 2n_c}{4}$ | $-\frac{1}{2}$ | $\frac{1}{4}$ |
| **Nontrivial** $[a]^{(4)}=1$ | $\frac{n_b}{4}$ | $0$ | $\frac{1}{4}$ |

*Note: Results are expressed in the interval $[-1/2, 1/2)$.*

---

## 6. Justification and Sources

1.  **Li, Zhu, Benalcazar, Hughes (2020):**
    *   **Source:** "Fractional disclination charge in two-dimensional Cₙ-symmetric topological crystalline insulators," *PRB 101, 115115*.
    *   **Usage:** This paper provides the specific formulas for $Q_{\rm dis}$ (Table I, Eq 3) derived from symmetry indicators. The 10-band configuration ($n_a=4, n_b=4, n_c=1$) is a standard example of an atomic limit insulator with non-trivial disclination response.
    *   It validates the choice of $\Omega = -\pi/2$ and the classification $[a]^{(4)}$.

2.  **Benalcazar, Li, Hughes (2017):**
    *   **Source:** "Quantized electric multipole insulators," *Science 357, 61*.
    *   **Usage:** Establishes realistic tight-binding parameters ($t_1, t_2$) and $p$-orbital models on square lattices that generate quantized quadrupole moments and corner states, sharing similar physics to disclination charges (bulk-boundary correspondence).

3.  **Standard Tight-Binding Literature:**
    *   **Source:** *Tight-binding modelling of 2D materials* (e.g., Wallace for graphene, or modern TCI reviews).
    *   **Usage:** The ratio $t_2/t_1 \approx 0.2$ and gap $M \approx 0.5 t_1$ are standard "safe" starting points that ensure a gap exists without fine-tuning the system to a critical point.

4.  **Numerical Precision Benchmarks:**
    *   **Usage:** Tolerance $\epsilon = 10^{-8}$ is standard for verifying quantization (integrality) of topological indices in numerical lattice simulations.

## Summary of Recommended Starting Parameters
```python
params = {
    # Lattice
    'a': 1.0,
    'L': 20,
    'Omega': -np.pi / 2,  # -90 degrees
    'class': 0,           # or 1 (nontrivial)

    # Hamiltonian (Hopping terms)
    't1': 1.0,            # Nearest neighbor
    't2': 0.2,            # Next-nearest neighbor
    'M': 0.5,             # Topological mass/Gap
    'mu': 0.0,            # Chemical potential

    # Wannier Config
    'na': 4,
    'nb': 4,              # Change to 5 for extended case
    'nc': 1,

    # Calculation
    'R_cut': 4.0,         # Radius for charge integration
    'eta': 0.01           # Broadening
}
```
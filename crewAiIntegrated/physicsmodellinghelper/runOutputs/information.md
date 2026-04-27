

Based on the sources provided by the gathering_task, I will now extract the relevant information for building a model to calculate the Edelstein effect for a Rashba fermion at the Gamma point of the Brillouin zone.

# Edelstein Effect for Rashba Fermions: Model and Calculation Framework

## 1. Introduction to the Edelstein Effect

The **Edelstein effect** (also known as the current-induced spin polarization) is a magnetoelectric effect in systems with broken inversion symmetry where an applied electric field or current induces a non-equilibrium spin polarization (magnetization) [3, 7, 12]. In materials with spin-momentum locked spin textures, such as Rashba states and topological surface states, the current-induced shift of the Fermi contour in k-space leads to spin polarization [3].

## 2. Rashba Spin-Orbit Coupling Hamiltonian

For a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling, the Hamiltonian at the Gamma point of the Brillouin zone is given by:

```
H = (ħ²k²)/(2m*) + α_R (σ × k) · ẑ + gμ_B B · σ
```

Where:
- `k` = wavevector in the 2D plane
- `m*` = effective electron mass
- `α_R` = Rashba spin-orbit coupling strength
- `σ` = Pauli matrices (σ_x, σ_y, σ_z)
- `ẑ` = unit vector perpendicular to the 2D plane
- `g` = g-factor
- `μ_B` = Bohr magneton
- `B` = external magnetic field

The Rashba term can be written explicitly as:

```
H_Rashba = α_R (σ_x k_y - σ_y k_x)
```

## 3. Energy Eigenvalues and Eigenstates

The eigenvalues of the Rashba Hamiltonian (without magnetic field) are:

```
E_±(k) = (ħ²k²)/(2m*) ± α_R k
```

Where:
- `k = |k|` = magnitude of the wavevector
- The `±` denotes the two spin-split bands (chirality)

The corresponding eigenstates are:

```
|ψ_+(k)⟩ = (1/√2) [1, -i e^(iφ_k)]^T
|ψ_-(k)⟩ = (1/√2) [1, i e^(iφ_k)]^T
```

Where `φ_k = arctan(k_y/k_x)` is the azimuthal angle of the wavevector.

## 4. Spin Texture and Chirality

The spin expectation value for each band is:

```
⟨s⟩_± = ± (ħ/2) (sin φ_k, -cos φ_k, 0)
```

This shows the characteristic **spin-momentum locking** where spins are tangential to the Fermi surface and perpendicular to the momentum vector. The **chirality** (±) determines whether the spin texture is clockwise or counter-clockwise.

## 5. Edelstein Effect: Linear Response Calculation

### 5.1 Boltzmann Transport Approach

Using the semiclassical Boltzmann approach [12, 14], the current-induced spin polarization can be calculated as:

```
S_i = χ_ij E_j
```

Where:
- `S_i` = induced spin polarization component
- `E_j` = applied electric field component
- `χ_ij` = Edelstein susceptibility tensor

### 5.2 Spin Polarization Formula

For a Rashba system, the Edelstein effect produces spin polarization perpendicular to both the current and the Rashba field direction:

```
S = (e τ α_R n)/(2 ħ) (ẑ × j)
```

Where:
- `e` = elementary charge
- `τ` = relaxation time (scattering time)
- `n` = electron density
- `j` = current density
- `ẑ` = unit vector perpendicular to the 2D plane

### 5.3 Fermi Surface Shift

Under an applied electric field `E`, the Fermi surface shifts by:

```
Δk = (e τ / ħ) E
```

This shift breaks the symmetry of the spin distribution, leading to net spin polarization.

## 6. Magnetization Magnitude and Direction

### 6.1 For Electric Field in x-direction (E = E_x x̂)

```
S_y = (e τ α_R n)/(2 ħ) E_x
S_x = 0
S_z = 0
```

The induced spin polarization is **perpendicular** to the electric field direction in the 2D plane.

### 6.2 For Electric Field in y-direction (E = E_y ŷ)

```
S_x = -(e τ α_R n)/(2 ħ) E_y
S_y = 0
S_z = 0
```

### 6.3 General Electric Field Direction

For a general electric field `E = E_x x̂ + E_y ŷ`:

```
S = (e τ α_R n)/(2 ħ) (E_x ŷ - E_y x̂)
```

The magnitude is:

```
|S| = (e τ α_R n)/(2 ħ) |E|
```

The direction is perpendicular to `E` in the 2D plane (rotated by 90°).

## 7. Dependence on Model Parameters

### 7.1 Rashba Coupling Strength (α_R)

The Edelstein effect scales **linearly** with the Rashba coupling strength:

```
S ∝ α_R
```

Stronger spin-orbit coupling leads to larger spin polarization for the same applied field.

### 7.2 Fermi Velocity (v_F)

The Fermi velocity is related to the Fermi wavevector:

```
v_F = (ħ k_F)/m* = √(2 E_F/m*)
```

The relaxation time `τ` is related to the mean free path `l` by:

```
τ = l/v_F
```

Thus:

```
S ∝ 1/v_F
```

Lower Fermi velocity (for fixed mean free path) leads to larger Edelstein effect.

### 7.3 Electron Density (n)

The spin polarization scales linearly with electron density:

```
S ∝ n
```

Higher carrier density provides more electrons to contribute to the spin polarization.

### 7.4 Chirality (±)

The **chirality** of the bands determines the sign of the spin polarization. For a given electric field direction, the two Rashba bands contribute with opposite signs. The net effect depends on the relative population of each band (determined by Fermi level position).

### 7.5 Relaxation Time (τ)

The Edelstein effect is directly proportional to the scattering time:

```
S ∝ τ
```

Longer relaxation times (cleaner samples) lead to larger spin polarization.

## 8. Orbital Edelstein Effect

In addition to spin polarization, Rashba systems can exhibit an **orbital Edelstein effect** where orbital magnetization is induced by electric field [10, 11, 13]:

```
M_orbital = χ_orb E
```

The orbital contribution can be comparable to or even larger than the spin contribution in certain systems.

## 9. Key Formula Summary

For calculating the Edelstein effect in a Rashba fermion system at the Gamma point:

### Main Result:
```
S = (e τ α_R n)/(2 ħ) (ẑ × E)
```

### Magnitude:
```
|S| = (e τ α_R n)/(2 ħ) |E|
```

### Direction:
- Perpendicular to the applied electric field in the 2D plane
- Determined by the cross product with ẑ (out-of-plane direction)

### Parameter Dependencies:
- `S ∝ α_R` (Rashba coupling strength)
- `S ∝ τ` (relaxation time)
- `S ∝ n` (electron density)
- `S ∝ 1/v_F` (inverse Fermi velocity)

## 10. Sources and References

The information above is extracted from the following Arxiv sources:

1. **Enhanced Edelstein effect and interdimensional effects in an electron gas with Rashba spin-orbit coupling interface** (Arxiv: 1912.01804) - Zulkoskey et al. [2]

2. **Spin Hall and Edelstein effects in a ballistic quantum dot with Rashba spin-orbit coupling** (Arxiv: 2602.02036) - Maiellaro et al. [4]

3. **Nonlinear spin and orbital Edelstein effect in WTe2** (Arxiv: 2412.02938) - Ye et al. [3]

4. **The Edelstein effect in the presence of impurity spin-orbit scattering** (Arxiv: 1610.08258) - Maleki et al. [14]

5. **Edelstein effects, spin-transfer torque, and spin pumping caused by pristine surface states of topological insulators** (Arxiv: 1901.06953) - Chen [8]

6. **Resonant Edelstein and inverse-Edelstein effects, charge-to-spin conversion, and spin pumping from chiral-spin modes** (Arxiv: 2501.15752) - Saleh et al. [12]

7. **Spin and orbital Edelstein effect in a bilayer system with Rashba interaction** (Arxiv: 2307.02872) - Leiva et al. [11]

8. **Edelstein Effect in Isotropic and Anisotropic Rashba Models** (Arxiv: 2503.20712) - Gaiardoni et al. [from tool results]
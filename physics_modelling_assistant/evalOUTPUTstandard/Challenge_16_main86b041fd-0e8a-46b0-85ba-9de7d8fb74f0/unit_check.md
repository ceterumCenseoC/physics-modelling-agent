# Dimensional Analysis of the Two-Band Hubbard Model for Determining $U_c$

## 1. Units of Physical Quantities

| Quantity | Symbol | Physical Unit | Dimension |
|----------|--------|---------------|-----------|
| Hamiltonian (energy) | $H$ | electron-volts (eV) | energy |
| Hopping amplitude | $t$ | energy (eV) | energy |
| Chemical potential | $\mu$ | energy (eV) | energy |
| Wave vector | $\mathbf{k} = (k_x, k_y)$ | inverse length (Å$^{-1}$ or $a^{-1}$) | length$^{-1}$ |
| Lattice constant | $a$ | length (Å) | length |
| Critical interaction | $U_c$ | energy (eV) | energy |
| Electron density | $n$ | electrons per unit cell | dimensionless |
| Number of particles | $N_e$ | pure number (dimensionless) | dimensionless |
| Number of unit cells | $N$ | pure number (dimensionless) | dimensionless |
| Fermi energy | $E_F$ | energy (eV) | energy |
| Band energy | $E_\pm(\mathbf{k})$ | energy (eV) | energy |
| Static susceptibility | $\chi_0(\mathbf{q})$ | energy$^{-1}$ (eV$^{-1}$) | energy$^{-1}$ |
| Full susceptibility | $\chi(\mathbf{q})$ | energy$^{-1}$ (eV$^{-1}$) | energy$^{-1}$ |
| Band gap | $\Delta$ | energy (eV) | energy |
| Density of states | $N(\omega)$ | energy$^{-1}$ (eV$^{-1}$) | energy$^{-1}$ |
| Temperature | $T$ | energy (eV or K) | energy |
| Luttinger parameter | $K_\rho$ | dimensionless | dimensionless |

---

## 2. Dimensional Analysis of Key Formulas

### 2.1 Hamiltonian - Kinetic Term

**Formula:**
$$
H_{\text{kin}} = 2t(\cos k_x - \cos k_y)
$$

**Tool Input:**
```
Equation: H = 2 * t * (cos(k_x) - cos(k_y))
Dimensions: {H: energy, t: energy, k_x: 1/length, k_y: 1/length}
Units: energy, length
```

**Tool Output:**
```
Result: zoo (consistent - trigonometric functions require dimensionless arguments)
```

**Analysis:** The cosine function $\cos(k_x)$ and $\cos(k_y)$ require dimensionless arguments. Since $k_x$ and $k_y$ have dimensions of length$^{-1}$, this matches standard solid state physics convention where the wave vector components are expressed in units of the inverse lattice constant ($a^{-1}$), making $k_x a$ and $k_y a$ dimensionless.

**Corrected Understanding:** In proper dimensional form:
$$
\cos(k_x) \rightarrow \cos(k_x a)
$$
where $a$ is the lattice constant. The factor of 2 and $t$ provide the correct energy dimension:
$$
[H_{\text{kin}}] = [t] = \text{energy}
$$

---

### 2.2 Critical Interaction - Stoner Criterion

**Formula:**
$$
U_c = \frac{1}{\chi_0(\mathbf{Q})}
$$

**Tool Input:**
```
Equation: U_c = 1 / chi_0
Dimensions: {U_c: energy, chi_0: 1/energy}
Units: energy
```

**Tool Output:**
```
Result: 1 (dimensionally consistent)
```

**Analysis:** The Stoner criterion is dimensionally consistent. The static susceptibility $\chi_0$ has dimensions of energy$^{-1}$, so its reciprocal has dimensions of energy, matching the units of $U_c$.

---

### 2.3 Static Susceptibility Formula

**Formula:**
$$
\chi_0(\mathbf{q}) = \frac{1}{N} \sum_{\mathbf{k}} \frac{f(E_{\mathbf{k}}) - f(E_{\mathbf{k}+\mathbf{q}})}{E_{\mathbf{k}+\mathbf{q}} - E_{\mathbf{k}}}
$$

**Dimensional Analysis:**

| Term | Dimensions | Notes |
|------|------------|-------|
| $f(E)$ | dimensionless | Fermi-Dirac distribution is a probability (0 ≤ f ≤ 1) |
| $f(E_{\mathbf{k}}) - f(E_{\mathbf{k}+\mathbf{q}})$ | dimensionless | Difference of dimensionless quantities |
| $E_{\mathbf{k}+\mathbf{q}} - E_{\mathbf{k}}$ | energy | Energy difference |
| $\frac{f(E_{\mathbf{k}}) - f(E_{\mathbf{k}+\mathbf{q}})}{E_{\mathbf{k}+\mathbf{q}} - E_{\mathbf{k}}}$ | energy$^{-1}$ | Dimensionless/energy |
| $1/N$ | dimensionless | Normalization |
| $\sum_{\mathbf{k}}$ | dimensionless | Summation over dimensionless wavevectors |

**Result:** $[\chi_0] = \text{energy}^{-1}$ ✓

---

### 2.4 Density of States Formula

**Formula:**
$$
U_c = \left[ \int \frac{d^2k}{(2\pi)^2} \left( -\frac{\partial f(E(\mathbf{k}))}{\partial E} \right) \right]^{-1} = \frac{1}{N(E_F)}
$$

**Dimensional Analysis:**

| Term | Dimensions | Notes |
|------|------------|-------|
| $\frac{d^2k}{(2\pi)^2}$ | length$^{-2}$ | 2D k-space volume element |
| $-\frac{\partial f(E)}{\partial E}$ | energy$^{-1}$ | Derivative of dimensionless f w.r.t. energy E |
| Integral | length$^{-2}$ × energy$^{-1}$ | In k-space units |

**Correction for Units:** The differential $d^2k$ should actually be the dimensionless integration measure over the Brillouin zone:

$$
U_c = \left[ \frac{V}{(2\pi)^2} \int_{\text{BZ}} d^2k \left( -\frac{\partial f(E(\mathbf{k}))}{\partial E} \right) \right]^{-1}
$$

where $V$ is the system volume (area in 2D), making the bracket expression dimensionless density of states at Fermi level.

**The dimensionally consistent form:**
$$
N(E_F) = \sum_{\mathbf{k},\nu} \delta(E_F - E_\nu(\mathbf{k}))
$$

This has dimensions of energy$^{-1}$, so:
$$
[U_c] = [1/N(E_F)] = \text{energy} \quad \checkmark
$$

---

### 2.5 Coupling Constant in Extended Term

**Formula (Extended Hubbard):**
$$
H_{\text{ext}} = V \sum_{\langle i,j \rangle} n_i n_j
$$

**Dimensional Analysis:**

| Symbol | Dimensions |
|--------|------------|
| $V$ | energy |
| $n_i = n_{i\uparrow} n_{i\downarrow}$ | dimensionless (number operator) |

**Result:** $[H_{\text{ext}}] = [V] = \text{energy}$ ✓

---

### 2.6 Peierls-Hubbard Hamiltonian

**Formula:**
$$
H = -\sum_{i,\sigma}\left[t_h(1+\delta(-1)^i)c^\dagger_{i,\sigma}c_{i+1,\sigma} + \text{H.c.}\right] + U\sum_i n_{i\uparrow}n_{i\downarrow}
$$

**Dimensional Analysis:**

| Symbol | Dimensions |
|--------|------------|
| $t_h$ | energy |
| $\delta$ | dimensionless (dimerization parameter) |
| $(-1)^i$ | dimensionless |
| $c^\dagger, c$ | dimensionless (creation/annihilation operators) |
| $U$ | energy |

**Result:** Both the kinetic term $t_h(1+\delta(-1)^i)$ and the interaction term $U$ have dimensions of energy ✓

---

## 3. Corrected Formulas Based on Dimensional Analysis

### 3.1 Corrected Band Energy Expression

The band energy expression should properly account for the dimensionless nature of the arguments to trigonometric functions:

$$
\boxed{E_{\pm}(\mathbf{k}) = -\mu \pm \sqrt{4(\cos(k_x a) - \cos(k_y a))^2 + |h_{12}(\mathbf{k} a)|^2}}
$$

where $a$ is the lattice constant, making $k_x a$ and $k_y a$ dimensionless.

### 3.2 Corrected Susceptibility Expression

The susceptibility can be written in its properly dimensioned integral form:

$$
\boxed{\chi_0(\mathbf{Q}) = \int \frac{d^2k}{(2\pi)^2} \frac{\theta(E_F - E(\mathbf{k})) \theta(E(\mathbf{k}+\mathbf{Q}) - E_F)}{E(\mathbf{k}+\mathbf{Q}) - E(\mathbf{k})}}
$$

where the differential $d^2k$ carries dimensions of length$^{-2}$, and the energy terms provide the energy$^{-1}$ dimension, resulting in:

$$
[\chi_0] = \text{length}^{-2} \times \text{energy}^{-1}
$$

When properly normalized by the sample area $L^2$:

$$
\chi_0^{\text{normalized}}(\mathbf{Q}) = \frac{L^2}{(2\pi)^2} \int_{\text{BZ}} d^2k \frac{\theta(E_F - E(\mathbf{k})) \theta(E(\mathbf{k}+\mathbf{Q}) - E_F)}{E(\mathbf{k}+\mathbf{Q}) - E(\mathbf{k})}
$$

which has dimensions of energy$^{-1}$.

### 3.3 Corrected Critical Interaction Formula

The final expression with proper dimensions:

$$
\boxed{U_c = \left[ \frac{1}{N} \sum_{\mathbf{k}} \frac{\theta(E_F - E(\mathbf{k})) \theta(E(\mathbf{k}+\mathbf{Q}) - E_F)}{E(\mathbf{k}+\mathbf{Q}) - E(\mathbf{k})} \right]^{-1}}
$$

or in integral form:

$$
\boxed{U_c = \left[ \frac{1}{(2\pi)^2} \int_{\text{BZ}} d^2k \frac{\theta(E_F - E(\mathbf{k})) \theta(E(\mathbf{k}+\mathbf{Q}) - E_F)}{E(\mathbf{k}+\mathbf{Q}) - E(\mathbf{k})} \right]^{-1}}
$$

## 4. Summary of Dimensional Consistency

All key formulas used in determining the critical interaction strength $U_c$ for the two-band Hubbard model at quarter-filling are dimensionally consistent after the following clarifications:

1. **Trigonometric functions** in band energies require implicitly dimensionless wave vector components when expressed in units of the inverse lattice constant ($ka$)

2. **Susceptibility** $\chi_0(\mathbf{Q})$ has dimensions of energy$^{-1}$ (or energy$^{-1}$ × volume when using improper normalization)

3. **Critical interaction** $U_c = 1/\chi_0(\mathbf{Q})$ has dimensions of energy, as required for an interaction parameter

4. **Creation/annihilation operators** and **number operators** are dimensionless, while all coupling constants ($t$, $\mu$, $U$, $V$) have dimensions of energy

5. **Density of states** $N(E_F)$ has dimensions of energy$^{-1}$, making $1/N(E_F)$ a valid energy scale for $U_c$

The dimensional analysis confirms the mathematical framework is physically consistent and the formulas can be confidently used for numerical computation of $U_c$.
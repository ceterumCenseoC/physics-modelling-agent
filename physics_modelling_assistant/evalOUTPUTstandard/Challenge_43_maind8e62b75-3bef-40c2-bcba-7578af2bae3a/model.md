# Mathematical Description of Fractional Disclination Charges in a 4-fold Symmetric Insulator

## Problem Setup

Consider a 4-fold rotationally symmetric ($C_4$) 2D insulator on a square lattice with **ten** occupied Wannierizable bands [1]. The Wannier orbital configuration is specified by the Wyckoff positions:

| Wyckoff Position | Multiplicity $M_\alpha$ | Description | Occupied Bands | $n_\alpha$ |
|---|---|---|---|---|
| **1a** | 1 | Lattice site | 4 | $n_a = 4$ |
| **1b** | 1 | Plaquette center | 4 | $n_b = 4$ |
| **2c** | 2 | Edge center | 2 | $n_c = 1$ |

Here, $n_\alpha$ represents the number of Wannier orbitals per Wyckoff position per unit cell. The total number of occupied bands is verified as:
$$M_a n_a + M_b n_b + M_c n_c = 1(4) + 1(4) + 2(1) = 10$$

## Theoretical Framework

### Disclination Charge Formula

For a $C_4$-symmetric topological crystalline insulator with zero Chern number, the fractional charge trapped at a disclination core is derived from the symmetry representation and the disclination holonomy [1, Eq. 3]:

$$Q^{(4)}_{\rm dis} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \pmod 1$$

where:
- $\Omega$ is the Frank angle of the disclination
- $T^{(4)}$ is the vector perpendicular to the translation holonomy
- $P^{(4)}$ is the bulk polarization given by $P^{(4)} = \frac{n_b + n_c}{2}(e_1 + e_2) \mod 1$

### Translation-Equivalence Classes

For disclinations with $\Omega = \pm \pi/2$, the conjugacy class is classified by the discrete quantity $[a]^{(4)} \in \mathbb{Z}_2$, derived from the translation part of the disclination holonomy [1, Sec. II]:
- **$[a]^{(4)} = 0$**: Trivial translation-equivalence class (even sum of components)
- **$[a]^{(4)} = 1$**: Nontrivial translation-equivalence class (odd sum of components)

Based on Table I of Li et al. [1], the specific formulas for $\Omega = -\pi/2$ are:

**For trivial class ($[a]^{(4)} = 0$):**
$$Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4} \mod 1$$

**For nontrivial class ($[a]^{(4)} = 1$):**
$$Q^{(4)}_{\rm dis} = \frac{n_b}{4} \mod 1$$

---

## Solution for Original Configuration ($n_b = 4, n_c = 1$)

### Case 1: Nontrivial Translation-Equivalence Class ($[a]^{(4)} = 1$)

Using the formula for the nontrivial class:
$$Q^{(4)}_{\rm dis} = \frac{n_b}{4} = \frac{4}{4} = 1$$

Reducing modulo 1:
$$Q = 1 \equiv 0 \pmod 1$$

Expressed in $[-1/2, 1/2)$:
$$\boxed{Q = 0}$$

### Case 2: Trivial Translation-Equivalence Class ($[a]^{(4)} = 0$)

Using the formula for the trivial class:
$$Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4} = -\frac{4 + 2(1)}{4} = -\frac{6}{4} = -\frac{3}{2}$$

Reducing modulo 1:
$$-\frac{3}{2} \equiv \frac{1}{2} \pmod 1$$

Expressed in $[-1/2, 1/2)$ (where $\frac{1}{2} \equiv -\frac{1}{2}$):
$$\boxed{Q = -\frac{1}{2}}$$

---

## Solution with Additional Band at 1b ($l = +1/2$)

Adding one occupied Wannier orbital at the **1b** position with angular momentum $l = +1/2$ increases $n_b$ by 1.

**New parameters:** $n_b = 5$, $n_c = 1$

### Case 3: Nontrivial Translation-Equivalence Class ($[a]^{(4)} = 1$)

$$Q^{(4)}_{\rm dis} = \frac{n_b}{4} = \frac{5}{4}$$

Reducing modulo 1:
$$\frac{5}{4} \equiv \frac{1}{4} \pmod 1$$

Expressed in $[-1/2, 1/2)$:
$$\boxed{Q = \frac{1}{4}}$$

### Case 4: Trivial Translation-Equivalence Class ($[a]^{(4)} = 0$)

$$Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4} = -\frac{5 + 2(1)}{4} = -\frac{7}{4}$$

Reducing modulo 1:
$$-\frac{7}{4} = -2 + \frac{1}{4} \equiv \frac{1}{4} \pmod 1$$

Expressed in $[-1/2, 1/2)$:
$$\boxed{Q = \frac{1}{4}}$$

---

## Summary of Results

| Configuration | Translation Class | $n_b$ | Trapped Charge $Q$ (in $[-1/2, 1/2)$) |
|---|---|---|---|
| **10 bands** | Nontrivial ($[a]^{(4)}=1$) | 4 | $\boxed{0}$ |
| **10 bands** | Trivial ($[a]^{(4)}=0$) | 4 | $\boxed{-\tfrac{1}{2}}$ |
| **11 bands** (+1 band at 1b, $l=+1/2$) | Nontrivial ($[a]^{(4)}=1$) | 5 | $\boxed{\tfrac{1}{4}}$ |
| **11 bands** (+1 band at 1b, $l=+1/2$) | Trivial ($[a]^{(4)}=0$) | 5 | $\boxed{\tfrac{1}{4}}$ |

## References

[1] T. Li, P. Zhu, W. A. Benalcazar, and T. L. Hughes, "Fractional disclination charge in two-dimensional Cₙ-symmetric topological crystalline insulators," *Phys. Rev. B* **101**, 115115 (2020), [arXiv:1906.02752](https://arxiv.org/abs/1906.02752).

- Table I provides the fractional disclination charge formulas for $C_4$ symmetry.
- Section II defines the translation-equivalence class classification.
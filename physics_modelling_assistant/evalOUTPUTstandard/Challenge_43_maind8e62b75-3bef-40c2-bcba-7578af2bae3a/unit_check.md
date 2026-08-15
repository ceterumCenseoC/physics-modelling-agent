# Fractional Disclination Charge Analysis

## Units of the Quantities

Before analyzing the formulas, let us establish the units of the quantities involved.

$$ [Q_{\rm dis}] = \text{charge} $$
$$ [\Omega] = 1 \quad (\text{dimensionless: angle in radians}) $$
$$ [n_\alpha] = 1 \quad (\text{dimensionless: count of orbitals}) $$
$$ [P] = \frac{\text{charge}}{\text{length}} \quad (\text{polarization density}) $$
$$ [T] = \text{length} \quad (\text{translation holonomy vector}) $$

## Dimensional Analysis of the Formula

The formula presented in the analysis is:
$$Q^{(4)}_{\rm dis} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \mod 1$$

Let us verify the dimensional consistency of each term.

**Term 1:**
$$ \left[ \frac{\Omega}{2\pi}(n_b + 2n_c) \right] = \frac{1}{1} \cdot (1 + 2 \cdot 1) = 1 $$

**Term 2:**
$$ [T^{(4)} \cdot P^{(4)}] = [T] \cdot [P] = \text{length} \cdot \left( \frac{\text{charge}}{\text{length}} \right) = \text{charge} $$

**Analysis:**
The term $\frac{\Omega}{2\pi}(n_b + 2n_c)$ is dimensionless (units of 1), while the term $T^{(4)} \cdot P^{(4)}$ has units of charge. These cannot be added directly.
The term $T^{(4)} \cdot P^{(4)}$ represents a dipole moment contribution.
Furthermore, the result is taken $\mod 1$ (modulo 1).
The formula as written mixes dipole moment contributions (charge) with pure numbers. The formula relies on a system of units (e.g., $e=1$) and a specific lattice scale ($a=1$).
We can make the formula dimensionally consistent by explicitly noting the units and the fact that $Q_{\rm dis}$ is being expressed in units of the elementary charge $e$.

## Corrected Formulas

To ensure unit consistency, we can reformulate the expression. The fractional disclination charge has units of charge.

**Corrected General Formula:**
$$Q^{(4)}_{\rm dis} = e \left[ \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \right] \mod e$$

Where $e$ is the elementary charge, $T^{(4)}$ has units of length, and $P^{(4)}$ has units of $e/\text{length}$.
Alternatively, all quantities can be expressed in natural units ($e=1, a=1$) where the formula is dimensionally consistent as pure numbers.

The simplified expressions from Table I of the paper (Li et al.) are expressions for the charge in units of $e$:
$$Q^{(4)}_{\rm dis} = e \left( \frac{n_b}{4} \right) \mod e \quad (\text{for } [a]^{(4)} = 1)$$
$$Q^{(4)}_{\rm dis} = e \left( -\frac{n_b + 2n_c}{4} \right) \mod e \quad (\text{for } [a]^{(4)} = 0)$$

These formulas are dimensionally consistent, returning a value with units of charge.

---

# Mathematical Description of Fractional Disclination Charges

The problem involves calculating the fractional charge trapped at a disclination in a C₄-symmetric insulator.

## Parameters and Setup

The Wannier orbital configuration in the unit cell is:

| Wyckoff Position | Multiplicity $M_\alpha$ | Occupied Bands | $n_\alpha$ (Orbitals/Point) |
|---|---|---|---|
| **a** (site) | 1 | 4 | $n_a = 4$ |
| **b** (center) | 1 | 4 | $n_b = 4$ |
| **c** (edge) | 2 | 2 | $n_c = 1$ |

Total bands: $M_a n_a + M_b n_b + M_c n_c = 1(4) + 1(4) + 2(1) = 10$.

## Fractional Charge Formulas

For a disclination with Frank angle $\Omega = -\pi/2$, the fractional charge in units of elementary charge $e$ is [1]:

*   **Nontrivial translation-equivalence class ($[a]^{(4)} = 1$):**
    $$ \frac{Q^{(4)}_{\rm dis}}{e} = \frac{n_b}{4} = \pm \frac{n_b}{4} \quad (\Omega = \mp \pi/2) $$

*   **Trivial translation-equivalence class ($[a]^{(4)} = 0$):**
    $$ \frac{Q^{(4)}_{\rm dis}}{e} = -\frac{n_b + 2n_c}{4} = \pm \frac{n_b + 2n_c}{4} \quad (\Omega = \pm \pi/2) $$

Results are taken modulo 1 (modulo $e$ for charge).

## Results (Units of $e$)

### Case 1: Original Configuration ($n_b = 4, n_c = 1$)

*   **Nontrivial ($[a]^{(4)} = 1$):**
    $$ \frac{Q}{e} = \frac{4}{4} = 1 \equiv 0 \pmod 1 $$
    $$ Q = 0 $$

*   **Trivial ($[a]^{(4)} = 0$):**
    $$ \frac{Q}{e} = -\frac{4 + 2(1)}{4} = -\frac{6}{4} = -\frac{3}{2} \equiv \frac{1}{2} \pmod 1 $$
    In the interval $[-1/2, 1/2)$, $\frac{1}{2} \equiv -\frac{1}{2}$.
    $$ Q = -\frac{1}{2}e $$

### Case 2: With Additional Band at 1b ($n_b = 5, n_c = 1$)

Adding one band at position b increases $n_b$ to 5.

*   **Nontrivial ($[a]^{(4)} = 1$):**
    $$ \frac{Q}{e} = \frac{5}{4} \equiv \frac{1}{4} \pmod 1 $$
    $$ Q = \frac{1}{4}e $$

*   **Trivial ($[a]^{(4)} = 0$):**
    $$ \frac{Q}{e} = -\frac{5 + 2(1)}{4} = -\frac{7}{4} = -2 + \frac{1}{4} \equiv \frac{1}{4} \pmod 1 $$
    $$ Q = \frac{1}{4}e $$

### Case 3: With Additional Band at 1a ($n_a = 5, n_b = 4, n_c = 1$)

The formulas depend only on $n_b$ and $n_c$. Since $n_b$ and $n_c$ are unchanged:
*   **Nontrivial ($[a]^{(4)} = 1$):** $Q = 0$
*   **Trivial ($[a]^{(4)} = 0$):** $Q = -\frac{1}{2}e$

### Case 4: With Additional Band at 2c ($n_c = 2, n_b = 4$)

Increasing $n_c$ to 2 (4 bands at 2c).

*   **Nontrivial ($[a]^{(4)} = 1$):**
    $$ \frac{Q}{e} = \frac{4}{4} = 1 \equiv 0 \pmod 1 $$
    $$ Q = 0 $$

*   **Trivial ($[a]^{(4)} = 0$):**
    $$ \frac{Q}{e} = -\frac{4 + 2(2)}{4} = -\frac{8}{4} = -2 \equiv 0 \pmod 1 $$
    $$ Q = 0 $$

## Summary Table

| Configuration | Translation Class | Charge ($Q/e$ in $[-1/2, 1/2)$) |
|---|---|---|
| **10 bands** ($n_b=4, n_c=1$) | Nontrivial ($[a]=1$) | **0** |
| **10 bands** ($n_b=4, n_c=1$) | Trivial ($[a]=0$) | **-1/2** |
| **+1 band at 1b** ($n_b=5$) | Nontrivial ($[a]=1$) | **1/4** |
| **+1 band at 1b** ($n_b=5$) | Trivial ($[a]=0$) | **1/4** |
| **+1 band at 1a** ($n_a=5$) | Nontrivial ($[a]=1$) | **0** |
| **+1 band at 1a** ($n_a=5$) | Trivial ($[a]=0$) | **-1/2** |
| **+1 band at 2c** ($n_c=2$) | Nontrivial ($[a]=1$) | **0** |
| **+1 band at 2c** ($n_c=2$) | Trivial ($[a]=0$) | **0** |

## Reference

[1] T. Li, P. Zhu, W. A. Benalcazar, and T. L. Hughes, "Fractional disclination charge in two-dimensional Cₙ-symmetric topological crystalline insulators," Phys. Rev. B **101**, 115115 (2020).
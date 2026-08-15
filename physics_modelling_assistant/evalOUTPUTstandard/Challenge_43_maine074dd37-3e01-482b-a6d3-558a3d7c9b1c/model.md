# Mathematical Description of the Model and Calculation of Disclination Charges

## 1. Physical Model Setup

We consider a 2D insulator on a square lattice with $C_4$ rotational symmetry. The system consists of $N$ occupied bands that are Wannierizable. The lattice vectors are chosen as $\mathbf{a}_1 = a \hat{x}$ and $\mathbf{a}_2 = a \hat{y}$. The unit cell is centered at the origin.

The specific configuration of the 10 occupied bands is as follows:
*   **2 bands:** Correspond to Wannier orbitals centered at the **2c** Wyckoff position.
    *   Position coordinate: $\mathbf{r}_c = (1/2, 0)a$ (edge center).
    *   Number of orbitals per unit cell: $n_c = 1$ pair (2 orbitals, or simply count 1 "site" of type c for the invariant). Note: The formula uses the multiplicity count $n_c$, which corresponds to the number of 2c sites (1). However, since the charge formula depends on the total representation characters at the high-symmetry points, we can map this to the orbital counts. The variables $n_b$ and $n_c$ in the standard formula represent the *multiplicity* of the Wyckoff positions per unit cell (i.e., number of plaquettes or edge centers per unit cell). For the 2c position, there is 1 such site unit cell per axis, but in the context of the "grid" for disclination index, we treat $n_c$ as the number of occupied orbitals per loop, which scales with the multiplicity. Here, we have one pair at 2c, contributing to the effective charge count.
    *   Effective count for charge calculation: We treat $n_c$ as the parameter associated with the high-symmetry points linked to this Wyckoff position. In the disclination charge formula adapted for grid constructions, $n_c$ represents the contribution from the filling anomaly associated with the specific Wyckoff position. Given the setup references "two of them correspond to a pair... at 2c", we assign the parameter $n_c=1$ representing the presence of the 2c orbitals (a single translational site type per cell corner).
*   **4 bands:** Correspond to Wannier orbitals centered at the **1b** Wyckoff position.
    *   Position coordinate: $\mathbf{r}_b = (1/2, 1/2)a$ (plaquette center).
    *   Number of orbitals per unit cell: $n_b = 1$ (one 1b site per unit cell, with multiplicity 4 for the 4 orbitals). However, the charge formula depends on the number of *placiente* indices or the total filling anomaly associated with the 1b site. Let's verify the definition of $n_b$. In the context of the formula developed by Li et al., $n_b$ corresponds to the number of plaquette-centered orbitals (or the contribution from the $b$ Wyckoff position) in the specific $C_n$ disclination context. Given "Four of them correspond to... 1b", this implies a filling associated with the 1b position.
*   **4 bands:** Correspond to Wannier orbitals centered at the **1a** Wyckoff position.
    *   Position coordinate: $\mathbf{r}_a = (0, 0)a$ (lattice site).
    *   This position is invariant under rotations and contributes trivially to the disclination charge deficit in the formulas concerning the filling anomaly at high symmetry points or specific Wyckoff positions $1b$ and $2c$. Their contribution to the $C_4$ polarization indices $x_{2\pi/n}$ is zero.

**Translation-Equivalence Class:**
The translation-equivalence class $[a]^{(4)}$ is a $Z_2$ index that distinguishes between two types of atomic limits in $C_4$-symmetric systems with a given partial filling. It determines how the filling anomaly is distributed.
*   $[a]^{(4)} = 0$: Trivial class.
*   $[a]^{(4)} = 1$: Nontrivial class.

## 2. Disclination Charge Formula

For a disclination with Frank angle $\Omega = -\pi/2$ (which corresponds to a $90^\circ$ wedge removal, effectively a rotation index of 1), the fractional charge trapped at the core $Q_{\text{dis}}^{(4)}$ (in units of electron charge $e$) is given by the relation derived from the filling anomaly and the index classification [1].

The general form of the trapped charge depends on the translation-equivalence class $[a]^{(4)}$ and the number of orbitals (or effective multiplicity) at the high-symmetry positions contributing to the anomaly. Specifically, the charge is modulated by the occupancy at positions $1b$ ($n_b$) and $2c$ ($n_c$).

The formula is:

$$Q_{\text{dis}}^{(4)} = \begin{cases} 
\dfrac{n_b}{4} \pmod 1 & \text{for nontrivial class } ([a]^{(4)} = 1) \\[8pt]
-\dfrac{n_b + 2n_c}{4} \pmod 1 & \text{for trivial class } ([a]^{(4)} = 0)
\end{cases}$$

**Variable definitions:**
*   $n_b$: The number of orbitals (or effective multiplicity factor) associated with the $1b$ (plaquette center) position in the context of the $C_4$ invariant. Here, we have 4 bands for one $1b$ site. In the context of the standard formula [1], $n_b$ effectively counts the contribution of the plaquette indices.
*   $n_c$: The number of orbitals (or effective multiplicity factor) associated with the $2c$ (edge center) position. Here we have 2 bands for one $2c$ site.

From the provided specific problem setup:
*   "Two of them correspond to ... 2c" $\rightarrow n_c = 1$ (representing the single loop contribution).
*   "Four of them correspond to ... 1b" $\rightarrow n_b = 1$ (representing the single plaquette contribution). *Correction*: The formula typically uses the count of bands associated with the *site* multiplicity or the grid index. Let's strictly follow the interpretation where "n_b" is the coefficient from the table in [1] matching the Wyckoff position filling. For $1b$, the index contribution is related to the number of bands at $1b$ modulo 4. The formula in [1] (Table I, Eq 37) gives $\Delta Q = n_b/4$ or $-(n_b+2n_c)/4$. Here $n_b$ and $n_c$ are the "count" of the orbitals at those specific symmetric Wyckoff positions in the basis of the eigenstates. Since the problem specifies bands originate from these positions, we map the "4 bands at 1b" to a parameter $n_b$ and "2 bands at 2c" to $n_c$. In the simplified notation for the "grid" model, $n_b$ often represents the number of plaquette orbitals in a reduced basis. Let's align with the provided context values: $n_b=4$ and $n_c=1$ (interpreting "pair at 2c" as $n_c=1$ pair, and "four at 1b" as $n_b=4$ bands). Actually, the prompt says $n_b=4, n_c=1$ in the context analysis derived from "four... at 1b" and "two... at 2c". Let's verify. If $n_b$ represents the number of occupied bands at $1b$, then $n_b=4$. If $n_c$ represents the number of pairs or equivalent count at $2c$, given the factor 2 in the formula, it might be $n_c=1$. Let's test consistency with typical dimensions.
    *   If $n_b=4$ (count of 1b bands) and $n_c=1$ (count of 2c pairs), the charge is $Q = 4/4 = 1 \equiv 0$ or $Q = -(4+2)/4 = -1.5 \equiv -0.5$.
    *   This matches the "Context" values.

Therefore, we adopt:
*   $n_b = 4$ (The number of Wannier bands at the 1b position).
*   $n_c = 1$ (The number of Wannier pairs at the 2c position).

## 3. Calculation for the 10-Band System

### Case A: Nontrivial Translation-Equivalence Class ($[a]^{(4)} = 1$)

Using the formula for the nontrivial class:
$$ Q = \frac{n_b}{4} \pmod 1 $$

Substituting $n_b = 4$:
$$ Q = \frac{4}{4} = 1 $$

To express this in the interval $[-1/2, 1/2)$, we subtract the integer part 1:
$$ 1 \equiv 0 \pmod 1 $$

**Result:** $\mathbf{0}$

### Case B: Trivial Translation-Equivalence Class ($[a]^{(4)} = 0$)

Using the formula for the trivial class:
$$ Q = -\frac{n_b + 2n_c}{4} \pmod 1 $$

Substituting $n_b = 4$ and $n_c = 1$:
$$ Q = -\frac{4 + 2(1)}{4} = -\frac{6}{4} = -1.5 $$

To express this in the interval $[-1/2, 1/2)$, we add 2 (since $-1.5 + 2 = 0.5$, which is the boundary, so we look for the equivalent form strictly in the interval or handle modulo 1 carefully).
$-1.5 \equiv 0.5 \pmod 1$.
However, the interval is $[-1/2, 1/2)$. The value $0.5$ is not included. The equivalent value on the other side is $0.5 - 1 = -0.5$.
(Note: The interval includes $-1/2$ but excludes $1/2$).

**Result:** $\mathbf{-0.5}$

## 4. Calculation for the 11-Band System (One Additional Band at 1b)

Now we consider adding one more occupied band. The new band corresponds to a Wannier orbital at the **1b** position with angular momentum $l=+1/2$.

*   New count of bands at 1b: $n_b' = 4 + 1 = 5$.
*   Count at 2c remains: $n_c' = 1$.

### Case A: Nontrivial Translation-Equivalence Class ($[a]^{(4)} = 1$)

Using the formula:
$$ Q = \frac{n_b'}{4} \pmod 1 $$

Substituting $n_b' = 5$:
$$ Q = \frac{5}{4} = 1.25 $$

Reducing modulo 1:
$$ 1.25 - 1 = 0.25 $$
This value lies in $[-1/2, 1/2)$.

**Result:** $\mathbf{0.25}$

### Case B: Trivial Translation-Equivalence Class ($[a]^{(4)} = 0$)

Using the formula:
$$ Q = -\frac{n_b' + 2n_c'}{4} \pmod 1 $$

Substituting $n_b' = 5$ and $n_c' = 1$:
$$ Q = -\frac{5 + 2(1)}{4} = -\frac{7}{4} = -1.75 $$

Reducing modulo 1:
We need a value $x \in [-1/2, 1/2)$ such that $x \equiv -1.75 \pmod 1$.
Adding 2:
$-1.75 + 2 = 0.25$.
$0.25$ lies in $[-1/2, 1/2)$.

**Result:** $\mathbf{0.25}$

## 5. Summary of Results

The fractional charges trapped to the disclination core are:

**For the initial 10-band configuration:**
*   Nontrivial translation-equivalence class ($[a]^{(4)}=1$): **0**
*   Trivial translation-equivalence class ($[a]^{(4)}=0$): **-0.5**

**For the system with one additional band at 1b ($l=+1/2$):**
*   Nontrivial translation-equivalence class ($[a]^{(4)}=1$): **0.25**
*   Trivial translation-equivalence class ($[a]^{(4)}=0$): **0.25**

## References

[1] T. Li, P. Zhu, W. A. Benalcazar, and T. L. Hughes, "Fractional disclination charge in two-dimensional $C_n$-symmetric topological crystalline insulators," *Phys. Rev. B* **101**, 115115 (2020).
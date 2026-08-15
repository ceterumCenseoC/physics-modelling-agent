Based on my analysis of the papers, I can now extract the relevant information needed to answer this problem about fractional disclination charges in a C₄-symmetric Wannierizable insulator.

The key paper is **Li, Zhu, Benalcazar, and Hughes, "Fractional disclination charge in two-dimensional Cₙ-symmetric topological crystalline insulators," Phys. Rev. B 101, 115115 (2020)** (arXiv:1906.02752). This paper provides the central framework for computing fractional disclination charges.

Let me work through the problem setup.

## Problem Setup Analysis

We have a C₄-symmetric 2D insulator on a square lattice with **ten** occupied Wannierizable bands:
- **2 bands** from Wannier orbitals at the **2c** position (edge center, Wyckoff position c with multiplicity 2)
- **4 bands** from Wannier orbitals at the **1b** position (plaquette center, Wyckoff position b with multiplicity 1)
- **4 bands** from Wannier orbitals at the **1a** position (lattice site, Wyckoff position a with multiplicity 1)

Wait, let me recount. The total is 10 occupied bands.

From the paper (Li et al.), for a C₄-symmetric TCI:
- Wyckoff position **a**: multiplicity 1 (lattice site)
- Wyckoff position **b**: multiplicity 1 (plaquette center)
- Wyckoff position **c**: multiplicity 2 (edge center)

The number of electrons per unit cell is $M_\alpha n_\alpha$ where $M_\alpha$ is the multiplicity. Total occupied bands: $\nu = \sum_\alpha M_\alpha n_\alpha$.

Given:
- 2 bands from position c (multiplicity 2): so $n_c = 1$ (each of the 2 orbitals at the two c-points carries 1 electron)
- 4 bands from position b (multiplicity 1): so $n_b = 4$
- 4 bands from position a (multiplicity 1): so $n_a = 4$

Total: $M_c n_c + M_b n_b + M_a n_a = 2(1) + 1(4) + 1(4) = 2 + 4 + 4 = 10$. ✓

## Fractional Disclination Charge Formula

From Li et al. (Eq. 3 in the paper), the fractional disclination charge for C₄-symmetric TCIs is:

$$Q^{(4)}_{\rm dis} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \mod 1$$

Where:
- $\Omega$ is the Frank angle
- $n_\alpha = \sum_l n_\alpha^l$ is the total number of Wannier orbitals at Wyckoff position $\alpha$
- $T^{(4)} = a_1 d_2 - a_2 d_1$ is the vector perpendicular to the translation holonomy
- $P^{(4)} = \frac{n_b + n_c}{2}(e_1 + e_2) \mod 1$ is the bulk polarization

Note: In the version by Wada & Murakami (arXiv:2512.04325), the formula is written with $\Delta$ (charge imbalance) instead of $n$: $Q^{(4)}_{\rm dis} \equiv -\frac{\Omega}{2\pi}(\Delta_b + 2\Delta_c) + T^{(4)} \cdot P^{(4)} \pmod{1}$, but the result is the same since $\Delta_\alpha = n_\alpha - m_\alpha$ and for a neutral system $\sum_\alpha \Delta_\alpha = 0$.

### Case 1: Disclination with Frank angle $\Omega = -\pi/2$

**Translation-equivalence class nontrivial, $[a]^{(4)} = 1$:**

From Table I in Li et al.:

$$Q^{(4)}_{\rm dis} = \mp\frac{n_b}{4} \quad \text{for } \Omega = \pm \frac{\pi}{2},\ [a]^{(4)} = 1$$

For $\Omega = -\pi/2$:
$$Q^{(4)}_{\rm dis} = \frac{n_b}{4} = \frac{4}{4} = 1 \equiv 0 \mod 1$$

Wait, let me check this more carefully. The paper states (Table I):

For C₄, $\Omega = \pm\pi/2$:
- $[a]^{(4)} = 0$: $Q^{(4)}_{\rm dis} = \pm\frac{n_b + 2n_c}{4}$
- $[a]^{(4)} = 1$: $Q^{(4)}_{\rm dis} = \mp\frac{n_b}{4}$

For $\Omega = -\pi/2$, $[a]^{(4)} = 1$: $Q^{(4)}_{\rm dis} = \frac{n_b}{4} = 1 \mod 1$.

Hmm, this gives an integer. But wait, I need to be more careful about what "nontrivial" means here for the translation-equivalence class.

From the paper: "For disclinations with Frank angle $\Omega = \pm\frac{\pi}{2}$, $[a]^{(4)}$ takes values in $\mathbb{Z}_2$, i.e., $[a]^{(4)} = 0$ or $[a]^{(4)} = 1$, by which we represent the sum of the two components of $a$ being even or odd respectively."

**Non-trivial** translation-equivalence class means $[a]^{(4)} = 1$.

So for $\Omega = -\pi/2$, $[a]^{(4)} = 1$ (nontrivial):

$$Q^{(4)}_{\rm dis} = \frac{n_b}{4} \mod 1$$

With $n_b = 4$: $Q = 4/4 = 1 \equiv 0 \pmod 1$.

Hmm, but that gives 0. Let me reconsider. Actually, looking more carefully at the bands setup and what $n_\alpha$ represents.

Actually, wait. I need to reconsider. The problem states the Wannier orbital configurations. The ten occupied bands break down as:
- 2 bands from position c → $n_c = 1$ (since multiplicity of c is 2, and there are 2 orbitals total, giving $M_c n_c = 2 \cdot n_c = 2$, so $n_c = 1$)

Wait, actually, from the paper: "the induced representation αl just represents an atomic insulator having Wannier orbitals with angular momentum l located at Wyckoff position α in each unit cell." So $n_\alpha^l$ is the number of such representations. And $n_\alpha = \sum_l n_\alpha^l$.

For Wyckoff position c with multiplicity 2, having 2 occupied Wannier bands means $n_c = 1$ (one pair of orbitals at the two c-points).

For Wyckoff position b with multiplicity 1, having 4 occupied Wannier bands means $n_b = 4$.

For Wyckoff position a with multiplicity 1, having 4 occupied Wannier bands means $n_a = 4$.

Now let me apply the formulas.

### Case A: $\Omega = -\pi/2$, $[a]^{(4)} = 1$ (nontrivial translation-equivalence class)

From Table I: $Q^{(4)}_{\rm dis} = \frac{n_b}{4} = \frac{4}{4} = 1 \equiv 0 \pmod 1$.

Expressed in $[-1/2, 1/2)$: $Q = 0$.

### Case B: $\Omega = -\pi/2$, $[a]^{(4)} = 0$ (trivial translation-equivalence class)

From Table I: $Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4} = -\frac{4 + 2(1)}{4} = -\frac{6}{4} = -\frac{3}{2} \equiv \frac{1}{2} \pmod 1$.

Let me verify: $-3/2 \mod 1 = -3/2 + 2 = 1/2$. 

So $Q = 1/2$, expressed in $[-1/2, 1/2)$: $Q = -1/2$ (since $1/2 \equiv -1/2 \pmod 1$).

Hmm, but the problem asks for values in $[-1/2, 1/2)$. So $1/2$ would be expressed as $-1/2$.

Wait, actually $1/2 \equiv -1/2 \pmod 1$. Both represent the same fractional charge. In the interval $[-1/2, 1/2)$, $1/2 \equiv -1/2$. So the answer would be $-1/2$.

Actually, let me re-examine. The problem says "Express each answer as a value in [-1/2,1/2)." So I need to express the fractional charge modulo 1, choosing the representative in that interval.

For Case B (trivial, $[a]^{(4)} = 0$): $Q = -3/2 \equiv 1/2 \pmod 1$. In $[-1/2, 1/2)$, this is $-1/2$.

### Now with one additional band at 1b with angular momentum $l = +1/2$

The problem asks: "If we consider one additional occupied band with Wannier orbitals at 1b position with angular momentum $l=+1/2$"

Adding one additional occupied band at position b means $n_b$ increases by 1. Wait, but position b has multiplicity 1, so adding one band means adding one orbital at b, giving $n_b = 5$.

Actually, I need to think about whether this is a spin-1/2 system or spinless system. The angular momentum $l = +1/2$ suggests this is a spinful system (for spinless systems, angular momenta are integers). But let me reconsider...

Actually, looking at the paper more carefully: for spin-1/2 systems, the angular momentum eigenvalues at C₄ rotation points are labeled by half-integers $l = 1/2, 3/2, \ldots$. But the problem specifically says to add a band with $l = +1/2$ at position b.

Hmm, but the problem doesn't explicitly say spin-1/2. Let me re-read. The problem says 10 occupied Wannierizable bands, with specific positions. It asks about adding "one additional occupied band with Wannier orbitals at 1b position with angular momentum $l=+1/2$."

This suggests we're dealing with a system where half-integer angular momentum is allowed, i.e., a spin-1/2 system (or at least treating it within a framework where $l$ can be half-integer at the C₄ point).

However, the key formula $Q^{(4)}_{\rm dis} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \mod 1$ applies regardless of whether $l$ is integer or half-integer. The key quantity is $n_\alpha = \sum_l n_\alpha^l$, the total number of orbitals at each position.

So adding one band at position b adds 1 to $n_b$: $n_b = 5$.

Let me recompute.

### Case A': $\Omega = -\pi/2$, $[a]^{(4)} = 1$, with extra b-orbital ($n_b = 5$)

From Table I: $Q^{(4)}_{\rm dis} = \frac{n_b}{4} = \frac{5}{4} \pmod 1$.

$\frac{5}{4} \equiv \frac{1}{4} \pmod 1$. In $[-1/2, 1/2)$: $Q = 1/4$.

### Case B': $\Omega = -\pi/2$, $[a]^{(4)} = 0$, with extra b-orbital ($n_b = 5$)

From Table I: $Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4} = -\frac{5 + 2}{4} = -\frac{7}{4} \pmod 1$.

$-\frac{7}{4} = -1 - \frac{3}{4} \equiv \frac{1}{4} \pmod 1$. In $[-1/2, 1/2)$: $Q = 1/4$.

Wait, that's interesting - both give $1/4$? Let me double-check.

$-\frac{7}{4} \mod 1$: $-\frac{7}{4} = -2 + \frac{1}{4}$, so $-\frac{7}{4} \equiv \frac{1}{4} \pmod 1$. Yes.

So $Q = 1/4$ for both cases.

Let me verify my understanding of the formulas more carefully. Let me use the more general formula from Eq. (3) of Li et al.:

For C₄: $Q^{(4)}_{\rm dis} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \mod 1$

where $P^{(4)} = \frac{n_b + n_c}{2}(e_1 + e_2) \mod 1$ and $T^{(4)} = a_1 d_2 - a_2 d_1$.

From the paper (Section II): For $\Omega = \pm\pi/2$, the translation part determines the conjugacy class. For $[a]^{(4)} = 0$, $a = -2e_1$ (even sum), so $T^{(4)} = a_1 d_2 - a_2 d_1 = -2 \cdot 0 - 0 \cdot 1 = 0$ (if $d_1 = e_1$, $d_2 = e_2$). Actually, I need to be careful with the definition.

Actually, let me just use Table I directly since the paper provides concrete formulas.

From Table I (Li et al.):
- C₄, $\Omega = -\pi/2$, $[a]^{(4)} = 0$: $Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4}$
- C₄, $\Omega = -\pi/2$, $[a]^{(4)} = 1$: $Q^{(4)}_{\rm dis} = \frac{n_b}{4}$

These values are taken modulo 1.

**Original setup (no extra band):** $n_b = 4$, $n_c = 1$
- $[a]^{(4)} = 0$: $Q = -\frac{4 + 2}{4} = -\frac{6}{4} = -\frac{3}{2} \equiv \frac{1}{2} \equiv -\frac{1}{2} \pmod 1$
  - In $[-1/2, 1/2)$: $Q = -1/2$
- $[a]^{(4)} = 1$: $Q = \frac{4}{4} = 1 \equiv 0 \pmod 1$
  - In $[-1/2, 1/2)$: $Q = 0$

**With one additional b-orbital with $l = +1/2$:** $n_b = 5$, $n_c = 1$
- $[a]^{(4)} = 0$: $Q = -\frac{5 + 2}{4} = -\frac{7}{4} \equiv \frac{1}{4} \pmod 1$
  - In $[-1/2, 1/2)$: $Q = 1/4$
- $[a]^{(4)} = 1$: $Q = \frac{5}{4} \equiv \frac{1}{4} \pmod 1$
  - In $[-1/2, 1/2)$: $Q = 1/4$

Wait, but I should double-check whether the angular momentum $l = 1/2$ affects the result beyond just changing $n_b$. 

The disclination charge formula depends on $n_\alpha$ (total number of Wannier orbitals at each position), not on individual angular momenta. So the only effect of adding this band is to change $n_b$ from 4 to 5. The angular momentum $l = 1/2$ allows this to be a valid spin-1/2 Wannier orbital at position b (which has site symmetry group C₄, allowing half-integer angular momenta in spin-1/2 systems).

Now let me also verify the total number of bands is correct. Original: 10 bands. Adding one: 11 bands. The formula $n_\alpha = \sum_l n_\alpha^l$ just counts total number of orbitals at each position. With the extra band: $n_a = 4$, $n_b = 5$, $n_c = 1$.

Let me also verify the formula using the general index formula from Eq. (10) of Li et al. for C₄:

$$Q^{(4)}_{\rm dis} = \frac{\Omega}{2\pi}\left([X^{(2)}_1] + \frac{3}{2}[M^{(4)}_3] - \frac{1}{2}[M^{(4)}_1]\right) + T^{(4)} \cdot P^{(4)} \mod 1$$

But we're working directly with the Wannier configuration, so Table I is the appropriate choice.

Now let me also consider whether the count of $n_\alpha$ should be reconsidered. Looking at the paper:

"2c0 + a1 means that there are two pairs of Wannier orbitals with angular momentum l = 0 located at two equivalent Wyckoff positions labelled by c, plus a Wannier orbital with angular momentum l = 1 located at the Wyckoff position labelled by a in each unit cell."

So in the notation of the paper:
- For our problem, we have 2 bands at position c, so $n_c = 1$ (one pair at the two c-points, each carrying 1 electron), giving $M_c \cdot n_c = 2$.
- 4 bands at position b, so $n_b = 4$, giving $M_b \cdot n_b = 1 \times 4 = 4$.
- 4 bands at position a, so $n_a = 4$, giving $M_a \cdot n_a = 1 \times 4 = 4$.

Total: $2 + 4 + 4 = 10$. ✓

Now, I need to also consider what happens if we need to check whether the system indeed has non-zero Chern number or can have a Wannier description. The problem states it's a "Wannierizable" insulator, so it has a well-defined Wannier representation.

Also, I should note that the problem specifies 4 bands at both positions a and b. Let me verify whether these are just $n_a = 4$ and $n_b = 4$ directly (assuming they're all $l=0$ type, which doesn't affect the total count $n_\alpha$).

Actually, I realize I should double-check whether the problem setup means all bands at each position are distinct Wannier orbitals. Since each Wannier orbital at a position with multiplicity $M_\alpha$ contributes $M_\alpha$ bands, and the problem says:
- 2 bands at 2c → $n_c = 1$ (2 bands = 2 c-points × 1 orbital each)
- 4 bands at 1b → $n_b = 4$ (1 b-point × 4 orbitals)
- 4 bands at 1a → $n_a = 4$ (1 a-point × 4 orbitals)

Total: $2 + 4 + 4 = 10$. ✓

So my calculations stand. Let me now formulate the final answer.

Actually, wait. Let me reconsider the non-trivial case more carefully. The paper says:

For C₄ with $\Omega = \pm\pi/2$:
- $[a]^{(4)} = 0$: $Q^{(4)}_{\rm dis} = \pm\frac{n_b + 2n_c}{4}$
- $[a]^{(4)} = 1$: $Q^{(4)}_{\rm dis} = \mp\frac{n_b}{4}$

The sign depends on the sign of $\Omega$. For $\Omega = -\pi/2$:
- $[a]^{(4)} = 0$: $Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4}$
- $[a]^{(4)} = 1$: $Q^{(4)}_{\rm dis} = +\frac{n_b}{4}$

With original $n_b = 4$, $n_c = 1$:
- $[a]^{(4)} = 0$ (trivial): $Q = -\frac{4+2}{4} = -\frac{6}{4} = -\frac{3}{2}$. Modulo 1: $-\frac{3}{2} \equiv \frac{1}{2}$. In $[-1/2, 1/2)$: $Q = -1/2$.
- $[a]^{(4)} = 1$ (nontrivial): $Q = \frac{4}{4} = 1 \equiv 0$. In $[-1/2, 1/2)$: $Q = 0$.

With extra b-orbital $n_b = 5$, $n_c = 1$:
- $[a]^{(4)} = 0$ (trivial): $Q = -\frac{5+2}{4} = -\frac{7}{4}$. Modulo 1: $-\frac{7}{4} = -2 + \frac{1}{4} \equiv \frac{1}{4}$. In $[-1/2, 1/2)$: $Q = 1/4$.
- $[a]^{(4)} = 1$ (nontrivial): $Q = \frac{5}{4}$. Modulo 1: $\frac{5}{4} \equiv \frac{1}{4}$. In $[-1/2, 1/2)$: $Q = 1/4$.

Interesting - with the extra band, both give $1/4$ in this range.

Now I need to produce the final answer in Markdown format with proper citations.

Let me formulate the complete answer.

# Fractional Disclination Charge in a C₄-Symmetric Wannierizable Insulator

## Problem Setup

Consider a 4-fold rotationally symmetric (C₄) 2D insulator on a square lattice with **ten** occupied Wannierizable bands [1]:

| Wyckoff Position | Multiplicity $M_\alpha$ | # Bands | $n_\alpha$ (orbitals/point) |
|---|---|---|---|
| **a** (lattice site, 1a) | 1 | 4 | $n_a = 4$ |
| **b** (plaquette center, 1b) | 1 | 4 | $n_b = 4$ |
| **c** (edge center, 2c) | 2 | 2 | $n_c = 1$ |

Total: $M_a n_a + M_b n_b + M_c n_c = 4 + 4 + 2 = 10$ bands ✓

## Fractional Disclination Charge Formula

For C₄-symmetric TCIs with zero Chern number (Wannierizable), the fractional disclination charge is given by [1, Eq. (3)]:

$$Q^{(4)}_{\rm dis} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)}\cdot P^{(4)} \mod 1$$

with the bulk polarization $P^{(4)} = \frac{n_b + n_c}{2}(e_1 + e_2) \mod 1$ [1, Eq. (2)].

For a disclination with Frank angle $\Omega = -\pi/2$, the specific values from Table I of Ref. [1] are:

- **$[a]^{(4)} = 0$ (trivial translation class):** $$Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4}$$
- **$[a]^{(4)} = 1$ (nontrivial translation class):** $$Q^{(4)}_{\rm dis} = +\frac{n_b}{4}$$

modulo 1 [1, Table I].

## Results for Original Configuration ($n_b = 4$, $n_c = 1$)

### Disclination with $\Omega = -\pi/2$

**Nontrivial translation-equivalence class, $[a]^{(4)} = 1$:**

$$Q^{(4)}_{\rm dis} = \frac{n_b}{4} = \frac{4}{4} = 1 \equiv 0 \pmod 1$$

$$\boxed{Q = 0}$$

**Trivial translation-equivalence class, $[a]^{(4)} = 0$:**

$$Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4} = -\frac{4 + 2}{4} = -\frac{6}{4} = -\frac{3}{2} \equiv \frac{1}{2} \pmod 1$$

$$\boxed{Q = -\tfrac{1}{2}} \quad (\text{since } \tfrac{1}{2} \equiv -\tfrac{1}{2} \pmod 1)$$

## Results with One Additional Band at 1b ($l = +1/2$)

Adding one occupied band with Wannier orbital at position **b** with angular momentum $l = +1/2$ gives $n_b = 5$, $n_c = 1$ [1].

### Disclination with $\Omega = -\pi/2$

**Nontrivial translation-equivalence class, $[a]^{(4)} = 1$:**

$$Q^{(4)}_{\rm dis} = \frac{n_b}{4} = \frac{5}{4} \equiv \frac{1}{4} \pmod 1$$

$$\boxed{Q = \tfrac{1}{4}}$$

**Trivial translation-equivalence class, $[a]^{(4)} = 0$:**

$$Q^{(4)}_{\rm dis} = -\frac{n_b + 2n_c}{4} = -\frac{5 + 2}{4} = -\frac{7}{4} \equiv \frac{1}{4} \pmod 1$$

$$\boxed{Q = \tfrac{1}{4}}$$

## Summary Table

| Configuration | Translation class | $n_b$ | $Q_{\rm dis}$ (in $[-1/2, 1/2)$) |
|---|---|---|---|
| 10 bands (original) | Nontrivial $[a]^{(4)}=1$ | 4 | **$0$** |
| 10 bands (original) | Trivial $[a]^{(4)}=0$ | 4 | **$-\tfrac{1}{2}$** |
| +1 band at 1b, $l=+1/2$ (11 bands) | Nontrivial $[a]^{(4)}=1$ | 5 | **$\tfrac{1}{4}$** |
| +1 band at 1b, $l=+1/2$ (11 bands) | Trivial $[a]^{(4)}=0$ | 5 | **$\tfrac{1}{4}$** |

## References

[1] T. Li, P. Zhu, W. A. Benalcazar, and T. L. Hughes, "Fractional disclination charge in two-dimensional Cₙ-symmetric topological crystalline insulators," Phys. Rev. B **101**, 115115 (2020). (arXiv:1906.02752)

The key results used from this reference are:
- Table I: Fractional charge at disclination cores for C₄-symmetric TCIs with zero Chern number.
- Eq. (2): Bulk polarization in terms of Wannier orbital counts.
- Eq. (3): General fractional disclination charge index for C₄ symmetry.
- Section II: Classification of disclinations by translation-equivalence classes $[a]^{(4)} \in \mathbb{Z}_2$.
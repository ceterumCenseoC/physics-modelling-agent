

### **Step-by-Step Derivation**

**1. Identification of Wannier Orbital Configuration**
In a 4-fold rotationally symmetric ($C_4$) square lattice, the occupied bands can be characterized by their Wannier orbital configurations at maximal Wyckoff positions. Based on the problem description:
- **1b position (plaquette center):** Has a multiplicity of 1. The problem states 4 bands correspond to orbitals here, so the total number of orbitals per unit cell is $n_b = 4$.
- **2c position (edge center):** Has a multiplicity of 2. The problem states 2 bands correspond to a "pair" of orbitals here, which constitutes exactly one $C_4$-symmetric representation spread over the two equivalent sites. Thus, $n_c = 1$.
- **1a position (lattice site):** The remaining $10 - 4 - 2 = 4$ bands correspond to $n_a = 4$ orbitals.

**2. General Formula for Disclination Charge**
For a $C_4$ symmetric topological crystalline insulator with a disclination of Frank angle $\Omega$, the fractional charge localized at the core is given by [1]:
$$Q_{\text{dis}}^{(4)} = \frac{\Omega}{2\pi}(n_b + 2n_c) + T^{(4)} \cdot P^{(4)} \mod 1$$
where $T^{(4)} \cdot P^{(4)}$ accounts for the translation-equivalence class of the disclination holonomy. The problem specifies $\Omega = -\pi/2$, so $\frac{\Omega}{2\pi} = -\frac{1}{4}$.

**3. Case 1: Initial Configuration ($n_b = 4, n_c = 1$)**
- **Nontrivial translation-equivalence class ($[a]^{(4)} = 1$):** According to the topological classification of disclinations [1], the translation contribution exactly cancels the $2n_c$ term and flips the sign relative to the rotation part. The charge simplifies to:
  $$Q_{\text{dis}} = +\frac{n_b}{4} \mod 1$$
  Substituting $n_b = 4$:
  $$Q_{\text{dis}} = \frac{4}{4} = 1 \equiv 0 \mod 1$$
- **Trivial translation-equivalence class ($[a]^{(4)} = 0$):** The translation contribution vanishes modulo 1, leaving only the rotation sector contribution:
  $$Q_{\text{dis}} = -\frac{1}{4}(n_b + 2n_c) \mod 1$$
  Substituting $n_b = 4, n_c = 1$:
  $$Q_{\text{dis}} = -\frac{1}{4}(4 + 2) = -\frac{6}{4} = -1.5 \equiv -0.5 \mod 1$$

**4. Case 2: Additional Band at 1b with $l = +1/2$**
Adding one occupied band at the 1b position increases the orbital count to $n_b' = 5$. The angular momentum label $l = +1/2$ specifies the site-symmetry representation but does not alter the topological charge formula, which depends strictly on the total count $n_b$ [1].
- **Nontrivial class:**
  $$Q_{\text{dis}} = \frac{n_b'}{4} = \frac{5}{4} = 1.25 \equiv 0.25 \mod 1$$
- **Trivial class:**
  $$Q_{\text{dis}} = -\frac{1}{4}(n_b' + 2n_c) = -\frac{1}{4}(5 + 2) = -\frac{7}{4} = -1.75 \equiv 0.25 \mod 1$$

All results are mapped to the interval $[-1/2, 1/2)$ as requested.

---

### **Mathematical Typesetting**
- Orbital counts: $n_b = 4$, $n_c = 1$, $n_a = 4$
- Frank angle factor: $\frac{\Omega}{2\pi} = -\frac{1}{4}$
- Initial Nontrivial: $Q = +\frac{4}{4} \equiv 0$
- Initial Trivial: $Q = -\frac{4+2}{4} \equiv -\frac{1}{2}$
- Modified Nontrivial: $Q = +\frac{5}{4} \equiv \frac{1}{4}$
- Modified Trivial: $Q = -\frac{5+2}{4} \equiv \frac{1}{4}$

---

### **Conventions and Units**
- Charges are expressed in units of the elementary electron charge $e$.
- Modulo 1 arithmetic is used for fractional charge quantization.
- Results are strictly confined to the half-open interval $[-1/2, 1/2)$.
- Citation: T. Li, P. Zhu, W. A. Benalcazar, and T. L. Hughes, *Fractional disclination charge in two-dimensional $C_n$-symmetric topological crystalline insulators*, Phys. Rev. B **101**, 115115 (2020) [1].

---

### **Final Answer:**
**Initial Configuration:**
- Nontrivial translation-equivalence class: `$0$`
- Trivial translation-equivalence class: `$-1/2$`

**With one additional band at 1b ($l=+1/2$):**
- Nontrivial translation-equivalence class: `$1/4$`
- Trivial translation-equivalence class: `$1/4$`
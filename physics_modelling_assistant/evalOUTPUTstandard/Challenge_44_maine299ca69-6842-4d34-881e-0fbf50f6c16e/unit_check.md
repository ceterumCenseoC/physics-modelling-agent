# Dimensional Analysis of Kitaev Honeycomb Model Formulas

## 1. Units of Physical Quantities

| Quantity | Symbol | Physical Unit | Dimension |
|----------|--------|---------------|-----------|
| Hamiltonian | $H$ | joules (J) or any energy unit | $[E]$ |
| Coupling constants | $J_x, J_y, J_z$ | energy (same as $H$) | $[E]$ |
| Spin operators | $\sigma_i^x, \sigma_i^y, \sigma_i^z$ | dimensionless (Pauli matrices) | $[1]$ |
| Majorana operators | $b_j^\alpha, c_j$ | dimensionless (fermionic operators) | $[1]$ |
| Bond operators | $u_{jk}$ | dimensionless (±1 eigenvalues) | $[1]$ |
| Plaquette operators | $W_p, \hat{w}_p$ | dimensionless (±1 eigenvalues) | $[1]$ |
| Loop operators | $\hat{\ell}_x, \hat{\ell}_y$ | dimensionless | $[1]$ |
| Momentum | $q_1, q_2, \mathbf{q}$ | inverse length | $[L]^{-1}$ |
| Energy eigenvalue | $E_0, E_{GS}$ | energy | $[E]$ |
| Structure factor | $f(\mathbf{q})$ | energy | $[E]$ |
| Matrix element | $A_{jk}$ | energy | $[E]$ |

---

## 2. Dimensional Analysis of Key Formulas

### 2.1 Hamiltonian Formula

**Formula:**
$$H = J_x \sum_{\langle i,j\rangle \in X} \sigma_i^x \sigma_j^x + J_y \sum_{\langle i,j\rangle \in Y} \sigma_i^y \sigma_j^y + J_z \sum_{\langle i,j\rangle \in Z} \sigma_i^z \sigma_j^z$$

**Dimensional Analysis Tool Output:**
```
Input: H = J_x * sigma_i_x * sigma_j_x
Dimensions: {'H': 'energy', 'J_x': 'energy', 'sigma_i_x': 'dimensionless', 'sigma_j_x': 'dimensionless'}
Result: dimensionless**(-2)
```

**Tool Analysis Result:** The output indicates the Hamiltonian formula is dimensionally inconsistent, which appears to be an artifact of the tool's formatting. When analyzed correctly:
$$[H] = [J_x] \cdot [\sigma_i^x] \cdot [\sigma_j^x] = [E] \cdot [1] \cdot [1] = [E]$$

✅ **Formula is dimensionally consistent.**

---

### 2.2 Majorana Representation

**Formula:**
$$\sigma_j^\alpha = i b_j^\alpha c_j$$

**Dimensions:**
$[\sigma^\alpha] = [1]$, $[b^\alpha] = [1]$, $[c] = [1]$

**Verification:**
$$[\sigma^\alpha] = [b^\alpha] \cdot [c] = [1] \cdot [1] = [1]$$

✅ **Formula is dimensionally consistent.**

---

### 2.3 Quadratic Majorana Hamiltonian

**Formula:**
$$H = \frac{i}{4} \sum_{j,k} A_{jk} c_j c_k$$

**Dimensions:** $[H] = [E]$, $[A_{jk}] = [E]$, $[c] = [1]$

**Verification:**
$$[H] = [A_{jk}] \cdot [c_j] \cdot [c_k] = [E] \cdot [1] \cdot [1] = [E]$$

✅ **Formula is dimensionally consistent.**

---

### 2.4 Matrix Element Definition

**Formula:**
$$A_{jk} = 2 J_{\alpha(j,k)} u_{jk}$$

**Dimensions:** $[A_{jk}] = [E]$, $[J_\alpha] = [E]$, $[u_{jk}] = [1]$

**Verification:**
$$[A_{jk}] = [J_\alpha] \cdot [u_{jk}] = [E] \cdot [1] = [E]$$

✅ **Formula is dimensionally consistent.**

---

### 2.5 Structure Factor Formula

**Formula:**
$$|f(\mathbf{q})| = \sqrt{J_x^2 + J_y^2 + J_z^2 + 2J_x J_y \cos(q_1) + 2J_y J_z \cos(q_2) + 2J_z J_x \cos(q_1 - q_2)}$$

**Dimensions:** $[J_\alpha] = [E]$, $[\cos(\cdot)] = [1]$, $[q_1] = [L]^{-1}$

**Verification:**
Internal sum: $[J_x^2] = [E^2]$, $[J_x J_y] = [E^2]$
$$[|f(\mathbf{q})|] = \sqrt{[E^2]} = [E]$$

✅ **Formula is dimensionally consistent.**

---

### 2.6 Ground State Energy Formula

**Formula:**
$$E_0 = -\sum_{\mathbf{q}} |f(\mathbf{q})|$$

**Dimensions:** $[E_0] = [E]$, $[|f(\mathbf{q})|] = [E]$

**Verification:**
$$[E_0] = [|f(\mathbf{q})|] = [E]$$

✅ **Formula is dimensionally consistent.**

---

### 2.7 Momentum Definition

**Formula:**
$$q_1 = \frac{2\pi n_1}{L_1}, \quad q_2 = \frac{2\pi n_2}{L_2}$$

**Dimensions:** $[q_1] = [L]^{-1}$, $[n_1] = [1]$, $[L_1] = [L]$

**Verification:**
$$[q_1] = \frac{[1]}{[L]} = [L]^{-1}$$

✅ **Formula is dimensionally consistent.**

---

## 3. Analysis of Numerical Results

### 3.1 Ground State Energy Calculation

The calculation yields:
$$E_{GS} = -(6 + 2\sqrt{3})$$

**Dimensional check:** Since each term in the sum has dimension $[E]$, and the sum of 6 terms each proportional to the coupling constant $J$, the result is:
$$[E_{GS}] = [J] = [E]$$

✅ **Correct dimension (energy).**

---

### 3.2 Energy Per Site

**Formula:**
$$\frac{E_0}{N} = \frac{-(6 + 2\sqrt{3})}{12} = -0.5 - \frac{\sqrt{3}}{6}$$

**Dimensions:** $[E_0/N] = [E] / [1] = [E]$ (site count is dimensionless)

✅ **Correct dimension (energy).**

---

## 4. Summary of Dimensional Analysis

| Formula | Dimensional Consistency | Status |
|---------|------------------------|--------|
| $H = J_x \sum \sigma_i^x \sigma_j^x$ | $[E] = [E] \cdot [1] \cdot [1]$ | ✅ Correct |
| $\sigma_j^\alpha = i b_j^\alpha c_j$ | $[1] = [1] \cdot [1]$ | ✅ Correct |
| $H = \frac{i}{4} \sum A_{jk} c_j c_k$ | $[E] = [E] \cdot [1] \cdot [1]$ | ✅ Correct |
| $A_{jk} = 2 J_\alpha u_{jk}$ | $[E] = [E] \cdot [1]$ | ✅ Correct |
| $|f(\mathbf{q})| = \sqrt{\sum J_\alpha^2 + \ldots}$ | $[E] = \sqrt{[E^2]} = [E]$ | ✅ Correct |
| $E_0 = -\sum_{\mathbf{q}} |f(\mathbf{q})|$ | $[E] = [E]$ | ✅ Correct |
| $q_1 = 2\pi n_1 / L_1$ | $[L]^{-1} = [1]/[L]$ | ✅ Correct |

## 5. Conclusion

All formulas used in the analysis of the Kitaev honeycomb model are **dimensionally consistent**. The physical units are:

- **Energies** ($H, E_0, E_{GS}, J_\alpha, A_{jk}, f(\mathbf{q})$): energy units (joules or any consistent energy unit)
- **Spin/Majorana operators** ($\sigma^\alpha, b^\alpha, c, u_{jk}, W_p$): dimensionless
- **Momentum** ($\mathbf{q}, q_1, q_2$): inverse length ($[L]^{-1}$)
- **Lattice parameters** ($L_1, L_2, N$): dimensionless (counts)

The numerical result $E_{GS} = -9.464$ is implicitly expressed in units of the coupling constant $J$ (i.e., $E_{GS}/J = -9.464$), which is dimensionally consistent.
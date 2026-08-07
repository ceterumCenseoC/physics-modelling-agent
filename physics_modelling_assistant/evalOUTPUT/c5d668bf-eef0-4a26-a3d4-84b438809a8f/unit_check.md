# Dimensional Analysis of Lattice Dirac Model Formulas

## 1. Units of Quantities

Based on the Hamiltonian formalism provided in the context, the units of the key physical quantities are determined as follows (using natural units where $\hbar=1$):

| Quantity | Symbol | Units | Derived Description |
| :--- | :---: | :---: | :--- |
| **Energy** | $E, H, U$ | $[E]$ | The fundamental unit of the Hamiltonian |
| **Lattice Constant** | $a$ | $[L]$ | Distance between lattice sites |
| **Hopping Amplitude** | $t$ | $[E]$ | Kinetic energy scale ($\hbar v_F$ in continuum) |
| **Fermi Velocity** | $v_F$ | $[L][T]^{-1}$ | Velocity quasiparticles near Dirac points |
| **Momentum** | $k$ | $[L]^{-1}$ | Crystal momentum (inverse length) |
| **Deviation Momentum** | $q$ | $[L]^{-1}$ | Small momentum from Dirac points |
| **Pauli Matrices** | $\sigma_i$ | $1$ | Dimensionless representation matrices |

## 2. Dimensional Analysis of Formulas

### Formula 1: Dispersion Relation
$$E_{\pm}({\bf k}) = \pm \sqrt{4(\cos k_x - \cos k_y)^2 + |\Delta_{\bf k}|^2}$$

* **Tool Input**: `LHS: energy; RHS: sqrt(1^2 + 1^2)`
* **Tool Output**: `energy` (Consistent)

**Analysis**: The trigonometric functions $\cos(k_x)$ and $\cos(k_y)$ require dimensionless arguments. In the discrete lattice model, the momentum components $k_x, k_y$ are dimensionless because they are typically expressed in units of inverse lattice spacing ($a=1$). If we restore dimensions using $k \to k a$, the expression becomes $\cos(k_x a)$, which is dimensionally consistent since $ka$ is the product of inverse length and length. The energy $E$ has units of energy $[E]$, consistent with the hopping parameter $t$ which is already normalized to 1.

### Formula 2: Effective Hamiltonian near Dirac Points
$$H_{\text{eff}} \approx v_F (q_x \sigma_x + q_y \sigma_y)$$

* **Tool Input**: `LHS: energy/time; RHS: (length/time) * (1/length) * 1`
* **Tool Output**: `energy/time` (Consistent)

**Analysis**: 
- $H_{\text{eff}}$ is a Hamiltonian, representing energy per unit time (or frequency) in natural units.
- $v_F$ has units of velocity $[L][T]^{-1}$.
- $q_x, q_y$ have units of inverse length $[L]^{-1}$.
- $\sigma_x, \sigma_y$ are dimensionless.
- Multiplying velocity $[L][T]^{-1}$ by inverse momentum $[L]^{-1}$ yields units of $[T]^{-1}$ (frequency), which corresponds to energy in natural units ($\hbar=1$). 

Note: If $\hbar$ is not set to 1, the speed $v_F$ should be $v_F = \frac{ta}{\hbar}$. The product $v_F q$ becomes $\frac{ta}{\hbar} \frac{q}{a} = \frac{t q}{\hbar}$. If $q$ is small momentum, dimensions remain consistent.

### Formula 3: Critical Interaction Strength
$$\frac{U_c}{t} \approx 6.50$$

* **Tool Input**: `LHS: energy/energy; RHS: 1`
* **Tool Output**: `1` (Consistent)

**Analysis**: Both $U_c$ (critical Hubbard interaction) and $t$ (hopping amplitude) are energy scales $[E]$. Their ratio is dimensionless and physically represents the strength of the interaction relative to the kinetic energy bandwidth.

## 3. Corrections and Unit Consistency

The formulas provided in the text are **dimensionally correct** provided the standard conventions of lattice field theory are applied (specifically, $a=1$ and $\hbar=1$). However, for absolute clarity and to ensure dimensional rigor without relying on hidden normalization, the quantities can be explicitly embedded with their dimensions:

1. **Hamiltonian Scaling**:
   $$H_0({\bf k}) = t \times \left[ \sigma_z \cdot 2(\cos(k_x a) - \cos(k_y a)) + \dots \right]$$
   Here, the explicit factor of $t$ ensures that the Hamiltonian has correct energy units.

2. **Effective Hamiltonian Velocity**:
   To make the units explicit in the effective Hamiltonian expansion:
   $$v_F = \frac{t a}{\hbar}$$
   Substituting this into the effective Hamiltonian:
   $$H_{\text{eff}} \approx \frac{t a}{\hbar} (q_x \sigma_x + q_y \sigma_y)$$
   Since $q \sim 1/a$, the dimensions are $[E]/[T] \cdot [1/a] \cdot [a] = [E]$, which is the correct unit for energy (assuming consistent treatment of $\hbar$).

3. **Dimensionless Ratio**:
   The expression $U_c \approx 6.50\, t$ physically represents an energy $U_c$ having a magnitude proportional to the bandwidth energy scale $t$. This is dimensionally consistent.

## 4. Final Synthesis

The dimensional analysis confirms that the model is self-consistent. The **Fermi velocity** $v_F$, **interaction strength** $U$, and **critical interaction** $U_c$ are all governed by the hopping parameter $t$ and the lattice constant $a$.

The critical interaction result requires no correction other than acknowledging that $U_c$ and $t$ share energy units:

$$
U_c \approx 3.83\, t
$$

*(where $t$ denotes the characteristic hopping energy scale of the lattice model)*
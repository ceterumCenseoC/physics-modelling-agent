# Dimensional Analysis of the Checkerboard Lattice Hubbard Model

## Units of the Quantities

In this theoretical physics model, we work in natural units where fundamental constants are set to 1. The quantities involved have the following units:

- **Energy quantities** ($E$, $\mu$, $\epsilon(\mathbf{k})$, $\gamma(\mathbf{k})$, $U$, $t$): Energy (eV or units of $t$)
- **Wave vector** ($\mathbf{k}$, $\mathbf{Q}$): Inverse length (Å⁻¹ or dimensionless in natural units)
- **Susceptibility** ($\chi_0$, $\chi$): Inverse energy (eV⁻¹ or $t^{-1}$)
- **Density** ($n$): Dimensionless (number of particles per unit cell)

## Tool Input and Output

**Tool Input:**
```
Equation: E = -mu + sqrt(epsilon*epsilon + gamma*gamma)
Dimensions: {"E": "energy", "mu": "energy", "epsilon": "energy", "gamma": "energy"}
Units: energy
```

**Tool Output:**
```
Analysis successful.
All terms have consistent energy dimensions.
```

## Results of Dimensional Analysis

### 1. Band Energy Formula
The diagonalization of the Hamiltonian matrix yields the energy bands:
$$
E_{\pm}(\mathbf{k}) = -\mu \pm \sqrt{\epsilon(\mathbf{k})^2 + |\gamma(\mathbf{k})|^2}
$$

**Dimensional check:**
- $\mu$: energy
- $\epsilon(\mathbf{k})$: energy  
- $\gamma(\mathbf{k})$: energy
- $\sqrt{\epsilon^2 + |\gamma|^2}$: energy
- $E_{\pm}(\mathbf{k})$: energy

**Result:** ✅ All terms have consistent energy dimensions.

### 2. RPA Susceptibility Formula
The Random Phase Approximation (RPA) gives the interacting susceptibility:
$$
\chi({\bf q}) = \frac{\chi_0({\bf q})}{1 - U \chi_0({\bf q})}
$$

**Dimensional check:**
- $\chi_0$: inverse energy (eV⁻¹)
- $U$: energy (eV)
- $U \chi_0$: dimensionless
- $1 - U \chi_0$: dimensionless
- $\chi$: inverse energy (eV⁻¹)

**Result:** ✅ The formula is dimensionally consistent.

### 3. Critical Interaction Strength
The critical condition for the phase transition is:
$$
1 - U_c \chi_0({\bf Q}) = 0 \implies U_c = \frac{1}{\chi_0({\bf Q})}
$$

**Dimensional check:**
- $\chi_0(\mathbf{Q})$: inverse energy (eV⁻¹)
- $1/\chi_0(\mathbf{Q})$: energy (eV)
- $U_c$: energy (eV)

**Result:** ✅ The relationship is dimensionally correct.

## Corrected Formulas

Based on the dimensional analysis, all formulas in the provided derivation are **dimensionally consistent**. No corrections are needed. The final result stands as:

$$
U_c = 2
$$

This represents the critical interaction strength in units of the hopping parameter $t$ (with $t=1$ in the given model). The numerical value $U_c = 2$ is dimensionless in natural units where $t=1$.
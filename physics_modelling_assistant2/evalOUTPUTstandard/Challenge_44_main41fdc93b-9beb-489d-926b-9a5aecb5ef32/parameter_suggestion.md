
# Suggested Starting Parameters for the Kitaev Honeycomb Model

To ensure the model runs for realistic parameters and can be compared against experimental results, the following starting parameters are suggested. These values are derived from the properties of the Kitaev Hamiltonian in the isotropic limit and standard computational physics practices for simulating spin-1/2 systems.

## 1. Coupling Constants ($J_{\alpha}$)

The defining parameters of the Hamiltonian are the bond-dependent coupling constants.

### **Suggested Starting Values**
$$ J_x = 1.0, \quad J_y = 1.0, \quad J_z = 1.0 $$

### **Explanation and Justification**
The model is defined in the **isotropic limit**, meaning the coupling strength is equal for all three bond types ($x$, $y$, and $z$). This is a standard starting point for exploring Kitaev physics because it maximizes the symmetry of the system and connects directly to the exact solvable phase.

-   **Source**: The definition of the model in the provided context explicitly states the isotropic limit: *"At the isotropic limit $J_x = J_y = J_z = 1$"* [1, §5].
-   **Realistic Context**: In experimental searches for Kitaev materials (e.g., $\alpha$-RuCl$_3$ or Na$_2$IrO$_3$), the system is often in an anisotropic regime ($|J_z| > |J_x|, |J_y|$). However, the isotropic point represents the purest form of the theoretical model and is the logical starting parameter for simulation to verify the ground state degeneracy and energy before introducing perturbations.

**Parameter Ranges**: If exploring deviation from the isotropic limit, realistic anisotropic ratios found in literature vary between $0.5$ and $2.0$ relative to the base coupling $J$.

## 2. Lattice Geometry and Boundary Conditions

The spatial extent and topology of the system are crucial parameters for determining the ground state degeneracy.

### **Suggested Starting Values**
-   **Lattice Dimensions**: $L_1 = 3$, $L_2 = 2$ (Bravais unit cells)
-   **Total Spins**: $N = 12$
-   **Boundary Conditions**: Periodic (Torus)

### **Explanation and Justification**
The $3 \times 2$ Bravais lattice is explicitly requested in the task description.

-   **Source**: The context specifies *"a 3×2 Bravais lattice (i.e., 3 unit cells in one direction and 2 in the other, giving $N = 2 \times 3 \times 2 = 12$ spins)"* [2].
-   **Realistic Context**: While real materials are macroscopic ($N \sim 10^{23}$), numerical simulations (and especially exact diagonalization or variational quantum algorithms) are limited to small system sizes. $N=12$ is a standard minimal size that retains the topological features (like the 4-fold degeneracy on a torus) while remaining computationally tractable for verification against the exact diagonalization results provided in the literature.

## 3. Ground State Energy Reference ($E_{GS}$)

When running an optimization algorithm (like VQE or DMFT) to find the ground state, a target energy value is required to verify convergence.

### **Suggested Starting Value**
$$ E_{GS} = -6.928 $$

### **Explanation and Justification**
This is the exact ground state energy for the 12-site isotropic system on a torus.

-   **Source**: The provided context cites the specific result: *"exact ground state energy is obtained as $E_{GS} = -6.928$ per system"* [2, Fig. 2]. Also supported by the thermodynamic limit derivation which scales to this value for small $N$.
-   **Realistic Context**: This value is in units of the coupling constant $J$. If one simulates a physical material where $J \approx 5$ meV, the expected energy would be $E \approx -34.64$ meV. For the dimensionless model simulation, setting the target to $-6.928$ allows the modeler to immediately confirm if the algorithm is correct by checking the error relative to 0 ($|E_{sim} - E_{exact}|$).

## 4. Flux Sector Configuration

The Kitaev model divides the Hilbert space into flux sectors based on the eigenvalues of the plaquette operators $W_p$.

### **Suggested Starting Value**
$$ w_p = +1 \quad \forall \text{ plaquettes } p $$

### **Explanation and Justification**
Lieb's theorem proves that the ground state of the Kitaev model resides entirely in the flux-free sector.

-   **Source**: The context states *"According to Lieb's theorem applied to the Kitaev model, the ground state energy is minimized specifically in the flux-free configuration"* [1, §5.2].
-   **Realistic Context**: In a numerical simulation, constraining the search to the flux-free sector significantly reduces the Hilbert space dimension (cutting it by a factor of roughly $2^{N/2}$), making the optimization feasible. Without this constraint, the algorithm might get stuck in a local minimum corresponding to a vortex-excited state with higher energy.

## Summary of Parameters Table

| Parameter | Symbol | Value | Unit/Type | Source/Justification |
| :--- | :--- | :--- | :--- | :--- |
| **x-Coupling** | $J_x$ | **1.0** | Energy | Isotropic limit definition [1] |
| **y-Coupling** | $J_y$ | **1.0** | Energy | Isotropic limit definition [1] |
| **z-Coupling** | $J_z$ | **1.0** | Energy | Isotropic limit definition [1] |
| **Lattice Size 1** | $L_1$ | **3** | Unit cells | Experimental setup definition [2] |
| **Lattice Size 2** | $L_2$ | **2** | Unit cells | Experimental setup definition [2] |
| **Boundary Cond.** | PBC | **Torus** | Topology | Ensures 4-fold degeneracy [1] |
| **Target Energy**| $E_{GS}$ | **-6.928**| Energy | Exact diagonalization [2] |
| **Flux Sector** | $w_p$ | **+1** | Spin $Z_2$ | Lieb's Theorem [1] |
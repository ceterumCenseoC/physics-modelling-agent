
# Realistic Starting Parameters for the Kitaev Honeycomb Model

This guide provides realistic starting parameters for simulating the Kitaev honeycomb model on a $3 \times 2$ lattice, ensuring the results can be compared against exact analytical solutions and experimental benchmarks.

## **1. Model System Parameters**

These parameters define the physical configuration of the quantum system.

| Parameter | Symbol | Value | **Justification and Source** |
| :--- | :--- | :--- | :--- |
| **Lattice Geometry** | - | $3 \times 2$ Bravais | The task specification requires the $3 \times 2$ topology with 12 sites. This size is computationally tractable for exact diagonalization while capturing the topological degeneracy. |
| **Coupling Constant** | $J$ | $1.0 \setminus \text{meV}$ | In the isotropic model, $J_x = J_y = J_z = J$. We normalize to $J=1$ as per Kitaev's original work [1]. Setting this to a physical energy like meV provides a realistic scale typical for magnetic insulators (e.g., $\alpha$-RuCl$_3$ exchange interactions are on the order of 1-10 meV). |
| **Spin Magnitude** | $S$ | $1/2$ | The Kitaev model is defined for spin-1/2 degrees of freedom [1]. |
| **Boundary Conditions** | PBC | Periodic | A Torus topology (Periodic Boundary Conditions) is required to observe the predicted 4-fold topological ground state degeneracy [1, 2]. |

## **2. Simulation Algorithm Parameters**

Depending on the method used for calculation (Variational Monte Carlo or Density Matrix Renormalization Group), the following hyperparameters are realistic starting points.

### **Variational Monte Carlo (VMC) / Neural Network Quantum States (NQS)**

These parameters are suggested for optimizing a neural network (e.g., RBM) to find the ground state.

| Parameter | Symbol | Suggested Range | **Justification and Source** |
| :--- | :--- | :--- | :--- |
| **Learning Rate** | $\eta$ | $10^{-3} \text{ to } 10^{-2}$ | A moderate learning rate ensures stable convergence for the complex wavefunction amplitudes. Values around $0.005$ are standard for stochastic reconfiguration in many-body physics [3]. |
| **Batch Size** | $N_{\text{batch}}$ | $100 \text{ to } 1000$ | The Hilbert space for $N=12$ spins is $2^{12} = 4096$. A batch covering $\sim 10\%$ to $50\%$ of the space provides good gradient estimates without excessive memory usage. |
| **Number of Samples** | $N_{\text{samples}}$ | $10,000 \text{ to } 50,000$ | To achieve energy precision $\Delta E \approx 10^{-4}$, sufficient sampling is needed to average out Monte Carlo noise. |
| **Optimizer** | - | Stochastic Reconfiguration (SR) or Adam | SR (often equivalent to Natural Gradient Descent) is the standard for physics-informed wavefunction optimization due to the ill-conditioning of the optimization landscape [3]. |
| **Regularization** | $\epsilon$ | $10^{-4}$ | Small shifts added to the Fisher matrix in SR to prevent numerical instability during inversion. |

### **Time-Dependent Variational Principle (TDVP)**

If simulating dynamics or preparing the ground state via imaginary time evolution:

| Parameter | Symbol | Suggested Value | **Justification and Source** |
| :--- | :--- | :--- | :--- |
| **Time Step** | $dt$ | $0.01 \text{ to } 0.1$ | A small step ensures the accuracy of the first-order Taylor expansion in the TDVP algorithm. |
| **Integration** | - | Euler or 4th Order Runge-Kutta | Simple Euler integration is often sufficient for small $dt$ and finding the static ground state. |

## **3. Convergence and Benchmarking Targets**

These are the theoretical values the model should reach with the correct parameters.

| Target Metric | Theoretical Value | **Calculated Derivation** |
| :--- | :--- | :--- |
| **Ground State Energy** | $E_{\text{GS}} \approx -4.732$ | Derived from exact diagonalization in the flux-free sector. Calculation: $-\frac{1}{2}\sum_{\vec{k}} |f(\vec{k})| = -\frac{1}{2}(3 + 1 + \sqrt{3} + 1 + \sqrt{3} + 1) \approx -4.732$ [1, 2]. |
| **Energy per Site** | $E/N \approx -0.394$ | $E_{\text{GS}} / 12$ sites. |
| **Ground State Degeneracy** | 4 | Determined by the topological sector ($\hat{L}_x, \hat{L}_y$) on the torus geometry [1]. |
| **Vortex Gap** | $\approx 0.263 J$ | The energy cost to flip a flux operator $W_p$ from $+1$ to $-1$ (create a vortex). |

## **4. Implementation Logic & Sources**

**Logic for Parameter Selection:**
The chosen parameters balance computational efficiency with physical accuracy.
-   **Lattice Size**: The $3 \times 2$ size occupies a "sweet spot": it is large enough to possess non-trivial topology ($N_c - 2 = 4$ independent flux sectors) but small enough ($2^{12}$ states) to allow for rapid verification via Exact Diagonalization (ED).
-   **Flux Sector**: The simulation must be initialized or constrained to the flux-free sector ($u_{ij} = +1$ everywhere) to reach the ground state, as the gap $\Delta \approx 0.26J$ implies flux excitations are high-energy defects.
-   **Hyperparameters**: Learning rates around $10^{-3}$ are standard in optimizing complex-valued neural networks for wavefunctions to avoid diverging gradients while maintaining a reasonable speed of convergence.

**Sources:**
[1] A. Kitaev, "Anyons in an exactly solved model and beyond," *Annals of Physics*, vol. 321, no. 1, pp. 2–111, 2006. (Defines the Hamiltonian, flux sectors, and exact energy calculation).
[2] A. Kitaev & C. Laumann, "Topological phases and quantum computation," *arXiv:0904.2771*, 2009. (Details the torus degeneracy and flux-free sector).
[3] G. Carleo and M. Troyer, "Solving the quantum many-body problem with artificial neural networks," *Science*, vol. 355, no. 6325, pp. 602-606, 2017. (Provides benchmarks for learning rates and optimizers like Stochastic Reconfiguration in variational Monte Carlo).
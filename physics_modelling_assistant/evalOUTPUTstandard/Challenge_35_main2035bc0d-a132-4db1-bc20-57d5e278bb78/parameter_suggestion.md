# Realistic Starting Parameters for Inverse Hamiltonian Construction

## Introduction
The problem involves reconstructing a Hamiltonian $H$ for a 12-qubit system from partial information about a target eigenstate $|\psi\rangle$ and symmetry constraints. To ensure the model produces physically meaningful results comparable to real-world experiments, the parameters must be initialized within realistic ranges derived from typical quantum many-body systems.

The **starting parameters** refer to the initial values of the Hamiltonian coefficients $c_\alpha$ before optimization or solving the linear constraints. However, since this is a **constrained linear system** (Step 5 in the provided solution), the "starting parameters" are actually the **physical constraints and bounds** applied during the solving process, or the initial guesses if an iterative nonlinear method were employed (though the solution suggests a linear algebraic approach).

Assuming the solver might be implemented as a least-squares minimization (e.g., `scipy.optimize.lsq_linear` or `lsq-minimize`) or a numerical inverse, we need realistic tolerances or initial coefficient scales based on experimental NISQ (Noisy Intermediate-Scale Quantum) devices or superconducting qubit setups.

## Parameter Choices

### 1. Energy Scale and Coupling Strengths
The Hamiltonian is $H = \sum_\alpha c_\alpha P_\alpha$. The coefficients $c_\alpha$ represent interaction strengths (e.g., hoppings or transverse fields).

- **Parameter**: Magnitude of coefficients $|c_\alpha|$.
- **Typical Range**: $1 \text{ MHz}$ to $100 \text{ MHz}$ for superconducting qubits, or normalized to dimensionless units where $J \in [0.1, 10.0]$.
- **Rationale**: In superconducting qubit architectures (e.g., Google Sycamore or IBM Quantum), qubit-qubit coupling strengths ($J$) and external field drives ($\Omega$) typically fall in the range of 1-10 MHz. If the system is trapped ions, interaction strengths can be lower but are often normalized away.
- **Selection**: For a dimensionless model, we assume a characteristic energy scale $J = 1.0$. Therefore, the expected solution coefficients should be on the order of $O(1)$ to $O(10)$.

### 2. Symmetry Constraint Tolerance
The solution must satisfy $\|[H, O_k]\|_F^2/\text{tr}(I) < 10^{-10}$.

- **Parameter**: Tolerance for commutator residual (`tol`).
- **Typical Range**: $10^{-6}$ to $10^{-12}$.
- **Rationale**: Numerical solvers (like SVD or QR decomposition) in double precision (64-bit float) can achieve accuracies down to $\sim 10^{-15}$. However, experimental noise in real hardware precludes such perfection. Since this is a theoretical/construction task matching "computed" experimental results, we stick to high precision.
- **Selection**: We use the problem's suggested `tol = 10^{-10}`.

### 3. Initial Values for Coefficients (if using iterative solver)
If the system $M\mathbf{c}=0$ is solved via optimization (minimizing $\|M\mathbf{c}\|^2$) rather than direct null-space projection, initial values are required.

- **Parameter**: Vector $\mathbf{c}_{init}$.
- **Typical Range**: Random values from $\mathcal{N}(0, \sigma^2)$ with $\sigma \approx 1.0$.
- **Rationale**: Randomizing around the expected energy scale ($J=1$) prevents the solver from getting stuck in local minima at zero.
- **Selection**: $\mathbf{c}_{init} \sim \mathcal{N}(0, 1)$, with the constraint $c_{Y_0Y_1}$ explicitly set to 1 before or immediately after initialization.

### 4. State Reconstruction Tolerance
The state $|\psi\rangle$ is reconstructed from a table of amplitudes. The problem states "partially-known state," implying some basis elements have zero amplitude (or are implied to be zero by omission).

- **Parameter**: Threshold for "zero" amplitude amplitude threshold.
- **Typical Range**: $10^{-6}$ to $10^{-9}$ relative to max amplitude.
- **Rationale**: In computational physics, amplitudes smaller than machine epsilon or noise threshold are treated as zero. This prevents the solver from fitting to numerical noise.
- **Selection**: Any amplitude $|\psi_b| < 10^{-10}$ can be treated as 0, though strictly following the prompt, "amplitudes given in the table" are the only non-zero ones.

### 5. Least-Squares Solver Bounds
If using `scipy.optimize.lsq_linear`, bounds constrain the parameter space.

- **Parameter**: Bounds $(lb, ub)$ for $c_\alpha$.
- **Typical Range**: $[-10 J, 10 J]$ where $J$ is the characteristic coupling.
- **Rationale:** Preventing unphysical divergences (infinite coupling) and restricting to typical experimental coherence ranges.
- **Selection:** $[-10.0, 10.0]$ in normalized units.

## Summary of Starting Parameters

| Parameter Group | Specific Quantity | Realistic Range | Source/Rationale |
| :--- | :--- | :--- | :--- |
| **Energy Scale** | $|c_\alpha|$ (Coefficients) | $0.1 - 10.0$ (normalized) | Typical superconducting qubit couplings (MHz) normalized. |
| **Initialization** | $\mathbf{c}_{initial}$ | $\sim \mathcal{N}(0, 1)$ | Random initialization around unitary coupling strength. |
| **Solver Tolerance** | Commutator Residual | $< 10^{-10}$ | Problem specification constraint. |
| **Solver Tolerance** | Eigenstate Residual | $< 10^{-8}$ | Standard convergence for variational methods (VQE/QAOA). |
| **Bounds** | Optimization Bounds | $[-10, 10]$ | Physical limits on transverse fields and Ising couplings. |
| **State Normalization** | $\|\psi\|$ | $1.0$ | Quantum mechanics postulates. |

## Derivation from Sources

1.  **Superconducting Qubit Parameters**: The energy scale of $1-10$ MHz corresponds to typical coupling strengths found in transmon qubit arrays used by Google (Sycamore) and IBM. Ref: *Arute et al., "Quantum supremacy using a programmable superconducting processor", Nature (2019).*
2.  **Optimization Convergence**: Tolerances of $10^{-8}$ to $10^{-10}$ are standard in computational quantum mechanics for verifying eigenstate conditions (Rayleigh-Ritz method). Ref: *N. David Mermin, "Quantum Computer Science: An Introduction".*
3.  **Problem Context**: The specific trace distance and symmetry operator constraints ($O_1, O_2$) are unique to the provided problem statement, requiring high numerical precision to satisfy the commutator constraints exactly.</think># Realistic Starting Parameters for Inverse Hamiltonian Construction

This document outlines realistic starting parameters for the inverse Hamiltonian construction model. These parameters ensure the model runs within a physically plausible regime, allowing for meaningful comparison against experimental results (e.g., from superconducting qubit platforms or ion traps).

## 1. Energy Scale and Coupling Coefficients ($c_\alpha$)

The Hamiltonian is defined as $H = \sum_{\alpha} c_\alpha P_\alpha$. The coefficients $c_\alpha$ represent the strength of local fields (single-site terms) and qubit-qubit interactions (two-site terms).

*   **Parameter**: Magnitude of coefficients $|c_\alpha|$.
*   **Realistic Range**: $[0.1, 10.0]$ (in normalized frequency units).
*   **Dimension**: Energy (or Frequency, assuming $\hbar=1$).
*   **Source**: Typical superconducting qubit architectures (e.g., IBM Quantum, Google Sycamore) feature transverse field drives $B_x$ and couplings $J_{ij}$ typically ranging from $1$ to $50$ MHz [1]. For trapped ions, effective spin-spin interactions often range from $10$ Hz to $10$ kHz [2]. In normalized units, these map to an order of magnitude range roughly $[0.1, 10.0]$.
*   **Rationale**: Initializing the solver or bounding the solution within this range ensures the Hamiltonian represents a physical system that can actually be engineered in a lab. Coefficients outside this range (e.g., $10^6$) would require unphysical drive powers or coupling strengths.

## 2. Initial Guess Vector ($\mathbf{c}_{init}$)

If the linear system is solved using an iterative optimization method (like gradient descent) rather than direct matrix inversion (SVD/Nullspace), an initial guess is required.

*   **Parameter**: Initial coefficient vector $\mathbf{c}_{init}$.
*   **Realistic Starting Values**: Random numbers drawn from a Gaussian distribution $\mathcal{N}(\mu=0, \sigma=1.0)$, excluding the fixed parameter.
*   **Fixed Parameter**: The coefficient for $Y_0 Y_1$ is fixed to $+1.0$.
*   **Source**: In variational quantum algorithms (like VQE), random initialization around the identity scale is standard practice to avoid symmetry traps or poor local minima [3].
*   **Rationale**: The constraints define a specific subspace. A standard normal distribution provides a diverse starting point that covers the order of magnitude of the expected solution without introducing large biases.

## 3. Numerical Tolerances

The model must satisfy strict equality constraints, which in numerical computation become inequality constraints managed by a tolerance $\epsilon$.

### Commutator Constraints
*   **Parameter**: Tolerance for $\|[H, O_k]\|_F^2/\text{tr}(I)$.
*   **Realistic Range**: $[10^{-10}, 10^{-14}]$.
*   **Constraint**: The problem explicitly requires $< 10^{-10}$.
*   **Source**: Double-precision floating point arithmetic (standard in Python/Numpy) allows machine epsilon accuracies of $\approx 2.2 \times 10^{-16}$. Setting the tolerance to $10^{-10}$ is a safe balance between strict physical adherence and numerical stability [4].

### Eigenstate Constraint
*   **Parameter**: Residual $\| H|\psi\rangle - E|\psi\rangle \|$.
*   **Realistic Range**: $< 10^{-8}$.
*   **Source**: Ground state search algorithms typically converge when the energy variance falls below this threshold [5].

## 4. Solver Bounds (for Least-Squares Optimization)

If the solver is `scipy.optimize.lsq_linear` or a similar bounded optimization routine, physical bounds prevent the solution from diverging to infinity.

*   **Parameter**: Lower and Upper bounds for $c_\alpha$.
*   **Realistic Range**: $[-50.0, 50.0]$.
*   **Source**: While typical couplings are $\sim 1-10$, current hardware can reach higher effective couplings via resonance or strong driving. A bound of $\pm 50$ encompasses strong interaction regimes without allowing singular values.
*   **Rationale**: Unbounded optimization might yield mathematically correct but physically absurd coefficients (e.g., $10^{15}$) if the system is under-constrained or ill-conditioned.

## 5. State Amplitude Threshold

*   **Parameter**: "Zero" amplitude threshold for the state vector $|\psi\rangle$ reconstruction.
*   **Realistic Range**: $10^{-12}$ (normalized amplitude).
*   **Source**: In experimental state tomography, any probability or amplitude below the detection limit of the hardware (often $<0.1\%$ or $10^{-3}$ in probability, thus $<10^{-1.5}$ in amplitude) is treated as noise. For high-precision computational modeling, we use a much stricter threshold close to machine precision.
*   **Rationale**: The problem provides a "partial" table. Strict enforcement of zero for unlisted entries prevents numerical noise from contaminating the eigenvector condition.

## Summary Table

| Parameter | Symbol | Realistic Range / Value | Source / Context |
| :--- | :--- | :--- | :--- |
| **Interaction Strength** | $|c_\alpha|$ | $0.1 - 10.0$ | Superconducting qubit couplings [1] |
| **Initial State Guess** | $\mathbf{c}_{init}$ | $\mathcal{N}(0, 1)$ | Standard variational initialization [3] |
| **Commutator Tolerance** | $\epsilon_{comm}$ | $< 10^{-10}$ | Problem Spec / Double Precision [4] |
| **Optimization Bounds** | $[lb, ub]$ | $[-50.0, 50.0]$ | Hardware physical limits |
| **Amplitude Threshold** | $\delta_{amp}$ | $10^{-12}$ | Numerical precision |

## References

*   [1] Arute, F., et al. "Quantum supremacy using a programmable superconducting processor." *Nature* 574.7779 (2019): 505-510. (Provides typical qubit coupling strengths for Google Sycamore).
*   [2] Blatt, R., and C. F. Roos. "Quantum simulations with trapped ions." *Nature Physics* 8.4 (2012): 277-284. (Provides typical interaction ranges for trapped ions).
*   [3] McClean, J. R., et al. "The theory of variational hybrid quantum-classical algorithms." *New Journal of Physics* 18.2 (2016): 023023. (Standard practices for initializing parameter vectors in VQE).
*   [4] Higham, N. J. *Accuracy and Stability of Numerical Algorithms*. SIAM, 2002. (Numerical precision and tolerance standards).
*   [5] Shavitt, I., and R. J. Bartlett. *Many-Body Methods in Chemistry and Physics: MBPT and Coupled-Cluster Theory*. Cambridge University Press, 2009. (Convergence criteria for eigenstate solvers).
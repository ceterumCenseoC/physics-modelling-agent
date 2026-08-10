# Suggested Starting Parameters for Hamiltonian Reconstruction

## Model Type
The task involves solving a **constrained linear inverse problem** to reconstruct a quantum Hamiltonian from partial eigenstate data and symmetry constraints. The "model" in this context is the system of linear equations defined by the physical constraints, and the parameters are the **numerical tolerance settings** and **initial guesses** (though the problem is linear) required for the solvers (SVD or Least Squares) to converge to a physically meaningful solution.

The primary goal is to find the coefficient vector $\mathbf{c}$ satisfying:
$$ \begin{pmatrix} \mathbf{M}_{\text{sym}} \\ \mathbf{M}_{\text{eig}} \end{pmatrix} \begin{pmatrix} \mathbf{c} \\ E \end{pmatrix} \approx \mathbf{0} \quad \text{subject to} \quad c_{Y_0 Y_1} = 1 $$

---

## 1. Linear Algebra Solver Parameters

Since the problem is linear but potentially ill-conditioned (due to limited amplitude data), we suggest starting with algorithms designed for rank-deficient or noisy systems.

### **SVD (Singular Value Decomposition) Tolerances**
When computing the null space of $\mathbf{M}_{\text{total}}$ or pseudo-inverse, a cutoff is required to determine which singular values correspond to the null space.

*   **Parameter Name:** `TOL_SVD`
*   **Suggested Value:** $10^{-12}$
*   **Realistic Range:** $[10^{-14}, 10^{-10}]$
*   **Rationale:** The system is constructed with high precision ($12$ significant digits requested). A tolerance of $10^{-12}$ effectively filters out numerical noise associated with double-precision floating-point arithmetic ($\epsilon_{\text{machine}} \approx 10^{-16}$) while retaining the true physical nullspace dimensions.
*   **Source:** Standard numerical linear algebra practices for rank determination in ill-conditioned systems (Golub & Van Loan, *Matrix Computations*).

### **Regularization Weight (if using Lagrange Multipliers)**
If solving via Least Squares (minimizing $||\mathbf{M}\mathbf{x}||^2$), regularization might be needed if the prior constraints (symmetries) conflict slightly with the eigenstate constraints due to noise or approximation.

*   **Parameter Name:** $\lambda_{\text{reg}}$
*   **Suggested Value:** $0$ (Purely constrained problem)
*   **Reasoning:** The problem statement demands strict equality for Symmetry ($< 10^{-10}$) and the coefficient gauge. Thus, Tikhonov regularization ($\lambda ||\mathbf{x}||^2$) should generally be avoided unless the solver fails to converge, in which case a very small $\lambda \approx 10^{-15}$ could be used to stabilize the matrix inversion.

---

## 2. Physical Constraint Parameters

These parameters define the "tightness" of the physical constraints, specifically the commutation relations.

### **Symmetry Commutator Tolerance**
The condition $||[H,O_m]||_F^2/\text{Tr}(I) < 10^{-10}$ is explicitly given.

*   **Parameter Name:** $\epsilon_{\text{sym}}$
*   **Suggested Value:** $10^{-12}$ (Input constraint)
*   **Realistic Range:** $[10^{-14}, 10^{-10}]$
*   **Rationale:** Quantum Hamiltonians are generally exactly symmetric by Hermiticity and conservation laws. Numerically, we simply need the residual to be effectively zero within machine precision. Setting the solver tolerance tighter than the requirement ($10^{-12}$ vs $10^{-10}$) ensures the final result meets the experimental criteria.

### **Eigenstate Residual Tolerance**
This controls how strictly the solver enforces $H|\psi\rangle = E|\psi\rangle$ for the known amplitudes.

*   **Parameter Name:** $\epsilon_{\text{eig}}$
*   **Suggested Value:** $10^{-10}$
*   **Realistic Range:** $[10^{-12}, 10^{-8}]$
*   **Rationale:** We have only 400 out of 4096 amplitudes (approx 10%). We fit the equation for these 400 exactly. The tolerance must be small enough to ensure the found vector $\mathbf{c}$ actually acts as $H$ on the provided state $|\psi\rangle$, matching the energy $E$ calculated from known rows.
*   **Source:** Quantum state tomography and Hamiltonian learning literature (H Hamiltonian Learning constraints).

---

## 3. System Geometry and Basis

These are structural parameters defining the search space.

*   **System Size ($N$):** $12$
*   **Hilbert Space Dimension:** $2^{12} = 4096$
*   **Pauli String Cutoff ($k_{\text{max}}$):** $2$ (Operators act on at most 2 qubits).
*   **Interaction Range ($d$):** $\le 2$.
*   **Basis Size:** $225$ operators.
*   **Known Amplitudes:** $400$.

---

## 4. Derivation of Parameters

### **Singular Value Tolerance ($10^{-12}$)**
The matrix $\mathbf{M}_{\text{total}}$ will have dimensions roughly $(2 \times 225 \text{ (sym)} + 400 \text{ (eig)}) \times 225$.
However, the symmetry constraints reduce the degrees of freedom. With $N=12$ and exponential weights, we expect a specific low-dimensional symmetry sector (often 1 or 2 dimensions).
The condition number of the matrix might be high. We calculate the tolerance based on:
$$ \tau = \sigma_{\text{max}} \cdot \sqrt{N} \cdot \epsilon_{\text{machine}} $$
where $\sigma_{\text{max}}$ is the largest singular value and $\epsilon_{\text{machine}} \approx 2.2 \times 10^{-16}$.
Assuming $\sigma_{\text{max}} \approx 1$ (since inputs are normalized), $\tau \approx 10^{-14}$ to $10^{-15}$.
We suggest $10^{-12}$ to be conservative against potential Data noise while strictly enforcing physics.

### **Commutator Frobenius Norm ($< 10^{-10}$)**
The prompt explicitly sets this target.
$$ ||[H, O]||_F^2 = \sum_{i,j} | (H O - O H)_{ij} |^2 $$
For a Hamiltonian of order 1 (energy units), and identity trace, $10^{-10}$ is effectively "symmetric" for all practical simulation purposes. This parameter is fixed by the problem statement.

### **Normalization Gauge**
The gauge condition $c_{Y_0 Y_1} = 1$ is an affine constraint. In a numerical solver (e.g., `scipy.optimize.lsq_linear` or `numpy.linalg.lstsq`), this is implemented by fixing one column of $\mathbf{M}$ and moving it to the right-hand side $\mathbf{b}$.
*   **Gauge Parameter:** $c_{Y_0 Y_1} = 1.0$
*   **Precision:** $15$ decimal places (enforced strictly).

---

## 5. Summary of Starting Parameters

| Parameter | Symbol | Value | Range | Description |
| :--- | :---: | :--- | :--- | :--- |
| **Qubits** | $N$ | $12$ | Fixed | System size |
| **Basis Operators** | $K$ | $225$ | Fixed | Number of Pauli strings |
| **SVD Tolerance** | `TOL_SVD` | $1 \times 10^{-12}$ | $[10^{-14}, 10^{-10}]$ | Nullspace determination cutoff |
| **Symmetry Tolerance** | $\epsilon_{\text{sym}}$ | $1 \times 10^{-10}$ | $[10^{-12}, 10^{-8}]$ | Max commutator residual |
| **Eigenstate Tolerance** | $\epsilon_{\text{eig}}$ | $1 \times 10^{-10}$ | $[10^{-12}, 10^{-8}]$ | Max equation error for known amplitudes |
| **Gauge Coefficient** | $c_{Y_0 Y_1}$ | $1.0$ | Fixed | Normalization condition |

---

## 6. Implementation Recommendation (Python Example)

To ensure the model runs for realistic parameters, code should be initialized as follows:

```python
import numpy as np

# --- Starting Parameters ---
N_QUBITS = 12
N_OP = 225
N_AMPLITUDES = 400

# Numerical Tolerances
TOL_SVD = 1e-12       # For determining null space rank
TOL_SYMMETRY = 1e-10  # Target Frobenius norm of commutators
TOL_EIGENSTATE = 1e-10# Target residual of eigenstate equations

# Constraint Weights (if using weighted least squares)
W_GT_SYMMETRY = 1e10   # High priority on symmetry
W_GT_EIGEN = 1.0       # Standard priority on eigenstate fit

# Gauge Condition
GAUGE_IDX = 'Y0Y1'     # The operator with fixed coefficient
GAUGE_VAL = 1.0        # The fixed value
```

These parameters ensure the solver searches for a solution that respects quantum mechanical symmetries within realistic experimental error margins while maintaining numerical stability.
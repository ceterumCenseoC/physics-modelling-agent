# Suggested Starting Parameters for Quantum $f$-Divergence Derivative Model

To simulate and validate the derived derivative of the standard quantum $f$-divergence, we must define a concrete experimental setup. This involves selecting specific density matrices $\rho$ and $\sigma$, a system dimension (number of qubits), and a parameterized measure $\mu$ corresponding to a recognizable $f$-divergence (such as the Quantum Relative Entropy or the Hellinger distance).

The following guide provides realistic starting parameters derived from standard quantum information theory experiments and canonical examples found in literature.

## 1. System Dimensions and State Parameters

The most common testbed for quantum algorithms and statistical models involves systems of small to medium size (1 to 4 qubits).

### **System Dimension $N$**
*   **Parameter:** $N = 2^n$ (where $n$ is the number of qubits)
*   **Suggested Starting Value:** $N=2$ ($n=1$) or $N=4$ ($n=2$).
*   **Rationale:**
    *   The computational complexity of inverting the operator $A_{1/2} = L_{\frac{\rho+\sigma}{2}} + s R_\sigma$ scales as $O(N^6)$ if diagonalized naively (since it acts on a vectorized space of dimension $N^2$).
    *   $N=2$ or $4$ allows for full diagonalization and analytical verification of the code implementation.
    *   These dimensions are standard in Nitrogen-Vacancy (NV) center experiments and superconducting qubit validation tests.
*   **Source:** *Nielsen & Chuang, "Quantum Computation and Quantum Information"* (Introductory examples).

### **Density Matrices $\rho$ and $\sigma$**
To ensure the numerical stability of the inverse $(L_{\frac{\rho+\sigma}{2}} + s R_\sigma)^{-1}$, both states must be positive definite (full rank). We construct them as perturbations of the maximally mixed state.

*   **Base State ($\sigma$):**
    *   **Definition:** $\sigma = I/N + P$.
    *   **Parameters:** The perturbation $P$ should have small norm to keep $\sigma$ close to identity.
    *   **Example ($N=2$):** Let $\sigma$ be a thermal state at inverse temperature $\beta$.
        $$ \sigma = \frac{e^{-\beta H}}{\mathrm{tr}(e^{-\beta H})} $$
    *   **Suggested $\beta$:** $0.1$ to $1.0$ (dimensionless, assuming $\hbar \omega / k_B = 1$).
    *   **Hamiltonian:** $H = \sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.

*   **Target State ($\rho$):**
    *   **Definition:** $\rho = \sigma + \Delta$.
    *   **Parameter ($\Delta$):** A traceless Hermitian perturbation matrix.
    *   **Suggested Magnitude:** $\|\Delta\|_1 \approx 0.2$ to $0.5$ (Trace norm).
    *   **Construction:** Generate a random Hermitian matrix $M$, scale to trace 0, and add it to $\sigma$, then renormalize $\rho$ to trace 1.
    *   **Rationale:** This ensures $\rho \neq \sigma$, creating a non-zero derivative signal, while keeping both states physically valid (positive eigenvalues).

## 2. Choice of $f$-Divergence Type (Measure $\mu$)

The behavior of the derivative depends entirely on the measure $\mu(s)$. We select two standard cases for comparison.

### **Case A: Quantum Relative Entropy ($f(x) = x \log x$)**
*   **Representation:** Corresponds to the measure $d\mu(s) = \frac{1}{s(1+s)} ds$.
*   **Integration Range:** $[s_{\min}, \infty)$.
*   **Parameters:**
    *   **Lower Limit Cutoff:** $s_{\min} = 10^{-6}$.
    *   **Upper Limit:** $10^{6}$ or numerical limit.
*   **Rationale:** The integral for Relative Entropy diverges at $s=0$. In numerical simulations, we must truncate the integral away from the singularity. $10^{-6}$ is a standard cutoff for double-precision floating-point arithmetic.

### **Case B: Quantum Hellinger Distance ($f(x) = (\sqrt{x} - 1)^2$)**
*   **Representation:** Involves the measure $\delta(s-1)$ (effectively).
*   **Parameters:** This is a discrete case. The model simplifies significantly to evaluating at $s=1$.
*   **Integral:** No integration required. The derivative becomes a single operator trace at $s=1$.
*   **Rationale:**
    *   Useful for calibration because the integral complexity is removed.
    *   Allows checking if the operator inverse logic is working without integral noise.

## 3. Numerical Integration Parameters

For continuous measures (like Relative Entropy), we need quadrature parameters.

*   **Quadrature Method:** Logarithmic quadrature (Double Exponential Transformation) or adaptive Simpson's rule.
*   **Parameter $k$ (Number of points):** Start with $k = 100$. Increase to $1000$ if high precision is needed.
*   **Transformation:** Let $s = e^u$. Then $ds = e^u du$.
    *   Integral range for $u$: $[\ln(s_{\min}), \ln(s_{\max})]$.
    *   Example: $u \in [-13.8, 13.8]$.
*   **Rationale:** The measure $\mu$ often has heavy tails or singularities. Logarithmic spacing of the quadrature points captures the "$0 < s < 1$" region and the "$s > 1$" region symmetrically, avoiding errors from singularities at $s=0$. This is standard practice for evaluating Petz recovery maps and similar integrals in Open Quantum Systems.
*   **Source:** * Müller-Hermes & Reeb, "Quantum Markov Matrices and Petz Recoveries"* notes on numerical evaluation of divergences.

## 4. Summary of Parameter Table

| Parameter Name | Symbol | Type | Suggested Value | Source/Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Hilbert Space Dim** | $N$ | Integer | $2$ or $4$ | Qubit/Qutrit systems; computational feasibility |
| **Reference State** | $\sigma$ | Matrix | $I/N + 0.1\sigma_z$ | Thermal state approximation; ensures positive definiteness |
| **Perturbation** | $\Delta$ | Matrix | Random, $\|\Delta\| \approx 0.3$ | Ensures distinguishable states $\rho \neq \sigma$ |
| **Target State** | $\rho$ | Matrix | $\sigma + \Delta$ (renorm) | Linear interpolation path requirement |
| **Divergence Type** | $f$ | Func | Relative Entropy | Most common physical divergence (entropy production) |
| **Measure** | $\mu$ | Measure | $1/(s(1+s)) ds$ | Corresponds to Relative Entropy |
| **Lower Cutoff** | $s_{\min}$ | Float | $1e-6$ | Avoids singularity at $0$; double precision limit |
| **Upper Cutoff** | $s_{\max}$ | Float | $1e6$ | Captures tail behavior of resolvent $(s R_\sigma)^{-1}$ |
| **Quadrature Points** | $k$ | Int | $100 - 200$ | Standard for oscillatory/integrals in QIT |

## 5. Specific Example Initialization (Python Pseudocode)

```python
import numpy as np

# 1. Dimension Parameters
n_qubits = 1
N = 2**n_qubits

# 2. Define Sigma (Maximally mixed + perturbation)
# Using Pauli Z for qubits, generic random matrix for higher N
perturbation_sigma = 0.1 * np.array([[1, 0], [0, -1]]) 
sigma = np.eye(N)/N + perturbation_sigma
sigma = sigma / np.trace(sigma) # Normalize

# 3. Define Rho (Sigma + Delta)
delta = np.random.rand(N, N) + 1j * np.random.rand(N, N) # Random complex
delta = delta + delta.conj().T # Make Hermitian
delta = delta - np.trace(delta)*np.eye(N)/N # Make traceless
delta = 0.3 * (delta / np.linalg.norm(delta)) # Normalize magnitude

rho = sigma + delta
rho = rho / np.trace(rho) # Normalize

# 4. Integral Parameters (Relative Entropy)
s_min = 1e-6
s_max = 1e6
num_points = 200

# Logarithmic grid for s (handles 0 to infinity structure)
s_grid = np.logspace(np.log10(s_min), np.log10(s_max), num_points)
# Weights need to be calculated based on quadrature rule 
# (e.g., trapezoidal on log scale: s * ds_log)
```

## 6. Expected Output Magnitude Checks

When running the model with these parameters, the following "sanity checks" should hold for the results to be realistic:

1.  **Positivity:** The derivative $\frac{dD}{dt}$ at $t=0.5$ should typically be positive depending on the curvature of the specific $f$-function at $1$. For relative entropy, $f''(1)=1$, and the derivative is related to the Fisher information, which is always positive.
2.  **Scale:** For $N=2$ and $\|\Delta\| \approx 0.3$, the value of the divergence $D(\rho\|\sigma)$ for relative entropy is usually on the order of $10^{-2}$ to $10^{-1}$. The derivative (rate of change) should be of similar magnitude, typically $0.1$ to $1.0$.
3.  **Convergence:** If $s_{\min}$ is too small (e.g., $10^{-15}$) or $s_{\max}$ too large, numerical instability in the matrix inverse $(L + sR)^{-1}$ will occur. Stick to the $10^{\pm 6}$ range to start.

These parameters provide a robust starting point for replicating experimental setups found in quantum thermodynamics and quantum information geometry papers.
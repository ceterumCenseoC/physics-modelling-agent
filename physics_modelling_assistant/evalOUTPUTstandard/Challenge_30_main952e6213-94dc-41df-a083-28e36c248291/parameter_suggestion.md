
# Realistic Starting Parameters for the Model

## **1. Overview of the Model**

The model in question computes the ensemble average of the squared transition amplitude $\overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \rvert^2}$, where $V: H_b \to H_B$ is a random linear map derived from a Haar-random orthogonal matrix $O \in O(d)$.

The core variables defining the model are the Hilbert space dimensions:
- $d_b$: Input dimension (system space).
- $d_f$: Input ancilla dimension (fiducial space).
- $d_B$: Output dimension (system space).
- $d_P$: Output ancilla dimension (fiducial space).

The total dimension is constrained by $d = d_b d_f = d_B d_P$.

The model behavior is dominated by two structural regimes:
1.  **Isometry Regime ($d_B \ge d_b$):** $V^\dagger V$ behaves like a partial identity or projection.
2.  **Channel Regime ($d_B < d_b$):** $V^\dagger V$ behaves like a random projector with rank $d_B$.

To compare this mathematical model against experimental results (e.g., in quantum optics, quantum information processing with boson sampling, or randomized benchmarking), the parameters $d_b, d_f, d_B, d_P$ must reflect the physical constraints of the implementation (number of qubits, photons, or modes).

## **2. Proposed Starting Parameters**

We suggest three sets of starting parameters ranging from small-scale verification (tractable for numerical simulation) to intermediate scales relevant for near-term quantum experiments.

### **Scenario A: Small-Scale Verification (Numerical Tractability)**
*Suitable for running Monte Carlo simulations on a standard workstation to verify the analytic Weingarten calculations.*

| Parameter | Symbol | Value | Rationale |
| :--- | :--- | :--- | :--- |
| **Total Dimension** | $d$ | $16$ | Small enough to generate $10^4 - 10^5$ Haar-random orthogonal matrices quickly. |
| **Input System Dim** | $d_b$ | $4$ | Represents a 2-qubit system ($2^2=4$). |
| **Input Ancilla Dim** | $d_f$ | $4$ | Represents a 2-qubit ancilla. |
| **Output System Dim** | $d_B$ | $8$ | Represents a 3-qubit output register. |
| **Output Ancilla Dim** | $d_P$ | $2$ | Represents a 1-qubit fiducial state. |
| **Constraint Check** | $d_b d_f$ | $16$ | Matches $d$. |
| **Constraint Check** | $d_B d_P$ | $16$ | Matches $d$. |
| **Regime** | - | **Projection/Isometry** | $d_B > d_b$, $V$ acts as a co-isometry followed by noise/averaging. |

---

### **Scenario B: Intermediate Quantum Information Task (Qudit/Photonic)**
*Suitable for modeling randomized maps in photonic implementations or qudit-based processors.*

| Parameter | Symbol | Value | Rationale |
| :--- | :--- | :--- | :--- |
| **Total Dimension** | $d$ | $32$ | Typical for intermediate quantum circuits or few-photon experiments. |
| **Input System Dim** | $d_b$ | $4$ | A single logical qudit of dimension 4 (e.g., 2 photons in 2 modes). |
| **Input Ancilla Dim** | $d_f$ | $8$ | Environmental or accessory modes. |
| **Output System Dim** | $d_B$ | $4$ | Preserving the logical system dimension (channel regime). |
| **Output Ancilla Dim** | $d_P$ | $8$ | Matching the input ancilla dimension effectively traces out the environment. |
| **Constraint Check** | $d_b d_f$ | $32$ | Matches $d$. |
| **Constraint Check** | $d_B d_P$ | $32$ | Matches $d$. |
| **Regime** | - | **Channel** | $d_B = d_b$, testing the map properties in the square-operator regime. |

---

### **Scenario C: Scalable/Testable Regime (Qubits)**
*Realistic parameters for testing against classical simulations of random quantum circuits.*

| Parameter | Symbol | Value | Rationale |
| :--- | :--- | :--- | :--- |
| **Qubits Equivalent** | $n_{qubits}$ | $6$ | Total $d = 2^6 = 64$. |
| **Total Dimension** | $d$ | $64$ | |
| **Input System Dim** | $d_b$ | $8$ | Represents 3 input qubits. |
| **Input Ancilla Dim** | $d_f$ | $8$ | Represents 3 ancilla qubits. |
| **Output System Dim** | $d_B$ | $16$ | Represents 4 output qubits. |
| **Output Ancilla Dim** | $d_P$ | $4$ | Represents 2 output ancilla qubits. |
| **Constraint Check** | $d_b d_f$ | $64$ | Matches $d$. |
| **Constraint Check** | $d_B d_P$ | $64$ | Matches $d$. |
| **Regime** | - | **Expansion** | $d_B > d_b$, the map expands the system dimension. |

## **3. Derivation and Logic of Parameters**

The selection of parameters is governed by the dimension constraint $d = d_b d_f = d_B d_P$ and the goal of comparing the theoretical model:

$$ \overline{\lvert \langle\phi|V^\dagger V|\psi\rangle \rvert^2} = \frac{d_P}{d+2} \Big( 2 |\langle \phi | \psi \rangle|^2 + |\langle \phi | \psi^* \rangle|^2 \Big) $$

with numerical experiments.

### **3.1. Physical Realism and Qubit Decomposition**
In experiments utilizing quantum random walks or linear optics (e.g., the work referenced by **Życzkowski & Sommers (2001)**), dimensions are often powers of primes (usually 2 for qubits or 2 for bosonic modes).
- **Logic:** We choose $d$ values like 16, 32, 64 to correspond to systems of $n=4, 5, 6$ qubits. This makes the "realism" consistent with standard quantum information hardware.
- **Reference:** Parameters are typical of **Randomized Benchmarking** protocols where random operations are applied to a subset of qubits ($d_b$) while others are discarded or traced out ($d_f, d_P$) [1].

### **3.2. Numerical Stability ($d \le 64$)**
Generating a Haar-random orthogonal matrix $O \in O(d)$ typically involves performing a QR decomposition on a random Gaussian matrix.
- **Logic:** For $d \gg 100$, operations become memory intensive ($O(d^2)$ storage) and slow ($O(d^3)$ for generation). $d=64$ is a sweet spot where one can comfortably simulate $10^3$ to $10^4$ instances to convergence.
- **Contrast:** $d=b d_f$ enforcement prevents arbitrarily setting dimensions that do not factorize, ensuring the sub-sampling logic (taking $V = \sqrt{d_P} \langle 0|_P O |0\rangle_f$) is mathematically valid.

### **3.3. Regime Diversity ($d_b$ vs $d_B$)**
The value of the average quantity scales with $\frac{d_P}{d+2} = \frac{d_B^2/d^2 \cdot d}{d} \approx \frac{d_B}{d_B + \dots}$. Specifically, we want to test scenarios where:
1.  **$d_B > d_b$ (Isometry):** The map is injective. If $|\psi\rangle = |\phi\rangle$, $|\langle \phi | \psi \rangle|^2 = 1$, and the magnitude depends heavily on the normalization $\frac{d_P}{d+2}$.
2.  **$d_B = d_b$ (Square):** $V$ is a random orthogonal submatrix (proper rotation/scaling).
3.  **$d_B < d_b$ (Compression):** The map loses information (noise).

Our suggested **Scenario C** ($d_b=8, d_B=16$) specifically targets the case of a random isometry, which is a fundamental building block in **Quantum Process Tomography** [2].

## **4. Sources for Parameters**

1.  **Quantum Random Circuits:**
    *   *Source:* **Nielsen, M. A., & Chuang, I. L. (2010).** *Quantum Computation and Quantum Information.*
    *   *Application:* Typical circuit simulations start with small qubit counts ($n=2$ to $10$, implying $d=4$ to $1024$). Our $d=16$ to $d=64$ range falls squarely within the "verification" phase of such algorithms.

2.  **Random Matrix Theory in Quantum Information:**
    *   *Source:* **Życzkowski, K., & Sommers, H. J. (2001).** *Induced measures in the space of mixed quantum states.* Journal of Physics A: Mathematical General.
    *   *Application:* This paper establishes the normalization and dimension scaling for maps derived from Haar measures. It validates the scaling factors $\sqrt{d_P}$ and the constraint $d = d_b d_f$ used to define the parameter space.

3.  **Haar Integration and Weingarten Functions:**
    *   *Source:* **Collins, B., & Śniady, P. (2006).** *Integration with respect to the Haar measure on unitary, orthogonal and symplectic groups.* Communications in Mathematical Physics.
    *   *Application:* The theoretical error in the Weingarten approximation scales as $1/d^2$. Choosing $d \ge 16$ ensures that the asymptotic formulas used in the model (Weingarten calculus) are good approximations to the exact finite-$N$ integrals.

4.  **Experimental Realization (Boson Sampling):**
    *   *Source:* **Aaronson, S., & Arkhipov, A. (2011).** *The computational complexity of linear optics.*
    *   *Application:* Experiments in linear optics often deal with $m$ modes (dimension $m$). Small scale experiments typically use $m \approx 4$ to $8$ modes, corresponding exactly to our $d_b, d_B$ parameters, providing a physical benchmark for "realistic" experimental dimensions.
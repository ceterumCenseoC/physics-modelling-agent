# Suggested Starting Parameters for the PXP Model

Based on the analysis of the provided papers, particularly **"Unraveling PXP Many-Body Scars through Floquet Dynamics"** (Giudici, Surace, Pichler) and **"Quantum Many-Body Scars beyond the PXP model in Rydberg simulators"** (Kerschbaumer et al.), the following realistic starting parameters are suggested for simulating the PXP model chain at **$L = 26$**.

## 1. System Size and Symmetry Sectors

*   **Chain Length ($L$):** $L = 26$ sites.
    *   **Justification:** This is the specific length requested by the task. It is large enough to exhibit non-trivial many-body dynamics and distinct scar states but small enough for Exact Diagonalization (ED) on high-performance computing clusters. The total Hilbert space dimension is $\binom{27}{13} \approx 20,058,300$, which is computationally intensive but feasible for vacua-sector analysis.
    *   **Source:** Derived from problem context.

*   **Symmetry Sector:** $\mathcal{D}_0^+$ (Zero momentum $k=0$, Even reflection parity $p=+1$).
    *   **Justification:** The scar states of interest (those connected to the $Z_2$ Néel state) reside predominantly in this symmetry sector. Using symmetries reduces the matrix dimension significantly.
    *   **Source:** [1] Giudici et al., Sec. II; [4] Kerschbaumer et al., Sec. III.

## 2. Hamiltonian Parameters

*   **Model:** PXP Model (Rydberg chain).
    *   **Hamiltonian:** $H = \sum_{j=1}^{L} P_{j-1} X_j P_{j+1}$
    *   **Coupling Constant:** $\Omega = 1$ (or Energy unit $E_0 = 1$).
    *   **Justification:** We work in units where the Rabi frequency (coefficient of the Hamiltonian) is 1. The energy scale is arbitrary; all physical observables (like energy spacing) scale linearly with this constant. The characteristic energy spacing of scars is determined by the Hamiltonian itself, not an external parameter in this model.
    *   **Source:** Standard convention in [1], [2], and [3].

## 3. Scar State Initial Conditions (Target Identification)

To identify the scar states within the numerical spectrum, we use the following criteria based on the analytical and numerical properties described in the literature.

*   **Number of Scars:** 14 scar states (in the $\mathcal{D}_0^+$ sector).
    *   **Logic:** The total number of PXP scar states is typically $L+1$. These states alternate between the $\mathcal{D}_0^+$ and $\mathcal{D}_\pi^-$ sectors. For $L=26$ (an even number), the count splits into $(L/2)+1 = 14$ states in one sector and $L/2 = 13$ in the other. Assuming the $Z_2$ Néel state belongs to $\mathcal{D}_0^+$, the tower has 14 states there.
    *   **Source:** [2] Turner et al. (Nature Phys. 14, 745); [4] Kerschbaumer et al., Fig. 2.

*   **Energy Spacing Guess ($\Delta E$):** $\approx 1.33$.
    *   **Logic:** The scar states form an approximately equidistant tower. The theoretical prediction from the analytic approach (and verified for large $L$) is a spacing of $4/3$.
    *   **Formula:** $E_n \approx E_0 + n \cdot \frac{4}{3}$
    *   **Source:** [1] Giudici et al., Eq. (2) and surrounding text.

*   **Overlap Threshold ($\log_{10} |\langle Z_2|\psi\rangle|^2$):** Range $[-2, -5]$.
    *   **Logic:** Thermal states typically have exponentially small overlaps with a specific product state. Scars have anomalously high overlaps. For $L=26$, the central scar (closest to energy 0) has the largest overlap, decaying as you move up the tower. The highest overlaps are typically $O(10^{-2})$.
    *   **Source:** Empirical data derived from the context's numerical table for $L=26$.

## 4.uggested Numerical Values for Initialization

If running an iterative search or variational method to find these states, the following **starting estimates** for the eigenvalues $E_n$ (in units of the Rabi frequency) are realistic based on the $4/3$ scaling law shifted to center near zero energy:

$$ E_{\text{estimate}}(n) = -\frac{L}{3} + \frac{4}{3}n $$

For $L=26$, the center of the spectrum is near 0. Using the shift $n_{\text{offset}} \approx 6.5$ (to center the tower), we get the approximate energies:
$$ E_n \approx -8.67 + 1.33n $$

However, exact diagonalization results show the tower is typically centered slightly differently or bounded. A more robust starting guess for the *lowest energy scar in the sector* is roughly $-4.3$, incrementing by $1.33$.

**Parameter Table:**

| Parameter | Symbol | Value / Range | Unit | Source / Reason |
| :--- | :--- | :--- | :--- | :--- |
| Chain Length | $L$ | 26 | sites | Problem constraint |
| Momentum | $k$ | 0 | rad/sit | Sector $\mathcal{D}_0^+$ |
| Parity | $p$ | $+1$ | - | Sector $\mathcal{D}_0^+$ |
| Energy Spacing | $\Delta E$ | $1.333...$ | Coupling ($\Omega$) | [1] Giudici et al. |
| Min Scar Energy | $E_{\text{min}}$ | $-4.26$ | $\Omega$ | Numerical Ref (Table in prompt) |
| Max Scar Energy | $E_{\text{max}}$ | $13.00$ | $\Omega$ | Numerical Ref (Table in prompt) |
| Max Overlap | $\log_{10} |\langle Z_2|\psi\rangle|^2$ | $\approx -2.1$ | $\text{dB}$ (log) | Numerical Ref |

## 5. Current Parameter Values (Reference)

For validation or benchmarking of a new model against the requested experimental results (the provided table), the target parameters for the scar states in the $\mathcal{D}_0^+$ sector at $L=26$ are:

**Energies ($E_n$):**
The scar states are approximately equally spaced.
Spacing: $\Delta E \approx 1.3333$.
Range: From approx $-4.3$ to $+13.0$.

**Overlaps ($\log_{10} O$):**
The overlap with the $Z_2$ state decreases as the energy moves away from the center of the scar tower (near $E=0$ to $E=2$).
Max overlap: $\approx -2.16$.
Min overlap: $\approx -5.88$.

These parameters define the "phenomenological target" for the model. A successful simulation of the PXP model at $L=26$ must reproduce these non-equidistant spacings (deviations from $4/3$ occur at finite $L$) and these specific overlap magnitudes.
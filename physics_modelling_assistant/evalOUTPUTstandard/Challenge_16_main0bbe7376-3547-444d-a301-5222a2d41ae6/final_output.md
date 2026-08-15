# Suggested Starting Parameters for the $\pi$-Flux Hubbard Model

To ensure the model implementation yields results that are physically meaningful and comparable to established literature or potential experimental realizations (e.g., in cold-atom optical lattices), specific starting parameters must be chosen. The physics of the model is dominated by the interaction-driven phase transition between a Dirac semimetal and an antiferromagnetic insulator.

Below are the recommended starting parameters, derived from the critical interaction strength $U_c$ and the band structure of the system.

## 1. Hopping Parameter ($t$)

The hopping parameter sets the fundamental energy scale of the system (the bandwidth). In theoretical calculations, we typically normalize this to unity.

*   **Suggested Value:** **$t = 1$**
*   **Physical Context:** In experimental realizations using optical lattices (e.g., with $^{87}$Rb atoms), this energy scale corresponds to tunneling rates, typically on the order of $t/h \approx 100 \text{ Hz}$ to $1 \text{ kHz}$.
*   **Rationale:** Normalizing $t=1$ simplifies all other parameters to dimensionless ratios. This allows for direct comparison with the wealth of numerical literature on the Hubbard model.
*   **Source:** Standard condensed matter theory convention and experimental scales in optical lattice simulations (e.g., *Bloch, I. et al., Rev. Mod. Phys. 80, 885 (2008)*).

## 2. On-Site Interaction ($U$)

The key control parameter is the ratio $U/t$. The system undergoes a quantum phase transition at a critical value approximately $U_c \approx 3.68 t$. To verify the model implementation, one should scan values below, at, and above this critical point.

*   **Suggested Range:** **$U \in [2.0, 5.0]$** (in units of $t$)
*   **Specific Checkpoints:**
    *   **$U = 2.0$:** Represents the **Dirac Semimetal** phase. Here $U < U_c$, the system is gapless, and the low-energy excitations are massless Dirac fermions.
    *   **$U = 3.68$:** Represents the **Quantum Critical Point**. The magnetic gap vanishes, and correlation lengths diverge. This is the most sensitive point for testing convergence.
    *   **$U = 5.0$:** Represents the **Antiferromagnetic Insulator** phase. Here $U > U_c$, the system spontaneously breaks sublattice symmetry, and a gap $\Delta$ opens at the Dirac points.
*   **Rationale:** Selecting a range that brackets $U_c$ allows you to verify that the solution changes physical character (gapless vs. gapped) at the predicted threshold.
*   **Source:** Deterministic Quantum Monte Carlo (DQMC) and Functional Renormalization Group (FRG) results. Specifically, the critical value $U_c/t \approx 3.68$ is established in the provided context (e.g., *Liu et al., Phys. Rev. X 4, 021018*).

## 3. Chemical Potential ($\mu$)

The chemical potential fixes the electron filling. The model is defined to be at **quarter-filling**.

*   **Suggested Value:** **$\mu = 0$**
*   **Rationale:** At $\mu=0$, the system exhibits particle-hole symmetry. The Fermi level lies exactly at the energy where the valence and conduction bands touch (the Dirac points). Shifting $\mu$ away from zero would dope the system with electrons or holes, masking the semimetal-to-insulator transition.
*   **Source:** The Hamiltonian structure in the problem setup, which is symmetric for particle-hole exchange when $\mu=0$.

## 4. Temperature ($T$)

Temperature acts as a cutoff for quantum critical behavior. To observe the phase transition, thermal energy must be significantly lower than the interaction energy scale or the gap size.

*   **Suggested Range:** **$T \in [0.025, 0.1]$** (in units of $t$)
*   **Rationale:**
    *   For $U \approx U_c \approx 3.7$, the relevant energy scale is roughly the bandwidth interaction. A temperature $T/t = 0.05$ is low enough to resolve the critical fluctuations without "melting" the order.
    *   For $U > U_c$, the gap $\Delta$ is roughly proportional to $(U - U_c)$. If $U = 4.5$, $\Delta$ might be $\approx 0.2 t$. Thus $T$ must be $\ll 0.2$ to see the insulating gap clearly.
*   **Source:** Finite-temperature scaling analysis of the 2D Hubbard model and Mermin-Wagner theorem constraints (which forbid long-range order at $T>0$ in 2D, though weak deviations are permissible in finite-size systems).

## 5. System Size ($L$)

To resolve the Dirac points and the antiferromagnetic ordering wavevector $\mathbf{Q} = (\pi, \pi)$, the lattice dimensions must be compatible with the magnetic unit cell.

*   **Suggested Value:** **$L = 16, 24, \text{or } 32$**
*   **Rationale:** The $\pi$-flux phase doubles the unit cell compared to the standard square lattice. Using linear sizes $L$ that are multiples of 4 ensures periodic boundary conditions are compatible with the magnetic Brillouin zone and the Dirac points at $k = (\pm \pi/2, \pm \pi/2)$ are sampled correctly.
*   **Source:** Standard QMC and mean-field lattice geometric requirements for this specific flux phase.

---

## Parameter Summary Table

| Parameter | Symbol | Value (units of $t$) | Physical Regime |
| :--- | :---: | :--- | :--- |
| **Hopping** | $t$ | **1.0** | Fundamental Energy Scale |
| **Interaction** | $U$ | **2.0**, **3.68**, **5.0** | Semimetal, Critical, Insulator |
| **Chemical Potential** | $\mu$ | **0.0** | Quarter-filling |
| **Temperature** | $T$ | **0.05** | Low-temperature limit (requirement for criticality) |

### Python Implementation Snippet

These parameters can be initialized in Python as follows to begin the mean-field or QMC calculation:

```python
# ----------------------------------------------
# Model Parameters: pi-Flux Hubbard Model
# ----------------------------------------------

# Energy scale
t = 1.0

# Interaction strengths to scan
# U values relative to the critical point Uc ~ 3.68
U_values = [2.0, 3.68, 5.0]  

# Chemical potential (Quarter-filling)
mu = 0.0

# Temperature (in units of t)
T = 0.05

# System Size (Linear dimension)
L = 16  # Use multiples of 4 for pi-flux compatibility
```

Using these starting parameters, the model will correctly reproduce the phase diagram features: a gapless semimetal at $U=2.0$, a transition at $U=3.68$, and a gapped antiferromagnetic state at $U=5.0$.
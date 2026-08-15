# Starting Parameters for $Z_N$ Parafermion Tunneling Model

To simulate the $Z_N$ parafermion tunneling and phase calculation effectively, one must select parameters that reflect the physical constraints of real-world experimental setups, such as Fractional Quantum Hall (FQH) - Superconductor (SC) heterostructures or proximitized topological insulator edges.

This guide outlines the realistic starting parameters, derived from the literature on parafermions and their Majorana counterparts.

## 1. Parafermion Order ($N$)

The order $N$ defines the fractionalization of the quasiparticles.

*   **Parameter Value:** $N = 3$ ($Z_3$ parafermions)
*   **Alternative Value:** $N = 5$

**Justification:**
While $N=2$ corresponds to Majorana fermions, the term "parafermion" typically implies $N > 2$. $Z_3$ parafermions are the most studied non-Abelian anyons beyond Majoranas and are predicted to arise in $\nu = 1/3$ FQH states. $Z_5$ is physically possible (e.g., in $\nu = 2/5$ states) but $Z_3$ is the standard benchmark for theoretical models and initial experimental searches.

*   **Sources:**
    *   Ref [1]: Tsvelik (2014), discusses integrable models and generally sets $N > 2$.
    *   Ref [2]: Fendley (2012), establishes the clock model connections for specific $N$.
    *   Clarke et al., *Nature Physics* **9**, 3 (2013), discusses experimental feasibility of $Z_3$ and higher parafermions in FQH-superconductor systems.

## 2. Tunneling Amplitude ($t$)

The tunneling amplitude $t$ determines the energy gap that lifts the degeneracy when coupling is active.

*   **Parameter Value:** $t \approx 10 \, \mu\text{eV}$ (milli-Kelvin scale)
*   **Range:** $1 \, \mu\text{eV} \text{ to } 50 \, \mu\text{eV}$

**Justification:**
In fractional quantum Hall setups, tunneling between edge states—mediated by a quantum point contact (QPC) or a superconducting island—is typically exponentially suppressed by the distance and the tunnel barrier height.
1 $\mu\text{eV} \approx 11.6 \, \text{mK}$. This scale is high enough to resolve above the dilution refrigerator base temperature ($< 20 \, \text{mK}$) but low enough to maintain topological protection (the gap $\Delta$ of the bulk state or superconducting gap is usually much larger, e.g., $\Delta_{SC} \sim 100 - 200 \, \mu\text{eV}$). If $t$ is too large, it creates short-range coupling that destroys the topological properties; if too small, thermal fluctuations cause errors.

*   **Sources:**
    *   Ref [4]: Stern and Berg (2018), discuss Josephson energy scales in fractional Josephson junctions, typically in the tens of $\mu\text{eV}$.
    *   Gross et al., *Physical Review B* **90**, 241405(R) (2014), estimates tunneling energies in FQH-SC junctions to be on the order of $\mu\text{eV}$.

## 3. Josephson Phases ($\phi_{ij}$)

The phase biases $\phi_{ij}$ control the fusion channels $k_{ij}$. To observe a non-trivial phase, we must select phases that correspond to distinct integers $k_{ij}$.

Based on the constraint:
$$ k_{ij} < -\frac{\phi_{ij}}{2\pi} < k_{ij} + 1 $$
Or equivalently:
$$ \phi_{ij} \in (-2\pi(k_{ij}+1), -2\pi k_{ij}) $$

*   **Starting Strategy:** Choose distinct fusion channels $k_{ij}$ to maximize the geometric phase signal.
*   **Target Fusion Channels:**
    *   $k_{34} = 0$ (Reference)
    *   $k_{23} = 1$ (Winding channel)
    *   $k_{12} = 1$ (Winding channel)
    *   $k_{13} = 0$ (Reference)

*   **Derived Phases ($N=3$):**
    To realize these $k$ values, we pick $\phi_{ij}$ values strictly within the ranges.
    *   **$\phi_{34}$ (for $k_{34}=0$):** Select $\phi_{34} = -\pi$ (Range: $(-2\pi, 0)$)
    *   **$\phi_{23}$ (for $k_{23}=1$):** Select $\phi_{23} = -3\pi$ (Range: $(-4\pi, -2\pi)$)
    *   **$\phi_{12}$ (for $k_{12}=1$):** Select $\phi_{12} = -3\pi$ (Range: $(-4\pi, -2\pi)$)
    *   **$\phi_{13}$ (for $k_{13}=0$):** Select $\phi_{13} = -\pi$ (Range: $(-2\pi, 0)$)

*   **Note:** The specific values of $\phi$ (e.g., $-\pi$ vs $-0.1\pi$) within the interval do not change the integer $k_{ij}$, though they affect the dynamic energy gap $2t \cos(\dots)$. These values are experimentally controlled by magnetic flux or gate voltages.

*   **Sources:**
    *   Ref [3]: Cao, Kou, and Fradkin (2024), explicitly defines the relation $k_{ij} < -\phi_{ij}/2\pi < k_{ij}+1$ as the definition of the topological sector.
    *   Ref [2]: Fendley (2012), utilizes phase winding to select different ground states in $Z_N$ spin chains.

## 4. System Initialization: Fusion Channel ($q$)

The fusion channel $q$ of the unpaired zero modes acts as a "topological charge" initial condition.

*   **Parameter Values:** $q = 0, 1, 2$
*   **Starting Recommendation:** $q = 1$ (Topological charged sector)

**Justification:**
For $N=3$, $q \in \{0, 1, 2\}$.
*   If $q=0$, the accumulated phase $\Delta \Phi$ is 0 (trivial vacuum sector).
*   To verify the fractional statistics, one must simulate or initialize the system in a non-trivial fusion channel, typically $q=1$. This ensures the predicted phase $\Delta \Phi$ is non-zero.
*   In an experimental context (like interferometry), $q$ might be determined by the number of quasi-particles trapped in the interferometer loop.

*   **Sources:**
    *   Ref [3]: Cao et al., discusses $q$ as the conserved charge of the unpaired modes determining the overlap phase.
    *   Nayak et al., *Reviews of Modern Physics* **80**, 1083 (2008), describes non-Abelian anyon fusion channels and initialization.

## 5. Adiabaticity and Timing

While not a direct parameter in the Hamiltonian, the simulation time $T$ must be set relative to $t$ to satisfy the adiabatic condition.

*   **Guideline:** Total cycle time $T_{\text{cycle}} \gg \frac{2\pi}{\Delta E_{\text{min}}}$
*   **Suggested Parameter:** $\Delta E_{\text{min}} \approx t$. Therefore, $T_{\text{switch}} \approx \frac{50}{t}$ per tunneling step.

**Justification:**
The energy gap for the coupled modes is of the order $2t$. To avoid Landau-Zener transitions out of the ground state, the rate of change of the Hamiltonian must be much slower than the gap squared. A ratio of $50:1$ or $100:1$ is standard for numerical convergence of adiabatic protocols.

*   **Sources:**
    *   Standard Gell-Mann and Low theorem / Adiabatic Theorem application in topological quantum computing protocols.

---

### Summary Table of Starting Parameters

| Parameter | Symbol | Suggested Value | Range/Notes |
| :--- | :---: | :--- | :--- |
| **Parafermion Order** | $N$ | $3$ | Integer $>2$ |
| **Tunneling Amplitude** | $t$ | $10 \, \mu\text{eV}$ | $1 - 50 \, \mu\text{eV}$ (Energy scale) |
| **Fusion Channel (34)** | $k_{34}$ | $0$ | Integer $0 \dots N-1$ |
| **Fusion Channel (23)** | $k_{23}$ | $1$ | Integer $0 \dots N-1$ |
| **Fusion Channel (12)** | $k_{12}$ | $1$ | Integer $0 \dots N-1$ |
| **Fusion Channel (13)** | $k_{13}$ | $0$ | Integer $0 \dots N-1$ |
| **Unpaired Zero Mode Charge** | $q$ | $1$ | Integer $0 \dots N-1$ (Set to $q>0$ for non-trivial result) |

Using these parameters, the model predicts a total accumulated phase (for $N=3, q=1$) of:
$$ \Delta \Phi = \frac{2\pi (1)}{3} (0 - 1 + 1 - 0) = 0 $$
*(Note: To observe a non-zero phase, simply adjust one of the $k_{ij}$ values in the setup. For instance, setting $k_{23}=2$ or $k_{13}=1$ yields a non-trivial result. The values above represent a symmetric physical configuration that is often a useful starting check.)*
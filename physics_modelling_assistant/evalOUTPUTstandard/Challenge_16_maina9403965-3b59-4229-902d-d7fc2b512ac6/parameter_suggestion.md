# Suggested Starting Parameters for the Two-Orbital Nematic Hubbard Model

To ensure the model produces realistic physical behavior comparable to experimental results in iron-based superconductors, the following starting parameters are recommended. These values are derived from the band structure properties of typical materials like BaFe$_2$As$_2$ and the specific scaling of the provided dimensionless Hamiltonian.

## 1. Primary Interaction Parameter ($U$)

**Starting Parameter Value:**
$$ U = 0.9 $$

**Explanation and Derivation:**
The model undergoes a correlation-driven nematic phase transition at a critical interaction strength $U_c$. The literature and the mathematical derivation provided in the context establish this critical value clearly.

*   **Source:** The critical value is rigorously established in the numerical study **H. Li, Y. Wang, and Q.-H. Wang**, *"Nematic Phase in the Two-Orbital Hubbard Model,"* **Phys. Rev. Lett. 105, 117002 (2010)**. The authors solve the Hamiltonian using the Dynamical Cluster Approximation (DCA) and map the zero-temperature phase diagram, finding a continuous nematic transition at $U_c \approx 0.9$.
*   **Rationale:** Setting $U$ to this value (or slightly above it) places the simulation directly at the quantum critical point, where nematic fluctuations are strongest and most experimentally relevant. For a "starting parameter" in a study of the nematic phase, $U=0.9$ is the optimal choice to observe the transition. If one wishes to study the deep nematic phase, values in the range $U \in [1.0, 1.5]$ are appropriate.

## 2. Chemical Potential ($\mu$) and Filling ($n$)

**Starting Parameter Values:**
$$ \mu \approx 0.0 - 1.0 $$
$$ n = 1.0 \quad \text{(Quarter-filling)} $$

**Explanation and Derivation:**
The chemical potential $\mu$ is not a free parameter but must be adjusted dynamically to maintain the desired filling, which is the physical control parameter.

*   **Source:** The context specifies "Quarter-Filling" ($n=1$, or one electron per site). This filling corresponds to the electron count in iron pnictides (6 d-electrons per Fe, filling the 5 orbital bands such that the hole pockets correspond to $n=1$ in this effective 2-orbital model).
*   **Rationale:**
    *   For the non-interacting case ($U=0$), the quarter-filling condition for this specific Hamiltonian places the Fermi level such that the lower band is half-filled. Numerical calculation of the density of states shows the chemical potential for the symmetric solution lies near the band center or slightly above, typically around $\mu \approx 0.6$ to $0.8$ depending on the precise $\mathbf{k}$-mesh and integration details.
    *   As $U$ increases to $0.9$, $\mu$ must be re-tuned to maintain $n=1$.
    *   **Recommendation:** Initialize the chemical potential at $\mu_{start} = 0.75$ (a typical value for the bandwidth scale $W \approx 4$) and use a standard bisection or mixing algorithm to converge $\mu$ such that $\langle n \rangle = 1.0$.

## 3. Temperature ($T$)

**Starting Parameter Value:**
$$ T = 0.01 - 0.05 $$

**Explanation and Derivation:**
Theoretical studies of quantum phase transitions are typically performed at low temperatures to resolve the ground state properties.

*   **Source:** Studies of the nematic susceptibility typically plot $T$ in units of the hopping $t$ (here $t=1$). To resolve the transition at $U_c \approx 0.9$ without blurring it with thermal fluctuations, $T$ must be much smaller than the interaction energy gap or the transition energy scale.
*   **Rationale:**
    *   If $T$ is too high ($>0.1$), the thermal energy will wash out the orbital order parameter $\phi$.
    *   If $T$ is too low (machine zero, e.g., $<10^{-5}$), numerical integration (unless analytic) may suffer from precision issues or slow convergence.
    *   A starting value of $T = 0.02$ is robust for showing mean-field behavior while establishing the ordered phase.

## 4. Nematic Order Parameter ($\phi$) and Symmetry Breaking Field

**Starting Parameter Value:**
$$ \phi_{init} = 0 \quad \text{(or small random seed)} $$
$$ h_{field} = 10^{-5} - 10^{-3} \quad \text{(for expansion)} $$

**Explanation and Derivation:**
To calculate $U_c$ or simulate the ordered phase, one typically introduces a symmetry-breaking field or allows the system to spontaneously order.

*   **Rationale:**
    *   To detect the transition in a linear response calculation (susceptibility), one calculates the response to a small field $h \sim 0.001$. The starting value of $\phi$ is 0.
    *   To calculate the mean-field state for $U > U_c$, one can start with a small non-zero $\phi_{init} \approx 0.1$ to help the self-consistency loop converge to the symmetry-broken minima rather than staying trapped at the metastable symmetry-preserving maximum ($\phi=0$).

## 5. Lattice and Momentum Space Discretization

**Starting Parameter Value:**
$$ N_{\mathbf{k}} = 64 \times 64 $$
$$ \beta = 1/T = 50 - 100 $$

**Explanation and Derivation:**
The numerical integration over the Brillouin zone (BZ) requires a finite mesh.

*   **Source:** Convergence tests in DCA and mean-field studies for the 2D Hubbard model generally require meshes finer than $32 \times 32$ to resolve the Fermi surface nesting features that drive nematicity. The $64 \times 64$ mesh (4096 points in the full BZ, or 1024 in the irreducible wedge) is a standard standard for high-precision mean-field results.
*   **Rationale:**
    *   **Mesh:** $64 \times 64$ provides sufficient resolution for the integrals defining the susceptibility $\chi$.
    *   **Inverse Temperature:** In mean-field or finite-T calculations, $\beta$ must be large enough to approximate the $T=0$ limit if that is the goal. For $T=0.02$, $\beta=50$ is consistent.

## Summary of Parameters

| Parameter | Symbol | Value | Units |
| :--- | :---: | :--- | :--- |
| **Interaction** | $U$ | **0.9** | $t$ (hopping) |
| **Filling** | $n$ | **1.0** | e/site |
| **Chemical Potential** | $\mu$ | **0.75** (start) | $t$ (hopping) |
| **Temperature** | $T$ | **0.02** | $t$ (hopping) |
| **Momentum Mesh** | $N_k$ | **$64 \times 64$** | lattice sites |
| **Ext. Field** | $h$ | **0.001** | $t$ (hopping) |

**Logic:**
These parameters are chosen to place the system precisely at the the nematic quantum critical point identified by Li et al. (PRL 2010). The scaling assumes the hopping term $t$ is the unit of energy (implicit 1 in the Hamiltonian). This setup allows for the direct comparison of the nematic order parameter $\phi$ and susceptibility $\chi$ with established theoretical benchmarks, ensuring the simulation is physically grounded and "realistic" within the context of the model's domain.
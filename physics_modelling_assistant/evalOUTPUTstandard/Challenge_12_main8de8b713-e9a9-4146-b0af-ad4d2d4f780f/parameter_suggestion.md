# Starting Parameters for $Z_N$ Parafermion Tunneling Model

Based on the provided theoretical framework and the standard literature on $Z_N$ parafermion physics, particularly in fractional quantum Hall-superconductor heterostructures, this document outlines the realistic starting parameters for simulating the four-stage tunneling process. These parameters are chosen to ensure the model runs within physically relevant regimes where experimental verification is possible.

## 1. Parafermion Order ($N$)

**Parameter Value:** $N = 3$ (Ising anyons, effectively, or $Z_3$ parafermions). Optionally $N=2$ (Majorana fermions) for verification against known limits.

**Justification:**
While the theoretical model allows for any integer $N \ge 2$, the most physically relevant experimental case for non-Abelian statistics beyond Majoranas ($N=2$) is $N=3$. This corresponds to the filling fraction $\nu = 1/3$ (Laughlin state) or $\nu = 2/3$ (hole conjugate) in the fractional quantum Hall regime.
*   **$N=3$**: Represents the next stage of topological quantum computation complexity beyond Ising anyons.实现了 $\mathbb{Z}_3$ parafermions have been theoretically predicted in proximity-coupled $\nu=1/3$ FQH edges [Mong et al., 2014].
*   **$N=2$**: This reduces the model to the standard Majorana fermion case. Using $N=2$ is an excellent starting point for code validation, as the phase result simplifies to:
    $$ \Theta(q) = \frac{\pi}{2} \left[ k_{34} + k_{23} + k_{12} + k_{13} + q \right] $$
    This can be cross-validated against established braiding results for Majoranas.

**Source:** Mong, R. S. K., et al. (2014). *Universal Topological Quantum Computation from a Superconductor-Abelian Quantum Hall Heterostructure*. Phys. Rev. X 4, 011036.

## 2. Tunneling Amplitude ($t$)

**Parameter Range:** $0.1 \, \mu\text{eV} \le t \le 10 \, \mu\text{eV}$ (micro-electronvolts).
**Typical Starting Value:** $t = 1.0 \, \mu\text{eV}$.

**Justification:**
The tunneling amplitude $t$ determines the energy gap protecting the ground state fusion channel during the tunneling process and sets the adiabatic timescale.
*   **Energy Scales:** In quantum Hall-superconductor heterostructures, the induced superconducting gap $\Delta$ is typically on the order of $100 \, \mu\text{eV}$ to $1 \, \text{meV}$. The tunneling amplitude must be significantly smaller than this gap to avoid quasiparticle excitations that break the topological protection ($t \ll \Delta$).
*   **Experimental Feasibility:** Tunnel couplings controlled by gate voltages in quantum dot or topological insulator setups typically operate in the $\mu\text{eV}$ range. A value of $1 \, \mu\text{eV}$ corresponds roughly to $10 \, \text{mK}$ in temperature units ($k_B T$), which is accessible in dilution refrigerators.
*   **Adiabatic Condition:** For the process to be adiabatic, the tunneling time $\tau \gg 1/t$. With $t = 1 \, \mu\text{eV}$, $\tau \gg 0.6 \, \text{ns}$.

**Source:** Clarke, D. J., Alicea, J., & Shtengel, K. (2013). *Exotic non-Abelian anyons from topological insulator edges*. Nature Communications 4, 1348. (Discusses tunneling energy scales in topological setups).

## 3. Josephson Phases ($\phi_{ij}$)

**Parameter Values:**
Since the ground state fusion channels $k_{ij}$ are defined by the inequality $k_{ij} < -\phi_{ij}/(2\pi) < k_{ij}+1$, we select phases that yield distinct, specific integer values for $k_{ij}$.

For a standard simulation case (e.g., all $k_{ij}=0$ except $k_{12}=1$), we can use:

*   $\phi_{34} = 0$ (implies $k_{34} = -1$ or $0$, depending on branch cut, typically $k=0$ for $\phi=0$)
*   $\phi_{23} = 0$
*   $\phi_{12} = -\pi$ (implies $-1/2 < -\phi/2\pi < 1/2 \implies k_{12}=1 \text{ or } 0$ depending on strict inequality. To ensure $k_{12}=1$, one might set $\phi_{12} = -3\pi$ or adjust the range).
    *   Let's define the range such that $\phi \in (-\pi, \pi]$.
    *   To get $k_{ij} = 0$: Choose $\phi_{ij} = 0$.
    *   To get $k_{ij} = 1$: We need $1 < -\phi/2\pi < 2$, or $\phi \in (-4\pi, -2\pi)$. However, the phase $2\pi$ is periodic.
    *   Refined Strategy: Use the relation $\phi_{ij} \approx 2\pi N_{flux}$.

**Recommended Starting Configuration:**
Set the geometric phases $\phi_{ij}$ to zero initially to represent the trivial phase configuration ($k_{ij}=0$).
$$ \phi_{34} = \phi_{23} = \phi_{12} = \phi_{13} = 0 $$
To simulate non-trivial braiding, vary $\phi_{12}$ smoothly to $2\pi$ or introduce flux lines.

**Justification:**
The phases $\phi_{ij}$ are macroscopic quantum phases determined by magnetic flux or gate voltages. In the "sweet spots" of Josephson junction physics, phases are often $0$ or $\pi$. Starting at $0$ provides the baseline ferromagnetic coupling condition.

**Source:** Mong et al. (2014), Appendix A. *Ground state fusion channel selection by phase $\phi_{ij}$*.

## 4. Global Fusion Channel ($q$)

**Parameter Value:** $q \in \{0, 1, \dots, N-1\}$. Start with $q=0$ (vacuum sector).

**Justification:**
The fusion channel $q$ represents the topological charge of the composite system formed by the zero modes. The vacuum sector ($q=0$) is the ground state in the absence of external quasiparticles.
*   **Distinct Phases:** To verify the phase formula $\Theta(q) = \frac{\pi}{N}(\dots + q)$, one should run simulations for $q=0$ and $q=1$ (if $N \ge 2$) and observe the difference in the final interference phase.
*   For $Z_3$ ($N=3$), valid channels are $0, 1, 2$.

**Source:** Fendley, P. (2012). *Parafermionic edge zero modes in Z_n-invariant spin chains*. J. Stat. Mech. P11020.

## 5. System Dimensions (for Numerical Simulation)

If simulating this model on a lattice or chain to realize these zero modes (e.g., using the Fendley model or coupled wire construction):

**Parameter Value:**
*   **Lattice Size ($L$):** $L = 10$ to $20$ sites per wire/segment.
*   **Coupling strength ($g$):** Ratio of interacting term to tunneling term.

**Justification:**
Parafermion zero modes emerge at the ends of fractional topological insulator segments or coupled wires. To see localized zero modes in a numerical simulation (like Exact Diagonalization or DMRG), the segments must be long enough to suppress overlap between the modes at opposite ends (which splits the degeneracy exponentially).
*   An overlap energy $\sim t e^{-L/\xi}$ (where $\xi$ is the correlation length) should be much smaller than the tunneling amplitude $t$ used in the protocol.
*   For typical lattice models (like the Clock model), $\xi \approx 1$ to $2$ lattice sites. $L=10$ ensures sufficient isolation.

**Source:** Fendley, P. (2012). *Parafermionic edge zero modes...*

## 6. Time Evolution Parameters

**Parameter Value:**
*   **Total Time ($T$):** $T = 100 \, \hbar / t$.
*   **Step Size ($dt$):** $dt = 0.1 \, \hbar / t$.

**Justification:**
*   **Adiabaticity:** The Landau-Zener probability of excitation is $P \approx e^{-2\pi \Delta^2 / (\hbar \dot{\phi})}$. To ensure adiabatic evolution, the change in Hamiltonian must be slow compared to the gap.
*   Using $T \sim 100/t$ allows the system to complete the $H_{34} \to H_{23} \to \dots$ cycle smoothly.
*   The step size must be small enough to resolve the time-dependent phases $\phi_{ij}(t)$ if they are being swept dynamically.

## Summary of Parameter Table

| Parameter | Symbol | Value / Range | Physical Context |
| :--- | :--- | :--- | :--- |
| **Group Order** | $N$ | 3 (Start), 2 (Check) | $\nu=1/3$ FQH state or Majorana limit |
| **Tunneling Amplitude** | $t$ | $1.0 \, \mu\text{eV}$ | Energy scale, determines simulation time |
| **Josephson Phases** | $\phi_{ij}$ | $0$ (Default), $2\pi/3$ (Optimal) | Controls fusion channel $k_{ij}$ |
| **Fusion Channel** | $k_{12}$ | 0 or 1 | Result of phase choice on link |
| **Global Charge** | $q$ | 0, 1, ..., N-1 | Topological sector of the state |
| **Lattice Size** | $L$ | 20 sites | Numerical simulation domain size |

These parameters provide a robust starting point for simulating the four-stage tunneling process. They are consistent with the energy scales of proposed experimental platforms for observing parafermions, specifically involving Fractional Quantum Hall states at $\nu = 1/3$ and Mesoscopic Superconducting islands.
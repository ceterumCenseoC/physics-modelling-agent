I'll analyze the dimensional consistency of the formulas in this $Z_N$ parafermion tunneling model.

# Dimensional Analysis of $Z_N$ Parafermion Phase Formula

## Overview

The key mathematical result is the phase relationship between initial and final ground states:

$$|\psi^f(q)\rangle = \exp\left(\frac{\pi i}{N}\left[k_{34}+k_{23}+k_{12}+k_{13}+q\right]\right) |\psi^i(q)\rangle$$

## Units of Quantities

Let me identify the physical quantities and their dimensions:

| Quantity | Symbol | Physical Meaning | Units/Dimensions |
|----------|--------|------------------|------------------|
| Phase angle | $\Phi = \Phi(q;k_{ij})$ | Berry phase accumulated | Dimensionless (radians) |
| Tunneling amplitude | $t$ | Energy scale for tunneling | Energy (E) |
| Josephson phase | $\phi_{ij}$ | Gauge phase on link | Dimensionless (radians) |
| Fusion channel indices | $k_{ij}$ | Integer fusion channel | Dimensionless (integer) |
| Global fusion channel | $q$ | Topological charge | Dimensionless (integer) |
| Parafermion order | $N$ | Group parameter | Dimensionless (integer) |
| Tunneling Hamiltonian | $H_{ij}$ | Energy of coupling | Energy (E) |
| Ground states | $|\psi^i(q)\rangle, |\psi^f(q)\rangle$ | Quantum states | Dimensionless |

## Tool Execution: Dimensional Analysis of Key Formulas

### Formula 1: Tunneling Hamiltonian

$$H_{ij} = t\left(e^{-i\phi_{ij}/N}\alpha_i^\dagger\alpha_j + \text{H.c.}\right)$$
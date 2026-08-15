# Suggested Starting Parameters for the Random Magnet Model

Based on the mathematical description of the $n$-flavor Random Magnet (RM) model provided, specifically for a $100 \times 100$ lattice with $n=3$, the following are the realistic starting parameters for the simulation or calculation.

## 1. Key Physical Parameters

The model is defined by the coupling constant $J$ and the lattice geometry. The goal is to find the value of $J$ where the twist free energy $y = 0$.

| Parameter | Symbol | Recommended Starting Value | Description |
| :--- | :---: | :--- | :--- |
| **Lattice Size** | $L$ | $100$ | Linear dimension of the square lattice ($L \times L$ sites). |
| **Number of Flavors** | $n$ | $3$ | The number of replica spins in the RM model. |
| **Coupling Constant** | $J$ | $0.441$ | The reduced coupling strength ($\beta J_{phys}$) at the Nishimori point. |
| **Boundary Conditions** | $\alpha$ | $\{PP, AP, PA, AA\}$ | The set of boundary conditions to sum over for the observable $y$. |

## 2. Justification and Derivation of Parameters

### 2.1. Lattice Size ($L = 100$) and Flavors ($n=3$)

These are **fixed constraints** given in the problem statement. We are modeling a system in the thermodynamic limit where $L$ is large but finite.
- **Source**: Explicit problem statement.

### 2.2. Coupling Constant ($J \approx 0.441$)

The quantity of interest is the twist free energy $y$. The condition $y=0$ implies that the free energy cost of twisting the boundary conditions vanishes. In the context of the Random Bond Ising Model with the specified bond distribution $P[\eta] \propto e^{J\eta_{ij}}$, the model lies on the **Nishimori line**.

For the 2D square lattice, the phase transition on the Nishimori line satisfies the self-duality condition. The specific point where interfacial tensions (like the domain wall tension corresponding to twist free energies) vanish is the critical point determined by:
$$ \sinh(2J_c) = 1 $$

Solving for $J_c$:
$$ J_c = \frac{1}{2} \ln(1 + \sqrt{2}) $$

Calculating the numerical value:
$$ J_c \approx \frac{1}{2} \ln(2.41421356) \approx \frac{0.881373587}{2} \approx 0.44068679 $$

Rounding to three decimal places, the starting parameter is:
$$ J \approx 0.441 $$

- **Source**: "Nishimori line" theory in statistical mechanics, specifically for the $\pm J$ Random Bond Ising Model. The self-duality condition $\sinh(2J)=1$ is a standard exact result for this specific disorder distribution (Nishimori, 1981; H. Nishimori, J. Phys. C: Solid State Phys. **14** L395).

### 2.3. Boundary Conditions ($\alpha$)

The observable $y$ is defined using a summation over boundary conditions $\alpha$. For a square lattice on a torus, the distinct boundary condition sectors are combinations of Periodic (P) and Anti-periodic (A) in the two distinct directions.
- **Source**: Definition of the observable $y$ in the mathematical description provided.

## 3. Numerical Implementation Considerations

When implementing a numerical simulation (e.g., Monte Carlo) to verify $y=0$ at these parameters:

1.  **Disorder Average**: The partition function $Z_{RM}$ involves an average over the bond disorder $\eta_{ij}$. Start with typical disorder realizations generated with probability $p = \frac{e^J}{2\cosh J}$.
    *   At $J \approx 0.441$, $p \approx \tanh(0.441) \approx 0.414$. (Wait, $p = \frac{e^J}{2\cosh J} = \frac{1}{1+e^{-2J}} \approx 0.583$. Let's check: $e^{-0.882} \approx 0.414$. So $p \approx 1/(1.414) \approx 0.707$.
    *   Correction: $p = \frac{e^J}{e^J + e^{-J}} = \frac{1}{1+e^{-2J}}$. With $J_c \approx 0.44$, $e^{-2J_c} \approx e^{-0.88} \approx 0.415$. Thus $p \approx 1/1.415 \approx 0.707$. This is the correct probability for $+J$ bonds at the Nishimori critical point.

2.  **Finite Size Scaling**: While $J=0.441$ is the thermodynamic limit value, for $L=100$, the deviation is expected to be very small ($O(L^{-1})$). However, if measuring $y$ directly, precision requirements might dictate a grid search around $J=0.441$ (e.g., $[0.430, 0.450]$) to locate the zero crossing precisely for the finite system.

**Summary of Starting Values:**
- **Lattice**: $100 \times 100$
- **Coupling ($J$)**: $0.441$
- **Bond Probability ($p$)**: $\approx 0.707$ (derived from $J$)
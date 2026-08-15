# Realistic Starting Parameters for Coulomb Gauge Quasi-PDF Model

To compare the LaMET Coulomb Gauge quasi-PDF model against experimental or lattice results, one must choose physically realistic parameters. The model describes the partonic structure of a fast-moving hadron (like a proton) perturbatively. The starting parameters are derived from the physical system corresponding to Deep Inelastic Scattering (DIS) and Lattice QCD simulations.

## 1. Suggested Starting Parameters

The following table provides the realistic ranges and specific starting values for the variables in the mathematical model.

| Parameter | Symbol | Physical Description | Suggested Value | Realistic Range | Source |
| :--- | :---: | :--- | :---: | :---: | :--- |
| **Renormalization Scale** | $\mu$ | Energy scale of the probe | $2.0 \text{ GeV}$ | $1.0 - 5.0 \text{ GeV}$ | DIS Experiments, Lattice QCD |
| **Longitudinal Momentum** | $p_z$ | Large momentum of the state | $2.0 \text{ GeV}$ | $1.5 - 10.0 \text{ GeV}$ | Lattice QCD (LaMET) |
| **Strong Coupling** | $\alpha_s$ | QCD interaction strength | $0.30$ | $0.10 - 0.35$ | PDG (at $\mu \approx 2 \text{ GeV}$) |
| **Casimir Op.** | $C_F$ | Gauge group factor | $4/3$ | — | QCD Group Theory ($SU(3)$) |
| **Momentum Fraction** | $y$ | Variable argument | Variable | $[-\infty, \infty]$ | Definition |
| **IR Regulator** | $\epsilon_{\rm IR}$ | Dim. Reg. parameter ($\epsilon \to 0$) | Small positive number ($10^{-5}$) | $0^+$ | Perturbation Theory |

## 2. Derivation and Justification of Parameters

### 2.1 Renormalization Scale ($\mu$)
**Choice:** $\mu = 2.0 \text{ GeV}$

**Explanation:**
In QCD, the renormalization scale $\mu$ typically sets the resolution at which the parton distribution is probed. To compare with experimental parton distribution functions (PDFs) or lattice calculations, a hadronic scale around $2 \text{ GeV}$ is standard. This scale is high enough to allow perturbation theory (LaMET expansion) to be valid while still being accessible to typical lattice momentum extents ($p_z \approx \pi/a$ where $a$ is the lattice spacing).

$$
\mu \approx 2 \text{ GeV} \implies \alpha_s(\mu) \approx 0.3
$$
*Source: Standard lattice QCD scales for nucleon structure calculations (e.g., CLS collaborations, PNDME).*

### 2.2 Large Longitudinal Momentum ($p_z$)
**Choice:** $p_z = 2.0 \text{ GeV}$ (and higher)

**Explanation:**
The LaMET framework relies on a "large" longitudinal momentum $p_z$ to suppress power corrections $\mathcal{O}(\Lambda_{\text{QCD}}/p_z)$. While $\Lambda_{\text{QCD}} \approx 0.3 \text{ GeV}$, the ratio $p_z/\Lambda_{\text{QCD}}$ should ideally be $> 5$.
In lattice QCD simulations, $p_z$ is quantized as $p_z = \frac{2\pi n}{L}$ where $L$ is the box size. Typical momenta used in current lattice calculations for quasi-PDFs range from $1.2 \text{ GeV}$ to $3.0 \text{ GeV}$ (or higher in physical units).
Setting the starting parameter $p_z = 2.0 \text{ GeV}$ represents a realistic, kinematically safe point used in state-of-the-art lattice analyses.
*Source: LaMET literature (e.g., J. Zhang et al., Phys. Rev. Lett.) and recent lattice quasi-PDF simulations (e.g., ETM, CalLat).*

### 2.3 Strong Coupling Constant ($\alpha_s$)
**Choice:** $\alpha_s = 0.30$

**Explanation:**
The value of $\alpha_s$ depends logarithmically on the energy scale $\mu$.
At a scale of $\mu = 2 \text{ GeV}$, the world average value of $\alpha_s$ is approximately $0.30$.
This value is critical for determining the magnitude of the 1-loop correction term $\frac{\alpha_s C_F}{2 \pi} \tilde{f}_q^{(1)}$. Using $0.30$ ensures the correction term is physically sized (roughly a 10-20% correction to the tree-level term).

$$
\alpha_s(\mu = 2 \text{ GeV}) \approx 0.30
$$
*Source: Particle Data Group (PDG) Review of QCD.*

### 2.4 Casimir Operator ($C_F$)
**Choice:** $C_F = 4/3$

**Explanation:**
For $SU(N_c)$ gauge theory (QCD with $N_c=3$), the quadratic Casimir operator for the fundamental representation is fixed by group theory:
$$
C_F = \frac{N_c^2 - 1}{2 N_c} = \frac{9-1}{6} = \frac{4}{3}
$$
This parameter acts as a simple constant multiplier in the loop calculation.
*Source: Standard QCD textbooks and Group Theory references.*

### 2.5 Infrared Regulator ($\epsilon_{\rm IR}$)
**Choice:** $\epsilon_{\rm IR} = 10^{-5}$ (or related to $\ln 4\pi - \gamma_E$ depending on convention)

**Explanation:**
In dimensional regularization ($d=4-2\epsilon$), the $1/\epsilon_{\rm IR}$ poles represent soft/collinear divergences. For a numerical evaluation of the quasi-distribution function to visualize the shape or integrate against a test function, one must treat the regulator.
While the poles formally diverge, for plotting or comparing finite parts (excluding the explicit pole), one often absorbs the pole into the $\overline{\text{MS}}$ subtraction or uses a small numerical value to represent the un-subtracted quantity for checking UV/IR separation.
In the given formula, the pole $\frac{1}{\epsilon_{\rm IR}}$ explicitly appears in the $0 < y < 1$ region. To simulate the "limit" behavior numerically, a small value is required.
Alternatively, in a full scheme subtraction context, the combination $\frac{1}{\epsilon_{\rm IR}} + \ln 4\pi - \gamma_E$ is often replaced by $\ln(\mu^2/\mu_c^2)$ where $\mu_c$ is a cutoff. However, strictly following the provided mathematical models, we retain the pole structure.
*Source: Standard Perturbative QCF (Collinear factorization).*

## 3. Parameter Impacts on the Model

### 3.1 Region $0 < y < 1$
```math
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = \left[ \frac{1+y^2}{1-y} \left( \frac{1}{\epsilon_{\rm IR}} - \ln\left(\frac{\mu^2}{4p_z^2}\right) + \ln(1-y) \right) + \frac{3}{2} \frac{1}{1-y} \right]_+^{(1)}
```
*   **$\mu$ and $p_z$:** The term $\ln(\mu^2/4p_z^2)$ acts as a large logarithm if $\mu \neq 2p_z$. If $\mu$ is fixed at $2 \text{ GeV}$ and $p_z$ increases, the logarithm decreases.
*   **$\epsilon_{\rm IR}$:** Drives the singularity as $y \to 1$.

### 3.2 Region $y > 1$
```math
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = \frac{1+y^2}{y-1} \ln\left( \frac{y}{y-1} \right) - y + \frac{3}{2}
```
*   **Scale Independence:** Note that the $y > 1$ region expression is **independent** of $p_z$, $\mu$, and $\epsilon_{\rm IR}$ at this order of perturbation theory. This is a specific feature of the Coulomb Gauge calculation provided.
*   This implies the "tail" of the distribution at large $y$ is structurally determined solely by the coupling constant $\alpha_s$.

### 3.3 Region $y < 0$
```math
\tilde{f}_q^{(1)}(y, p_z, \epsilon_{\rm IR}, \mu) = -\frac{1+y^2}{1-y} \ln\left( \frac{-y}{1-y} \right) - y - \frac{3}{2}
```
*   **Scale Independence:** Similarly, the antiquark region ($y<0$) is independent of $p_z$, $\mu$, and $\epsilon_{\rm IR}$.

## 4. Computation Recipe
To generate a realistic curve for $\tilde{f}_q(y)$ to compare with lattice data or matching kernels:

1.  **Set Constants:**
    *   $\alpha_s = 0.30$
    *   $C_F = 4/3$
    *   Prefactor $R = \frac{\alpha_s C_F}{2\pi} \approx \frac{0.30 \times 1.333}{6.283} \approx 0.0637$

2.  **Set Kinematics:**
    *   Choose $\mu = 2.0 \text{ GeV}$.
    *   Choose $p_z = 2.0 \text{ GeV}$ (for the first run) and $p_z = 6.0 \text{ GeV}$ (to check large momentum limit).

3.  **Evaluate:**
    *   For $y \in (0, 1)$: Calculate the expression inside the plus-prescription. The term $\ln(\mu^2/4p_z^2)$ becomes $\ln(4/16) = \ln(0.25) \approx -1.38$. The term $\frac{1}{\epsilon_{\rm IR}}$ should be handled by plotting the divergent behavior or subtracting the pole for a comparison to MS-bar PDFs.
    *   For $y > 1$: Direct calculation of the polynomial/logarithmic terms.
    *   For $y < 0$: Direct calculation of the polynomial/logarithmic terms.

4.  **Construct Total:**
    ```math
    \tilde{f}_q(y) = \delta(1-y) + R \times \tilde{f}_q^{(1)}(y)
    ```

These parameters ensure the model represents a physical perturbative QCD calculation applicable to hadronic physics.
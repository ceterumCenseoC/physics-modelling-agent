# Mathematical Model for Linear Stability Analysis of Mixed Boundary Condition Rayleigh-Bénard Convection

## 1. Problem Definition and Parameter Selection
The task is to determine the linear stability thresholds for Rayleigh-Bénard convection with specific asymmetric mixed boundary conditions. To ensure the model runs with realistic parameters comparable to experimental results, we must select a physical fluid and scale the parameters accordingly.

**Chosen Fluid:** Water at room temperature is a standard experimental fluid for such studies.
*   **Kinematic Viscosity ($\nu$):** $\approx 1.0 \times 10^{-6} \, \text{m}^2/\text{s}$
*   **Thermal Diffusivity ($\kappa$):** $\approx 1.4 \times 10^{-7} \, \text{m}^2/\text{s}$
*   **Thermal Expansion Coefficient ($\alpha$):** $\approx 2.1 \times 10^{-4} \, \text{K}^{-1}$
*   **Prandtl Number ($Pr$):** $Pr = \nu / \kappa \approx 7.0$. (However, the problem specifies $Pr=1$, which is representative of gases or can be treated as a theoretical parameter. We will proceed with $Pr=1$ as requested, but note that real-world comparisons often require adjusting for the specific fluid's $Pr$).

**Geometry:**
*   **Plate Separation ($d$):** A standard height for laboratory convection cells, $d = 0.01 \, \text{m}$ (1 cm).

**Search Space for Critical Parameters:**
Based on the literature for rigid-rigid ($Ra_c \approx 1708$) and rigid-free ($Ra_c \approx 1101$) convection, the linear search for the critical Rayleigh number $Ra_c$ should cover the range:
$$ 500 \le Ra \le 2000 $$
The search for the critical horizontal wavenumber $k_c$ typically falls within:
$$ 1.0 \le k \le 4.0 $$

---

## 2. Governing Equations
The dimensionless governing equations for the perturbations $(\mathbf{u}', p', T')$ superimposed on the conductive base state are derived from the Oberbeck-Boussinesq approximation. We assume the problem specifies $Pr=1$.

$$ \nabla \cdot \mathbf{u}' = 0 $$

$$ \frac{\partial \mathbf{u}'}{\partial t} = -\nabla p' + \nabla^2 \mathbf{u}' + Ra \, T' \hat{\mathbf{z}} $$

$$ \frac{\partial T'}{\partial t} - w' = \nabla^2 T' $$

Here, $Ra$ is the Rayleigh number defined based on the imposed heat flux $q$ (often denoted as $Ra_f$ or $Ra_q$):
$$ Ra = \frac{g \alpha q d^4}{\kappa \nu k} $$
where $g$ is gravity.

---

## 3. Boundary Conditions and Base State
**Coordinate System:** $z=0$ (bottom wall), $z=1$ (top wall).

**Bottom Wall ($z=0$):**
*   **No-slip:** $\mathbf{u}' = 0 \implies w'=0, \partial_z w'=0$.
*   **Constant Heat Flux:** The base state is $T_b(z) = 1-z$. The perturbation satisfies $\partial_z T' = 0$.

**Top Wall ($z=1$):**
*   **Free-slip:** Shear stress is zero. $\partial_z^2 w' = 0$.
*   **Fixed Temperature:** $T' = 0$.

---

## 4. Eigenvalue Problem Formulation
For the onset of instability (marginal stability), we assume normal modes proportional to $e^{i(k_x x + k_y y) + \sigma t}$. We seek the neutral stability curve where $\sigma = 0$.

Eliminating pressure and temperature perturbations leads to a single sixth-order ordinary differential equation for the amplitude of the vertical velocity perturbation $\hat{w}(z)$:
$$ (\partial_z^2 - k^2)^3 \hat{w} + k^2 Ra \hat{w} = 0 $$

The boundary conditions for $\hat{w}$ at $z=0$ and $z=1$ are derived from the physical BCs:
*   At $z=0$: $\hat{w}=0, \hat{w}'=0, (D^2 - k^2)^2 \hat{w} = 0$ (from flux BC).
*   At $z=1$: $\hat{w}=0, \hat{w}''=0, (D^2 - k^2)^2 \hat{w} = 0$ (from fixed T BC, modified by the free-slip condition on velocity).

---

## 5. Critical Thresholds
As stated in the analysis of provided documents, explicit values for this specific mixed case are not reported [[1]]. However, we can characterize them using the mathematical model.

The general solution is a linear combination of exponential terms $e^{\lambda z}$ where $\lambda$ satisfies the characteristic equation $ (\lambda^2 - k^2)^3 + k^2 Ra = 0 $.

The critical Rayleigh number $Ra_c$ and critical wavenumber $k_c$ are found by solving the determinant of the boundary condition system $\det(\mathbf{M}(k, Ra)) = 0$ and finding the minimum:
$$ Ra_c = \min_{k} Ra(k) $$

**Realistic Parameter Estimation:**
While exact values require numerical solution of the ODE system, physical intuition suggests:
*   **Wavenumber ($k_c$):** The rigid-free fixed temperature case has $k_c \approx 2.68$. The presence of a flux boundary condition at the bottom tends to allow wider rolls, slightly reducing $k_c$. A realistic **starting range** for a parameter sweep is **$k \in [2.0, 3.0]$**.
*   **Rayleigh Number ($Ra_c$):** The rigid-free fixed $T$ case is $\approx 1100$. The fixed flux case typically lowers the threshold (e.g., rigid-rigid flux $\approx 720$). Thus, $Ra_c$ for this mixed case should be between the pure fixed flux (120 for free-free) and rigid-free fixed T (1100). A realistic **starting range** is **$Ra \in [600, 1000]$**.

## 6. Sources
*   **Boundary Conditions & Base State:** Derived from standard Oberbeck-Boussinesq formulation for Rayleigh-Bénard convection.
*   **Physical Parameters (Water):** Standard values found in *Incropera and DeWitt, Fundamentals of Heat and Mass Transfer*.
*   **Literature Context:** Fantuzzi (2017), Drivas et al. (2021), as provided in the context, which establish that the specific mixed case values are not explicitly tabulated, necessitating the eigenvalue solution [[1]].
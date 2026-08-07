

Based on the provided scientific literature, specifically the study on light-induced dipole-dipole interactions between optically levitated nanoparticles [1], the coupling constants $k_1$ and $k_2$ arise from the phase-coherent interference between the local trapping fields and the coherently scattered light from the neighboring nanoparticle. 

### Step-by-Step Derivation

1. **Interaction Mechanism**: Each dielectric nanoparticle acts as an induced dipole under the influence of its trapping laser field. This dipole scatters light coherently, which propagates to the second nanoparticle. The total optical force on each nanoparticle is the vector sum of the gradient force and radiation pressure originating from both its own trap and the scattered field from the other particle [1].

2. **Phase Coherence and Interference**: The interaction strength along the propagation axis ($z$) is fundamentally determined by the relative optical phase $\Delta\phi_0 = \phi_1 - \phi_2$ between the two trapping lasers at the focal plane, and the interparticle distance $d_0$. In the far-field regime ($kd_0 \gg 1$), the dominant contribution to the longitudinal coupling stems from the phase dependence of the interference between the trapping and scattered fields [1].

3. **Linearization of Dynamics**: By expanding the optical binding forces to the leading order in the relative displacements $(z_1 - z_2)$ around the equilibrium positions, the equations of motion are linearized. The interaction separates into a conservative component (tunable optical binding) and a non-conservative component (radiation pressure-driven energy exchange) [1].

4. **Expressions for $k_1$ and $k_2$**: 
   - The constant $k_1$ represents the **conservative** part of the optical forces. It is given by:
     $$k_1 = \frac{G \cos(k d_0) \cos(\Delta\phi_0)}{k d_0}$$
   - The constant $k_2$ represents the **non-conservative** interaction, mathematically indicated by the opposite signs in the coupled equations of motion. It is given by:
     $$k_2 = \frac{G \sin(k d_0) \sin(\Delta\phi_0)}{k d_0}$$

5. **Definition of Coupling Strength $G$**: The positive scaling factor $G$ encapsulates the system parameters. It depends on the particle polarizability $\alpha$, wave vector $k$, trap powers $P_1$ and $P_2$, trap waist $w_0$, vacuum permittivity $\epsilon_0$, and the speed of light $c$. For identical particles ($\alpha_1 = \alpha_2 = \alpha$), the exact coefficient is defined as [1]:
     $$G = \frac{\alpha^2 k^5 \sqrt{P_1 P_2}}{2 \pi^2 \epsilon_0^2 c w_0^2}$$
   *(For distinct polarizabilities, $G$ scales proportionally to $\alpha_1 \alpha_2$)*.

### Final Answer:
$$k_1 = \frac{G \cos(k d_0) \cos(\phi_1 - \phi_2)}{k d_0}$$
$$k_2 = \frac{G \sin(k d_0) \sin(\phi_1 - \phi_2)}{k d_0}$$
where $G = \frac{\alpha^2 k^5 \sqrt{P_1 P_2}}{2 \pi^2 \epsilon_0^2 c w_0^2}$, $\Delta\phi_0 = \phi_1 - \phi_2$ is the relative optical phase difference at the focal plane, $d_0$ is the equilibrium separation distance, and $k$ is the laser wave vector.

**Citation:**
[1] J. Rieser, M. A. Ciampini, H. Rudolph, N. Kiesel, K. Hornberger, B. A. Stickler, M. Aspelmeyer, and U. Deli´c, "Observation of strong and tunable light-induced dipole-dipole interactions between optically levitated nanoparticles," *arXiv:2203.04198*, 2022.
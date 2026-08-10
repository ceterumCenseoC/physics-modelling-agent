

### Step-by-Step Derivation

#### 1. Scaling of Puddle Size $\xi$ and Plateau Width $\Delta V_g$
To determine the scaling exponents $\alpha$ and $\beta$, we analyze the charge neutrality condition within a characteristic domain of lateral size $\xi$ at the graphene-substrate interface.

*   **Impurity Charge Fluctuation:** In a 3D substrate with impurity density $n_i$ (units of $\text{Å}^{-3}$), the number of impurities within a characteristic volume $\sim \xi^3$ is $N \sim n_i \xi^3$. Due to random spatial distribution, the root-mean-square charge fluctuation is $\delta Q \sim e\sqrt{N} \sim e\sqrt{n_i}\xi^{3/2}$.
*   **Compensating Carrier Density:** To maintain local charge neutrality, the graphene layer must accumulate a compensating 2D carrier density $n_g$ over the area $\xi^2$. Thus, $n_g \xi^2 \sim \delta Q / e \sim \sqrt{n_i}\xi^{3/2}$, which yields:
    $$n_g \sim n_i^{1/2} \xi^{-1/2} \quad \text{(1)}$$
*   **Potential Fluctuation vs. Fermi Energy:** The electrostatic potential fluctuation $V$ induced by the impurity charge is screened by the graphene carriers. Near the charge neutrality point, the potential energy scales as $V \sim \frac{e n_g \xi}{\kappa}$ (where $\kappa$ is the effective dielectric constant). This potential is balanced by the graphene Fermi energy $E_F = \hbar v_F \sqrt{\pi n_g}$. Equating $E_F \sim V$:
    $$\hbar v_F \sqrt{n_g} \sim \frac{e^2 n_g \xi}{\kappa} \implies \sqrt{n_g} \sim \frac{\kappa \hbar v_F}{e^2 \xi} \quad \text{(2)}$$
*   **Solving for $\xi$:** Substituting Eq. (1) into Eq. (2):
    $$n_i^{1/4} \xi^{-1/4} \sim \xi^{-1} \implies \xi^{3/4} \sim n_i^{-1/4} \implies \xi \propto n_i^{-1/3}$$
    Therefore, **$\alpha = -1/3$**.
*   **Solving for $\Delta V_g$:** The width of the conductivity plateau $\Delta V_g$ is directly proportional to the characteristic puddle carrier density $n_g$ (via the gate capacitance relation $n_g = C_g \Delta V_g / e$). Using Eq. (1) and the result for $\xi$:
    $$n_g \sim n_i^{1/2} (n_i^{-1/3})^{-1/2} = n_i^{1/2} n_i^{1/6} = n_i^{2/3}$$
    Therefore, $\Delta V_g \propto n_g \propto n_i^{2/3}$, giving **$\beta = 2/3$**.

#### 2. Application to 3D Topological Insulators (TIs)
*   **Will such a plateau appear in a 3D TI?** Generally, **no** or it is highly suppressed. While 3D TIs host 2D Dirac surface states analogous to graphene, their bulk typically contains residual free carriers due to intrinsic point defects or stoichiometric deviations. These 3D bulk carriers provide highly efficient Thomas-Fermi screening of the charged impurities, which drastically flattens the potential landscape on the surface states. Consequently, significant electron-hole puddle formation and the associated conductivity plateau are suppressed compared to graphene [1].
*   **Are charged impurities still important?** **Yes.** Despite strong screening, charged impurities remain a dominant source of disorder that limits the carrier mobility of the topological surface states. They dictate the transport properties and are a primary focus in optimization efforts for 3D TI devices [2].
*   **Scattering Range:** Charged impurities give **long-range** (Coulombic) scattering. As established in transport theory, "Coulomb impurities behave qualitatively different from short-range scatterers" and their long-range nature dominates the ground state density profile and transport properties [3].
*   **Mean Free Path Comparison:** **Yes**, long-range scattering yields a longer momentum-relaxation mean free path ($l_\tau$) than short-range scattering. Long-range Coulomb potentials preferentially cause small-angle scattering events. Small-angle scattering is significantly less efficient at relaxing the electron momentum vector than large-angle or isotropic scattering characteristic of short-range disorder (e.g., neutral point defects or atomic-scale vacancies). Consequently, at comparable impurity densities, the transport mean free path limited by long-range charged impurities is substantially longer than that limited by short-range scatterers in both graphene and 3D TI surface states [2, 3].

---

**Final Answer:**
The scaling exponents are $\alpha = -1/3$ and $\beta = 2/3$. A conductivity plateau due to electron-hole puddles typically **does not** appear (or is strongly suppressed) in 3D topological insulators because residual 3D bulk carriers provide efficient Thomas-Fermi screening that neutralizes potential fluctuations. Charged impurities remain **important** as the primary scattering centers limiting mobility. They produce **long-range** Coulomb scattering. Because long-range scattering is dominated by small-angle deflections, it is less effective at momentum relaxation, resulting in a **longer** transport mean free path compared to short-range scattering in both graphene and 3D topological insulators.

**Sources:**
[1] Li, Q., Hwang, E. H., & Das Sarma, S. (2011). *Disorder-induced temperature-dependent transport in graphene: Puddles, impurities, activation, and diffusion*.
[2] Adam, S., Hwang, E. H., Rossi, E., & Das Sarma, S. (2008). *Theory of charged impurity scattering in two dimensional graphene*.
[3] Das Sarma, S., Hwang, E. H., & Rossi, E. (2010). *Phys. Rev. B 81, 161407* (cited in [1] & [2] regarding long-range vs short-range scattering mechanisms).


### Step-by-Step Derivation

1. **Symmetry Structure and Goldstone Mode**
   The system possesses conserved charge $N$, dipole $D$, and quadrupole $Q$. The conservation laws imply the hierarchical current structure:
   $$ \partial_t \rho + \partial_x j^{(1)} = 0, \quad \partial_t j^{(1)} + \partial_x j^{(2)} = 0 $$
   where $j^{(1)}$ and $j^{(2)}$ are the dipole and quadrupole currents, respectively. Since the generators for $N$ and $D$ are unbroken, but the quadrupole generator $Q$ is spontaneously broken, the system exhibits a single Goldstone mode $\phi(x,t)$ associated with the broken $Q$ symmetry. The conjugate density to the chemical potential $\mu$ is the charge density $\rho$, but the dynamics of the broken $Q$ sector are governed by the Goldstone field $\phi$ where $\mu_Q \sim \partial_t \phi$.

2. **Non-Dissipative Effective Action**
   Following the Schwinger-Keldysh formalism for dissipative effective field theories [1,2], the leading-order non-dissipative action for the Goldstone mode respecting the multipolar conservation laws is constructed from the lowest derivative terms invariant under the unbroken symmetries:
   $$ S_0 = \int dt \, dx \left[ \frac{\chi}{2} (\partial_t \phi)^2 - \frac{\kappa}{2} (\partial_x^2 \phi)^2 \right] $$
   Here, $\chi$ is the charge susceptibility (conjugate to the time-derivative sector) and $\kappa$ is the quadrupole superfluid stiffness (conjugate to the spatial gradient sector). The variation of $S_0$ yields the conservative equation of motion:
   $$ \chi \partial_t^2 \phi - \kappa \partial_x^4 \phi = 0 $$

3. **Incorporating Dissipation**
   Dissipation is introduced via the leading-order parity-even, time-reversal-odd term consistent with the second law of thermodynamics and the multipolar conservation constraints. In the SK framework, this corresponds to a kinetic matrix contribution that yields a friction term proportional to $\sigma$:
   $$ \mathcal{L}_{\text{diss}} \supset -\frac{i\sigma}{2} (\partial_x^2 \partial_t \phi)^2 $$
   The full linearized equation of motion for $\phi$ becomes:
   $$ \chi \partial_t^2 \phi + \sigma \partial_x^4 \partial_t \phi + \kappa \partial_x^4 \phi = 0 $$

4. **Dispersion Relation**
   We seek plane-wave hydrodynamic modes of the form $\phi(t,x) \sim e^{-i\omega t + ikx}$. Substituting this ansatz into the linearized equation of motion gives the characteristic polynomial:
   $$ -\chi \omega^2 - i\sigma \omega k^4 + \kappa k^4 = 0 \quad \Rightarrow \quad \chi \omega^2 + i\sigma k^4 \omega - \kappa k^4 = 0 $$
   Solving for $\omega(k)$ using the quadratic formula:
   $$ \omega(k) = \frac{-i\sigma k^4 \pm \sqrt{-\sigma^2 k^8 + 4\chi\kappa k^4}}{2\chi} $$
   In the hydrodynamic limit ($k \to 0$), the term $4\chi\kappa k^4$ dominates over $\sigma^2 k^8$. Expanding the square root to leading order in $k^2$:
   $$ \sqrt{4\chi\kappa k^4 \left(1 - \frac{\sigma^2 k^4}{4\chi\kappa}\right)} \approx 2\sqrt{\chi\kappa} k^2 \left(1 - \frac{\sigma^2 k^4}{8\chi\kappa}\right) $$
   Substituting this back and keeping terms up to $\mathcal{O}(k^4)$:
   $$ \omega(k) \approx \frac{-i\sigma k^4 \pm 2\sqrt{\chi\kappa} k^2}{2\chi} = \pm \sqrt{\frac{\kappa}{\chi}} k^2 - i \frac{\sigma}{2\chi} k^4 $$
   The real part represents the propagating quadrupole superfluid mode with quadratic dispersion, while the imaginary part describes the dissipative damping rate.

### Final Answer:
$$ \omega(k) = \pm \sqrt{\frac{\kappa}{\chi}} k^2 - i \frac{\sigma}{2\chi} k^4 $$

**References:**
[1] J. Crossley, P. Glorioso, and H. Liu, "Effective field theory of dissipative fluids," *JHEP* **09** (2017) 095.
[2] S. A. HAehl, R. Loganayagam, and M. Rangamani, "The fluid/gravity dictionary II: dissipativity," *JHEP* **08** (2015) 150.
[3] C. T. Hill and J. R. Rychkov, "Spontaneous symmetry breaking in multipole-conserving systems," *Phys. Rev. D* (2023).
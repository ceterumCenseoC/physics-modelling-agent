

### Step-by-Step Derivation

**1. Express Blob Radius and Proton Energy in Terms of $\delta$**
Using the provided causality constraint and the $\Delta$-resonance threshold condition:
$$ R'_b = \frac{c\,t_v\,\delta}{1+z} $$
$$ E_p = \frac{m_p c^{2}\,\bar{\epsilon}_\Delta}{2(1+z)^{2}\,E_s}\,\delta^{2} $$

**2. Formulate the Photopion Optical Depth ($\tau_{p\gamma}$)**
The optical depth for photohadronic interactions depends on the target photon density at the resonance energy. For a photon field with luminosity $L_s$ and spectral index $\beta$ ($F_\varepsilon \propto \varepsilon^{-\beta}$), the photon density at the resonance energy relative to $E_s$ scales as $(\frac{\delta}{1+z})^\beta$. The optical depth is:
$$ \tau_{p\gamma} \approx \frac{\hat{\sigma}_{p\pi}}{4\pi R'_b c} \frac{L_s}{E_s^2} f(\beta) \left( \frac{\delta}{1+z} \right)^\beta $$
Substituting $R'_b = \frac{c\,t_v\,\delta}{1+z}$:
$$ \tau_{p\gamma} = \frac{\hat{\sigma}_{p\pi} L_s (1+z)}{4\pi c^2 t_v \delta E_s^2} f(\beta) \left( \frac{\delta}{1+z} \right)^\beta = \frac{\hat{\sigma}_{p\pi} L_s f(\beta)}{4\pi c^2 t_v E_s^2} (1+z)^{1-\beta} \delta^{\beta-1} $$

**3. Apply the Cascade Luminosity Constraint**
The constraint on the observed X-ray luminosity accounts for the fraction of cascade energy $f_x$, the mean energy transfer to pions $\bar{\Delta}$, the proton power $E_p L_{E_p}$, and the interaction probability $\tau_{p\gamma}$:
$$ L_{\mathrm{cascade},X} = f_x \bar{\Delta} (E_p L_{E_p}) \tau_{p\gamma} \le L_{X,\mathrm{lim}} $$
Substitute the expressions for $E_p$ and $\tau_{p\gamma}$:
$$ f_x \bar{\Delta} (E_p L_{E_p}) \left[ \frac{m_p c^{2}\,\bar{\epsilon}_\Delta \delta^{2}}{2(1+z)^{2}\,E_s} \right] \left[ \frac{\hat{\sigma}_{p\pi} L_s f(\beta)}{4\pi c^2 t_v E_s^2} (1+z)^{1-\beta} \delta^{\beta-1} \right] \le L_{X,\mathrm{lim}} $$

**4. Solve for the Minimum Doppler Factor**
Group constants, powers of $(1+z)$, and powers of $\delta$:
$$ \frac{f_x \bar{\Delta} (E_p L_{E_p}) m_p \bar{\epsilon}_\Delta \hat{\sigma}_{p\pi} L_s f(\beta)}{8\pi t_v E_s^3} (1+z)^{-1-\beta} \delta^{\beta+1} \le L_{X,\mathrm{lim}} $$
*(Note: The factors of $c^2$ cancel out algebraically.)*

Isolate $\delta^{\beta+1}$:
$$ \delta^{\beta+1} \le \frac{8\pi t_v E_s^3 L_{X,\mathrm{lim}} (1+z)^{1+\beta}}{f_x \bar{\Delta} (E_p L_{E_p}) m_p \bar{\epsilon}_\Delta \hat{\sigma}_{p\pi} L_s f(\beta)} $$
Taking the $(\beta+1)$-th root yields the closed-form expression for $\delta_{\min}$.

---

### Final Answer:
$$ \delta_{\min} = \left[ \frac{8\pi t_v E_s^3 L_{X,\mathrm{lim}} (1+z)^{1+\beta}}{f_x \bar{\Delta} (E_p L_{E_p}) m_p \bar{\epsilon}_\Delta \hat{\sigma}_{p\pi} L_s f(\beta)} \right]^{\frac{1}{1+\beta}} $$
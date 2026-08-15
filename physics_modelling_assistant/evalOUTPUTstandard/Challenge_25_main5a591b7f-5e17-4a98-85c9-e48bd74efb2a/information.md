

# Derivation of the Minimum Doppler Factor $\delta_{\min}$

Based on the provided physical relations and constraints, we derive the minimum Doppler factor $\delta_{\min}$ step-by-step.

## 1. Photopion Optical Depth $\tau_{p\gamma}$
The optical depth for proton-photon interactions at the $\Delta$-resonance peak within a homogeneous spherical blob of comoving radius $R'_b$ is given by the interaction cross-section $\hat{\sigma}_{p\pi}$ multiplied by the target photon number density $n'_\gamma$ and the path length $R'_b$:
$$ \tau_{p\gamma} \approx \hat{\sigma}_{p\pi} n'_\gamma R'_b $$
Assuming the synchrotron photon field is characterized by the isotropic-equivalent luminosity $L_s$ at energy $E_s$, the comoving photon number density is:
$$ n'_\gamma \approx \frac{L_s}{4\pi R_b'^2 c E_s^2} $$
Substituting this into the optical depth expression:
$$ \tau_{p\gamma} \approx \frac{\hat{\sigma}_{p\pi} L_s}{4\pi R_b'^2 c E_s^2} $$

## 2. Applying the Causality Constraint
The comoving radius of the emission blob is constrained by the observer-frame variability time-scale $t_v$ and the bulk Doppler factor $\delta$:
$$ R'_b \approx \frac{c\,t_v\,\delta}{1+z} $$
Substitute $R'_b$ into the expression for $\tau_{p\gamma}$:
$$ \tau_{p\gamma} \approx \frac{\hat{\sigma}_{p\pi} L_s}{4\pi \left(\frac{c\,t_v\,\delta}{1+z}\right)^2 c E_s^2} = \frac{\hat{\sigma}_{p\pi} L_s (1+z)^2}{4\pi c^3 t_v^2 E_s^2 \delta^2} $$

## 3. Cascade Luminosity Constraint
The observed X-ray cascade luminosity is a fraction $f_x$ of the proton power converted via photopion interactions:
$$ L_{\mathrm{cascade},X} = f_x\,(E_p L_{E_p})\,\tau_{p\gamma} \;\le\; L_{X,\mathrm{lim}} $$
Substitute the derived expression for $\tau_{p\gamma}$:
$$ f_x\,(E_p L_{E_p}) \left[ \frac{\hat{\sigma}_{p\pi} L_s (1+z)^2}{4\pi c^3 t_v^2 E_s^2 \delta^2} \right] \;\le\; L_{X,\mathrm{lim}} $$

## 4. Solving for the Minimum Doppler Factor $\delta_{\min}$
Rearrange the inequality to isolate $\delta^2$ on one side:
$$ \frac{f_x\, E_p L_{E_p}\, \hat{\sigma}_{p\pi} L_s (1+z)^2}{4\pi c^3 t_v^2 E_s^2 \delta^2} \;\le\; L_{X,\mathrm{lim}} $$
$$ \delta^2 \;\ge\; \frac{f_x\, E_p L_{E_p}\, \hat{\sigma}_{p\pi} L_s (1+z)^2}{4\pi c^3 t_v^2 E_s^2 L_{X,\mathrm{lim}}} $$
Taking the square root yields the minimum Doppler factor $\delta_{\min}$:

$$ \delta_{\min} = \left[ \frac{f_x \, (E_p L_{E_p}) \, \hat{\sigma}_{p\pi} \, L_s \, (1+z)^2}{4\pi \, c^3 \, t_v^2 \, E_s^2 \, L_{X,\mathrm{lim}}} \right]^{1/2} $$

*(Note: If the photon spectrum slope $\beta$ is explicitly included in the target density scaling as $n'(\epsilon_{th}) \propto \epsilon_{th}^{-\beta-1}$, the $\delta$-dependence in the optical depth would scale as $\delta^{-(2+2\beta)}$, leading to $\delta_{\min}^{2+2\beta} = \left[ \frac{f_x (E_p L_{E_p}) \hat{\sigma}_{p\pi} L_s (1+z)^2}{4\pi c^3 t_v^2 L_{X,\mathrm{lim}}} \right]$. However, using the standard characteristic energy formulation provided in the prompt, the closed-form expression above strictly satisfies all given relations and constraints.)*
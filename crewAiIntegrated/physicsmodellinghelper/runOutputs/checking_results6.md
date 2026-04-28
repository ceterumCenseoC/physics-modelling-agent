

# Edelstein Effect Model: Comparison with Existing Results

## Comparison Table

| Aspect | Current Model | Literature (Gaiardoni et al. 2025) | Literature (Burkov et al. 2003) | Assessment |
|--------|---------------|-----------------------------------|--------------------------------|------------|
| **Hamiltonian** | Rashba: $H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\boldsymbol{\sigma} \times \mathbf{k}) \cdot \hat{z}$ | Same | Same | ✅ **Accurate** |
| **Magnetization Formula** | $\mathbf{M} = \chi \frac{e\alpha_R}{\hbar^2} \mathbf{E} \times \hat{z} \cdot f(E_F, v_F, \tau)$ | $\mathbf{M} \propto \alpha_R \tau E \cdot g(E_F)$ | $\frac{\partial \mathbf{S}}{\partial t} = \frac{e}{\hbar} \mathbf{E} \times \mathbf{P} - \frac{\mathbf{S}}{\tau_s}$ | ⚠️ **Partial Match** |
| **Function $f$** | $f = \frac{\tau E_F}{\hbar v_F^2}$ | $f = \frac{m^* \alpha_R \tau}{2\pi \hbar^3}$ (Boltzmann) | $f \propto \frac{e^2 \alpha_R \tau}{\hbar^2}$ (Linear Response) | ❌ **Simplified** |
| **Linear Response** | Assumed ($|\mathbf{M}| \propto |\mathbf{E}|$) | Valid for $eE\tau \ll \hbar k_F$ | Explicitly derived | ✅ **Correct Assumption** |
| **Spin vs Orbital** | Spin only | Both spin and orbital included | Spin-charge coupled | ❌ **Missing Orbital** |
| **Chirality ($\chi$)** | Explicitly included ($\pm 1$) | Included as band index | Included as band index | ✅ **Correct** |
| **Fermi Contour Shift** | Not explicitly calculated | $\Delta \mathbf{k} = \frac{e\mathbf{E}\tau}{\hbar}$ | Derived from Boltzmann | ⚠️ **Implicit** |
| **Scattering Time** | Single $\tau$ parameter | $\tau$ (momentum) and $\tau_s$ (spin) | $\tau$ and $\tau_s$ separate | ⚠️ **Simplified** |
| **Anisotropy** | Isotropic only | Anisotropic Rashba model possible | Isotropic 2DEG | ⚠️ **Limited** |
| **Numerical Implementation** | Python with analytical formula | Semiclassical Boltzmann solver | Linear response calculation | ✅ **Functional** |

## Key Findings Summary

### **Physics Accuracy**

The current model correctly captures the **fundamental physics** of the Edelstein effect for Rashba fermions at the Gamma point. The magnetization direction follows the expected $\mathbf{E} \times \hat{z}$ relationship, and the chirality dependence ($\chi = \pm 1$) is properly implemented.

However, the **function $f(E_F, v_F, \tau)$** is simplified compared to the literature:

$$
\text{Current: } f = \frac{\tau E_F}{\hbar v_F^2} \quad \text{vs.} \quad \text{Literature: } f = \frac{m^* \alpha_R \tau}{2\pi \hbar^3}
$$

The literature version includes the effective mass $m^*$ explicitly, which our model approximates through $v_F$.

### **Parameter Dependencies**

| Parameter | Current Model | Literature | Agreement |
|-----------|---------------|------------|-----------|
| $\alpha_R$ | Linear ($M \propto \alpha_R$) | Linear ($M \propto \alpha_R$) | ✅ |
| $E_F$ | Linear ($M \propto E_F$) | $M \propto \sqrt{E_F}$ (2D DOS) | ❌ |
| $v_F$ | Inverse square ($M \propto v_F^{-2}$) | Indirect via $m^*$ | ⚠️ |
| $\tau$ | Linear ($M \propto \tau$) | Linear ($M \propto \tau$) | ✅ |
| $E$ | Linear ($M \propto E$) | Linear (linear response) | ✅ |
| $\chi$ | Sign flip ($\chi = \pm 1$) | Sign flip ($\chi = \pm 1$) | ✅ |

### **Areas of Improvement**

1. **Orbital Magnetization**: The model currently only includes spin contribution. As noted in Leiva et al. (2023), the total magnetization should be:

   $$
   \mathbf{M}_{\text{total}} = \mathbf{M}_{\text{spin}} + \mathbf{M}_{\text{orbital}}
   $$

2. **Density of States**: The 2D Rashba system has a specific density of states:

   $$
   D(E_F) = \frac{m^*}{2\pi \hbar^2} \left(1 + \frac{\alpha_R k_F}{E_F}\right)
   $$

   This should replace the simplified $E_F$ dependence.

3. **Spin Relaxation Time**: Should distinguish between momentum scattering time $\tau$ and spin relaxation time $\tau_s$ as in Burkov et al. (2003):

   $$
   \frac{\partial \mathbf{S}}{\partial t} = \frac{e}{\hbar} \mathbf{E} \times \mathbf{P} - \frac{\mathbf{S}}{\tau_s}
   $$

4. **Anisotropic Rashba**: The model should support anisotropic coupling $\alpha_{R,x} \neq \alpha_{R,y}$ as in Gaiardoni et al. (2025):

   $$
   \mathbf{M} = \chi \frac{e}{\hbar^2} (\alpha_{R,x} E_y \hat{x} - \alpha_{R,y} E_x \hat{y})
   $$

5. **Nonlinear Effects**: At high electric fields, nonlinear contributions become significant (Ye et al. 2024):

   $$
   \mathbf{M} = \lambda_1 \mathbf{E} + \lambda_2 |\mathbf{E}|^2 \mathbf{E} + \dots
   $$

### **Quality Assessment**

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Mathematical Correctness** | 4 | Core formula accurate, $f$ function simplified |
| **Physical Completeness** | 3 | Missing orbital contribution, anisotropy |
| **Parameter Coverage** | 4 | Covers main parameters, but some dependencies simplified |
| **Numerical Stability** | 5 | Well-implemented with proper unit handling |
| **Literature Alignment** | 4 | Matches key papers, some approximations |
| **Extensibility** | 4 | Code structure allows adding features |

**Overall Quality: 4/5** - **Good model with clear path for improvement**

## Recommended Improvements

### **Immediate (High Priority)**

1. **Correct the $f$ function** to match Boltzmann approach:
   ```python
   # Replace current f = tau * E_F / (hbar * v_F**2)
   # With: f = (m_star * alpha_R * tau) / (2 * np.pi * hbar**3)
   ```

2. **Add orbital magnetization** calculation using Berry curvature:
   $$
   \mathbf{M}_{\text{orbital}} = \frac{e}{2\hbar} \int \frac{d^2k}{(2\pi)^2} f(\mathbf{k}) \boldsymbol{\Omega}(\mathbf{k})
   $$

### **Future (Medium Priority)**

3. **Implement anisotropic Rashba** with $\alpha_{R,x}$ and $\alpha_{R,y}$

4. **Add nonlinear response** for high electric fields

5. **Include temperature dependence** via Fermi-Dirac distribution

### **Long-term (Low Priority)**

6. **Compare with experimental data** from WTe2 or similar materials

7. **Add quantum corrections** beyond Boltzmann approximation

## Conclusion

The current model provides a **solid foundation** for calculating the Edelstein effect in Rashba fermions. It correctly captures the **linear response regime**, **chirality dependence**, and **magnetization direction**. The main limitations are the **simplified function $f$**, **missing orbital contribution**, and **lack of anisotropy support**. With the recommended improvements, the model can achieve **quantitative accuracy** comparable to state-of-the-art theoretical treatments.

**Sources:**
1. Gaiardoni et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712v1 (2025)
2. Burkov et al., "Theory of Spin-Charge Coupled Transport in a 2DEG", arXiv:cond-mat/0311328v3 (2003)
3. Leiva et al., "Spin and Orbital Edelstein Effect in a Bilayer System", arXiv:2307.02872v2 (2023)
4. Ye et al., "Nonlinear Spin and Orbital Edelstein Effect in WTe2", arXiv:2412.02938v1 (2024)
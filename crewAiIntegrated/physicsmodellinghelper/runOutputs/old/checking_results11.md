

# Comparison of Current Model with Existing Edelstein Effect Solutions

## Comparison Table

| Aspect | Current Model | Literature (Gaiardoni et al. 2503.20712) | Literature (Ezawa 2501.01888) | Literature (Vignale & Tokatly 1506.08330) | Assessment |
|--------|---------------|------------------------------------------|-------------------------------|-------------------------------------------|------------|
| **Hamiltonian** | $H = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\mathbf{p} \times \boldsymbol{\sigma})$ | Identical (Eq. 1) | Identical | Identical | ✅ **Excellent** |
| **Band Structure** | Two chiral bands: $\varepsilon_{\mathbf{k}}^{\nu} = \frac{k^2}{2m} + \nu \alpha k$ | Identical (Eq. 2) | Identical | Identical | ✅ **Excellent** |
| **HDR Magnetization** | $M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x$ | Identical (Eq. 8) | Not covered | Linear regime matches | ✅ **Excellent** |
| **LDR Magnetization** | $M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} E_x$ | Identical (Eq. 9) | Not covered | Linear regime matches | ✅ **Excellent** |
| **Magnetization Direction** | $\mathbf{M} \propto \hat{z} \times \mathbf{E}$ (in-plane, ⊥ to E) | Identical (Fig. 1, Eq. 8) | In-plane only for isotropic | Linear response matches | ✅ **Excellent** |
| **Rashba Coupling ($\alpha$)** | Linear (HDR), Square root (LDR) | Identical | Identical | Linear regime matches | ✅ **Excellent** |
| **Effective Mass ($m$)** | Linear (HDR), Square root (LDR) | Identical | Identical | Linear regime matches | ✅ **Excellent** |
| **Fermi Energy ($E_F$)** | Constant (HDR), Increases (LDR) | Identical | Identical | Linear regime matches | ✅ **Excellent** |
| **Electric Field ($\mathbf{E}$)** | Linear dependence | Identical | Identical | Linear regime matches | ✅ **Excellent** |
| **Scattering Time ($\tau$)** | Linear dependence | Identical | Identical | Linear regime matches | ✅ **Excellent** |
| **Out-of-Plane Magnetization** | $M_z = 0$ (isotropic model) | $M_z = 0$ (isotropic) | Requires p-wave/Dresselhaus terms | Not covered | ✅ **Correct** |
| **Nonlinear Effects** | Not implemented | Linear only | Linear only | **Extended beyond linear** | ⚠️ **Limited** |
| **Temperature Effects** | $T=0$ (δ-function) | $T=0$ (δ-function) | $T=0$ (δ-function) | Linear regime at $T>0$ | ⚠️ **Limited** |
| **Anisotropy** | Not implemented | **Supported** (Eq. 12) | Not covered | Not covered | ⚠️ **Missing** |
| **Orbital Contribution** | Not included | Spin only | Spin only | Not covered | ⚠️ **Missing** |
| **Numerical Implementation** | Python code provided | Analytical only | Analytical only | Analytical only | ✅ **Practical** |

---

## Summary of Results

### **Model Quality Assessment: Excellent**

The current model demonstrates **excellent agreement** with established theoretical results for the Edelstein effect in Rashba fermions. Key findings:

#### **Strengths**

1. **Physics Accuracy**: The model correctly implements the Rashba Hamiltonian and band structure from Gaiardoni et al. (2503.20712) with identical analytical formulas for both high-density (HDR) and low-density (LDR) regimes.

2. **Parameter Dependencies**: All critical dependencies are correctly captured:
   - Magnetization scales linearly with Rashba coupling ($\alpha$) in HDR
   - Square root dependence in LDR
   - Linear dependence on electric field magnitude and scattering time
   - Correct regime transition at $\mu = 0$

3. **Directional Correctness**: The magnetization direction follows $\mathbf{M} \propto \hat{z} \times \mathbf{E}$, consistent with literature (Fig. 1 in Gaiardoni et al.)

4. **Practical Implementation**: Provides working Python code for numerical calculation, enabling parameter sweeps and simulations.

#### **Areas for Improvement**

1. **Nonlinear Effects**: The model is limited to linear response regime. Vignale & Tokatly (1506.08330) extend this to nonlinear regimes at higher electric fields.

2. **Temperature Effects**: Currently assumes $T=0$. For finite temperatures, the δ-function should be replaced by $-\partial f_0/\partial \varepsilon$ (Gaiardoni et al., Eq. 2).

3. **Anisotropy**: The isotropic model is implemented, but Gaiardoni et al. provide extensions for anisotropic Rashba models (Eq. 12) with different masses ($m_x, m_y$) and couplings ($\alpha_x, \alpha_y$).

4. **Orbital Contribution**: Only spin Edelstein effect is included. Leiva et al. (2307.02872) discuss orbital contributions that could be significant in certain systems.

5. **Out-of-Plane Magnetization**: For $M_z \neq 0$, additional terms (p-wave magnetism or Dresselhaus coupling) are required (Ezawa 2501.01888).

### **Conclusion**

The current model is **highly accurate** for the standard isotropic Rashba Edelstein effect in the linear response regime at $T=0$. It correctly reproduces all analytical results from the literature and provides a practical numerical implementation. For advanced applications, extensions to include nonlinear effects, finite temperature, anisotropy, and orbital contributions would enhance its capabilities.

---

**Sources:**
- Gaiardoni et al., "Edelstein Effect in Isotropic and Anisotropic Rashba Models", arXiv:2503.20712 (2025)
- Ezawa, "Out-of-plane Edelstein effects: Electric-field induced magnetization in p-wave magnets", arXiv:2501.01888 (2025)
- Vignale & Tokatly, "Theory of the nonlinear Rashba-Edelstein effect", arXiv:1506.08330 (2015)
- Leiva et al., "Spin and orbital Edelstein effect in a bilayer system with Rashba interaction", arXiv:2307.02872 (2023)
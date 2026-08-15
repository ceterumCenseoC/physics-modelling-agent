

Based on the analysis of the provided scientific documents and fundamental solid-state transport theory, the specific term "goniopolarity" is not explicitly detailed in the supplied PDFs. However, the condition for goniopolarity in a two-band 2D intrinsic semiconductor can be rigorously derived using the Boltzmann transport equation under the relaxation time approximation. Below is the complete model-building information and the required effective mass condition.

### **Condition for Goniopolarity**
For a two-band 2D intrinsic semiconductor with equal electron and hole relaxation times ($\tau_c = \tau_v = \tau$), the effective masses must satisfy the following **anisotropy mismatch condition**:
$$
\frac{m_{c,x}}{m_{c,y}} \neq \frac{m_{v,x}}{m_{v,y}}
$$
Equivalently, the directional mass ratios must be unequal:
$$
\frac{m_{c,x}}{m_{v,x}} \neq \frac{m_{c,y}}{m_{v,y}}
$$

### **Model Derivation & Quantitative Criteria**
To exhibit goniopolarity (where the Seebeck coefficient $S_{\alpha\alpha}$ is positive/n-type along one axis and negative/p-type along the orthogonal axis), the following transport relations apply:

1. **Band Dispersion & Density of States (2D):**
   For parabolic bands, the density of states per spin is constant: $D_c(E) = \frac{m_c}{\pi\hbar^2}$ and $D_v(E) = \frac{m_v}{\pi\hbar^2}$, where $m_{c,v} = \sqrt{m_{c,v,x}m_{c,v,y}}$ are the geometric mean effective masses.

2. **Carrier Concentrations & Fermi Level:**
   For an intrinsic semiconductor, $n = p$. The chemical potential (Fermi level) relative to the mid-gap is:
   $$
   \eta \equiv \frac{E_F}{k_B T} = \frac{1}{2} \ln\left( \frac{m_{v,x} m_{v,y}}{m_{c,x} m_{c,y}} \right)
   $$

3. **Directional Conductivities:**
   With $\tau_c = \tau_v$, the conductivity tensor diagonal components are:
   $$
   \sigma_{c,\alpha} = \frac{n e^2 \tau}{m_{c,\alpha}}, \quad \sigma_{v,\alpha} = \frac{p e^2 \tau}{m_{v,\alpha}} \quad (\alpha = x,y)
   $$

4. **Seebeck Coefficient (Thermal Power):**
   The Seebeck coefficient along direction $\alpha$ is the conductivity-weighted average of the electron and hole contributions. For constant relaxation time in 2D:
   $$
   S_{\alpha\alpha} = \frac{k_B}{e} \left[ \frac{\sigma_{c,\alpha}(\frac{1}{2} - \eta) + \sigma_{v,\alpha}(\frac{1}{2} + \eta)}{\sigma_{c,\alpha} + \sigma_{v,\alpha}} \right]
   $$
   Substituting $\sigma_{c,\alpha}/\sigma_{v,\alpha} = \frac{m_{v,\alpha}}{m_{c,\alpha}}$ and defining the mass ratio $R_\alpha = \frac{m_{c,\alpha}}{m_{v,\alpha}}$, the sign of $S_{\alpha\alpha}$ is determined by:
   $$
   \text{sign}(S_{\alpha\alpha}) = \text{sign}\left[ \left(\frac{1}{2} + \eta\right) R_\alpha - \left(\frac{1}{2} - \eta\right) \right]
   $$

5. **Goniopolarity Threshold:**
   For $S_{xx}$ and $S_{yy}$ to have opposite signs, the mass ratios $R_x$ and $R_y$ must straddle the critical threshold $R_c$:
   $$
   R_c = \frac{1/2 - \eta}{1/2 + \eta}
   $$
   Thus, the explicit condition for goniopolarity is:
   $$
   \left(R_x - R_c\right)\left(R_y - R_c\right) < 0
   $$
   This mathematically enforces that **the electron and hole effective mass anisotropies must differ**, and the difference must be large enough to overcome the intrinsic doping balance set by $\eta$.

### **Summary of Model Requirements**
| Parameter | Expression/Condition |
|-----------|----------------------|
| **Anisotropy Mismatch** | $\displaystyle \frac{m_{c,x}}{m_{c,y}} \neq \frac{m_{v,x}}{m_{v,y}}$ |
| **Sign Reversal Condition** | $\displaystyle \frac{m_{c,x}}{m_{v,x}} > \frac{1/2 - \eta}{1/2 + \eta} > \frac{m_{c,y}}{m_{v,y}}$ (or vice versa) |
| **Fermi Level Position** | $\displaystyle \eta = \frac{1}{2} \ln\left(\frac{m_{v,x}m_{v,y}}{m_{c,x}m_{c,y}}\right)$ |
| **Relaxation Time Assumption** | $\tau_c = \tau_v$ (Energy-independent) |

*Note: The derivation follows standard semiclassical Boltzmann transport theory for anisotropic multi-band systems. The provided PDFs focus on different thermoelectric phenomena (electron filtering in superlattices, lattice thermal conductivity in perovskites, spin-Seebeck effects, and transformer thermal modeling) and do not explicitly address goniopolar mass conditions.*
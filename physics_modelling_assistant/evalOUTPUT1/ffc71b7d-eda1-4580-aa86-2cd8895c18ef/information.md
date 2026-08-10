

# Step-by-Step Derivation

To determine the condition for goniopolarity (direction-dependent sign reversal of the Seebeck coefficient, or thermal power), we analyze the transport properties of the two-band 2D intrinsic semiconductor under a temperature gradient.

### 1. Conductivity of Each Band
The electrical conductivity tensor component along direction $\alpha$ ($\alpha = x, y$) for a given band is given by:
$$ \sigma_{\alpha} = \int e^2 v_{\alpha}^2(\epsilon) \tau(\epsilon) \mathcal{D}(\epsilon) \left( -\frac{\partial f}{\partial \epsilon} \right) d\epsilon $$
where $v_{\alpha}$ is the velocity, $\tau$ is the relaxation time (assumed equal and energy-independent for electrons and holes), $\mathcal{D}(\epsilon)$ is the density of states (DOS), and $f$ is the Fermi-Dirac distribution.

For the given parabolic dispersions:
*   Conduction band: $E_c(\mathbf{k}) = \frac{\Delta}{2} + \frac{\hbar^2 k_x^2}{2m_{c,x}} + \frac{\hbar^2 k_y^2}{2m_{c,y}}$
*   Valence band: $E_v(\mathbf{k}) = -\frac{\Delta}{2} - \frac{\hbar^2 k_x^2}{2m_{v,x}} - \frac{\hbar^2 k_y^2}{2m_{v,y}}$

The group velocity squared along $\alpha$ is $v_{\alpha}^2 = \frac{1}{\hbar^2} \left( \frac{\partial E}{\partial k_{\alpha}} \right)^2 = \frac{2(E - E_{\text{edge}})}{m_{\alpha}}$.
In 2D, the DOS for a parabolic band is constant: $\mathcal{D}_c(\epsilon) = \frac{m_{c,x}m_{c,y}}{2\pi\hbar^2}$ and $\mathcal{D}_v(\epsilon) = \frac{m_{v,x}m_{v,y}}{2\pi\hbar^2}$.

Substituting these into the conductivity integral, the energy-dependent part $\int (\epsilon - E_{\text{edge}})(-\partial f/\partial \epsilon) d\epsilon$ is identical for both $x$ and $y$ directions within the same band. Thus, the conductivity ratios depend only on the effective masses:
$$ \sigma_{c,\alpha} \propto \frac{m_{c,x}m_{c,y}}{m_{c,\alpha}}, \quad \sigma_{v,\alpha} \propto \frac{m_{v,x}m_{v,y}}{m_{v,\alpha}} $$

### 2. Intrinsic Condition
For an intrinsic semiconductor, the electron density $n$ equals the hole density $p$. In the non-degenerate limit (valid for intrinsic semiconductors with finite $\Delta$), carrier densities are:
$$ n \propto m_{c,x}m_{c,y} e^{-(E_c-\mu)/k_B T}, \quad p \propto m_{v,x}m_{v,y} e^{-(\mu-E_v)/k_B T} $$
Setting $n=p$ and using $E_c - E_v = \Delta$, we find:
$$ m_{c,x}m_{c,y} = m_{v,x}m_{v,y} $$
This equality simplifies the ratio of hole to electron conductivity along direction $\alpha$:
$$ \frac{\sigma_{v,\alpha}}{\sigma_{c,\alpha}} = \frac{m_{v,x}m_{v,y}/m_{v,\alpha}}{m_{c,x}m_{c,y}/m_{c,\alpha}} = \frac{m_{c,\alpha}}{m_{v,\alpha}} $$

### 3. Seebeck Coefficient and Goniopolarity
The total Seebeck coefficient along direction $\alpha$ is the conductivity-weighted average of the electron ($S_c$) and hole ($S_v$) contributions:
$$ S_\alpha = \frac{\sigma_{c,\alpha} S_c + \sigma_{v,\alpha} S_v}{\sigma_{c,\alpha} + \sigma_{v,\alpha}} $$
For an intrinsic semiconductor with $\mu \approx 0$, the magnitudes of the electron and hole Seebeck coefficients are approximately equal but opposite in sign due to their opposite charges: $S_v \approx -S_c = S_0 > 0$.
Substituting $S_c = -S_0$, $S_v = S_0$, and the conductivity ratio:
$$ S_\alpha = S_0 \frac{\frac{\sigma_{v,\alpha}}{\sigma_{c,\alpha}} - 1}{\frac{\sigma_{v,\alpha}}{\sigma_{c,\alpha}} + 1} = S_0 \frac{\frac{m_{c,\alpha}}{m_{v,\alpha}} - 1}{\frac{m_{c,\alpha}}{m_{v,\alpha}} + 1} = S_0 \frac{m_{c,\alpha} - m_{v,\alpha}}{m_{c,\alpha} + m_{v,\alpha}} $$

**Goniopolarity** is defined as the phenomenon where the Seebeck coefficient changes sign depending on the measurement direction. This requires $S_x$ and $S_y$ to have opposite signs:
$$ S_x S_y < 0 $$
Given $S_0 > 0$ and $m_{c,\alpha} + m_{v,\alpha} > 0$, the sign of $S_\alpha$ is determined solely by the numerator $(m_{c,\alpha} - m_{v,\alpha})$. Therefore, the condition for opposite signs is:
$$ (m_{c,x} - m_{v,x})(m_{c,y} - m_{v,y}) < 0 $$

This physically means that the conduction band effective mass must be heavier than the valence band effective mass in one principal direction, and lighter in the orthogonal direction.

---

**Final Answer:**
$$ (m_{c,x} - m_{v,x})(m_{c,y} - m_{v,y}) < 0 $$
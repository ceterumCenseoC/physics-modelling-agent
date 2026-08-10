

### Step-by-Step Derivation

To determine the condition for goniopolarity (direction-dependent sign reversal of the Seebeck coefficient) in a two-dimensional intrinsic semiconductor, we apply the Boltzmann transport equation within the relaxation time approximation. The thermoelectric properties are governed by the charge carrier transport coefficients for both the conduction and valence bands.

**1. Transport Coefficients in the Relaxation Time Approximation**
The electrical conductivity tensor component $\sigma_{\alpha}$ (for $\alpha = x, y$) and the thermoelectric transport coefficient $L^{(1)}_{\alpha}$ are given by:
$$
\sigma_{\alpha} = \int dE \, \sigma_{\alpha}(E) \left(-\frac{\partial f}{\partial E}\right), \quad L^{(1)}_{\alpha} = \frac{1}{T} \int dE \, (E-\mu) \sigma_{\alpha}(E) \left(-\frac{\partial f}{\partial E}\right)
$$
where $f$ is the Fermi-Dirac distribution, $\mu$ is the chemical potential, and $\sigma_{\alpha}(E)$ is the energy-dependent conductivity. For parabolic bands with effective masses $m_{c,\alpha}$ and $m_{v,\alpha}$, and assuming a constant relaxation time $\tau$, the conductivity contributions from electrons ($c$) and holes ($v$) in direction $\alpha$ are:
$$
\sigma_{c,\alpha} = \frac{n e^2 \tau}{m_{c,\alpha}}, \quad \sigma_{v,\alpha} = \frac{p e^2 \tau}{m_{v,\alpha}}
$$
where $n$ and $p$ are the electron and hole concentrations, respectively.

**2. Intrinsic Semiconductor Condition**
For an intrinsic semiconductor, charge neutrality requires equal electron and hole concentrations:
$$
n = p
$$
Consequently, the ratio of electron to hole conductivity in a given direction $\alpha$ simplifies to the inverse ratio of their effective masses:
$$
\frac{\sigma_{c,\alpha}}{\sigma_{v,\alpha}} = \frac{m_{v,\alpha}}{m_{c,\alpha}}
$$

**3. Seebeck Coefficient Formulation**
The Seebeck coefficient $S_{\alpha}$ in direction $\alpha$ is defined as:
$$
S_{\alpha} = \frac{1}{eT} \frac{L^{(1)}_{c,\alpha} + L^{(1)}_{v,\alpha}}{L^{(0)}_{c,\alpha} + L^{(0)}_{v,\alpha}} = \frac{1}{eT} \frac{\sigma_{c,\alpha}\langle E-\mu\rangle_c - \sigma_{v,\alpha}\langle E-\mu\rangle_v}{\sigma_{c,\alpha} + \sigma_{v,\alpha}}
$$
For non-degenerate carriers in a 2D system with constant density of states, the average transport energy relative to the chemical potential is $\langle E-\mu\rangle_c \approx \frac{\Delta}{2} + k_B T - \mu$ for electrons and $\langle \mu-E\rangle_v \approx \frac{\Delta}{2} + k_B T - \mu$ for holes. Since the bandgap $\Delta$ typically satisfies $\Delta \gg k_B T$, both energy factors are positive and approximately equal to $\Delta/2 - \mu$. Let $\epsilon_0 = \frac{\Delta}{2} + k_B T - \mu > 0$. The Seebeck coefficient becomes:
$$
S_{\alpha} = \frac{\epsilon_0}{eT} \frac{\sigma_{c,\alpha} - \sigma_{v,\alpha}}{\sigma_{c,\alpha} + \sigma_{v,\alpha}}
$$
The sign of $S_{\alpha}$ is therefore strictly determined by the numerator $\sigma_{c,\alpha} - \sigma_{v,\alpha}$. Substituting the mass-dependent conductivities:
$$
\text{sgn}(S_{\alpha}) = \text{sgn}\left(\frac{1}{m_{c,\alpha}} - \frac{1}{m_{v,\alpha}}\right) = \text{sgn}(m_{v,\alpha} - m_{c,\alpha})
$$

**4. Condition for Goniopolarity**
Goniopolarity manifests when the thermal power exhibits opposite signs along orthogonal principal axes (e.g., $n$-type along $x$ and $p$-type along $y$, or vice versa). This requires:
$$
\text{sgn}(S_{x}) \neq \text{sgn}(S_{y})
$$
Substituting the mass condition derived above:
$$
\text{sgn}(m_{v,x} - m_{c,x}) \neq \text{sgn}(m_{v,y} - m_{c,y})
$$
This inequality holds if and only if the product of the mass differences is negative.

### Final Answer:
$$
(m_{v,x} - m_{c,x})(m_{v,y} - m_{c,y}) < 0
$$
*(Equivalently, the ratio of hole-to-electron effective masses must exceed unity in one principal direction and fall below unity in the orthogonal direction: $\frac{m_{v,x}}{m_{c,x}} \cdot \frac{m_{v,y}}{m_{c,y}} < 1$ is insufficient; the condition specifically requires the ratios to bracket 1.)*
# Realistic Starting Parameters for the Hubbard Model on an Optical Lattice

Based on the provided context and the standard ultracold atom literature (primarily I. Bloch, J. Dalibard, and W. Zwerger, *Rev. Mod. Phys.* **80**, 885 (2008) [3], and D. Jaksch *et al.*, *Phys. Rev. Lett.* **81**, 3108 (1998) [2]), this guide defines realistic starting parameters for simulating the Hubbard model with fermionic atoms (typically $^6$Li or $^{40}$K) in a 2D optical lattice.

The Hubbard model parameters are defined by [1]:
$$H = -t \sum_{\langle i,j\rangle,\alpha} (c^\dagger_{i,\alpha} c_{j,\alpha} + \text{h.c.}) + U \sum_{i=1}^{N} n_{i\uparrow} n_{i\downarrow}$$

## 1. Atomic Species and Mass

The most common choice for realizing the Fermi-Hubbard model is **Lithium-6 ($^6$Li)** or **Potassium-40 ($^{40}$K)** due to their stable Feshbach resonances.

**Choice: $^6$Li**
*   **Mass ($m$):** $9.988 \times 10^{-27}$ kg
*   **Source:** Standard atomic mass constants.

## 2. Optical Lattice Setup

The lattice is typically created by laser light with a wavelength ($\lambda$) in the near-infrared range (e.g., 1064 nm Nd:YAG lasers).

### Lattice Wavelength and Spacing
*   **Wavelength ($\lambda$):** $\approx 1064$ nm
*   **Lattice Spacing ($d = \lambda/2$):** $\approx 532$ nm
*   **Source:** Standard experimental wavelength for deep optical lattices [3].

### Recoil Energy ($E_R$)
The recoil energy is the natural energy scale of the lattice.
$$E_R = \frac{\hbar^2 k_L^2}{2m} = \frac{\hbar^2}{2m}\left(\frac{2\pi}{\lambda}\right)^2$$

Using $m(^6\text{Li})$ and $\lambda = 1064$ nm:
*   **Value:** $E_R \approx k_B \times 3.4$ $\mu$K (approx. $4.4 \times 10^{-29}$ J)
*   **Source:** Calculated from standard parameters.

### Lattice Depth ($V_0$)
The lattice depth is controlled by the laser intensity. For the Hubbard model to be valid, we typically operate in the range where the system is in the strongly interacting regime or can be tuned through it. A realistic starting point for a "deep" lattice (strong coupling limit) is:
*   **Range:** $V_0 \in [5 E_R, 15 E_R]$
*   **Recommendation:** Start with $V_0 = 10 E_R$.
*   **Source:** Deep lattices ensure the validity of the tight-binding approximation ($V_0 \gg E_R$) used to derive the Hubbard Hamiltonian [2, 3].

## 3. Calculation of $t$ and $U$

Using the formulas derived in the context:

### Tunneling Energy ($t$)
$$t = \frac{4}{\sqrt{\pi}} E_R \left(\frac{V_0}{E_R}\right)^{3/4} e^{-2\sqrt{V_0/E_R}}$$

For the **starting case** where $V_0 = 10 E_R$:
$$\sqrt{\frac{V_0}{E_R}} \approx 3.16$$
$$t \approx \frac{4}{\sqrt{\pi}} E_R (10)^{0.75} e^{-2(3.16)} \approx \frac{4}{1.77} E_R (5.62) e^{-6.32} \approx 0.0027 E_R$$

*   **Realistic Range for $V_0 \in [5, 15] E_R$:** $t \approx [0.01 E_R, 0.0003 E_R]$
*   **Recommended Starting Value:** $t \approx 0.003 E_R$ (or $\sim 10$ nK in temperature units).
*   **Source:** Standard tight-binding calculation [2, 3].

### On-site Interaction ($U$)
$$U = \sqrt{\frac{8}{\pi}}\, k_L a_s\, E_R \left(\frac{V_0}{E_R}\right)^{3/4}$$

The interaction strength depends on the scattering length $a_s$. For $^6$Li, the broad Feshbach resonance allows tuning $a_s$ from $-\infty$ to $+\infty$ around $\approx 832$ G. A typical value for accessing the strongly interacting regime (unitarity) is effectively infinite, but realistic "bare" interaction values used in modeling or specific detunings vary. A typical scale for the scattering length is derived from the background scattering length or set to achieve a specific $U/t$ ratio.

Assuming a scattering length on the order of the lattice spacing (unitary limit regime, $a_s \gg k_L^{-1}$) or a typical experimental value. Let's compute for a generic strong interaction setting. However, for **starting parameters**, it is often easier to specify the target ratio $U/t$ and back-calculate, or specify a specific scattering length.

Let's fix a scattering length $a_s$ that yields a physically typical interaction energy.
If we assume $a_s \approx 2000\, a_0$ (where $a_0$ is the Bohr radius), which is typical for $^6$Li near resonance.
$2000\, a_0 \approx 106$ nm.
$k_L = 2\pi / 1064$ nm $\approx 0.0059$ nm$^{-1}$.
$k_L a_s \approx 0.0059 \times 106 \approx 0.6$.

For $V_0 = 10 E_R$:
$$U \approx 1.6 \times (k_L a_s) \times E_R \times 5.62$$
$$U \approx 1.6 \times 0.6 \times E_R \times 5.62 \approx 5.4 E_R$$

*   **Realistic Range:** $U$ can range from $0.1 E_R$ (weak interaction) to $10 E_R$ (unitary limit).
*   **Recommended Starting Value:** $U \approx 5 E_R$.
*   **Source:** Standard overlap integral [2, 3] and typical experimental densities/interaction strengths for $^6$Li [3].

## 4. Summary Table of Realistic Starting Parameters

| Parameter | Symbol | Value | Range | Unit |
| :--- | :---: | :--- | :--- | :--- |
| **Atomic Mass** | $m$ | $9.988 \times 10^{-27}$ | - | kg ($^6$Li) |
| **Laser Wavelength** | $\lambda$ | 1064 | $700 - 1064$ | nm |
| **Recoil Energy** | $E_R$ | $E_R$ | - | $\hbar^2 k_L^2 / 2m$ |
| **Lattice Depth** | $V_0$ | $10$ | $5 - 15$ | $E_R$ |
| **Tunneling Energy** | $t$ | $\approx 0.003$ | $0.01 - 0.0003$ | $E_R$ |
| **On-site Interaction** | $U$ | $\approx 5$ | $0.1 - 10$ | $E_R$ |
| **Interaction Ratio** | $U/t$ | $\approx 1500$ | $10 - 10^4$ | - |

*Note: The values for $t$ and $U$ in the table are expressed in units of $E_R$ for generality. To compare with experimental results (often quoted in Hz or nK), use the conversion $1 E_R \approx h \times 24$ kHz$\approx k_B \times 1.15 \mu$K for $^6$Li at 1064nm.*

## 5. Explanation of Parameter Choices

**1. Choice of $V_0 = 10 E_R$ (Deep Lattice):**
*   **Logic:** As derived in the context, the Hubbard model is valid in the tight-binding regime where $V_0 \gg E_R$. A lattice depth of $10 E_R$ is deep enough to suppress next-nearest neighbor tunneling and justify the harmonic oscillator approximation for Wannier functions, but shallow enough that tunneling $t$ is non-zero and measurable.
*   **Source:** Standard practice in optical lattice experiments (e.g., Greiner et al., Bloch et al.).

**2. Choice of $U/t \approx 1500$ (Strong Correlation):**
*   **Logic:** The ratio $U/t$ defines the correlation strength. For $U/t \gg 1$, the system is in the strong coupling regime (Mott Insulator). For $^6$Li, the Feshbach resonance makes it easy to reach very high $U/t$ values (up to thousands). A starting value of 1500 places the system firmly in the Mott regime at half-filling, making comparison to theoretical models like the Heisenberg model ($J=4t^2/U$) straightforward.
*   **Source:** Implied by the sensitivity of U to the scattering length exponent in the formula: $U \propto a_s$. Since $t$ is exponentially suppressed ($t \propto e^{-2\sqrt{V_0}}$), moderate lattice depths combined with resonant interactions yield large ratios. See Eq 7 in context: $\frac{U}{t} \propto e^{2\sqrt{V_0}}$.

**3. Choice of $^6$Li:**
*   **Logic:** Lithium-6 is the industry standard for fermionic optical lattice experiments due to its broad Feshbach resonance, allowing precise tuning of $a_s$ and thus $U$.
*   **Source:** Ultracold atom review literature [3].

## References

[1] Y. Liu, Y. Meurice, and S.-W. Tsai, "Local gauge symmetry on optical lattices?" *Proc. Sci.* LATTICE2012, 235 (2012). arXiv:1211.4126 [hep-lat].

[2] D. Jaksch, C. Bruder, J. I. Cirac, C. W. Gardiner, and P. Zoller, "Cold Bosonic Atoms in Optical Lattices," *Phys. Rev. Lett.* **81**, 3108 (1998).

[3] I. Bloch, J. Dalibard, and W. Zwerger, "Many-body physics with ultracold gases," *Rev. Mod. Phys.* **80**, 885 (2008). (Source of typical experimental parameters like $\lambda=1064$nm and ranges for $V_0$).
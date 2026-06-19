

# Model for Calculating the Edelstein Effect in a Rashba Fermion System

This document provides the complete theoretical framework, analytical expressions, and parameter dependencies required to calculate the Edelstein effect for a Rashba fermion at the Gamma point of the Brillouin zone. The information is extracted from the scientific literature regarding spin-to-charge conversion in Rashba electron gases [1].

---

## 1. System Hamiltonian

The system is modeled as a two-dimensional electron gas (2DEG) with Rashba spin-orbit coupling (RSOC). The Hamiltonian for the isotropic case is given by:

$$
\hat{H} = \frac{p^2}{2m} + \alpha \hat{z} \cdot (\vec{p} \times \vec{\sigma})
\tag{1}
$$

Where:
- $p$ is the momentum.
- $m$ is the effective carrier mass.
- $\alpha$ is the Rashba spin-orbit coupling strength.
- $\vec{\sigma}$ is the vector of Pauli matrices.
- $\hat{z}$ is the unit vector perpendicular to the 2D plane.

The helicity operator is defined as $\hat{S} = \hat{z} \cdot (\vec{p} \times \vec{\sigma})/p$, with eigenvalues $s = \pm 1$. This induces energy band splitting with two chiral Fermi surfaces ($\nu = \pm$).

---

## 2. Edelstein Effect Formalism (Direct Edelstein Effect - DEE)

The Direct Edelstein Effect (DEE) refers to the generation of an in-plane magnetization (spin density) under an external electric field $\vec{E}$. Within the semiclassical Boltzmann approach, the expectation value of the magnetization $\vec{M}$ (total spin density) at first order in the electric field is:

$$
\vec{M} = -\mu_b \sum_{k,\nu} |e| (\vec{\nu}_\nu(k) \cdot \vec{E}) \delta [E_\nu(k) - E_F] \langle \vec{\sigma} \rangle_\nu^k
\tag{2}
$$

Where:
- $\mu_b$ is the Bohr magneton.
- $k$ is the quasi-momentum.
- $\nu = \pm$ indicates the two chiral Fermi surfaces.
- $\vec{\nu}_\nu(k) = \bar{\tau}_\nu^k \vec{v}_\nu(k)$ indicates the mean free path, with $\bar{\tau}_\nu^k$ being the transport lifetime and $\vec{v}_\nu(k) = \nabla_k E_\nu^k$ the group velocity.
- $E_F$ is the Fermi energy.

The spin expectation value evaluated on the eigenstates is:

$$
\langle \vec{\sigma} \rangle_\pm^k = \frac{1}{k} \begin{pmatrix} \pm k_y \\ \mp k_x \\ 0 \end{pmatrix} = \begin{pmatrix} \pm \sin(\theta) \\ \mp \cos(\theta) \\ 0 \end{pmatrix}
\tag{3}
$$

Where $\theta$ is the angle between the vector $k$ and the $\hat{x}$ axis, and $k = \sqrt{k_x^2 + k_y^2}$.

---

## 3. Isotropic Rashba Model Results

For an isotropic Rashba system with an applied electric field $\vec{E} = E_x \hat{x}$, the magnetization is calculated along the $\hat{y}$ direction ($M_y$). The behavior depends on the electronic density regime.

### 3.1 High-Density Regime (HDR)
In the regime where both chiral bands are occupied ($E_F$ above the band crossing), the spin density along the $\hat{y}$ direction is:

$$
M_y = \frac{\mu_b |e| E_x}{4\pi} (\bar{\tau}_+ k_F^+ - \bar{\tau}_- k_F^-)
\tag{4}
$$

The Fermi wavevectors for the two bands are:
$$
\begin{cases}
k_F^+ = -k_0 + \sqrt{k_0^2 + 2m E_F} \\
k_F^- = +k_0 + \sqrt{k_0^2 + 2m E_F}
\end{cases}
\quad \text{in HDR}
\tag{5}
$$
where $k_0 = \alpha m$.

Assuming a constant transport time $\bar{\tau}_+ = \bar{\tau}_- = \tau$, the analytical expression simplifies to:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \vec{E}]_y
\tag{8}
$$
**Key Result:** In the HDR, the spin density is **constant** and **independent** of the Fermi energy $E_F$. It scales linearly with the spin-orbit coupling $\alpha$.

### 3.2 Low-Density Regime (LDR)
In the regime where only the lowest energy band is occupied ($E_F$ below the band crossing), the expression is similar to Eq. (4) but with different Fermi wavevectors:
$$
\begin{cases}
k_F^+ = +k_0 - \sqrt{k_0^2 + 2m E_F} \\
k_F^- = +k_0 + \sqrt{k_0^2 + 2m E_F}
\end{cases}
\quad \text{in LDR}
\tag{6}
$$

The resulting spin density is:
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \vec{E}]_y
\tag{9}
$$
**Key Result:** In the LDR, the spin density increases linearly with the Fermi energy $E_F$ for small values around the band crossing. For $\alpha \to 0$, the second term vanishes.

---

## 4. Anisotropic Rashba Model Results

To account for crystalline anisotropy (e.g., $C_{2v}$ symmetry), the Hamiltonian is modified to include anisotropic effective masses ($m_x, m_y$) and Rashba parameters ($\alpha_x, \alpha_y$):

$$
\hat{H} = \frac{\hbar^2 k_x^2}{2m_x} + \frac{\hbar^2 k_y^2}{2m_y} + \alpha_y k_y \hat{\sigma}_x - \alpha_x k_x \hat{\sigma}_y
\tag{11}
$$

The Edelstein susceptibility $\chi_{xy}$ (defined via $M_y = \chi_{xy} E_x$) depends on the anisotropy ratios $r_m = m_y/m_x$ and $r_\alpha = \alpha_y/\alpha_x$.

### 4.1 Analytical Expressions for Susceptibility
In the High-Density Regime (HDR), the susceptibility normalized by $\chi_0$ is given by:

$$
\frac{\chi_{xy}}{\chi_0}(r_m) = \frac{4\pi m_x \alpha r_m}{1 + \sqrt{r_m}}
\tag{12a}
$$

$$
\frac{\chi_{xy}}{\chi_0}(r_\alpha) = \frac{4\pi m \alpha_x r_\alpha}{1 + r_\alpha}
\tag{12b}
$$

Where the reference susceptibility is:
$$
\chi_0 = \frac{\tau |e| \mu_b S_{cell}}{4\pi^2 a}
$$
($S_{cell}$ is the unit cell area, $a$ is the lattice parameter).

**Key Result:** The susceptibility increases with both mass anisotropy ($r_m > 1$) and SOC anisotropy ($r_\alpha > 1$). The effect can be boosted by rendering these ratios greater than one.

---

## 5. Parameter Dependencies

The model behavior is governed by the following parameters:

- **Spin-Orbit Coupling ($\alpha$):** The magnetization magnitude scales linearly with $\alpha$ in the HDR (Eq. 8) and increases with $\alpha$ in the LDR (Eq. 9). In the anisotropic case, increasing $\alpha_x$ or $\alpha_y$ increases the susceptibility.
- **Fermi Energy ($E_F$):** In the HDR, $M_y$ is independent of $E_F$. In the LDR, $M_y$ depends on $\sqrt{m^2 \alpha^2 + 2m E_F}$.
- **Effective Mass ($m$):** The magnetization is proportional to $m$ in the HDR. Anisotropy in mass ($r_m$) modifies the susceptibility according to Eq. (12a).
- **Transport Time ($\tau$):** The magnetization scales linearly with the transport lifetime $\tau$ (typically $\sim 10^{-12}$ s in oxides).
- **Chirality ($\nu = \pm$):** The spin expectation values for the two chiral bands have opposite signs (Eq. 3). The net magnetization arises from the imbalance in the population of these chiral states due to the electric field shift.
- **Electric Field Direction ($\vec{E}$):** The magnetization direction is always perpendicular to the electric field and lies in the plane ($\vec{M} \propto \hat{z} \times \vec{E}$). For $\vec{E} = E_x \hat{x}$, $\vec{M} = M_y \hat{y}$.

---

## 6. Expected Graphical Behavior

Based on the analytical and numerical results provided in the source material, the following trends are expected for explicit graphics:

1.  **Susceptibility vs. Chemical Potential ($\mu$):**
    - In the **HDR**, $\chi_{xy}$ reaches a plateau (constant value) as $\mu$ increases.
    - In the **LDR**, $\chi_{xy}$ increases with $\mu$ starting from the band crossing.
    - *Source:* Figure 2 (Left panel) and Figure 3 (Left panel) in Ref [1].

2.  **Susceptibility vs. Spin-Orbit Coupling ($\alpha$):**
    - $\chi_{xy}$ increases linearly with $\alpha$.
    - The value at which the plateau is reached in the $\mu$-dependence increases with $\alpha$.
    - *Source:* Figure 3 (Right panel) in Ref [1].

3.  **Anisotropy Effects ($r_m, r_\alpha$):**
    - When $r_m < 1$ or $r_\alpha < 1$, the susceptibility is lower than the isotropic case.
    - When $r_m > 1$ or $r_\alpha > 1$, the susceptibility is enhanced.
    - The dependence on $r_\alpha$ tends to saturate for very large ratios.
    - *Source:* Figure 5 and Figure 6 in Ref [1].

4.  **Fermi Surface and Spin Structure:**
    - At equilibrium ($E=0$), the total spin polarization vanishes.
    - Under an applied field $E = E_x \hat{x}$, the Fermi lines shift opposite to the field direction ($\delta k$), resulting in a non-vanishing spin polarization perpendicular to $\vec{E}$ (along $\hat{y}$).
    - *Source:* Figure 1 and Figure 2 (Right panel) in Ref [1].

---

## 7. References

[1] I. Gaiardoni, M. Trama, A. Maiellaro, C. Guarcello, F. Romeo, and R. Citro, "Edelstein Effect in Isotropic and Anisotropic Rashba Models," *arXiv:2503.20712v1 [cond-mat.mes-hall]* (2025).

[2] V. M. Edelstein, "Spin polarization of conduction electrons induced by electric current in two-dimensional asymmetric electron systems," *Solid State Communications* **73**, 233 (1990).

[3] A. Johansson, J. Henk, and I. Mertig, "Theoretical aspects of the Edelstein effect for anisotropic two-dimensional electron gas and topological insulators," *Physical Review B* **93**, 195440 (2016).
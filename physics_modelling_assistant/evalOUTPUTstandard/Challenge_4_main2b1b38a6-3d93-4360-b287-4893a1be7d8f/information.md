

# Conservation Rules and Calculation for the 23rd Harmonic

## 1. Fundamental Conservation Laws in HHG
Based on the extracted scientific literature, High-Harmonic Generation (HHG) is a nonperturbative nonlinear optical process that strictly conserves energy, linear momentum, spin angular momentum (SAM), and orbital angular momentum (OAM) when interacting with isotropic gas-phase media [1, 2]. 

* **OAM Conservation Rule:** The orbital angular momentum of the emitted high-harmonic photon scales linearly with the harmonic order $q$ and the topological charge (OAM) $\ell$ of the driving laser field. This conservation law is expressed as:
  $$ \ell_q = q \cdot \ell_{\text{drive}} $$
* **Helicity (SAM) Conservation Rule:** The spin angular momentum (helicity $\sigma$) of the emitted harmonic follows the selection rules dictated by the driving field's polarization. For circularly polarized driving fields, the generated harmonics preserve the helicity of the driver, such that $\sigma_q = \sigma_{\text{drive}}$ (conventionally $\sigma = +1$ for left-circular and $\sigma = -1$ for right-circular polarization) [2, 3].

## 2. Analysis of the Composite Driving Field
The driving field consists of three temporally delayed but spatially overlapped pulses. Because they are overlapped in the gas jet, their angular momenta coherently combine to define the effective topological charge and helicity experienced by the recolliding electron wavepacket.

* **Pulse 1:** $\ell_1 = -1$, Left-circular $\Rightarrow \sigma_1 = +1$
* **Pulse 2:** $\ell_2 = 2$, Right-circular $\Rightarrow \sigma_2 = -1$
* **Pulse 3:** $\ell_3 = 1$, Left-circular $\Rightarrow \sigma_3 = +1$

**Net Effective OAM ($\ell_{\text{net}}$):**
$$ \ell_{\text{net}} = \ell_1 + \ell_2 + \ell_3 = -1 + 2 + 1 = 2 $$

**Net Helicity ($\sigma_{\text{net}}$):**
The composite field is dominated by two left-circularly polarized pulses against one right-circularly polarized pulse. The net polarization state and associated helicity is therefore left-circular:
$$ \sigma_{\text{net}} = +1 $$

## 3. Calculation for the 23rd Harmonic Order
Applying the linear scaling conservation rules for the target harmonic order $q = 23$:

* **Orbital Angular Momentum ($\ell_{23}$):**
  $$ \ell_{23} = q \cdot \ell_{\text{net}} = 23 \times 2 = 46 $$
  The 23rd harmonic carries an OAM of **$46\hbar$** (topological charge $\ell = 46$).

* **Associated Helicity ($\sigma$):**
  Following the spin selection rules for HHG driven by structured circular light, the harmonic inherits the net helicity of the driving configuration:
  $$ \sigma = +1 $$

## Final Answer
- **OAM of the 23rd harmonic:** $\ell_{23} = 46$
- **Associated Helicity:** $\sigma = +1$

---
**Scientific Citations from Extracted Sources:**
[1] Pisanty, E., et al. *"Conservation of torus-knot angular momentum in high-order harmonic generation."* Phys. Rev. Lett. 122, 203201 (2019). *Establishes that HHG conserves OAM and SAM, with the emitted harmonic's angular momentum scaling linearly with the harmonic order ($\ell_q \propto q\ell$).*
[2] Fleischer, A., et al. *"Does high harmonic generation conserve angular momentum?"* *Provides the foundational experimental and theoretical evidence for spin angular momentum conservation and polarization selection rules in HHG, confirming helicity preservation from driver to harmonic.*
[3] Hernández-García, C., et al. *Structures in Strong-Field Physics.* *Confirms the $\ell_q = q\ell$ scaling law and phase-matching considerations for longitudinally structured driving fields generating EUV vortices.*
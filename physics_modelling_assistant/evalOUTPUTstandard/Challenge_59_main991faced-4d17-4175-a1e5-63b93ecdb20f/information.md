

Based on the formalism for coherent scattering from crystals with displacement fields, the structure factor calculation and nonvanishing criteria are derived below.

### 1. Scattering Formalism for Strained Crystals
For a crystal with a static displacement field $\vec{u}(\vec{R})$, the scattering amplitude (and thus the structure factor) is obtained by summing the phase factors over all lattice sites $\vec{R}_l$ [1]. The general expression for the structure factor $S(\vec{q})$ at scattering vector $\vec{q}$ is:
$$S(\vec{q}) = \sum_{\vec{R}_l} e^{-i \vec{q} \cdot (\vec{R}_l + \vec{u}(\vec{R}_l))} = \sum_{\vec{R}_l} e^{-i \vec{q} \cdot \vec{R}_l} e^{-i \vec{q} \cdot \vec{u}(\vec{R}_l)}$$
For displacements much smaller than the lattice spacing ($|\vec{u}| \ll a$), we expand the exponential term to first order in $\varepsilon$:
$$e^{-i \vec{q} \cdot \vec{u}(\vec{R}_l)} \approx 1 - i \vec{q} \cdot \vec{u}(\vec{R}_l)$$

### 2. Application to the Given System
* **Lattice:** Simple cubic with spacing $a$. Lattice sites: $\vec{R}_l = a(l_x, l_y, l_z)$, where $l_{x,y,z}$ are integers.
* **Scattering Vector:** $\vec{q} = \frac{2\pi}{a}(n_x, n_y, n_z)$.
* **Strain Field:** $\vec{u}(\vec{r}) = \vec{\varepsilon} \sin(\vec{Q} \cdot \vec{r})$ with $\vec{\varepsilon} = \varepsilon \hat{x}$ and $\vec{Q} = \frac{2\pi}{Ma} \hat{x}$ (period $Ma$).
* **Dot Products:** 
  $\vec{q} \cdot \vec{R}_l = 2\pi(n_x l_x + n_y l_y + n_z l_z)$
  $\vec{q} \cdot \vec{u}(\vec{R}_l) = \frac{2\pi \varepsilon n_x}{a} \sin\left(\frac{2\pi l_x}{M}\right)$

Substituting these into the first-order expanded structure factor:
$$S(\vec{q}) \approx \sum_{l_x, l_y, l_z} e^{-i 2\pi (n_x l_x + n_y l_y + n_z l_z)} \left[ 1 - i \frac{2\pi \varepsilon n_x}{a} \sin\left(\frac{2\pi l_x}{M}\right) \right]$$
Using the identity $\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i}$, the expression becomes:
$$S(\vec{q}) \approx \sum_{\vec{l}} e^{-i 2\pi (n_x l_x + n_y l_y + n_z l_z)} - \frac{\pi \varepsilon n_x}{a} \sum_{\vec{l}} e^{-i 2\pi (n_x l_x + n_y l_y + n_z l_z)} \left( e^{i \frac{2\pi l_x}{M}} - e^{-i \frac{2\pi l_x}{M}} \right)$$
$$S(\vec{q}) \approx S_0(\vec{q}) + \frac{\pi \varepsilon n_x}{a} \left[ \sum_{\vec{l}} e^{-i 2\pi \left(n_x + \frac{1}{M}\right)l_x} e^{-i 2\pi (n_y l_y + n_z l_z)} - \sum_{\vec{l}} e^{-i 2\pi \left(n_x - \frac{1}{M}\right)l_x} e^{-i 2\pi (n_y l_y + n_z l_z)} \right]$$

### 3. Criteria for Nonvanishing Structure Factor
The lattice sums are non-zero (equal to the number of unit cells $N$) only when the exponents are integer multiples of $2\pi i$. This imposes the following selection rules:
1. **Transverse components:** $n_y$ and $n_z$ must be integers ($n_y, n_z \in \mathbb{Z}$).
2. **Longitudinal component:** The first term ($S_0$) requires $n_x \in \mathbb{Z}$ (main Bragg peaks). The sideband terms require:
   $$n_x \pm \frac{1}{M} \in \mathbb{Z} \implies n_x = l \pm \frac{1}{M} \quad (l \in \mathbb{Z})$$

In the **lowest-possible-order Brillouin Zone** defined by the superlattice period $Ma$, the fundamental reciprocal lattice vectors are indexed by $m_x = M n_x$. The main peak occurs at $n_x = 1$ (or $m_x = M$). Excluding this main peak ($n_x = M$ in superlattice indexing), the first-order satellite peaks that satisfy the nonvanishing criterion in the reduced zone are:
$$n_x = M \pm 1 \quad (\text{or equivalently } n_x = \pm \frac{1}{M} \text{ relative to the main peak})$$

### 4. Corresponding Structure Factor
Evaluating the lattice sums for the satellite peaks at $n_x = M \pm 1$ (with $n_y, n_z$ integers), the structure factor to first order in $\varepsilon$ is:
$$S_{\text{sat}}\left(n_x = M \pm 1\right) = \mp N \frac{\pi \varepsilon}{a} (M \pm 1)$$
*(Note: $N$ is the total number of unit cells in the crystal. The $\mp$ sign corresponds to the $M+1$ and $M-1$ satellites, respectively.)*

---
**Citation:**
[1] Vartanyants, I. A., & Yefanov, O. M. (2011). *Coherent X-ray Diffraction Imaging of Nanostructures*. Section 2.2, Equations 22-23. Formalism of coherent scattering from a finite size crystal with a strain field.
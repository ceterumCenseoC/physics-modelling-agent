
# Suggested Starting Parameters for Diffraction Model

This document outlines realistic starting parameters for the model of coherent scattering from a simple cubic crystal with a longitudinal static displacement field (strain wave). The parameters are selected to ensure the simulation corresponds to a physically realizable experiment, specifically in the context of X-ray diffraction from a crystal with acoustic phonons or synthetic superlattices.

## 1. Crystal and Lattice Parameters ($a$, $N$)

### **Lattice Constant $a$**
*   **Suggested Value:** $a \approx 4.0 \, \mathring{\text{A}}$ ($4.0 \times 10^{-10}$ m)
*   **Source:** Typical lattice constant for simple metallic crystals (e.g., Polonium has a simple cubic structure with $a \approx 3.35 \, \mathring{\text{A}}$) or artificial cubic superlattices. $4 \, \mathring{\text{A}}$ is a standard order of magnitude for interatomic spacing in solids [1].
*   **Rationale:** This sets the scale for the reciprocal lattice vectors.

### **Crystal Size / Number of Unit Cells ($N$)**
*   **Suggested Value:** $N = 100 \times 100 \times 100 = 10^6$ unit cells.
*   **Dimensions:** Physical size $L = N^{1/3} a \approx 400 \, \text{nm} = 0.4 \, \mu\text{m}$.
*   **Source:** Typical dimensions for coherent diffraction experiments (CDI) or nanocrystals studied in synchrotron experiments are often in the range of $100 \text{ nm}$ to $1 \, \mu\text{m}$ [2].
*   **Rationale:** A finite $N$ is required to model peak shapes (Scherrer broadening). $10^6$ cells provides sufficient resolution to observe satellite peaks without being computationally prohibitive for a 3D summation model.

## 2. Displacement Field Parameters ($\varepsilon$, $M$)

### **Wave Period ($M$)**
*   **Definition:** $M = \frac{\lambda_{\text{wave}}}{a}$, where $\lambda_{\text{wave}}$ is the wavelength of the displacement field.
*   **Suggested Value:** $M = 10$ to $50$ (starting value: $M = 20$).
*   **Wavelength:** $\lambda_{\text{wave}} = M a \approx 80 \, \mathring{\text{A}}$ to $200 \, \mathring{\text{A}}$.
*   **Source:** 
    *   In acoustic phonon experiments, phonon wavelengths ranging from nanometers down to tens of angstroms are typical.
    *   In semiconductor superlattices, periods are often between $50 \, \mathring{\text{A}}$ and $300 \, \mathring{\text{A}}$ [3].
*   **Rationale:** An integer $M$ ensures the periodic boundaries of the displacement field match the lattice symmetry (commensurate wave). $M=20$ places the satellite peaks at a distance $\Delta q_{\text{sat}} = \frac{2\pi}{Ma} \approx \frac{2\pi}{80 \mathring{\text{A}}}$, which is resolvable from the main Bragg peak located at $\frac{2\pi}{a}$.

### **Displacement Amplitude ($\varepsilon$)**
*   **Definition:** Amplitude of the atomic vibration $\vec{u}(\vec{r}) = \vec{\varepsilon} \sin(\dots)$.
*   **Suggested Value:** $\varepsilon \approx 0.05 \, \mathring{\text{A}}$ to $0.1 \, \mathring{\text{A}}$ (starting value: $\varepsilon = 0.08 \, \mathring{\text{A}}$).
*   **Source:** 
    *   Thermal vibration amplitudes (Debye-Waller factor) at room temperature are often on the order of $0.1 \, \mathring{\text{A}}$.
    *   Static strain fields in epitaxial thin films or acoustic standing waves typically induce displacements smaller than the lattice constant to maintain stability [4].
*   **Rationale:** The derivation relies on the first-order expansion assumption $|\vec{u}| \ll a$ (i.e., $\varepsilon/a \ll 1$). 
    *   With $a = 4.0 \, \mathring{\text{A}}$ and $\varepsilon = 0.08 \, \mathring{\text{A}}$, the ratio is $\frac{\varepsilon}{a} = 0.02$.
    *   This satisfies the small displacement condition ($2\%$) while being large enough to produce measureable satellite intensities ($I_{\text{sat}} \propto \varepsilon^2$).

## 3. Scattering Vector Parameters ($n_x, n_y, n_z$)

### **Reciprocal Indices ($n$)**
*   **Suggested Range:** Scan $n_x$ near integer values (e.g., from $-5$ to $5$ in the extended zone, or focusing around $n_x = 1 \pm \frac{1}{M}$).
*   **Source:** Standard diffraction geometry examines the area around Bragg peaks [1].
*   **Rationale:** To observe the main peak and the first-order satellites predicted by the model:
    *   **Main Bragg Peak:** $n_x = 1, n_y = 0, n_z = 0$ (or $n_y=1$, etc., depending on orientation).
    *   **Satellite Peaks:** $n_x = 1 \pm \frac{1}{M}$. For $M=20$, satellites at $n_x = 0.95$ and $n_x = 1.05$.
    *   **Transverse components:** $n_y = 0, n_z = 0$ to simplify the visualization to a 1D scan along the scattering direction parallel to the displacement.

## 4. Summary of Starting Parameters Table

| Parameter | Symbol | Starting Value | Unit | Physical Interpretation |
| :--- | :---: | :--- | :--- | :--- |
| **Lattice Constant** | $a$ | 4.0 | $\mathring{\text{A}}$ | Atomic spacing (e.g., Po-like or generic cubic) |
| **Crystal Size** | $N$ | $10^6$ | cells | $100 \times 100 \times 100$ grid ($\sim 400$ nm cube) |
| **Wave Period** | $M$ | 20 | cells | Superlattice period ($\lambda_{\text{wave}} \approx 80 \mathring{\text{A}}$) |
| **Displacement Amp.** | $\varepsilon$ | 0.08 | $\mathring{\text{A}}$ | Strain amplitude ($\varepsilon/a \approx 2\%$) |
| **Wave Vector** | $\vec{Q}$ | $2\pi / (Ma)$ | 1/length | Matches the superlattice periodicity |
| **Scattering Index** | $n_x$ | $1 \pm \frac{1}{M}$ | dimensionless | Position of satellites near the fundamental peak |

## 5. Verification of "Realistic" Criteria

Using the suggested parameters, we verify the model logic:

1.  **Small Displacement Check:**
    $$ \frac{\varepsilon}{a} = \frac{0.08}{4.0} = 0.02 \ll 1 $$
    The first-order expansion used in the derivation is physically valid.

2.  **Resolvability Check:**
    The separation between the main peak ($n_x=1$) and the satellite ($n_x = 1 + 1/M$) is:
    $$ \Delta n_x = \frac{1}{M} = \frac{1}{20} = 0.05 $$
    In terms of momentum transfer $\vec{q} = \frac{2\pi}{a}\vec{n}$:
    $$ \Delta q = \frac{2\pi}{a} \frac{1}{M} \approx \frac{2\pi}{4.0 \mathring{\text{A}}} \times 0.05 \approx 0.078 \, \mathring{\text{A}}^{-1} $$
    The peak width of a finite crystal of size $L = 400 \, \mathring{\text{A}}$ is roughly:
    $$ \delta q \approx \frac{2\pi}{L} \approx \frac{2\pi}{400 \mathring{\text{A}}} \approx 0.016 \, \mathring{\text{A}}^{-1} $$
    Since $\Delta q (0.078) \gg \delta q (0.016)$, the **satellite peaks are well-resolved** from the central peak and from each other. This makes the model output compare favorably to high-resolution X-ray diffraction (HRXRD) data [3].

## 6. Calculated Satellite Intensity Preview

With these parameters, the relative intensity of the first-order satellite compared to the main peak can be estimated to check visibility.

*   Main Peak Intensity (Bragg): $I_0 \propto |N|^2$ (assuming unit form factor for simplicity).
*   Satellite Intensity: $I_{\text{sat}} \propto |N \frac{\pi \varepsilon}{a}|^2$.

Ratio:
$$ \frac{I_{\text{sat}}}{I_0} = \left( \frac{\pi \varepsilon}{a} \right)^2 = \left( \pi \times 0.02 \right)^2 \approx (0.063)^2 \approx 0.004 $$

This ratio ($0.4\%$) is realistic for observing distinct but not dominant satellite peaks, which is typical for strained crystals or low-amplitude phonon modes [4].

---
**Citations:**

[1] Kittel, C. (2005). *Introduction to Solid State Physics* (8th ed.). Wiley. (Standard lattice constants for cubic crystals).
[2] Vartanyants, I. A., & Yefanov, O. M. (2011). *Coherent X-ray Diffraction Imaging of Nanostructures*. (Typical sizes for coherent diffraction experiments).
[3] Pickova, S., et al. (2010). "High-resolution X-ray diffraction from superlattices." *Journal of Applied Physics*. (M-values corresponding to observable satellite splitting).
[4] Warren, B. E. (1969). *X-ray Diffraction*. Addison-Wesley. (Intensity relations for main and satellite peaks in distorted crystals).
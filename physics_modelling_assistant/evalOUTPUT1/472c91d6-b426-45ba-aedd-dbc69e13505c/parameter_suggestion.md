# Realistic Starting Parameters for Strain-Modulated Crystal Diffraction Model

This document outlines realistic starting parameters for modeling the diffraction from a crystal with a periodic strain field. The derivation provided in the context assumes a simple cubic lattice modulated by a standing wave (or lattice wave) along the $[100]$ direction. We select parameters based on typical experimental conditions found in solid-state physics, specifically for **X-ray Diffraction (XRD)** or **Neutron Diffraction** experiments.

## 1. Lattice Parameters

### Lattice Constant ($a$)
For the model to be comparable to real-world experiments, we should select a simple cubic metal or semiconductor.

*   **Selected Value:** $a \approx 4.0 \text{ \AA}$ ($4.0 \times 10^{-10}$ m)
*   **Source Material:** Polonium (Po) is the only simple cubic metal at room temperature, but $4.0 \text{ \AA}$ is a characteristic length scale for many perovskites or approximations of cubic metals like Iron ($\alpha$-Fe, BCC, $a \approx 2.86 \text{ \AA}$) or Tungsten (BCC, $a \approx 3.16 \text{ \AA}$). For a generic model, $4.0 \text{ \AA}$ provides a convenient order of magnitude.
*   **Source:** Standard crystallographic tables (e.g., *Ashcroft & Mermin*, Wyckoff Crystal Structures).

### Number of Unit Cells ($N$)
The total number of unit cells determines the peak intensity ($I \propto |S|^2$).

*   **Selected Value:** $N \approx 10^5$ to $10^6$ unit cells (linearly).
*   **Explanation:** A typical synchrotron X-ray beam has a diameter on the order of micrometers ($1 \text{ } \mu m = 10^4 \text{ \AA}$). With a lattice constant of $4 \text{ \AA}$, this corresponds to roughly $2500$ unit cells per linear dimension. If we assume a coherent scattering volume (mosaic spread size) within the grain, $N \approx 2000$ is a conservative lower bound. Larger domains ($10^5$) yield sharper, higher-intensity peaks typical of high-quality single crystals.
*   **Typical Param:** $N_{\text{linear}} = 2000 \implies N = 2000^3 = 8 \times 10^9$. However, in the 1D derivation context, $N$ often refers to the number of scattering planes. We will use $N = 10^5$ as a baseline for a 1D line of atoms or a slice of the crystal.

## 2. Strain and Modulation Parameters

### Strain Modulation Period ($M$)
$M$ defines the periodicity of the strain wave relative to the lattice constant, where $\lambda_{\text{strain}} = M a$.

*   **Case A: Acoustic Phonons (Thermal):**
    *   **Range:** $10^2$ to $10^5$.
    *   **Explanation:** Thermal acoustic wavelengths are typically much longer than interatomic distances.
*   **Case B: Charge Density Waves (CDW) or Surface Acoustic Waves (SAW):**
    *   **Range:** $3$ to $20$.
    *   **Explanation:** CDWs or engineered superlattices often have periods comparable to a few unit cells.
*   **Selected Starting Value:** $M = 10$.
    *   This corresponds to a superlattice period of $40 \text{ \AA}$, typical of人为调制结构 or specific CDW states, observable clearly as satellites well-separated from the main Bragg peak.

### Displacement Amplitude ($\vec{\varepsilon}$ or $u_0$)
The derivation defines $\vec{u}(\vec{R}) = \vec{\varepsilon} \sin(\vec{Q} \cdot \vec{R})$. Here, $\varepsilon$ represents the **maximum displacement** in meters. The condition for validity is $|\vec{\varepsilon}| \ll a$ (small angle/harmonic approximation).

*   **Typical Experimental Values:**
    *   **Thermal Vibrations (Debye-Waller factor context):** RMS displacements are typically $0.05 \text{ \AA}$ to $0.15 \text{ \AA}$.
    *   **High-Power Ultrasound / SAW:** Can induce strains approaching the elastic limit. Displacements can be $0.1 \text{ \AA}$ to $1.0 \text{ \AA}$.
    *   **Ferroelectric Domain Walls / Piezoelectric actuation:** Local strains can be significant ($> 1\%$).
*   **Selected Starting Value:** $\varepsilon = 0.04 \text{ \AA}$ ($4 \times 10^{-12}$ m).
*   **Verification:**
    $$ \frac{\varepsilon}{a} = \frac{0.04 \text{ \AA}}{4.0 \text{ \AA}} = 0.01 = 1\% $$
    This is a significant strain (1%) but satisfies $\varepsilon \ll a$ sufficiently for a first-order approximation to hold while yielding a measurable signal. If the model is meant to represent pure thermal noise, use $0.004 \text{ \AA}$.

*Note:* If using $\varepsilon$ as dimensionless strain ($\Delta L / L$), a typical value is $10^{-3}$ to $10^{-2}$. In the code/model implementation, ensure $\varepsilon$ is treated as length (meters) to match the provided formula $S_{\pm} \propto \varepsilon/a$.

## 3. Diffraction Geometry Indices

### Miller Indices ($n_x, n_y, n_z$)
These define the scattering vector $\vec{K} = \frac{2\pi}{a}(n_x, n_y, n_z)$.

*   **Lowest Order Calculation:** $(1, 0, 0)$.
    *   This is the (100) Bragg peak.
    *   Condition: $n_x = 1, n_y = 0, n_z = 0$.
    *   This satisfies the criteria $n_x \neq 0$ for the structure factor to be non-vanishing along the $[100]$ polarization direction.
*   **Comparison Point:** Often useful to compare against $(2, 0, 0)$ or points with $n_x = 0$ (like $(0, 1, 1)$) to demonstrate the polarization sensitivity ($\vec{K} \cdot \vec{\varepsilon}=0$) and vanishing sidebands.

## 4. Summary of Parameter Table

The following table summarizes the starting parameters derived above.

| Parameter | Symbol | Value | Unit | Source / Justification |
| :--- | :---: | :--- | :---: | :--- |
| **Lattice Constant** | $a$ | $4.0$ | $\text{\AA}$ ($10^{-10}$ m) | Typical cubic crystal scale (e.g., Perovskites). |
| **Number of Cells** | $N$ | $1.0 \times 10^5$ | count | Linear count approx. $40 \text{ } \mu m$ beam width / $4 \text{ \AA}$. |
| **Modulation Period** | $M$ | $10$ | unitless | Superlattice/CDW regime $\lambda = 10a = 40 \text{ \AA}$. |
| **Displacement Amp.** | $\varepsilon$ | $0.04$ | $\text{\AA}$ ($10^{-12}$ m) | Corresponds to 1% strain ($\varepsilon/a = 0.01$). |
| **Reciprocal Index X** | $n_x$ | $1$ | unitless | Fundamental (100) reflection direction. |
| **Reciprocal Index Y** | $n_y$ | $0$ | unitless | Scattering plane aligned with strain. |
| **Reciprocal Index Z** | $n_z$ | $0$ | unitless | Scattering plane aligned with strain. |

## 5. Verification of the Model Output

Using the final validated formula with these parameters, we can estimate the ratio of the satellite intensity to the main Bragg peak intensity. The main Bragg peak term is $S_0 \propto f N$. The sideband term is:

$$S_{\pm} \approx \pm \frac{\pi f N \varepsilon}{a} n_x$$

The intensity ratio $R$ is:

$$R = \frac{I_{\text{satellite}}}{I_{\text{main}}} \approx \frac{|S_{\pm}|^2}{|S_0|^2} = \left( \frac{\pi \varepsilon n_x}{a} \right)^2$$

Substituting our parameters ($\varepsilon/a = 0.01$, $n_x = 1$):

$$R \approx (\pi \times 0.01)^2 \approx (0.0314)^2 \approx 9.86 \times 10^{-4} \approx 0.1\%$$

**Interpretation:** A 1% strain amplitude yields satellite peaks with approximately 0.1% of the intensity of the main Bragg peak. This is a realistic, detectable signal in a high-resolution X-ray diffraction experiment (where dynamic range is often $10^6$ or better). It confirms that the chosen $\varepsilon$ is experimentally relevant—not too small to be lost in noise, and not so large as to violate the linear approximation or destroy the crystal structure.
# Suggested Starting Parameters for the Model

To simulate the quantum Fisher information (QFI) model derived for imaging two incoherent thermal sources, it is essential to select parameters that reflect realistic optical experimental conditions. The parameters must define the physical characteristics of the imaging system (Point Spread Function), the configuration of the sources (positions and separation), and the resulting scaling factors of the model.

Below is a detailed breakdown of the suggested starting parameters, their realistic ranges, and the sources/justifications for these choices.

## 1. System Parameters: Point Spread Function (PSF)

The Point Spread Function $\psi(x)$ defines the spatial resolution of the imaging system. In optical microscopy and astronomy, this is typically determined by the diffraction limit of a circular aperture, approximated by a Gaussian function for paraxial, in-focus imaging to simplify analytical calculations while maintaining physical relevance.

**Parameter Choice:**
We model the PSF as a normalized Gaussian amplitude profile:
$$
\psi(x) = \left( \frac{1}{\pi \sigma^2} \right)^{1/4} \exp\left( - \frac{x^2}{2\sigma^2} \right)
$$
where:
*   **$x$**: Image plane coordinate (dimensionless in code, normalized to wavelength/NA).
*   **$\sigma$ (PSF Width):** Represents the standard deviation of the intensity distribution (often related to the Rayleigh criterion).

### **Starting Parameter: $\sigma$**
*   **Value:** $1.0$
*   **Justification:** Normalizing the PSF width $\sigma=1$ sets the fundamental length scale of the system. In simulation, this allows us to define source separations $d$ relative to the system's resolution width (e.g., sub-Rayleigh $d < 1$ or super-Rayleigh $d > 1$).
*   **Dimensional Realism:** In a real-world experiment with wavelength $\lambda = 500$ nm and Numerical Aperture $NA = 1.0$, the standard deviation of the intensity PSF is approximately $\sigma \approx \frac{\lambda}{2\pi NA} \approx 80$ nm. Setting $\sigma=1$ in the model corresponds to scaling all distances by this factor.

---

## 2. Source Configuration Parameters

The sources are two incoherent thermal point sources located at positions $u_1$ and $u_2$.

### **Starting Parameter: Source Separation ($d$)**
Since the system is translation invariant, the critical geometric parameter is the distance between the two sources.
$$d \equiv u_2 - u_1$$

*   **Suggested Values (Range):** $0.1$ to $3.0$ (units of $\sigma$)
*   **Specific Starting Value:** $0.5$ (Sub-Rayleigh regime)
*   **Justification:**
    *   **Sub-Rayleigh ($d < 1$):** This is the regime of high interest in quantum estimation theory (Tsang, 2014), where direct imaging fails to resolve the sources but precise estimation of the centroid or separation is still possible.
    *   **Unit:** The separation is normalized by the PSF width $\sigma$. A separation of $d=0.5$ corresponds to the sources being closer than the standard deviation of the intensity profile, a challenging but realistic scenario for testing Fisher information limits.
*   **Source:** *Tsang, M. "Quantum limits to optical point-source localization," Optica **1**, 44 (2014).*

### **Starting Parameter: Source Positions ($u_1, u_2$)**
To satisfy the symmetry assumption in the model ($J_{11} = J_{22}$):

*   **Value:** $u_1 = -d/2$, $u_2 = +d/2$
*   **Example:** $u_1 = -0.25$, $u_2 = +0.25$ (for $d=0.5$).
*   **Justification:** Centering the sources symmetrically around the optical axis ($x=0$) simplifies the calculation of the overlap integrals and ensures that the imaging system vignetting or alignment errors do not bias the simulation.

---

## 3. Calculated Model Constants ($\Delta k^2$ and $\gamma$)

Using the Gaussian PSF defined in Section 1, we can calculate explicit starting values for the QFI components.

### **Calculation for $\Delta k^2$**
$$
\Delta k^2 \equiv \int_{-\infty}^{\infty} dx \left[ \frac{\partial \psi(x)}{\partial x} \right]^2
$$
For the Gaussian $\psi(x) = (\pi \sigma^2)^{-1/4} e^{-x^2/2\sigma^2}$, the derivative is $\psi'(x) = -\frac{x}{\sigma^2}\psi(x)$.
Solving the integral yields:
$$
\Delta k^2 = \frac{1}{2\sigma^2}
$$

*   **Starting Value:** $\Delta k^2 = 0.5$ (assuming $\sigma=1$).
*   **Physical Meaning:** This represents the inverse variance of the position estimate for a single isolated source. It sets the scale for the "classical" precision limit.

### **Calculation for $\gamma$**
Based on the dimensionally corrected definition using the overlap of derivatives:
$$
\gamma \equiv \int_{-\infty}^{\infty} dx \frac{\partial \psi(x)}{\partial x} \frac{\partial \psi\left(x - (u_2 - u_1)\right)}{\partial x}
$$
For the Gaussian PSF with separation $d$:
$$
\gamma = \frac{\Delta k^2}{\sqrt{2}} \exp\left( - \frac{d^2}{4\sigma^2} \right) = \frac{1}{2\sqrt{2}\sigma^2} \exp\left( - \frac{d^2}{4\sigma^2} \right)
$$

*   **Starting Value (for $d=0.5$):**
    $$ \gamma \approx \frac{0.5}{1.414} \exp(-0.125) \approx 0.353 \times 0.882 \approx 0.312 $$
*   **Physical Meaning:** This term captures the "confusion" or correlation between the two signals caused by their PSF overlap. As $d \to 0$, $\gamma \to \Delta k^2 / \sqrt{2}$ (for Gaussian derivatives). As $d \to \infty$, $\gamma \to 0$.

---

## 4. Summary of Starting Parameters Table

The following table provides the concrete values to initialize the model simulation for a realistic "sub-Rayleigh" scenario.

| Parameter | Symbol | Value | Unit | Description |
| :--- | :---: | :--- | :---: | :--- |
| **PSF Width** | $\sigma$ | $1.0$ | $\sigma$ | Width of the Gaussian point spread function (normalized). |
| **Source Separation** | $d$ | $0.5$ | $\sigma$ | Distance between $u_1$ and $u_2$. Indicates sub-Rayleigh separation. |
| **Position 1** | $u_1$ | $-0.25$ | $\sigma$ | Position of the first thermal source. |
| **Position 2** | $u_2$ | $+0.25$ | $\sigma$ | Position of the second thermal source. |
| **Bandwidth (Diagonal QFI)**| $\Delta k^2$ | $0.5$ | $\sigma^{-2}$ | The single-source Fisher information scaling factor. |
| **Overlap (Cross QFI)** | $\gamma$ | $0.312$ | $\sigma^{-2}$ | The cross-correlation factor for $d=0.5$. |

**Final QFI Estimate for $\theta$:**
Using the derived formula $\mathcal{J}_\theta = \frac{5}{9} \Delta k^2 + \frac{4}{9} \gamma$ with the parameters above:
$$
\mathcal{J}_\theta = \frac{5}{9}(0.5) + \frac{4}{9}(0.312) \approx 0.277 + 0.139 \approx 0.416
$$
This value represents the achievable precision (inverse variance) per photon for the weighted centroid parameter in this specific configuration.
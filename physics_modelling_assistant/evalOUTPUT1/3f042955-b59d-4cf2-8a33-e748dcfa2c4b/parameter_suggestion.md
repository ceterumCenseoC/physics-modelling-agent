# Suggested Starting Parameters for the Quantum Fisher Information Model

To generate realistic numerical results for the Quantum Fisher Information (QFI) model derived in the previous section (specifically the expression $F_Q = \frac{5}{9}\Delta k^2 + \frac{4}{9}\gamma'$), we must select parameters that correspond to a feasible optical experiment. The model involves estimating a linear combination of positions of two thermal sources based on single-photon detection.

Below are the suggested starting parameters, the logic behind their selection, and the sources used.

## 1. Optical Wavelength ($\lambda$) and Wave Number ($k$)

**Parameter Value:**
*   **Wavelength ($\lambda$):** $532 \text{ nm}$
*   **Wave number ($k$):** $\frac{2\pi}{\lambda} \approx 11.81 \times 10^6 \text{ m}^{-1}$

**Logic and Derivation:**
The "width" of the spatial mode wavefunction $\psi(x)$ is inversely proportional to the wave number. To calculate the variance $\Delta k^2$ (which describes the spatial frequency content), we must assume a bandlimit for the optical system. A standard diffraction-limited system is often modeled by a Gaussian point spread function (PSF) or a sinc function (rectangular aperture). For a circular aperture of diameter $D$, the cut-off spatial frequency is $k_c \approx \pi D / (\lambda f)$. However, for a simple starting model using a Gaussian approximation:
$$ \psi(x) \propto e^{-\frac{x^2}{2\sigma^2}} $$
The variance in k-space is related to the variance in position (the width of the PSF, $\sigma_{PSF}$) by the uncertainty relation. A typical width for a diffraction-limited Airy disk (first zero) is $1.22 \lambda \text{NA}$. We choose $\lambda = 532 \text{ nm}$ (green laser), which is a very common wavelength in laboratory quantum optics experiments (e.g., spontaneous parametric down-conversion sources).

**Sources:**
*   *Common experimental standard:* 532nm is the frequency-doubled output of a Nd:YAG laser (1064nm).
*   *Physics:* Quantum Optics textbooks (e.g., Mandel & Wolf, "Optical Coherence and Quantum Optics") utilize visible light ranges for diffraction examples.

## 2. Spatial Separation ($\Delta u = u_2 - u_1$)

**Parameter Value:**
*   **Source Separation ($\Delta u$):** $200 \text{ nm}$ to $500 \text{ nm}$ (sub-Rayleigh or near-Rayleigh regime).

**Logic and Derivation:**
The QFI model is designed to resolve closely spaced sources. The Rayleigh criterion states that two point sources are resolvable when their center-to-center distance is approximately $\lambda / (2 \text{NA})$.
For a typical Numerical Aperture (NA) of 0.9 (high magnification oil immersion objective):
$$ R_c \approx \frac{532 \text{ nm}}{2 \times 0.9} \approx 295 \text{ nm} $$
To test model performance in the "super-resolution" regime (where quantum metrology provides benefits over classical imaging), the separation should be close to or below this diffraction limit. A starting value of $\Delta u = 300 \text{ nm}$ is realistic for studying estimation limits.

**Sources:**
*   *Rayleigh Criterion definition:* Hecht, "Optics", or Born & Wolf, "Principles of Optics".
*   *Super-resolution literature:* Tsang, Nair, and Lu (2016) - "Quantum Theory of Superresolution for Two Incoherent Optical Point Sources", which typically operates in the sub-Rayleigh regime ($d < \lambda/2$).

## 3. Numerical Aperture (NA) and Mode Bandwidth ($\Delta k$)

**Parameter Value:**
*   **Numerical Aperture (NA):** $0.85$
*   **Spatial Bandwidth ($\Delta k$):** $\frac{\text{NA} \cdot k}{z}$ (normalized to object plane coordinates) or approximated as $\approx \frac{1}{\sigma_{PSF}}$.

**Logic and Derivation:**
The term $\Delta k^2$ in the QFI formula represents the variance of the spatial frequencies collected by the system. For a diffraction-limited system with a Gaussian PSF of width $\sigma_{PSF}$:
$$ \Delta k^2 \approx \frac{1}{2\sigma_{PSF}^2} $$
Assuming a Gaussian approximation of the Airy disk, where the width is determined by the NA:
$$ \sigma_{PSF} \approx \frac{0.61 \lambda}{\text{NA}} $$
With $\lambda = 532 \text{ nm}$ and NA = 0.85:
$$ \sigma_{PSF} \approx \frac{0.61 \times 532}{0.85} \approx 381 \text{ nm} $$
$$ \Delta k^2 \approx \frac{1}{2 (381 \times 10^{-9})^2} \approx 3.44 \times 10^{12} \text{ m}^{-2} $$
(If using dimensionless units optimized for code, one might normalize such that $\sigma_{PSF} = 1$, leading to $\Delta k^2 = 0.5$. However, for physical comparison, we use SI units here).

**Sources:**
*   *Fourier Optics:* Goodman, "Introduction to Fourier Optics". The relationship between the aperture size (NA) and the Gaussian beam width.

## 4. Source Positions ($u_1, u_2$)

**Parameter Value:**
*   **$u_1$:** $0$ (Central reference)
*   **$u_2$:** $300 \text{ nm}$ (Based on separation $\Delta u$)

**Logic and Derivation:**
We set the origin of the coordinate system at the midpoint between the two sources or at the location of the first source. For simplicity in calculating $\gamma'$, let $u_1 = -d/2$ and $u_2 = d/2$ (symmetric around 0) or $u_1 = 0, u_2 = d$.
Assuming $u_1 = 0$ and $u_2 = 300 \text{ nm}$.

## 5. The Overlap Integral ($\gamma'$)

**Parameter Value:**
*   **$\gamma'$:** Calculate dynamically based on the PSF profile.

**Definition:**
$$ \gamma' = \int_{-\infty}^{\infty} \frac{\partial \psi(x-u_1)}{\partial x} \frac{\partial \psi(x-u_2)}{\partial x} \, dx $$

**Logic and Derivation:**
This value depends on the distance between the sources. For a Gaussian PSF $\psi(x) = (2\pi\sigma^2)^{-1/4} e^{-x^2/4\sigma^2}$:
$$ \frac{\partial \psi}{\partial x} = -\frac{x}{2\sigma^2} \psi(x) $$
Substituting and solving the Gaussian integral yields a function that decays as the separation $|u_2 - u_1|$ increases. If the sources are far apart, $\gamma' \to 0$. If they overlap perfectly, $\gamma' \to \Delta k^2$. At the Rayleigh limit, $\gamma'$ will be a significant fraction of $\Delta k^2$.
*Example calculation:*
If $\sigma = 381 \text{ nm}$ and separation $\Delta u = 300 \text{ nm}$:
Using the property of Gaussian derivatives, $\gamma' = \Delta k^2 \cdot \exp(-\frac{(\Delta u)^2}{4\sigma^2}) \cdot (1 - \frac{(\Delta u)^2}{4\sigma^2})$.
With these numbers, the model will produce a concrete numerical value for QFI。

## Summary of Starting Parameters

| Parameter | Symbol | Value | Unit | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Wavelength** | $\lambda$ | $532$ | $nm$ | Green laser (2nd harmonic Nd:YAG) |
| **Numerical Aperture** | NA | $0.85$ | - | High-end microscope objective |
| **PSF Width (Gaussian)** | $\sigma_{PSF}$ | $381$ | $nm$ | Derived from $\approx 0.61\lambda / \text{NA}$ |
| **Spatial Freq Variance** | $\Delta k^2$ | $3.44 \times 10^{12}$ | $m^{-2}$ | $\approx 1 / (2\sigma_{PSF}^2)$ |
| **Source 1 Position** | $u_1$ | $-150$ | $nm$ | Centered around 0 |
| **Source 2 Position** | $u_2$ | $+150$ | $nm$ | Centered around 0 |
| **Total Separation** | $\Delta u$ | $300$ | $nm$ | Near the Rayleigh limit |
| **Overlap Integral** | $\gamma'$ | *Calculated* | $m^{-2}$ | Function of $\Delta u$ and $\sigma_{PSF}$ |
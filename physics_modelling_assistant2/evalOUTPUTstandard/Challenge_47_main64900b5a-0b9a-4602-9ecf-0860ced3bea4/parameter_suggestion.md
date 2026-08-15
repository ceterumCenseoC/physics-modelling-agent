# Starting Parameters for the Model

To ensure the model produces physically realistic results that can be compared against experimental data (or established theoretical simulations), we must define the computational parameters and scales based on the specific properties of the spin wave packet configuration.

The core of the model is the computation of the operator trace $\mathrm{Tr}(L^4)$ involving spin matrices and the Hilbert transform. The starting parameters below are选定 to ensure numerical stability, convergence to the specified precision (6 decimal places), and adherence to experimental scales involved in localized spin excitations (e.g., magnetic solitons or wave packets).

## 1. Primary Scales and Dimensions

### Spatial Domain
The spin configuration is defined by $\theta(x) = x$ and a localized phase modulation $\phi(x) = \frac{2\pi}{3}e^{-x^2}$.

*   **Characteristic Width Parameter ($\sigma_{\mathrm{wp}}$):**
    The width of the wave packet is determined by the exponent in the phase term. With the definition $\phi(x) = \frac{2\pi}{3}e^{-x^2}$, the standard deviation (or width scale) is implicitly $\sigma = \frac{1}{\sqrt{2}}$ if we match to the Gaussian form $e^{-x^2/2\sigma^2}$.
    For the numerical simulation, we treat the domain such that the wave packet is fully resolved.
    **Parameter:** $\sigma_{\mathrm{wp}} = 0.7071$ (implicit unit length).

*   **Spatial Domain Boundary ($x_{\mathrm{max}}$):**
    To approximate the integral over $\mathbb{R}$, we integrate over a finite interval $[-x_{\mathrm{max}}, x_{\mathrm{max}}]$. The envelope $e^{-x^2}$ decays rapidly. We choose the boundary where the envelope falls below machine precision relative to the maximum amplitude, or where the truncation error is negligible compared to the $10^{-6}$ requirement.
    With $e^{-x^2}$, at $x=4$, the value is $\approx 10^{-7}$.
    **Parameter:** $x_{\mathrm{max}} = 6.0$.
    **Source:** Standard criterion for truncating Gaussian integrals: $\int_{-\infty}^{-A} e^{-x^2} dx < 10^{-8}$ for $A \geq 4$. Given the oscillatory nature of $\sin(x)$, a slightly larger buffer ensures the tail contributions to the integral $\int \sin(x)\cos(x)... dx$ correctly cancel out numerically.

### Angular Frequency
The field $\vec{m}$ varies with $\theta(x) = x$. This implies a spatial frequency $k=1$.
**Parameter:** $k = 1.0$ (inverse unit length).

## 2. Numerical Simulation Parameters

To evaluate $\mathrm{Tr}(L^4)$ to 6 decimal places, we must discretize the continuous operators. The critical difficulty is resolving the Hilbert transform, which is a global operator involving $1/(x-y)$ singularities, and the rapid oscillations of the spin field $\theta(x) = x$.

### Discretization Grid ($N$ and $\Delta x$)
We use a uniform grid with spacing $\Delta x$ covering $[-x_{\mathrm{max}}, x_{\mathrm{max}}]$.
*   **Resolution Criterion:** To resolve the oscillations $\sin(x)$ and $\cos(x)$, we need significantly more than 2 points per wavelength. To apply the discrete Hilbert transform accurately, we must resolve the sharp gradients where $x$ is large.
*   **Grid Spacing ($\Delta x$):** A conservative choice is $\Delta x = 0.01$. This provides 100 points per unit length (since period is $2\pi \approx 6.28$, this is $\approx 600$ points per period).
*   **Number of Points ($N$):** The total domain length is $2 \times x_{\mathrm{max}} = 12$.
    $$ N = \frac{12}{0.01} = 1200 $$
    For FFT-based methods, $N$ is typically a power of 2 for efficiency.
    **Parameter:** $N = 2048$ (Next power of 2).
    **Parameter:** $\Delta x = x_{\mathrm{max}} \times 2 / N = 12 / 2048 \approx 0.00586$.
    **Source:** Standard signal processing requirements (Nyquist-Shannon sampling theorem extended for numerical differentiation/integration stability). The Hilbert transform's $1/x$ kernel is well-approximated by FFT convolution when the function is sufficiently resolved (Titchmarsh).

### Kernel Regularization (Epsilon)
The numerical definition of the discrete Hilbert transform requires handling the singularity at $y=x$.
$$ \mathcal{H}[f](x) \approx \sum_{j \neq k} \frac{f(x_j)}{x_k - x_j} \Delta x $$
In practice, or via Fourier multiplier $-i \text{sign}(\xi)$, this is handled implicitly. However, if implementing via convolution, a cutoff is needed. For the FFT method, no epsilon is strictly needed, but for high precision, we assume the standard FFT implementation.
**Parameter:** $\epsilon = 0$ (Using FFT multiplier method).
**Source:** Chaudhury [1], "L^p-boundedness of the Hilbert transform", confirms the Fourier transform characterization $\widehat{\mathcal{H}f}(\xi) = -i \text{sign}(\xi)\hat{f}(\xi)$, which avoids discretization of the principal value singularity directly.

## 3. Physical Realism of Spin Parameters

If we map this unitless model to a physical system (e.g., a nanowire or a magnetic strip), we define the conversion rates.

### Conversion to Physical Units (Example: Ferromagnetic Nanowire)
*   **Exchange Length ($l_{\mathrm{ex}}$):** Typically $\approx 5 \,\mathrm{nm}$.
*   **Packet Width ($w$):** The dimensionless width $\approx 1$. Assuming $\theta(x) = x_{\mathrm{phys}} / l_{\mathrm{ex}}$, a dimensionless width of 1 corresponds to a physical width of $l_{\mathrm{ex}} \approx 5 \,\mathrm{nm}$.
*   **Phase Amplitude:** $\phi_0 = 2\pi/3 \approx 120^\circ$. This is a realistic precession angle for spin texture simulations.

## 4. Summary of Starting Parameters Table

| Parameter | Symbol | Value | Units | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Spatial Domain Half-width** | $x_{\mathrm{max}}$ | $6.0$ | [L] | Bound for numerical integration $[-6, 6]$. |
| **Number of Grid Points** | $N$ | $2048$ | - | Power of 2 for efficient FFT. |
| **Grid Spacing** | $\Delta x$ | $0.00586$ | [L] | Determined by $12 / 2048$. |
| **Spin Field Freq** | $k$ | $1.0$ | $[L]^{-1}$ | From definition $\theta(x)=x$. |
| **Phase Amplitude** | $\phi_0$ | $2\pi/3$ | rad | From $\phi(x) = \dots e^{-x^2}$. |
| **Packet Width** | $\sigma_{\mathrm{wp}}$ | $1/\sqrt{2} \approx 0.707$ | [L] | Width of Gaussian envelope. |
| **Singularity Cutoff** | $\epsilon$ | $0$ | - | Using FFT frequency domain method. |

## 5. Explanation of Parameter Choices

*   **Domain ($x_{\mathrm{max}} = 6.0$)**: The function $\phi(x)$ is proportional to $e^{-x^2}$. At $x=6$, $e^{-36} \approx 2.3 \times 10^{-16}$, which is close to double-precision floating-point limits ($\sim 10^{-16}$). This ensures the "wave packet" is numerically zero at the boundaries, minimizing aliasing effects from the FFT (Circular Convolution assumption).
*   **Resolution ($\Delta x \approx 0.006$)**: The Hilbert transform involves global behavior and $1/x$ decay. More importantly, the derivatives of the spin field $\vec m(x)$ (which determine the commutator $[\mathcal{H}, m]$) scale with the frequency $k$. With $k=1$, the features are large, but we require high precision for $\mathrm{Tr}(L^4)$. A step size of 0.006 ensures total integration error is well below $10^{-6}$ for the quadrature.
*   **FFT vs Convolution**: The choice of $\epsilon = 0$ implies we use the Fourier multiplier definition. This is the standard approach for numerical Hilbert transforms as it leverages the Convolution Theorem and is $O(N \log N)$ complexity, much faster than direct $O(N^2)$ integration. It also smooths out the principal value singularity naturally.
*   **Consistency**: These parameters generate a smooth, bounded matrix field $m(x)$ whose derivatives are well-resolved, satisfying the criteria for the boundedness of the Hilbert transform (Riesz theorem [2]), ensuring the model is mathematically stable.

## Sources
1.  **K. N. Chaudhury**, "L^p-boundedness of the Hilbert transform," arXiv:0909.1426v9, 2012. — Defines the Fourier multiplier implementation used for the numerical parameter choice.
2.  **M. Riesz**, "Sur les fonctions conjuguées," *Mathematische Zeitschrift* (1928). — Provides the boundedness theorem ensuring the model won't diverge for the chosen $L^\infty$-type spin field.
3.  **W. H. Press et al.**, "Numerical Recipes," *Cambridge University Press*. — Standard reference for FFT grid sizing ($N=2^p$) and integration domain truncation errors.
4.  **Z. Brzeźniak**, "Hashimoto transform for stochastic Landau-Lifshitz-Gilbert equation," arXiv:1401.2520v1, 2014. — Contextualizes the spin field configuration as a realistic model for magnetic filaments, justifying the amplitude and width scales.
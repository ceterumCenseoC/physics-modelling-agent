# Starting Parameters for the AdS$_3$/BCFT$_2$ One-Point Function Model

## 1. Model Overview and Parameter Selection Logic

The model describes the holographic calculation of a thermal one-point function $\langle \mathcal{O} \rangle$ in a Boundary Conformal Field Theory (BCFT$_2$) dual to a Euclidean BTZ black hole terminated by an End-of-the-World (ETW) brane.

The core of the model is the **geodesic approximation**:
$$
\langle \mathcal{O}(x) \rangle \propto e^{-m \ell_{\text{geo}}^{\text{ren}}},
$$
where $m$ (or $\Delta$) is the mass of the dual scalar field and $\ell_{\text{geo}}^{\text{ren}}$ is the renormalized geodesic length from the boundary to the ETW brane.

To ensure the model runs for realistic parameters and can be compared to experimental results (or standard numerical simulations in AdS/CFT), we select starting parameters based on the following logic:

1.  **Scale Invariance**: In AdS/CFT, the physics is scale invariant unless we introduce a physical scale like the AdS radius $L_{\text{AdS}}$. We work in dimensionless AdS units where $L_{\text{AdS}}=1$.
2.  **Large Mass Limit**: The derivation relies on the large-$m$ (or large-$\Delta$) limit, where the semi-classical approximation is valid.
3.  **Horizon Scale**: The black hole horizon radius $r_0$ sets the temperature scale $T = \frac{r_0}{2\pi}$. We vary $r_0$ to represent different thermal energies.
4.  **Brane Tension**: The brane tension $\eta$ determines the geometry of the ETW brane. In the "Karch-Randall" type setup for branes behind the horizon, the tension determines how "deep" the brane sits.

## 2. Realistic Starting Parameters

Below are the suggested starting parameters for the model, categorized by their physical role. All values are in dimensionless AdS units ($L_{\text{AdS}}=1$).

### 2.1 Bulk Scalar Parameters

| Parameter | Symbol | Description | Suggested Range / Value | Justification |
| :--- | :---: | :--- | :--- | :--- |
| **Mass / Dimension** | $m$ or $\Delta$ | Conformal dimension of the operator $\mathcal{O}$. | **Start:** $m = 5.0$ <br> **Range:** $[1.0, 20.0]$ | The geodesic approximation requires $m \gg 1$. Values like $5, 10, 20$ are standard in numerical holography (e.g., in computing scalar field spectra or geodesic lengths) to ensure the semi-classical WKB approximation holds while avoiding numerical overflows in exponentials like $e^{-m\ell}$. Values $\Delta \ge 1$ ensure the Breitenlohner-Freedman bound is satisfied ($m^2 L^2 \ge -1$). |
| **Interaction Constant** | $\lambda$ | Coupling constant for the cubic interaction $\lambda \chi^2 \phi$. | **Start:** $\lambda = 0.1$ | The source text treats the perturbation as first order. Small coupling constants ($0.01 - 1.0$) are typical for perturbative expansions in QFT to ensure higher-order terms ($\lambda^2, \lambda^3$) remain negligible compared to the leading order. |

### 2.2 Spacetime Parameters (Black Hole)

| Parameter | Symbol | Description | Suggested Range / Value | Justification |
| :--- | :---: | :--- | :--- | :--- |
| **Horizon Radius** | $r_0$ (or $r_+$) | Radius of the event horizon. Sets the temperature $T = r_0/2\pi$. | **Start:** $r_0 = 1.0$ <br> **Range:** $[0.5, 5.0]$ | This sets the "thermal scale". $r_0=1$ corresponds to the scale of the AdS radius. Varying $r_0$ from 0.5 to 5 explores low and high-temperature regimes where the black hole size varies relative to the AdS curvature scale. |
| **Radial Cutoff** | $\Lambda$ | UV cutoff for the renormalization of the geodesic length. | **Start:** $\Lambda = 1000.0$ <br> **Convergence:** Check at $\Lambda = 10000.0$ | The boundary is at $r \to \infty$. Numerical integrals require a finite cutoff. $\Lambda \gg r_0$ is required to approximate the boundary divergence accurately. The value $1000$ is typically sufficient to stabilize the renormalized length $\ell^{\text{ren}}$, while larger values can be used to verify convergence. |

### 2.3 Brane Parameters

| Parameter | Symbol | Description | Suggested Range / Value | Justification |
| :--- | :---: | :--- | :--- | :--- |
| **Brane Tension** | $\eta$ | Tension of the ETW brane determining its embedding. | **Start:** $\eta = 0.5$ <br> **Range:** $(0, 1)$ or $[0.1, 2.0]$ | In the AdS/BCFT correspondence, the brane tension determines the angle at which the brane meets the AdS boundary (or its position behind the horizon). For spherical branes or those behind the horizon in BTZ, tensions $0 < \eta < 1$ are common in specific models (depending on the specific definitions of $\eta$, sometimes $\eta = \cot \theta$). A starting value of $0.5$ represents a "moderate" tension that significantly alters the geometry from the pure black hole ($\eta=0$) case. |

### 2.4 Numerical Integration Parameters

| Parameter | Symbol | Description | Suggested Value | Justification |
| :--- | :---: | :--- | :--- | :--- |
| **Integration Step** | $dr$ | Step size for the radial integral of the geodesic length. | $10^{-3}$ to $10^{-4}$ | The integral $\int \frac{dr}{\sqrt{r^2 - r_0^2}}$ has a singularity at $r=r_0$. A small step size is required near the horizon to maintain accuracy. |

## 3. Derived Analytical Start Values

Based on the selected parameters, the theoretical starting value for the one-point function (magnitude) can be calculated to verify the model's output.

**Theoretical Prediction:**
Using the unperturbed result $\langle \mathcal{O} \rangle \propto e^{-m \ell_{\text{hor}}}$ with $\ell_{\text{hor}}^{\text{ren}} = -\ln r_0$:
$$
|\langle \mathcal{O} \rangle| \approx e^{m \ln r_0} = r_0^m.
$$

**Example Calculation with Starting Parameters:**
*   $r_0 = 1.0$
*   $m = 5.0$
$$
|\langle \mathcal{O} \rangle|_{\text{pred}} = 1.0^{5.0} = 1.0.
$$

**Example with $r_0 = 2.0$ (increased temperature):**
$$
|\langle \mathcal{O} \rangle|_{\text{pred}} = 2.0^{5.0} = 32.0.
$$

**Perturbation Check:**
The perturbation $\delta \langle \mathcal{O} \rangle$ is proportional to $\epsilon m e^{-m\ell} \delta\ell$.
With small coupling $\epsilon \sim 0.1$ and $m=5$, the perturbation is of order 0.5 to 1.0 relative to the magnitude 32.0 (approx 1-3% change if $\delta\ell$ is small), which is numerically resolvable.

## 4. Sources and References

The parameters and limits are derived from the following sources and standard practices in the field:

1.  **Geodesic Approximation Validity ($m \gg 1$):**
    *   Source: *Faulkner, et al., "Gravitation from Entanglement in Holographic CFTs" (JHEP 2014)* and general literature on heavy operators.
    *   Logic: The semi-classical limit $\Delta \to \infty$ simplifies the bulk-to-boundary propagator to a simple exponential of the geodesic length.

2.  **Thermal One-Point Function ($\langle \mathcal{O} \rangle \sim r_0^\Delta$):**
    *   Source: **Dey, Goldar, Kajuri**, *"Geodesics, One Point Functions and Black Hole Perturbations,"* arXiv:2601.09397 (2026). (Specifically Eqs 1.4 and 1.5 and the discussion on $\ell_{\text{hor}}$).
    *   Logic: The specific dependence on the horizon radius $r_0$ and the logarithmic renormalized length $\ell_{\text{hor}} = -\ln r_0$ are explicitly derived in the provided text.

3.  **Brane Tension ($\eta$) in AdS/BCFT:**
    *   Source: *Takayanagi, et al., "Holographic Dual of a Boundary Conformal Field Theory" (PTEP 2011/2012)*.
    *   Logic: The brane tension $\eta$ is the fundamental parameter determining the brane embedding in the bulk. Values $\eta \sim \mathcal{O}(1)$ are the standard phenomenological starting points.

4.  **Numerical Cutoffs ($\Lambda$):**
    *   Source: Standard practices in computational general relativity (e.g., *Skenderis, "Lecture notes on holographic renormalization"*).
    *   Logic: To extract finite AdS quantities, one must introduce a cutoff $\Lambda$ and subtract divergences. $\Lambda \approx 10^2 - 10^4$ ensures the UV region is adequately sampled.
# Mathematical Model for Determining Magic Wavelengths in Ytterbium

## Model Overview

This model provides a mathematical framework for calculating the magic wavelengths ($\lambda_{\text{magic}}$) for imaging Ytterbium (Yb) atoms isotopes $^{171}\text{Yb}$ and $^{174}\text{Yb}$. The model focuses on the optical transition between the ground state manifold ($^1S_0$) and the excited state ($^3P_1$).

A magic wavelength is defined as a specific wavelength of trapping/imaging light where the **AC Stark shift** (or light shift) is identical for both atomic states involved in the transition. This equality ensures that the transition frequency remains unperturbed by the external light field, allowing for high-fidelity imaging and state manipulation without decoherence.

**Note on Data Availability:**
Based on the provided source material, specific numerical values for polarizabilities or transition strengths for Yb in the 400-600 nm range are not available. The provided texts discuss Yb$^+$ ions, the 398.9 nm transition in neutral Yb, and transitions in Calcium. Consequently, this model outlines the **mathematical procedure and governing equations** to be solved, but numerical results cannot be generated without external data on the dynamic polarizabilities of $^{171}\text{Yb}$ and $^{174}\text{Yb}$ states.

---

## Theoretical Background

### 1. The AC Stark Shift

The interaction of an atomic state $|i\rangle$ with an oscillating electric field (light) leads to a shift in its energy levels, known as the AC Stark shift ($\Delta E_i$). For a state with total angular momentum $F$, the shift depends on the light intensity $I$, the wavelength $\lambda$, and the polarization of the light relative to the quantization axis.

The general expression for the light shift is:

$$ \Delta E(F, m_F) = -\frac{1}{4} \alpha(F, \omega, \text{pol}) \langle E^2 \rangle $$

Where:
- $F$ is the total angular momentum quantum number.
- $m_F$ is the projection of $F$ onto the quantization axis.
- $\omega = 2\pi c / \lambda$ is the angular frequency of the light.
- $\text{pol}$ denotes the polarization (either $\sigma^{\pm}$ or $\pi$).
- $\alpha(F, \omega, \text{pol})$ is the **dynamic polarizability** of the state.
- $\langle E^2 \rangle$ is the time-averaged square of the electric field amplitude, related to intensity $I$ by $I = \frac{1}{2} c \epsilon_0 \langle E^2 \rangle$.

### 2. Dynamic Polarizability Structure

The dynamic polarizability $\alpha(F, \omega)$ tensor can be decomposed into scalar, vector, and tensor components. For the ground state $^1S_0$ ($J=0$), there are only scalar components. For the excited state $^3P_1$ ($J=1$), all three components contribute.

However, because the ground state $^1S_0$ has $J=0$ and total angular momentum $F_{\text{ground}}$ is determined solely by nuclear spin $I$, it is insensitive to orientation (tensor shift is zero). The excited state $^3P_1$ has $J=1$, and its hyperfine structure depends on the nuclear spin $I$.

Let $|g\rangle$ denote the ground state manifold ($^1S_0$) and $|e\rangle$ denote the excited state ($^3P_1$).

The polarizability for a specific sublevel $|F, m_F\rangle$ is given by:

$$ \alpha(F, m_F, \omega, \text{pol}) = \alpha^{(0)}(F, \omega) + \alpha^{(1)}(F, \omega) \frac{m_F \kappa}{F} + \alpha^{(2)}(F, \omega) \frac{3 m_F^2 - F(F+1)}{F(2F-1)} $$

Where:
- $\alpha^{(0)}$ is the **scalar polarizability** (wavelength dependent).
- $\alpha^{(1)}$ is the **vector polarizability** (non-zero only if $F \geq 1/2$).
- $\alpha^{(2)}$ is the **tensor polarizability** (non-zero only if $F \geq 1$).
- $\kappa$ is a polarization parameter: $\kappa = 0$ for linear ($\pi$) polarization, $\kappa = \pm 1$ for circular ($\sigma^{\pm}$) polarization.

### 3. Isotope Specific Properties

The model requires nuclear spin ($I$) values for the isotopes to determine the hyperfine structure ($F$ quantum numbers) of the $^3P_1$ state.

*   **$^{174}\text{Yb}$:**
    *   Nuclear spin $I = 0$.
    *   Total angular momentum $F = J$.
    *   Ground state $^1S_0$: $F_g = 0$.
    *   Excited state $^3P_1$: $F_e = 1$.
    *   Hyperfine splitting is absent.
    *   Since $F_e=1$, vector shift $\alpha^{(1)} = 0$ (due to parity/time-reversal symmetry in averaging, or effectively 0 for linear/circular in simple definitions for bosons, but Tensor is present). *Correction:* For $F=1$, vector shift is allowed if states are not degenerate, but structural simplification occurs. However, for Magic Wavelengths with $J=0 \to J'=1$ transitions, we typically account for scalar and tensor shifts. Vector shifts average to zero for linear polarization or in a standing wave, but are crucial for circular polarization. Standard Magic Wavelength definition for $\pi$ and $\sigma$ transitions refers to the tensor contribution.

*   **$^{171}\text{Yb}$:**
    *   Nuclear spin $I = 1/2$.
    *   Ground state $^1S_0$: $J=0 \Rightarrow F_g = 1/2$.
    *   Excited state $^3P_1$: $J=1 \Rightarrow F_e \in \{1/2, 3/2\}$. (We typically seek magic conditions for the clock transition or specific hyperfine components; for imaging, often the cycling transition $F_g=1/2 \leftrightarrow F_e=3/2$ or $F_g=1/2 \leftrightarrow F_e=1/2$ is considered. The problem implies generic transition types $\sigma$ and $\pi$).
    *   Both scalar and vector/tensor components must be considered.

---

## Mathematical Model Steps

### Step 1: Define the Magic Wavelength Condition

The magic wavelength $\lambda_{\text{magic}}$ is the root of the equation where the AC Stark shift of the ground state equals the AC Stark shift of the excited state.

$$ \Delta E_g(\lambda_{\text{magic}}) = \Delta E_e(\lambda_{\text{magic}}) $$

Using the polarizability formulation:

$$ \alpha_g(\lambda_{\text{magic}}) = \alpha_e(\lambda_{\text{magic}}) $$

Note: For $^{171}\text{Yb}$, the "ground state" might refer to a specific sublevel $|F_g, m_{F_g}\rangle$. The equality must strictly hold for the specific states being used for imaging.

### Step 2: Formulate Polarizability for Ground State ($^1S_0$)

For both isotopes, the ground state is $^1S_0$.
Since $J=0$, the polarizability of the ground state ($\alpha_g$) is purely scalar. It has no dependence on polarization or $m_F$.

$$ \alpha_g(\omega) = \alpha_g^{(0)}(\omega) $$

The scalar polarizability is a sum of contributions from all dipole-allowed transitions from the ground state:

$$ \alpha_g^{(0)}(\omega) = \sum_{k} \frac{|\langle \psi_k | \mathbf{d} |\psi_g \rangle|^2}{\hbar (\omega_{kg} - \omega - i \Gamma_k/2)} $$

However, for finding magic wavelengths in a specific range (400-600 nm), we often parameterize this using known matrix elements and transition frequencies (which are not provided in the context).

### Step 3: Formulate Polarizability for Excited State ($^3P_1$)

The polarizability of the excited state $\alpha_e$ depends on the isotope (determining $F$) and the polarization.

#### Case A: Isotope $^{174}\text{Yb}$ ($F_e = 1$)
The excited state has a tensor contribution. The ground state ($F_g=0$) has no tensor contribution.
For a "magic wavelength" to exist with $\pi$ or $\sigma$ light, the shifts must match.
If using linear polarization ($\pi$, $\kappa=0$), the vector term vanishes.
For $\pi$-transitions (light polarized along the quantization axis, $\Delta m = 0$ selection rules for absorption, but here we discuss the shift mechanism):

$$ \alpha_e(F_e=1, m_{F_e}, \omega, \pi) = \alpha_e^{(0)}(\omega) + \alpha_e^{(2)}(\omega) \frac{3 m_{F_e}^2 - 2}{2} $$

The ground state shift is $\alpha_g^{(0)}(\omega)$.
Equality condition:
$$ \alpha_g^{(0)}(\omega) = \alpha_e^{(0)}(\omega) + \alpha_e^{(2)}(\omega) \frac{3 m_{F_e}^2 - 2}{2} $$

For $\sigma^{\pm}$ polarization, the vector term might appear (though often averaged out in 3D molasses or specific 1D traps). Assuming a simplified case where vector is negligible or we look for "tensor magic" points:
$$ \alpha_g^{(0)}(\omega) = \alpha_e^{(0)}(\omega) + \alpha_e^{(2)}(\omega) \frac{3 m_{F_e}^2 - 2}{2} $$
(Note: The "associated transition type" $\sigma$ or $\pi$ in the prompt likely refers to the polarization configuration that satisfies the condition).

#### Case B: Isotope $^{171}\text{Yb}$ ($I=1/2$)
Here we have hyperfine levels $F_e = 1/2$ and $F_e = 3/2$.
Assuming the imaging transition involves the "cycling" transition (often $F_g=1/2 \to F_e=3/2$) or the sensitive transition.
Let us assume we are finding the magic condition for $F_g=1/2 \to F_e=3/2$.

For $F_e = 3/2$, the polarizability is:
$$ \alpha_{e, 3/2}(m_F, \omega) = \alpha^{(0)}_{3/2}(\omega) + \alpha^{(1)}_{3/2}(\omega) \frac{m_F \kappa}{3/2} + \alpha^{(2)}_{3/2}(\omega) \frac{3 m_F^2 - (3/2)(5/2)}{(3/2)(2)} $$

The ground state is $F_g=1/2$. Since $J=0$, it has no vector or tensor shifts.
$$ \alpha_g(\omega) = \alpha_g^{(0)}(\omega) $$

**$\pi$-polarization condition ($\kappa=0$):**
$$ \alpha_g^{(0)}(\omega) = \alpha^{(0)}_{3/2}(\omega) + \alpha^{(2)}_{3/2}(\omega) \frac{3 m_F^2 - 15/4}{3} $$

**$\sigma$-polarization condition ($\kappa=\pm 1$):**
$$ \alpha_g^{(0)}(\omega) = \alpha^{(0)}_{3/2}(\omega) + \alpha^{(1)}_{3/2}(\omega) \frac{m_F (\pm 1)}{3/2} + \alpha^{(2)}_{3/2}(\omega) \frac{3 m_F^2 - 15/4}{3} $$

### Step 4: Solving for $\lambda$

To find the specific wavelengths in the range 400 nm to 600 nm, one must:

1.  **Parameterize the polarizabilities:** Express $\alpha^{(k)}(\omega)$ as functions of $\lambda$. This typically involves summing over dipole matrix elements for transitions from the $^3P_1$ state to other states (e.g., $^3S_1$, $^3D_{1,2,3}$, continuum, etc.).
    $$ \alpha^{(k)}(\omega) \propto \sum_j \frac{1}{\omega_j - \omega} $$

2.  **Numerical Root Finding:** Substitute the mathematical expressions for $\alpha_g$ and $\alpha_e$ into the equality equation derived in Step 3. Solve the equation for $\omega$ (or $\lambda = 2\pi c / \omega$) within the interval $[400, 600]$ nm.

3.  **Identification of Transition Type:**
    *   If the solution satisfies the $\pi$-polarization equation (where vector term is canceled or $m_F$ terms vanish/invariant), the type is **$\pi$**.
    *   If the solution satisfies the $\sigma$-polarization equation (accounting for the vector shift), the type is **$\sigma$**.

---

## Conclusion

This model defines the condition for magic wavelengths as the equality of dynamic polarizabilities between the $^1S_0$ ground state and specific sublevels of the $^3P_1$ excited state. The calculation requires detailed knowledge of the scalar, vector, and tensor dynamic polarizabilities of Yb in the visible spectrum, specifically the matrix elements and transition frequencies to higher-lying states. Without this specific spectroscopic data, numerical values for the magic wavelengths cannot be computed.
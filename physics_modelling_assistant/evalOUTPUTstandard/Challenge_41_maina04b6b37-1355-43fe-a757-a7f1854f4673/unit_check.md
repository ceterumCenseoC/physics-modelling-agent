# Dimensional Analysis of 2D Finite-Size Correction Formulas

## 1. Units of Quantities

I will determine the units of the physical quantities used in the 2D finite-size correction formulas. The analysis is performed in Hartree atomic units ($\hbar = m_e = e = a_B = 1$), but the dimensional consistency is verified in general SI-like dimensions ([Length], [Time], [Mass], [Charge]).

| Quantity | Symbol | Dimensions | Atomic Unit Equivalent |
| :--- | :--- | :--- | :--- |
| Coulomb Potential (k-space) | $v_k$ | $[M][L]^4[T]^{-2}[Q]^{-2}$ | Energy $\cdot$ Length |
| Electron Charge | $e$ | $[Q]$ | 1 (elementary charge) |
| Mass | $m_e$ | $[M]$ | 1 (electron mass) |
| Density | $n$ | $[L]^{-2}$ | $1/a_B^2$ |
| Wavevector | $k$ | $[L]^{-1}$ | $1/a_B$ |
| Plasma Frequency | $\omega_p$ | $[T]^{-1}$ | Ha/$\hbar$ |
| Reduced Planck Constant | $\hbar$ | $[M][L]^2[T]^{-1}$ | 1 |
| Energy | $E$ | $[M][L]^2[T]^{-2}$ | Ha (Hartree) |

## 2. Dimensional Analysis Results

### Formula 1: 2D Coulomb Potential
The Fourier transform of the 2D Coulomb interaction is given by:
$$ v_k = \frac{2\pi e^2}{k} $$

**Tool Input/Output:**
```python
Input: v_k = 2*pi*e^2/k
Dimensions: v_k=[energy*length], e=[charge], k=[length^-1]
Output: energy/(2*pi*charge**2)
```
**Analysis:** In atomic units ($e=1$, energy=Ha), $v_k$ has units of $\text{Ha} \cdot a_B$. Dimensionally, $[Q]^2/[L]^{-1} = [Q]^2[L]$. Since $[E] \sim [Q]^2/[L]$, this is equivalent to $[E][L]$. The formula is **dimensionally consistent**.

### Formula 2: 2D Plasma Frequency
The plasma frequency for the 2D electron gas is:
$$ \omega_p(k) = \sqrt{\frac{2\pi n e^2 k}{m_e}} $$

**Tool Input/Output:**
```python
Input: omega_p = sqrt(2*pi*n*e^2*k/m)
Dimensions: omega_p=[time^-1], n=[length^-2], e=[charge], k=[length^-1], m=[mass]
Output: sqrt(2)*length^(3/2)*sqrt(mass)/(2*sqrt(pi)*charge*time)
```
**Analysis:** The dimensional output is $\frac{\sqrt{[M][L]^3}}{[Q][T]}$. In Coulomb systems, $[E] \sim \frac{[Q]^2}{[L]}$, and $[E] \sim \frac{[M][L]^2}{[T]^2}$.
Combining these: $\frac{[M][L]^2}{[T]^2} \sim \frac{[Q]^2}{[L]} \implies \frac{\sqrt{[M]}}{[Q]} \sim \frac{1}{[T] \sqrt{[L]^3/2}}$.
Therefore, the output unit $\frac{\sqrt{[M][L]^3}}{[Q][T]}$ simplifies to frequency $[T]^{-1}$.
The formula is **dimensionally consistent**.

### Formula 3: Leading-Order Energy Correction
The general leading-order correction is:
$$ \Delta E_{\text{LO}} = \frac{\hbar \omega_p}{2N} $$

**Analysis:** Since $N$ is dimensionless:
$[\hbar \omega_p] = ([M][L]^2[T]^{-1}) \cdot ([T]^{-1}) = [M][L]^2[T]^{-2}$.
This is exactly the dimension of Energy. The formula is **dimensionally consistent**.

## 3. Corrected Formulas

The formulas provided in the context are already dimensionally consistent. Below is the consolidated set of formulas for the 2D electron gas finite-size correction, explicitly showing the derivation of the final numerical coefficient.

### 3.1 2D Coulomb Potential
$$ v_k = \frac{2\pi e^2}{k} $$

### 3.2 2D Plasma Frequency
$$ \omega_p(k) = \sqrt{\frac{2\pi n e^2 k}{m_e}} $$
*   In Hartree atomic units ($e=m_e=\hbar=1$):
    $$ \omega_p(k) = \sqrt{2\pi n k} $$

### 3.3 Leading-Order Finite-Size Correction
$$ \Delta E_{\text{LO}} = \frac{\hbar \omega_p(k_{\min})}{2N} $$

Substituting the atomic units expression for $\omega_p$:
$$ \Delta E_{\text{2D}} = \frac{1}{2N} \sqrt{2\pi n k_{\min}} $$

For an unpolarized 2D electron gas, $n = \frac{1}{\pi r_s^2}$ and $k_{\min} = \frac{2\sqrt{\pi}}{r_s\sqrt{N}}$.

**Derivation of explicit form:**
1.  **Substitute Density and k-min:**
    $$ \Delta E_{\text{2D}} = \frac{1}{2N} \sqrt{ \frac{2\pi}{\pi r_s^2} \cdot \frac{2\sqrt{\pi}}{r_s\sqrt{N}} } $$
2.  **Simplify constants:**
    $$ \Delta E_{\text{2D}} = \frac{1}{2N} \sqrt{ \frac{2}{r_s^2} \cdot \frac{2\sqrt{\pi}}{r_s\sqrt{N}} } = \frac{1}{2N} \sqrt{ \frac{4\sqrt{\pi}}{r_s^3 \sqrt{N}} } $$
3.  **Extract roots:**
    $$ \Delta E_{\text{2D}} = \frac{1}{2N} \frac{2\pi^{1/4}}{r_s^{3/2} N^{1/4}} = \frac{\pi^{1/4}}{r_s^{3/2} N^{5/4}} $$

### Final Corrected Formula
The dimensionally consistent formula for the leading-order finite-size correction per electron for a 2D electron gas is:

$$ \Delta E_{\text{2D}} = \frac{\pi^{1/4}}{r_s^{3/2} N^{5/4}} \quad \text{(Hartree)} $$

**Numerical Verification (for $N=122, r_s=10$):**
$$ \Delta E_{\text{2D}} = \frac{1.3313}{10^{3/2} \cdot 122^{5/4}} \approx 1.0 \times 10^{-4} \text{ Ha} $$


# Theoretical Framework & Model Setup

To determine the smallest inverse coupling scale $\Lambda_\gamma^{-1}$ probed by the Cosmic Explorer (CE), we utilize the standard effective field theory description of a scalar dark matter (DM) field $\phi$ linearly coupled to the electromagnetic field strength tensor. The interaction Lagrangian is given by:
$$\mathcal{L}_\text{int} = \frac{\phi}{4\Lambda_\gamma} F^{\mu\nu}F_{\mu\nu}$$
When this scalar field permeates a dielectric medium (such as the beamsplitter), it induces a time-varying shift in the material's index of refraction $n$. For a background index $n_0$, the oscillating scalar field $\phi(t) = \phi_0 \cos(2\pi f t)$ produces a relative change:
$$\delta n(t) = \frac{n_0^2 - 1}{2} \frac{\phi(t)}{\Lambda_\gamma}$$
In a laser interferometer with arm length $L$ and a dielectric component of thickness $d$, this refractive index modulation translates to an equivalent differential arm length strain $h(t)$:
$$h(t) = \frac{d}{2L} \delta n(t) = \frac{d(n_0^2 - 1)}{4L} \frac{\phi_0}{\Lambda_\gamma} \cos(2\pi f t)$$
The amplitude of the strain signal is $h_0 = \frac{d(n_0^2 - 1)}{4L} \frac{\phi_0}{\Lambda_\gamma}$. For a monochromatic signal observed over time $T_{\text{obs}}$ with instrumental strain noise spectral density $h_n(f)$, the signal-to-noise ratio (SNR) is:
$$\text{SNR} = \frac{h_0}{h_n(f)} \sqrt{T_{\text{obs}}}$$
Setting $\text{SNR} = 1$ allows us to solve for the minimum detectable coupling strength:
$$\Lambda_\gamma^{-1} = \frac{4L \, h_n(f)}{d(n_0^2 - 1) \, \phi_0 \sqrt{T_{\text{obs}}}}$$

# Parameter Extraction & Conversion

| Parameter | Symbol | Value | Notes |
|:---|:---:|:---|:---|
| Arm Length | $L$ | $40 \text{ km} = 4.00 \times 10^6 \text{ cm}$ | CE design specification |
| Beamsplitter Thickness | $d$ | $6 \text{ cm}$ | LIGO-like optics |
| Refractive Index | $n_0$ | $3.5$ | $\Rightarrow n_0^2 - 1 = 11.25$ |
| Strain Noise Density | $h_n$ | $2.00 \times 10^{-25} \text{ Hz}^{-1/2}$ | CE planned sensitivity |
| Observation Frequency | $f$ | $200 \text{ Hz}$ | Target band |
| Local DM Density | $\rho_{\text{loc}}$ | $0.4 \text{ GeV/cm}^3$ | Standard halo model |
| Overdensity Factor | $\eta$ | $178$ | Clump/stream enhancement |
| Local Velocity | $v$ | $230 \text{ km/s}$ | Galacto-kinematic standard |

**1. Effective Dark Matter Density:**
$$\rho_{\text{DM}} = \eta \rho_{\text{loc}} = 178 \times 0.4 = 71.2 \text{ GeV/cm}^3$$
Converting to natural units ($\hbar=c=1$, $1 \text{ GeV/cm}^3 \approx 7.69 \times 10^{-42} \text{ GeV}^4$):
$$\rho_{\text{DM}} \approx 5.48 \times 10^{-40} \text{ GeV}^4$$

**2. Scalar Field Amplitude ($\phi_0$):**
The oscillation mass is $m = 2\pi f$. Using $f=200 \text{ Hz} \Rightarrow m \approx 1.91 \times 10^{-21} \text{ GeV}$.
Assuming the field comprises the local energy density $\langle \rho \rangle = m^2 \phi_0^2$:
$$\phi_0 = \frac{\sqrt{2\rho_{\text{DM}}}}{m} = \frac{\sqrt{1.10 \times 10^{-39}}}{1.91 \times 10^{-21}} \approx 5.41 \times 10^2 \text{ GeV}^{1/2}$$

# Calculation Results

Substituting parameters into the sensitivity expression:
$$\Lambda_\gamma^{-1} = \frac{4(4.00 \times 10^6 \text{ cm})(2.00 \times 10^{-25})}{(6 \text{ cm})(11.25)(541 \text{ GeV}^{1/2}) \sqrt{T_{\text{obs}}}} = \frac{3.20 \times 10^{-18}}{3.645 \times 10^4 \sqrt{T_{\text{obs}}}} \text{ GeV}^{-1}$$
$$\Lambda_\gamma^{-1} = \frac{8.78 \times 10^{-23}}{\sqrt{T_{\text{obs}}}} \text{ GeV}^{-1}$$

**Case 1: $T_{\text{obs}} = 1000 \text{ s}$**
$$\sqrt{T_{\text{obs}}} = 31.62 \quad \Rightarrow \quad \Lambda_\gamma^{-1} = \frac{8.78 \times 10^{-23}}{31.62} = 2.78 \times 10^{-24} \text{ GeV}^{-1}$$
Converting to $\text{TeV}^{-1}$ ($1 \text{ GeV}^{-1} = 10^{-12} \text{ TeV}^{-1}$):
$$\Lambda_\gamma^{-1} = \mathbf{2.78 \times 10^{-6} \text{ TeV}^{-1}}$$

**Case 2: $T_{\text{obs}} = 0.7 \text{ yrs}$**
$$T_{\text{obs}} = 0.7 \times 3.156 \times 10^7 \text{ s} = 2.209 \times 10^7 \text{ s} \quad \Rightarrow \quad \sqrt{T_{\text{obs}}} = 4.700 \times 10^3$$
$$\Lambda_\gamma^{-1} = \frac{8.78 \times 10^{-23}}{4.700 \times 10^3} = 1.87 \times 10^{-26} \text{ GeV}^{-1}$$
Converting to $\text{TeV}^{-1}$:
$$\Lambda_\gamma^{-1} = \mathbf{1.87 \times 10^{-8} \text{ TeV}^{-1}}$$

# Final Answer
Under the assumption of an overdensity factor of 178 and utilizing the Cosmic Explorer's specified strain sensitivity and optical parameters, the smallest inverse coupling scale $\Lambda_\gamma^{-1}$ probed at $f=200\,\text{Hz}$ with $\text{SNR}=1$ is:
* **For $T_{\text{obs}} = 1000\,\text{s}$:** $\Lambda_\gamma^{-1} = 2.78 \times 10^{-6}\,\text{TeV}^{-1}$ ($2.78 \times 10^{-24}\,\text{GeV}^{-1}$)
* **For $T_{\text{obs}} = 0.7\,\text{yrs}$:** $\Lambda_\gamma^{-1} = 1.87 \times 10^{-8}\,\text{TeV}^{-1}$ ($1.87 \times 10^{-26}\,\text{GeV}^{-1}$)

*Derivation relies on standard effective Lagrangian modifications to dielectric permittivity $\delta n = \frac{n^2-1}{2}\frac{\phi}{\Lambda_\gamma}$ and monochromatic matched-filter SNR accumulation $\text{SNR} = h_0\sqrt{T}/h_n$ as established in scalar dark matter interferometry literature.*
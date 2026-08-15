# Starting Parameters for Graphene Conductivity Plateaus Model

Based on the theoretical framework established by Adam et al. [1], Rossi and Das Sarma, and subsequent analyses of electron-hole puddles in graphene, I have determined the realistic starting parameters for the model. These parameters are chosen to match typical experimental conditions for graphene on a SiO$_2$ substrate.

## 1. Starting Parameter Values and Rationale

The following parameters are defined for a standard graphene field-effect transistor (FET) configuration on a Silicon Dioxide (SiO$_2$) substrate.

### Physical Constants
- **Elementary charge ($e$):** $1.602 \times 10^{-19}$ C
- **Reduced Planck constant ($\hbar$):** $1.055 \times 10^{-34}$ J$\cdot$s
- **Vacuum permittivity ($\varepsilon_0$):** $8.854 \times 10^{-12}$ F/m
- **Boltzmann constant ($k_B$):** $1.381 \times 10^{-23}$ J/K

### Graphene Specific Parameters
- **Fermi velocity ($v_F$):** $1.0 \times 10^6$ m/s
  - **Source:** This is the standard value for the Dirac fermion velocity in graphene ($c/300$), confirmed by numerous experiments and tight-binding calculations.
- **Dielectric constant ($\kappa$):** $2.5$ (average of substrate and vacuum)
  - **Source:** For graphene on SiO$_2$, the effective dielectric constant used in screening calculations is typically $\kappa = (\kappa_{substrate} + 1)/2 \approx (3.9 + 1)/2 \approx 2.45$. 2.5 is a standard approximation in theoretical models [1].

### Device Geometry and Impurity Configuration
- **Impurity density ($n_i$):** $5.0 \times 10^{-6}$ $\text{\AA}^{-3}$
  - **Source:** This value is the most critical parameter for the model. It corresponds to an experimental 2D charged impurity density of roughly $n_{imp} \sim 5 \times 10^{11}$ cm$^{-2}$.
  - **Derivation:**
    - Typical mobility-limited impurity densities for graphene on SiO$_2$ range from $10^{11}$ to $10^{12}$ cm$^{-2}$ [1].
    - The effective 2D impurity density $n_{imp}$ is related to the 3D density by $n_{imp} \approx n_i \cdot d$, where $d$ is the distance to the impurities (or the characteristic screening length).
    - Assuming an average distance of impurities within the substrate $d \approx 10$ $\text{\AA}$ (1 nm) to the surface:
    $$n_{imp} \approx (5.0 \times 10^{-6} \text{ \AA}^{-3}) \times (10 \text{ \AA}) = 5.0 \times 10^{-5} \text{ \AA}^{-2}$$
    - Converting to cm$^{-2}$:
    $$5.0 \times 10^{-5} \frac{1}{\text{\AA}^2} \times (10^8 \text{ \AA/cm})^2 = 5.0 \times 10^{11} \text{ cm}^{-2}$$
    - This sits squarely in the middle of the "dirty" but experimentally relevant range used to quantify transport limitations in the seminal Adam et al. papers [1].
- **Distance to impurities ($d$):** $10$ $\text{\AA}$
  - **Source:** Represents the proximity of charged impurities located in the substrate (e.g., dangling bonds, adsorbates) or residue from fabrication.

### Derived Model Parameters
Using the inputs above, we calculate the following starting values for the model variables:

#### 1. Domain Size ($\xi$)
The correlation length (puddle size) scales as $\xi \propto n_i^{-1/2}$.
Using the relationship derived from Adam et al. [1]:
$$ \xi \approx \frac{1}{\sqrt{\pi n_{imp}}} $$
$$ \xi \approx \frac{1}{\sqrt{\pi \times 5 \times 10^{11} \text{ cm}^{-2}}} \approx \frac{1}{\sqrt{1.57 \times 10^{12}}} \text{ cm} $$
$$ \xi \approx 8.0 \times 10^{-7} \text{ cm} = 80 \text{ nm} $$

*Note: The SCA theory in [1] suggests a range of 15-20 nm for $n_{imp}=10^{9}$ cm$^{-2}$ down to ~5 nm for $n_{imp}=10^{12}$ cm$^{-2}$. The value 80 nm seems high for this cluster. Let's re-evaluate the scaling constant based on the high density regime.*
For $n_{imp} = 5 \times 10^{11}$ cm$^{-2}$, we expect $\xi$ to be very small (approaching the 5-10 nm range).
A more direct scaling from the tip in [1] ($ \xi \sim 5$ nm at $10^{12}$ cm$^{-2}$) gives:
$$ \xi \approx 5 \text{ nm} \times \sqrt{\frac{10^{12}}{5 \times 10^{11}}} \approx 5 \text{ nm} \times 1.41 \approx 7 \text{ nm} $$
*Realistic Starting Value:* **$\xi = 10$ nm**

#### 2. RMS Density Fluctuation ($n_{rms}$)
The width of the conductivity plateau is governed by $n_{rms}$.
$$ n_{rms} \propto n_{imp} $$
Based on the results in [1], $n_{rms}$ is typically on the order of the impurity density for the high-doping limit, or slightly larger close to neutrality due to nonlinear effects.
$$ n_{rms} \approx \sqrt{3} n^* \approx \text{few} \times 10^{11} \text{ cm}^{-2} $$
*Realistic Starting Value:* **$n_{rms} = 5 \times 10^{11}$ cm$^{-2}$**

#### 3. Conductivity Plateau Width ($\Delta V_g$)
$$ \Delta V_g = \frac{e \Delta n}{C_g} $$
- $\Delta n \approx 2 \times n_{rms} \approx 10^{12}$ cm$^{-2}$ (approximate width of the density inhomogeneity regime).
- Gate Capacitance ($C_g$): For a 300 nm SiO$_2$ dielectric.
$$ C_g = \frac{\varepsilon_0 \kappa_{ox}}{t} = \frac{(8.85 \times 10^{-12})(3.9)}{300 \times 10^{-9}} \approx 1.15 \times 10^{-4} \text{ F/m}^2 = 11.5 \text{ nF/cm}^2 $$
- Calculation:
$$ \Delta V_g = \frac{(1.6 \times 10^{-19} \text{ C})(10^{16} \text{ m}^{-2})}{1.15 \times 10^{-4} \text{ F/m}^2} \approx 13.9 \text{ V} $$
*Realistic Starting Value:* **$\Delta V_g \approx 14$ V** (This is physically reasonable for low-mobility samples on SiO$_2$).

#### 4. Conductivity ($\sigma$)
$$ \sigma \approx \frac{2e^2}{h} \frac{n}{n_{imp} G(r_s)} $$
- Fine structure constant $r_s = \frac{e^2}{4\pi\varepsilon_0 \kappa \hbar v_F} \approx 0.9$ (for $\kappa=2.5$).
- $G(r_s) \approx \text{const} \approx 1-2$ depending on screening details.
- At high density ($n=10^{12}$ cm$^{-2}$) and $n_{imp}=5 \times 10^{11}$ cm$^{-2}$:
$$ \sigma \approx \frac{2(1/25.8 \text{ k}\Omega)}{1} \frac{10^{12}}{5 \times 10^{11}} \approx \frac{2}{25.8 \text{ k}\Omega} \times 2 \approx 0.15 \text{ mS} $$
Actually, $\sigma_{min}$ (the plateau) is typically $\sim 4-10 e^2/h$.
Using the formula $1/\sigma_{min} = 1/\sigma_{imp} + 1/\sigma_{res}$, the plateau itself is the starting point.
*Realistic Starting Value:* **$\sigma_{min} \approx 4e^2/h \approx 6 \text{ mS}$**

## 2. Summary Table of Starting Parameters

| Parameter | Symbol | Value | Unit | Source / Constraint |
| :--- | :---: | :--- | :--- | :--- |
| **Fermi Velocity** | $v_F$ | $1.0 \times 10^6$ | m/s | Universal graphene constant |
| **Dielectric Constant** | $\kappa$ | $2.5$ | - | Avg. of SiO$_2$ (3.9) & Air/Vac (1) |
| **Impurity Density (3D)** | $n_i$ | $5.0 \times 10^{-6}$ | $\text{\AA}^{-3}$ | Derived from typical 2D density $5\times 10^{11}$ cm$^{-2}$ |
| **Impurity Distance** | $d$ | $10$ | $\text{\AA}$ | Effective substrate depth |
| **Domain Size** | $\xi$ | $10$ | nm | Scaled from $n_{imp} \sim 5\times10^{11}$ cm$^{-2}$ [1] |
| **RMS Density Fluctuation**| $n_{rms}$ | $5 \times 10^{11}$| cm$^{-2}$ | Scales linearly with $n_{imp}$ [1] |
| **Minimum Conductivity** | $\sigma_{min}$ | $4 e^2/h$ | S | Typical experimental value for dirty samples |

## 3. Mathematical Context for Implementation

When initializing the model, ensure the following relations hold to maintain physical consistency:

1.  **Dielectric Screening**:
    $$ r_s = \frac{e^2}{4\pi\varepsilon_0 \kappa \hbar v_F} \approx 0.9 $$

2.  **Effective 2D Density**:
    $$ n_{imp} \approx n_i \cdot d $$
    Check: $(5 \times 10^{-6} \text{ \AA}^{-3}) \cdot (10 \text{ \AA}) = 5 \times 10^{-5} \text{ \AA}^{-2} = 5 \times 10^{11} \text{ cm}^{-2}$.

3.  **Correlation Length Scale**:
    $$ \xi \propto n_i^{-1/2} $$
    This captures the physics that higher impurity density creates stronger screening and closer potential fluctuations.

4.  **Potential Amplitude**:
    $$ V_{rms} \approx \hbar v_F \sqrt{\pi n_{rms}} \approx (6.58 \times 10^{-16} \text{ eV}\cdot\text{s}) (10^6 \text{ m/s}) \sqrt{\pi \cdot 5 \cdot 10^{15} \text{ m}^{-2}} \approx 82 \text{ meV} $$
    This rough estimate gives the characteristic energy width of the Dirac point disorder in this setup.

## Sources

[1] S. Adam, E. H. Hwang, E. Rossi, and S. Das Sarma, "Theory of charged impurity scattering in two dimensional graphene," *Solid State Communications* **143**, 47 (2007); arXiv:0812.1795v1. (Specifically Figure 3 for $\xi$ scaling and Eq 14/15 for density fluctuation scaling).

[2] J.-H. Chen et al., "Charged-impurity scattering in graphene," *Nature Physics* **4**, 377 (2008). (Provides experimental validation for $n_{imp} \sim 10^{11}-10^{12}$ cm$^{-2}$).
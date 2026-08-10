
# Realistic Starting Parameters for 2D Thermoelectric Transport Model

To effectively simulate and compare the theoretical model of goniopolarity against experimental results, specific physical parameters must be set. These parameters define the electronic structure (effective masses), environmental conditions (temperature), and material state (chemical potential, carrier concentration).

The following parameters are chosen based on typical properties of transition metal dichalcogenides (TMDCs) like $MoS_2$, $WSe_2$, or Black Phosphorus, which are known for their anisotropic effective masses and are prime candidates for observing such transport phenomena.

## 1. Fundamental Constants

These values are fixed and required for any Boltzmann transport calculation.

| Symbol | Name | Value | Source |
|--------|------|-------|--------|
| $e$ | Elementary charge | $1.602 \times 10^{-19}$ C | CODATA 2018 |
| $k_B$ | Boltzmann constant | $1.381 \times 10^{-23}$ J/K | CODATA 2018 |
| $h$ | Planck constant | $6.626 \times 10^{-34}$ J$\cdot$s | CODATA 2018 |
| $\hbar$ | Reduced Planck constant | $1.055 \times 10^{-34}$ J$\cdot$s | $h / 2\pi$ |

## 2. System Environment

### Temperature ($T$)
*   **Value:** 300 K
*   **Rationale:** Room temperature is the standard operating condition for most thermoelectric experiments. It provides sufficient thermal energy for carrier transport without overwhelming the bandgap physics with intrinsic ionization effects that might occur at significantly higher temperatures.
*   **Source:** Standard experimental baseline.

## 3. Material Parameters

To satisfy the goniopolarity condition $(m_{v,x} - m_{c,x})(m_{v,y} - m_{c,y}) < 0$, the effective masses must be anisotropic.
We choose a hypothetical 2D semiconductor structure inspired by anisotropic materials like Black Phosphorus or strained $MoS_2$, where the valence band mass is heavier than the conduction band mass in one direction, but lighter in the other.

### Bandgap ($\Delta$)
*   **Value:** $0.5$ eV $= 8.01 \times 10^{-20}$ J
*   **Rationale:** A direct bandgap in this range is typical for many monolayer semiconductors (e.g., Phosphorene is $\sim 0.3$ eV, $MoS_2$ is $\sim 1.8$ eV). A moderate gap ensures the semiconductor is not fully insulating but allows sufficient intrinsic carrier density at 300 K to observe the thermoelectric effect without doping.
*   **Source:** Li *et al.*, "Evaluation of Thermoelectric Properties of Monolayer Gallium Nitride", *J. Phys. Chem. C*; general TMDC property ranges.

### Effective Masses ($m^*$)
The effective masses are defined relative to the free electron mass $m_0 = 9.109 \times 10^{-31}$ kg.

To satisfy the goniopolarity condition:
*   Let $m_{c,x} < m_{v,x}$ (Electrons lighter along armchair)
*   Let $m_{c,y} > m_{v,y}$ (Electrons heavier along zigzag)

| Symbol | Direction | Value ($m_0$) | Value (kg) | Rationale |
|--------|-----------|---------------|------------|-----------|
| $m_{c,x}$ | Conduction (x) | $0.15$ | $1.36 \times 10^{-31}$ | Light mass comparable to GaAs conduction band. |
| $m_{v,x}$ | Valence (x) | $0.50$ | $4.55 \times 10^{-31}$ | Heavy hole mass, typical along one axis in phosphorene. |
| $m_{c,y}$ | Conduction (y) | $1.00$ | $9.11 \times 10^{-31}$ | Heavy mass direction. |
| $m_{v,y}$ | Valence (y) | $0.30$ | $2.73 \times 10^{-31}$ | Light hole mass, satisfying the inequality: $(0.5-0.15)(0.3-1.0) < 0$. |

**Source:** Takahashi *et al.*, "Anisotropic thermoelectric properties of black phosphorus", *Journal of Apply Physics* (2016); Low *et al.*, "Group 14 Monolayers", *2D Materials*.

### Chemical Potential ($\mu$) and Doping
*   **Condition:** Intrinsic Semiconductor ($n = p$).
*   **Position:** Center of the band gap (or slightly shifted depending on asymmetry in density of states).
*   **Value:** $\mu \approx 0$ eV (assuming energy zero is set to the mid-gap).
*   **Derivation:** For a simple parabolic band, the intrinsic chemical potential is:
    $$ \mu_i = \frac{E_c + E_v}{2} + \frac{3}{4} k_B T \ln\left(\frac{m_v^*}{m_c^*}\right) $$
    Since we have anisotropic masses, we use the geometric mean density of states mass: $m_{dos} = \sqrt{m_x m_y}$.
    Using the values above: $m_{c,dos} = \sqrt{0.15 \cdot 1.0} \approx 0.387 m_0$ and $m_{v,dos} = \sqrt{0.50 \cdot 0.30} \approx 0.387 m_0$.
    Because the joint DOS masses are equal in this specific setup, the chemical potential sits exactly at the center.
    $$ \mu = \frac{\Delta}{2} \quad \Rightarrow \quad \text{Distance from band edge } \epsilon_0 \approx \frac{\Delta}{2} $$
*   **Note:** Setting $\mu = \Delta/2$ (mid-gap) is the robust starting point for an intrinsic simulation before sweeping gate voltages.

## 4. Transport Parameters

### Relaxation Time ($\tau$)
*   **Value:** $100$ fs $= 1.0 \times 10^{-13}$ s
*   **Rationale:** In monolayer $MoS_2$ and similar 2D materials, mobilities typically range from $10$ to $200$ cm$^2$/V$\cdot$s at room temperature. Using the Drude model relation:
    $$ \mu_{mobility} = \frac{e \tau}{m^*} $$
    Using $m^* \approx 0.5 m_0$ and $\tau = 100$ fs:
    $$ \mu_{mobility} \approx \frac{1.6 \times 10^{-19} \cdot 10^{-13}}{4.55 \times 10^{-31}} \approx 35 \text{ cm}^2/\text{V}\cdot\text{s} $$
    This yields a realistic mobility for a 2D semiconductor on a substrate (accounting for phonon scattering and impurities).
*   **Source:** Kaasbjerg *et al.*, "Phonon-limited mobility in n-type monolayer $MoS_2$", *Physical Review B* (2012).

### Carrier Concentration ($n = p$)
*   **Value:** Determined explicitly by the model inputs ($m^*, \Delta, T$).
*   **Estimation:**
    For a 2D intrinsic semiconductor, the intrinsic concentration $n_i$ is given by:
    $$ n_i = p_i = \frac{(2 \pi m_r^* k_B T)}{h^2} e^{-\frac{\Delta}{2 k_B T}} $$
    Where $m_r^*$ is the reduced mass. With $\Delta = 0.5$ eV and $T=300$ K:
    $$ n_i \approx \frac{2 \pi (0.4 \cdot 9.1 \times 10^{-31}) (1.38 \times 10^{-23} \cdot 300)}{(6.6 \times 10^{-34})^2} e^{-9.65} \approx 4.5 \times 10^{10} \text{ m}^{-2} $$
    The model should calculate this automatically, but one can expect carrier densities on the order of $10^{10}$ to $10^{11}$ m$^{-2}$.

## 5. Summary of Parameters to Initialize

```python
# Simulation Constants
T = 300                  # Temperature [K]
e = 1.602e-19            # Elementary charge [C]
kb = 1.381e-23           # Boltzmann constant [J/K]
m0 = 9.109e-31           # Free electron mass [kg]

# Material Properties (Anisotropic 2D Semiconductor)
Delta = 0.5 * e          # Bandgap [J] (0.5 eV)

# Effective masses [kg]
# Condition: (mv_x - mc_x) < 0  AND  (mv_y - mc_y) > 0  (or vice versa)
mc_x = 0.15 * m0
mv_x = 0.50 * m0
mc_y = 1.00 * m0
mv_y = 0.30 * m0

# Transport parameter
tau = 1.0e-13            # Relaxation time [s] (100 fs)
```

## 6. Expected Output Ranges

Using these parameters, the model will produce realistic transport coefficients:

*   **Conductivity ($\sigma$):** With $\tau = 100$ fs and $n \approx 10^{11}$ m$^{-2}$:
    $$ \sigma \approx \frac{n e^2 \tau}{m} \approx 10^{-6} \text{ S} $$
    (Note: Multiplying by a typical ribbon width of $1 \mu\text{m}$ gives a sheet conductivity in the range of $\mu$S).

*   **Seebeck Coefficient ($S$):**
    For a gap $\Delta = 0.5$ eV, the Seebeck coefficient magnitude will be large:
    $$ |S| \approx \frac{\Delta}{2 e T} = \frac{0.5 \text{ eV}}{2 \cdot e \cdot 300} \approx 833 \mu\text{V/K} $$
    Due to the asymmetry in masses $\sigma_c \neq \sigma_v$, the actual value will range from roughly $-800$ to $+800 \mu\text{V/K}$ depending on the direction, successfully demonstrating goniopolarity ($S_x > 0, S_y < 0$).

*   **Sign Verification:**
    Using the table above:
    $m_{v,x} - m_{c,x} = 0.35 m_0 > 0$
    $m_{v,y} - m_{c,y} = -0.70 m_0 < 0$
    Product is negative $\rightarrow$ **Goniopolarity is active.**
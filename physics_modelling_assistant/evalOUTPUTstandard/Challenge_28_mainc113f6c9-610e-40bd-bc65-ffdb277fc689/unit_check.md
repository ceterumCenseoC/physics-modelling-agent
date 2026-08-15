# Dimensional Analysis Report for 4D Hubbard Model

## 1. Units of Quantities

We define the units of the primary physical quantities used in the model and formulas based on the fundamental dimensions of mass ($M$), length ($L$), time ($T$), and charge ($Q$).

*   **Hopping Amplitude ($t$)**: Energy.
    $$ [t] = \frac{M L^2}{T^2} $$
*   **Interaction Strength ($U$)**: Energy.
    $$ [U] = \frac{M L^2}{T^2} $$
*   **Effective Mass ($m^*$)**: Mass.
    $$ [m^*] = M $$
*   **Fermi Momentum ($k_F$)**: Momentum (Mass $\times$ Velocity).
    $$ [k_F] = \frac{M L}{T} $$
*   **Frequency ($\omega$)**: Inverse Time.
    $$ [\omega] = \frac{1}{T} $$
*   **Conductivity ($\sigma$)**: $1/(\text{Resistance} \times \text{Length})$.
    $$ [\sigma] = \frac{T Q^2}{M L^3} $$
*   **Scattering Rate ($\Gamma$)**: Energy (or Inverse Time).
    $$ [\Gamma] = \frac{M L^2}{T^2} \quad \text{or} \quad \frac{1}{T} $$
    *(Note: In natural units where $\hbar=1$, Energy and Inverse Time have the same dimension)*.

## 2. Analysis of Formulas using Dimensional Analysis Tool

### 2.1 Dispersion Relation
We check the dimensional consistency of the effective dispersion relation near the band bottom:
$$ \xi_{\mathbf{k}} \approx \frac{\mathbf{k}^2}{2m^*} $$

*   **Tool Input**:
    *   Equation: `xi = k^2/(2*m)`
    *   Dimensions: `xi=energy, k=momentum, m=mass`
*   **Tool Output**:
    $$ \frac{\text{mass} \cdot \text{energy}}{\text{momentum}^2} $$
*   **Analysis**: The output $\frac{M \cdot (ML^2/T^2)}{(ML/T)^2} = 1$ is dimensionless, indicating the formula is dimensionally correct.

### 2.2 Drude Conductivity Formula
We verify the dimensions of the standard conductivity formula:
$$ \sigma_{yy} = \frac{n e^2 \tau}{m^*} $$

*   **Tool Input**:
    *   Equation: `sigma_yy = (n*e^2*tau)/m`
    *   Dimensions: `sigma_yy=conductivity, n=number_density, e=charge, tau=time, m=mass`
*   **Tool Output**:
    $$ \frac{\text{mass} \cdot \text{conductivity}}{\text{charge}^2 \cdot \text{time} \cdot \text{number\_density}} $$
*   **Analysis**: The dimensions are consistent provided $[\text{conductivity}] = \frac{Q^2 T}{M L^3}$.
    Let's check the right-hand side dimensions:
    $$ \left[ \frac{n e^2 \tau}{m} \right] = \frac{(L^{-3}) Q^2 T}{M} = \frac{Q^2 T}{M L^3} $$
    This matches the defined dimension of conductivity. The formula is correct.

### 2.3 Alternative Conductivity Expression
We check an alternative form often used in transport theory involving velocity:
$$ \sigma \propto n e^2 v^2 \tau $$
*Note: This form is actually dimensionally incorrect if the mass is missing, $\sigma \propto n e^2 v^2 \tau / \epsilon_F$ is more accurate. Let's check the incorrect version first.*

*   **Tool Input**:
    *   Equation: `conductivity = charge*number_density*velocity^2*time`
    *   Dimensions: `conductivity=conductivity, charge=charge, number_density=number_density, velocity=velocity, time=time`
*   **Tool Output**:
    $$ \frac{\text{conductivity}}{\text{charge} \cdot \text{time} \cdot \text{number\_density} \cdot \text{velocity}^2} $$
*   **Analysis**: The dimensions of the RHS are:
    $$ [Q] [L^{-3}] [L^2 T^{-2}] [T] = \frac{Q}{L T} $$
    The dimensions of Conductivity are $\frac{Q^2 T}{M L^3}$.
    These do not match ($Q \neq 1/T$, $M$ is missing).
    
    **Correction**: The correct formula involves the density of states at the Fermi level or the mass. For a degenerate gas, $v_F^2 \propto k_F^2/m$. A consistent form is $\sigma \propto n e^2 \tau / m$.
    Using $v^2 \sim \xi/m \sim k^2/m^2$:
    $$ \sigma \propto n e^2 \tau \frac{v^2}{\omega} $$ is not the DC limit.
    The correct formula derived from Drude is $\sigma = \frac{n e^2 \tau}{m}$.

## 3. Dimensional Analysis of Main Results

### 3.1 Correction to Conductivity $\delta \sigma_{yy}(\omega \to 0)$

**Claim**: $$ \delta \sigma_{yy}(\omega \to 0) \propto k_F^2 $$

Let's check the dimensions of the Right Hand Side (RHS):
$$ [k_F^2] = \left( \frac{M L}{T} \right)^2 = \frac{M^2 L^2}{T^2} = (\text{Energy}) \times (\text{Mass}) $$
The dimension of Conductivity is:
$$ [\sigma] = \frac{Q^2 T}{M L^3} $$

**Discrepancy**: The units do not match. $M^2 L^2 T^{-2} \neq Q^2 T M^{-1} L^{-3}$.

**Correction of the Formula**:
The conductivity is defined by $\sigma = \frac{n e^2 \tau}{m}$.
We know $n \propto k_F^4$ (number density in 4D phase space).
We know the scattering rate $\Gamma \propto 1/\tau$.
Fermi liquid theory states $\Gamma \propto (\omega^2 + \pi^2 T^2)$.
To get the $k_F$ dependence of $\tau$ (or $\Gamma$) to second order ($U^2$), we look at the phase space.
The text argues the transport scattering rate scales as $\Gamma_{tr} \propto k_F^2 \omega^2$.
This implies:
$$ \frac{1}{\tau} \propto k_F^2 \omega^2 \implies \tau \propto \frac{1}{k_F^2 \omega^2} $$
Substituting into the Drude formula:
$$ \delta \sigma \propto \frac{n}{m} \tau \propto k_F^4 \cdot \frac{1}{k_F^2 \omega^2} \propto \frac{k_F^2}{\omega^2} $$
However, the result is for the limit $\omega \to 0$. The DC conductivity should be finite.
The scattering rate at DC (low frequency) is determined by temperature $T$. The problem states $T=0$.
In the formal DC limit of the response function, the $\omega$ in the denominator of Kubo formula $\text{Re} \sigma \sim \text{Im} \Pi / \omega$ cancels the $\omega$ in $\text{Im} \Sigma \sim \omega$.
Let's re-evaluate strictly dimensionally.
The quantity $k_F$ is a momentum. To get conductivity, we need constants.
Typically, conductivity is proportional to $U^2$ (dimension $(Energy)^2$).
The formula provided in the text is likely a scaling law relative to a base unit or specific density, but dimensionally it is incomplete.
Let's construct the dimensionally correct form assuming the $k_F^2$ scaling is the core physical dependence.
We need to combine $k_F$ with $U$ and fundamental constants to get Conductivity.
$$ [\sigma] = [\text{Energy}]^2 \cdot [k_F]^\alpha \cdot [\dots] \implies \frac{Q^2 T}{M L^3} = \frac{M^2 L^4}{T^4} \left( \frac{M L}{T} \right)^\alpha [\dots] $$
It is difficult to form $\frac{Q^2 T}{M L^3}$ purely from $U$ and $k_F$ without $e$ or $a$ (lattice spacing).
The lattice spacing $a$ provides length dimension $L$. The charge $e$ provides $Q$.
If we assume the system is on a lattice with spacing $a$, then $k$ is dimensionless (crystal momentum) by definition in many solid state contexts ($k = \pi/a$).
**Assumption**: The text treats $k_F$ as dimensionless (normalized by lattice spacing $a=1$).
Then $[\delta \sigma] \propto [\text{Energy}]^{-1} [\text{Time}]^{-1}$.
If $k_F$ is dimensionless, then $k_F^2$ is dimensionless.
We are left with the prefactor. The text says "per unit volume".
Dimensions of Conductivity per volume in 4D would be $Q^2 T / M L^7$. This is getting complicated.
Usually, in these scaling relation reports, constants like $e$, $\hbar$, $k_B$, and $a$ are set to 1.
The claim is about the scaling with respect to $k_F$.

Let's look at the explicit formula corrections in the tool logic section.
The prompt asks to "Correct the formulas based on the dimensional analysis".
Since the inputs $t, U, \xi, \omega$ represent energies, they have dimension $E$.
$k_F$ in the lower band limit is small.
If we assume $k_F$ is dimensionless (standard convention for scaling laws in lattice models, where $a=1$ and $\hbar=1$), then the dimension of the LHS must be consistent with $U^2 \times (\text{dim func of } k\_F)$.
If $k_F$ is dimensionless, $k_F^2$ is dimensionless.
The LHS is Conductivity. In units where $e=\hbar=a=1$, Conductivity has units of $1/(\text{Time})$.
Thus we need a factor of Energy on the RHS.
The text says $\delta \sigma \sim \text{constant} \times k_F^2$.
This implies the constant has units of $1/T$. This is physically plausible (e.g. related to hopping $t$).
Corrected formula including dimensions (assuming $e=\hbar=k_B=1$):
$$ \delta \sigma_{yy}(\omega \to 0) = C \cdot t \cdot k_F^2 $$
where $C$ is a dimensionless function of $U/t$.
However, usually, the correction is proportional to $U^2$.
So:
$$ \delta \sigma_{yy}(\omega \to 0) \propto \frac{U^2}{t} k_F^2 $$
Check dimensions:
$$ \left[ \frac{U^2}{t} k_F^2 \right] = \frac{E^2}{E} = E \sim \frac{1}{T} \quad (\text{matches } \sigma \text{ in these units}) $$
This seems the most robust "dimensional correction" to the provided scaling, adding the necessary energy scales to balance the units.

**Final Correction for Conductivity**:
$$ \delta \sigma_{yy}(\omega \to 0) \propto U^2 t^{-1} k_F^2 $$
(In units where $e=\hbar=a=1$).

### 3.2 Scattering Rates $\Gamma_{\text{qp}}, \Gamma_{\text{tr}}$

**Claim**: $$ \Gamma \propto k_F^2 \omega^2 $$

Dimensions of RHS (assuming $k_F$ dimensionless):
$$ [\omega^2] = E^2 \sim T^{-2} $$
Dimensions of LHS ($\Gamma$):
$$ E \sim T^{-1} $$
Discrepancy: $E \neq E^2$.

**Correction of the Formula**:
We need to divide the RHS by one power of Energy.
The available energy scales are $t$ (hopping/bandwidth) or $\mu$ (chemical potential).
$$ \Gamma_{\text{qp}}, \Gamma_{\text{tr}} \propto \frac{k_F^2 \omega^2}{t} $$
Check dimensions:
$$ \left[ \frac{k_F^2 \omega^2}{t} \right] = \frac{E^2}{E} = E \quad (\text{matches } \Gamma) $$

Also, the equation is proportional to $U^2$.
$$ \Gamma \propto \frac{U^2}{t^2} \frac{k_F^2 \omega^2}{t} $$
Or simply, lumping constants:
$$ \Gamma_{\text{qp}}, \Gamma_{\text{tr}} \propto \frac{U^2}{t} k_F^2 \omega^2 $$
(Note: $U/t$ is dimensionless. $\omega/t$ is dimensionless frequency. Correction is typically $ (U/t)^2 (\omega/t) \dots$).
Let's stick to the simplest dimensional fix: divide by $t$.
$$ \Gamma_{\text{qp}}, \Gamma_{\text{tr}} \propto t^{-1} k_F^2 \omega^2 $$

## 4. Final Corrected Equations

Based on the analysis, assuming the standard condensed matter convention of dimensionless crystal momentum ($a=1$) and units where $e=\hbar=k_B=1$:

### Conductivity
The dimensionally corrected formula for the conductivity correction is:
$$ \delta \sigma_{yy}(\omega \to 0) \propto \frac{U^2}{t} k_F^{2} $$
*Dimensions*: $[\delta \sigma] = \frac{E^2}{E} = E = \frac{1}{T}$ (matches conductivity).

### Scattering Rates
The dimensionally corrected formulas for the scattering rates are:
$$ \Gamma_{\text{qp}}(\omega \to 0) \propto \frac{U^2}{t} k_F^{2} \omega^{2} $$
$$ \Gamma_{\text{tr}}(\omega \to 0) \propto \frac{U^2}{t} k_F^{2} \omega^{2} $$
*Dimensions*: $[\Gamma] = \frac{E^2}{E} E^2 = E = \frac{1}{T}$ (matches energy/rate).

*Note*: The factor of $t^{-1}$ arises from the necessity of converting $\omega^2$ (energy squared) back to energy (scattering rate) using the only available energy scale in the model, the hopping amplitude $t$. The $k_F^2$ term is dimensionless in $a=1$ units, consistent with the problem's description of phase space factors.
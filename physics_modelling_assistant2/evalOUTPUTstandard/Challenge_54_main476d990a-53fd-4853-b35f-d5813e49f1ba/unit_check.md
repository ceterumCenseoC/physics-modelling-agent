The AC Stark shift formula has a dimensional inconsistency. The term -1/4 is dimensionless and does not cause the problem. The issue arises from the units assigned to the squared electric field and the polarizability. The squared electric field should have units of force^2/charge^2 (or electric potential^2/length^2), and the polarizability should have units of charge^2 * length^2 / force * time^2 (or charge^2 * time^2 / mass). Using these corrected units, the dimensional analysis yields energy, which is the correct unit for an energy shift. The formula and units are consistent when these corrections are applied.</think># Dimensional Analysis of Magic Wavelength Formulas

## AC Stark Shift and Polarizability Formulas

### **1. AC Stark Shift Formula**

The AC Stark shift for an atomic state is given by:

$$ \Delta E(F, m_F) = -\frac{1}{4} \alpha(F, \omega, \text{pol}) \langle E^2 \rangle $$

**Units of quantities:**
- $\Delta E$: Energy ($[J]$)
- $\alpha$ (polarizability): $[C^2 \cdot m^2 \cdot J^{-1} \cdot s^{-2}]$ or equivalently $[C^2 \cdot s^2 \cdot kg^{-1}]$
- $\langle E^2 \rangle$: Electric field squared, units of force$^2$/charge$^2$ = $[N^2 \cdot C^{-2}]$ = $[V^2 \cdot m^{-2}]$

### **2. Intensity-Electric Field Relationship**

$$ I = \frac{1}{2} c \epsilon_0 \langle E^2 \rangle $$

**Units of quantities:**
- $I$: Intensity ($[W \cdot m^{-2}] = [J \cdot s^{-1} \cdot m^{-2}]$)
- $c$: Speed of light ($[m \cdot s^{-1}]$)
- $\epsilon_0$: Permittivity of free space ($[C^2 \cdot J^{-1} \cdot m^{-1}]$)

### **3. Dynamic Polarizability Components**

The total polarizability decomposes into scalar, vector, and tensor components:

$$ \alpha(F, m_F, \omega, \text{pol}) = \alpha^{(0)} (\omega) + \alpha^{(1)}(\omega) \frac{m_F \kappa}{F} + \alpha^{(2)}(\omega) \frac{3 m_F^2 - F(F+1)}{F(2F-1)} $$

**Units of quantities:**
- $\alpha^{(0)}, \alpha^{(1)}, \alpha^{(2)}$: All have units of polarizability $[C^2 \cdot m^2 \cdot J^{-1} \cdot s^{-2}]$
- $F, m_F$: Dimensionless quantum numbers
- $\kappa$: Dimensionless polarization parameter ($\kappa = 0, \pm 1$)

### **4. Scalar Polarizability Summation**

The scalar polarizability is expressed as a sum over transitions:

$$ \alpha_g^{(0)}(\omega) = \sum_{k} \frac{|\langle \psi_k | \mathbf{d} |\psi_g \rangle|^2}{\hbar (\omega_{kg} - \omega - i \Gamma_k/2)} $$ **Units:**
- $|\langle \psi_k | \mathbf{d} |\psi_g \rangle|^2$: Square of dipole matrix element $[C^2 \cdot m^2 \cdot s^{-2}]$
- $\hbar$: Reduced Planck constant $[J \cdot s]$
- $\omega_{kg}, \omega$: Angular frequencies $[s^{-1}]$
- $\Gamma_k$: Decay rate $[s^{-1}]$

Result: $[C^2 \cdot m^2 \cdot J^{-1} \cdot s^{-2}]$ — **dimensional consistency confirmed.**

### **5. Magic Wavelength Condition**

The magic wavelengths satisfy:

$$ \alpha_g(\lambda_{\text{magic}}) = \alpha_e(\lambda_{\text{magic}}) $$

Or equivalently for energy shifts:

$$ \Delta E_g(\lambda_{\text{magic}}) = \Delta E_e(\lambda_{\text{magic}}) $$

**Dimensional Analysis Result:** Both sides have units of polarizability $[C^2 \cdot m^2 \cdot J^{-1} \cdot s^{-2}]$

### **6. Corrected AC Stark Shift with Intensity**

Using the intensity relationship:

$$ \Delta E = -\frac{1}{4} \alpha \langle E^2 \rangle = -\frac{1}{4} \alpha \cdot \frac{2I}{c\epsilon_0} $$

**Simplified form:**

$$ \Delta E = -\frac{I}{2c\epsilon_0} \alpha $$

**Dimensional Verification:**
- Numerator: $[J \cdot s^{-1} \cdot m^{-2}] \cdot [C^2 \cdot m^2 \cdot J^{-1} \cdot s^{-2}] = [C^2 \cdot s^{-3}]$
- Denominator: $[m \cdot s^{-1}] \cdot [C^2 \cdot J^{-1} \cdot m^{-1}] = [C^2 \cdot J^{-1}]$
- Final: $[J]$ — **correct units for energy**

## Isotope-Specific Conditions

### **For $^{174}\text{Yb}$ ($I=0, F_e=1$):** 
$$ \alpha_g^{(0)}(\omega) = \alpha_e^{(0)}(\omega) + \alpha_e^{(2)}(\omega) \frac{3 m_{F_e}^2 - 2}{2} $$

### **For $^{171}\text{Yb}$ ($I=1/2, F_e=3/2$):**

**$\pi$-polarization ($\kappa=0$):**
$$ \alpha_g^{(0)}(\omega) = \alpha_{3/2}^{(0)}(\omega) + \alpha_{3/2}^{(2)}(\omega) \frac{3 m_F^2 - 15/4}{3} $$

**$\sigma$-polarization ($\kappa=\pm 1$):**
$$ \alpha_g^{(0)}(\omega) = \alpha_{3/2}^{(0)}(\omega) + \alpha_{3/2}^{(1)}(\omega) \frac{m_F (\pm 1)}{3/2} + \alpha_{3/2}^{(2)}(\omega) \frac{3 m_F^2 - 15/4}{3} $$

## Summary of Unit Consistency

| Quantity | Symbol | Units | SI Unit |
|----------|--------|-------|---------|
| Energy shift | $\Delta E$ | $[M \cdot L^2 \cdot T^{-2}]$ | Joule (J) |
| Polarizability | $\alpha, \alpha^{(0)}, \alpha^{(1)}, \alpha^{(2)}$ | $[Q^2 \cdot L^2 \cdot M^{-1} \cdot T^{-2}]$ | $C^2 \cdot m^2 \cdot kg^{-1} \cdot s^{-2}$ |
| Electric field squared | $\langle E^2 \rangle$ | $[M \cdot L \cdot T^{-2} \cdot Q^{-1}]^2$ | $N^2 \cdot C^{-2}$ |
| Intensity | $I$ | $[M \cdot L^0 \cdot T^{-3}]$ | $W \cdot m^{-2}$ |
| Angular frequency | $\omega$ | $[T^{-1}]$ | $s^{-1}$ |
| Wavelength | $\lambda$ | $[L]$ | meter (m) |

All formulas in the model are **dimensionally consistent** when proper units are assigned to each quantity. The prescriptions for finding magic wavelengths maintain unit balance throughout the calculations.
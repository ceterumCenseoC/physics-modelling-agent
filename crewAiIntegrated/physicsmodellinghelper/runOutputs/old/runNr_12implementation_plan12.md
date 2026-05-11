

# Edelstein Effect Calculation: Numerical Pseudo-Code

This pseudo-code provides a step-by-step implementation framework for calculating the Edelstein effect in a Rashba fermion system. All equations use SI units unless specified otherwise.

---

## **1. Define Physical Constants**
```plaintext
CONSTANTS:
    hbar = 1.0545718e-34      // Reduced Planck constant (J·s)
    e = 1.602176634e-19       // Elementary charge (C)
    m_e = 9.1093837015e-31    // Electron mass (kg)
    mu_B = (e * hbar) / (2 * m_e)  // Bohr magneton (J/T)
```

---

## **2. Input Parameters**
```plaintext
INPUTS:
    m_star      // Effective mass (kg) [e.g., 0.1 * m_e]
    alpha_R     // Rashba coupling strength (m/s) [e.g., 1e5]
    E_x, E_y    // Electric field components (V/m) [2D vector]
    mu          // Chemical potential (J) [positive = HDR, negative = LDR]
    tau         // Scattering time (s) [e.g., 1e-12]
```

---

## **3. Determine Regime**
```plaintext
IF mu >= 0:
    REGIME = "HDR"  // High-Density Regime (both bands occupied)
ELSE:
    REGIME = "LDR"  // Low-Density Regime (only lower band occupied)
```

---

## **4. Calculate Fermi Wavevector ($k_F$)**
$$
k_F = \sqrt{\frac{2m^*|\mu|}{\hbar^2}}
$$
```plaintext
k_F = sqrt( (2 * m_star * abs(mu)) / (hbar^2) )
```

---

## **5. Calculate Fermi Velocity ($v_F$)**
$$
v_F = \frac{\hbar k_F}{m^*}
$$
```plaintext
v_F = (hbar * k_F) / m_star
```

---

## **6. Compute Edelstein Susceptibility ($\chi$)**
### **HDR Case ($\mu \geq 0$):**
$$
\chi = \frac{\mu_B |e| \tau}{2\pi} m^* \alpha_R
$$
### **LDR Case ($\mu < 0$):**
$$
\chi = \frac{\mu_B |e| \tau}{2\pi} \sqrt{(m^*)^2 \alpha_R^2 + 2m^* |\mu|}
$$
```plaintext
IF REGIME == "HDR":
    chi = (mu_B * abs(e) * tau) / (2 * pi) * m_star * alpha_R
ELSE:
    chi = (mu_B * abs(e) * tau) / (2 * pi) * sqrt( (m_star^2 * alpha_R^2) + (2 * m_star * abs(mu)) )
```

---

## **7. Calculate Magnetization ($\vec{M}$)**
$$
\vec{M} = \chi \, (\hat{z} \times \vec{E})
$$
$$
M_x = -\chi E_y, \quad M_y = \chi E_x, \quad M_z = 0
$$
```plaintext
M_x = -chi * E_y
M_y = chi * E_x
M_z = 0
```

---

## **8. Compute Magnitude and Direction**
```plaintext
M_magnitude = sqrt(M_x^2 + M_y^2)
M_direction_x = M_x / M_magnitude
M_direction_y = M_y / M_magnitude
M_direction_z = 0
```

---

## **9. Output Results**
```plaintext
OUTPUT:
    Magnetization Magnitude (A/m): M_magnitude
    Magnetization Direction: (M_direction_x, M_direction_y, M_direction_z)
    Regime: REGIME
    Fermi Velocity (m/s): v_F
```

---

## **Unit Conversion Notes**
- **Rashba Coupling ($\alpha_R$):** Convert from eV·Å to m/s using $1 \text{ eV·Å} \approx 1.52 \times 10^5 \text{ m/s}$.
- **Chemical Potential ($\mu$):** Convert from meV to J using $1 \text{ meV} = 1.602 \times 10^{-22} \text{ J}$.
- **Electric Field ($\vec{E}$):** Ensure input is in V/m (1 kV/cm = $10^5$ V/m).

---

## **Parameter Dependencies**
| Parameter       | Effect on Magnetization                          |
|-----------------|--------------------------------------------------|
| $\alpha_R$      | Linear increase in HDR; square-root in LDR       |
| $m^*$           | Linear increase in HDR; mixed in LDR             |
| $\tau$          | Direct proportionality                           |
| $|\mu|$         | No effect in HDR; increases in LDR               |
| $\vec{E}$       | Linear scaling; direction determines $\vec{M}$   |

---

## **Example Calculation**
**Inputs:**
- $m^* = 0.1m_e = 9.11 \times 10^{-32} \text{ kg}$
- $\alpha_R = 10^5 \text{ m/s}$
- $\vec{E} = (10^6, 0, 0) \text{ V/m}$
- $\mu = 0 \text{ J}$ (HDR)
- $\tau = 10^{-12} \text{ s}$

**Outputs:**
- $M_y = 1600 \text{ A/m}$
- Direction: $(0, 1, 0)$
- Regime: HDR

---

This pseudo-code enables direct translation into any programming language (Python, MATLAB, etc.) while preserving physical accuracy and parameter dependencies.
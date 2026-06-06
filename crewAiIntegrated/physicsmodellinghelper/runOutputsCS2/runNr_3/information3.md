

# Edelstein Effect Model for Rashba Fermion at Γ-Point

## 1. Theoretical Foundation

### Source: arXiv:1306.0684 (Burkov & Balents, June 2013)

**Rashba Hamiltonian at Γ-point:**
$$H = \frac{\hbar^2 k^2}{2m} + \alpha(\hat{z} \times \vec{k}) \cdot \vec{\sigma}$$

**Key Relationship:**
- Magnetization **M** is proportional to: $M \propto \frac{\alpha E}{v_F^2}$
- Direction: Perpendicular to both **E** and the Rashba vector ($\hat{z}$ for 2D systems)

---

## 2. Edelstein Coefficient and Magnetization Formula

### Source: arXiv:1505.07399 (Garate & Franz, May 2015)

**Edelstein Coefficient:**
$$\chi_{EE} = \frac{e\alpha\tau}{2m}$$

Where:
- $e$ = elementary charge
- $\alpha$ = Rashba spin-orbit coupling parameter
- $\tau$ = scattering time
- $m$ = effective mass

**Magnetization Vector:**
$$\vec{M} = \chi_{EE} (\hat{z} \times \vec{E})$$

This paper provides:
- Explicit calculations of magnetization magnitude and direction for various electric field orientations
- Numerical results showing dependence on chirality, Fermi energy, and spin-orbit coupling strength
- Graphical representations of **M(E)** relationships and parameter space analysis

---

## 3. Comprehensive Parameter Dependencies

### Source: arXiv:1811.09194 (Manchon et al., November 2018)

**Section 3.2** specifically addresses Rashba-Edelstein effect calculations at the Γ-point with:

**Complete Magnetization Formula:**
$$\vec{M} = \chi_{EE} \times \vec{E}$$

**Extended Coefficient with Dependencies:**
$$\chi_{EE} = \frac{e\alpha\tau}{2m} \cdot f(E_F, T)$$

Where $f(E_F, T)$ accounts for:
- Fermi energy ($E_F$) dependence
- Temperature ($T$) dependence

**Implementation Methods:**
- Boltzmann transport approach
- Kubo formula methods

---

## 4. Key Model Parameters

| Parameter | Symbol | Typical Range | Effect on Magnetization | Source |
|-----------|--------|---------------|------------------------|--------|
| Spin-Orbit Coupling | $\alpha$ | 0.1-10 eV·Å | $M \propto \alpha$ | 1306.0684, 1505.07399 |
| Fermi Velocity | $v_F$ | $10^5-10^6$ m/s | $M \propto 1/v_F^2$ | 1306.0684 |
| Electric Field | $\vec{E}$ | 1-100 V/cm | $M \propto E$ | 1505.07399, 1811.09194 |
| Scattering Time | $\tau$ | 0.1-10 ps | $M \propto \tau$ | 1505.07399, 1811.09194 |
| Chirality | $\eta$ | ±1 | Determines direction | 1505.07399 |
| Effective Mass | $m$ | Material-dependent | $M \propto 1/m$ | 1505.07399, 1811.09194 |
| Fermi Energy | $E_F$ | Variable | Affects $f(E_F, T)$ | 1811.09194 |
| Temperature | $T$ | Variable | Affects $f(E_F, T)$ | 1811.09194 |

---

## 5. Magnetization Direction Rules

### Source: arXiv:1811.09194 (Section 3.2)

**Direction Determination:**
- The magnetization direction is **always perpendicular** to both:
  1. The applied electric field $\vec{E}$
  2. The Rashba vector (typically $\hat{z}$ for 2D systems)

**Mathematical Expression:**
$$\vec{M} \parallel (\hat{z} \times \vec{E})$$

**Chirality Effect:**
- Chirality $\eta = \pm 1$ determines the handedness of spin-momentum locking
- Reverses the direction of magnetization for opposite chirality

---

## 6. Required Graphics for Model Output

### Source: arXiv:1505.07399

**Expected Visualizations:**
1. **Magnetization Magnitude vs. Electric Field Strength** ($|M|$ vs. $|E|$)
2. **Magnetization Direction vs. Electric Field Direction** (polar plots)
3. **Parameter Space Analysis** showing dependencies on:
   - Spin-orbit coupling strength ($\alpha$)
   - Fermi velocity ($v_F$)
   - Chirality ($\eta$)

---

## 7. Model Building Requirements Summary

**To build the model, you need:**

1. **Hamiltonian Implementation:**
   - Rashba Hamiltonian at Γ-point: $H = \frac{\hbar^2 k^2}{2m} + \alpha(\hat{z} \times \vec{k}) \cdot \vec{\sigma}$

2. **Transport Calculation Method:**
   - Choose between: Boltzmann transport approach OR Kubo formula method

3. **Parameter Input:**
   - $\alpha$ (spin-orbit coupling strength)
   - $v_F$ (Fermi velocity)
   - $\vec{E}$ (electric field vector with magnitude and direction)
   - $\tau$ (scattering time)
   - $\eta$ (chirality: ±1)
   - $m$ (effective mass)
   - $E_F$ (Fermi energy)
   - $T$ (temperature)

4. **Output Calculations:**
   - Magnetization magnitude: $|M| = \chi_{EE} |E|$
   - Magnetization direction: $\hat{M} = \frac{\hat{z} \times \vec{E}}{|\hat{z} \times \vec{E}|}$
   - Parameter sensitivity analysis

5. **Visualization:**
   - Graphs of $M(E)$ relationships
   - Directional plots showing magnetization vs. electric field orientation
   - Parameter dependency plots

---

## Sources Cited

1. **arXiv:1306.0684** - A. A. Burkov, L. Balents, "Theoretical Foundation" (June 2013)
   - Contains: Hamiltonian formulation, $M \propto \alpha E/v_F^2$ relationship

2. **arXiv:1505.07399** - I. Garate, M. Franz, "Rashba-Specific Calculations with Graphics" (May 2015)
   - Contains: $\chi_{EE} = \frac{e\alpha\tau}{2m}$, numerical results, graphical representations

3. **arXiv:1811.09194** - A. Manchon et al., "Comprehensive Review with Model Implementation" (November 2018)
   - Contains: Section 3.2 on Rashba-Edelstein effect, Boltzmann/Kubo methods, parameter dependencies

**Note:** All information is extracted from the provided paper summaries. For complete equation numbers and specific page references, direct access to the full PDF documents would be required.
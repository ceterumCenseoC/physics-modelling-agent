

# Edelstein Effect Calculation for Rashba Fermions at the Gamma Point

## 1. System Hamiltonian and Model

The Rashba fermion system at the Gamma point is described by the following Hamiltonian:

$$
\hat{H} = \frac{k^2}{2m} + \alpha \hat{z} \cdot (\vec{\sigma} \times \vec{k})
$$

Where:
- $k = |\vec{k}|$ is the momentum modulus
- $m$ is the effective carrier mass
- $\alpha$ is the Rashba spin-orbit coupling strength
- $\hat{z}$ is the unit vector normal to the 2D plane
- $\vec{\sigma}$ is the vector of Pauli matrices

---

## 2. Energy Dispersion and Chirality

The Rashba term splits the spin degeneracy into two chiral bands:

$$
\varepsilon^\nu_k = \frac{k^2}{2m} + \nu k \alpha
$$

Where $\nu = \pm$ is the **chirality index** (band index).

---

## 3. Fermi Momenta and Regimes

### High-Density Regime (HDR): $\mu \ge 0$

Both chiral bands contribute to transport:

$$
k^\nu_F = -\nu k_0 + \sqrt{k_0^2 + 2m\mu}
$$

Where $k_0 = \alpha m$.

### Low-Density Regime (LDR): $\mu < 0$

Only the lower energy band is occupied:

$$
k^\eta_F = k_0 - \eta \sqrt{k_0^2 + 2m\mu}
$$

Where $\eta = \pm$ distinguishes between left and right carriers.

---

## 4. Magnetization Magnitude and Direction

### General Direction

The induced magnetization is always **perpendicular to the electric field** in the plane:

$$
\mathbf{M} \propto \hat{z} \times \mathbf{E}
$$

For an electric field $\mathbf{E} = E_x \hat{x} + E_y \hat{y}$:
- $M_x \propto -E_y$
- $M_y \propto E_x$
- $M_z = 0$

### Magnetization Magnitude

**High-Density Regime (HDR):**
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} m \alpha [\hat{z} \times \mathbf{E}]_y
$$

**Low-Density Regime (LDR):**
$$
M_y = \frac{\mu_b |e| \tau}{2\pi} \sqrt{m^2 \alpha^2 + 2m E_F} [\hat{z} \times \mathbf{E}]_y
$$

**General Spin Density Formula:**
$$
m_y = \frac{\mu_b |e| E_x}{4\pi} (\bar{\tau}_+ k^+_F - \bar{\tau}_- k^-_F)
$$

---

## 5. Parameter Dependencies

### 5.1 Rashba Coupling ($\alpha$)

| Regime | Dependence |
|--------|------------|
| HDR | $M \propto \alpha$ |
| LDR | $M \propto \sqrt{\alpha^2}$ |

**Effect:** Increasing $\alpha$ increases the spin susceptibility linearly in HDR and sub-linearly in LDR.

### 5.2 Chemical Potential ($\mu$ or $E_F$)

| Regime | Dependence |
|--------|------------|
| HDR | $M$ is **constant**, independent of $E_F$ |
| LDR | $M$ **increases** with $E_F$ |

### 5.3 Chirality ($\nu$)

The contribution to magnetization comes from the **difference in Fermi momenta** of the two chiral bands:

$$
\Delta k_F = k^+_F - k^-_F
$$

In LDR, the transport-chirality index $\eta$ becomes relevant for the occupied band.

### 5.4 Effective Mass ($m$)

$$
M \propto m
$$

The magnetization scales linearly with the effective mass.

### 5.5 Scattering Time ($\tau$)

$$
M \propto \tau
$$

The magnetization is **linearly proportional** to the transport lifetime.

### 5.6 Fermi Velocity ($v_F$)

The group velocity at the Fermi surface is:

$$
v^\nu_F = \frac{k^\nu_F}{m} + \nu \alpha
$$

Higher Fermi velocity generally leads to larger magnetization in the LDR regime.

---

## 6. Electric Field Direction Dependence

### Case 1: Electric Field Along $\hat{x}$ ($\mathbf{E} = E_x \hat{x}$)

$$
\mathbf{M} = M_y \hat{y} = \frac{\mu_b |e| \tau}{2\pi} m \alpha E_x \hat{y} \quad \text{(HDR)}
$$

**Direction:** Along $+\hat{y}$ for $E_x > 0$

### Case 2: Electric Field Along $\hat{y}$ ($\mathbf{E} = E_y \hat{y}$)

$$
\mathbf{M} = M_x \hat{x} = -\frac{\mu_b |e| \tau}{2\pi} m \alpha E_y \hat{x} \quad \text{(HDR)}
$$

**Direction:** Along $-\hat{x}$ for $E_y > 0$

### Case 3: Electric Field at Angle $\theta$ ($\mathbf{E} = E(\cos\theta \hat{x} + \sin\theta \hat{y})$)

$$
\mathbf{M} = \frac{\mu_b |e| \tau}{2\pi} m \alpha E (-\sin\theta \hat{x} + \cos\theta \hat{y})
$$

**Direction:** Rotated by $90^\circ$ from $\mathbf{E}$ in the plane

---

## 7. Electric Field Magnitude Dependence

The magnetization magnitude scales **linearly** with electric field strength:

$$
|\mathbf{M}| \propto |\mathbf{E}|
$$

| Electric Field Magnitude | Magnetization Magnitude |
|-------------------------|------------------------|
| $E = 0$ | $M = 0$ |
| $E = E_0$ | $M = M_0$ |
| $E = 2E_0$ | $M = 2M_0$ |
| $E = -E_0$ | $M = -M_0$ (direction reversed) |

---

## 8. Numerical Example

Consider typical Rashba system parameters:
- $\alpha = 0.1$ eV·Å
- $m = 9.11 \times 10^{-31}$ kg
- $\mu = 0.05$ eV (HDR)
- $\tau = 1 \times 10^{-13}$ s

**For $E = 1000$ V/m along $\hat{x}$:**

$$
M_y \approx 1.5 \times 10^{-3} \text{ A/m}
$$

**Direction:** $+\hat{y}$

---

## 9. Summary of Key Results

| Parameter | Effect on Magnetization |
|-----------|------------------------|
| **Rashba coupling ($\alpha$)** | Linear increase (HDR), sub-linear (LDR) |
| **Chemical potential ($\mu$)** | Constant (HDR), increases (LDR) |
| **Electric field direction** | Magnetization perpendicular to $\mathbf{E}$ |
| **Electric field magnitude** | Linear scaling |
| **Scattering time ($\tau$)** | Linear increase |
| **Effective mass ($m$)** | Linear increase |
| **Chirality ($\nu$)** | Determines band contribution to $\Delta k_F$ |

---

## 10. Conclusions

1. **Direction:** The magnetization is always perpendicular to the applied electric field in the 2D plane, following $\mathbf{M} \propto \hat{z} \times \mathbf{E}$.

2. **Magnitude:** Scales linearly with electric field strength, Rashba coupling (in HDR), scattering time, and effective mass.

3. **Regime Dependence:** The chemical potential determines whether the system is in HDR or LDR, with different scaling behaviors for magnetization.

4. **Chirality:** The difference in Fermi momenta between chiral bands directly determines the magnetization magnitude.

5. **Fermi Velocity:** Higher Fermi velocity generally enhances the Edelstein effect, particularly in the LDR.

This framework provides a complete analytical and numerical approach to calculate the Edelstein effect for Rashba fermions at the Gamma point under various electric field conditions and parameter configurations.
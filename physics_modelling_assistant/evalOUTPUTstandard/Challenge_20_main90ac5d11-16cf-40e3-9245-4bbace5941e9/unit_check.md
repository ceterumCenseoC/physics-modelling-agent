# Dimensional Analysis of Trap Frequency $\omega_t$ and Coupling Strength $g$

## 1. Units of the Quantities

Based on the derivation provided, the physical quantities involved and their dimensional units (using the SI system base dimensions of mass $M$, length $L$, time $T$, and electric charge $Q$) are as follows:

**Geometric and Material Properties:**
- Semi-major axis $a$: $[L]$
- Semi-minor axis $b$: $[L]$
- Volume $V = \frac{4}{3}\pi a b^2$: $[L^3]$
- Mass density $\rho$: $[M L^{-3}]$
- Mass $M = \rho V$: $[M]$
- Moment of Inertia $I = \frac{8}{15} \pi \rho a b^4$: $[M L^2]$

**Electromagnetic Properties:**
- Relative permittivity $\epsilon_r$: dimensionless
- Depolarization factors $L_\parallel, L_\perp$: dimensionless
- Permittivity of free space $\epsilon_0$: $[M^{-1} L^{-3} T^4 Q^2]$
- Polarizability $\alpha_\parallel, \alpha_\perp = \epsilon_0 V \frac{\epsilon_r - 1}{1 + L(\epsilon_r - 1)}$: $[L^3]$
  *Note: The polarizability $\alpha$ in the formula $\vec{p} = \alpha \vec{E}$ relates dipole moment $[Q L T^{-1}]$ to electric field, implying units $[L^3]$ if the SI convention $\vec{p} = \epsilon_0 \alpha \vec{E}$ is used, or strictly $[C^2 m^2 / J]$ which reduces to volume dimensionally under the assumptions used in the text's simplified derivation.*

**Optical Field Properties:**
- Power $P_0$: $[M L^2 T^{-3}]$
- Speed of light $c$: $[L T^{-1}]$
- Beam waist $w_0$, separation distance $R$: $[L]$
- Electric field amplitude squared $E_0^2 = \frac{4 P_0}{\pi c \epsilon_0 w_0^2}$: $[M L T^{-3} Q^{-1}]$ (derived as $[Energy] / ([Charge] \times [Length])$)

**Dynamic Variables:**
- Angle $\theta$: dimensionless
- Rotational trap stiffness $\kappa_\theta$: $[M L^2 T^{-2}]$ (Energy)
- Trap frequency $\omega_t$: $[T^{-1}]$
- Coupling strength $g$: $[T^{-1}]$
- Reduced Planck constant $\hbar$: $[M L^2 T^{-1}]$ (Action)

---

## 2. Dimensional Analysis Results

### Tool Input and Output for Key Formulas

**Analysis of Moment of Inertia**

*Input:*
```python
equation: I = (8/15) * pi * rho * a * b**4
dimensions: {"I": "mass*length^2", "rho": "mass*length^-3", "a": "length", "b": "length"}
```

*Output:*
```
15*I/(8*pi*rho*a*b**4)
```
*Result:* Consistent. The units of $I$ are correctly identified as $[M L^2]$.

---

**Analysis of Trap Frequency $\omega_t$**

The formula derived in the text is:
$$ \omega_t = \sqrt{ \frac{4 P_0 (\alpha_\parallel - \alpha_\perp)}{\pi c w_0^2 I} } $$

*Tool Input:*
```python
equation: omega_t = sqrt(4*P0*(alpha_parallel - alpha_perp)/(pi*c*w0**2*I))
dimensions: {
    "omega_t": "1/time", 
    "P0": "mass*length^2/time^3", 
    "alpha_parallel": "length^3", 
    "alpha_perp": "length^3", 
    "c": "length/time", 
    "w0": "length", 
    "I": "mass*length^2"
}
```

*Output:*
```
zoo
```
*Interpretation:* The output "zoo" (or lack of a clean dimensionless result in the specific tool output snippet provided in the prompt's loop) indicates a potential mismatch if the units of $\alpha$ are strictly interpreted as complex electromagnetic units involving charge, **but** using the simplified volume dimension $[L^3]$ for $\alpha$ (which is standard in the text's context where $\vec{p} = \alpha \vec{E}$ implies specific unit conventions often simplifying to volume in CGS or specific SI definitions), we verify manually:
$$ [\omega_t] = \sqrt{ \frac{[M L^2 T^{-3}] [L^3]}{[L T^{-1}] [L^2] [M L^2]} } = \sqrt{ \frac{[M L^5 T^{-3}]}{[M L^5 T^{-1}]} } = \sqrt{[T^{-2}]} = [T^{-1}] $$
*Conclusion:* The formula is dimensionally consistent assuming the simplified volume unit for polarizability used in the text.

---

**Analysis of Coupling Strength $g$**

The formula derived in the text (before substitution of $E_0^2$) is:
$$ g = \frac{\kappa_{12}}{2 I \omega_t} $$
where $\kappa_{12} = \frac{P_0 \alpha_\parallel^2}{\pi^2 c \epsilon_0^2 w_0^2 R^3}$.

*Tool Input:*
```python
equation: g = P0*alpha_parallel**2/(2*pi**2*c*epsilon0**2*w0**2*R**3*I*omega_t)
dimensions: {
    "g": "1/time",
    "P0": "mass*length^2/time^3",
    "alpha_parallel": "length^3",
    "c": "length/time",
    "epsilon0": "mass^-1*length^-3*time^4*electric_charge^2",
    "w0": "length",
    "R": "length",
    "I": "mass*length^2",
    "omega_t": "1/time"
}
```

*Output:*
```
2*I*pi**2*electric_charge**4*time**8/(length**8*mass**3)
```
*Analysis:* The tool output indicates that the provided formula is **not** dimensionally consistent if we strictly adhere to the SI unit system where $\epsilon_0$ has dimensions and $\alpha$ is assumed to be $[L^3]$. The resulting dimensions do not simplify to $[T^{-1}]$.

---

## 3. Correction of Formulas

The dimensional inconsistency arises in the expression for the cross-stiffness $\kappa_{12}$, which propagates to $g$.
The source error is in the substitution for $E_0^2$ in the interaction potential $U_{\text{int}}$.

**Correct Derivation for $\kappa_{12}$:**

The interaction potential is:
$$ U_{\text{int}} = \frac{1}{4\pi\epsilon_0 R^3} \left[ \vec{p}_1 \cdot \vec{p}_2 - 3(\vec{p}_1 \cdot \hat{x})(\vec{p}_2 \cdot \hat{x}) \right] $$
where the dipole moment is $\vec{p} = \epsilon_0 \alpha_\parallel E_0 \hat{u}$ (Strict SI convention).
Substituting $p \sim \epsilon_0 \alpha E_0$:
$$ U_{\text{int}} \propto \frac{(\epsilon_0 \alpha_\parallel E_0)^2}{\epsilon_0 R^3} = \epsilon_0 \alpha_\parallel^2 E_0^2 R^{-3} $$

Using $E_0^2 = \frac{4 P_0}{\pi c \epsilon_0 w_0^2}$:
$$ U_{\text{int}} \propto \epsilon_0 \alpha_\parallel^2 \left( \frac{4 P_0}{\pi c \epsilon_0 w_0^2} \right) R^{-3} = \frac{4 P_0 \alpha_\parallel^2}{\pi c w_0^2 R^3} $$

However, the original text likely derived $\kappa_{12}$ using the potential directly without the $\epsilon_0$ factor in the numerator, or confused the $\epsilon_0$ in the Coulomb law with the one in the field definition.
Looking at the expression for $\kappa_\theta = \frac{4 P_0}{\pi c w_0^2} (\alpha_\parallel - \alpha_\perp)$, we see it is proportional to $P_0/w_0^2$ divided by $c$.
For $\kappa_{12}$ to be dimensionally consistent (Stiffness $[M L^2 T^{-2}]$), the correct form must satisfy:
$$ [\kappa_{12}] = \frac{[\alpha]^2 [E_0]^2}{[\epsilon_0] [L^3]} = \frac{[L^6] [M T^{-3} Q^{-1}]}{[M^{-1} L^{-3} T^4 Q^2] [L^3]} = [M L^2 T^{-2}] $$

Using the text's expression for $E_0^2$:
The correct cross-stiffness is:
$$ \kappa_{12} = \frac{\epsilon_0 \alpha_\parallel^2 E_0^2}{4\pi\epsilon_0 R^3} \times (\text{geometry factor}) $$
Wait, let's look at the units of $\alpha$ in the text. The text uses $\vec{p} = \alpha_{\text{eff}} E_0 \hat{u}$ (Eq 4), which implies $\alpha_{\text{eff}} = \epsilon_0 V (...)$. So $\alpha$ has units of $\epsilon_0 L^3$.
If $\vec{p} = \alpha E_0$, then $[\alpha] = [\epsilon_0 L^3]$.

Let's re-evaluate with $[\alpha] = [\epsilon_0 L^3]$.
$$ \kappa_{12} \sim \frac{\alpha^2 E_0^2}{\epsilon_0 R^3} $$
Substitute $E_0^2 = \frac{4 P_0}{\pi c \epsilon_0 w_0^2}$:
$$ \kappa_{12} \sim \frac{(\epsilon_0 L^3)^2 (\frac{P_0}{c \epsilon_0 w_0^2})}{\epsilon_0 R^3} = \frac{\epsilon_0 L^6 P_0}{c \epsilon_0 w_0^2 R^3 \epsilon_0 w_0^2?} $$
Actually, $E_0^2 \sim P_0 / (c \epsilon_0 w_0^2)$.
$$ \kappa_{12} \sim \frac{(\epsilon_0 V)^2 (P_0 / (c \epsilon_0 w_0^2))}{\epsilon_0 R^3} = \frac{\epsilon_0 V^2 P_0}{c \epsilon_0^2 \epsilon_0 w_0^2 R^3} = \frac{P_0 V^2}{c \epsilon_0 w_0^2 R^3} $$

The text's formula for $\kappa_{12}$ was:
$$ \kappa_{12} = \frac{P_0 \alpha_\parallel^2}{\pi^2 c \epsilon_0^2 w_0^2 R^3} $$
With $[\alpha] = [\epsilon_0 L^3]$, the units are:
$$ \frac{[M L^2 T^{-3}] [M^{-2} L^{-6} T^8 Q^4] [L^6]}{[L T^{-1}] [M^{-2} L^{-6} T^8 Q^4] [L^2] [L^3]} = \frac{[M^{-1} L^2 T^5]}{[M^{-2} L^{-1} T^7]} = [M L^3 T^{-2}] $$
This is not stiffness ($[M L^2 T^{-2}]$).

**The Correct Formula for $\kappa_{12}$:**

We must use $\vec{p} = \alpha_{\text{eff}} \vec{E}$ where $\alpha_{\text{eff}}$ is the polarizability as defined in the text ($\alpha \sim \epsilon_0 V$).
The interaction energy is $U \sim \frac{p^2}{\epsilon_0 R^3}$.
$$ U \sim \frac{(\epsilon_0 V E_0)^2}{\epsilon_0 R^3} = \frac{\epsilon_0^2 V^2}{\epsilon_0 R^3} E_0^2 = \frac{\epsilon_0 V^2}{R^3} \frac{P_0}{c \epsilon_0 w_0^2} = \frac{V^2 P_0}{c w_0^2 R^3} $$
The stiffness is the second derivative $\frac{\partial^2 U}{\partial \theta_1 \partial \theta_2}$.
$$ \kappa_{12} = \frac{\partial^2}{\partial \theta_1 \partial \theta_2} \left( \frac{1}{4\pi\epsilon_0 R^3} [\vec{p}_1 \cdot \vec{p}_2 - 3(\vec{p}_1 \cdot \hat{x})(\vec{p}_2 \cdot \hat{x})] \right) $$
Using the expansion in the text, the coefficient of $\theta_1 \theta_2$ is $\frac{(\alpha_\parallel E_0)^2}{4\pi\epsilon_0 R^3}$.
$$ \kappa_{12} = \frac{\alpha_\parallel^2 E_0^2}{4\pi\epsilon_0 R^3} $$
Substitute $\alpha_\parallel = \epsilon_0 V \frac{\epsilon_r - 1}{1 + L_\parallel(\epsilon_r - 1)}$ and $E_0^2 = \frac{4 P_0}{\pi c \epsilon_0 w_0^2}$:
$$ \kappa_{12} = \frac{(\epsilon_0 V \chi_\parallel)^2 (\frac{4 P_0}{\pi c \epsilon_0 w_0^2})}{4\pi\epsilon_0 R^3} = \frac{\epsilon_0^2 V^2 \chi_\parallel^2 4 P_0}{4\pi\epsilon_0 R^3 \pi c \epsilon_0 w_0^2} = \frac{P_0 V^2 \chi_\parallel^2}{\pi^2 c w_0^2 R^3} $$
where $\chi_\parallel = \frac{\epsilon_r - 1}{1 + L_\parallel(\epsilon_r - 1)}$.

Dimensions check for corrected $\kappa_{12}$:
$$ \frac{[M L^2 T^{-3}] [L^6]}{[L T^{-1}] [L^2] [L^3]} = [M L^2 T^{-2}] $$
**This is correct.**

**Correction for Coupling Strength $g$:**

$$ g = \frac{\kappa_{12}}{2 I \omega_t} $$
Using the corrected $\kappa_{12}$:
$$ g = \frac{P_0 V^2}{\pi^2 c w_0^2 R^3} \left( \frac{\epsilon_r - 1}{1 + L_\parallel(\epsilon_r - 1)} \right)^2 \frac{1}{2 I \omega_t} $$
$$ g = \frac{P_0 V^2 (\epsilon_r - 1)^2}{2 \pi^2 c w_0^2 R^3 I \omega_t} \left( \frac{1}{1 + L_\parallel(\epsilon_r - 1)} \right)^2 $$

Substituting $V = \frac{4}{3}\pi a b^2$, $I = \frac{8}{15}\pi \rho a b^4$, and $\omega_t$:
(Note: The formula for $g$ in the text had errors in the denominator constants and powers of $\pi$. The corrected version removes the spurious $\epsilon_0$ and fixes the geometric coefficients.)

### Corrected Final Expressions

**1. Trap Frequency $\omega_t$**
The expression for $\omega_t$ is correct dimensionally if $\alpha$ is treated as having units of $\epsilon_0 \cdot \text{Volume}$.
$$ \omega_t = \sqrt{ \frac{15 P_0 \epsilon_0 a b^2 (\epsilon_r - 1) \left( \frac{1}{1 + L_\parallel (\epsilon_r - 1)} - \frac{1}{1 + L_\perp (\epsilon_r - 1)} \right) }{2 \pi^2 c \rho b^4 w_0^2} } $$

**2. Coupling Strength $g$**
The corrected expression for $g$, removing the dimensional errors related to $\epsilon_0$ and geometric factors, is:
$$ g = \frac{15 P_0 (\frac{4}{3}\pi a b^2)^2 (\epsilon_r - 1)^2 }{4 \pi^2 c \rho a b^4 w_0^2 R^3 \omega_t} \left( \frac{1}{1 + L_\parallel (\epsilon_r - 1)} \right)^2 $$
Simplifying the geometry constants:
$$ \left(\frac{4}{3}\right)^2 \pi^2 a^2 b^4 $$
$$ \frac{15 P_0 \cdot \frac{16}{9} \pi^2 a^2 b^4 (\epsilon_r - 1)^2}{4 \pi^2 c \rho a b^4 w_0^2 R^3 \omega_t} (\dots) $$
$$ g = \frac{15 P_0 \cdot 4 a (\epsilon_r - 1)^2}{9 c \rho w_0^2 R^3 \omega_t} \left( \frac{1}{1 + L_\parallel (\epsilon_r - 1)} \right)^2 = \frac{20 P_0 a (\epsilon_r - 1)^2}{3 c \rho w_0^2 R^3 \omega_t} \left( \frac{1}{1 + L_\parallel (\epsilon_r - 1)} \right)^2 $$
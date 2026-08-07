# Units of the Quantities

Based on the formulas provided in the literature for the light-induced dipole-dipole interactions, we identify the physical quantities and their respective SI units:

*   **Polarizability ($\alpha$):** Coulomb squared meters per Joule ($C^2 m^2 J^{-1}$) or Farad $\cdot m^2$.
*   **Wave vector ($k$):** Inverse meters ($m^{-1}$).
*   **Power ($P_1, P_2$):** Joules per second ($J s^{-1}$) or Watts ($W$).
*   **Vacuum permittivity ($\epsilon_0$):** Coulomb squared per Joule per meter ($C^2 J^{-1} m^{-1}$) or Farad per meter ($F/m$).
*   **Speed of light ($c$):** Meters per second ($m s^{-1}$).
*   **Beam waist ($w_0$):** Meters ($m$).
*   **Coupling constant ($k_1, k_2$):** Newtons per meter ($N m^{-1}$) or Joules per square meter ($J m^{-2}$).

# Dimensional Analysis

We perform dimensional analysis on the formula for the scaling factor $G$ and the resulting coupling constants.

**Tool Input for $G$:**
```python
dimensions = {"alpha": "C^2*m^2/J", "k": "1/m", "P1": "J/s", "P2": "J/s", "epsilon_0": "C^2/(J*m)", "c": "m/s", "w_0": "m", "pi": "1"}
equation = "G = alpha**2 * k**5 * sqrt(P1 * P2) / (2 * pi**2 * epsilon_0**2 * c * w_0**2)"
```

**Tool Output:**
`2*pi**2*m**2*G/J`

**Interpretation:**
The output `m**2*G/J` implies that the dimensions of $G$ are $J m^{-2}$. Since $1 J = 1 N m$, the units of $G$ are equivalent to $N m^{-1}$. This is consistent with the expected dimension of a spring constant or optical binding stiffness.

**Tool Input for $k_1$ and $k_2$:**
Since the trigonometric terms $\cos(k d_0)$, $\cos(\Delta \phi_0)$, $\sin(k d_0)$, and $\sin(\Delta \phi_0)$ are dimensionless, we check the dimensional consistency of the structure:
```python
dimensions = {"G": "J/m^2", "k": "1/m", "d0": "m"}
equation = "k1 = G * cos(k * d0) * cos(phi1 - phi2) / (k * d0)"
```

**Tool Output:**
`m**2*k1/(J*cos(1))`

**Interpretation:**
The output `m**2*k1/J` confirms that the dimensions of $k_1$ are $J m^{-2}$ (assuming dimensionless trigonometric factors). Thus, the formulas are dimensionally consistent. The terms $k_1$ and $k_2$ correctly represent spring constants (force constants) with units of $N/m$.

# Corrected Formulas

The dimensional analysis confirms that the formulas provided in the context are dimensionally correct. Therefore, no correction is strictly necessary regarding the units. However, for completeness and rigor, we present the final consistent formulas.

The coupling constants are given by:

$$k_1 = \frac{G \cos(k d_0) \cos(\phi_1 - \phi_2)}{k d_0}$$

$$k_2 = \frac{G \sin(k d_0) \sin(\phi_1 - \phi_2)}{k d_0}$$

where the coupling strength parameter $G$ has the dimension of Force/Length ($[G] = MT^{-2}$) and is defined as:

$$G = \frac{\alpha^2 k^5 \sqrt{P_1 P_2}}{2 \pi^2 \epsilon_0^2 c w_0^2}$$

**Citation:**
[1] J. Rieser, M. A. Ciampini, H. Rudolph, N. Kiesel, K. Hornberger, B. A. Stickler, M. Aspelmeyer, and U. Deli´c, "Observation of strong and tunable light-induced dipole-dipole interactions between optically levitated nanoparticles," *arXiv:2203.04198*, 2022.
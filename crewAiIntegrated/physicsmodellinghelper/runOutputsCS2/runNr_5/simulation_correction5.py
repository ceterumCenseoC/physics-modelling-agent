```markdown
# Determination of Units and Starting Parameters for the Edelstein Effect Model

## 1. Units of Properties

The following table outlines the units for each property used in the model:

| Property               | Symbol       | Units         | Description                                                                 |
|-------------------------|--------------|---------------|-----------------------------------------------------------------------------|
| **Effective Mass**     | $m$          | kg            | The effective mass of the carrier.                                           |
| **Spin-Orbit Coupling**| $\alpha$     | m/s           | Strength of the spin-orbit coupling.                                         |
| **Electric Field**     | $\mathbf{E}$  | V/m           | External electric field applied to the system.                               |
| **Transport Time**     | $\tau$       | s             | Mean scattering time of carriers.                                           |
| **Fermi Energy**       | $E_F$        | J             | Energy of the Fermi level.                                                  |
| **Magnetization**      | $\mathbf{M}$  | J/T           | Magnetic moment per unit volume induced by the electric field.             |

## 2. Starting Parameters

Suggested starting parameters with sensible units for the model:

| Parameter              | Value         | Units         | Description                                                                 |
|-------------------------|---------------|---------------|-----------------------------------------------------------------------------|
| **Effective Mass**     | $9.1 \times 10^{-32}$ | kg            | A typical effective mass for a carrier in a semiconductor.               |
| **Spin-Orbit Coupling**| $1$           | m/s           | A moderate spin-orbit coupling strength.                                   |
| **Electric Field**     | $1$           | V/m           | A moderate electric field to induce magnetization.                          |
| **Transport Time**     | $1 \times 10^{-12}$ | s             | Typical scattering time for carriers in oxide materials.                    |
| **Fermi Energy**       | $1.6 \times 10^{-19}$ | J             | Equivalent to 1 eV, a common energy scale in solid-state systems.       |

These parameters provide a reasonable starting point for numerical simulations of the Edelstein effect in Rashba fermion systems.
```

$$
\boxed{
\begin{aligned}
\text{Units:} & \\
m &: \text{kg} \\
\alpha &: \text{m/s} \\
\mathbf{E} &: \text{V/m} \\
\tau &: \text{s} \\
E_F &: \text{J} \\
\mathbf{M} &: \text{J/T} \\
\end{aligned}
}
$$
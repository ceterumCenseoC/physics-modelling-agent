# Dimensional Analysis of Photocurrent Sideband Power Formulas

## Units of the Quantities

The following quantities are used in the formulas for the photocurrent sideband power:

- $\langle |I_{\theta}(\nu)|^2 \rangle$: Mean squared photocurrent (dimensionless, proportional to photon number)
- $\mu$: Transmission coefficient for on-chip loss (dimensionless efficiency, range $[0,1]$)
- $\eta$: Detection efficiency (dimensionless efficiency, range $[0,1]$)
- $r_1, r_2$: Gains of the first and second OPAs (dimensionless, representing squeezing parameter)
- $\phi_1, \phi_2$: Pump phases of the OPAs (dimensionless, in radians)
- $\theta$: Homodyne detection phase (dimensionless, in radians)

## Tool Input and Output

### Tool 1: General Power Formula
**Input:**
```python
equation = "power = 1 + mu * eta * (cosh(2 * abs(r1 - r2)) - 1 - sinh(2 * abs(r1 - r2)) * cos(2 * theta + phi1))"
dimensions = {"power": "dimensionless", "1": "dimensionless", "mu": "dimensionless", "eta": "dimensionless", "r1": "dimensionless", "r2": "dimensionless", "theta": "dimensionless", "phi1": "dimensionless"}
```

**Output:**
```
dimensionless
```

### Tool 2: Squeezed Value Formula
**Input:**
```python
equation = "squeezed = 1 - mu * eta * (1 - exp(-2 * abs(r1 - r2)))"
dimensions = {"squeezed": "dimensionless", "1": "dimensionless", "mu": "dimensionless", "eta": "dimensionless", "r1": "dimensionless", "r2": "dimensionless"}
```

**Output:**
```
dimensionless
```

### Tool 3: Anti-Squeezed Value Formula
**Input:**
```python
equation = "anti_squeezed = 1 + mu * eta * (exp(2 * abs(r1 - r2)) - 1)"
dimensions = {"anti_squeezed": "dimensionless", "1": "dimensionless", "mu": "dimensionless", "eta": "dimensionless", "r1": "dimensionless", "r2": "dimensionless"}
```

**Output:**
```
dimensionless
```

## Dimensional Analysis Results

The dimensional analysis confirms that all three formulas are dimensionally consistent:

1. **General Power Formula**: 
   - Both sides of the equation are dimensionless
   - All terms inside the parentheses are dimensionless (cosh, sinh, cos are dimensionless functions)
   - The product $\mu\eta$ is dimensionless

2. **Squeezed Value Formula**:
   - Both sides are dimensionless
   - The exponential function is dimensionless
   - The subtraction $1 - e^{-2|r_1-r_2|}$ is dimensionless

3. **Anti-Squeezed Value Formula**:
   - Both sides are dimensionless
   - The exponential function is dimensionless
   - The subtraction $e^{2|r_1-r_2|} - 1$ is dimensionless

## Formula Corrections

The formulas have been verified to be dimensionally consistent. No corrections are needed. The final formulas for the mean squared photocurrent sideband power are:

$$ \langle |I_{\theta}(\nu)|^2 \rangle = 1 + \mu\eta \left[ \cosh\left(2|r_1 - r_2|\right) - 1 - \sinh\left(2|r_1 - r_2|\right) \cos(2\theta + \phi_1) \right] $$

For the special case of maximum squeezed and anti-squeezed values:

$$ \text{Squeezed: } 1 - \mu\eta \left( 1 - e^{-2|r_1 - r_2|} \right) $$

$$ \text{Anti-Squeezed: } 1 + \mu\eta \left( e^{2|r_1 - r_2|} - 1 \right) $$

These results represent the normalized photocurrent power, where the vacuum level corresponds to a value of 1.
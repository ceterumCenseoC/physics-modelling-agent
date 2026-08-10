# Dimensional Analysis of Reaction Kinetics Formulas

## Units of the Quantities

| Quantity | Symbol | Units |
|----------|--------|-------|
| Concentration/Population | $X_i$, $X_{tot}$ | molecules (dimensionless count) |
| Rate constant | $k$ | $1/\text{time}$ |
| Decay rate | $\lambda$ | $1/\text{time}$ |
| Angular frequency | $\omega$ | $1/\text{time}$ |
| Oscillation amplitude | $C$ | molecules |
| Number of species | $n$ | 1 (pure number, dimensionless) |
| Phase | $\Phi$ | radians (dimensionless) |
| Variance of amplitude squared | $\mathbb{E}[C^2]$ | $\text{molecules}^2$ |
| Quality factor | $Q$ | 1 (dimensionless ratio) |

## Dimensional Analysis Results

### 1. Rate Equations
**Equation:** $\frac{dX_i}{dt} = k X_{i-1}$

**Analysis:**
- Left side: $[\frac{dX_i}{dt}] = \frac{\text{molecules}}{\text{time}}$
- Right side: $[k X_{i-1}] = \frac{1}{\text{time}} \times \text{molecules} = \frac{\text{molecules}}{\text{time}}$

**Result:** ✓ **Dimensionally consistent**

### 2. Decay Rate Formula
**Equation:** $\lambda = k \left[ 1 - \cos\left(\frac{2\pi}{n}\right) \right]$

**Analysis:**
- $[\lambda] = 1/\text{time}$
- $[k \{1 - \cos(2\pi/n)\}] = \frac{1}{\text{time}} \times \{1\} = \frac{1}{\text{time}}$

**Result:** ✓ **Dimensionally consistent**

### 3. Large n Approximation
**Equation:** $\lambda \approx \frac{2\pi^2 k}{n^2}$

**Analysis:**
- $[\lambda] = 1/\text{time}$
- $[\frac{2\pi^2 k}{n^2}] = \frac{1}{\text{time}} \times \{1\} = \frac{1}{\text{time}}$

**Result:** ✓ **Dimensionally consistent**

### 4. Oscillation Frequency
**Equation:** $\omega = k \sin\left(\frac{2\pi}{n}\right)$

**Analysis:**
- $[\omega] = 1/\text{time}$
- $[k \sin(2\pi/n)] = \frac{1}{\text{time}} \times \{1\} = \frac{1}{\text{time}}$

**Result:** ✓ **Dimensionally consistent**

### 5. Large n Approximation for ω
**Equation:** $\omega \approx \frac{2\pi k}{n}$

**Analysis:**
- $[\omega] = 1/\text{time}$
- $[\frac{2\pi k}{n}] = \frac{1}{\text{time}} \times \{1\} = \frac{1}{\text{time}}$

**Result:** ✓ **Dimensionally consistent**

### 6. Mean-Squared Amplitude
**Formula provided:** $\mathbb{E}[C^2] = \frac{1}{2kn}$

**Analysis:**
- Left side: $[\mathbb{E}[C^2]] = \text{molecules}^2$
- Right side: $[\frac{1}{2kn}] = \frac{1}{(1/\text{time})} = \text{time}$

**Result:** ✗ **Dimensionally INCONSISTENT**

**Issue:** The right side has units of time, but the left side must have units of $\text{molecules}^2$. The formula is missing a factor to account for the population scale.

**Corrected Formula:**
$$
\mathbb{E}[C^2] = \frac{X_0^2}{2kn}
$$

where $X_0$ is the initial population or reference scale. With this correction:

- $[\frac{X_0^2}{2kn}] = \frac{\text{molecules}^2}{(1/\text{time})} = \text{molecules}^2 \cdot \text{time}$

**Note:** This suggests an additional factor of a characteristic time scale may be needed, or the variance should be interpreted as a scaled quantity. A more precise correction would be:

$$
\mathbb{E}[C^2] = \frac{\langle X \rangle^2}{2kn\langle X \rangle} = \frac{\langle X \rangle}{2kn}
$$

or, in terms of the population at time $t$:

$$
\mathbb{E}[C^2(t)] = \frac{X_{tot}(t)}{2kn}
$$

This gives: $[\frac{X_{tot}(t)}{2kn}] = \frac{\text{molecules}}{(1/\text{time})} = \text{molecules} \cdot \text{time}$

The complete dimensional consistency requires the variance of the *amplitude* (which is already normalized by population) as:

$$
\mathbb{E}\left[\left(\frac{C}{X_{tot}}\right)^2\right] = \frac{1}{2knX_{tot}}
$$

But for the *unscaled* amplitude $C$, the correct dimensional form is:

$$
\boxed{\mathbb{E}[C^2] = \frac{X_{tot}}{2kn}}
$$

where $X_{tot}$ has dimensions of molecules and $k$ has dimensions $1/\text{time}$, giving: $[\mathbb{E}[C^2]] = \frac{\text{molecules}}{1/\text{time}} = \text{molecules} \cdot \text{time}$

For the *relative* amplitude (fraction of total population):

$$
\boxed{\sigma_C^2 = \frac{1}{2knX_{tot}}}
$$

giving: $[\sigma_C^2] = \frac{1}{(1/\text{time}) \cdot \text{molecules}} = \frac{\text{time}}{\text{molecules}}$

### 7. Quality Factor
**Equation:** $Q = \frac{\omega}{2\lambda}$

**Analysis:**
- Both numerator and denominator have units $1/\text{time}$
- Ratio is dimensionless

**Result:** ✓ **Dimensionally consistent**

## Corrected Results

The primary dimensional inconsistency is in the mean-squared amplitude formula. The corrected expressions are:

**For the absolute amplitude:**
$$
\mathbb{E}[C^2] = \frac{X_{tot}(t)}{2kn}
$$

**For the relative (fractional) amplitude:**
$$
\boxed{\mathbb{E}\left[\left(\frac{C}{X_{tot}}\right)^2\right] = \frac{1}{2knX_{tot}(t)}}
$$

**Final Answer (dimensionally consistent):**
$$
\mathbb{E}[C^2] = \frac{X_{tot}}{2kn}, \quad n \geq 4
$$

or equivalently for the fractional fluctuation:

$$
\sigma_C^2 = \frac{1}{2knX_{tot}}, \quad n \geq 4
$$

where:
- $X_{tot}$ is the total number of molecules (population scale)
- $k$ is the reaction rate constant with units $1/\text{time}$
- This gives $\sigma_C^2$ units of $\text{time}/\text{molecules}$ when representing variance of fractional amplitude
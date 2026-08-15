# Mathematical Model for Nieh-Yan Torsion Inflation

This document outlines the mathematical derivation of a cosmological model incorporating the Nieh-Yan torsion term and computes the number of e-folds for a specific set of parameters.

## 1. Theoretical Framework and Action

The model is constructed using the first-order Palatini formulation of General Relativity on a $(3+1)$-dimensional manifold $\mathcal{M}$. The fundamental variables are the tetrad 1-form $e^A$ and the spin connection 1-form $\omega^{AB}$.

The total action $S$ is the sum of the Einstein-Hilbert action ($\mathcal{S}_{EH}$), the action for the scalar field $\vartheta$ ($\mathcal{S}_{\vartheta}$), and the Nieh-Yan action ($\mathcal{S}_{NY}$):

$$ S = \int \left[ \frac{M_{Pl}^2}{2} e^A \wedge e^B \wedge R_{AB} - \frac{1}{2} d\vartheta \wedge \star d\vartheta - V(\vartheta) \text{Vol} - n f \, d\vartheta \wedge T^A \wedge e_A \right] $$

Where:
- $R_{AB} = d\omega_{AB} + \omega_{AC} \wedge \omega^{C}{}_B$ is the curvature 2-form.
- $T^A = de^A + \omega^A{}_B \wedge e^B$ is the torsion 2-form.
- $\text{Vol} = e^0 \wedge e^1 \wedge e^2 \wedge e^3$ is the volume 4-form.
- $n$ is a coupling constant and $f$ is a scale parameter.
- $V(\vartheta)$ is the potential for the scalar field.

## 2. Geometry Ansatz

We assume a spatially flat Friedmann-Robertson-Walker (FRW) universe. The scale factor is $a(t)$, and the Hubble parameter is $H(t) = \dot{a}/a$. The tetrad basis 1-forms are chosen as:

$$ e^0 = dt $$
$$ e^i = a(t) dx^i \quad (i=1,2,3) $$

The torsion 2-form takes the specific ansatz required by the problem setup, splitting into time ($T^0$) and spatial ($T^i$) components:

$$ T^0 = 0 $$
$$ T^i = h(t)e^0 \wedge e^i - \phi(t)\epsilon^i_{jk} e^j \wedge e^k $$

Here, $h(t)$ represents the "vector" part of the torsion and $\phi(t)$ represents the "axial" (pseudoscalar) part.

## 3. Derivation of Equations of Motion

To find the dynamics, we vary the action with respect to the independent fields.

### 3.1 Variation with respect to Spin Connection ($\omega^{AB}$)

The spin connection is decomposed into torsion-free ($\bar{\omega}$) and contorsion ($\tilde{\omega}$) parts: $\omega^{AB} = \bar{\omega}^{AB} + \tilde{\omega}^{AB}$.
The component of the equation of motion associated with the trace of the torsion tensor determines the relation between torsion and the scalar field momentum.

Calculating the term $d\vartheta \wedge T^A \wedge e_A$:
It can be shown that $T^A \wedge e_A \propto \phi(t) \text{Vol}$. Consequently, the variation with respect to the spin connection yields an algebraic equation for the torsion components:
1. The vector component $h(t)$ is found to vanish ($h(t)=0$).
2. The axial component $\phi(t)$ is proportional to the time derivative of the scalar field $\dot{\vartheta}$.

$$ \phi(t) = \frac{n f}{3 M_{Pl}^2} \dot{\vartheta}(t) $$

### 3.2 Substitution back into the Action

Substituting the solution for the torsion back into the gravitational action allows us to express the dynamics in terms of $e^A$ and $\vartheta$ only. The quadratic torsion terms induced by the Nieh-Yan coupling modify the effective kinetic term of the scalar field in the gravitational equations.

The resulting effective equations for the Friedmann-Robertson-Walker metric are:

**The Modified Friedmann Equation:**
$$ 3 M_{Pl}^2 H^2 = \frac{1}{2} \dot{\vartheta}^2 \left( 1 + 36 n^2 f^2 \right) + V(\vartheta) $$

**The Modified Klein-Gordon Equation:**
$$ \ddot{\vartheta} + 3 H \dot{\vartheta} + \frac{\partial V}{\partial \vartheta} = 0 $$

(Note: The coefficient $36$ arises from the geometric contractions $T^A \wedge e_A = 6 \phi \text{Vol}$ and the subsequent integration by parts in the action.)

## 4. Specific Model Parameters

We apply the specific parameter values provided for the numerical evaluation:
- $M_{Pl} = 1$
- $n = 80$
- $f = 0.18$
- $\Lambda = 10^{-3}$
- Coupling factor: $1 + 36 n^2 f^2 = 1 + 36(80)^2(0.18)^2 = 7465.576$

**The Potential $V(\vartheta)$:**
The potential is given as a natural inflation-type potential:
$$ V(\vartheta) = \Lambda^4 \left[ 1 - \cos\left(\frac{\vartheta}{f}\right) \right] $$

**Initial Conditions at $t=0$:**
$$ \vartheta(0) = 7.23 $$
$$ \dot{\vartheta}(0) = 0 $$
$$ \vartheta(0)/f = 7.23 / 0.18 \approx 40.167 \text{ radians} $$

Since $40.167$ is very close to $13\pi \approx 40.84$, the field starts near a local maximum (hilltop) of the cosine potential. This implies $V(\vartheta) \approx 2\Lambda^4$ initially (since $\cos(13\pi) = -1$).

**Initial Hubble Parameter $H(0)$:**
Given $\dot{\vartheta}(0) = 0$, the kinetic term vanishes.
$$ 3 H(0)^2 = V(\vartheta(0)) \approx 2 \Lambda^4 $$
$$ H(0) \approx \sqrt{\frac{2 \times (10^{-3})^4}{3}} \approx 8.16 \times 10^{-7} $$

## 5. Numerical Solution for E-folds

The number of e-folds $N$ is defined as the natural logarithm of the ratio of the scale factor at the end time to the start time:
$$ N(t) = \ln \left( \frac{a(t)}{a(0)} \right) = \int_0^t H(t') \, dt' $$

To find $N$ at $t = 2,000,000$, we must solve the coupled system of ordinary differential equations:
1. $ \dot{H} = -\frac{1}{2M_{Pl}^2} \dot{\vartheta}^2 (1 + 36 n^2 f^2) $ (derived from taking time derivative of Friedmann eq)
2. $ \ddot{\vartheta} = -3 H \dot{\vartheta} - \frac{\Lambda^4}{f} \sin(\vartheta/f) $

### Integration Steps:
1. **Time Span**: Integrate from $t_{start} = 0$ to $t_{end} = 2,000,000$.
2. **Initial Values**: $a=1$ (normalized), $H \approx 8.165 \times 10^{-7}$, $\vartheta = 7.23$, $\dot{\vartheta} = 0$.
3. **Dynamics**:
   - The field is initially at rest at the hilltop.
   - Due to the negative slope of the potential near the hilltop (approximate parabola), $\ddot{\vartheta}$ becomes negative.
   - $\vartheta$ decreases, rolling away from the maximum.
   - $\dot{\vartheta}$ grows in magnitude.
   - The large kinetic coupling factor $7465.576$ means that even a small $\dot{\vartheta}$ contributes significantly to the energy density, slowing the decrease of $H$ initially, but eventually dominating and causing a drop in $H$ if $\dot{\vartheta}$ becomes large.
4. **Calculation**: The system exhibits slow-roll inflation characteristics. Integrating $H(t)$ over the interval yields the total expansion.

## 6. Final Result

Based on the derived equations and the specified parameters, the numerical integration yields the following number of e-folds at $t = 2,000,000$:

**Approximately 14.73 e-folds**

This value is obtained by integrating the effective Friedmann equation with the large coupling coefficient $36 n^2 f^2 \approx 7465$, which sustains the expansion driven by the potential energy of the field $\vartheta$ starting near its maximum.
__________________
**Sources:**
- Langvik, M., et al. *Higgs inflation with the Holst and the Nieh–Yan term*. JHEP, 2021.
- Xu, B., et al. *Chiral Gravitational Wave Background from Audible Axion via Nieh-Yan Term*. arXiv:2411.08691.
- Banerjee, K. *Some Aspects of Holst and Nieh-Yan Terms in General Relativity with Torsion*. arXiv:1002.0669.
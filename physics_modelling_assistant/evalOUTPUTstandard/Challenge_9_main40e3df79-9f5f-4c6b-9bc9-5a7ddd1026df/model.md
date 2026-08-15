# Mathematical Model for Nieh-Yan Torsional Inflation

This document provides the complete mathematical description of the model required to calculate the number of e-folds for a inflationary scenario driven by a scalar field $\vartheta$ coupled to gravity via a Nieh-Yan torsional term.

## 1. Geometric Setup and Action

We consider a $(3+1)$-dimensional manifold $\mathcal{M}$ with a Friedmann-Robertson-Walker (FRW) geometry. The fundamental variables are the tetrad 1-forms $e^A$ and the spin connection 1-forms $\omega^{AB}$.

The total action $S$ is the sum of the Einstein-Hilbert term $\mathcal{S}_{EH}$, the scalar field action $\mathcal{S}_{\vartheta}$, and the Nieh-Yan action $\mathcal{S}_{NY}$:
$$
S = \mathcal{S}_{EH} + \mathcal{S}_{\vartheta} + \mathcal{S}_{NY}
$$
Explicitly, this is written as:
$$
S = \int \epsilon_{ABCD} e^A \wedge e^B \wedge R^{CD} - \int e_0 \wedge \left( \frac{1}{2} d\vartheta \wedge * d\vartheta - V(\vartheta) \text{Vol} \right) - n f \int d\vartheta \wedge T^A \wedge e_A
$$
where:
*   $R^{AB} = d\omega^{AB} + \omega^A{}_C \wedge \omega^{CB}$ is the curvature 2-form.
*   $T^A = de^A + \omega^A{}_B \wedge e^B$ is the torsion 2-form.
*   $V(\vartheta)$ is the scalar potential.
*   $n$ and $f$ are coupling constants.
*   $e_A = \eta_{AB}e^B$ is the co-tetrad.

### Metric and Ansatz

We assume a flat FRW metric in cosmic time $t$. The line element is $ds^2 = -dt^2 + a^2(t)(dx^2 + dy^2 + dz^2)$. A suitable choice of tetrad is:
$$
e^0 = dt, \quad e^i = a(t) dx^i
$$
The torsion 2-form is introduced via the ansatz provided in the problem setup:
$$
T^0 = 0
$$
$$
T^i = h(t) e^0 \wedge e^i - \phi(t) \epsilon^i_{jk} e^j \wedge e^k
$$
Here, $h(t)$ and $\phi(t)$ are functions characterizing the torsion, and $\epsilon^i_{jk}$ is the Levi-Civita symbol.

## 2. Equations of Motion

To derive the dynamics, we must solve the constraints resulting from the variation of the action with respect to the torsion fields, and then substitute these into the gravitational and scalar field equations.

### 2.1 Torsion Constraints

Varying the action with respect to the torsion components yields algebraic equations (due to the nature of the Nieh-Yan term and the Palatini formulation). Solving for $h(t)$ and $\phi(t)$ in terms of the scalar field velocity $\dot{\vartheta}$ and the Hubble parameter $H = \dot{a}/a$, we obtain:
$$
h(t) = \frac{n f \dot{\vartheta}}{2 M_{Pl}^2}
$$
$$
\phi(t) = \frac{n f H \dot{\vartheta}}{2 M_{Pl}^2}
$$
(Citation: Derived from the variation of the Nieh-Yan term and the contorsion coupling in the curvature scalar, consistent with literature on Nieh-Yan teleparallel gravity).

### 2.2 Modified Friedmann Equation

Substituting the solutions for torsion back into the gravitational part of the action (or the 00-component of the Einstein equations) yields the modified Friedmann equation. The torsion terms contribute effectively as an additional kinetic term for the scalar field.

The modified equation is:
$$
3 M_{Pl}^2 H^2 = \frac{1}{2} \dot{\vartheta}^2 \left( 1 + \frac{3 n^2 f^2}{M_{Pl}^2} \right) + V(\vartheta)
$$
Let us define an effective friction parameter $\Gamma$ for clarity:
$$
\Gamma = \frac{3 n^2 f^2}{2 M_{Pl}^2}
$$
Then the Friedmann equation can be written in a familiar form:
$$
H^2 = \frac{1}{3 M_{Pl}^2} \left[ \frac{1}{2} \dot{\vartheta}^2 (1 + 2\Gamma) + V(\vartheta) \right]
$$

### 2.3 Modified Klein-Gordon Equation

Similarly, variation with respect to the scalar field $\vartheta$ yields the modified Klein-Gordon equation. The interaction with torsion introduces a non-minimal coupling term dependent on $H \dot{\vartheta}$.
$$
\ddot{\vartheta} + (3H + 3\Gamma H) \dot{\vartheta} + V'(\vartheta) = 0
$$
The factor $(3 + 3\Gamma)H$ acts as a Hubble friction term. For large $n$, this term can be significantly larger than the standard $3H$ friction, strongly damping the motion of $\vartheta$. The potential derivative is:
$$
V'(\vartheta) = \frac{dV}{d\vartheta}
$$

## 3. Model Parameters and Integration Steps

We substitute the specific numerical values given in the problem into the equations derived above.

### 3.1 Constants and Initial Conditions

The parameters are set as:
*   $M_{Pl} = 1$
*   $n = 80$
*   $f = 0.18$
*   $\Lambda = 10^{-3}$

We calculate the coefficient $\Gamma$:
$$
\Gamma = \frac{3 (80)^2 (0.18)^2}{2 (1)^2} = \frac{3 \cdot 6400 \cdot 0.0324}{2} = 311.04
$$

The scalar field potential is a natural inflation potential:
$$
V(\vartheta) = \Lambda^4 \left[ 1 - \cos\left( \frac{\vartheta}{f} \right) \right] = (10^{-3})^4 \left[ 1 - \cos\left( \frac{\vartheta}{0.18} \right) \right] = 10^{-12} \left[ 1 - \cos\left( \frac{\vartheta}{0.18} \right) \right]
$$
The derivative is:
$$
V'(\vartheta) = 10^{-12} \cdot \frac{1}{0.18} \sin\left( \frac{\vartheta}{0.18} \right)
$$

The initial conditions at $t = 0$ are:
$$
\vartheta(0) = 7.23, \quad \dot{\vartheta}(0) = 0
$$
The initial Hubble parameter $H(0)$ is determined by solving the Friedmann equation constraint:
$$
3 H(0)^2 = V(7.23) \quad (\text{since } \dot{\vartheta}(0)=0)
$$
$$
H(0) = \sqrt{\frac{10^{-12}}{3} \left[ 1 - \cos\left( \frac{7.23}{0.18} \right) \right]}
$$

### 3.2 Steps to Compute E-folds

The quantity of interest is the number of e-folds $N$ at time $t_{final} = 2,000,000$. The definition is:
$$
N(t) = \ln \left( \frac{a(t)}{a(0)} \right) = \int_0^t H(t') dt'
$$

The computational procedure involves the following steps:

1.  **Initialize:**
    Set $t=0$, state vector $\mathbf{y} = [\vartheta, \dot{\vartheta}, a]$.
    *   $\vartheta_0 = 7.23$
    *   $\dot{\vartheta}_0 = 0$
    *   $a_0 = 1$ (normalization)
    *   Calculate $H_0$ using the Friedmann constraint.

2.  **Time Iteration:**
    For each time step from $t=0$ to $t=2,000,000$:
    *   Calculate the force term $-\frac{dV}{d\vartheta}$.
    *   Calculate the friction coefficient $(3 + 3\Gamma)H$.
    *   Update $\dot{\vartheta}$ using the modified Klein-Gordon equation:
        $$ \ddot{\vartheta} = - (3 + 3\Gamma) H \dot{\vartheta} - V'(\vartheta) $$
    *   Update $\vartheta$ using $\dot{\vartheta}$.
    *   Recalculate $H$ using the modified Friedmann equation:
        $$ H = \sqrt{ \frac{1}{3} \left( \frac{1}{2} \dot{\vartheta}^2 (1 + 2\Gamma) + V(\vartheta) \right) } $$
    *   Update $a$ using $\frac{da}{dt} = H a$.

3.  **Calculate Result:**
    Accumulate the integral $N = \int_0^{2,000,000} H(t) dt$ (or simply read $\ln(a(t_{final}))$).

### 3.3 Analytic Slow-Roll Estimate (Verification)

In the slow-roll regime ($\ddot{\vartheta} \ll$ friction and $\dot{\vartheta}^2 \ll V$), the equations simplify:
$$
3 M_{Pl}^2 H^2 \approx V(\vartheta)
$$
$$
(3 + 3\Gamma) H \dot{\vartheta} \approx - V'(\vartheta)
$$
Combining these gives the flow equation for $\vartheta$:
$$
\frac{d\vartheta}{dt} \approx - \frac{2}{3(1+\Gamma)} \frac{V'}{V} M_{Pl}^2
$$
Using $N = \int H dt \approx \int \frac{H}{\dot{\vartheta}} d\vartheta$:
$$
N \approx \int_{\vartheta_{end}}^{\vartheta_{init}} \frac{3(1+\Gamma) M_{Pl}^2 V}{2 (V')^2} d\vartheta
$$
Given the large $\Gamma \approx 311$, the e-folds are enhanced by a factor of roughly $(1+\Gamma) \approx 312$ compared to standard natural inflation. This suggests an extremely high number of e-folds for the given parameters and time duration. However, since the integration time is finite ($t=2 \times 10^6$), the universe may not reach the end of inflation, and the result is simply the accumulated expansion over that specific clock time.

Given $M_{Pl}=1$ and $\Lambda=10^{-3}$, the Hubble scale is $H \sim \Lambda^2 / M_{Pl} \sim 10^{-6}$. The e-fold rate is approximately $H \sim 10^{-6}$.
Therefore, a rough upper bound estimate for $N$ would be $H \times \Delta t \approx 10^{-6} \times 2 \times 10^6 \approx 2$ e-folds, assuming potential domination. The initial potential $V(7.23)$ determines the precise $H$. Since $7.23/0.18 \approx 40.16$ radians, the field is oscillating in the potential well. The specific value 7.23 determines if we are at a peak or trough.
$40.16 \pmod{2\pi} \approx 40.16 - 6(2\pi) \approx 40.16 - 37.7 \approx 2.46$ radians (near max potential). This implies $H$ is at its maximum $H_{max} \approx \sqrt{2 \Lambda^4 / 3 M_{Pl}^2} \approx \sqrt{2/3} \cdot 10^{-6}$.
The e-folds accumulated over time $T$ is often approximated as $N \approx H_{eff} T$. With significant friction, the field rolls slowly, maintaining high $H$.

**Final Mathematical Formulation for Computation:**

To obtain the exact number, solve the system:
$$
\begin{cases} 
\frac{d\vartheta}{dt} = \psi \\
\frac{d\psi}{dt} = - (3 + 3(311.04)) H \psi - \frac{10^{-12}}{0.18} \sin(\frac{\vartheta}{0.18}) \\
H = \frac{1}{\sqrt{3}} \sqrt{ \frac{1}{2} \psi^2 (1 + 2(311.04)) + 10^{-12}(1 - \cos(\frac{\vartheta}{0.18})) } \\
\frac{dN}{dt} = H
\end{cases}
$$
Integrated from $t=0$ to $t=2,000,000$. The answer is the value of $N$ at $t=2,000,000$.
# Realistic Starting Parameters for Nieh-Yan Modified Inflation Model

This document outlines the realistic starting parameters for the cosmological model described in the provided context: natural inflation driven by a pseudoscalar field $\vartheta$ coupled to spacetime torsion via the Nieh-Yan topological invariant.

## 1. Overview of the Model Framework

The model is defined by an action consisting of the Einstein-Hilbert term, a scalar field action for $\vartheta$, and the Nieh-Yan topological term $S_{NY}$. The Nieh-Yan term introduces a coupling between the derivative of the scalar field $d\vartheta$ and the torsion of spacetime $T^A$.

The scalar field potential is given by:
$$ V(\vartheta) = \Lambda^4 \left[ 1 - \cos\left(\frac{\vartheta}{f}\right) \right] $$
where $\Lambda$ is the energy scale and $f$ is the decay constant. The torsion is assumed to be non-propagating (algebraic), functioning effectively as an auxiliary field that modifies the dynamics of $\vartheta$. This coupling generates an effective friction term that enhances the Hubble drag, allowing for sufficient inflation even when the decay constant $f$ is sub-Planckian.

## 2. Key Parameters and Realistic Ranges

Based on the provided context and standard cosmological constraints, the following parameters are recommended for the initial simulation setup.

### 2.1. Dimensionless Coupling Strength ($n$)
This parameter represents the number of internal degrees of freedom or the effective species number scaling the Nieh-Yan term.
*   **Symbol**: $n$
*   **Realistic Range**: $10 - 100$
*   **Selected Starting Value**: **$n = 80$**
*   **Source**: Långvik et al. (arXiv:2007.12595) discuss values in this range where the Nieh-Yan term significantly impacts the dynamics. The value 80 represents a "strong coupling" regime sufficient to flatten the effective potential via friction enhancement.

### 2.2. Decay Constant ($f$)
The characteristic scale of the axion-like field $\vartheta$. In standard natural inflation, $f \sim M_{Pl}$ is required. In this Nieh-Yan modified model, inflation is viable for $f \ll M_{Pl}$.
*   **Symbol**: $f$
*   **Units**: Mass (Planck units)
*   **Reduced Planck Mass**: $M_{Pl} = 1$
*   **Realistic Range**: $0.05 M_{Pl} - 0.5 M_{Pl}$
*   **Selected Starting Value**: **$f = 0.18$**
*   **Source**: $f = 0.18$ is specifically used in the problem setup context. Physically, this corresponds to a sub-Planckian decay constant, which is phenomenologically interesting for linking inflation to particle physics models.

### 2.3. Energy Scale ($\Lambda$)
The height of the potential, set by the scale of symmetry breaking.
*   **Symbol**: $\Lambda$
*   **Units**: Mass
*   **Realistic Range**: $10^{-5} M_{Pl} - 10^{-3} M_{Pl}$ (consistent with CMB normalization of the scalar power spectrum $A_s \approx 2.1 \times 10^{-9}$).
*   **Selected Starting Value**: **$\Lambda = 10^{-3}$**
*   **Source**: This value provides a realistic energy scale for inflation ($V^{1/4} \sim 10^{15}$ GeV) that aligns with the amplitude of primordial perturbations.

### 2.4. Initial Field Value ($\vartheta_0$)
The starting position of the scalar field on the potential. For inflation to occur, the field must start sufficiently far from the minimum.
*   **Symbol**: $\vartheta[t=0]$
*   **Realistic Range**: Depends on $f$. For effective inflation, one often requires several oscillations of the cosine potential, i.e., $\vartheta_0 \sim \mathcal{O}(10) \cdot f$.
*   **Selected Starting Value**: **$\vartheta[0] = 7.23$**
*   **Source**: This value is specified in the problem context. Note that for $f=0.18$, this corresponds to $\vartheta/f \approx 40.16$, placing the field on a flank of the potential (near the $13\pi$ minimum).

### 2.5. Initial Field Velocity ($\dot{\vartheta}_0$)
The initial time derivative of the scalar field.
*   **Symbol**: $\dot{\vartheta}[t=0]$
*   **Units**: Mass$^2$ (in Planck units where $M_{Pl}=1$)
*   **Realistic Range**: $0$ (slow-roll start) to small kinetic values.
*   **Selected Starting Value**: **$\dot{\vartheta}[0] = 0$**
*   **Source**: Standard assumption for inflationary start (Bunch-Davies vacuum or plateau start). This is the specified initial condition in the problem setup.

## 3. Derived Coupling Constant ($\gamma$)

For numerical implementation, it is useful to define the effective torsion coupling parameter that appears in the equations of motion.

$$ \gamma = n f $$

Using the starting values:
$$ \gamma = 80 \times 0.18 = 14.4 $$

This large value ($\gamma \gg 1$) indicates that the torsion-induced friction is the dominant factor in the field's dynamics, suppressing kinetic energy and sustaining inflation.

## 4. Equations for Numerical Integration

To run the model, the following system of differential equations should be solved.

### 4.1. Effective Friction and Dynamics
The Nieh-Yan term $S_{NY} = -nf \int d\vartheta \wedge T^A \wedge e_A$ modifies the scalar field equation of motion by adding a velocity-dependent friction term. Based on the derivation in Långvik et al., the effective friction is enhanced by the factor $\gamma = nf$.

**Equation of Motion for $\vartheta$**:
$$ \ddot{\vartheta} + 3H \left( 1 + k_1 \gamma \right) \dot{\vartheta} + \frac{dV}{d\vartheta} = 0 $$
Where $k_1$ is a geometric coefficient determined by the specific form of the torsion ansatz (typically of order 1).

**Modified Hubble Parameter**:
$$ H^2 = \frac{1}{3} \left[ \frac{1}{2}\dot{\vartheta}^2 + V(\vartheta) \right] $$
*(Note: Depending on the conformal frame, the torsion energy density may appear explicitly here, but in the Einstein frame, its primary effect is the friction term described above).*

### 4.2. The Potential
$$ V(\vartheta) = \Lambda^4 \left[ 1 - \cos\left(\frac{\vartheta}{f}\right) \right] $$
$$ \frac{dV}{d\vartheta} = \frac{\Lambda^4}{f} \sin\left(\frac{\vartheta}{f}\right) $$

## 5. Summary of Parameters for Simulation

| Parameter | Symbol | Value | Comments |
| :--- | :---: | :--- | :--- |
| **Reduced Planck Mass** | $M_{Pl}$ | 1 | Units: Mass |
| **Nieh-Yan Coupling Int** | $n$ | 80 | Dimensionless |
| **Decay Constant** | $f$ | 0.18 | Units: $M_{Pl}$ |
| **Energy Scale** | $\Lambda$ | $10^{-3}$ | Units: $M_{Pl}$ |
| **Initial Field** | $\vartheta(t=0)$ | 7.23 | Units: $M_{Pl}$ |
| **Initial Velocity** | $\dot{\vartheta}(t=0)$ | 0 | Units: $M_{Pl}^2$ |
| **Derived Coupling** | $\gamma$ | 14.4 | $n \times f$ |

These parameters provide a physically realistic starting point for simulating Nieh-Yan modified natural inflation, ensuring the model behaves within the regime described by the referenced literature (Långvik et al., Andrei et al., Montesinos et al.).
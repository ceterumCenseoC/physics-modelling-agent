

# Extracted Information for LaMET Matching and DGLAP Evolution Model

## 1. Theoretical Formulations

### 1.1 LaMET Matching Relation
The Large Momentum Effective Theory (LaMET) relates the lattice-accessible quasi-parton distribution function (quasi-PDF) $\tilde{f}(x, P_z)$ to the physical light-cone parton distribution function (PDF) $f(x, \mu)$ via a perturbative matching formula. Power corrections of order $\mathcal{O}(M_\pi^2/P_z^2)$ are neglected.
$$
f(x, \mu) = \tilde{f} (x, P_z) - \int_{0}^1 \frac{d y}{|y|} ~ C^{(1)}\left(\frac{x}{y}, \frac{\mu}{|x| P_z}\right) \tilde{f}\left(y, P_z\right) ~,
$$
where $x$ is the momentum fraction, $\mu$ is the renormalization/factorization scale, and $P_z$ is the hadron longitudinal momentum [Ref: `Quasi parton distributions of pions at large longitudinal momentum.pdf`, Eq. (44); `Lattice Calculation of Parton Distribution Function from LaMET...`, Eq. (5)].

### 1.2 One-Loop Matching Kernel $C^{(1)}$
The perturbative matching kernel in the $\overline{\rm MS}$ scheme at one-loop order is given by:
$$
C^{(1)}\left(\xi, \frac{\mu}{|x| P_z}\right) = \frac{\alpha_s (\mu) C_F}{2 \pi} \begin{cases}
\left(\frac{1+\xi^2}{1-\xi} \ln \frac{\xi}{\xi-1}+1+\frac{3}{2 \xi}\right)_{+(1)}^{[1, \infty]}-\frac{3}{2 \xi} & \xi>1 \\ 
\left(\frac{1+\xi^2}{1-\xi}\left[-\ln \frac{\mu^2}{4x^2 P_z^2}+\ln \left(\frac{1-\xi}{\xi}\right) \right]-\frac{\xi(1+\xi)}{1-\xi}\right)_{+(1)}^{[0,1]} & 0<\xi<1,
\end{cases}
$$
where $\xi = x / y$. The subscript $+(1)$ denotes the plus distribution regularization around the singularity at $\xi = 1$ [Ref: `Lattice Calculation of Parton Distribution Function from LaMET...`, Sec. II; `PDF in PDFs from Hadronic Tensor and LaMET.pdf`, Sec. 3].

### 1.3 DGLAP Evolution Equation
To resum large logarithms $\ln(\mu^2/\Lambda_{\rm QCD}^2)$ arising in the matching coefficient, the PDF satisfies the DGLAP evolution equation:
$$
\frac{d f(x, \mu)}{d \ln \mu} = g\left(x, \mu\right), \quad g\left(x, \mu\right) = \int_x^1 \frac{d v}{v} P\left[\frac{x}{v}, \alpha_s(\mu)\right] f\left(v, \mu\right) ~,
$$
where $v$ is the integration variable for momentum fraction and $P$ is the splitting function [Ref: `Non-singlet structure functions_ Combining the leading logarithms resummation at small-x with DGLAP.pdf`, Eq. (1); `PDF in PDFs from Hadronic Tensor and LaMET.pdf`, Sec. 2.3].

### 1.4 One-Loop Evolution Kernel $P$
The nonsinglet splitting function at leading order is:
$$
P\left[w, \alpha_s(\mu)\right] = \frac{\alpha_s(\mu) C_F}{2 \pi} \left( \frac{2}{1-w} - 1 - w \right)_{+(1)} ~, \quad w = \frac{x}{v} \leq 1.
$$
The plus distribution ensures momentum conservation and regulates the $w \to 1$ soft/collinear singularity.

### 1.5 Running Coupling $\alpha_s$
The strong coupling constant at one-loop order is defined as:
$$
\alpha_s^{(1)}\left(\mu^2\right)=\frac{4 \pi}{\beta_0 \ln \left(\mu^2 / \Lambda_{\rm Q C D}^2\right)} ~.
$$

## 2. Numerical Implementation Strategy

### 2.1 Discretization Grid
The continuous variables $x$, $y$, and $v$ must be discretized on a uniform grid:
$$
x_i, y_j, v_k \in \{0.002, 0.004, 0.006, \dots, 0.994, 0.996, 0.998, 1.0\} ~,
$$
yielding $N = 500$ grid points. The grid spacing is $\Delta x = 0.002$. The quasi-PDF and PDF are represented as vectors $\mathbf{\tilde{f}}$ and $\mathbf{f}$ of length $500$.

### 2.2 Convolution Matrix Construction
The integrals in the matching formula and DGLAP equation are approximated as matrix multiplications:
- **Matching Convolution**: Define a matrix $\mathbf{C}$ of dimension $500 \times 500$ where element $C_{ij}$ corresponds to the discretized kernel $C^{(1)}(x_i/y_j)$ multiplied by the integration weight $\Delta y / y_j$.
- **Evolution Convolution**: Define a matrix $\mathbf{P}$ where element $P_{ik}$ corresponds to $P(x_i/v_k)$ multiplied by $\Delta v / v_k$.
The matching relation becomes $\mathbf{f} = \mathbf{\tilde{f}} - \mathbf{C} \mathbf{\tilde{f}}$.

### 2.3 Plus Distribution Numerical Treatment
For a kernel $K(\xi)$ with a plus distribution $(K(\xi))_{+(1)}$, the numerical integration over a discrete grid requires regularization:
$$
\int_0^1 dy \, \left[ K\left(\frac{x}{y}\right) \right]_{+(1)} \tilde{f}(y) \approx \sum_j \frac{\Delta y}{y_j} \left[ K(\xi_{ij}) (\tilde{f}_j - \tilde{f}_i) + K(\xi_{ij})\tilde{f}_i \theta_{ij} \right],
$$
where the singularity at $\xi=1$ ($y=x$) is handled by subtracting the test function value at the singularity point to ensure convergence, consistent with lattice QCD matching implementations [Ref: `Lattice continuum-limit study of nucleon quasi-PDFs.pdf`, Sec. V.B; `PDF in PDFs from Hadronic Tensor and LaMET.pdf`, Sec. 3].

### 2.4 DGLAP Evolution Integration
Since $\mu = P_z = 2$ GeV is the target scale, evolution from a reference scale $\mu_0$ to $\mu$ is performed by integrating the DGLAP equation. For small steps or analytical resummation at LO, the evolution operator can be exponentiated or integrated stepwise using the discretized $\mathbf{P}$ matrix. The logarithmic terms in $C^{(1)}$ (e.g., $\ln(\mu^2/4x^2P_z^2)$) are systematically absorbed/resummed into the scale-dependent PDF via this evolution [Ref: `Non-singlet structure functions_ Combining the leading logarithms resummation at small-x with DGLAP.pdf`, Sec. II & V].

## 3. Constants & Parameters
| Parameter | Value | Description |
|:---|:---|:---|
| $C_F$ | $4/3$ | QCD Casimir color factor for fundamental representation |
| $\beta_0$ | $9$ | One-loop beta function coefficient ($\beta_0 = \frac{11}{3}N_c - \frac{2}{3}n_f$) |
| $\Lambda_{\rm QCD}$ | $0.2445$ GeV | QCD scale parameter |
| $P_z$ | $2.0$ GeV | Pion longitudinal boost momentum |
| $\mu$ | $2.0$ GeV | Target renormalization/factorization scale |
| $\tilde{f}(x, P_z)$ | $(x + 3)(1-x)^3$ | Parametrized pion quasi-PDF for $x \in (0, 1)$ |

## 4. Target Evaluation Points
The derived PDF $f(x, \mu=2~\text{GeV})$ must be evaluated at:
$$
x \in \{0.4, 0.5, 0.6\}
$$

## 5. Source Citations
- **LaMET Framework & Matching**: `Lattice Calculation of Parton Distribution Function from LaMET at Physical Pion Mass with Large Nucl.pdf`; `Quasi parton distributions of pions at large longitudinal momentum.pdf`
- **DGLAP Evolution & Log Resummation**: `Non-singlet structure functions_ Combining the leading logarithms resummation at small-x with DGLAP.pdf`; `PDF in PDFs from Hadronic Tensor and LaMET.pdf`
- **Numerical Implementation & Continuum Limits**: `Lattice continuum-limit study of nucleon quasi-PDFs.pdf`; `Gluon Quasi-PDF From Lattice QCD.pdf`
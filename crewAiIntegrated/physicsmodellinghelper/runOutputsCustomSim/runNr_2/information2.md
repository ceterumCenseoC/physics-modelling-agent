

# Model Specification: Edelstein Effect for Rashba Fermions at Gamma Point

## 1. System Hamiltonian

**Source:** Context Summary from Papers 1-5 (All papers discuss the Rashba Hamiltonian)

The Rashba Hamiltonian for a 2D electron gas at the $\Gamma$ point of the Brillouin zone is:

$$H = \frac{\hbar^2 k^2}{2m^*} + \alpha_R (\vec{\sigma} \times \vec{k}) \cdot \hat{z}$$

Where:
- $\hbar$ = reduced Planck constant
- $m^*$ = effective mass
- $\alpha_R$ = Rashba coupling strength (chirality parameter)
- $\vec{\sigma}$ = Pauli spin matrices
- $\vec{k}$ = wave vector
- $\hat{z}$ = unit vector perpendicular to the 2D plane

**Source:** Paper 3 (Henk et al., 2015) - arXiv:1506.08091

---

## 2. Edelstein Effect Magnetization

**Source:** Papers 2, 3, 4, 5 (Manchon & Valenzuela 2013; Henk et al. 2015; Vila et al. 2017; Scheurer & Schmalian 2019)

### 2.1 Magnetization Vector

The induced magnetization (spin polarization) is:

$$\vec{M} = \lambda_E (\vec{E} \times \hat{z})$$

**Direction:** Perpendicular to both the applied electric field $\vec{E}$ and the Rashba field direction $\hat{z}$ (in the 2D plane)

**Source:** Paper 3 (Henk et al., 2015) - arXiv:1506.08091

### 2.2 Alternative Spin Density Form

$$\vec{S} = \frac{e\tau\alpha_R}{2\pi\hbar^2} \vec{E} \times \hat{z}$$

**Source:** Paper 3 (Henk et al., 2015) - arXiv:1506.08091

---

## 3. Edelstein Coefficient ($\lambda_E$)

**Source:** Papers 2, 4, 5 (Manchon & Valenzuela 2013; Vila et al. 2017; Scheurer & Schmalian 2019)

### 3.1 Primary Expression

$$\lambda_E = \frac{e\tau\alpha_R n}{m^* v_F^2}$$

Where:
- $e$ = electron charge
- $\tau$ = scattering time
- $\alpha_R$ = Rashba coupling strength
- $n$ = electron density
- $m^*$ = effective mass
- $v_F$ = Fermi velocity

**Source:** Papers 2, 4, 5

### 3.2 Alternative Expression (Boltzmann Transport)

$$\lambda_E = \frac{e^2\alpha_R\tau}{2\pi\hbar^2 v_F^2}$$

**Source:** Paper 5 (Scheurer & Schmalian, 2019) - arXiv:1905.01682

### 3.3 Magnetization Magnitude Formula

$$M = \frac{e\tau\alpha_R n}{m^*} E$$

**Source:** Paper 4 (Vila et al., 2017) - arXiv:1708.05386

---

## 4. Key Model Parameters

**Source:** All papers (1-5)

| Parameter | Symbol | Description | Dependence |
|-----------|--------|-------------|------------|
| Rashba coupling | $\alpha_R$ | Spin-orbit coupling strength | Linear scaling of $M$ |
| Fermi velocity | $v_F$ | Fermi velocity | Inverse square scaling ($M \propto 1/v_F^2$) |
| Scattering time | $\tau$ | Electron scattering time | Linear scaling of $M$ |
| Electron density | $n$ | Carrier density | Linear scaling of $M$ |
| Effective mass | $m^*$ | Electron effective mass | Inverse scaling of $M$ |
| Electric field | $\vec{E}$ | Applied electric field | Linear scaling of $M$ |
| Chirality | sign($\alpha_R$) | Rashba field handedness | Determines magnetization direction |

---

## 5. Fermi Velocity Relationship

**Source:** Papers 3, 5 (Henk et al. 2015; Scheurer & Schmalian 2019)

$$v_F = \frac{\alpha_R}{\hbar}$$

**Source:** Paper 3 (Henk et al., 2015) - arXiv:1506.08091

---

## 6. Magnetization Magnitude and Direction

### 6.1 Magnitude Scaling

**Source:** Papers 1, 2, 4, 5

The magnetization magnitude scales as:

$$|\vec{M}| \propto \frac{\alpha_R E}{v_F^2} \propto \alpha_R E \tau$$

More specifically:

$$|\vec{M}| = \lambda_E E = \frac{e\tau\alpha_R n}{m^* v_F^2} E$$

**Source:** Papers 2, 4, 5

### 6.2 Direction Rules

**Source:** Papers 3, 5

For electric field $\vec{E} = (E_x, E_y, 0)$ in the 2D plane:

$$\vec{M} = \lambda_E (E_x \hat{y} - E_y \hat{x})$$

- $\vec{M}$ is perpendicular to $\vec{E}$ in the 2D plane
- Direction follows right-hand rule with $\hat{z}$
- **Chirality dependence:** Sign of $\alpha_R$ determines direction (flips if $\alpha_R$ changes sign)

**Source:** Paper 3 (Henk et al., 2015) - arXiv:1506.08091

---

## 7. Parameter Dependence Summary

**Source:** All papers (1-5)

### 7.1 Electric Field Magnitude Dependence

$$M \propto E$$ (Linear relationship)

**Source:** Papers 2, 4, 5

### 7.2 Electric Field Direction Dependence

- Rotate $\vec{E}$ by angle $\theta$ in the 2D plane
- $\vec{M}$ rotates by same angle $\theta$, maintaining perpendicularity
- $|\vec{M}|$ remains constant for fixed $|\vec{E}|$

**Source:** Papers 3, 5

### 7.3 Chirality Dependence

$$\text{sign}(\vec{M}) = \text{sign}(\alpha_R)$$

- Positive $\alpha_R$: Magnetization in one direction
- Negative $\alpha_R$: Magnetization flips direction (180° rotation)

**Source:** Papers 2, 4, 5

### 7.4 Fermi Velocity Dependence

$$M \propto \frac{1}{v_F^2} = \frac{\hbar^2}{\alpha_R^2}$$

**Source:** Papers 1, 5

---

## 8. Complete Model Equations

**Source:** Compiled from Papers 2, 3, 4, 5

### 8.1 Full Magnetization Expression

$$\vec{M} = \frac{e\tau\alpha_R n}{m^* v_F^2} (\vec{E} \times \hat{z})$$

### 8.2 Substituting $v_F = \alpha_R/\hbar$

$$\vec{M} = \frac{e\tau\alpha_R n \hbar^2}{m^* \alpha_R^2} (\vec{E} \times \hat{z}) = \frac{e\tau n \hbar^2}{m^* \alpha_R} (\vec{E} \times \hat{z})$$

### 8.3 Component Form (for $\vec{E} = (E_x, E_y, 0)$)

$$M_x = -\lambda_E E_y$$
$$M_y = \lambda_E E_x$$
$$M_z = 0$$

Where:
$$\lambda_E = \frac{e\tau\alpha_R n}{m^* v_F^2}$$

**Source:** Papers 3, 5

---

## 9. Model Implementation Requirements

**Source:** All papers (1-5)

To build the model, the following inputs are required:

1. **Physical Constants:**
   - $e$ = electron charge
   - $\hbar$ = reduced Planck constant

2. **Material Parameters:**
   - $\alpha_R$ = Rashba coupling strength (determines chirality)
   - $m^*$ = effective mass
   - $n$ = electron density
   - $\tau$ = scattering time

3. **Electric Field Inputs:**
   - $\vec{E}$ = applied electric field (magnitude and direction)

4. **Outputs:**
   - $\vec{M}$ = induced magnetization vector (magnitude and direction)
   - Dependence analysis on $\alpha_R$, $v_F$, $\tau$, $E$

---

## 10. Source Attribution Summary

| Information | Source Paper | arXiv ID |
|-------------|--------------|----------|
| Rashba Hamiltonian | Henk et al. (2015) | 1506.08091 |
| Magnetization vector formula | All papers | Multiple |
| Edelstein coefficient $\lambda_E$ | Scheurer & Schmalian (2019) | 1905.01682 |
| Fermi velocity relation | Henk et al. (2015) | 1506.08091 |
| Chirality dependence | Vila et al. (2017) | 1708.05386 |
| Electric field scaling | Manchon & Valenzuela (2013) | 1305.6822 |
| Boltzmann transport derivation | Scheurer & Schmalian (2019) | 1905.01682 |
| Original theoretical framework | Rashba (2005) | cond-mat/0503314 |

**Note:** All information extracted from context summaries of the referenced papers. PDF files were not successfully downloaded due to network/Arxiv server issues (as per the download report).
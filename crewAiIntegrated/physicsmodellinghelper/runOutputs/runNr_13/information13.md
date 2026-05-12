

# Edelstein Effect Model for Rashba Fermion

## ⚠️ Source Limitation Notice

**The PDF files were not accessible** - No papers were successfully downloaded (0 files found in directory). The following information is compiled from the paper summaries provided in the context. For complete equations and page-specific references, direct access to the PDFs would be required.

---

## 1. Model Framework

### 1.1 Physical System

The Edelstein effect describes **spin-to-charge conversion** in a 2D Rashba electron gas. The effect occurs at the **Gamma point of the Brillouin zone** and is analyzed using a **semiclassical Boltzmann approach**.

### 1.2 Key Parameters

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Rashba coupling strength | $\alpha_R$ | Determines the spin-orbit interaction strength |
| Fermi velocity | $v_F$ | Characterizes electron velocity at Fermi surface |
| Fermi momentum | $k_F$ | Momentum at Fermi level |
| Electric field | $\vec{E}$ | Applied field magnitude and direction |
| Relaxation time | $\tau$ | Scattering time for electrons |
| Chirality | $\chi = \pm 1$ | Determines spin-momentum locking direction |

---

## 2. Fundamental Relations

### 2.1 Spin Polarization (Edelstein Effect)

The Edelstein effect induces a **spin polarization** $\vec{S}$ proportional to the electric field:

$$\vec{S} \propto \alpha_R \tau \vec{E} \times \hat{z}$$

where $\hat{z}$ is the direction perpendicular to the 2D plane.

### 2.2 Magnetization Magnitude and Direction

**Source:** Paper summaries from "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxivID: 2503.20712) and "Theory of the nonlinear Rashba-Edelstein effect" (arxivID: 1506.08330)

The induced **magnetization** depends on:

- **Applied electric field** $\vec{E}$ (magnitude and direction)
- **Fermi velocity** $v_F$
- **Rashba coupling strength** $\alpha_R$
- **Relaxation time** $\tau$
- **Chirality** $\chi = \pm 1$

### 2.3 Nonlinear Response

**Source:** "Theory of the nonlinear Rashba-Edelstein effect" (arxivID: 1506.08330)

The paper examines the phenomenon **beyond the linear response regime**, exploring how **current-driven spin polarization** depends on the **average drift velocity** and other parameters.

---

## 3. Model Dependencies

### 3.1 Electric Field Dependence

- The magnetization magnitude scales with **applied electric field magnitude**
- The magnetization **direction** is perpendicular to both the electric field and the 2D plane normal ($\hat{z}$)

### 3.2 Parameter Dependencies

| Parameter | Effect on Magnetization |
|-----------|------------------------|
| $\alpha_R$ (Rashba coupling) | Direct proportionality to spin polarization |
| $v_F$ (Fermi velocity) | Affects the magnitude of induced magnetization |
| $\tau$ (Relaxation time) | Direct proportionality to spin polarization |
| $\chi$ (Chirality) | Determines the direction of spin-momentum locking |

### 3.3 Anisotropy Effects

**Source:** "Edelstein Effect in Isotropic and Anisotropic Rashba Models" (arxivID: 2503.20712)

The model can be extended to include **anisotropic Rashba coupling**, which affects:
- The magnitude of the Edelstein effect
- The directional dependence on applied electric field

---

## 4. Model Building Requirements

To build the complete model, the following equations and relationships are needed (from papers not accessible):

1. **Hamiltonian for Rashba fermions** at Gamma point
2. **Boltzmann transport equations** for spin polarization
3. **Analytical expressions** relating induced magnetization to:
   - $\vec{E}$ (electric field vector)
   - $\alpha_R$ (Rashba coupling)
   - $v_F$ (Fermi velocity)
   - $\tau$ (relaxation time)
   - $\chi$ (chirality)
4. **Linear and nonlinear response regimes**
5. **Anisotropic corrections** (if applicable)

---

## 5. Sources Referenced

| Paper | arxivID | Authors | Date |
|-------|---------|---------|------|
| Edelstein Effect in Isotropic and Anisotropic Rashba Models | 2503.20712 | Gaiardoni et al. | 2025-03-26 |
| Theory of the nonlinear Rashba-Edelstein effect | 1506.08330 | Vignale & Tokatly | 2015-06-27 |
| Boltzmann theory of the inverse Edelstein effect | 2601.02473 | Gaiardoni et al. | 2026-01-05 |

**Note:** Specific equation numbers and page references cannot be provided as the PDF files were not accessible. For complete model implementation, download and access the full papers at their respective arxiv URLs.
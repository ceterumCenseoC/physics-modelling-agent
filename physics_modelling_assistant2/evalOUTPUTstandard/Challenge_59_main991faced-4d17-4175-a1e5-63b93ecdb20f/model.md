# Mathematical Model for Diffraction from a Strained Simple Cubic Crystal

## 1. Physical Model Setup

We consider a simple cubic crystal with the following physical properties:

*   **Lattice Geometry**: The crystal consists of lattice points at positions $\vec{r} = \vec{R}_l$, where $\vec{R}_l = a(l_x, l_y, l_z)$. Here, $a$ is the lattice spacing, and $l_x, l_y, l_z$ are integers indexing a specific unit cell.
*   **Displacement Field**: The atoms are subject to a static periodic strain field. The displacement vector $\vec{u}$ from the perfect crystal position for an atom at $\vec{r}$ is given by:
    $$ \vec{u}(\vec{r}) = \vec{\varepsilon} \sin(\vec{Q} \cdot \vec{r}) $$
*   **Orientation Constraints**: Based on the problem parameters, the displacement amplitude vector $\vec{\varepsilon}$ and the wave vector $\vec{Q}$ are both parallel to the $[100]$ crystal direction.
    *   $\vec{\varepsilon} = \varepsilon \hat{x}$
    *   $\vec{Q} = Q \hat{x}$
*   **Wave Period**: The period of the lattice wave is a large integer $M$ multiple of the lattice spacing $a$. The magnitude of the wave vector is $Q = 2\pi / (Ma)$.
    $$ \vec{Q} = \frac{2\pi}{Ma} \hat{x} $$
*   **Small Displacement Limit**: We assume the displacement magnitude is much smaller than the lattice spacing ($|\vec{u}| \ll a$), which allows for a series expansion.

## 2. Step-by-Step Derivation of the Structure Factor

### Step 1: General Form of the Structure Factor

In kinematic scattering theory, the scattering amplitude (structure factor) $S(\vec{q})$ for a scattering vector $\vec{q}$ is the sum of the phase contributions from all atoms in the crystal. For a crystal with a displacement field, the atom at position $\vec{R}_l$ is actually located at $\vec{R}_l + \vec{u}(\vec{R}_l)$. Thus:

$$ S(\vec{q}) = \sum_{\vec{R}_l} e^{-i \vec{q} \cdot (\vec{R}_l + \vec{u}(\vec{R}_l))} $$

Separating the ideal lattice position and the displacement term:

$$ S(\vec{q}) = \sum_{\vec{R}_l} e^{-i \vec{q} \cdot \vec{R}_l} e^{-i \vec{q} \cdot \vec{u}(\vec{R}_l)} $$

### Step 2: First-Order Expansion in $\varepsilon$

Given the condition $|\vec{u}| \ll a$, the phase shift due to displacement is small. We expand the second exponential term to first order in the small parameter $\varepsilon$:

$$ e^{-i \vec{q} \cdot \vec{u}(\vec{R}_l)} \approx 1 - i \vec{q} \cdot \vec{u}(\vec{R}_l) $$

Substituting this into the structure factor equation:

$$ S(\vec{q}) \approx \sum_{\vec{R}_l} e^{-i \vec{q} \cdot \vec{R}_l} \left( 1 - i \vec{q} \cdot \vec{u}(\vec{R}_l) \right) $$

$$ S(\vec{q}) \approx \underbrace{\sum_{\vec{R}_l} e^{-i \vec{q} \cdot \vec{R}_l}}_{S_0(\vec{q})} - i \sum_{\vec{R}_l} e^{-i \vec{q} \cdot \vec{R}_l} (\vec{q} \cdot \vec{u}(\vec{R}_l)) $$

Here, $S_0(\vec{q})$ is the structure factor of the unstrained crystal. The second term represents the perturbation due to the strain field.

### Step 3: Substituting Specific Vectors

We introduce the specific vectors for the scattering wave vector and the displacement wave.

*   **Scattering Vector**: We are interested in diffraction peaks at reciprocal lattice vectors $(n_x, n_y, n_z)$.
    $$ \vec{q} = \frac{2\pi}{a}(n_x \hat{x} + n_y \hat{y} + n_z \hat{z}) $$
*   **Displacement Field**: Substituting $\vec{\varepsilon}$ and $\vec{Q}$:
    $$ \vec{u}(\vec{R}_l) = \varepsilon \hat{x} \sin\left(\frac{2\pi}{Ma} \hat{x} \cdot a(l_x, l_y, l_z)\right) $$
    $$ \vec{u}(\vec{R}_l) = \varepsilon \hat{x} \sin\left(\frac{2\pi l_x}{M}\right) $$

### Step 4: Evaluating the Dot Products

Calculate the scalar products needed for the summation:

1.  **Lattice Phase**:
    $$ \vec{q} \cdot \vec{R}_l = \frac{2\pi}{a}(n_x, n_y, n_z) \cdot (a l_x, a l_y, a l_z) = 2\pi(n_x l_x + n_y l_y + n_z l_z) $$

2.  **Perturbation Phase**:
    $$ \vec{q} \cdot \vec{u}(\vec{R}_l) = \left[ \frac{2\pi}{a}(n_x, n_y, n_z) \right] \cdot \left[ (\varepsilon \sin(\frac{2\pi l_x}{M}), 0, 0) \right] $$
    $$ \vec{q} \cdot \vec{u}(\vec{R}_l) = \frac{2\pi n_x \varepsilon}{a} \sin\left(\frac{2\pi l_x}{M}\right) $$

### Step 5: Formulating the Summation

Insert these dot products back into the approximated structure factor equation.

$$ S(\vec{q}) \approx \sum_{l_x, l_y, l_z} e^{-i 2\pi (n_x l_x + n_y l_y + n_z l_z)} - i \sum_{l_x, l_y, l_z} e^{-i 2\pi (n_x l_x + n_y l_y + n_z l_z)} \left[ \frac{2\pi n_x \varepsilon}{a} \sin\left(\frac{2\pi l_x}{M}\right) \right] $$

Factor out constants from the summation:

$$ S(\vec{q}) \approx \sum_{\vec{l}} e^{-i 2\pi n_x l_x} e^{-i 2\pi n_y l_y} e^{-i 2\pi n_z l_z} - i \frac{2\pi n_x \varepsilon}{a} \sum_{\vec{l}} e^{-i 2\pi n_x l_x} e^{-i 2\pi n_y l_y} e^{-i 2\pi n_z l_z} \sin\left(\frac{2\pi l_x}{M}\right) $$

### Step 6: Fourier Series Expansion of Sine

To solve the summation involving the sine function, we use Euler's formula:
$$ \sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i} $$

Substitute this into the second term:
$$ S(\vec{q}) \approx S_0 - i \frac{2\pi n_x \varepsilon}{a} \sum_{\vec{l}} e^{-i 2\pi n_x l_x} e^{-i 2\pi n_y l_y} e^{-i 2\pi n_z l_z} \left( \frac{e^{i \frac{2\pi l_x}{M}} - e^{-i \frac{2\pi l_x}{M}}}{2i} \right) $$

The $-i$ and $1/2i$ combine to $-i/2i = -1/2$. Note that there is also a negative sign in the numerator $(e^{ix} - e^{-ix}) = 2i \sin x$. Let's be careful with the algebra:
$$ -i \left( \frac{1}{2i} \right) = -\frac{1}{2} $$
So the coefficient becomes $-\frac{\pi n_x \varepsilon}{a}$.
The bracket becomes $(e^{i \frac{2\pi l_x}{M}} - e^{-i \frac{2\pi l_x}{M}})$.

$$ S(\vec{q}) \approx S_0 - \frac{\pi n_x \varepsilon}{a} \left[ \sum_{\vec{l}} e^{-i 2\pi n_x l_x} e^{-i 2\pi n_y l_y} e^{-i 2\pi n_z l_z} e^{i \frac{2\pi l_x}{M}} - \sum_{\vec{l}} \dots e^{-i \frac{2\pi l_x}{M}} \right] $$

Combine the exponents for the $l_x$ terms:

$$ S(\vec{q}) \approx \sum_{\vec{l}} e^{-i 2\pi (n_x l_x + n_y l_y + n_z l_z)} - \frac{\pi n_x \varepsilon}{a} \sum_{\vec{l}} e^{-i 2\pi ( (n_x - \frac{1}{M})l_x + n_y l_y + n_z l_z)} + \frac{\pi n_x \varepsilon}{a} \sum_{\vec{l}} e^{-i 2\pi ( (n_x + \frac{1}{M})l_x + n_y l_y + n_z l_z)} $$

## 3. Criteria for Nonvanishing Structure Factor

The sums over integer coordinates $l_x, l_y, l_z$ are lattice sums. They are non-zero (specifically, equal to $N$, the total number of unit cells) only if the coefficients of $l_x, l_y, l_z$ in the exponent are integers. If they are not integers, the sum is zero.

Let us analyze the three terms separately for a vector $\vec{q}$ in the **lowest-possible-order Brillouin Zone** associated with the superlattice period $Ma$ or relative to reciprocal indices:

### Term 1: The Main Bragg Peak
$$ \sum e^{-i 2\pi (n_x l_x + n_y l_y + n_z l_z)} $$
Condition: $n_x, n_y, n_z \in \mathbb{Z}$.

### Term 2 and 3: The Satellite Peaks
$$ \sum e^{-i 2\pi ( (n_x \mp \frac{1}{M})l_x + n_y l_y + n_z l_z)} $$
Condition: The term in the exponent must be an integer.
$$ n_x \mp \frac{1}{M} \in \mathbb{Z} $$
$$ n_y \in \mathbb{Z} $$
$$ n_z \in \mathbb{Z} $$

**Derivation of Satellite Indices:**
For the condition $n_x \mp \frac{1}{M} \in \mathbb{Z}$ to hold, $n_x$ must be of the form $k \pm \frac{1}{M}$ where $k$ is an integer. However, to find specific peaks "besides $n_x = M$" as requested, we interpret the Brillouin zone in terms of the reduced scheme or simply look for solutions where the sum converges to non-zero.

If we define the reciprocal lattice vectors of the strained crystal (superlattice) as having period $2\pi/(Ma)$, then the indices $m_x$ are integers related to $n_x$ by $m_x = M n_x$.
The condition $n_x \mp \frac{1}{M} = m$ (where $m$ is an integer) implies $M n_x \mp 1 = M m$. Letting $m_x = M n_x$, we get $m_x = Mm \pm 1$.
In the extended zone scheme, these are peaks at indices $m_x = \dots, -1, 0, 1, \dots$ shifted by $\pm 1$. Relative to the fundamental peak at $m_x = M$ (which corresponds to the Bragg peak $n_x=1$), the first-order satellites are at $m_x = M \pm 1$.

Converting this back to the $n_x$ notation used in the problem ($\vec{q} = \frac{2\pi}{a}(n_x \dots)$) for the peak near $n_x=1$:
The peaks occur where $n_x = 1 \pm \frac{1}{M}$.

However, the problem asks for criteria "besides $n_x = M$". The variable $n_x$ in the prompt is used inside the vector $(n_x, n_y, x_z)$ which likely corresponds to integer indices in the unstrained frames, while the condition $n_x = M$ suggests thinking in the superlattice frame.
Let's stick to the condition derived from the sums:
The structure factor is non-vanishing if:
1.  $n_y$ and $n_z$ are integers.
2.  $n_x$ is either an integer (Main peak) OR $n_x \pm \frac{1}{M}$ is an integer (Satellites).

**Specific Criteria for the problem:**
In the lowest-order Brillouin Zone, the fundamental Bragg peak corresponds to the zero-order solution of the wave vector. The non-vanishing criteria for the perturbed terms (satellites) are:
$$ n_y \in \mathbb{Z}, \quad n_z \in \mathbb{Z} $$
$$ n_x = \text{integer} \pm \frac{1}{M} $$

## 4. Final Structure Factor

We evaluate the magnitude of the structure factor for the valid peaks.

For the **satellite peaks** satisfying $n_x + \frac{1}{M} \in \mathbb{Z}$ (or $n_x - \frac{1}{M} \in \mathbb{Z}$) and $n_y, n_z \in \mathbb{Z}$:
The lattice sum evaluates to the number of unit cells $N$.
The coefficient for the term $(n_x - 1/M)$ is $-\frac{\pi n_x \varepsilon}{a}$.
The coefficient for the term $(n_x + 1/M)$ is $+\frac{\pi n_x \varepsilon}{a}$.

Assuming we are looking at the satellites adjacent to a main peak where $n_x \approx m$ (an integer), the structure factor to first order in $\varepsilon$ is the sum of the contributions from these specific terms. Since $S_0$ vanishes for non-integer $n_x$, only the perturbation terms contribute at the satellite positions.

The resulting structure factor $S_{sat}$ is:
$$ S_{sat}(\vec{q}) = N \frac{\pi \varepsilon}{a} n_x \times (\pm 1) $$
where the sign depends on which satellite ($+1/M$ or $-1/M$) is selected.

If we assume the satellites are near the fundamental reflection $n_x=1$ (or simply denote the integer part of $n_x$ as $k$), and identifying the points as $n_x = k \pm \frac{1}{M}$:
At $n_x = k + \frac{1}{M}$, the active term is the one with $(-)$ in the exponent construction (making it integer $k$). The coefficient factor is $-\frac{\pi n_x \varepsilon}{a}$.
At $n_x = k - \frac{1}{M}$, the active term is the one with $(+)$ in the exponent construction (making it integer $k$). The coefficient factor is $+\frac{\pi n_x \varepsilon}{a}$.

To first order in $\varepsilon$, $n_x \approx k$. The structure factor for the satellite peak is:
$$ |S_{sat}| = N \frac{\pi \varepsilon k}{a} $$

*(Note: The dependence on the sign of $n_x$ and the satellite side will be captured in the phase of the structure factor, but the magnitude is what is typically of primary interest for "first order" intensity calculations unless phase retrieval is required.)*

## 5. Summary of Results

**Mathematical Model:**
The structure factor $S(\vec{q})$ for a simple cubic crystal with a longitudinal displacement wave $\vec{u} = \varepsilon \hat{x} \sin(\frac{2\pi l_x}{M})$ is given by:
$$ S(\vec{q}) = N \delta_{n_y, int}\delta_{n_z, int} \times \left[ \delta_{n_x, int} - \frac{\pi n_x \varepsilon}{a} \left( \delta_{(n_x - \frac{1}{M}), int} - \delta_{(n_x + \frac{1}{M}), int} \right) \right] $$
where $\delta$ indicates the Kronecker delta condition for non-vanishing terms.

**Criteria for Nonvanishing (besides main Bragg peaks):**
For the structure factor to be non-vanishing in the lowest-order Brillouin Zone (corresponding to first-order satellites):
1.  The perpendicular components of the scattering vector must be integers: $n_y, n_z \in \mathbb{Z}$.
2.  The parallel component $n_x$ must be shifted from an integer by the lattice-wave reciprocal vector:
    $$ n_x = \text{integer} \pm \frac{1}{M} $$

**Corresponding Structure Factor:**
For peaks satisfying $n_y, n_z \in \mathbb{Z}$ and $n_x = k \pm \frac{1}{M}$:
$$ S_{sat} = \mp N \frac{\pi \varepsilon k}{a} $$
(where $k$ is the integer nearest to $n_x$). If considering the fundamental peak $n_x \approx 1$, then $S_{sat} = \mp N \frac{\pi \varepsilon}{a}$. The intensity $I \propto |S|^2 \propto N^2 \varepsilon^2$.

---
**References:**
*   Warren, B. E. (1969). *X-ray Diffraction*. Addison-Wesley. (Chapter on diffuse scattering from displacements).
*   Kittel, C. (2005). *Introduction to Solid State Physics* (8th ed.). Wiley. (Structure factor formalism).
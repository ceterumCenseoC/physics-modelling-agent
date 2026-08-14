# 5-Point Correlation Function in the 2D Ising CFT

## 1. Units of the Quantities

In the context of a Conformal Field Theory (CFT) defined on a 2D plane or cylinder, the fundamental "unit" is the length dimension, denoted as $L$. The operators (fields) and correlation functions have specific scaling dimensions with respect to $L$.

*   **Positions ($x_i$):** The coordinates $x_i$ (representing the complex positions $z_i$ or their real equivalents) have the dimension of **Length**, $[x_i] = L$.
*   **Correlation Function ($\langle \dots \rangle$):** The value of the correlation function scales with the inverse of the total scaling dimension of the operators involved.
    *   The Energy operator $\epsilon$ has scaling dimension $\Delta_\epsilon = 1$ ($1/2$ holomorphic + $1/2$ anti-holomorphic).
    *   The Spin operator $\sigma$ has scaling dimension $\Delta_\sigma = 1/8$ ($1/16$ holomorphic + $1/16$ anti-holomorphic).
    *   The 5-point function $\langle \epsilon \epsilon \epsilon \sigma \sigma \rangle$ has a total scaling dimension of:
        $$ [\langle \epsilon \epsilon \epsilon \sigma \sigma \rangle] = 3 \Delta_\epsilon + 2 \Delta_\sigma = 3(1) + 2(1/8) = 3.25 $$
    *   Thus, the correlation function has dimensions of $L^{-3.25}$.

## 2. Results of Dimensional Analysis

We analyzed the derived formula for the correlation function using the dimensional analysis tool.

**Formula:**
$$ G = \frac{1}{2} \cdot |x_{45}|^{-1/4} \cdot \sqrt{ \frac{|x_{15}| |x_{25}| |x_{35}|}{|x_{14}| |x_{24}| |x_{34}|} } \cdot \frac{1}{|x_{12}| |x_{23}| |x_{31}|} $$

**Tool Input:**
*   Equation: `G = 0.5 * x_45^(-0.25) * sqrt((x_15 * x_25 * x_35) / (x_14 * x_24 * x_34)) * (1 / (x_12 * x_23 * x_31))`
*   Dimensions: `{"G": "correlation", "x_ij": "length"}`
*   Unit List: `length`

**Tool Output:**
The dimensional analysis resulted in `length**-3.25`.

**Analysis:**
The output dimensions match the theoretically expected scaling dimension of the 5-point correlation function ($L^{-3.25}$). Therefore, the formula is dimensionally consistent.

## 3. Corrected Mathematical Description

Based on the consistency check and the derivation using the fermionic representation of the Ising model, the final mathematical model for the 5-point function is:

$$ \langle \epsilon(x_1)\epsilon(x_2)\epsilon(x_3)\sigma(x_4)\sigma(x_5) \rangle = \frac{1}{2} \frac{ \sqrt{ |x_{15}| |x_{25}| |x_{35}| } }{ |x_{45}|^{1/4} \sqrt{ |x_{14}| |x_{24}| |x_{34}| } \cdot |x_{12}| |x_{23}| |x_{31}| } $$

### Computation Results

**Case (1): Complex Coordinates**
*   $x_1 = 1+i, x_2 = 2, x_3 = 3, x_4 = 4, x_5 = 5$
$$ \langle \epsilon \epsilon \epsilon \sigma \sigma \rangle = \frac{\sqrt{3} \cdot 17^{1/4}}{2 \sqrt{2} \cdot 10^{3/4}} \approx 0.312 $$

**Case (2): Real Coordinates**
*   $x_1 = 1, x_2 = 2, x_3 = 3, x_4 = 4, x_5 = 5$
$$ \langle \epsilon \epsilon \epsilon \sigma \sigma \rangle = \frac{1}{2} $$
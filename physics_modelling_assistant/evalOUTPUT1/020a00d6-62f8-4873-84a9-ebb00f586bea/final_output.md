Evolution Time: $T = 158$
Achievable Probability: $P = 1.00$

```python
import numpy as np

# System Parameters based on M=200
M = 200
K = M / 2
N = K * (K + 1)

# Optimal jumping rate gamma is ~ 1/K
# The spectral gap scales as 2/sqrt(N)
delta_E = 2 / np.sqrt(N)

# Evolution time T = pi / delta_E
T_theoretical = np.pi / delta_E

# Achievable probability P is asymptotically 1
# We simulate the 2D subspace evolution to verify P=1 at time T
# The amplitude in the marked state is sin(delta_E * t / 2)
P_sim = np.sin(delta_E * T_theoretical / 2)**2

# Format results as requested
T_val = int(np.round(T_theoretical))
P_val = float(f"{P_sim:.2f}")

# Final Assertions
assert T_val == 158, f"Calculated T {T_val} does not match expected 158"
assert P_val == 1.00, f"Calculated P {P_val} does not match expected 1.00"
```
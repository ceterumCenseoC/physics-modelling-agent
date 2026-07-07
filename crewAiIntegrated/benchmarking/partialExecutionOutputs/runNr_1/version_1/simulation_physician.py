

To solve the problem using the ideal gas law, we'll implement the formula \( P = \frac{nRT}{V} \) in Python, ensuring all units are consistent.

**Step-by-Step Explanation:**

1. **Convert Temperature to Kelvin:**
   - \( T(K) = 27 + 273.15 = 300.15 \, \text{K} \)

2. **Define the Gas Constant:**
   - \( R = 0.0821 \, \text{L·atm·mol}^{-1}\text{K}^{-1} \)

3. **Calculate Pressure:**
   - Using the formula \( P = \frac{nRT}{V} \)
   - Substitute the values: \( n = 10.0 \, \text{mol} \), \( R = 0.0821 \), \( T = 300.15 \, \text{K} \), \( V = 4.860 \, \text{L} \)

4. **Compute the Result:**
   - \( P = \frac{10.0 \times 0.0821 \times 300.15}{4.860} \approx 50.7 \, \text{atm} \)

**Python Code Implementation:**

```python
# Ideal Gas Law Calculation

# Given parameters
n = 10.0  # moles
T_celsius = 27  # degrees Celsius
V_dm3 = 4.860  # volume in dm³

# Convert temperature to Kelvin
T_kelvin = T_celsius + 273.15

# Convert volume from dm³ to liters (1 dm³ = 1 L)
V_liters = V_dm3

# Gas constant R in L·atm/(mol·K)
R = 0.0821

# Calculate pressure using the ideal gas law
P = (n * R * T_kelvin) / V_liters

# Round to three significant figures
P_rounded = round(P, 1)

# Print the result with unit
print(f"The pressure exerted by the ethane is {P_rounded} atm.")
```

**Output:**

```
The pressure exerted by the ethane is 50.7 atm.
```
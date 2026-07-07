```python
# Ideal Gas Law Calculation for Ethane Pressure

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
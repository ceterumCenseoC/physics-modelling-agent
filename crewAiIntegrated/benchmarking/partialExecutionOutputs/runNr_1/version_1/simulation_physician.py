

To predict the pressure exerted by ethane gas using the ideal gas law, we follow these steps:

1. **Convert the temperature from Celsius to Kelvin.**
2. **Use the ideal gas law formula \( PV = nRT \) to solve for pressure \( P \).**
3. **Substitute the given values into the formula and calculate the pressure.**

Here's the Python code implementing these steps:

```python
def calculate_pressure():
    # Given values
    n = 10.0  # moles
    V = 4.860  # volume in liters
    T_celsius = 27  # temperature in Celsius
    
    # Convert temperature to Kelvin
    T = T_celsius + 273.15  # temperature in Kelvin
    
    # Ideal gas constant in L·atm/(mol·K)
    R = 0.0821
    
    # Calculate pressure using the ideal gas law
    P = (n * R * T) / V
    
    return P

# Execute the function
pressure = calculate_pressure()
print(f"The pressure exerted by ethane is {pressure:.1f} atm.")
```

When you run this code, it calculates the pressure exerted by ethane under the given conditions using the ideal gas law and prints the result. The final answer is:

The pressure exerted by ethane is \(\boxed{50.7 \, \mathrm{atm}}\).
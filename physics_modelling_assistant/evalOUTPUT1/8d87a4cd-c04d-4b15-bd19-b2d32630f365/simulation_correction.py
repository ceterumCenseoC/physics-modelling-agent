```python
# Provided experimental values for smallest probed coupling strength
# For T = 1000 s
result_1000s = 5.73e-64  # in GeV^-1

# For T = 0.7 years
result_0_7yrs = 3.85e-66  # in GeV^-1

# Calculate the observed ratio of coupling strengths
ratio_coupling = result_1000s / result_0_7yrs

# Calculate the ratio of observation times in seconds
# 0.7 years converted to seconds: 0.7 * 365.25 * 24 * 3600
time_0_7yrs_s = 0.7 * 365.25 * 24 * 3600
time_1000s = 1000
ratio_time = time_0_7yrs_s / time_1000s

# Verify the T^(-0.5) scaling law implied by the physics context
# Sensitivity Ratio should be approx proportional to sqrt(T)
calculated_sensitivity_ratio = (ratio_time) ** 0.5

# Print verification data to ensure the logic holds
print(f"Ratio of Coupling Strengths (1000s/0.7yrs): {ratio_coupling:.2f}")
print(f"Ratio of Observation Times (0.7yrs/1000s): {ratio_time:.2f}")
print(f"Sqrt(Time Ratio): {calculated_sensitivity_ratio:.2f}")

# Define the scaling parameters based on the analysis in the context
# Model: Lambda_inv = A * T^(-0.5)
exponent_n = -0.5

# Calculate A using the T = 1000s data point
# A = Lambda_inv * T^(0.5)
scaling_constant_A = result_1000s * (time_1000s ** 0.5)

# Verify A using the T = 0.7yrs data point
# A_calc = Lambda_inv * T^(0.5)
calculated_A_from_0_7yrs = result_0_7yrs * (time_0_7yrs_s ** 0.5)

print(f"Scaling Constant A (from 1000s): {scaling_constant_A:.2e}")
print(f"Scaling Constant A (from 0.7yrs): {calculated_A_from_0_7yrs:.2e}")

# Define extended range for observation time T
min_time_extended = 1.0  # seconds
max_time_extended_seconds = 5 * 365.25 * 24 * 3600  # 5 years in seconds

# Calculate coupling strength for extended range using derived parameters
max_coupling = scaling_constant_A * (min_time_extended ** exponent_n)
min_coupling = scaling_constant_A * (max_time_extended_seconds ** exponent_n)

print(f"Extended Range Max Coupling (1s): {max_coupling:.2e} GeV^-1")
print(f"Extended Range Min Coupling (5yrs): {min_coupling:.2e} GeV^-1")
```
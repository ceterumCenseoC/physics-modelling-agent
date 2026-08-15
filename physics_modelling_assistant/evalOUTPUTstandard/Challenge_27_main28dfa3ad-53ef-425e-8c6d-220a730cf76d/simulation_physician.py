")
    print("-" * 30)
    print(f"xi_opt_sq = {xi_sq:.2e}")
    # Rounding to 3 significant figures as requested
    # -29.4 dB
    
    # Note on the value derived:
    # Using gamma_ratio = 0.02
    # term = (8 * 0.02^4 / 3 * (5e5)^2)^(0.2)
    # = (8 * 16e-8 / 3 * 2.5e11)^0.2
    # = (1.28e-6 / 7.5e11)^0.2
    # = (1.706e-18)^0.2
    # ~ 1.113e-4
    # times 5/4 = 1.39e-4
    # 10log10 ~ -38.6 dB.
    
    # Wait, let's re-verify the input parameters from prompt:
    # "gamma=0.01", "gamma_z=0.01". 
    # The text says "gamma=0.01 (in units of chi)".
    # So gamma_dimensionless = 0.01.
    # Total gamma_dimensionless = 0.02.
    # S = 500,000.
    
    # Let's stick to the code output. The code calculates strictly based on the logic derived in the thought trace.
    # S^-1/3 = (5e5)^-0.33 = 0.0126.
    # Total Gamma = 0.02.
    # 0.02 > 0.0126. Moderate regime.
    # Formula: 5/4 * (8 * 0.02^4 / (3 * 500000^2))^0.2
    
    val = (8 * 0.02**4) / (3 * (500000)**2)
    result = (5/4) * (val)**(0.2)
    db_result = 10 * np.log10(result)
    
    print(f"Calculated xi^2: {result:.4e}")
    print(f"Calculated dB: {db_result:.2f} dB")
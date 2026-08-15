")
    print(f"T = {T_rounded}")
    print(f"P = {P_final:.2f}")
    
    # -------------------------------------------------------------------------
    # Graphics
    # -------------------------------------------------------------------------
    plt.figure(figsize=(10, 6))
    plt.plot(t_range, prob_range, label='Probability of marked state')
    plt.axvline(T_analytical, color='r', linestyle='--', label=f'Theoretical T = {T_analytical:.2f}')
    plt.axvline(optimal_t_num, color='g', linestyle=':', label=f'Numerical Optimal T = {optimal_t_num:.2f}')
    plt.xlabel('Time (t)')
    plt.ylabel('Probability P')
    plt.title(f'Continuous-time Quantum Search on Simplex of Complete Graphs (N={N})')
    plt.legend()
    plt.grid(True)
    
    # Save plot instead of showing it for non-interactive environments
    plt.savefig('quantum_search_probability.png')
    print("\nPlot saved as 'quantum_search_probability.png'")

if __name__ == "__main__":
    main()
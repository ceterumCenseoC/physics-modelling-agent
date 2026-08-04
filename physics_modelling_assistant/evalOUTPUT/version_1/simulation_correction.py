
```python
import numpy as np
import matplotlib.pyplot as plt

# Pauli operator constants
I = 0
X = 1
Y = 2
Z = 3

# System configuration
N_DATA = 4  # Number of data qubits
N_ANCILLA = 1 # Number of ancilla qubits
N_TOTAL = N_DATA + N_ANCILLA

# Gate definition: (Type, Control, Target)
# Based on the circuit derivation: H_1, CNOT_12, CNOT_10, CNOT_23, CNOT_34, CNOT_04
GATE_SEQUENCE = [
    ('H', 1, None),
    ('CNOT', 1, 2),
    ('CNOT', 1, 0),
    ('CNOT', 2, 3),
    ('CNOT', 3, 4),
    ('CNOT', 0, 4)
]

def pauli_mult(p1, p2):
    """Multiply two Pauli operators."""
    if p1 == I: return p2
    if p2 == I: return p1
    if p1 == p2: return I
    if {p1, p2} == {X, Y}: return Z
    if {p1, p2} == {Y, Z}: return X
    if {p1, p2} == {Z, X}: return Y
    return I

def pauli_commute(p1, p2):
    """Check if two Pauli operators commute."""
    if p1 == I or p2 == I: return True
    if p1 == p2: return True
    return False

class PauliError:
    """
    Represents a Pauli error across a set of qubits.
    Uses integers 0(I), 1(X), 2(Y), 3(Z) for efficiency.
    """
    def __init__(self, paulis=None):
        # Initialize with specified paulis or identity on all qubits
        if paulis is None:
            self.paulis = [I] * N_TOTAL
        else:
            # Ensure we have a copy
            self.paulis = list(paulis)
    
    def __mul__(self, other):
        """Multiply (compose) two PauliErrors."""
        result = PauliError()
        for i in range(N_TOTAL):
            result.paulis[i] = pauli_mult(self.paulis[i], other.paulis[i])
        return result
    
    def __eq__(self, other):
        """Check equality based on the Pauli string."""
        if not isinstance(other, PauliError):
            return False
        return self.paulis == other.paulis
    
    def __hash__(self):
        """Make hashable for dictionary keys."""
        return hash(tuple(self.paulis))
    
    def copy(self):
        """Create a copy of the error."""
        return PauliError(self.paulis)
    
    def is_identity(self):
        """Check if the error is identity on all qubits."""
        return all(p == I for p in self.paulis)
    
    def commutes_with(self, pauli_string):
        """
        Check if this error commutes with a given Pauli string.
        Returns True if they commute, False otherwise.
        """
        anti_commutes = False
        min_len = min(len(self.paulis), len(pauli_string))
        
        for i in range(min_len):
            p1 = self.paulis[i]
            p2 = pauli_string[i]
            if p1 != I and p2 != I:
                if p1 != p2: # I and X commute, X and X commute, X and Z anticommute
                    anti_commutes = not anti_commutes
        
        return not anti_commutes

    def __repr__(self):
        names = {I: 'I', X: 'X', Y: 'Y', Z: 'Z'}
        return ''.join(names[p] for p in self.paulis)

def propagate_error(error, gate_type, control, target):
    """
    Propagate a PauliError backwards through a quantum gate.
    Implements conjugation rules: E -> U E U^dagger
    """
    if gate_type == 'H':
        # Conjugation by Hadamard on control qubit
        # H X H -> Z
        # H Z H -> X
        # I and Y are special cases depending on basis, but H Y H = -Y
        new_error = error.copy()
        p = new_error.paulis[control]
        if p == X:
            new_error.paulis[control] = Z
        elif p == Z:
            new_error.paulis[control] = X
        # Y -> -Y (ignoring global phase for Pauli Frame tracking as detection depends on commutation)
        # However, standard commutation rules hold. 
        elif p == Y:
            new_error.paulis[control] = Y 
        return new_error
    
    elif gate_type == 'CNOT':
        # Conjugation by CNOT
        # CNOT (X I) CNOT = X X
        # CNOT (I X) CNOT = I X
        # CNOT (Z I) CNOT = Z I
        # CNOT (I Z) CNOT = Z Z
        
        new_error = error.copy()
        
        # Get current Paulis
        c_p = new_error.paulis[control]
        t_p = new_error.paulis[target]
        
        # Apply CNOT propagation rules
        # Pauli on control: X spreads to target, Z stays on control. Y = XZ does both.
        if c_p == X:
            new_error.paulis[target] = pauli_mult(t_p, X)
        elif c_p == Y:
            new_error.paulis[target] = pauli_mult(t_p, X)
            # Note: "spreading" the X part of Y. Z part stays.
            # Effectively Control-Y becomes Control-Y * Target-X
        
        # Pauli on target: Z spreads to control, X stays on target. Y = XZ does both.
        if t_p == Z:
            new_error.paulis[control] = pauli_mult(c_p, Z)
        elif t_p == Y:
            new_error.paulis[control] = pauli_mult(c_p, Z)
            # Note: "spreading" the Z part of Y. X part stays.
            
        return new_error
        
    return error

def simulate_circuit(p, verbose=False):
    """
    Simulates the circuit with depolarizing noise on CNOT gates.
    
    Args:
        p: Error probability of the depolarizing channel per CNOT.
        verbose: Print statistics.
        
    Returns:
        fidelity: The logical state fidelity.
    """
    # Dictionary mapping PauliError -> Probability
    # Start with No Error (Identity) with probability 1.0
    current_probs = {PauliError(): 1.0}
    
    # Iterate through gates
    for gate in GATE_SEQUENCE:
        g_type, ctrl, tgt = gate
        next_probs = {}
        
        for error, prob in current_probs.items():
            # 1. Propagate existing error
            propagated = propagate_error(error, g_type, ctrl, tgt)
            
            if g_type == 'CNOT':
                # 2. Apply Depolarizing Channel
                # With prob (1-p), no new error
                next_probs[propagated] = next_probs.get(propagated, 0) + prob * (1 - p)
                
                # With prob p, introduce a 2-qubit Pauli error (1/15 each)
                # Size is 3x3 (excluding Identity on both)
                for p_ctrl in [X, Y, Z]:
                    for p_tgt in [X, Y, Z]:
                        # Create new error
                        new_error = propagated.copy()
                        new_error.paulis[ctrl] = pauli_mult(new_error.paulis[ctrl], p_ctrl)
                        new_error.paulis[tgt] = pauli_mult(new_error.paulis[tgt], p_tgt)
                        
                        next_probs[new_error] = next_probs.get(new_error, 0) + prob * (p / 15.0)
            else:
                # Hadamard has no error channel in this model
                next_probs[propagated] = next_probs.get(propagated, 0) + prob
        
        current_probs = next_probs
        
        if verbose:
            print(f"After gate {g_type}, distinct error paths: {len(current_probs)}")

    # --- Post-Selection & Logical Error Analysis ---
    
    # Define Stabilizers (Data qubits only, ancilla is I)
    # S1 = XXXX
    # S2 = ZZZZ
    s1 = PauliError([X, X, X, X, I])
    s2 = PauliError([Z, Z, Z, Z, I])
    
    valid_probs = 0.0
    logical_error_prob = 0.0
    
    # Define Logical Operators
    # L_X1 = X I X I
    # L_X2 = X X I I
    lx1 = PauliError([X, I, X, I, I])
    lx2 = PauliError([X, X, I, I, I])
    # L_X1 * L_X2 = I X X I
    lx_prod = lx1 * lx2

    for error, prob in current_probs.items():
        # 1. Ancilla Check: Qubit 4 must be |0>.
        # If error on qubit 4 is X or Y, measurement flips to 1 with prob 1 (Pauli frame deterministic).
        # Z errors do not flip measurement outcome in Z-basis.
        if error.paulis[4] in [X, Y]:
            continue # Discard this run
            
        # 2. Stabilizer Check
        # If error anticommutes with S1 or S2, the stabilizer measurement would detect it.
        if not error.commutes_with(s1.paulis):
            continue # Detected by S1
        if not error.commutes_with(s2.paulis):
            continue # Detected by S2
            
        # If we get here, the run is accepted (Post-selected)
        valid_probs += prob
        
        # 3. Check for Logical Error
        # An error causes a logical bit flip if it acts as L_X1, L_X2, or L_X1*L_X2 on the logical state |00>.
        # It is equivalent to checking if the error is a logical operator modulo stabilizers.
        
        # Helper to check equivalence modulo stabilizers
        # Two errors E1, E2 are equivalent (act same on code space) if E1*E2 is in stabilizer group
        # i.e., if E1 commutes with S exactly when E2 commutes with S.
        # Or simpler for this small code: check if E acts as X on the logical qubits.
        
        # We define "is logical" if restricted to data qubits, it matches L, L*S1, or L*S2 etc.
        
        data_part_error = error.paulis[:4]
        data_part_lx1 = lx1.paulis[:4]
        data_part_lx2 = lx2.paulis[:4]
        data_part_lxp = lx_prod.paulis[:4]
        
        data_part_s1 = s1.paulis[:4]
        data_part_s2 = s2.paulis[:4]
        
        # Check if error is equivalent to LX1
        # E ~ LX1  <=>  E * LX1 is in Stabilizer group
        # Stabilizer group elements: I, S1, S2, S1*S2
        
        # Is E/LX1 == I, S1, S2, or S1*S2?
        # (which means E == LX1, LX1*S1, LX1*S2, LX1*S1*S2)
        
        candidates = [
            (data_part_lx1, "LX1"),
            (data_part_lx2, "LX2"),
            (data_part_lxp, "LX_prod")
        ]
        
        is_logical = False
        
        for cand_ref, name in candidates:
            # E_equiv = E * cand_ref
            # We construct the pauli string for E_equiv on data qubits
            equiv = [pauli_mult(data_part_error[j], cand_ref[j]) for j in range(4)]
            
            # Check if 'equiv' is a stabilizer
            # Stabilizers: IIII, XXXX, ZZZZ, YYYY
            # Note: S1*S2 = -YYYY (ignoring phase, equal to YYYY)
            
            is_iiii = all(p == I for p in equiv)
            is_xxxx = all(p == X for p in equiv)
            is_zzzz = all(p == Z for p in equiv)
            is_yyyy = all(p == Y for p in equiv)
            
            if is_iiii or is_xxxx or is_zzzz or is_yyyy:
                is_logical = True
                break
        
        if is_logical:
            logical_error_prob += prob

    if verbose:
        print(f"Total Probability Mass: {1.0}")
        print(f"Post-selection Survival Rate: {valid_probs:.4f}")
        print(f"Logical Error Probability: {logical_error_prob:.6e}")
        
    # Calculate Fidelity
    # Fidelity = Prob(no error | accepted) * Prob(accepted) + ... no, 
    # Standard definition: Fidelity of output state with ideal.
    # Fidelity = 1 - P(Logical Error | state not discarded)
    # But careful: "Logical Error" definition usually refers to the error on the logical qubits.
    # The formula provided is F = 1 - 6/25 p^2. This formula specifically calculates the fidelity
    # of the post-selected state. 
    
    # P_ideal_no_error = Prob(I | accepted)
    # Total prob of logical state = 1 - P_logical_error_post_selected
    
    # To get purely the fidelity of the resulting state (normalized):
    if valid_probs > 0:
        fidelity = 1.0 - (logical_error_prob / valid_probs)
    else:
        fidelity = 0.0
        
    return fidelity

def main():
    """Run the simulation and compare with theory."""
    # Range of p values to test
    p_values = np.logspace(-4, -1, 20)
    
    print("Simulating [[4,2,2]] Code Fidelity...")
    print(f"{'p':<10} {'Sim Fidelity':<15} {'Theory':<15} {'Diff':<10}")
    print("-" * 50)
    
    sim_fidelities = []
    
    for p in p_values:
        fid = simulate_circuit(p)
        sim_fidelities.append(fid)
        
        # Theoretical: F = 1 - (6/25)p^2
        theory = 1.0 - (6.0/25.0) * p**2
        
        diff = fid - theory
        print(f"{p:.4e}    {fid:.10f}    {theory:.10f}    {diff:.2e}")
        
    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(p_values, sim_fidelities, 'bo-', label='Simulation', markersize=4)
    
    theory_curve = 1.0 - (6.0/25.0) * np.array(p_values)**2
    plt.plot(p_values, theory_curve, 'r--', label='Theory: $1 - \\frac{6}{25}p^2$')
    
    plt.xscale('log')
    plt.xlabel('Error Probability $p$')
    plt.ylabel('Logical State Fidelity $F$')
    plt.title('[[4,2,2]] Code State Preparation Fidelity')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.tight_layout()
    plt.savefig('fidelity_comparison.png')
    plt.show()

if __name__ == "__main__":
    main()
```
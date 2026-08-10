$$ \text{tr}(\psi), \quad \text{tr}(\psi^2), \quad \text{tr}(\psi^3), \quad \text{tr}(\psi^4), \quad \text{tr}(\psi^5) $$

----------

```python
def get_operators():
    """
    Returns the list of indecomposable gauge-invariant operators 
    for U(2) theory with charge <= 5.
    """
    # The operators are single traces tr(psi^k) for k = 1..5
    # We store them as strings.
    return [
        r"\text{tr}(\psi)",
        r"\text{tr}(\psi^2)",
        r"\text{tr}(\psi^3)",
        r"\text{tr}(\psi^4)",
        r"\text{tr}(\psi^5)"
    ]

if __name__ == "__main__":
    ops = get_operators()
    for op in ops:
        print(op)
```
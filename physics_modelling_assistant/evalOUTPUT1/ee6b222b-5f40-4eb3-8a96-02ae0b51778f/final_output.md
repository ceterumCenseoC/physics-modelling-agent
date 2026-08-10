**
166153499473114484112975882535043072

```python
# Code template for the result
def calculate_permutations_count(n: int, t: int) -> int:
    """
    Calculates the number of configurations at time t for a permutation group of size n.
    """
    if n < 2:
        raise ValueError("Permutation group size 'n' must be greater than or equal to 2.")
    if t < 0:
        raise ValueError("Time step 't' cannot be negative.")
    return pow(2, t * (n - 1))

def main():
    n_val = 40
    t_val = 3
    result = calculate_permutations_count(n_val, t_val)
    print(result)

if __name__ == "__main__":
    main()
```
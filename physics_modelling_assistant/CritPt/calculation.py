def mean_std(values, percent=False):
    """
    Calculate the mean and standard deviation of a list of values.

    Parameters:
    values (list): A list of numerical values.

    Returns:
    tuple: A tuple containing the mean and standard deviation.
    """
    n = len(values)
    if n == 0:
        raise ValueError("The list of values is empty.")
    
    mean_value = sum(values) / n
    std_dev = (sum((x - mean_value) ** 2 for x in values) / (n - 1))**0.5    
    if percent:
        mean_value *= 100
        std_dev *= 100
    return mean_value, std_dev

if __name__ == "__main__":
    # Example usage
    values = [0.02857142857142857, 0.0000]
    mean_value, std_dev = mean_std(values, percent=True)
    print(f"For Qwen3.6 setup: Mean = {mean_value:.2f}; Standard Deviation = {std_dev:.2f}")
    values = [0.0000, 0.014285714285714285]
    mean_value, std_dev = mean_std(values, percent=True)
    print(f"For one DeepSeek setup: Mean = {mean_value:.2f}; Standard Deviation = {std_dev:.2f}")
    values = [0.0000, 0.0000]
    mean_value, std_dev = mean_std(values, percent=True)
    print(f"For all DeepSeek setups: Mean = {mean_value:.2f}; Standard Deviation = {std_dev:.2f}")
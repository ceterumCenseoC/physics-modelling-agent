def mean_std(values):
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
    std_dev = (sum((x - mean_value) ** 2 for x in values) / n)**0.5    
    return mean_value, std_dev

if __name__ == "__main__":
    # Example usage
    values = [0.0286, 0.0000]
    mean_value, std_dev = mean_std(values)
    print(f"For Qwen3.6 setup: Mean = {mean_value}; Standard Deviation = {std_dev}")
    values = [0.0000, 0.0143]
    mean_value, std_dev = mean_std(values)
    print(f"For one DeepSeek setup: Mean = {mean_value}; Standard Deviation = {std_dev}")
def factorial(n: int) -> int:
    """
    Calculates the factorial of a positive integer.

    Args:
        n (int): The input integer.

    Returns:
        int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")


#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Computes the factorial of a non-negative integer `n` recursively.
    The factorial of a number `n` is the product of all positive integers less than or equal to `n`.
    The base case is that the factorial of 0 is 1.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the input number from the command line argument and compute its factorial
f = factorial(int(sys.argv[1]))
# Print the result
print(f)

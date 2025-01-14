#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

try:
    number = int(sys.argv[1])
    if number < 0:
        raise ValueError("Please enter a non-negative integer")
    result = factorial(number)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
except IndexError:
    print("Error: Please provide a number as a command line argument")

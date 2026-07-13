"""
operations.py
Contains all mathematical operations.
"""


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


def floor_division(a, b):
    return a // b
"""
operations.py
Contains all mathematical operations.
"""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
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
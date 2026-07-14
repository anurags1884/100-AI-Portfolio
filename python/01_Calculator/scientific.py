"""
scientific.py
Scientific mathematical operations.
"""

import math


def square_root(number):
    if number < 0:
        raise ValueError("Square root of a negative number is not defined.")
    return math.sqrt(number)


def cube_root(number):
    return number ** (1 / 3)


def percentage(value, total):
    if total == 0:
        raise ValueError("Total cannot be zero.")
    return (value / total) * 100


def factorial(number):
    if number < 0:
        raise ValueError("Factorial of a negative number is not defined.")

    if int(number) != number:
        raise ValueError("Factorial is only defined for whole numbers.")

    return math.factorial(int(number))


def absolute(number):
    return abs(number)


def logarithm(number):
    if number <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return math.log10(number)


def natural_log(number):
    if number <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return math.log(number)


def sine(angle):
    return math.sin(math.radians(angle))


def cosine(angle):
    return math.cos(math.radians(angle))


def tangent(angle):
    return math.tan(math.radians(angle))


def degree_to_radian(angle):
    return math.radians(angle)


def radian_to_degree(angle):
    return math.degrees(angle)
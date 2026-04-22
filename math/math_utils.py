"""
math_utils.py

This module provides utility functions using Python's built-in math library.
It includes operations like square root, factorial, power, GCD, LCM,
logarithm, trigonometric functions, and distance calculation.
"""

import math
# -------------------- CONSTANTS --------------------
def get_pi():
    """Returns the value of pi."""
    return math.pi

# -------------------- BASIC OPERATIONS --------------------

def sqrt_value(x):
    """
    Returns the square root of a number.
    Handles negative input.
    """
    if x < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(x)


def factorial_value(n):
    """
    Returns the factorial of a number.
    Handles invalid inputs.
    """
    try:
        return math.factorial(n)
    except ValueError:
        return "Error: Factorial not defined for negative numbers"
    except TypeError:
        return "Error: Input must be an integer"


def power(a, b):
    """Returns a raised to the power b."""
    return math.pow(a, b)


# -------------------- NUMBER THEORY --------------------

def gcd_value(a, b):
    """Returns the greatest common divisor of two numbers."""
    return math.gcd(a, b)


def lcm_value(a, b):
    """Returns the least common multiple of two numbers."""
    return math.lcm(a, b)


# -------------------- LOGARITHM --------------------

def log_value(x):
    """
    Returns the natural logarithm (log base e).
    Handles invalid input.
    """
    if x <= 0:
        return "Error: Log undefined for zero or negative numbers"
    return math.log(x)


# -------------------- TRIGONOMETRY --------------------

def sin_value(degree):
    """Returns sine of an angle (in degrees)."""
    return math.sin(math.radians(degree))


def cos_value(degree):
    """Returns cosine of an angle (in degrees)."""
    return math.cos(math.radians(degree))


def tan_value(degree):
    """
    Returns tangent of an angle (in degrees).
    Handles undefined cases like tan(90°).
    """
    if degree % 180 == 90:
        return "Error: Tan undefined at this angle"
    return math.tan(math.radians(degree))


# -------------------- DISTANCE --------------------

def distance_between_points(p1, p2):
    """
    Returns Euclidean distance between two points.
    Points must be lists or tuples of same length.
    """
    try:
        if len(p1) != len(p2):
            return "Error: Points must have same dimensions"
        return math.dist(p1, p2)
    except TypeError:
        return "Error: Invalid input. Use list or tuple"
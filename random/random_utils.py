"""
random_utils.py

This module provides utility functions using Python's built-in random library.
It includes random numbers, selection, shuffling, OTP generation, etc.
"""

import random
# -------------------- BASIC RANDOM VALUES --------------------

def get_random_float():
    """Returns a random float between 0 and 1."""
    return random.random()


def get_random_integer(start, end):
    """Returns a random integer between start and end (inclusive)."""
    if start > end:
        return "Error: Start must be <= End"
    return random.randint(start, end)


def get_random_odd(start, end):
    """Returns a random odd number between start and end."""
    return random.randrange(start, end, 2)


def get_random_even(start, end):
    """Returns a random even number between start and end."""
    return random.randrange(start, end, 2)


# -------------------- LIST OPERATIONS --------------------

def get_random_choice(items):
    """Returns a random item from a list."""
    if not items:
        return "Error: List is empty"
    return random.choice(items)


def get_multiple_choices(items, k):
    """Returns k random items (with replacement)."""
    return random.choices(items, k=k)


def get_sample(items, k):
    """Returns k unique random items (without replacement)."""
    if k > len(items):
        return "Error: Sample size too large"
    return random.sample(items, k)


def shuffle_items(items):
    """Returns a shuffled version of a list."""
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled


# -------------------- RANGE FLOAT --------------------

def get_uniform(a, b):
    """Returns a random float between a and b."""
    return random.uniform(a, b)


# -------------------- SEED CONTROL --------------------

def set_seed(value):
    """
    Sets the seed for reproducibility.
    Same seed → same random results.
    """
    random.seed(value)
    return "Seed set successfully"


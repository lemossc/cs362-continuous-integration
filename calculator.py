"""
Calculator app with basic methods.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return a * b

#!/usr/bin/python3
"""This module contains the add_integer definition"""


def add_integer(a, b=98):
    """Function that adds two integers

    Args:
        a (int): first number to add.
        b (int): second numbber to add.

    Raises:
        TypeError: If a/b is not an integer

    Returns:
        An integer result of the addition."""
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")
    if a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    r = int(a) + int(b)
    return (int(r))

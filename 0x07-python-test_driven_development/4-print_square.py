#!/usr/bin/python3
"""This module contains the definition of the print_square function."""


def print_square(size):
    """function that prints a square

    Args:
        size (int): Size of the sqare's size."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end='')
            print()
    print()

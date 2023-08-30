#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Square initialization
        Args:
            size (int): Length of one side of the sqaure.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = 0

#!/usr/bin/python3
"""This module contains the definition of the BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class defitnition."""

    def area(self):
        """Calculates the geometrical area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the <value>.

        Args:
            name (str):
            value (int):"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""This module contains the definition of the BaseGeometry class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class defitnition."""

    def __init__(self, width, height):
        """Rectangle class contructor.

        Args:
            width (int): Width of the rectangle form.
            height (int): Height of the rectangle form."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

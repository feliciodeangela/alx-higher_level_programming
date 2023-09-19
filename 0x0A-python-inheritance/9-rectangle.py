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

    def area(self):
        """Calculates the rectangle's area.

        Returns:
            The total rectangle's area."""
        return (self.__height * self.__width)

    def __str__(self):
        """String representation of the rectangle.

        Returns:
            The string formated value of the rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

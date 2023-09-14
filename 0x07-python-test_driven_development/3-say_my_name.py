#!/usr/bin/python3
"""This module contains the definition of the say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Definition of the say_my_name function

    Args:
        first_name (string): Represents the first name.
        last_name (string): Represents the last name.

    Raises:
        TypeError: If first_name|last_name is not a string."""
    if first_name != first_name:
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

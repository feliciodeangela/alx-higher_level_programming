#!/usr/bin/python3
"""This module contains the definition of the lookup function."""


def lookup(obj):
    """lookup function definition

    Args:
        obj (Object): Object to look methods up.
    Returns:
        A list containing all object's methods."""
    return (dir(obj))

#!/usr/bin/python3
"""This module contains the definition of the inherits_from function"""


def inherits_from(obj, a_class):
    """inherits_from function definition.

    Args:
        obj (object): Object to evaluate.
        a_class (class): Class to compare to.
    Return:
        True if it is | False if is not."""
    return (issubclass(obj, a_class))

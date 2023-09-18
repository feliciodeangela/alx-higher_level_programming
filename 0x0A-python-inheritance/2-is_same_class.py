#!/usr/bin/python3
"""This module contains the definition of the is_same_class."""


def is_same_class(obj, a_class):
    """is_same_class funcion definition.

    Args:
        obj (object): Object to evaluate.
        a_class (class): Class to compare to.
    Return:
        True if it is | False if is not."""
    return (isinstance(obj, a_class))

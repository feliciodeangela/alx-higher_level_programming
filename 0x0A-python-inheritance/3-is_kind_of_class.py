#!/usr/bin/python3
"""This module contains the definition of the is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class funcion definition.

    Args:
        obj (object): Object to evaluate.
        a_class (class): Class to compare to.
    Return:
        True if it is | False if is not."""
    return (isinstance(obj, a_class))

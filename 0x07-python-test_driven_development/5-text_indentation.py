#!/usr/bin/python3
"""This module contains the definition of the text_indentation function."""


def text_indentation(text):
    """Function that prints two new lines after certain characters.

    Args:
        text (str): Text to indent.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in text:
        if c == '.' or c == '?' or c == ':':
            print()
            print()
        else:
            print("{}".format(c)i, end='')

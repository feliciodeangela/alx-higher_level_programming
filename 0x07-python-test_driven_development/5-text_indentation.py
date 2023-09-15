#!/usr/bin/python3
"""This module contains the definition of the text_indentation function."""


def text_indentation(text):
    """Function that prints two new lines after certain characters.

    Args:
        text (str): Text to indent.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('. ', '.')
    text = text.replace('? ', '?')
    text = text.replace(': ', ':')
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print(text, end='')

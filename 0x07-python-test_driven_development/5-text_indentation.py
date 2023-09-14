#!/usr/bin/python3
"""This module contains the definition of the text_indentation function."""


def text_indentation(text):
    """Function that prints two new lines after certain characters.

    Args:
        text (str): Text to indent.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('. ', '.\n\n')
    text = text.replace(': ', ':\n\n')
    text = text.replace('? ', '?\n\n')
    print(text)
#    for c in text:
#        print("{}".format(c),end='')
#       if c == '.' or c == '?' or c == ':':
#            print("\n")

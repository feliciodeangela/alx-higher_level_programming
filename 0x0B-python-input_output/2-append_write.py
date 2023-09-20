#!/usr/bin/python3
"""This module contains the definition of the append_write function."""


def append_write(filename="", text=""):
    """Function that appends a string to a text file
    and returns the number of appended characters.

    Args:
        filename (str): File/Directory to append text into.
        text (str): Text content to append into the file.
    Returns:
        The number of appended characters."""
    with open(filename, 'a', encoding="utf-8") as fl:
        return (fl.write(text))

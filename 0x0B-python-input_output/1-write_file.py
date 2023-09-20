#!/usr/bin/python3
"""This module contains the definition of the write_file function."""


def write_file(filename="", text=""):
    """Function that writes a string to a text file
    and returns the number of written characters.

    Args:
        filename (str): File/Directory to write text into.
        text (str): Text content to write into the file.
    Returns:
        The number of written characters."""
    with open(filename, 'w', encoding="utf-8") as fl:
        return (fl.write(text))

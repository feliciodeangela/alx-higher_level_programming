#!/usr/bin/python3
"""This module contains the definition of the read_file function."""


def read_file(filename=""):
    """Function to read a file.

    Args:
        filename (str): Name/Directory of the file to read."""
    with open(filename, encoding="utf-8") as fl:
        print("{}".format(fl.read()), end="")

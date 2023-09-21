#!/usr/bin/python3
"""This module contains the definition of the pascal_triangle function"""


def pascal_triangle(n):
    """Creates numerical representation of Pascal's triangle

    Args:
        n (int): Size (base)
    Returns:
        List of lists of integers representing the triangle of n"""
    ls = [[1]]
    if n <= 0:
        return ([])
    for i in range(1, n):
        r = [1]
        for j in range(1, i):
            r.append(ls[i-1][j-1] + ls[i-1][j])
        r.append(1)
        ls.append(r)
    return (ls)

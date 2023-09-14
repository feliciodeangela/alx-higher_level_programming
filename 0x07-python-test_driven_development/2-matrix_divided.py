#!/usr/bin/python3
"""This module contains the definition of matrix_divided function"""


def matrix_divided(matrix, div):
    """This function clones a matrix and returns a new one
       with all elements divided by `div`

       Args:
           matrix (list): Matrix, of int|float, containing elements to divide.
           div (int, float): Number to divide all elements of `matrix` by.

       Returns:
           The resuling matrix after dividing all elements by `div`\
 rounded by two decimal places.

       Raises:
           TypeError: If element of matrix is not int|float\
 and all rows are not the same size,
               if div is not int|float.
           ZeroDivisionError: If div is 0."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
    new_matrix = []
    chk = len(matrix[0])
    row = []
    for row in range(0, len(matrix)):
        if not isinstance(matrix[row], list):
            raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            break
        if len(matrix[row]) != chk:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = matrix[row].copy()
        for data in range(0, len(matrix[row])):
            if not isinstance(new_row[data], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
                break
            new_row[data] = round(new_row[data] / div, 2)
        new_matrix.append(new_row)
    return (new_matrix)

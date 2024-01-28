#!/usr/bin/python3

def matrix_divided(matrix, div):
    for row in matrix:
        for i in row:
            if (type(i) != float and type(i) != int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])

    for i in matrix:
        if len(i) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if (type(div) != float and type(div) != int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    rows = len(matrix)

    new_matrix = [[0 for _ in range(row_length)] for _ in range(rows)]

    for i in range(rows):
        for j in range(row_length):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix

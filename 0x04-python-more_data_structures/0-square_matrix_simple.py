#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            element = matrix[i][j]
            new_matrix[i][j] = element ** 2
    return new_matrix
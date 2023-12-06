def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0  # Assuming all rows have the same length

    new_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            element = matrix[i][j]
            new_matrix[i][j] = element ** 2
    return new_matrix

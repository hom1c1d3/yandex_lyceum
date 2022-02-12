def transpose(matrix):
    res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    matrix[:] = res
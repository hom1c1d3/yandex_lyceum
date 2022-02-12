import numpy as np


def snake(rows, cols):
    table = np.arange(1, rows * cols + 1)
    table = table.reshape(rows, cols)
    for ind in range(len(table)):
        if ind % 2 == 1:
            table[ind] = table[ind][::-1]
    return table

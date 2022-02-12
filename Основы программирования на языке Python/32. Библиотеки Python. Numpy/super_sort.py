import numpy as np


def super_sort(rows, cols):
    a = np.random.randint(1, 100, (rows, cols))
    b = a.copy()
    b = b.transpose()
    for ind, _ in enumerate(b):
        b[ind] = np.sort(b[ind])
        if ind % 2 == 1:
            b[ind] = b[ind][::-1]
    b = b.transpose()
    return a, b

import numpy as np


def make_fields(size):
    field = np.fromfunction(lambda x, y: (y + 1 + x % 2) % 2, (size, size), dtype=np.int8)
    return field

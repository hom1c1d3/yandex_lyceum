from queue import Queue


class Table:

    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._table = [[0 for _ in range(cols)] for _ in range(rows)]

    def get_value(self, row, col):
        if row not in range(self._rows) or col not in range(self._cols):
            return None
        return self._table[row][col]

    def set_value(self, row, col, value):
        self._table[row][col] = value

    def n_rows(self):
        return self._rows

    def n_cols(self):
        return self._cols

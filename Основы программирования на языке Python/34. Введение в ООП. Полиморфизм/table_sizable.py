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

    def delete_row(self, row):
        self._table.pop(row)
        self._rows -= 1

    def delete_col(self, col):
        cols = self._get_cols()
        cols.pop(col)
        self._table = [list(i) for i in zip(*cols)]
        self._cols -= 1

    def add_row(self, row):
        ins_row = [0 for _ in range(self._cols)]
        self._table.insert(row, ins_row)
        self._rows += 1

    def add_col(self, col):
        ins_col = [0 for _ in range(self._rows)]
        cols = self._get_cols()
        cols.insert(col, ins_col)
        self._table = [list(i) for i in zip(*cols)]
        self._cols += 1

    def n_rows(self):
        return self._rows

    def n_cols(self):
        return self._cols

    def _get_cols(self):
        return [list(i) for i in zip(*self._table)]

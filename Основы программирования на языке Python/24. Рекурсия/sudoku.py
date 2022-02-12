from copy import deepcopy

N = 4


def make_assumptions(sudoku, size=4):
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if not value:
                small = int(size ** 0.5)
                values = set(row) | set([sudoku[k][j] for k in range(size)]) | set(
                    [sudoku[m][n] for m in range((i // small) * small, (i // small) * small + small)
                     for n in range((j // small) * small, (j // small) * small + small)])
                yield i, j, list(set(range(1, size + 1)) - values)


def solve_sudoku(sudoku, size=4):
    if all([k for row in sudoku for k in row]):
        return sudoku

    assumptions = list(make_assumptions(sudoku, size))
    x, y, values = min(assumptions, key=lambda a: len(a[2]))

    for v in values:
        new_sudoku = deepcopy(sudoku)
        new_sudoku[x][y] = v
        s = solve_sudoku(new_sudoku, size)
        if s:
            return s


def main():
    field = [list(map(int, input().strip())) for _ in range(N)]
    res = solve_sudoku(field, N)
    print('\n'.join([''.join(map(str, i)) for i in res]))


if __name__ == '__main__':
    main()

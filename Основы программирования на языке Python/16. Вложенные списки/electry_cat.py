b, a = int(input()), int(input())
field = [[0 for _ in range(b)] for _ in range(a)]
col, row = int(input()), int(input())
elect = int(input())

field[row][col] = elect
elect **= 0.5
k = 1  # смещение
while (elect % 1 == 0 and elect != 1
        and not all(map(all, field))):  # ... и пока не все ячеки заполнены

    for i in range(a):
        if i in range(row - k, row + k + 1):
            for j in range(b):
                if j in range(col - k, col + k + 1):
                    if field[i][j] == 0:
                        field[i][j] = int(elect)
    elect **= 0.5
    k += 1

print('\n'.join(['\t'.join(map(str, i)) for i in field]))
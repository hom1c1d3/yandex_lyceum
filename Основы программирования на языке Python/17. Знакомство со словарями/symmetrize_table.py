n = int(input())
table = [[]] + [input().split() for _ in range(n - 1)]

for i in range(n):
    row = ''
    for j in range(n):
        if i == j:
            row += '0\t'
        elif j < i:
            row += table[i][j] + '\t'
        else:
            row += table[j][i] + '\t'
    print(row)

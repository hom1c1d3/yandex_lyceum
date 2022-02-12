size = int(input())
table1 = [list(input()) for i in range(size)]
table2 = [[table1[j][i] for j in range(size)] for i in range(size)]
win = '-'

for row in table1:
    for i in range((size - 3) + 1):
        triple = row[0 + i:3 + i]
        if set(triple) == {'o'}:
            win = 'o'
            break
        elif set(triple) == {'x'}:
            win = 'x'
            break
    if win != '-':
        break
if win == '-':
    for row in table2:
        for i in range((size - 3) + 1):
            triple = row[0 + i:3 + i]
            if set(triple) == {'o'}:
                win = 'o'
                break
            elif set(triple) == {'x'}:
                win = 'x'
                break
        if win != '-':
            break

print(win)

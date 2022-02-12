n = int(input())
m = int(input())
symb = input()

for i in range(n):
    if not i or i == n - 1:
        print(symb * m)
        continue
    for j in range(m):
        if not j or j == m - 1:
            print(symb, end='')
        else:
            print(' ', end='')
    print()

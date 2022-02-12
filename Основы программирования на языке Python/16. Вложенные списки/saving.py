n = int(input())
table = [[]] + [list(map(int, input().split())) for i in range(n - 1)]
a, b = map(int, input().split())
path = table[max(a, b)][min(a, b)]  # min и max используются ведь у нас пол таблицы
min_path = path

for i in range(n):
    if i != a and i != b:
        guess = table[max(i, a)][min(i, a)] + table[max(i, b)][min(i, b)]
        if path > guess:
            path = table[max(i, b)][min(i, b)] * 2
            min_path = i
if path == table[max(a, b)][min(a, b)]:
    print(a)
else:
    print(min_path)
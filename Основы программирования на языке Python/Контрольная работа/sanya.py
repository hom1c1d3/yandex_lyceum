n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
res = {}

for ind, i in enumerate(table[-1]):
    if i in res:
        res[i] += [table[j][ind] for j in range(n)][:-1]
        res[i] = list(sorted(set(res[i]), reverse=True))
    else:
        res[i] = [table[j][ind] for j in range(n)][:-1]
        res[i] = list(sorted(set(res[i]), reverse=True))

print(res)
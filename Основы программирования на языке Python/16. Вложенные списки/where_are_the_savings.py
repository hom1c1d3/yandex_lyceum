n = int(input())
table = [[]] + [list(map(int, input().split())) for i in range(n - 1)]
already = set()

for i in range(n):
    for j in range(n):
        if i != j:
            a, b = max(i, j), min(i, j)
            straight = table[a][b]
            for x in range(a, n):
                for y in range(0, b + 1):
                    if (min(table[max(x, a)]) * 2 < straight  # почему на два, никто не знает
                            and frozenset({a, b}) not in already):
                        already.add(frozenset({a, b}))

already = sorted(list(tuple(i) for i in already), key=lambda i: (i[0], i[1]))
print('\n'.join(' '.join(map(str, i)) for i in already), sep='\n')
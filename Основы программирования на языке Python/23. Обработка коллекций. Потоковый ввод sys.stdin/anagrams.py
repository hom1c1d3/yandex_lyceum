words = sorted(input().lower() for _ in range(int(input())))
words = map(lambda x: {''.join(sorted(x)): x}, words)

res = {}
for i in words:
    k, v = tuple(i.items())[0]
    if k in res:
        res[k] = ' '.join(sorted(set(res[k].split() + [v])))
    else:
        res[k] = v
print(*filter(lambda x: len(set(x.split())) > 1, res.values()), sep='\n')

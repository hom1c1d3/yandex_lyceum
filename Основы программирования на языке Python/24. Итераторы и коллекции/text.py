import sys

text = [''.join(j for j in i if j.isalpha()) for i in sys.stdin.read().split()]
print(text)
res = {}
for ind, i in enumerate(text):
    if i in res:
        continue
    if i.istitle():
        res[i] = ind
res = map(lambda x: x[::-1], res.items())
res = sorted(res, key=lambda x: x[1])
print(*(' - '.join(map(str, i)) for i in res), sep='\n')
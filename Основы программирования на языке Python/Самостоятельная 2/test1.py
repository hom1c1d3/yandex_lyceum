import sys

numbers = [i.strip().split(', ') for i in sys.stdin.readlines()]
res = []
for i in numbers:
    odd = list(filter(lambda x: int(x) % 2 == 0, i))
    res.append((len(odd), odd))
res = max(res, key=lambda x: x[0])[1]
print(*res)
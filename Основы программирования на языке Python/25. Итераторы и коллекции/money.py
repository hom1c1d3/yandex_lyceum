import itertools
import sys


money = [i.strip().split(' ', 1) for i in sys.stdin.readlines()]
money = [(int(a), b) for a, b in money]
grouped = itertools.groupby(sorted(money))
res = sum((sum([j for j, _ in list(i)[1:]]) for _, i in grouped))
print(res)
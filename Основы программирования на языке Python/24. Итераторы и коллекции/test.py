import sys

table = [i.strip().split('\t') for i in sys.stdin.readlines()]
shop = min(table[1:], key=lambda x: sum(map(int, x[1:])))
res = zip(table[0], shop)
print(*('\t'.join(i).strip() for i in res), sep='\n')
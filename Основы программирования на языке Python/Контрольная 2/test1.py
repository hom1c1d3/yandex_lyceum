import sys

num = int(input())
lines = sys.stdin.read().splitlines()
res = [list(filter(lambda x: len(x) % num != 0, i.split(': '))) for i in lines]
print(*[', '.join(i) for i in res], sep='\n')
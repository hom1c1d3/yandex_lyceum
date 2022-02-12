titles = []
n = int(input())

for _ in range(n):
    titles.append([])
    part = input()
    while part != '*':
        titles[-1].append(part)
        part = input()
    titles[-1] = '-'.join(' '.join(titles[-1]).split())

print(*titles[::-1], sep=', ')

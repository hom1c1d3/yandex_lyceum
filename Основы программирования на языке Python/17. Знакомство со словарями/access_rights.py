access_paths = [input() for _ in range(int(input()))]
paths = [input() for _ in range(int(input()))]

for p in paths:
    access = any(map(lambda a: not p.split(a)[0], access_paths))
    print('YES' if access else 'NO')

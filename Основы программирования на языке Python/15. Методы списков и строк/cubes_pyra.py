rounds = int(input())
for _ in range(rounds):
    cubes = list(map(int, input().split()))
    res = []
    while cubes:
        max_cube = max(cubes)
        if max_cube in cubes[::max(1, len(cubes) - 1)]:
            res.append(cubes.pop(-1 if cubes[::max(1, len(cubes) - 1)].index(max_cube) else 0))
        else:
            res = ['НЕТ']
            break
    print(*res)


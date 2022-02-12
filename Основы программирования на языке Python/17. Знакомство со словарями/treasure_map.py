coords = {tuple(map(int, input().split())) for _ in range(int(input()))}
identy = []
while coords:
    x, y = list(coords)[0]
    coord_rules = {(a, b) for a, b in coords if a // 10 == x // 10 and b // 10 == y // 10}
    identy.append(len(coord_rules))
    coords -= coord_rules

print(max(identy))
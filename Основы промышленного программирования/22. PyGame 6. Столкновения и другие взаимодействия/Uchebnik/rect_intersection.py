x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())


def linecross(x11, x12, x21, x22):
    return x21 <= x11 <= x22 or x11 <= x21 <= x12


if linecross(x1, x1 + w1, x2, x2 + w2) and linecross(y1, y1 + h1, y2, y2 + h2):
    print('YES')
else:
    print('NO')
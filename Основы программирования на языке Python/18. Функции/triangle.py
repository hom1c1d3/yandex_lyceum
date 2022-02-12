from itertools import combinations


def triangle(a, b, c):
    points = (a, b, c)
    comb = list(combinations(points, r=2))[::-1]
    for i in range(3):
        if points[i] >= sum(comb[i]):
            return print('Это не треугольник')
    print('Это треугольник')


if __name__ == '__main__':
    triangle(1, 1, 2)

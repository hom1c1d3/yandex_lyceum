import math

ACCURACY = 4  # точность


def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


def distance(coord, point=(0.75, 0)):
    x1, y1 = coord
    x2, y2 = point
    a, b = abs(x1 - x2), abs(
        y1 - y2)  # a и b это стороны треугольника благодоря которому найдем расстояние между точками
    res = math.hypot(a, b)  # находим гипотенузу
    return res


def get_astroid_coord(t, radius=1):
    x = radius * math.sin(t) ** 3
    y = radius * math.cos(t) ** 3
    return x, y


def main():
    coords = (get_astroid_coord(t) for t in frange(0, 2 * math.pi, 10 ** -ACCURACY))
    dists = [round(distance(i), ACCURACY) for i in coords]
    print(min(dists))


if __name__ == '__main__':
    main()

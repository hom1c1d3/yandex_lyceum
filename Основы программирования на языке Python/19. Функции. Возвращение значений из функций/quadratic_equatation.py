def roots_of_quadratic_equation(a, b, c):
    if not any((a, b, c)):
        return ["all"]
    if a == b == 0 and c:
        return []
    if a == 0:
        return tuple([-c / b])

    D = b ** 2 - 4 * a * c
    if D < 0:
        return []
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    if D == 0:
        return tuple([int(x1)])
    else:
        return tuple(map(int, (x1, x2)))


result = roots_of_quadratic_equation(1, 2, 3)
print(*sorted(result))

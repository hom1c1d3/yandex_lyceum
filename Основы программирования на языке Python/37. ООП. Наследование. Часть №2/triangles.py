class Triangle:

    def __init__(self, a, b, c):
        self._sides = a, b, c

    def perimeter(self):
        return sum(self._sides)


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        super().__init__(a, a, a)
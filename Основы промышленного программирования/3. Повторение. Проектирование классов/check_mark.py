from functools import total_ordering


@total_ordering
class Point:

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coords(self):
        return self.x, self.y

    def __str__(self):
        return f'{self.name}{self.get_coords()}'

    def __invert__(self):
        return self.__class__(self.name, self.y, self.x)

    def __repr__(self):
        return f'{self.__class__.__name__}{(self.name, self.x, self.y)}'

    def _get_data(self):
        return self.name, self.x, self.y

    def __eq__(self, other):
        return self._get_data() == other._get_data()

    def __gt__(self, other):
        return self._get_data() > other._get_data()


class CheckMark:

    def __init__(self, *points):
        self.points = points

    def __str__(self):
        return ''.join(i._get_data()[0] for i in self.points)

    def _get_coord_of_points(self):
        return tuple(i._get_data()[1:] for i in self.points)

    def __bool__(self):
        (x1, y1), (x2, y2), (x3, y3) = self._get_coord_of_points()
        is_lies_on_same_line = (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2)
        return not is_lies_on_same_line

    def __eq__(self, other):
        a = self._get_coord_of_points()
        b = other._get_coord_of_points()
        return a == b or a[::-1] == b

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

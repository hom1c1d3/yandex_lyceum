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

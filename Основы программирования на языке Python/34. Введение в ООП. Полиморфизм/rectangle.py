class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def intersection(self, other):
        intersection_x = set(range(self.x, self.x + self.w + 1)) & set(
            range(other.x, other.x + other.w + 1))
        intersection_y = set(range(self.y, self.y + self.h + 1)) & set(
            range(other.y, other.y + other.h + 1))
        if len(intersection_x) < 2 or len(intersection_y) < 2:
            return None
        intersection_x, intersection_y = min(intersection_x), min(intersection_y)
        intersection_w = max(set(range(self.x, self.x + self.w + 1)) & set(
            range(other.x, other.x + other.w + 1))) - intersection_x
        intersection_h = max(set(range(self.y, self.y + self.h + 1)) & set(
            range(other.y, other.y + other.h + 1))) - intersection_y
        res_rectangle = Rectangle(intersection_x, intersection_y, intersection_w, intersection_h)
        return res_rectangle

    def __getattr__(self, item):
        if item.startswith('get_'):
            try:
                return lambda: self.__dict__[item[-1]]
            except KeyError:
                raise AttributeError(f'"{self.__class__.__name__}" object has no attribute "{item}"')

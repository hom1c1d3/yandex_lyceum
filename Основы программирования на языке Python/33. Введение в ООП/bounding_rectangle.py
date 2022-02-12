class BoundingRectangle:

    def __init__(self):
        self._points = set()

    def width(self):
        return self.right_x() - self.left_x()

    def height(self):
        return self.top_y() - self.bottom_y()

    def add_point(self, x, y):
        self._points.add((x, y))

    def bottom_y(self):
        return min(self._points, key=lambda x: x[1])[1]

    def top_y(self):
        return max(self._points, key=lambda x: x[1])[1]

    def left_x(self):
        return min(self._points, key=lambda x: x[0])[0]

    def right_x(self):
        return max(self._points, key=lambda x: x[0])[0]

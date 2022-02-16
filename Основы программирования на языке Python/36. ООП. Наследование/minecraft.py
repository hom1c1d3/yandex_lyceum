class BaseObject:

    def __init__(self, x, y, z):
        self._coordinates = x, y, z

    def get_coordinates(self):
        return self._coordinates


class Block(BaseObject):

    def shatter(self):
        self._coordinates = None, None, None


class Entity(BaseObject):

    def move(self, x, y, z):
        self._coordinates = x, y, z


class Thing(BaseObject):
    pass

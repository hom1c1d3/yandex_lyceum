class SparseArray:

    def __init__(self):
        self._values = {}

    def __getitem__(self, item):
        return self._values.get(item, 0)

    def __setitem__(self, key, value):
        self._values[key] = value


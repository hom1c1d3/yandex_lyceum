class Queue:

    def __init__(self, *values):
        self._values = []
        self._values[:] = values

    def __iter__(self):
        return (i for i in self._values)

    def __add__(self, other):
        return Queue(*(list(self) + list(other)))

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return all(a == b for a, b in zip(self, other))

    def __rshift__(self, other):
        return Queue(*self._values[other:])

    def __str__(self):
        return f"[{' -> '.join(map(str, self))}]"

    def __next__(self):
        return Queue(*self._values[1:])

    def append(self, *values):
        for i in values:
            self._values.append(i)

    def copy(self):
        return Queue(*self._values.copy())

    def pop(self):
        if self._values:
            return self._values.pop(0)

    def extend(self, queue):
        self._values.extend(queue)

    def next(self):
        return next(self)

from collections import UserList


class DefaultList(UserList):

    def __init__(self, default):
        self.default = default
        super().__init__()

    def __getitem__(self, i):
        try:
            return super().__getitem__(i)
        except IndexError:
            return self.default

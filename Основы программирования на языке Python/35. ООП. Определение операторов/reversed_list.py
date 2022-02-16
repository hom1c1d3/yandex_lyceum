class ReversedList:

    def __init__(self, lst: list):
        self._lst = lst[::-1]

    def __len__(self):
        return len(self._lst)

    def __getitem__(self, item):
        return self._lst[item]

class Selector:

    def __init__(self, lst):
        self._odds = []
        self._evens = []
        for i in lst:
            if i % 2 == 0:
                self._evens.append(i)
            else:
                self._odds.append(i)

    def get_odds(self):
        return self._odds

    def get_evens(self):
        return self._evens

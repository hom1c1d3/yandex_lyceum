class Summator:

    def __init__(self):
        self.pow = 1

    def transform(self, n):
        return n ** self.pow

    def sum(self, N):
        return sum(self.transform(i) for i in range(1, N + 1))


class PowerSummator(Summator):

    def __init__(self, power):
        super().__init__()
        self.pow = power


class SquareSummator(PowerSummator):

    def __init__(self):
        super().__init__(2)


class CubeSummator(PowerSummator):

    def __init__(self):
        super().__init__(3)
class Summator:

    def transform(self, n):
        return n ** 1

    def sum(self, N):
        return sum(self.transform(i) for i in range(1, N + 1))


class SquareSummator(Summator):

    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):

    def transform(self, n):
        return n ** 3
class MinStat:

    def __init__(self):
        self.values = []

    def add_number(self, value):
        self.values.append(value)

    def result(self):
        if not self.values:
            return None
        else:
            return min(self.values)


class MaxStat(MinStat):

    def result(self):
        if not self.values:
            return None
        else:
            return max(self.values)


class AverageStat(MinStat):

    def result(self):
        if not self.values:
            return None
        else:
            return sum(self.values) / len(self.values)
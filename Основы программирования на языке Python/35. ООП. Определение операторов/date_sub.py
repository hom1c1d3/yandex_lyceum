import datetime


class Date:

    def __init__(self, month, day):
        self.date = datetime.datetime(1981, month, day)  # 1981 первый невисокосный год с эпохи

    def __sub__(self, other):
        return (self.date - other.date).days

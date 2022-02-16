from datetime import datetime


class AmericanDate:

    def __init__(self, *args):
        self.date = datetime(*args[:3])

    def set_year(self, value):
        self.date = self.date.replace(year=value)

    def set_month(self, value):
        self.date = self.date.replace(month=value)

    def set_day(self, value):
        self.date = self.date.replace(day=value)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def format(self):
        return self.date.strftime('%m.%d.%Y')


class EuropeanDate(AmericanDate):

    def format(self):
        return self.date.strftime('%d.%m.%Y')


american = AmericanDate(2000, 9, 3)
european = EuropeanDate(2000, 9, 3)
print(american.format())
print(european.format())
american.set_year(2012)
print(american.get_month())
print(american.format())
print(european.format())
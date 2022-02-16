from itertools import zip_longest


class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __getitem__(self, item):
        return self.coefficients[item]

    def __len__(self):
        return len(self.coefficients)

    def __call__(self, x):
        return sum(i * x ** ind for ind, i in enumerate(self.coefficients))

    def __add__(self, other):
        coefficients = list(map(sum, zip_longest(self, other, fillvalue=0)))
        return Polynomial(coefficients)

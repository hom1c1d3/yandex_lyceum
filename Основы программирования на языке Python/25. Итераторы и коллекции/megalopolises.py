import sys
import itertools


def get_intervals(number):
    number //= 100000
    number *= 100
    return number, number + 100


cities = [i.split()[::2] for i in sys.stdin.readlines()]
cities = [(a, int(b)) for a, b in cities]
cities = sorted(((a, get_intervals(b)) for a, b in cities), key=lambda x: x[1])
grouper = itertools.groupby(cities, lambda x: x[1])
res = [(k, sorted(g)) for k, g in grouper]
res = [f"{' - '.join(map(str, k))}: {', '.join(map(lambda x: x[0], g))}" for k, g in res]
print(*res, sep='\n')
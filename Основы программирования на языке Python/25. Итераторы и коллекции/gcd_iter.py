import math
import functools
import sys


numbers = (int(i) for i in sys.stdin.readlines())
res = functools.reduce(math.gcd, numbers)
print(res)
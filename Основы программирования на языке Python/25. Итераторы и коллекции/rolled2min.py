import functools
import sys


text = (i.strip() for i in sys.stdin.readlines())
print(functools.reduce(lambda a, b: a if a < b else b, text))
import time


def cached(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            res = func(*args)
            cache[args] = res
            return res
    return wrapper

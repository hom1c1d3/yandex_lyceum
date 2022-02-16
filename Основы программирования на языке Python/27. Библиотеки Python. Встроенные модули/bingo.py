import random


def make_bingo():
    sample = random.sample(range(1, 76), 25)
    sample[12] = 0
    return tuple(tuple(i) for i in (sample[j*5:j*5+5] for j in range(5)))

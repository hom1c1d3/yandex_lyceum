import random
from math import hypot


def rand_coord(stop):
    x = 0
    while x < stop:
        yield random.randint(0, stop), random.randint(0, stop)
        x += 1


def get_close_pi(accuracy):
    count = 0
    for a, b in rand_coord(accuracy):
        if round(hypot(a, b), accuracy) <= accuracy:
            count += 1
    return 4 * (count / accuracy)


if __name__ == '__main__':
    # get_close_pi(100000000) => 3.14171268
    print(get_close_pi(100))

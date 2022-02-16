import random
import sys


def make_pairs(people):
    rand_people = random.sample(people, len(people))
    while set(enumerate(people)) & set(enumerate(rand_people)):
        rand_people = random.sample(people, len(people))
    return tuple(zip(people, rand_people))


students = [i.strip() for i in sys.stdin.readlines()]
res = make_pairs(students)
print(*(' - '.join(i) for i in res), sep='\n')
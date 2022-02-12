import sys


def ismagic(table):
    return all([sum(a) == sum(b) for a, b in zip(table, zip(*table))])


def main():
    table = [list(map(int, i.split())) for i in sys.stdin.readlines()]
    res = ismagic(table)
    print('YES' if res else 'NO')


main()
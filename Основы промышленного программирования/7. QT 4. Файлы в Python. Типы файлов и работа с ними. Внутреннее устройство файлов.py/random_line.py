import random


def rand_line(file):
    try:
        line = next(file)
    except StopIteration:
        return

    for ind, iline in enumerate(file, 2):
        if random.randrange(line):
            continue
        line = iline

    return line


def main():
    with open('lines.txt', 'r', encoding='utf8') as f:
        res = rand_line(f)
        if res is not None:
            print(res)


if __name__ == '__main__':
    main()
import sys


def parse_args():
    args = sys.argv[1], sys.argv[2]
    args = [int(i) for i in args]
    return args


def main():
    try:
        res = sum(parse_args())
    except (IndexError, ValueError):
        print(0)
    else:
        print(res)


if __name__ == '__main__':
    main()
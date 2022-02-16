import sys


def parse_args():
    args = sys.argv[1:]
    if not args:
        return None
    args = [int(i) for i in args]
    return args


def main():
    try:
        args = parse_args()
    except (IndexError, ValueError) as e:
        print(e.__class__.__name__)
    else:
        if args is None:
            print('NO PARAMS')
        res = 0
        k = 1
        for i in args:
            res += k * i
            k = -k
        print(res)


if __name__ == '__main__':
    main()

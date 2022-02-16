import sys
from statistics import mean


def parse_args():
    args = sys.argv[1:]
    args = [int(i) for i in args]
    return args


def main():
    try:
        nums = parse_args()
        sm = sum(nums)
        mn = mean(nums)
    except IndexError:
        print(0)
    else:
        print('Сумма', sm)
        print('Среднее', mn)


if __name__ == '__main__':
    main()
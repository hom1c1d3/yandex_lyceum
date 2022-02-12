import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', nargs='*')
    args = parser.parse_args()
    nums = args.numbers
    if len(nums) > 2:
        print('TOO MANY PARAMS')
        return 1
    elif len(nums) == 1:
        print('TOO FEW PARAMS')
        return 1
    elif not nums:
        print('NO PARAMS')
        return 1
    try:
        nums = [int(i) for i in nums]
    except Exception as e:
        print(e.__class__.__name__)
        return 1
    print(sum(nums))


if __name__ == '__main__':
    main()
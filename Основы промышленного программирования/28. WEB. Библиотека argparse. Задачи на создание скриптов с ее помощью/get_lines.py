import argparse
import os


def count_lines(file_name):
    if not os.path.exists(file_name):
        return 0
    num_lines = sum(1 for _ in open(file_name))
    return num_lines


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--file')
    args = parser.parse_args()
    file_name = args.file
    if file_name is None:
        print(0)
        return
    if not os.path.exists(file_name):
        print(0)
        return
    num_lines = count_lines(file_name)
    print(num_lines)


if __name__ == '__main__':
    main()
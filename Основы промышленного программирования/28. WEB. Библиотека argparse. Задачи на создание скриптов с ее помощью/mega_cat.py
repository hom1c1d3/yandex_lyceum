import argparse


def get_file_lines(file_name):
    with open(file_name, 'r', encoding='utf8') as fd:
        data = fd.read()
    lines = data.splitlines()
    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', action='store_true')
    parser.add_argument('--num', action='store_true')
    parser.add_argument('--sort', action='store_true')
    parser.add_argument('file_name')
    args = parser.parse_args()
    is_count = args.count
    is_num = args.num
    is_sort = args.sort
    file_name = args.file_name
    if file_name is None:
        print('ERROR')
        return 1
    try:
        lines = get_file_lines(file_name)
    except FileNotFoundError:
        print('ERROR')
        return 1
    if is_sort:
        lines = sorted(lines)
    for ind, i in enumerate(lines):
        if is_num:
            print(ind, end=' ')
        print(i)
    if is_count:
        print(f'rows count: {len(lines)}')
    return 0


if __name__ == '__main__':
    main()
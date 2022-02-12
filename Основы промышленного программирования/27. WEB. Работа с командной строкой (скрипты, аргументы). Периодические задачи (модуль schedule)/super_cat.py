import sys


def get_file_lines(file_name):
    with open(file_name, 'r', encoding='utf8') as fd:
        data = fd.read()
    lines = data.splitlines()
    return lines


def main():
    args = sys.argv[1:]
    is_count = False
    is_num = False
    is_sort = False
    file_name = None
    for arg in args:
        if '--count' == arg:
            is_count = True
        elif '--num' == arg:
            is_num = True
        elif '--sort' == arg:
            is_sort = True
        else:
            file_name = arg
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
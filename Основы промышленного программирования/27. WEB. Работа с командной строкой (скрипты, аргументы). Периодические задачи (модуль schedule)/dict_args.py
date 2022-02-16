import sys


def main():
    args = sys.argv[1:]
    if '--sort' in args:
        sort = True
        args = filter(lambda x: x != '--sort', args)
    else:
        sort = False
    dict_args = (i.split('=', 1) for i in args)
    dict_args = {k: v for k, v in dict_args}
    res = list(dict_args.items())
    if sort:
        res = sorted(res, key=lambda x: x[0])
    for k, v in res:
        print(f"Key: {k} Value: {v}")


if __name__ == '__main__':
    main()

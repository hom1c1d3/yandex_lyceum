import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sort', action='store_true')
    parser.add_argument('args', nargs='*')
    args = parser.parse_args()
    sort = args.sort
    args = args.args
    dict_args = (i.split('=', 1) for i in args)
    dict_args = {k: v for k, v in dict_args}
    res = list(dict_args.items())
    if sort:
        res = sorted(res, key=lambda x: x[0])
    for k, v in res:
        print(f"Key: {k} Value: {v}")


if __name__ == '__main__':
    main()

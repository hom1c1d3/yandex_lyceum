import argparse

parser = argparse.ArgumentParser()

parser.add_argument('arg', nargs='*')
args = parser.parse_args()
if args.arg:
    print(*args.arg, sep='\n')
else:
    print('no args')
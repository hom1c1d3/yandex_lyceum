import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('integers', metavar='integers', nargs='+', type=int, help="integers to be converted")
parser.add_argument('--base', default=2, type=int, help="numeric system base")
parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'), help="the file to write converted result")
args = parser.parse_args()
try:
    s = ' '.join(str(int(str(i), args.base)) for i in args.integers)
except ValueError as e:
    raise argparse.ArgumentError(args.integers, message=e.args[0])
args.log.write(s + '\n')
args.log.close()

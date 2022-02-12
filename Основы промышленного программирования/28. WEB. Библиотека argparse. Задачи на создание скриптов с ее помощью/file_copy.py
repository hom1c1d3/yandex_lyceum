import argparse


parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('destination')
parser.add_argument('--upper', action='store_true')
parser.add_argument('--lines', type=int)

args = parser.parse_args()

source_file_name = args.source
dest_file_name = args.destination


with open(source_file_name, 'r') as fd:
    lines = fd.readlines()
    lines = lines[slice(None, args.lines)]


if args.upper:
    lines = [i.upper() for i in lines]


with open(dest_file_name, 'w') as fd:
    for line in lines:
        fd.write(line)
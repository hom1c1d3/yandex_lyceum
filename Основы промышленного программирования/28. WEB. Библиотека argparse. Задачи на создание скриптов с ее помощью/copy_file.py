import argparse


parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('destination')
parser.add_argument('--upper', action='store_true')
parser.add_argument('--lines', type=int)

args = parser.parse_args()

source_file_name = args.source
dest_file_name = args.destination


with open(source_file_name, 'r', encoding='utf8') as fd:
    lines = fd.read()
    lines = lines.splitlines()
    lines = lines[slice(None, args.lines)]


if args.upper:
    lines = [i.upper() for i in lines]


with open(dest_file_name, 'w', encoding='utf8') as fd:
    for line in lines:
        fd.write(line + '\n')

if args.lines is None and not args.upper:
    print(lines)
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('arg1')
args = parser.parse_args()
print(args.arg1)
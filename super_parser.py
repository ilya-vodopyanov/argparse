import argparse

parser = argparse.ArgumentParser()
parser.add_argument("arg", nargs="*", type=str, default=['no args'])

args = parser.parse_args()
print(*args.arg, sep='\n')
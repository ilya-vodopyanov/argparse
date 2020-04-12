import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--num", action="store_true")
parser.add_argument("--count", action="store_true")
parser.add_argument("--sort", action="store_true")
parser.add_argument("file")

args = parser.parse_args()

try:
    fn = args.file
    with open(fn) as file:
        lines = list(line.strip() for line in file.readlines())
except FileNotFoundError:
    print('ERROR')
    exit(1)
if args.sort:
    lines.sort()
if args.num:
    lines = list(str(n) + ' ' + line for n, line in enumerate(lines))
print(*lines, sep='\n')
if args.count:
    print(f'rows count: {len(lines)}')
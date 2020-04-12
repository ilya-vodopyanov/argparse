import argparse


parser = argparse.ArgumentParser()
parser.add_argument("params", nargs="*")
parser.add_argument("--sort", action="store_true", default=False)

args = parser.parse_args()
items = {i.split('=')[0]: i.split('=')[1] for i in args.params}
items = list(f'Key: {key}\tValue: {value}' for key, value in items.items())
if args.sort:
    items.sort(key=lambda x: x.split(":")[1])

print(*items, sep='\n')
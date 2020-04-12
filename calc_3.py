import argparse


parser = argparse.ArgumentParser()
parser.add_argument("params", nargs="*")

numbers = parser.parse_args().params
try:
    numbers = list(int(n) for n in numbers)
except Exception as e:
    print(e.__class__.__name__)
    exit(1)

if len(numbers) > 2:
    print('TOO MUCH PARAMS')
elif len(numbers) == 1:
    print('TOO FEW PARAMS')
elif not len(numbers):
    print('NO PARAMS')
else:
    print(sum(numbers))
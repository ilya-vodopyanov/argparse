import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--per-day', type=int, default=0)
parser.add_argument('--per-week', type=int, default=0)
parser.add_argument('--per-month', type=int, default=0)
parser.add_argument('--per-year', type=int, default=0)
parser.add_argument('--get-by', choices=['day', 'month', 'year'], default='day')

args = parser.parse_args()
profit = args.per_day
profit += args.per_week / 7
profit += args.per_month / 30
profit += args.per_year / 360

if args.get_by == 'day':
    print(int(profit))
elif args.get_by == 'week':
    print(int(profit * 7))
elif args.get_by == 'month':
    print(int(profit * 30))
elif args.get_by == 'year':
    print(int(profit * 360))
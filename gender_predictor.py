import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--barbie", type=int, default=50)
parser.add_argument("--cars", type=int, default=50)
parser.add_argument("--movie", default="other")

scores = {"melodrama": 0, "football": 100}

args = parser.parse_args()
barbie = args.barbie if 0 <= args.barbie <= 100 else 50
car = args.cars if 0 <= args.cars <= 100 else 50
movie = scores.get(args.movie, 50)

boy = (100 - barbie + car + movie) // 3
print(f"boy: {boy}\ngirl: {100 - boy}")
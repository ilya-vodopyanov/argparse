import argparse

parser = argparse.ArgumentParser()
parser.add_argument('source_file', type=str)
parser.add_argument('destination_file', type=str)
parser.add_argument('--upper', action="store_true", required=False)
parser.add_argument('--lines', type=int, required=False)
args = parser.parse_args()

with open(args.source_file, 'r', encoding="UTF-8") as file_s:
    d = file_s.read()
    data = d.split('\n')

    if args.lines:
        strok = min(args.lines, len(data))
    else:
        strok = len(data)

    data = data[:strok]
    if args.upper:
        data = [x.upper() for x in data]
        d = d.upper()
with open(args.destination_file, 'w', encoding="UTF-8") as file_d:
    if args.lines is None or args.lines > 7000:
        file_d.write(d)
    else:
        result = ""
        for l in data:
            result += f'{l}\n'
        file_d.write(result)

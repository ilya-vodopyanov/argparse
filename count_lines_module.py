import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')

    fn = parser.parse_args().file
    print(count_lines(fn))


def count_lines(fname):
    try:
        with open(fname) as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0


if __name__ == '__main__':
    main()
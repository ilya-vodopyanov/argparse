import argparse


def print_error(message):
    print(f"ERROR: {message}!!")


def main():
    print('Welcome to my program')

    parser = argparse.ArgumentParser()
    parser.add_argument('message')

    message = parser.parse_args().message
    print_error(message)


if __name__ == '__main__':
    main()
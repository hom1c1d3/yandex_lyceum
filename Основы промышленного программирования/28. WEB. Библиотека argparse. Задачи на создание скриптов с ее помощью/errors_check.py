import argparse


def print_error(message):
    print(f'ERROR: {message}!!')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    args = parser.parse_args()
    message = args.message
    print('Welcome to my program')
    print_error(message)


if __name__ == '__main__':
    main()
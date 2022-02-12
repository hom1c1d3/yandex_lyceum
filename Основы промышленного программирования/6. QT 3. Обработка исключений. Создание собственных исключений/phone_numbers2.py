class NumberFormatError(Exception):
    pass


class NumberLengthError(Exception):
    pass


def solve_number(number):
    number = ''.join(number.split())
    if number.startswith('+'):
        if number[:2] != '+7':
            raise NumberLengthError
        number = '+7' + number[2:]
    elif number.startswith('8'):
        number = '+7' + number[1:]
    else:
        raise NumberLengthError

    open_bracket_count = number.count('(')
    closing_bracket_count = number.count(')')
    if open_bracket_count == 1 and closing_bracket_count == 1:
        number = number.replace('(', '').replace(')', '')

    dash_split = number.split('-')
    if not all(dash_split):
        raise NumberLengthError
    else:
        number = ''.join(dash_split)

    if not all(i.isnumeric() for i in number[2:]):
        raise NumberLengthError

    if len(number) != 12:
        raise NumberLengthError

    return number


number = input()

try:
    print(solve_number(number))
except (NumberFormatError, NumberLengthError):
    print('error')

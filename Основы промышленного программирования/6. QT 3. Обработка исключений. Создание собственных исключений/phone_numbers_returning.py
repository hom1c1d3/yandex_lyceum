class NumberFormatError(Exception):
    def __init__(self, message=None):
        message = message if message is not None else 'неверный формат'
        super().__init__(message)


class NumberLengthError(Exception):
    def __init__(self, message=None):
        message = message if message is not None else 'неверное количество цифр'
        super().__init__(message)


def solve_number(number):
    number = ''.join(number.split())
    if number.startswith('+'):
        if number[:2] != '+7':
            raise NumberFormatError
        number = '+7' + number[2:]
    elif number.startswith('8'):
        number = '+7' + number[1:]
    else:
        raise NumberFormatError

    open_bracket_count = number.count('(')
    closing_bracket_count = number.count(')')
    if open_bracket_count == 1 and closing_bracket_count == 1:
        number = number.replace('(', '').replace(')', '')

    dash_split = number.split('-')
    if not all(dash_split):
        raise NumberFormatError
    else:
        number = ''.join(dash_split)

    if not all(i.isnumeric() for i in number[2:]):
        raise NumberFormatError

    if len(number) != 12:
        raise NumberLengthError

    return number


number = input()

try:
    print(solve_number(number))
except (NumberFormatError, NumberLengthError) as e:
    print(e)

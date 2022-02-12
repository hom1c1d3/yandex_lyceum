class NumberError(Exception):
    pass


class NumberFormatError(NumberError):
    def __init__(self, message=None):
        message = message if message is not None else 'неверный формат'
        super().__init__(message)


class NumberLengthError(NumberError):
    def __init__(self, message=None):
        message = message if message is not None else 'неверное количество цифр'
        super().__init__(message)


class MobileOperatorError(NumberError):
    def __init__(self, message=None):
        message = message if message is not None else 'не определяется оператор сотовой связи'
        super().__init__(message)


class CountryCodeError(NumberError):
    def __init__(self, message=None):
        message = message if message is not None else 'не определяется код страны'
        super().__init__(message)


def solve_number(number):
    mobile_operators = ((*range(910, 919 + 1), *range(980, 989 + 1)),
                        (*range(920, 939 + 1),),
                        (*range(902, 906 + 1), *range(960, 969 + 1)))
    country_code = ('8', '+7', '+359', '+55', '+1')
    number = ''.join(number.split())

    open_bracket_count = number.count('(')
    closing_bracket_count = number.count(')')
    if open_bracket_count or closing_bracket_count:
        if open_bracket_count == 1 and closing_bracket_count == 1:
            number = number.replace('(', '').replace(')', '')
        else:
            raise NumberFormatError

    dash_split = number.split('-')
    if not all(dash_split):
        raise NumberFormatError
    else:
        number = ''.join(dash_split)

    if not all(i.isnumeric() for i in number.replace('+', '')):
        raise NumberFormatError

    is_country_code_not_found = True
    for i in country_code:
        if number.startswith(i):
            if i == '8':
                number = '+7' + number[1:]
            is_country_code_not_found = False
            break

    if len(number) < 12:
        raise NumberLengthError

    if is_country_code_not_found:
        raise CountryCodeError

    if number.startswith('+7'):
        if not any(number[2:5] == str(three_number) for operator_numbers in mobile_operators
                   for three_number in operator_numbers):
            raise MobileOperatorError

    return number


number = input()

try:
    print(solve_number(number))
except NumberError as e:
    print(e)

def is_correct_mobile_phone_ru(number):
    number = ''.join(number.split())
    if number.startswith('+'):
        if number[:2] != '+7':
            return False
        number = '+7' + number[2:]
    elif number.startswith('8'):
        number = '+7' + number[1:]
    else:
        return False

    open_bracket_count = number.count('(')
    closing_bracket_count = number.count(')')
    if open_bracket_count == 1 and closing_bracket_count == 1:
        if number.index(')') - number.index('(') != 4:
            return False
        number = number.replace('(', '').replace(')', '')
    elif open_bracket_count != 0 or closing_bracket_count != 0:
        return False

    dash_split = number.split('-')
    if not all(dash_split):
        return False
    else:
        number = ''.join(dash_split)

    if not all(i.isnumeric() for i in number[2:]):
        return False

    if len(number) != 12:
        return False

    return True


if __name__ == '__main__':
    res = is_correct_mobile_phone_ru(input())
    if res:
        print('YES')
    else:
        print('NO')

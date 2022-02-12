number = input()

number = ''.join(number.split())
if number.startswith('+'):
    if number[:2] != '+7':
        print('error')
        exit()
    number = '+7' + number[2:]
elif number.startswith('8'):
    number = '+7' + number[1:]
else:
    print('error')
    exit()

open_bracket_count = number.count('(')
closing_bracket_count = number.count(')')
if open_bracket_count == 1 and closing_bracket_count == 1:
    number = number.replace('(', '').replace(')', '')

dash_split = number.split('-')
if not all(dash_split):
    print('error')
    exit()
else:
    number = ''.join(dash_split)

if not all(i.isnumeric() for i in number[2:]):
    print('error')
    exit()

if len(number) != 12:
    print('error')
    exit()

print(number)
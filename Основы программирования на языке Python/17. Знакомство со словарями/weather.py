current = input()
bright = float(input())
dull = float(input())
days = int(input())

if current == 'ясно':
    second = 1 - bright
    if bright ** days > second * dull ** (days - 1):
        print('ясно')
        print(bright ** days)
    elif bright ** days == second * dull ** (days - 1):
        print('равновероятно')
        print(bright ** days)
    else:
        print('пасмурно')
        print(second * dull ** (days - 1))
elif current == 'пасмурно':
    second = 1 - dull
    if dull ** days > second * bright ** (days - 1):
        print('пасмурно')
        print(dull ** days)
    elif dull ** days == second * bright ** (days - 1):
        print('равновероятно')
        print(dull ** days)
    else:
        print('ясно')
        print(second * bright ** (days - 1))
def factorial(n):
    if n < 0:
        raise ValueError
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


while True:
    a = int(input())
    symbol = input()
    if symbol == 'x':
        print(a)
        break
    if symbol == '!':
        try:
            factorial(a)
            continue
        except ValueError:
            continue
    b = int(input())

    try:
        eval(f'{a} {symbol} {b}')
    except ZeroDivisionError:
        continue

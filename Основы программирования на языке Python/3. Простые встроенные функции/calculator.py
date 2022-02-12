signs = '+-*/'
num1 = int(input())
num2 = int(input())
sign = input()

if sign in signs:
    try:
        print(eval(f"{num1} {sign} {num2}"))
    except ZeroDivisionError:
        print(888888)
else:
    print("888888")

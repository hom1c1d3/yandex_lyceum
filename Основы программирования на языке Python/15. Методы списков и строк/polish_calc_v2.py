exp = input().split()
simple = ('+', '-', '*', '/')


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


while len(exp) > 1:
    for ind, i in enumerate(exp):
        if i in simple:
            a, b = exp[ind - 2:ind]
            calc = eval(f'{a} {"//" if i == "/" else i} {b}')
            exp[ind - 2:ind + 1] = [calc]
            break
        elif i == '~':
            calc = - int(exp[ind - 1])
            exp[ind - 1:ind + 1] = [calc]
            break
        elif i == '!':
            calc = factorial(int(exp[ind - 1]))
            exp[ind - 1:ind + 1] = [calc]
            break
        elif i == '#':
            calc = [exp[ind - 1]] * 2
            exp[ind - 1:ind + 1] = calc
            break
        elif i == '@':
            a, b, c = exp[ind - 3:ind]
            calc = [b, c, a]
            exp[ind - 3:ind + 1] = calc
            break
        else:
            exit('WTF is that?')
print(*exp)

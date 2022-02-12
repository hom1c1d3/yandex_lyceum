signs = ('+', '*', '-')
exp = input().split()

while len(exp) > 1:

    for ind, i in enumerate(exp):
        if i in signs:
            a, b = exp[ind - 2:ind]
            calc = eval(f'{a} {i} {b}')
            exp[ind - 2:ind + 1] = [calc]
            break
print(*exp)
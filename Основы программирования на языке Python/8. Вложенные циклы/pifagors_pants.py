n = int(input())

res = ""
first, second, third = 0, 0, 0
for c in range(2, n + 1):
    for a in range(c - 1, c // 2 - 1, -1):
        b = round((c ** 2 - a ** 2) ** .5)
        if c ** 2 == a ** 2 + b ** 2:
            a, b, c = tuple(sorted((a, b, c)))
            num1, num2, num3 = a, b, c
            while num2:
                num1, num2 = num2, num1 % num2
                while num3:
                    num1, num3 = num3, num1 % num3
            if num1 > 1:
                continue
            if (a, b, c) == (first, second, third):
                continue
            first, second, third = a, b, c
            res += str(a) + ' ' + str(b) + ' ' + str(c) + '\n'

print(res)

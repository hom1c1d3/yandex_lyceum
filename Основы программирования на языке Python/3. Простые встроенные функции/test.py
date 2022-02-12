city1 = input()
city2 = input()
city_last = {"Тула", "Пенза"}

if city1 != city2 and city_last != {city1, city2} and (city1 == 'Тула' or
                                                      city2 == 'Пенза'):
    print("ДА")
else:
    print("НЕТ")


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(9))


num = float(input())

if -0.000001 < num < 0.000001:
    print(1000000)
else:
    print(num**-1)


print('\n'.join(sorted((input(), input(), input()), key=int, reverse=True)))


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


num = int(input())
num_list = list(map(int, str(num)))
half_sum = (max(num_list) + min(num_list)) / 2
last_num = num_list[num_list.index(
    list(
        (set(
            num_list) - {max(num_list), min(num_list)}))[0])]
if half_sum == last_num:
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")


num = int(input())
a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10

# ставим на первое место минимальное число кроме 0
if a > b and b:
    a, b = b, a
if a > c and c:
    a, c = c, a
if a > d and d:
    a, d = d, a
# сортируем оставшиеся три числа в порядке возрастания
if b > d:
    b, d = d, b
if b > c:
    b, c = c, d
if c > d:
    c, d = d, c

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

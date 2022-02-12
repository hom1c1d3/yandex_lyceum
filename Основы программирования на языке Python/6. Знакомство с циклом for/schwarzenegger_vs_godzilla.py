# идея в том, чтобы просто перемножить все знаменатели

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


numerator = 0
denominator = 1

for _ in range(int(input())):
    user_numerator, user_denominator = int(input()), int(input())
    numerator = numerator * user_denominator + user_numerator * denominator
    denominator *= user_denominator
nod = gcd(numerator, denominator)
numerator, denominator = numerator / nod, denominator / nod

print(f"{int(numerator)}/{int(denominator)}")

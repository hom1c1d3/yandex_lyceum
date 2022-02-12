num = input()

while num[0] != '1' and int(num) < 10**9:
    num = str(int(num) * int(num[0]))

print(num)
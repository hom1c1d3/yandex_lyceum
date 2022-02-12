n = int(input())
num_place_digits = 9
num_digits, max_num_digits = 1, 0
while num_digits * num_place_digits < n:
    n -= num_place_digits * num_digits
    num_digits += 1
    num_place_digits = 10 * num_place_digits
if num_digits - 1:
    max_num_digits = int('9' * (num_digits - 1))
res = n // num_digits + max_num_digits
print(res)

def get_sum_divisors(number):
    return sum(x for x in range(1, number // 2 + 1) if number % x == 0)


pairs = {}
for i in range(2, 10001):
    sum_div = get_sum_divisors(i)
    if sum_div != 1:  # если не простое
        if i in pairs:
            n1, n2 = i, pairs[i]  # нам нужно проверить евляется ли сумма делителей суммы
            # текущего числа ровна текущему
            if (n1 // n2) and (get_sum_divisors(n1) == n2):
                print(*sorted([n2, n1]))
        else:
            pairs[sum_div] = i
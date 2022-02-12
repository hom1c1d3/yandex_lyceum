def is_prime(n):
    try:
        int(n)
    except ValueError:
        return False
    if n != str(int(n)):
        return False
    n = int(n)
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


if __name__ == '__main__':
    res = is_prime(input())
    if res:
        print('YES')
    else:
        print('NO')
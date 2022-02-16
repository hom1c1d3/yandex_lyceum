def tribonacci(n):
    if n < 2:
        return 0
    if 0 < n <= 3:
        return 1
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

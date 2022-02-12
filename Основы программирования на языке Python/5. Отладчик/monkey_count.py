def count_monkey_moves(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        count += 1
    return count


if __name__ == '__main__':
    number = int(input())
    print(count_monkey_moves(number))

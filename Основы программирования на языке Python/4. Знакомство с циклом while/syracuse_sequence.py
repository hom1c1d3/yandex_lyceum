def syracuse(n):
    hail = [n]
    while True:
        if len(hail) > 1 and n == 1 or n == 0:
            break
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        hail.append(int(n))
    return hail


if __name__ == '__main__':
    num = int(input())
    if num > 1:
        print(len(syracuse(num)[1:]))
    else:
        print(0)

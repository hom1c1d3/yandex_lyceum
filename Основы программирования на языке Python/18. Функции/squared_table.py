def trange(start, stop):
    st = start
    sp = start + 9
    while sp <= stop:
        yield range(st, sp + 1)
        st += 10
        sp += 10
    yield range(st, stop + 1)


def squared(a, b, k):
    for i in trange(a, b):
        for j in i:
            num = j ** 2
            if num % k:
                print(f'{num:<4}', end=' ')
        print()


squared(11, 99, 10)
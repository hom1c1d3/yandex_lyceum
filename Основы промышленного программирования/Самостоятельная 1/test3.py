class NotEnoughError(Exception):
    ...


def stubbornness(*args):
    res = []
    for i in args:
        if len(i) < 2:
            raise NotEnoughError('Not enough values')
        first = i[0]
        max_other = max(i[1:])
        min_other = min(i[1:])
        if 0 in (max_other, min_other):
            raise ZeroDivisionError('Cannot be divided by zero')
        if ((first % max_other == 0) and
                (first % min_other == 0)):
            res.append(first)

    res = sorted(set(res))
    if not res:
        raise IndexError('Empty Return Error')
    return res

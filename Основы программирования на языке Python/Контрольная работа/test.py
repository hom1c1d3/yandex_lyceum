punct = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
nums = set(map(str, range(0, 10)))

first = input().split(' ')
second = input().lower().split('$$')
third = input().lower().split(')(')

for i in first:
    fil_sec = list(filter(lambda a: len(set(a) - set(i)) > 2, second))
    sor_sec = sorted(list(map(lambda a: a.lower(), fil_sec)) + [i.lower()])
    fil_sec = list(filter(lambda a: a in sor_sec[:sor_sec.index(i.lower())], fil_sec))
    fil_sec = map(lambda a: a.upper(), fil_sec)
    fil_sec = ' - '.join(fil_sec)
    fil_thd = filter(lambda a: set(a) & punct or set(a) & nums, third)
    fil_thd = filter(lambda a: len(a) < len(i), fil_thd)
    fil_thd = f' {i[2].upper()} '.join(fil_thd)
    print(f'{i}:')
    print(fil_sec)
    print(fil_thd)
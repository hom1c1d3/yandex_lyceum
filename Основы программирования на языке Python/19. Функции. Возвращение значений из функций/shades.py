def make_shades(alley, k):
    alley = alley[::(k // abs(k)) if k else 1]
    res = [False] * len(alley)
    shades = []
    for ind, i in enumerate(alley):
        if i:
            shades.extend(list(range(ind, ind + i * abs(k) + 1)))
        if ind in shades:
            res[ind] = True
    res = res[::(k // abs(k)) if k else 1]
    return res


def calculate_sunny_length(shades):
    shades = list(filter(lambda x: not x, shades))
    return len(shades)


def main():
    k = int(input())
    alley = list(map(int, input().split()))
    shades = make_shades(alley, k)
    non_shades_len = calculate_sunny_length(shades)
    if non_shades_len < 10:
        print('Тени достаточно')
    else:
        print('Обгорел')

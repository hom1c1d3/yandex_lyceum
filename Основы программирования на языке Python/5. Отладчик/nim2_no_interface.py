# Источники вдохновения:
# https://informatics.mccme.ru/mod/page/view.php?id=19149
# https://ru.wikipedia.org/wiki/%D0%9D%D0%B8%D0%BC_(%D0%B8%D0%B3%D1%80%D0%B0)


from functools import reduce, partial
from operator import itemgetter, xor  # xor(n, m) тоже самое, что n^m

xor_sum = partial(reduce, xor)  # сравнивает каждой двоичный разряд из переданных, если разные


# то 1, если одинаковые то 0, потом записывает результат сравнения под каждым разрядом и получаем
# двоичное число, но функция xor возвращант сразу десятичное


def max_from_tuple(tupl):
    """
    Находит первое значение из подкортежей в кортеже и возвращает целое двоичное число ДО найденного
     и само найденное

    :param tupl: кортеж с найденным числом, Целое двоичное число,
     из которого была найдена подстрока
    :return: [целое двоичное число ДО найденного, максиммальное найденное]
    """
    res_num, res_num_origin = list(sorted(tupl, key=lambda a: a[0][0]))[-1]
    return [res_num_origin[::-1][len(res_num):][::-1], res_num]


def nflon(iterable, num):
    """
    Numbers_From_Len_Of_Num
     Для каждого числа iterable функция берет подстроку длиной двоичного num справа налево и
    возвращает (найденное число, целое число в двоичном формате из которго находилась подстрока})

    :param iterable: последовательность чисел.
    :param num: число чьей длиной в двоичном представлении будет искаться подстрока
     вкаждом числе последовательности с права налево
    :return: кортеж с
    (найденное число, целое число в двоичном формате из которго находилась подстрока)
    """
    bin_list = [bin(n)[2:] if n else '0' for n in iterable]
    nums_from_len_of_num = tuple((b[::-1][:len(bin(num)[2:])][::-1], b) for b in bin_list)

    return nums_from_len_of_num


def make_move(piles):
    """
    Подсчитывает такой шаг, чтобы xor самма всех кучек стала ровна нулю

    :param piles: кучки камней
    :return: (количество камней в кучке из которой мы будем брать, сколько камней взять)
    """
    xorsum_nums = xor_sum(piles)

    if xorsum_nums:
        bin_nums = nflon(piles, xorsum_nums)
        max_from_pile = max_from_tuple(bin_nums)
        if len(bin_nums) > 1:
            remain = sorted((int(i, 2) for i, _ in bin_nums), reverse=True)[1:]
            xorsum_remain = xor_sum(remain)
            from_origin_max = bin(xorsum_remain)[2:].zfill(len(max_from_pile[1]))
            res_pile = int(''.join(max_from_pile), 2)
            move = res_pile - (int(max_from_pile[0] + from_origin_max, 2))

        else:
            res_pile = piles[0]
            move = res_pile

        return res_pile, move
    else:
        return max(piles), 1


def main():
    num_piles = 3
    piles = [int(input()) for _ in range(num_piles)]

    while any(piles):
        from_pile, computer_move = make_move(piles)
        pile_num = piles.index(from_pile)
        piles[pile_num] -= computer_move
        print(pile_num + 1, computer_move, ' '.join(map(str, piles)))
        if not any(piles):
            print("ИИ выиграл!")
            break
        pile_num = int(input())
        user_move = int(input())
        true_piles_ind = (ind for ind, value in enumerate(piles))
        while (pile_num - 1 not in true_piles_ind
               or user_move > piles[pile_num - 1]
               or user_move < 1):
            print(f'Некорректный ход: {pile_num} {user_move}')
            pile_num = int(input())
            user_move = int(input())
            true_piles_ind = (ind for ind, value in enumerate(piles))
        piles[pile_num - 1] -= user_move
        print(pile_num, user_move, ' '.join(map(str, piles)))
        if not any(piles):
            print('Вы выиграли!')
            break


if __name__ == '__main__':
    main()

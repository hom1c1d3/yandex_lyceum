bad = {'борщ', 'сахар', 'пирожное', 'кока-кола', 'блины', 'пончики', 'печенье', 'крендельки', 'мед',
       'хлеб', 'картошка фри', 'сало', 'гамбургер', 'конфеты', 'колбаса', 'торт', 'пицца'}


def diet(dishes):
    dishes = dishes.split(', ')
    count = 0
    half = int(len(dishes) / 2)
    for dish in dishes:
        if dish in bad:
            count += 1
        if count > half:
            return 'Не ешь столько, По!'

    return 'Так держать, Воин Дракона!'


print(diet("печенье, чай, сахар, фрукты, мед"))

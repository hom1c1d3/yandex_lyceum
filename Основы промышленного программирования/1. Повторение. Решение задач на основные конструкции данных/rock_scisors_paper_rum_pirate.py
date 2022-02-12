win_positions = {  # ключ - кто, значение - кого побеждает
    'ножницы': ('бумага', 'ром'),
    'бумага': ('пират', 'камень'),
    'камень': ('ром', 'ножницы'),
    'ром': ('пират', 'бумага'),
    'пират': ('ножницы', 'камень'),
}

first_move, second_move = input(), input()
if first_move in win_positions[second_move]:  # если первый находится в кортеже побеждаемых второго
    print('второй')
elif second_move in win_positions[first_move]:
    print('первый')
else:
    print('ничья')

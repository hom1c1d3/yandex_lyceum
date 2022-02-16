first, second = input(), input()
players = ['камень', 'ножницы', 'бумага']
win_positions = list(zip(players, players[1:] + players[:1]))
variants = [set(i) for i in win_positions]
current_variant = {first, second}
if len(current_variant) == 1:
    print('ничья')
    exit()
current_position = win_positions[variants.index(current_variant)]
winner = current_position[0]  # первая позиция в паре - победитель
winner_ind = (first, second).index(winner)
if winner_ind == 0:
    print('первый')
else:
    print('второй')

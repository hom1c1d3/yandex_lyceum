coord = {'x': int(input()), 'y': int(input())}
current_cord = {'x': 0, "y": 0}
direction = ("север", "восток", "юг", "запад")
current_direction = "север"
min_moves_num = 0
move_direction = "стоп"

while current_cord != coord:
    current_direction = input().lower().replace("ё", "е")
    num_moves = int(input())
    # изменяем текущее местоположение
    # по X
    if current_direction in direction[::-2]:
        # смотрим какое движение по координатной плоскости, положительное или отрицательное
        # если положительное направление
        if current_direction in direction[:2]:
            current_cord["x"] += num_moves
        else:
            current_cord["x"] -= num_moves
    # по Y
    else:
        # смотрим какое движение по координатной плоскости, положительное или отрицательное
        # если положительное направление
        if current_direction in direction[:2]:
            current_cord["y"] += num_moves
        else:
            current_cord["y"] -= num_moves

    min_moves_num += 1
else:
    while move_direction != "стоп":
        try:
            move_direction = input().lower().replace("ё", "е")
        except EOFError:
            break
        if move_direction == "вперед":
            num_moves = int(input())

print(min_moves_num, sep="\n")

coord = {'x': int(input()), 'y': int(input())}
current_cord = {'x': 0, "y": 0}
direction = ("север", "восток", "юг", "запад")
current_direction = "север"
min_moves_num = 0
move_direction = "стоп"

while current_cord != coord:
    move_direction = input().lower().replace("ё", "е")
    if move_direction == "вперед":
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

    # изменение текущего направления вычесляется так: все направления записаны в кортеж по часовой
    # стрелке с права налево. Если мы хотим повернуть налево то мы будем двигаться от текущего
    # направления в обратную сторону по кортежу, т.е. индекс измениться на минус один
    elif move_direction == "налево":
        current_direction = direction[(direction.index(current_direction) - 1) % 4]
    elif move_direction == "направо":
        current_direction = direction[(direction.index(current_direction) + 1) % 4]
    elif move_direction == "разворот":
        current_direction = direction[(direction.index(current_direction) + 2) % 4]
    else:
        break

    min_moves_num += 1
else:
    while move_direction != "стоп":
        try:
            move_direction = input().lower().replace("ё", "е")
        except EOFError:
            break
        if move_direction == "вперед":
            num_moves = int(input())

print(min_moves_num, current_direction, sep="\n")

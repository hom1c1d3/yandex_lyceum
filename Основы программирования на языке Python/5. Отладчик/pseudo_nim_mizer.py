rock_num = int(input("Введите количество камней: "))
max_num_move = 3
print()

while rock_num:
    if rock_num == 1:
        remain = 1
    else:
        remain = (rock_num - 1) % (max_num_move + 1)
    if remain == 0:
        computer_move = max_num_move
    else:
        computer_move = remain
    rock_num -= computer_move
    print("Я взял ", computer_move, " камней")
    print("осталось ", rock_num, " камней")
    if rock_num == 0:
        print("Вы выиграли! Но только в этот раз... ")
        break
    print("Ваш ход")
    user_move = int(input("Какое количество вы возьмете? "))
    while user_move < 1 or user_move > max_num_move or user_move > rock_num:
        user_move = int(input("Вы ввели недопустимое значение, попробуйте еще раз: "))
    rock_num -= user_move
    print("Вы взяли: ", user_move, " камней")
    print("осталось ", rock_num, " камней")
    if rock_num == 0:
        print("Ха ха ха! Я победил, ты жалок!")
        break

print("Конец игры")

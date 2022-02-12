pile1 = int(input())
pile2 = int(input())

while pile1 or pile2:
    pile_num = int(input())
    move = int(input())
    if pile_num == 1:
        pile1 -= move
    else:
        pile2 -= move
    print(pile1, pile2)

pile1 = int(input())
pile2 = int(input())
pile3 = int(input())

while pile1 or pile2 or pile3:
    pile_num = int(input())
    move = int(input())
    if pile_num == 1:
        pile1 -= move
    elif pile_num == 2:
        pile2 -= move
    else:
        pile3 -= move
    print(pile1, pile2, pile3)

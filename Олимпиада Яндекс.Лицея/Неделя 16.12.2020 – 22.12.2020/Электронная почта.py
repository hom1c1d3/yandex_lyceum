blank = input()
blank = blank.partition('.')
blank = list(blank[0].partition('@') + blank[1:])
cards = list(input())
indexes = []

while not all(blank):
    card = cards.pop()
    if card == '@':
        if blank[1]:
            print('Impossible')
            indexes = []
            break
        indexes.append(len(blank[0]))
        blank[1] = '@'
    elif card == '.':
        if blank[2]:
            print('Impossible')
            indexes = []
            break
        indexes.append(len(''.join(blank[:3])))
        blank[3] = '.'
    else:
        letter_ind = blank[::2].index('' if '' in blank[::2] else blank[0]) * 2
        indexes.append(len(''.join(blank[:letter_ind])))
        blank[letter_ind] += card
if not indexes:
    if all(blank):
        print('Done')
else:
    print(*indexes)
    print(*blank, sep='')

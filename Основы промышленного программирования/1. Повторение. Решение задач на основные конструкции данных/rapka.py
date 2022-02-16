characters = input().split(' -> ')
for i in range(int(input())):
    current_character = input()
    character_ind = characters.index(current_character)
    res = []
    for j in range(character_ind - 1, character_ind + 2):
        if j not in range(len(characters)):
            continue
        res.append(characters[j])
    print(' -> '.join(res))

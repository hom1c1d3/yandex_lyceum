def str2coord(s):
    letters = 'ABCDEFGH'
    s = list(s)
    return letters.index(s[0]) + 1, int(s[1])


def coord2str(coord):
    letters = 'ABCDEFGH'
    return letters[coord[0] - 1] + str(coord[1])


def ispossible(coord):
    if isinstance(coord, str):
        coord = str2coord(coord)
    pos = range(1, 9)
    if coord[0] in pos and coord[1] in pos:
        return True
    return False


def get_turns(coord):
    if isinstance(coord, str):
        coord = str2coord(coord)

    delta_x = 1
    delta_y = 2
    for _ in range(2):
        x, y = coord
        for _ in range(2):
            yield x + delta_x, y + delta_y
            delta_x = -delta_x
        for _ in range(2):
            yield x + delta_x, y - delta_y
            delta_x = -delta_x
        delta_x, delta_y = delta_y, delta_x


def possible_turns(cell):
    turns = get_turns(cell)
    pos_turns = filter(ispossible, turns)
    pos_turns = map(coord2str, pos_turns)
    res = sorted(pos_turns)
    return res

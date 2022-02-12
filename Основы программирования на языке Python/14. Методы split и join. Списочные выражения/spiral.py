n = int(input('n please?') or 30)
character = input('char please?') or '*'

blank_line = ['   ' for _ in range(n)]
blank_canvas = [list(blank_line) for _ in range(n)]


def fill_canvas(coords):
    blank_canvas[coords[0]][coords[1]] = ' {} '.format(character)


row = int(n/2)
col = int(n/2)
fill_canvas((row, col))
n = 1
direction = 'left'
finished = False
while not finished:
    n += 1
    for _ in range(n):
        if direction == 'down':
            row += 1
        elif direction == 'right':
            col += 1
        elif direction == 'up':
            row -= 1
        elif direction == 'left':
            col -= 1
        try:
            fill_canvas((row, col))
        except IndexError:
            finished = True
    direction = {'left': 'up', 'up': 'right', 'right': 'down', 'down': 'left'}[direction]
for row in blank_canvas:
    print(''.join(row))

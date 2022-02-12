n = int(input())
symb = '*'

spiral_1d = [i for i in range(n, 0, -1)]
spiral_1d = [i + 1 if i in spiral_1d[::2][1:] else i for i in spiral_1d]
blank_line = [' ' for _ in range(n)]
blank_canvas = [blank_line[:] for _ in range(n)]

row = 0
col = n
pos_directions = ('left', 'down', 'right', 'up')
direction = 'left'
for i in spiral_1d:
    for j in range(i):
        if direction == 'down':
            row += 1
        elif direction == 'right':
            col += 1
        elif direction == 'up':
            row -= 1
        elif direction == 'left':
            col -= 1
        blank_canvas[row][col] = symb
    direction = pos_directions[(pos_directions.index(direction) + 1) % len(pos_directions)]

for r in blank_canvas:
    print(' '.join(r))

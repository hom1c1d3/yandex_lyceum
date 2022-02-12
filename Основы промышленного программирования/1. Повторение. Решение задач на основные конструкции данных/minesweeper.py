import random

EASY = (8, 10)
MEDIUM = (14, 18)
HARD = (20, 24)
BOMBS_COUNT = {EASY: 10, MEDIUM: 40, HARD: 99}


def create_field(size):
    """генирируем поле"""
    field = [[0 for _ in range(size[1])] for _ in range(size[0])]
    return field


def print_field(fld):
    cols_num = len(fld[0])
    print('   ', end='')
    for i in range(1, cols_num + 1):
        print(str(i).center(3), end='')
    print()
    for row_ind, i in enumerate(fld, 1):
        print(str(row_ind).ljust(3), end='')
        for j in i:
            if j == 0:
                print('[■]', end='')
            elif j == ' ':
                print('[ ]', end='')
            elif isinstance(j, int):
                print(f'[{j}]', end='')
            else:
                print(f'[{j}]', end='')
        print()


def is_coord_in_other_coord_buffer(coord, other_coord):
    if coord == other_coord:
        return False
    x0, y0 = other_coord
    x1, y1 = coord
    delta_x = abs(x0 - x1)
    delta_y = abs(y0 - y1)
    return delta_x in (0, 1) and delta_y in (0, 1)


def put_bomb(fld, coord):
    rows_num, cols_num = len(fld), len(fld[0])
    x, y = coord
    fld[x][y] = 'X'
    # в соседних клетках информацию увеличить на еденицу
    for i in range(rows_num):
        for j in range(cols_num):
            if is_coord_in_other_coord_buffer((i, j), (x, y)):
                try:
                    fld[i][j] += 1
                except TypeError:
                    pass
    return x, y


def mark_clear_by_near_cells(field, coord):
    """По соседним клеткам определяет, чистая ли она и рекурсивно продолжает с другими"""
    near_cells_coord = ((x, y) for x, i in enumerate(field) for y, j in enumerate(i)
                        if is_coord_in_other_coord_buffer((x, y), coord))
    near_cells_coord = [(x, y) for x, y in near_cells_coord if field[x][y] != ' ']
    if all(field[x][y] != 'X' for x, y in near_cells_coord):
        field[coord[0]][coord[1]] = ' '
        for i in near_cells_coord:
            mark_clear_by_near_cells(field, i)


def generate_field(size, first_move_coord):
    bombs_count = BOMBS_COUNT[size]
    field = create_field(size)
    for i in range(bombs_count):
        bomb_coord = random.randint(0, len(field) - 1), random.randint(0, len(field[0]) - 1)
        if not is_coord_in_other_coord_buffer(bomb_coord, first_move_coord):
            put_bomb(field, bomb_coord)
    mark_clear_by_near_cells(field, first_move_coord)
    return field


def add_clear_cells_to_user_field(field, user_field):
    clear_cells = [(x, y) for x, i in enumerate(field) for y, j in enumerate(i)
                   if j == ' ']
    number_cells = []
    for row_ind, row in enumerate(field):
        for col_ind, col in enumerate(row):
            near_cells = ((x, y) for x, i in enumerate(field) for y, j in enumerate(i)
                          if is_coord_in_other_coord_buffer((x, y), (row_ind, col_ind)))
            if any(j in clear_cells for j in near_cells):
                number_cells.append((row_ind, col_ind))
    showed_cells = clear_cells + number_cells
    for row_ind, row in enumerate(field):
        for col_ind, col in enumerate(row):
            if (row_ind, col_ind) in showed_cells:
                user_field[row_ind][col_ind] = col
    return user_field


def check_all_flags_on_bombs(field, user_field):
    return all(
        user_field[row_ind][col_ind] == 'F' for row_ind, i in enumerate(field) for col_ind, j in
        enumerate(i) if j == 'X')


def make_move(move_string, field, user_field):
    row, col, *flag = move_string.split()
    row, col = int(row) - 1, int(col) - 1
    try:
        cell = field[row][col]
    except IndexError:
        return False
    if user_field[row][col] in ('F', '?'):
        user_field[row][col] = 0
    elif flag:
        flag = flag[0]
        if flag not in ('F', '?'):
            return False
        user_field[row][col] = flag
    elif cell == 'X':
        user_field[row][col] = cell
    elif cell == 0:
        mark_clear_by_near_cells(field, (row, col))
    elif isinstance(cell, int):
        user_field[row][col] = cell
    add_clear_cells_to_user_field(field, user_field)
    return True


def game(level):
    print('row - строка, col - колонка, flag - флажок (F, ?)')
    print('Например: Ход (row col [flag]): F')
    user_field = [[0 for _ in range(level[1])] for _ in range(level[0])]
    print_field(user_field)
    move = input('Ход (row col [flag]): ')
    row, col = map(int, move.split()[:2])
    field = generate_field(level, (row, col))
    user_field = add_clear_cells_to_user_field(field, user_field)
    print_field(user_field)
    move = input('Ход (row col [flag]): ')
    while move:
        move_res = make_move(move, field, user_field)
        print_field(user_field)
        if not move_res:
            print('TRY AGAIN')
        elif check_all_flags_on_bombs(field, user_field):
            print('WIN')
            break
        elif any(j == 'X' for i in user_field for j in i):
            print('GAME OVER')
            break
        move = input('Ход (row col [flag]): ')


def main():
    game_level = input('Введите уровень сложности (EASY, MEDIUM, HARD, CUSTOM): ').upper()
    if game_level == 'EASY':
        game_level = EASY
    elif game_level == 'MEDIUM':
        game_level = MEDIUM
    elif game_level == 'HARD':
        game_level = HARD
    elif game_level == 'CUSTOM':
        game_level = input('Количество строк по горизонтали, по вертикали'
                           ' и количество бомб (10 15 10): ')
        *game_level, mines_count = tuple(map(int, game_level.split()))
        game_level = tuple(game_level)
        BOMBS_COUNT[game_level] = mines_count
    else:
        return print('Попробуйте еще раз')
    game(game_level)


if __name__ == '__main__':
    main()

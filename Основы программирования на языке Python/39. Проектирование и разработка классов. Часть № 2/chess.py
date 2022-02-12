import abc
import typing
from copy import deepcopy
import pickle

WHITE = 1
BLACK = 2


# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    """Доска"""

    def __init__(self):
        self.color = WHITE
        self.field: typing.List[typing.List[typing.Optional[BaseFigure]]] = []
        self.clear_field()
        self.standard_fill_field()

    def clear_field(self):
        self.field = [[None] * 8 for _ in range(8)]

    def standard_fill_field(self):
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def is_under_attack(self, row1, col1):
        res = False
        original_board_color = self.color
        for row, i in enumerate(self):
            for col, j in enumerate(i):
                piece = self[row, col]
                if isinstance(self[row, col], BaseFigure):
                    self.color = piece.color
                if self.can_move(row, col, row1, col1):
                    res = True
        self.color = original_board_color
        return res

    @staticmethod
    def letter_cell2row_col_index(item):
        letter, number = item
        try:
            if len(letter) > 1:
                raise TypeError(f'Expected a character, but string of length {len(letter)} found')
            letter = letter.lower()
            if ord(letter) not in range(ord('a'), ord('z') + 1):
                raise TypeError(f'Letter must be in latin alphabet')
            row, col = int(number) - 1, ord(letter) - ord('a')
        except TypeError:
            row, col = map(int, item)
        return row, col

    @staticmethod
    def check_key(key):
        if isinstance(key, tuple):
            if len(key) != 2:
                raise TypeError('If indices specifies as tuple it should be length 2')
        elif isinstance(key, str):
            if len(key) != 2:
                raise TypeError('If indices specifies as string it should be length 2')
        else:
            return False  # не может справится с проверкой
        return True

    def __getitem__(self, item):
        if not self.check_key(item):
            return self.field[item]
        row, col = self.letter_cell2row_col_index(item)
        return self.field[row][col]

    def __setitem__(self, key, value):
        self.check_key(key)
        row, col = self.letter_cell2row_col_index(key)
        self.field[row][col] = value

    def __len__(self):
        return len(self.field)

    def current_player_color(self):
        return self.color

    def cell(self, row: int, col: int):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self[row, col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self[row, col]
        else:
            return None

    def can_move(self, row, col, row1, col1):
        (row, col), (row1, col1) = map(self.letter_cell2row_col_index, ((row, col), (row1, col1)))
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self[row, col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self[row1, col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self[row1, col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        return True

    def make_base_move(self, row, col, row1, col1):
        (row, col), (row1, col1) = map(self.letter_cell2row_col_index, ((row, col), (row1, col1)))
        piece = self[row, col]
        if isinstance(piece, Rook) or isinstance(piece, King):
            piece.is_already_moved = True
        self[row, col] = None  # Снять фигуру.
        self[row1, col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False"""
        if not self.can_move(row, col, row1, col1):
            return False
        return self.make_base_move(row, col, row1, col1)

    def _castling(self, col):
        if col not in (0, 7):
            return ValueError('Column must be 0 or 7')
        castling_row = 0 if self.color == WHITE else 7
        king_col = [ind for ind, i in enumerate(self.field[castling_row])
                    if isinstance(i, King) and i.color == self.color]
        if not king_col:
            return False
        king_col = king_col[0]
        if not isinstance(self[castling_row, col], Rook):
            return False
        if getattr(self[castling_row, king_col], 'is_already_moved', False):
            return False
        if getattr(self[castling_row, col], 'is_already_moved', False):
            return False
        if (king_col < 2) if col == 0 else (king_col > 5):  # иначе королю некуда прыгать
            return False
        can_move = self.move_piece(castling_row, col,
                                   castling_row, king_col + (-1 if col == 0
                                                             else + 1))  # двигаем ладью
        if not can_move:
            return False
        self.color = opponent(self.color)  # Это же все как один ход
        king_new_row_ind = king_col + (-2 if col == 0 else 2)
        origin_king_move_method = self[castling_row, king_col].can_move
        # патчим, разрешая королю ходить в нужное нам место
        self[castling_row, king_col].can_move = (lambda board, row0, col0, row1, col1: True
                                                 if row1 == castling_row
                                                 and col1 == king_new_row_ind else False)
        origin_king_base_move_method = self[castling_row, king_col].can_base_move
        self[castling_row, king_col].can_base_move = (lambda *args, **kwargs: True)
        can_move = self.move_piece(castling_row, king_col,
                                   castling_row, king_new_row_ind)  # король перепрыгиваеи ладью
        self[castling_row, king_new_row_ind].can_move = origin_king_move_method
        self[castling_row, king_new_row_ind].can_base_move = origin_king_base_move_method
        if not can_move:
            return False
        return True

    def castling0(self):
        """рокировка в левом ряду"""
        return self._castling(0)

    def castling7(self):
        """рокировка в правом ряду"""
        return self._castling(7)

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if not self._can_move_and_promote_pawn(row, col, row1, col1):
            return False
        pawn = self[row, col]
        self[row, col] = None  # снимаем пешку
        if char == 'Q':
            self[row1, col1] = Queen(pawn.get_color())
        elif char == 'R':
            self[row1, col1] = Rook(pawn.get_color())
        elif char == 'B':
            self[row1, col1] = Bishop(pawn.get_color())
        elif char == 'N':
            self[row1, col1] = Knight(pawn.get_color())
        self.color = opponent(self.color)
        return True

    def _can_move_and_promote_pawn(self, row, col, row1, col1):
        piece = self[row, col]
        if not isinstance(piece, Pawn):
            return False
        if not self.can_move(row, col, row1, col1):
            return False
        return True

    def get_piece_positions(self, piece_class, color):
        positions = []
        for row_ind, row in enumerate(self):
            for col_ind, col in enumerate(row):
                piece = self[row_ind, col_ind]
                if isinstance(piece, piece_class):
                    if piece.color == color:
                        positions.append((row_ind, col_ind))
        return positions


class BaseFigure(metaclass=abc.ABCMeta):
    CHAR = None

    def __init__(self, color):
        self.color = color

    def char(self):
        return self.CHAR

    def get_color(self):
        return self.color

    @abc.abstractmethod
    def can_move(self, board, row, col, row1, col1):
        """Логика проверки возможности хода"""

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    @staticmethod
    def can_base_move(row, col, row1, col1):
        """Реализует необязательную вспомогательную базовую логику проверки возможности ходов"""
        return True


class Pawn(BaseFigure):
    """Класс пешки"""
    CHAR = 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # если рядом вражеская пешка пыталась проскочить
        double_moved_pawn_cell = self._is_double_moved_pawn_near(board, row, col)
        if double_moved_pawn_cell and self.can_attack(board, row, col, row1, col1):
            double_moved_pawn = board[double_moved_pawn_cell]
            board[double_moved_pawn_cell] = None  # берем на проходе
            board[row1, col1] = double_moved_pawn  # на самом деле ставим туда,где пешка может съесть

        # ход на 1 клетку
        if row + direction == row1:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board[row + direction, col] is None):
            self.__dict__['is_already_double_moved'] = True
            return True

        return False

    @staticmethod
    def _is_double_moved_pawn_near(board, row, col):
        near_valid = False
        for i in (-1, 1):  # слева и справа
            near_cell = (row, col + i)
            if not correct_coords(*near_cell):
                continue
            if getattr(board[near_cell], 'is_already_double_moved', False):
                near_valid = True
                break
        if not near_valid:
            return False
        return near_cell

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if self.color == WHITE else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Rook(BaseFigure):
    """Класс ладьи"""
    CHAR = 'R'

    def can_move(self, board, row, col, row1, col1):
        if self.can_base_move(row, col, row1, col1):
            return False
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1 + step, step):
            # Если на пути по горизонтали есть фигура
            piece = board[r, col]
            if not (piece is None):
                return self.color != piece.color and (r == row1 and col == col1)  # учитываем цвет
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1 + step, step):
            # Если на пути по вертикали есть фигура
            piece = board[row, c]
            if not (piece is None):
                return self.color != piece.color and (row == row1 and c == col1)  # учитываем цвет
        return True

    @staticmethod
    def can_base_move(row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if row != row1 and col != col1:
            return False
        return True


class Knight(BaseFigure):
    """Класс коня"""
    CHAR = 'N'

    def can_move(self, board, row, col, row1, col1):
        if not self.can_base_move(row, col, row1, col1):
            return False
        dest_cell = board[row1, col1]
        if dest_cell is not None:
            return opponent(dest_cell.color) == self.color
        return True

    @staticmethod
    def can_base_move(row, col, row1, col1):
        delta_row = abs(row - row1)
        delta_col = abs(col - col1)
        return max(delta_row, delta_col) == 2 and min(delta_row, delta_col) == 1


class King(BaseFigure):
    """Класс короля"""
    CHAR = 'K'

    def can_move(self, board, row, col, row1, col1):
        if not self.can_base_move(row, col, row1, col1):
            return False
        dest_cell = board[row1, col1]
        if dest_cell is not None:
            return opponent(dest_cell.color) == self.color
        return True

    @staticmethod
    def can_base_move(row, col, row1, col1):
        delta_row = abs(row - row1)
        delta_col = abs(col - col1)
        return delta_row in (0, 1) and delta_col in (0, 1)


class Queen(BaseFigure):
    """Класс ферзя."""
    CHAR = 'Q'

    def can_move(self, board, row, col, row1, col1):
        if not self.can_base_move(row, col, row1, col1):
            return False
        # для диагоналей
        is_like_bishop = Bishop(self.color).can_move(board, row, col, row1, col1)
        # для перпиндикуляров
        is_like_rook = Rook(self.color).can_move(board, row, col, row1, col1)
        return is_like_bishop or is_like_rook

    @staticmethod
    def can_base_move(row, col, row1, col1):
        delta_row = abs(row - row1)
        delta_col = abs(col - col1)
        return delta_row == delta_col or row == row1 or col == col1


class Bishop(BaseFigure):
    """Класс слона"""
    CHAR = 'B'

    def can_move(self, board, row, col, row1, col1):
        if not self.can_base_move(row, col, row1, col1):
            return False
        step_col = -1 if (col1 - col) < 0 else 1
        step_row = -1 if (row1 - row) < 0 else 1
        x, y = row, col
        while not (x, y) == (row1, col1):
            x, y = x + step_row, y + step_col
            piece = board[x, y]
            if not correct_coords(x, y):
                break
            if piece is not None:
                return self.color != piece.color and (x == row1 and y == col1)
        return True

    @staticmethod
    def can_base_move(row, col, row1, col1):
        delta_row = abs(row - row1)
        delta_col = abs(col - col1)
        return delta_row == delta_col


def print_board_colored(board, color=WHITE):  # Распечатать доску в текстовом виде
    bg_color_rgb = (lambda r, g, b: f"\033[48;2;{r};{g};{b}m")
    text_color_rgb = (lambda r, g, b: f'\033[38;2;{r};{g};{b}m')
    reset_color = (lambda: '\033[0m')
    cell_width = 7
    left_border_buffer = 5
    num_progression_args = (8,)
    num_regression_args = (7, -1, -1)
    if color == BLACK:
        num_progression_args, num_regression_args = num_regression_args, num_progression_args
    print(end=' ' * left_border_buffer)
    for col in range(*num_progression_args):
        print(chr(ord('a') + col).upper().center(cell_width), end='')
    print()
    cur_cell_bg, next_cell_bg = bg_color_rgb(240, 217, 181), bg_color_rgb(181, 136, 99)
    for row in range(*num_regression_args):
        print(end=' ' * left_border_buffer)
        for i in range(*num_progression_args):
            cur_cell_bg, next_cell_bg = next_cell_bg, cur_cell_bg
            print(f"{cur_cell_bg}{''.center(cell_width)}{reset_color()}", end='')
        print()
        cur_cell_bg, next_cell_bg = next_cell_bg, cur_cell_bg
        print(str(row + 1).center(left_border_buffer), end='')
        for col in range(*num_progression_args):
            cell = board.cell(row, col)
            if cell[0] == 'b':
                cell_color = text_color_rgb(0, 0, 0)
            else:
                cell_color = text_color_rgb(255, 255, 255)
            cell = f"{cur_cell_bg}{cell_color} {cell[1].center(cell_width - 2)}{cur_cell_bg}"
            print(cell, sep='', end=' ')
            cur_cell_bg, next_cell_bg = next_cell_bg, cur_cell_bg
        print(reset_color(), str(row + 1).center(left_border_buffer), sep='')
        print(end=' ' * left_border_buffer)
        for i in range(*num_progression_args):
            print(f"{cur_cell_bg}{''.center(cell_width)}{reset_color()}", end='')
            cur_cell_bg, next_cell_bg = next_cell_bg, cur_cell_bg
        print()
    print(end=' ' * left_border_buffer)
    for col in range(*num_progression_args):
        print(chr(ord('a') + col).upper().center(cell_width), end='')
    print(reset_color())


def print_board_borders(board, color=WHITE):  # Распечатать доску в текстовом виде
    num_progression_args = (8,)
    num_regression_args = (7, -1, -1)
    if color == BLACK:
        num_progression_args, num_regression_args = num_regression_args, num_progression_args
    print(end='        ')
    for col in range(*num_progression_args):
        print(chr(ord('a') + col).upper(), end='    ')
    print()
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(*num_regression_args):
        print(' ', row + 1, end='  ')
        for col in range(*num_progression_args):
            print('|', board.cell(row, col), end=' ')
        print('|', row + 1, sep='  ')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(*num_progression_args):
        print(chr(ord('a') + col).upper(), end='    ')
    print('\n')


def get_print_board_func(*, colored=False):
    return print_board_colored if colored else print_board_borders


class InvalidCommandError(ValueError):
    ...


class Game:

    def __init__(self, *, colored=False):
        self.board = Board()
        self._print_board = get_print_board_func(colored=colored)
        self._board_backup = None

    def print_board(self):
        self._print_board(self.board, self.board.color)

    @property
    def num_buffer_lines(self):
        from os import get_terminal_size
        try:
            num_buffer_lines = get_terminal_size().lines
        except OSError:
            num_buffer_lines = 80
        return num_buffer_lines

    @staticmethod
    def get_possible_commands_help():
        possible_commands_help = '''        exit                               -- выход
        move <cell> <cell1>                -- ход из клетки cell
                                              в клетку cell1, e.g. move a2 A4
        castlingA                          -- рокировка в ряду A 
        castlingB                          -- рокировка в ряду B 
        save                               -- сохранить игру'''
        return possible_commands_help

    def solve_castling(self, command):
        """Парсит command. Если возможна рокировка, то делает и возвращает True"""
        move_type = command.strip()
        col = move_type[-1]
        move_type = move_type[:-1] + ('0' if move_type[-1] == 'A' else '7')
        castling_method = getattr(self.board, move_type, lambda: False)
        movement_result = castling_method()
        if not movement_result:
            raise InvalidCommandError(f'Рокировка в ряду {col} не удалась!')
        return movement_result

    def parse_command(self, command):
        """Если возможно распарсить, возвращает подготовленные значения.
         Иначе поднимает ValueError"""
        try:
            move_type, *args = command.split()
            (row, col), (row1, col1) = args
            (row, col), (row1, col1) = map(self.board.letter_cell2row_col_index,
                                           ((row, col), (row1, col1)))
        except ValueError:
            raise InvalidCommandError('Неверное значение. Попробуйте еще раз.')
        return row, col, row1, col1

    def solve_pawn_promotion(self, row, col, row1, col1):
        """Пытается сделать превращение пешки. Если не получается, то поднимает ValueError"""
        possible_promote_chars = ('Q', 'R', 'B', 'N')
        possible_promote_chars = str(possible_promote_chars).replace("'", '')
        promote_char = input(
            f"На какую фигуру заменить пешку {possible_promote_chars}: ")
        if promote_char not in possible_promote_chars:
            raise InvalidCommandError('Неверное значение. Попробуйте еще раз.')
        movement_result = self.board.move_and_promote_pawn(row, col, row1, col1, promote_char)
        if not movement_result:
            raise InvalidCommandError('Превращение пешки не удалось!')
        return movement_result

    def solve_command(self, command):
        if 'save' in command:
            self.save()
            movement_result = True
        elif 'castling' in command:
            movement_result = self.solve_castling(command)
        else:
            row, col, row1, col1 = self.parse_command(command)
            if (isinstance(self.board[row, col], Pawn) and
                    row1 == (7 if self.board.color == WHITE else 0)):
                movement_result = self.solve_pawn_promotion(row, col, row1, col1)
            else:
                movement_result = self.board.move_piece(row, col, row1, col1)
        return movement_result

    def is_king_under_attack(self, color):
        king_position = self.board.get_piece_positions(King, color)
        if len(king_position) == 1:
            king_position = king_position[0]
        else:
            return False  # Если нет королей (?)
        is_king_under_attack = self.board.is_under_attack(*king_position)
        return is_king_under_attack

    def solve_check(self):
        """
        Обработка шаха. Если шах — возвращает True
        """
        if self._board_backup is None:
            if self.is_king_under_attack(self.board.color):
                self._board_backup = deepcopy(self.board)
                print('Король под угрозой!')
                return True
        elif self.is_king_under_attack(self._board_backup.color):
            self.board = deepcopy(self._board_backup)
            print('Вы не ушли от угрозы королю. Попробуйте еще раз')
            return True
        else:
            self._board_backup = None
        return False

    def is_not_end(self):
        if self.solve_check():
            pass
        return True

    def main_game_cycle(self):
        """Цикл ввода команд игроков"""
        print('\n' * self.num_buffer_lines)
        while self.is_not_end():
            # Выводим положение фигур на доске
            self.print_board()
            # Подсказка по командам
            print('Команды:')
            print(self.get_possible_commands_help())
            # Выводим приглашение игроку нужного цвета
            if self.board.current_player_color() == WHITE:
                print('Ход белых:')
            else:
                print('Ход чёрных:')
            command = input()
            if 'exit' in command:
                break
            try:
                movement_result = self.solve_command(command)
                print('\n' * self.num_buffer_lines)
            except InvalidCommandError as e:
                print('\n' * self.num_buffer_lines)
                print(e)
                continue
            if movement_result:
                print('Ход успешен')
            else:
                print('Неудача! Попробуйте другой ход!')

    def save(self):
        import datetime
        with open(datetime.datetime.now().strftime('%d-%m-%y_%H_%M_%S') + '.pkl', 'wb') as fp:
            pickle.dump(self, fp)

    @classmethod
    def from_save_file(cls, filename):
        with open(filename, 'rb') as fp:
            return pickle.load(fp)

    def run(self):
        self.main_game_cycle()


def main():
    from sys import argv
    if len(argv) == 2:
        game = Game.from_save_file(argv[1])
    else:
        game = Game(colored=True)
    game.run()


if __name__ == '__main__':
    main()

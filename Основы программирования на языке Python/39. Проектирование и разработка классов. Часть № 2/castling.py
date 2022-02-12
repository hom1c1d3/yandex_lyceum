import abc
import typing

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
        for row in range(8):
            self.field.append([None] * 8)
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

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        if isinstance(piece, Rook) or isinstance(piece, King):
            piece.is_already_moved = True
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True

    def _castling(self, col):
        if col not in (0, 7):
            return ValueError('Column must be 0 or 7')
        castling_row = 0 if self.color == WHITE else 7
        king_col = [ind for ind, i in enumerate(self.field[castling_row])
                    if isinstance(i, King) and i.color == self.color]
        if not king_col:
            return False
        king_col = king_col[0]
        if not isinstance(self.field[castling_row][col], Rook):
            return False
        if getattr(self.field[castling_row][king_col], 'is_already_moved', False):
            return False
        if getattr(self.field[castling_row][col], 'is_already_moved', False):
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
        origin_king_move_method = self.field[castling_row][king_col].can_move
        # патчим, разрешая королю ходить в нужное нам место
        self.field[castling_row][king_col].can_move = (lambda board, row0, col0, row1, col1: True
                                                       if row1 == castling_row
                                                       and col1 == king_new_row_ind else False)
        can_move = self.move_piece(castling_row, king_col,
                                   castling_row, king_new_row_ind)  # король перепрыгиваеи ладью
        self.field[castling_row][king_new_row_ind].can_move = origin_king_move_method
        if not can_move:
            return False
        return True

    def castling0(self):
        """рокировка в левом ряду"""
        return self._castling(0)

    def castling7(self):
        """рокировка в правом ряду"""
        return self._castling(7)


class ABCMetaFigure(abc.ABCMeta):

    def __new__(mcs, class_name, parents, attributes):
        try:
            char = attributes['CHAR']
            if parents:
                if not (isinstance(char, str) and char.isupper() and len(char) == 1):
                    raise ValueError
        except KeyError:
            raise ValueError
        return super().__new__(mcs, class_name, parents, attributes)


class BaseFigure(metaclass=ABCMetaFigure):
    CHAR = None

    def __init__(self, color):
        self.color = color

    def char(self):
        return self.CHAR

    def get_color(self):
        return self.color

    @abc.abstractmethod
    def can_move(self, board, row, col, row1, col1):
        ...

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Rook(BaseFigure):
    CHAR = 'R'

    def can_move(self, board, row, col, row1, col1):
        if (not correct_coords(row1, col1) or
                not self.can_base_move(row, col, row1, col1) or
                (row == row1 and col == col1)):
            return False
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1 + step, step):
            # Если на пути по горизонтали есть фигура
            piece = board.get_piece(r, col)
            if not (piece is None):
                return self.color != piece.color and (r == row1 and col == col1)  # учитываем цвет
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1 + step, step):
            # Если на пути по вертикали есть фигура
            piece = board.get_piece(row, c)
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


class Pawn(BaseFigure):
    CHAR = 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Knight(BaseFigure):
    """Класс коня"""
    CHAR = 'N'

    def can_move(self, board, row, col, row1, col1):
        if (not correct_coords(row1, col1) or
                not self.can_base_move(row, col, row1, col1) or
                (row == row1 and col == col1)):
            return False
        dest_cell = board.field[row1][col1]
        if dest_cell is not None:
            return opponent(dest_cell.color) == self.color
        return True

    @staticmethod
    def can_base_move(row, col, row1, col1):
        if not correct_coords(row, col):
            return False
        delta_row = abs(row - row1)
        delta_col = abs(col - col1)
        return max(delta_row, delta_col) == 2 and min(delta_row, delta_col) == 1


class King(BaseFigure):
    """Класс короля"""
    CHAR = 'K'

    def can_move(self, board, row, col, row1, col1):
        if (not correct_coords(row1, col1) or
                not self.can_base_move(row, col, row1, col1) or
                (row == row1 and col == col1)):
            return False
        dest_cell = board.field[row1][col1]
        if dest_cell is not None:
            return opponent(dest_cell.color) == self.color
        return True

    @staticmethod
    def can_base_move(row, col, row1, col1):
        if not correct_coords(row, col):
            return False
        delta_row = abs(row - row1)
        delta_col = abs(col - col1)
        return delta_row in (0, 1) and delta_col in (0, 1)


class Queen(BaseFigure):
    """Класс ферзя."""
    CHAR = 'Q'

    def can_move(self, board, row, col, row1, col1):
        if (not correct_coords(row1, col1) or
                not self.can_base_move(row, col, row1, col1) or
                (row == row1 and col == col1)):
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
    """Класс слона. Пока что заглушка, которая может ходить в любую клетку."""
    CHAR = 'B'

    def can_move(self, board, row, col, row1, col1):
        if (not correct_coords(row1, col1) or
                not self.can_base_move(row, col, row1, col1) or
                (row == row1 and col == col1)):
            return False
        step_col = -1 if (col1 - col) < 0 else 1
        step_row = -1 if (row1 - row) < 0 else 1
        x, y = row, col
        while not (x, y) == (row1, col1):
            x, y = x + step_row, y + step_col
            piece = board.get_piece(x, y)
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


def check():
    board = Board()
    board.field = [([None] * 8) for i in range(8)]
    board.field[0][0] = Knight(WHITE)
    board.field[0][4] = King(WHITE)
    board.field[0][7] = Bishop(WHITE)

    board.field[7][0] = Queen(BLACK)
    board.field[7][4] = King(BLACK)
    board.field[7][7] = Pawn(BLACK)

    board.field[1][4] = Pawn(WHITE)

    print('before:')
    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()
    print()

    print("Попытки рокировок короля не с ладьёй")
    print(board.castling0())
    print(board.castling7())

    print('3 turns after:')
    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()
    print()

    board.move_piece(1, 4, 3, 4)
    print(board.castling0())
    print(board.castling7())

    print('1 turns after:')
    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()


def print_board(board):  # Распечатать доску в текстовом виде (см. скриншот)
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row, end='  ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col, end='    ')
    print()


def main():
    # Создаём шахматную доску
    board = Board()
    # Цикл ввода команд игроков
    while True:
        # Выводим положение фигур на доске
        print_board(board)
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    move <row> <col> <row1> <row1>     -- ход из клетки (row, col)')
        print('                                          в клетку (row1, col1)')
        # Выводим приглашение игроку нужного цвета
        if board.current_player_color() == WHITE:
            print('Ход белых:')
        else:
            print('Ход чёрных:')
        command = input()
        if command == 'exit':
            break
        move_type, row, col, row1, col1 = command.split()
        row, col, row1, col1 = int(row), int(col), int(row1), int(col1)
        if board.move_piece(row, col, row1, col1):
            print('Ход успешен')
        else:
            print('Координаты некорректы! Попробуйте другой ход!')


if __name__ == '__main__':
    main()

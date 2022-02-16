WHITE = 1
BLACK = 2


# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


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


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
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
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True


class BaseFigure:
    CHAR = None

    def __init__(self, color):
        self.color = color

    def char(self):
        return self.CHAR

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        return NotImplemented  # Заглушка

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

    def can_base_move(self, row, col, row1, col1):
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
    """Класс коня. Пока что заглушка, которая может ходить в любую клетку."""
    CHAR = 'N'

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка


class King(BaseFigure):
    """Класс короля. Пока что заглушка, которая может ходить в любую клетку."""
    CHAR = 'K'

    def can_move(self, board, row, col, row1, col1):
        return True  # Заглушка


class Queen(BaseFigure):
    """Класс ферзя. Пока что заглушка, которая может ходить в любую клетку."""
    CHAR = 'Q'

    def can_move(self, board, row, col, row1, col1):
        if (not correct_coords(row1, col1) or
                not self.can_base_move(row, col, row1, col1) or
                (row == row1 and col == col1)):
            return False
        # для диагоналей
        is_like_bishop = Bishop.can_move(Bishop(self.color), board, row, col, row1, col1)
        # для перпиндикуляров
        is_like_rook = Rook.can_move(Rook(self.color), board, row, col, row1, col1)
        return is_like_bishop or is_like_rook

    def can_base_move(self, row, col, row1, col1):
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
            if piece is not None:
                return self.color != piece.color and (x == row1 and y == col1)
            if not correct_coords(x, y):
                break
        return True

    def can_base_move(self, row, col, row1, col1):
        delta_row = abs(row - row1)
        delta_col = abs(col - col1)
        return delta_row == delta_col


def check():
    board = Board()
    board.field = [([None] * 8) for i in range(8)]
    queen = Queen(WHITE)
    r0, c0 = 6, 3
    board.field[r0][c0] = queen

    board.field[7][3] = Knight(BLACK)
    board.field[4][3] = Knight(WHITE)

    board.field[7][4] = Rook(BLACK)
    board.field[4][1] = Rook(WHITE)

    board.field[6][5] = Bishop(BLACK)
    board.field[6][1] = Bishop(WHITE)

    board.field[5][4] = Pawn(BLACK)
    board.field[7][2] = Pawn(WHITE)

    for row in range(7, -1, -1):
        for col in range(8):
            if queen.can_move(board, r0, c0, row, col):
                print('x', end='')
            else:
                cell = board.cell(row, col)[1]
                cell = cell if cell != ' ' else '-'
                print(cell, end='')
        print()
    print()


if __name__ == '__main__':
    check()

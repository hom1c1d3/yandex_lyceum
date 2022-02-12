WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class BaseFigure:
    CHAR = None

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return self.CHAR

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        return NotImplemented  # Заглушка


class Knight(BaseFigure):
    CHAR = 'N'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        delta_row = abs(self.row - row)
        delta_col = abs(self.col - col)
        return max(delta_row, delta_col) == 2 and min(delta_row, delta_col) == 1


class Bishop(BaseFigure):
    CHAR = 'B'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        delta_row = abs(self.row - row)
        delta_col = abs(self.col - col)
        return delta_row == delta_col


class Queen(BaseFigure):
    CHAR = 'Q'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        delta_row = abs(self.row - row)
        delta_col = abs(self.col - col)
        is_like_bishop = delta_row == delta_col
        return is_like_bishop or self.row == row or self.col == col


class Rook(BaseFigure):
    CHAR = 'R'

    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = [[None for _ in range(8)] for _ in range(8)]

    def is_under_attack(self, row, col, color):
        for i in self.field:
            for j in i:
                if j is None:
                    continue
                if j.color != color:
                    continue
                if j.can_move(row, col):
                    return True

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

    def move_piece(self, row, col, row1, col1):
        """Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернет True.
        Если нет --- вернет False"""

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True


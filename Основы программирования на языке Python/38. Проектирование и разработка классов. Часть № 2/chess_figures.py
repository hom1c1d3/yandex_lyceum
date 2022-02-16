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


def main():
    WHITE = 1
    BLACK = 2

    row0 = 7
    col0 = 3
    queen = Queen(row0, col0, BLACK)

    print('white' if queen.get_color() == WHITE else 'black')
    for row in range(8, -2, -1):
        for col in range(-1, 9):
            if row == row0 and col == col0:
                print(queen.char(), end='')
            elif queen.can_move(row, col):
                print('x', end='')
            else:
                print('-', end='')
        print()


if __name__ == '__main__':
    main()

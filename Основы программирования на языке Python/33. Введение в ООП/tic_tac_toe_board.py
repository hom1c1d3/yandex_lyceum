class TicTacToeBoard:

    def __init__(self):
        self._size = 3
        self._field = [['-' for _ in range(self._size)] for _ in range(self._size)]
        self._moves = 0
        self._is_game_over = False

    def new_game(self):
        self.__init__()

    def get_field(self):
        return self._field

    def check_field(self):
        for row in self._field:
            row = list(set(row))
            if len(row) == 1 and row[0] != '-':
                return row[0]
        for col in zip(*self._field):
            col = list(set(col))
            if len(col) == 1 and col[0] != '-':
                return col[0]
        diagonal1 = {self._field[i][i] for i in range(self._size)}
        diagonal2 = {self._field[i][-(i + 1)] for i in range(self._size)}
        for i in (diagonal1, diagonal2):
            if len(i) == 1 and i != {'-', }:
                return list(i)[0]
        tie_field = [i for i in self._field if i != '-']
        return 'D' if len(tie_field) == self._size ** 2 else None

    def make_move(self, row, col):
        row, col = row - 1, col - 1
        if self._is_game_over:
            return 'Игра уже завершена'
        if self._field[row][col] != '-':
            return f'Клетка {row + 1}, {col + 1} уже занята'
        move = ('X', '0')[self._moves % 2]
        self._moves += 1
        self._field[row][col] = move
        check = self.check_field()
        self._is_game_over = True
        if check == 'X':
            return 'Победил игрок X'
        elif check == '0':
            return 'Победил игрок 0'
        elif check == 'D':
            return 'Ничья'
        else:
            self._is_game_over = False
            return 'Продолжаем играть'

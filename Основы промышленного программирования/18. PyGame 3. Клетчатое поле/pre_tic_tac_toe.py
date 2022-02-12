import pygame


class TicTacToePerks:
    Cross = 1
    Circle = 2


class Board:

    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[(0, 'black')] * width for _ in range(height)]
        # дефолтные значения
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.cur_move = TicTacToePerks.Cross
        self.colors = [pygame.Color('blue'), pygame.Color('red')]
        self.cur_color = self.colors[0]

    def render(self, screen):
        # color = 0 if self.width % 2 else 1
        color = 1
        for row, row_v in enumerate(self.board):
            col = 0
            for col, col_v in enumerate(row_v):
                col_v, col_clr = col_v
                clr = 'white' if color else 'black'
                rect_width = 1
                pygame.draw.rect(screen, pygame.Color(clr),
                                 (self.left + col * self.cell_size,
                                  self.top + row * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 rect_width)
                self.draw_perk(screen, (row, col), col_v, col_clr)
                # color = not color
                color = color
            if col % 2 != 0:
                # color = not color
                color = color

    def set_view(self, left, top, cell_size):
        self.left, self.top, self.cell_size = left, top, cell_size

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.left < x < self.left + (self.width * self.cell_size):
            cell_x = (x - self.left) // self.cell_size
        else:
            return
        if self.top < y < self.top + (self.height * self.cell_size):
            cell_y = (y - self.top) // self.cell_size
        else:
            return
        return cell_x, cell_y

    def draw_perk(self, screen, cell_pos, perk, color):
        r, c = cell_pos
        x, y = self.left + (c * self.cell_size), self.top + (r * self.cell_size)
        d = 4
        x, y = x + d, y + d
        w, h = self.cell_size - d * 2, self.cell_size - d * 2
        if perk == TicTacToePerks.Cross:
            self.draw_cross(screen, color, x, y, w, h)
        if perk == TicTacToePerks.Circle:
            self.draw_circle(screen, color, x, y, w, h)

    def draw_cross(self, screen, color, x, y, width, height):
        pygame.draw.line(screen, color, (x, y), (x + width, y + height), 2)
        pygame.draw.line(screen, color, (x, y + height), (x + width, y), 2)

    def draw_circle(self, screen, color, x, y, width, height):
        pygame.draw.ellipse(screen, color, (x, y, width, height), 2)

    def on_click(self, cell_pos):
        if cell_pos is None:
            return
        row, col = cell_pos[::-1]
        if self.board[row][col] != (0, 'black'):
            return
        self.board[row][col] = self.cur_move, self.cur_color
        self.next_move()

    def next_move(self):
        if self.cur_move == TicTacToePerks.Cross:
            self.cur_move = TicTacToePerks.Circle
        else:
            self.cur_move = TicTacToePerks.Cross
        self.cur_color = self.colors[(self.colors.index(self.cur_color) + 1) % len(self.colors)]

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


def main():
    pygame.init()
    size = width, height = 540, 390
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Пра-пра-пра-крестики-нолики')
    board = Board(10, 7)
    board.set_view(20, 20, 50)
    running = True
    while running:
        # цикл приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        # отрисовка и изменения св-в объекта
        board.render(screen)
        pygame.display.flip()  # обновление экрана
    pygame.quit()


if __name__ == '__main__':
    main()